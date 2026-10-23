# Exact Joint Code-Dimension and *k*-Galois Hull Enumerators for Repeated-Root Constacyclic Codes over Affine Algebras

This repository contains the complete research paper, mathematical proofs, LaTeX source files, computational verification scripts, benchmark tables, and generated figures for the manuscript:

> **“Exact Joint Code-Dimension and *k*-Galois Hull Enumerators for Repeated-Root Constacyclic Codes over Affine Algebras”**  
> *Authors:* Arun Kumar Yadav, Vipin Gupta, Pooja Soni, Manju Pruthi  
> *Target Journal:* Finite Fields and Their Applications (Elsevier)

---

## 1. Project Overview & Research Contributions

This work develops the first exact, comprehensive algebraic framework for computing the bivariate joint code-dimension and $k$-Galois-hull enumerator for **repeated-root constacyclic codes** over arbitrary square-free affine algebras $\mathcal{A} \cong \bigoplus_{s=1}^m \mathbb{F}_{q_s}$.

### Key Innovations:
1. **Multi-State Valuation State Space:** In repeated-root codes ($n = \bar{n} p^a$, multiplicity $M = p^a \ge 2$), ambient quotient rings decompose into direct sums of local finite chain rings $\mathbb{F}_q[x]/\langle f_i(x)^M\rangle$. The code selection at each factor is an integer state $u \in \{0, 1, \dots, M\}$ rather than a binary choice $\{0, 1\}$.
2. **Exact Hull Dimension Formula:** We prove that for any repeated-root constacyclic code $C$, the $k$-Galois hull dimension is given by:
   $$\dim_{\mathbb{F}_q}(\operatorname{Hull}_k(C)) = \sum_{i=1}^r \deg(f_i) \min\left(u_i, M - u_{\pi^{-1}(i)}\right),$$
   where $\pi$ is the permutation induced on irreducible factors by the $k$-Galois reciprocal involution $f^{*, k}(x)$.
3. **$(M+1) \times (M+1)$ Polynomial Transfer Matrix:** We define the polynomial matrix $\mathbf{T}_{M, d}(x, y)$ with entries $[\mathbf{T}_{M, d}]_{i, j} = x^{d j} y^{d \min(j, M - i)}$ and prove that the orbit joint enumerator is exactly:
   $$\Phi_{\mathcal{O}}(x, y) = \operatorname{Tr}\left(\mathbf{T}_{M, d}(x, y)^\ell\right).$$
4. **Structural Properties & LCD Classification:** We prove duality palindromicity $\Phi(x, y) = x^n \Phi(x^{-1}, y)$, classify and count $k$-LCD codes (showing non-trivial $k$-LCD codes cannot exist within single repeated-root components), and enumerate self-dual and self-orthogonal codes.
5. **Exact Moments & Asymptotics:** We derive closed-form expressions for the unconditional mean $\mathbb{E}[H]$, variance $\operatorname{Var}(H)$, and adjacent-state covariance $\operatorname{Cov}(X_1, X_2)$, establishing that as $M \to \infty$, the expected hull dimension ratio $\mathbb{E}[H]/n \to 1/3$ (contrasting with $1/4$ for simple-root codes).
6. **100% Linear-Algebra Verification:** Comprehensive test suite in Python confirming 100% agreement between the transfer-matrix traces and independent finite-field linear algebra (null spaces, RREF, code intersection) across characteristics $p=2, 3, 5$.

---

## 2. Directory Structure & File Manifest

- `main.tex` — Complete manuscript in Elsevier `elsarticle` format.
- `references.bib` — BibTeX bibliography database with full, verified citations.
- `elsarticle.cls`, `elsarticle-num.bst` — Elsevier document class and numeric bibliography style.
- `Highlights.tex` — Executive article highlights.
- `Cover_Letter.tex` — Formal submission cover letter to the journal editors.
- `code/verify_all.py` — Complete computational verification suite and benchmark generator.
- `code/generate_figures.py` — Publication-quality figure generation script.
- `figures/`
  - `fig_state_diagram.png` — Directed state-transition graph for $(M+1)$-state transfer matrix ($M=2$).
  - `fig_hull_distribution.png` — Joint enumerator heatmap and conditional moment profile for $n=42$.
  - `fig_asymptotic_moments.png` — Mean hull ratio $\mathbb{E}[H]/n$ and variance scaling vs multiplicity $M$.
- `tables/`
  - `family1_F2_n6_joint_enumerator.csv` — Exact joint distribution for $\mathbb{F}_2, n=6, M=2$.
  - `family2_F2_n14_joint_enumerator.csv` — Exact joint distribution for $\mathbb{F}_2, n=14, M=2$ (2-cycle).
  - `family3_F3_n6_joint_enumerator.csv` — Exact joint distribution for $\mathbb{F}_3, n=6, M=3$.
  - `family4_F3_n12_joint_enumerator.csv` — Exact joint distribution for $\mathbb{F}_3, n=12, M=3$.
  - `family5_F4_n10_joint_enumerator.csv` — Exact joint distribution for $\mathbb{F}_4, n=10, M=2, k=1$.
  - `family6_Affine_A_n6_joint_enumerator.csv` — Exact joint distribution for $\mathcal{A} \cong \mathbb{F}_2 \oplus \mathbb{F}_4, n=6$.
  - `family7_F2_n30_joint_enumerator.csv` — Exact joint distribution for $\mathbb{F}_2, n=30, M=2$.
  - `family8_F2_n42_joint_enumerator.csv` — Exact joint distribution for $\mathbb{F}_2, n=42, M=2$.
  - `summary_all_families.csv` — Summary comparison table across all 8 tested families.

---

## 3. How to Reproduce Computations

### Requirements:
- Python 3.8+
- `numpy`, `sympy`, `matplotlib`

### Run Verification Suite:
```bash
python3 code/verify_all.py
```
This script runs the entire verification pipeline, compares every code against ground truth linear algebra, and exports all CSV tables into `tables/`.

### Generate Figures:
```bash
python3 code/generate_figures.py
```

---

## 4. How to Compile the LaTeX Manuscript

To compile the LaTeX manuscript in any standard TeX environment (TeX Live, MacTeX, Overleaf, MikTeX):
```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

---

## 5. License & Citation

This research package is distributed for peer review and academic research. If you build upon this work, please cite:

```bibtex
@article{Yadav2026RepeatedRoot,
  author  = {Yadav, Arun Kumar and Gupta, Vipin and Soni, Pooja and Pruthi, Manju},
  title   = {Exact Joint Code-Dimension and $k$-{G}alois Hull Enumerators for Repeated-Root Constacyclic Codes over Affine Algebras},
  journal = {Finite Fields and Their Applications},
  year    = {2026}
}
```
