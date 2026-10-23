# PROJECT STATUS — Repeated-Root Joint Code-Dimension & $k$-Galois-Hull Enumerators

**Target venue:** *Finite Fields and Their Applications* (Elsevier, `elsarticle`)  
**Working title:** *Joint Code-Dimension and $k$-Galois-Hull Enumerators for Repeated-Root Constacyclic Codes over Square-Free Affine Algebras*  
**Authors:** Arun Kumar Yadav, Vipin Gupta, Pooja Soni, Manju Pruthi

---

## Author Confirmation Status (Confirmed 2026-10-24)
1. **Authors & affiliations:** Finalized in `manuscript/main.tex` (*Arun Kumar Yadav, Vipin Gupta, Pooja Soni, Manju Pruthi*).
2. **Self-containment:** Completely self-contained — zero citation or discussion of any unpublished companion manuscript (`M=1` treated directly as the simple-root specialisation of $M=p^t\ge 1$).
3. **Funding:** Standard no-external-funding statement included in `\section*{Funding}` in `manuscript/main.tex` and `submission/author_declarations.md`.

---

## Execution Checklist
- [x] Phase 0 — Repository initialisation, pre-flight audit of `code/`, `tables/`, `figures/`, and primary-source verification.
- [x] Phase 1 — Setting (Section 2) and $k$-Galois Duality (Section 3) in `manuscript/main.tex`, plus Gate G1 verification (`code/test_phase1_duality.py`) and LaTeX/BibTeX auditor (`code/audit_latex.py`).
- [x] Phase 2 — Hull min-formula, transfer matrix and Main Theorem with full proof (Section 4 in `manuscript/main.tex`: Lemma 4.1 ideal intersection, Theorem 4.2 hull generator & edge-min formula, Remark 4.3 reconciliation with Debnath et al. Theorem 8, Definition 4.4 transfer matrix $T_w^{(M)}(U,Z)$, Lemma 4.5 trace formula, Theorem 4.6 Main Theorem, Corollary 4.7 short orbits & $M=1$ simple-root binomial formula, Example 4.8 full enumerator; verified by `code/test_phase2_transfer.py` & `code/audit_latex.py`).
- [x] Phase 3 — Consequences: marginals, LCD invariance, proved support trapezoid theorem, moments, and extremal classes (Section 5 in `manuscript/main.tex`: Proposition 5.1 marginals & duality symmetry, Theorem 5.2 $p$-power LCD invariance, Theorem 5.3 proved Support Trapezoid Theorem via threshold pairs & 1-Lipschitz adjacent-pebble walks, Corollary 5.4 global Minkowski hull spectrum, Theorem 5.5 exact mean/variance across $a=1,2,\ge 3$ & $\Cov(\kappa,\eta_k)=0$, Proposition 5.6 conditional moments, Theorem 5.7 SO/DC/SD enumerators & odd-$p$ vs $p=2$ self-dual dichotomy; verified by `code/test_phase3_consequences.py` & `code/audit_latex.py`).
- [x] Phase 4 — Algorithm/complexity and worked examples completed in `manuscript/main.tex` (Section 6: Proposition 6.1 polynomial-time DP & truncated $3$-jet algorithm, Section 6.2 independent Gram-rank & raw $\F_4^{30}$ quotient-ring verification, Table 4 across 11 benchmark families, Worked Examples 6.2–6.5 & Figures 8–9); upgraded `code/finite_fields.py` with arbitrary-degree Cantor–Zassenhaus factorisation and expanded `code/verify_rr.py` + `tables/verification_log.txt`.
- [x] Phase 5 — Live literature protocol, Introduction (with Table 2), Abstract, Conclusions, and Elsevier Highlights (`manuscript/highlights.txt` all $\le 83$ chars).
- [x] Phase 6 — Internal forensic referee audit, high-contrast regeneration of all 9 figures (`figures/*.pdf`, `figures/*.png`) and 18 tables (`tables/*`), zero-orphan BibTeX & CSV-to-LaTeX table verification (`code/audit_latex.py`), and referee audit register (`docs/REFEREE_AUDIT_REGISTER.md`).
- [x] Phase 7 — Final self-contained submission package (`manuscript/elsarticle.cls`, `manuscript/elsarticle-num.bst`, `submission/cover_letter_FFA.md`, `submission/author_declarations.md`, `submission/SUBMISSION_CHECKLIST_AND_BUILD_GUIDE.md`, and turnkey archives in `deliverables/`).
