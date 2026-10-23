# Submission Build Guide & Package Manifest

## 1. Ready-to-Use Turnkey Archives (`deliverables/`)
1. **`Paper2_Overleaf_Elsevier_Source.zip`** — Self-contained `elsarticle` LaTeX source package ready for **one-click Overleaf upload** (`New Project -> Upload Project`) OR **Elsevier Editorial Manager** flat source upload:
   - `main.tex` (uses `\graphicspath{{../figures/}{figures/}{./}}`, so it compiles identically whether figures sit in `figures/`, `../figures/`, or flat alongside `main.tex`)
   - `references.bib` (all 38 published entries verified with exact DOIs, 100% cited, 0 orphans)
   - `highlights.txt` (5 Elsevier bullet highlights, all $\le 83$ characters including spaces)
   - `elsarticle.cls` & `elsarticle-num.bst`
   - `figures/fig1_workflow.pdf` through `figures/fig9_conditional_F32.pdf`
2. **`Paper2_Supplementary_Code_and_Tables.zip`** — Clean referee & journal supplementary reproducibility package:
   - `README.md`
   - `code/` (`rr_enumerator.py`, `test_rr_enumerator.py`, `finite_fields.py`, `verify_rr.py`, `test_phase1_duality.py`, `test_phase2_transfer.py`, `test_phase3_consequences.py`, `generate_tables_figures.py`, `audit_latex.py`)
   - `tables/` (all 18 exact CSV/JSON coefficient, moment, extremal, summary, and verification log files)
3. **`Paper2_Complete_Submission_Repo_2026-10-23.bundle`** — Full private Git repository bundle tracking every commit sequentially from Phase 0 (`dc5f28a`) through Phase 7.

---

## 2. Compiling `main.pdf` Locally or on Overleaf
```bash
cd manuscript
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```
*(Or upload `Paper2_Overleaf_Elsevier_Source.zip` directly into Overleaf — zero configuration required, compiles with `pdfLaTeX`.)*

---

## 3. Running Full Verification & Audit Suite
```bash
python3 code/audit_latex.py
python3 code/test_rr_enumerator.py
python3 code/test_phase1_duality.py
python3 code/test_phase2_transfer.py
python3 code/test_phase3_consequences.py
python3 code/verify_rr.py
python3 code/generate_tables_figures.py
```
