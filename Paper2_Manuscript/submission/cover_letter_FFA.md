# Cover Letter — *Finite Fields and Their Applications*

**Date:** October 24, 2026

**To:** The Editor-in-Chief, *Finite Fields and Their Applications* (Elsevier)

**Subject:** Submission of original research manuscript — *"Joint Code-Dimension and $k$-Galois-Hull Enumerators for Repeated-Root Constacyclic Codes over Square-Free Affine Algebras"*

Dear Editor-in-Chief,

We respectfully submit our manuscript entitled **"Joint Code-Dimension and $k$-Galois-Hull Enumerators for Repeated-Root Constacyclic Codes over Square-Free Affine Algebras"** for consideration for publication as a regular research article in *Finite Fields and Their Applications*.

### Scientific context and main contributions
The $k$-Galois hull $\operatorname{Hull}_{\mathcal{A},k}(C) = C \cap D_{\mathcal{A},k}(C)$ unifies Euclidean ($k=0$), Hermitian, and general Frobenius dualities, governing both linear complementary dual (LCD) codes and entanglement-assisted quantum error-correcting code (EAQECC) parameters. Very recently, Debnath, Islam, Martínez-Moro, and Prakash (*Discrete Mathematics* **349**(2) (2026), 114750) studied $k$-Galois hulls of constacyclic codes over split square-free affine algebras ($m_s = 1$) under $\gcd(\operatorname{ord}(\lambda), n') = 1$ and posed in their Conclusion (p. 23) the open problem of counting the number of constacyclic codes over $\mathcal{A}$ having each prescribed $k$-Galois hull dimension.

In this work, we resolve that open problem in full generality — jointly with the $\mathbb{F}_q$-code dimension $\kappa(C)$ — for arbitrary lengths $n = n' p^t$ ($M = p^t \ge 1$, $\gcd(n', p) = 1$), arbitrary finite field extensions $K_s = \mathbb{F}_{q^{m_s}}$ ($m_s \ge 1$) inside any finite commutative square-free affine algebra $\mathcal{A} \cong \prod_{s=1}^{N} K_s$, arbitrary twists $\lambda \in \mathcal{A}^*$ (both compatible and incompatible, with zero coprimality restriction between $\operatorname{ord}(\lambda_s)$ and $n'$), and all $0 \le k < e$:

1. **Repeated-root $k$-Galois duality and twist compatibility:** Passing to unique $p^t$-th roots $\lambda_{s,0} \in K_s^*$ preserves twist compatibility unchanged ($\lambda_{s,0}^{\,1+p^{em_s-k}} = 1 \iff \lambda_s^{\,1+p^{em_s-k}} = 1$), collapses all incompatible components to trivial hulls, and expresses $\dim_{K_s}\operatorname{Hull}_k(C_s(e))$ on compatible components as cyclic sums of local edge minima $\min\{e_{O,i}, M - e_{O,i+1}\}$ along inverse-Frobenius reciprocal orbits.
2. **Universal $(M+1)\times(M+1)$ transfer-matrix trace product:** We prove a closed trace-product formula for the bivariate enumerator $\mathscr{E}^{(M)}(U, Z) = \sum_C U^{\kappa(C)} Z^{\eta_k(C)}$ that evaluates exponentially large code spaces (such as $5^{31} \approx 4.66 \times 10^{21}$ codes over $\mathbb{F}_{32}$ at $n = 124$) in $< 0.3$ seconds of exact integer arithmetic while containing the simple-root theory ($M = 1$) as an immediate special case.
3. **Structural and statistical consequences:** From $\mathscr{E}^{(M)}(U,Z)$, we prove (i) $p$-power invariance $2^{\sum_s |\mathcal{O}_s|}$ of the compatible $k$-Galois LCD code count via the rank-$2$ unipotent Jordan block of $T_1^{(M)}(1,0)$, (ii) an unconditional characterisation of the single-orbit support trapezoid $\min\{R, M, aM - R\} \le H \le \min\{R, aM - R\}$ and global Minkowski hull spectrum, (iii) closed rational formulas for $\mathbb{E}[\eta_k]$, $\operatorname{Var}(\eta_k)$ across all three correlation regimes ($a=1$ even/odd $M$, $a=2$, and $a \ge 3$), $\operatorname{Cov}(\kappa, \eta_k) = 0$, and conditional factorial moments given $\kappa$, and (iv) exact enumerators for self-orthogonal, dual-containing, and self-dual codes revealing a sharp $p = 2$ versus odd-$p$ dichotomy on odd-length orbits.
4. **Complete independent computational verification:** Every formula and table is independently verified from first principles using arbitrary-degree Cantor–Zassenhaus factorisation, finite-field Gram-rank computations, and raw quotient-polynomial linear algebra in $\mathbb{F}_4^{30}$ across characteristics $2$, $3$, and $5$; the complete zero-dependency Python verification package accompanies the submission.

### Declarations
This manuscript is original, is not under consideration elsewhere, and has been approved by all co-authors. This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors, and the authors declare no competing financial or personal interests.

Thank you very much for considering our manuscript for *Finite Fields and Their Applications*.

Sincerely,

**Arun Kumar Yadav** (Corresponding Author)  
*On behalf of co-authors Vipin Gupta, Pooja Soni, and Manju Pruthi*  
School of Basic and Applied Sciences, K.R. Mangalam University, Sohna Road, Gurugram 122103, Haryana, India  
Email: `arunyadav0307@gmail.com`
