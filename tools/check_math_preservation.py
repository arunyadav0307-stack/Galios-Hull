#!/usr/bin/env python3
"""Verify that display mathematics is preserved between the source paper and
the revised manuscript.

Compares multisets of display-math contents after normalization:
  - \\[...\\], $$...$$, and equation-environment contents are all treated
    as displays;
  - one outer \\boxed{...} wrapper is stripped (boxes became numbered eqs);
  - \\label{...} lines inside equations are removed;
  - whitespace is collapsed.

Known intentional differences (allowlisted, each documented):
  REMOVED (abstract): the two abstract display blocks of the source paper
    (the revised abstract is prose-only, reference style). Their mathematics
    appears identically in the body (pairing; joint enumerator + matrix).
  REMOVED (dedup): two displays the source paper states twice: the
    Section-11 compatibility condition (now cited as Equation (6)) and the
    Section-2 prose decomposition display (now Equation (2) in Proposition 1).
  ADDED: new displays in the two worked examples (Section 5.1), whose numbers
    come from the source validation captures (see CONSISTENCY_CHECK.md).

Exit 0 iff old-minus-new == REMOVED and new-minus-old == ADDED.
"""
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OLD = Path("/tmp/src/Galios-Hull-kGalois-Phase10F/manuscript/main.tex")
NEW = ROOT / "manuscript" / "main.tex"

# Fallback: allow override via argv for reproducibility outside this sandbox.
if len(sys.argv) > 1:
    OLD = Path(sys.argv[1])
if len(sys.argv) > 2:
    NEW = Path(sys.argv[2])


def strip_comments(text: str) -> str:
    out = []
    for line in text.splitlines():
        buf = []
        j = 0
        while j < len(line):
            if line[j] == "%" and (j == 0 or line[j - 1] != "\\"):
                break
            buf.append(line[j])
            j += 1
        out.append("".join(buf))
    return "\n".join(out)


def extract_displays(text: str) -> list[str]:
    text = strip_comments(text)
    # keep only the document body
    m = re.search(r"\\begin\{document\}(.*)\\end\{document\}", text, re.DOTALL)
    body = m.group(1) if m else text
    found: list[str] = []
    # equation environments (record inner content, drop \label)
    for mm in re.finditer(r"\\begin\{equation\*?\}(.*?)\\end\{equation\*?\}",
                          body, re.DOTALL):
        inner = re.sub(r"\\label\{[^}]*\}", "", mm.group(1))
        found.append(inner)
    # \[ ... \] (remove the equation spans first to avoid double counting)
    rest = re.sub(r"\\begin\{equation\*?\}.*?\\end\{equation\*?\}", "",
                  body, flags=re.DOTALL)
    for mm in re.finditer(r"\\\[(.*?)\\\]", rest, re.DOTALL):
        found.append(mm.group(1))
    # $$ ... $$ (none expected, but cover it)
    rest2 = re.sub(r"\\\[.*?\\\]", "", rest, flags=re.DOTALL)
    for mm in re.finditer(r"\$\$(.*?)\$\$", rest2, re.DOTALL):
        found.append(mm.group(1))
    return [normalize(d) for d in found]


def normalize(d: str) -> str:
    d = d.strip()
    # strip one outer \boxed{...} wrapper
    m = re.fullmatch(r"\\boxed\{(.*)\}", d, re.DOTALL)
    if m:
        d = m.group(1).strip()
    # collapse all whitespace runs
    d = re.sub(r"\s+", " ", d)
    return d


def main() -> int:
    old_displays = extract_displays(OLD.read_text(encoding="utf-8"))
    new_displays = extract_displays(NEW.read_text(encoding="utf-8"))
    old_c: Counter = Counter(old_displays)
    new_c: Counter = Counter(new_displays)

    removed = list((old_c - new_c).elements())
    added = list((new_c - old_c).elements())

    print(f"source displays: {len(old_displays)} "
          f"({len(old_c)} distinct)")
    print(f"revised displays: {len(new_displays)} "
          f"({len(new_c)} distinct)")
    print(f"removed: {len(removed)}, added: {len(added)}")

    # ---- expected removals: 2 abstract blocks + 2 dedups ----
    expected_removed = Counter([
        normalize(r"\langle x,y\rangle_{s,k}=\sum_i x_i y_i^{p^k}"),
        normalize(r"""\Epoly(u,z)=\prod_s\prod_{O\in\Os}\operatorname{tr}\bigl(T_{w_O}(u,z)^{a_O}\bigr),
            \qquad
            T_w(u,z)=\begin{pmatrix}u^w&1\\u^wz^w&1\end{pmatrix}."""),
        normalize(r"\lambda_s^{1+p^{d_s-k}}=1."),
        normalize(r"\A\cong \prod_{s=1}^{N}K_s."),
    ])

    ok = True
    if Counter(removed) != expected_removed:
        print("---- removed displays (must equal the allowlisted set) ----")
        for d in removed:
            print("  REMOVED:", d[:150])
        print("---- expected ----")
        for d in expected_removed:
            print("  EXPECTED:", d[:150])
        ok = False
    else:
        print("removed displays: exactly the allowlisted set (expected)")

    # ---- expected additions: worked-example displays + none else ----
    # Every added display must contain only example arithmetic already
    # justified in CONSISTENCY_CHECK.md; here we just list them for review
    # and require the count to match the known new displays.
    print("---- added displays (must all be in Section 5.1 examples) ----")
    for d in added:
        print("  ADDED:", d[:160])
    # the two examples introduce exactly 5 new displays:
    #  Ex1: factorization; trace product expansion; ring hull polynomial.
    #  Ex2: hull polynomial; joint histogram.
    if len(added) != 5:
        print(f"ERROR: expected exactly 5 added example displays, "
              f"found {len(added)}")
        ok = False
    else:
        # spot-check fingerprints of the five known displays
        fingerprints = [
            "x^5-1=(x+1)(x^2+ax+1)(x^2+(a+1)x+1)",
            "(u+1)(1+u^4+2u^2z^2)=1+u+u^4+u^5+2u^2z^2+2u^3z^2",
            "(4+4z^2)^4=256+1024z^2+1536z^4+1024z^6+256z^8",
            "2P_{6,1}(z)=2(2+30z+30z^2+2z^3)=4+60z+60z^2+4z^3",
            "(7,0):1",
        ]
        joined = " ".join(added)
        for fp in fingerprints:
            if fp not in joined:
                print(f"ERROR: added-display fingerprint missing: {fp[:60]}")
                ok = False
        if ok:
            print("added displays: exactly the 5 verified example displays")

    print("RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
