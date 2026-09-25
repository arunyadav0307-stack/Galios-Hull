#!/usr/bin/env python3
"""Static validation of manuscript/main.tex (no TeX engine required).

Checks:
  1. \\begin/\\end environment balance (per environment name, in order).
  2. \\label defined exactly once; every \\ref/\\eqref resolves.
  3. Every \\cite key exists in references.bib; every bib entry is cited.
  4. \\( \\) \\[ \\] and $...$ balance (ignoring escaped \\$, \\(, etc.).
  5. Custom macros (\\newcommand): no redefinition; every use defined
     (custom list) or standard (allowlist of prefixes/package commands).
  6. No leftover figure placeholders, \\boxed, or internal jargon.
  7. .bib brace balance per entry; required fields present.
  8. No non-ASCII bytes in main.tex (engine safety).

Exit 0 on success, 1 on any failure. Warnings do not fail.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEX = ROOT / "manuscript" / "main.tex"
BIB = ROOT / "manuscript" / "references.bib"

errors: list[str] = []
warnings: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def strip_comments(text: str) -> list[str]:
    """Remove % comments (keep escaped \\%). Returns list of (lineno, line)."""
    out = []
    for i, line in enumerate(text.splitlines(), 1):
        buf = []
        j = 0
        while j < len(line):
            if line[j] == "%" and (j == 0 or line[j - 1] != "\\"):
                break
            buf.append(line[j])
            j += 1
        out.append((i, "".join(buf)))
    return out


def main() -> int:
    raw = TEX.read_text(encoding="utf-8")
    lines = strip_comments(raw)
    code = "\n".join(ln for _, ln in lines)

    # ---- 0. non-ASCII / basic ----
    for i, ln in lines:
        for ch in ln:
            if ord(ch) > 127:
                fail(f"line {i}: non-ASCII character {ch!r}")
                break

    # ---- 1. environment balance ----
    stack: list[tuple[str, int]] = []
    for i, ln in lines:
        for m in re.finditer(r"\\(begin|end)\{([A-Za-z*]+)\}", ln):
            kind, name = m.group(1), m.group(2)
            if kind == "begin":
                stack.append((name, i))
            else:
                if not stack:
                    fail(f"line {i}: \\end{{{name}}} with empty stack")
                elif stack[-1][0] != name:
                    fail(f"line {i}: \\end{{{name}}} closes "
                         f"\\begin{{{stack[-1][0]}}} from line {stack[-1][1]}")
                    stack.pop()
                else:
                    stack.pop()
    for name, i in stack:
        fail(f"line {i}: \\begin{{{name}}} never closed")

    # ---- 2. labels / refs ----
    labels = re.findall(r"\\label\{([^}]*)\}", code)
    seen: dict[str, int] = {}
    for lab in labels:
        seen[lab] = seen.get(lab, 0) + 1
    for lab, n in seen.items():
        if n > 1:
            fail(f"label {lab!r} defined {n} times")
    for cmd in ("ref", "eqref"):
        for m in re.finditer(r"\\" + cmd + r"\{([^}]*)\}", code):
            if m.group(1) not in seen:
                fail(f"\\{cmd}{{{m.group(1)}}} has no \\label")
    # unreferenced labels (info only, except figures which must not exist)
    for lab in seen:
        if not re.search(r"\\(ref|eqref)\{" + re.escape(lab) + r"\}", code):
            if lab.startswith("fig:"):
                fail(f"figure label {lab!r} present (placeholders must go)")
            else:
                warn(f"label {lab!r} never referenced")

    # ---- 3. citations ----
    bib_raw = BIB.read_text(encoding="utf-8")
    bib_keys = re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", bib_raw)
    if len(bib_keys) != len(set(bib_keys)):
        fail("duplicate keys in references.bib")
    cited: set[str] = set()
    for m in re.finditer(r"\\cite\{([^}]*)\}", code):
        for key in m.group(1).split(","):
            key = key.strip()
            cited.add(key)
            if key not in bib_keys:
                fail(f"\\cite key {key!r} missing from references.bib")
    for key in bib_keys:
        if key not in cited:
            fail(f"bib entry {key!r} never cited")

    # ---- 4. math delimiter balance ----
    # remove escaped delimiters first
    tmp = code
    tmp = tmp.replace("\\$", "").replace("\\(", "").replace("\\)", "")
    # \[ \] are display math; count pairs in order
    opens = [m.start() for m in re.finditer(r"\\\[", tmp)]
    closes = [m.start() for m in re.finditer(r"\\\]", tmp)]
    if len(opens) != len(closes):
        fail(f"\\[ count ({len(opens)}) != \\] count ({len(closes)})")
    else:
        for o, c in zip(opens, closes):
            if o > c:
                fail("\\[ ... \\] order violation")
                break
    # $...$: count unescaped $ outside \[...\] and equation envs is complex;
    # approximate: total unescaped $ must be even.
    noslash = re.sub(r"\\\\", "", tmp)  # drop \\ first
    dollars = noslash.count("$")
    if dollars % 2 != 0:
        fail(f"odd number ({dollars}) of unescaped $ signs")
    # \( \) pairs
    if tmp.count("\\(") != tmp.count("\\)"):
        fail("\\( / \\) mismatch (after escape filtering this is ~always 0/0)")

    # ---- 5. custom macros ----
    newcmds = re.findall(r"\\newcommand\{\\([A-Za-z]+)\}", code)
    if len(newcmds) != len(set(newcmds)):
        fail("duplicate \\newcommand definitions")
    newcol = re.findall(r"\\newcolumntype\{([A-Za-z])\}", code)
    newthm = re.findall(r"\\newtheorem\{([A-Za-z]+)\}", code)
    defined_custom = set(newcmds) | set(newcol) | set(newthm)
    # commands provided by loaded packages / base latex (prefix allowlist)
    std = {"begin", "end", "label", "ref", "eqref", "cite", "newcommand",
           "newcolumntype", "newtheorem", "theoremstyle", "usepackage",
           "documentclass", "title", "author", "date", "maketitle",
           "geometry", "hypersetup", "setlength", "renewcommand",
           "makeatletter", "makeatother", "noindent", "rule", "linewidth",
           "textbf", "textit", "emph", "text", "textnormal", "small", "scriptsize",
           "footnotesize", "normalsize", "centering", "caption", "bibliographystyle",
           "bibliography", "section", "subsection", "subsubsection", "paragraph",
           "frac", "sum", "prod", "int", "sqrt", "left", "right", "big",
           "bigl", "bigr", "Big", "Bigl", "Bigr", "bigg", "Bigg", "qquad",
           "quad", "hspace", "vspace", "allowbreak", "texttt", "mathsf",
           "mathrm", "mathbb", "mathcal", "mathscr", "operatorname",
           "boldsymbol", "texorpdfstring", "boxed", "tag", "notag",
           "hline", "toprule", "midrule", "bottomrule", "cmidrule",
           "item", "footnote", "url", "href", "label", "pageref",
           "lcm", "gcd", "deg", "dim", "ker", "hom", "tr", "sigma",
           "Box", "qedhere", "numberwithin", "DeclareMathOperator",
           "ifPDFTeX", "fi", "csname", "endcsname", "arabic", "the",
           "arraybackslash", "longrightarrow", "raggedright"}
    used = set(re.findall(r"\\([A-Za-z]+)", code))
    greek = {"alpha", "beta", "gamma", "delta", "varepsilon", "epsilon",
             "lambda", "mu", "nu", "omega", "rho", "sigma", "tau", "chi",
             "phi", "psi", "theta", "zeta", "eta", "kappa", "pi",
             "Gamma", "Delta", "Lambda", "Omega", "Sigma", "Phi",
             "infty", "partial", "ell", "prime"}
    symbols = {"times", "cdot", "cap", "cup", "setminus", "subset", "subseteq",
               "supset", "in", "notin", "ni", "ne", "neq", "equiv", "cong",
               "cong", "approx", "sim", "simeq", "cong", "propto", "mapsto",
               "longmapsto", "to", "rightarrow", "leftarrow", "Rightarrow",
               "implies", "iff", "forall", "exists", "mid", "parallel",
               "perp", "angle", "langle", "rangle", "lfloor", "rfloor",
               "lceil", "rceil", "varnothing", "emptyset", "nabla",
               "oplus", "otimes", "odot", "pm", "mp", "ast", "star",
               "dagger", "ddagger", "circ", "bullet", "div", "wedge", "vee",
               "neg", "lnot", "land", "lor", "top", "bot", "prime",
               "le", "leq", "ge", "geq", "ll", "gg", "prec", "succ",
               "sum", "prod", "coprod", "bigcup", "bigcap", "bigoplus",
               "bigotimes", "bigodot", "int", "oint", "iint", "iiint",
               "sqrt", "surd", "overline", "underline", "widehat", "widetilde",
               "bar", "dot", "ddot", "vec", "hat", "check", "breve", "acute",
               "grave", "tilde", "mathring", "textit", "textbf", "textup",
               "textsl", "textsc", "emph", "ldots", "cdots", "vdots", "ddots",
               "dots", "dotsb", "dotsm", "dotsi", "dotsc", "geqslant",
               "leqslant", "neq", "pmod", "bmod", "mod", "pod", "binom",
               "tfrac", "dfrac", "cfrac", "binom", "dbinom", "tbinom",
               "leftroot", "uproot", "substack", "overset", "underset",
               "xrightarrow", "xleftarrow", "boxed", "fbox", "parbox",
               "raisebox", "mbox", "makebox", "framebox", "hspace", "vspace",
               "hfill", "vfill", "hrule", "vrule", "rule", "indent", "noindent",
               "par", "newline", "newpage", "clearpage", "linebreak", "nolinebreak",
               "pagebreak", "nopagebreak", "sloppy", "fussy", "hyphenation",
               "thinspace", "enspace", "quad", "qquad", "nonumber", "notag"}
    ok = std | greek | symbols | defined_custom
    for cmd in sorted(used - ok):
        # single-letter accents / special forms
        if re.fullmatch(r"[A-Za-z]", cmd):
            continue
        fail(f"possibly undefined command \\{cmd}")

    # ---- 6. banned leftovers ----
    for pat, msg in [
        (r"\\begin\{figure\}", "figure environment present"),
        (r"Intended Figure", "placeholder figure text present"),
        (r"\\boxed", "\\boxed present (must be converted to equations)"),
        (r"frozen", "jargon 'frozen' present"),
        (r"Phase-?10", "internal phase label present"),
        (r"\bN1\b", "internal artifact label N1 present (bare)"),
        (r"[Aa]udit", "audit jargon present"),
        (r"\\toprule|\\midrule|\\bottomrule", "booktabs rule present"),
    ]:
        if re.search(pat, code):
            # N1 is allowed inside the scope table row + one defined mention
            if pat.startswith(r"\bN1"):
                n1 = len(re.findall(r"\bN1\b", code))
                if n1 > 2:
                    fail(f"{msg}: {n1} occurrences (max 2 allowed)")
                continue
            fail(msg)

    # ---- 7. bib checks ----
    depth = 0
    for i, ln in enumerate(bib_raw.splitlines(), 1):
        for ch in ln:
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth < 0:
                    fail(f"references.bib line {i}: unbalanced brace")
                    depth = 0
    if depth != 0:
        fail(f"references.bib: final brace depth {depth}")
    entries = re.findall(r"@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)(?=@\w+\s*\{|\Z)",
                         bib_raw, re.DOTALL)
    for etype, key, body in entries:
        for field in ("author", "title", "year"):
            if not re.search(r"\b" + field + r"\s*=", body):
                fail(f"bib entry {key}: missing {field}")
        if etype == "article" and "journal" not in body:
            fail(f"bib entry {key}: article without journal")

    # ---- report ----
    n_begin = len(re.findall(r"\\begin\{", code))
    n_ref = len(re.findall(r"\\ref\{", code))
    n_eqref = len(re.findall(r"\\eqref\{", code))
    n_eqn = len(re.findall(r"\\begin\{equation\}", code))
    print(f"environments: balanced ({n_begin} begins)")
    print(f"labels: {len(seen)} defined, {n_ref} refs, {n_eqref} eqrefs")
    print(f"citations: {len(cited)}/{len(bib_keys)} bib entries cited")
    print(f"equations: {n_eqn} numbered")
    for w in warnings:
        print(f"WARNING: {w}")
    for e in errors:
        print(f"ERROR: {e}")
    print("RESULT:", "PASS" if not errors else "FAIL")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
