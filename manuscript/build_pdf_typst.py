#!/usr/bin/env python3
"""Render manuscript/main.pdf from manuscript/main.typ using Typst.

Fallback build chain: this sandbox provides no TeX engine and no network
route to TeX distributions (apt/CTAN/TinyTeX unreachable; only PyPI/npm/
GitHub-API are reachable, and no TeX engine is published there). The LaTeX
source manuscript/main.tex therefore remains the authoritative manuscript;
manuscript/main.typ is a faithful port (same text, mathematics, numbering,
table data, and bibliography) used only to produce a reviewable PDF here.

Requires: pip install typst pymupdf  (typst 0.15.0 used for main.pdf)
Usage:   python3 manuscript/build_pdf_typst.py   (run from repo root)
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TYP = ROOT / "main.typ"
PDF = ROOT / "main.pdf"


def main() -> int:
    import typst
    import pymupdf

    print(f"typst input : {TYP}")
    print(f"pdf output  : {PDF}")
    try:
        _, warnings = typst.compile_with_warnings(str(TYP), str(PDF))
    except Exception as exc:  # typst.TypstError
        print(f"ERROR: typst compilation failed:\n{exc}")
        return 1
    if warnings:
        print("typst warnings:")
        for w in warnings:
            print(f"  - {w}")
    else:
        print("typst warnings: none")
    doc = pymupdf.open(PDF)
    print(f"pages: {doc.page_count}")
    print(f"bytes: {PDF.stat().st_size}")
    # crude overflow tripwire: lines extending past the right margin
    bad = 0
    for i, page in enumerate(doc):
        w = page.rect.width
        for line in page.get_text("dict")["blocks"]:
            for ln in line.get("lines", []):
                if ln["bbox"][2] > w - 36:  # within 0.5in of edge
                    bad += 1
                    if bad <= 10:
                        xs = [s["text"] for s in ln["spans"]]
                        print(f"  wide line p{i + 1}: {''.join(xs)[:80]!r}")
    print(f"lines near right edge (inspect): {bad}")
    print("RESULT: PDF written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
