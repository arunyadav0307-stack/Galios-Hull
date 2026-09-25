# Galios-Hull — Reference-Style Manuscript Revision

Revision of the source paper *"Exact Joint Enumeration of k-Galois Hull
Dimensions for Labeled Constacyclic Codes over Square-Free Affine
Algebras"* (from `Galios-Hull-Submission-Phase10F.zip`) so its
presentation, organization, and mathematical writing style match the
reference coding-theory article (Debnath–Islam–Martínez-Moro–Prakash,
*Galois hulls of constacyclic codes over affine algebra rings*), while
keeping the source paper's mathematics unchanged. The reference was used
as a structural/stylistic model only; none of its content was imported.

## Layout

| Path | Description |
|---|---|
| `manuscript/main.tex` | **Revised LaTeX source** (authoritative manuscript) |
| `manuscript/references.bib` | Bibliography: 13 source entries + 17 verified additions = 30, all cited |
| `manuscript/main.pdf` | Compiled 18-page PDF (see build note) |
| `manuscript/main.typ` | Typst port used only to render the PDF here |
| `manuscript/build_pdf_typst.py` | PDF build script (fallback chain) |
| `tools/check_manuscript.py` | LaTeX static validator (envs, refs, cites, macros) |
| `tools/check_math_preservation.py` | Source-vs-revised display-math comparison |
| `tools/check_pdf.py` | Rendered-PDF content-closure check |
| `STYLE_MAPPING.md` | Reference-vs-source style mapping + plan |
| `CHANGELOG.md` | What changed (presentation only) + build-chain note |
| `CONSISTENCY_CHECK.md` | Proof that no mathematics was altered |
| `Galios-Hull-Submission-Phase10F.zip` | Original source package (untouched) |
| `Galios hulls of constacclic codes over affine algebra rings'.pdf` | Style reference (untouched) |

## Build the PDF from LaTeX (on any TeX Live system)

```bash
cd manuscript
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Validate (no TeX engine needed)

```bash
python3 tools/check_manuscript.py        # expect RESULT: PASS
python3 tools/check_math_preservation.py # expect RESULT: PASS
python3 manuscript/build_pdf_typst.py    # needs: pip install typst pymupdf
python3 tools/check_pdf.py               # expect RESULT: PASS
```

## Build note

This sandbox has no TeX engine and no network route to TeX
distributions, so `manuscript/main.pdf` was rendered from the faithful
Typst port `manuscript/main.typ` (identical text, math, numbering,
tables, bibliography; `typst 0.15.0`, zero warnings). The LaTeX source
was validated statically in place of compilation; see `CHANGELOG.md`.
