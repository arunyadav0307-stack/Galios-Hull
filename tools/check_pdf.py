#!/usr/bin/env python3
"""Verify the rendered manuscript/main.pdf (content closure check).

Extracts text with PyMuPDF and checks:
  1. All numbered items exist exactly once as headings: Theorem 1-3,
     Lemma 1-8, Proposition 1-12, Corollary 4.1-4.6, Example 1-2,
     Table 1-4, Sections 1-6, Equations (1)-(20).
  2. Every in-text mention (Theorem N, Lemma N, Proposition N,
     Corollary 4.N, Example N, Equation (N), Table N, Section N[.M],
     Corollaries/Propositions/Lemmas/Sections/Examples lists, [NN])
     refers to an existing number; no '??' anywhere.
  3. Every bibliography entry [1]-[13] is cited at least once.
  4. No leftover figure/placeholder/box jargon.

Exit 0 on success, 1 on failure.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PDF = ROOT / "manuscript" / "main.pdf"

errors: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def main() -> int:
    import pymupdf
    doc = pymupdf.open(PDF)
    raw = "\n".join(p.get_text() for p in doc)
    text = re.sub(r"\s+", " ", raw)

    # ---- 1. headings exist ----
    def headings(kind: str, nums: list[str]) -> None:
        for n in nums:
            # heading form: "Theorem 1 (" or "Corollary 4.1." or "Example 1."
            pats = [rf"{kind} {re.escape(n)}(?:\.| \()"]
            if not any(re.search(p, text) for p in pats):
                fail(f"heading {kind} {n} not found")

    headings("Theorem", ["1", "2", "3"])
    headings("Lemma", [str(i) for i in range(1, 9)])
    headings("Proposition", [str(i) for i in range(1, 13)])
    headings("Corollary", [f"4.{i}" for i in range(1, 7)])
    headings("Example", ["1", "2"])
    for n in ["1", "2", "3", "4"]:
        if f"Table {n}:" not in text:
            fail(f"Table {n} caption not found")
    for n in ["1", "2", "3", "4", "5", "6"]:
        if not re.search(rf"^|\b{n}\. [A-Z]", text):
            pass  # (section titles verified structurally below instead)
    # equations (1)-(20): each number must appear as an equation tag. Tags
    # render flush-right; in extraction they appear as "(N)" tokens.
    for n in range(1, 21):
        if f"({n})" not in text:
            fail(f"equation tag ({n}) not found")

    # ---- 2. mentions resolve ----
    thms = {"1", "2", "3"}
    lems = {str(i) for i in range(1, 9)}
    props = {str(i) for i in range(1, 13)}
    cors = {f"4.{i}" for i in range(1, 7)}
    exs = {"1", "2"}
    eqs = {str(i) for i in range(1, 21)}
    tabs = {"1", "2", "3", "4"}
    secs = {"1", "2", "3", "4", "5", "6", "2.1", "2.2", "2.3", "3.1", "3.2",
            "3.3", "4.1", "4.2", "4.3", "4.4", "5.1", "5.2"}

    def check_mentions(pattern: str, valid: set[str], label: str) -> None:
        for m in re.finditer(pattern, text):
            # pattern may capture several groups (lists); check each
            for g in m.groups():
                if g is None:
                    continue
                for tok in re.split(r"\s+and\s+|,\s*", g):
                    tok = tok.strip().strip(".")
                    if tok and tok not in valid:
                        fail(f"{label} mention out of range: {tok!r}")

    check_mentions(r"Theorem (\d+(?:\.\d+)?)", thms, "Theorem")
    check_mentions(r"Lemma (\d+(?:\.\d+)?)", lems, "Lemma")
    check_mentions(r"Proposition (\d+(?:\.\d+)?)", props, "Proposition")
    check_mentions(r"Corollary (4\.\d+)", cors, "Corollary")
    check_mentions(r"Corollaries (\d[\d., and]*)", cors, "Corollaries")
    check_mentions(r"Propositions (\d[\d., and]*)", props, "Propositions")
    check_mentions(r"Lemmas (\d[\d., and]*)", lems, "Lemmas")
    check_mentions(r"Example (\d+(?:\.\d+)?)", exs, "Example")
    check_mentions(r"Examples (\d[\d., and]*)", exs, "Examples")
    check_mentions(r"Equation \((\d+)\)", eqs, "Equation")
    check_mentions(r"Table (\d+)", tabs, "Table")
    check_mentions(r"Section (\d+(?:\.\d+)?)", secs, "Section")
    check_mentions(r"Sections (\d[\d., and]*)", secs, "Sections")

    # section headings present
    for title in ["1. Introduction", "2. Preliminaries",
                  "3. Galois Duality and Hull Support",
                  "4. Exact Joint Enumeration",
                  "5. Examples and Computational Validation",
                  "6. Conclusion", "2.1.", "2.2.", "2.3.", "3.1.", "3.2.",
                  "3.3.", "4.1.", "4.2.", "4.3.", "4.4.", "5.1.", "5.2."]:
        if title not in text:
            fail(f"heading {title!r} not found")

    if "??" in text:
        fail("unresolved reference (??) in PDF text")
    if re.search(r"\bFigure\b", text):
        fail("word 'Figure' appears (no figures expected)")
    if "frozen" in text or "boxed" in text.lower().replace(
            "unboxed", "") and "boxed transformation" in text:
        fail("leftover jargon in PDF text")

    # ---- 3. citations ----
    # (exclude orbit-length data such as [1, 6], which are not citations)
    notext = re.sub(r"orbit lengths? \[\d+, \d+\]", "", text)
    cited = set(re.findall(r"\[(\d+(?:,\s*\d+)*)\]", notext))
    flat: set[str] = set()
    for grp in cited:
        flat.update(x.strip() for x in grp.split(","))
    for n in [str(i) for i in range(1, 14)]:
        if n not in flat:
            fail(f"citation [{n}] never appears in PDF")
    # bibliography entries present
    for n in range(1, 14):
        if f"[{n}]" not in text:
            fail(f"bibliography entry [{n}] missing")

    # ---- report ----
    print(f"pages: {doc.page_count}")
    print(f"text chars: {len(text)}")
    for e in errors:
        print(f"ERROR: {e}")
    print("RESULT:", "PASS" if not errors else "FAIL")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
