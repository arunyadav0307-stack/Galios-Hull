# Joint Code-Dimension & $k$-Galois-Hull Enumerators for Repeated-Root Constacyclic Codes

**Title:** *Joint Code-Dimension and $k$-Galois-Hull Enumerators for Repeated-Root Constacyclic Codes over Square-Free Affine Algebras*  
**Authors:** Arun Kumar Yadav, Vipin Gupta, Pooja Soni, Manju Pruthi  
**Target Journal:** *Finite Fields and Their Applications* (Elsevier, `elsarticle`)

---

## Directory Layout
- `manuscript/` — Self-contained `elsarticle` journal source (`main.tex`, `references.bib`, `main.bbl`, `main.pdf` [36 pages], `highlights.txt`, `elsarticle.cls`, `elsarticle-num.bst`).
- `figures/` — The 3 publication vector PDFs (`fig1_workflow.pdf`, `fig5_joint_F8_n14.pdf`, `fig6_joint_F32_n62.pdf`) + 300-DPI PNG previews.
- `tables/` — All 18 exact CSV/JSON enumerator tables, moment tables, extremal tables, and `verification_log.txt`.
- `code/` — Complete reproducible verification and generation suite:
  - `rr_enumerator.py` — Transfer-matrix dynamic programming, exact moments, LCD/SO/DC/SD extraction, support trapezoid.
  - `finite_fields.py` — Exact arithmetic over $\mathbb{F}_{p^e}$, Distinct-Degree + Cantor–Zassenhaus factorisation, Gram-rank dual/hull spaces.
  - `verify_rr.py` — Exhaustive, sampled, degree-3/4, and raw $\mathbb{F}_4^{30}$ non-split quotient-algebra verification across 15 test suites.
  - `test_rr_enumerator.py` — Combinatorial & closed-form identity test suite.
  - `test_phase1_duality.py` — Gate G1 repeated-root duality, compatibility invariance, incompatible twist collapse, and pairing invariance tests.
  - `test_phase2_transfer.py` — Symbolic $(M+1)\times(M+1)$ transfer-matrix trace, $M=1$ simple-root binomial reduction, and Debnath–min equivalence tests.
  - `test_phase3_consequences.py` — Constructive 1-Lipschitz adjacent-pebble walk across 153 slices, moment polynomials up to $M=30$, and extremal counts.
  - `generate_tables_figures.py` — Regenerates all 18 CSV/JSON data files in `tables/` and all 18 PDF/PNG figures in `figures/`.
  - `audit_latex.py` — Strict AST, macro, label/ref, zero-orphan BibTeX, CSV-to-LaTeX table cell, and Elsevier Highlights auditor.
- `docs/` — Architecture blueprint (`BLUEPRINT.md`), literature notes (`LITERATURE_NOTES.md`), and referee audit register (`REFEREE_AUDIT_REGISTER.md`).
- `submission/` — Editorial cover letter (`cover_letter_FFA.md`), Elsevier declarations (`author_declarations.md`), and build guide (`SUBMISSION_CHECKLIST_AND_BUILD_GUIDE.md`).

---

## Reproducing Everything From Scratch
```bash
python3 code/test_rr_enumerator.py
python3 code/test_phase1_duality.py
python3 code/test_phase2_transfer.py
python3 code/test_phase3_consequences.py
python3 code/verify_rr.py
python3 code/generate_tables_figures.py
python3 code/audit_latex.py
```
