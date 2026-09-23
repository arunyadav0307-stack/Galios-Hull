# Exact Enumeration of `k`-Galois Hull Dimensions of Constacyclic Codes over Square-Free Affine Algebras

> **Blueprint status:** This is a revised research blueprint after mathematical consistency checks and exhaustive computational validation of the listed finite examples. The general results remain subject to complete formal proofs and final literature verification before manuscript submission.
>
> **Evidence categories:**
>
> - **Computationally verified:** only the finite instances explicitly listed in Section 10 and the accompanying validators.
> - **Mathematical proof targets:** the general reciprocal, dual-generator, hull-support, orbit, transfer-matrix, distribution, LCD, and moment results.
> - **Externally dependent:** standard finite-field, CRT, square-free-factorization, and any eventual quantum-construction results, each with a citation and scope check.
> - **VERIFY BEFORE MANUSCRIPT FINALIZATION:** all priority claims, complete published-paper comparisons, unresolved parameter details for N1/N2, and any result not supported by a cited proof or a reproducible computation.
>
> **Base paper:** Debnath, Islam, Martínez-Moro, and Prakash, *Galois hulls of constacyclic codes over affine algebra rings*, *Discrete Mathematics* 349 (2026), Article 114750, DOI 10.1016/j.disc.2025.114750.
>
> **Positioning:** The proposed paper is an exact enumerative study. It makes no Pólya/Burnside orbit-counting claim; a transfer matrix over labeled factor orbits counts selections directly.

## Abstract (draft for manuscript)

We study the exact distribution of `k`-Galois hull dimensions of `lambda`-constacyclic codes over a square-free affine algebra. The square-free hypothesis decomposes the algebra into finite-field components and reduces each component code to a binary selection of irreducible factors of a simple-root constacyclic polynomial. With the second-slot convention

\[
\langle x,y\rangle_{s,k}=\sum_i x_i y_i^{p^k},
\]

we define the normalized `k`-Galois reciprocal, its factor permutation, and the resulting hull-support statistic. Under the explicitly collected hypotheses of Section 3, the main proof target is the bivariate enumerator

\[
\mathscr E(u,z)=\prod_s\prod_O\operatorname{tr}\bigl(T_{w_O}(u,z)^{a_O}\bigr),
\qquad
T_w(u,z)=\begin{pmatrix}u^w&1\\u^wz^w&1\end{pmatrix},
\]

where `u` records `F_q`-code dimension and `z` records `F_q`-hull dimension. Its specialization gives the exact hull-distribution polynomial, the total-code count, the LCD count, and closed mean and variance formulas, including the exceptional two-cycle variance. The paper distinguishes theorem-level proofs from exhaustive finite computations. The current validation suite confirms the formulas for the `F_4` pilot, a long `F_8` orbit, an `F_{16}` extension component, a nontrivial compatible twist, and an incompatible-twist diagnostic; N1 and N2 are retained as validation obligations whose complete parameters and outputs must be verified before submission.

## Notation table and convention audit

| Symbol | Meaning | Scope or warning |
|---|---|---|
| `p` | characteristic prime | `q=p^e` |
| `q` | base-field size | `\mathbb F_q` |
| `e` | base-field extension degree | positive integer |
| `k` | Galois parameter | `0\le k<e` |
| `\sigma_{s,k}` | main coefficient Frobenius | `a\mapsto a^{p^k}` on `K_s`; it acts on the second inner-product slot |
| `\rho_s` | inverse of `\sigma_{s,k}` | alternative notation only: `\rho_s=\sigma_{s,k}^{-1}`; it must not replace `\sigma_{s,k}` in the main dual-generator formula |
| `A` | square-free affine algebra | decomposes as `\prod_s K_s` |
| `K_s` | simple field component | `K_s=\mathbb F_{q^{m_s}}` |
| `m_s` | component degree | `[K_s:\mathbb F_q]` |
| `n` | constacyclic coordinate length | `n\ge1`, normally `\gcd(n,p)=1` |
| `\lambda_s` | component of the constacyclic unit | `\lambda_s\in K_s^\times` |
| `N` | number of simple algebra components | `1\le s\le N` |
| `\ell` | number of affine variables | appears in the presentation of `A` |
| `e_s` | primitive orthogonal idempotent | identifies the component `K_s` |
| `M_s(x)` | component constacyclic modulus | `x^n-\lambda_s` |
| `\mathcal F_s` | monic irreducible factors of `M_s` | distinct factors in the square-free case |
| `\mathcal O_s` | set of `\tau_{s,k}`-orbits in `\mathcal F_s` | orbits are indexed factor selections, not equivalence classes |
| `J_s` | selected factor subset | indexes one component code |
| `g_{J_s}` | generator factor product | `\prod_{f\in J_s}f` |
| `h_{J_s}` | check-polynomial factor product | `(x^n-\lambda_s)/g_{J_s}` |
| `\tau_{s,k}` | factor permutation | `f\mapsto f^{\#_{s,k}}` under compatibility |
| `O` | one `\tau_{s,k}`-orbit | length `a_O` |
| `a_O` | orbit length | positive integer |
| `d_O` | common `K_s`-degree in an orbit | `\deg_{K_s}f` |
| `w_O` | `F_q`-weight of an orbit | `m_s d_O` |
| `\varepsilon_i` | binary selection indicator | `1` means the factor is in the generator set |
| `b_O(\varepsilon)` | cyclic boundary count | number of `1\to0` transitions on `O` |
| `P_{a,w}(z)` | one-orbit hull polynomial | specialization of the trace at `u=1` |
| `\operatorname{Hull}_k(C)` | `C\cap C^{\perp_k}` | dimensions below are over `\mathbb F_q` unless labeled `K_s` |
| `\mathscr C(A,n,\lambda)` | set of distinct labeled factor-selection codes | no quotient by equivalence |
| `T_w(u,z)` | one-orbit transfer matrix | `u` tracks code dimension, `z` tracks hull dimension |
| `u,z` | enumerator variables | `u` for code dimension and `z` for hull dimension |
| `L` | ambient `F_q`-dimension | `L=n\dim_{\mathbb F_q}A` |
| `\mathscr E(u,z)` | joint enumerator | counts distinct labeled codes |
| `H(z)` | hull-distribution polynomial | `H(z)=\mathscr E(1,z)` |
| `N_h` | number of codes with hull dimension `h` | `[z^h]H(z)` |

**Convention audit.** The principal convention is

\[
\langle x,y\rangle_{s,k}=\sum_i x_i y_i^{p^k},
\qquad
\sigma_{s,k}(a)=a^{p^k}.
\]

The normalized reciprocal, dual-generator identity, root action, and compatibility condition below use `\sigma_{s,k}` (equivalently the exponent `p^k`). The inverse exponent `\rho_s` may occur only in a clearly labeled comparison with the alternative first-slot/inverse convention. A final global search must confirm that no inverse-`\rho_s` expression remains in a principal formula except the explicitly labeled N2 comparison.

---

## 0. Audit findings — what was corrected and why

The previous framework had the right research direction, but several statements needed to be made conditional or proved more carefully.

### Correction A — title and positioning

The earlier title invoked Pólya/Burnside orbit counting. The revised title is:

> **Exact Enumeration of `k`-Galois Hull Dimensions of Constacyclic Codes over Square-Free Affine Algebras**

A shorter alternative, if the bivariate result is emphasized, is:

> **Joint Enumeration of Code and `k`-Galois Hull Dimensions for Constacyclic Codes over Square-Free Affine Algebras**

The actual framework uses factor orbits, transfer matrices, and generating functions. A genuine Burnside/Pólya equivalence-class construction is only optional and is not assumed in the main theorem.

### Correction B — the second-slot convention fixes the main exponent

On `K_s`, write

\[
\sigma_{s,k}(a)=a^{p^k}.
\]

The inner product used throughout is

\[
\langle x,y\rangle_{s,k}=\sum_i x_i\sigma_{s,k}(y_i).
\]

Accordingly, the main normalized reciprocal and dual-generator formulas below use `\sigma_{s,k}` and the root action is `\alpha\mapsto\alpha^{-p^k}`. The same-twist compatibility condition is `\lambda_s^{1+p^k}=1`.

For comparison only, one may write `\rho_s=\sigma_{s,k}^{-1}` on `K_s`; if `r_s\equiv-k\pmod{em_s}`, then `\rho_s=p^{r_s}`. That inverse notation belongs to the alternative convention and is not used in the principal formulas. This distinction is essential when `\sigma_{s,k}\ne\rho_s`, as in the N2 validation obligation.

### Correction C — the factor permutation is explicit under `p^k`

For a monic factor

\[
f(x)=\sum_{i=0}^{d}f_i x^i,
\qquad f_0\ne0,
\]

define the normalized `k`-Galois reciprocal over `K_s` by

\[
f^{\#_{s,k}}(x)
=f_0^{-p^k}\sum_{i=0}^{d}f_i^{p^k}x^{d-i}.
\tag{0.1}
\]

Then

\[
\tau_{s,k}(f):=f^{\#_{s,k}}
\]

has root action

\[
\alpha\longmapsto\alpha^{-p^k}.
\]

The compatibility condition for the same constacyclic polynomial is

\[
\lambda_s^{1+p^k}=1.
\tag{0.2}
\]

Under (0.2), `tau` maps the factor set to itself. It is a permutation, but it is **not assumed to be an involution**. General orbit lengths are allowed.

### Source theorem references and scope

The published finite-field source and its correction use inverse/first-slot notation in some displayed formulas (including a `p^{e-k}` exponent); that notation is not copied into the principal theorem. The source paper is cited using its final published version: I. Debnath, H. Islam, E. Martínez-Moro, and O. Prakash, “Galois hulls of constacyclic codes over affine algebra rings,” *Discrete Mathematics* 349 (2026), Article 114750, DOI 10.1016/j.disc.2025.114750. The arXiv version is retained only as an openly accessible prepublication record.

The relevant source labels are: Section 2.2, Lemma 1 for the finite-field dual twist; Section 2.2, Theorem 1 for the finite-field dual generator and lcm hull generator; Section 2.3, Theorems 2 and 3 for componentwise constacyclic decomposition and generators; and Section 3, Theorems 4 and 5 for the affine-algebra dual twist and component generator. Those source statements must be checked against the final published text before citation in the manuscript. The present blueprint uses the second-slot convention above and therefore requires a direct proof of the displayed `p^k` version rather than silently importing a differently normalized source formula.

### Correction D — the support set is fixed by derivation

With the convention `tau(f)=f^{#}`, the component hull support is

\[
(\mathcal F_s\setminus J_s)\cap\tau_{s,k}(J_s),
\tag{0.3}
\]

not an arbitrarily chosen inverse-image variant. The reason is derived in Section 4 below from the lcm of the generator and the dual generator.

### Correction E — boundary orientation is fixed

Let `tau(f_i)=f_{i+1}`. A factor `f_{i+1}` contributes to the hull exactly when

\[
\varepsilon_i=1,
\qquad \varepsilon_{i+1}=0.
\]

Thus the convention used throughout the revised blueprint is

\[
b_O(\varepsilon)
=\sum_{i=0}^{a-1}\varepsilon_i(1-\varepsilon_{i+1}),
\qquad \varepsilon_a=\varepsilon_0.
\tag{0.4}
\]

This counts `1 -> 0` transitions. The number of `0 -> 1` transitions is equal on a cyclic binary word, but the paper will not switch orientation silently.

### Correction F — the explicit orbit polynomial was checked

The formula

\[
P_{a,w}(z)=2+
\sum_{b=1}^{\lfloor a/2\rfloor}
\frac{a}{b}\binom{a-1}{2b-1}z^{bw}
\tag{0.5}
\]

is correct for the cyclic `1 -> 0` boundary statistic. Direct checks give:

\[
\begin{aligned}
P_{1,w}(z)&=2,\\
P_{2,w}(z)&=2+2z^w,\\
P_{3,w}(z)&=2+6z^w,\\
P_{4,w}(z)&=2+12z^w+2z^{2w},\\
P_{5,w}(z)&=2+20z^w+10z^{2w}.
\end{aligned}
\]

These agree with direct enumeration of all `2^a` binary words. The derivation is given in Section 6.

### Correction G — moments are derived, including the `a=2` exception

For an orbit of length `a=1`, the boundary indicator is identically zero. For `a=2`, the two cyclic transition indicators are mutually exclusive, so the variance is `1/4`, not `a/16=1/8`. For `a>=3`, the variance is `a/16`. The corrected formulas are in Section 8.

### Correction H — the pilot example was actually verified

The script `code/validate_pilot.py` performs an independent dependency-free computation over `F_4` and checks:

1. factorization of `x^5-1`;
2. the Hermitian factor action;
3. all component factor selections;
4. direct hull dimensions;
5. the four-component ring histogram.

It returns `PASS`, with the distribution

\[
256+1024z^2+1536z^4+1024z^6+256z^8.
\]

The complete verification is recorded in Section 10.

The existing `F_4` setup and its numerical conclusions are retained. The only change to its exposition is the correction that the code-dimension transfer matrix is the unselected-factor matrix in Section 7.

### Correction H2 — independent long-orbit and extension-field validations were added

The existing script `code/validate_long_orbit_examples.py` verifies:

- a genuine `k=1` example over `F_8` with a `tau`-orbit of length `6`;
- an `F_{16}=F_{4^2}` component with `m_s=2` and a `tau`-orbit of length `4`;
- direct hull dimensions, orbit-boundary histograms, and transfer-matrix enumerators.

All three computations agree in both examples.

### Correction I — complexity wording was weakened

The transfer-matrix method avoids enumerating all factor selections, but no unsupported “polynomial-time” claim is made. The actual arithmetic cost depends on factorization, orbit lengths, truncation degrees, coefficient representation, and polynomial multiplication. A cautious estimate is given in Section 13.

### Correction J — Burnside and quantum sections are secondary

Burnside’s lemma is retained only conditionally, with a precise group-action requirement. The quantum section is an application plan only; no quantum parameter is inferred from hull dimension alone.

### Correction K — the original transfer matrix tracked codimension, not code dimension

The matrix

\[
\begin{pmatrix}1&u^w\\z^w&u^w\end{pmatrix}
\]

assigns `u^w` whenever a factor is selected. Therefore its `u`-exponent is the selected-factor degree, namely the **codimension** of the component code, not the code dimension stated in the original definition of `E(u,z)`.

The corrected code-dimension matrix assigns `u^w` to an unselected factor:

\[
T_w(u,z)=
\begin{pmatrix}
 u^w&1\\
 u^w z^w&1
\end{pmatrix}.
\tag{0.6}
\]

The old matrix remains useful as a codimension enumerator, but it must not be used while claiming that `u` tracks `dim(C)`. The revised theorem uses `T_w`. In the `F_4` pilot the final polynomial happens to be unchanged because the factor-degree polynomial is palindromic; the matrix interpretation is nevertheless different and must be stated correctly.

---

## 1. Research question and novelty

### What the supplied paper establishes

The supplied paper studies `k`-Galois duals and hulls of `lambda`-constacyclic codes over an affine algebra. Its main path is:

1. decompose the algebra using primitive idempotents;
2. reduce to component constacyclic codes;
3. describe dual and hull generators;
4. obtain a formula for the hull dimension of a selected code;
5. give LCD conditions and quantum-code examples.

### Research question

> For a fixed square-free affine algebra `A`, length `n`, unit `lambda`, and Galois parameter `k`, how many constacyclic codes have each possible `k`-Galois hull dimension? Can code dimension and hull dimension be enumerated jointly? Can the exact mean, variance, and LCD count be obtained from the factor action?

The proposed paper is therefore an enumerative follow-up, not a paraphrase of the original hull-generator paper.

### Main contribution package

The paper should claim the following only after proofs and computations are complete:

1. a precise factor permutation induced by the `k`-Galois reciprocal;
2. a component hull-support characterization;
3. a weighted cyclic-boundary formula for hull dimension;
4. a bivariate transfer-matrix enumerator for code and hull dimensions;
5. exact multiplicities for every hull dimension;
6. LCD count, mean, and variance as corollaries;
7. reproducible exhaustive validation for small examples.

The inequivalent-code/Burnside problem is a high-value optional extension, not a premise of the title.

[FINAL LITERATURE AUDIT REQUIRED BEFORE SUBMISSION]

The introduction must distinguish explicitly between:

- established results imported from previous literature;
- results derived in the present work;
- computational observations on finite instances;
- proposed extensions and future work.

Use cautious positioning such as: “The present work focuses on the exact joint enumeration of code dimension and `k`-Galois hull dimension through factor-orbit and transfer-matrix methods.” Do not use “first,” “no previous work,” or “completely new” without a documented literature search supporting the exact claim.

---

## 2. Fresh literature audit and comparison

### 2.1 Audit protocol and verified source scope

**Audit date:** 23 September 2026. Publisher landing pages, abstracts, metadata, and the openly accessible prepublication record for the affine-algebra paper were checked. The audit distinguishes what is explicitly stated in an abstract or publisher record from theorem-level overlap. A paywalled or incompletely exposed full text is not treated as proof that a displayed theorem is absent. Every unresolved theorem-level comparison remains **VERIFY BEFORE MANUSCRIPT FINALIZATION**.

The audited records establish the following scope statements:

| Record | Scope verified from the publisher record | Limitation of the present audit |
|---|---|---|
| Sangwisut, Jitman, Ling, and Udomkavanich, *Finite Fields and Their Applications* 33 (2015), 232–257, DOI `10.1016/j.ffa.2014.12.008` | Euclidean and Hermitian hull dimensions and fixed-hull-dimension enumerations for cyclic and negacyclic finite-field codes | The exact translation of every theorem into the present `k`-Galois and orbit notation still requires a full-text check. |
| Debnath, Prakash, and Islam, *Cryptography and Communications* 15 (2023), 111–127, DOI `10.1007/s12095-022-00591-6`, with its correction | A Galois-hull dimension formula for finite-field constacyclic codes and, under restrictions on `q`, counts for a prescribed hull dimension | The exact restrictions and whether the count is equivalent to the proposed coefficient formula require theorem-by-theorem comparison. |
| Jitman and Sangwisut, *Advances in Mathematics of Communications* 12 (2018), 451–463, DOI `10.3934/amc.2018027` | Average Hermitian-hull dimension of finite-field constacyclic codes over `F_{q^2}` and bounds | It is an average result, not evidence by itself for the affine product/joint enumerator. |
| Liu and Pan, *Designs, Codes and Cryptography* 88 (2020), 241–255, DOI `10.1007/s10623-019-00681-2` | General methods and invariance results for Galois hulls of finite-field linear codes, including matrix-product applications | It is not a constacyclic factor-selection enumeration paper. |
| Debnath, Islam, Martínez-Moro, and Prakash, *Discrete Mathematics* 349(2) (2026), Article 114750, DOI `10.1016/j.disc.2025.114750` | Square-free affine algebra, `k`-Galois dual/hull generators, a hull-dimension formula, LCD conditions, and quantum-code examples | The final article abstract does not verify an exact all-code or bivariate transfer-matrix enumerator; the complete final-text comparison is **VERIFY BEFORE MANUSCRIPT FINALIZATION**. |
| Debnath and Prakash, *Advances in Mathematics of Communications* 19(6) (2025), 1569–1604, DOI `10.3934/amc.2025010` | Average Galois-hull dimensions over finite fields and over `R_{m,q}=F_q[u]/\langle u^m-u\rangle`, with LCD constructions | The relation between its ring decomposition and the present arbitrary square-free multivariate product must be checked from the full paper. |
| Debnath, Islam, Yadav, and Prakash, *Advances in Mathematics of Communications* 22 (2026), 1–18, DOI `10.3934/amc.2025054` | Conditions for hull dimensions one and two for constacyclic codes and EAQECC applications | It does not, from the verified abstract, establish the proposed all-dimensions joint enumerator. |
| Jitman and Sangwisut, *Thai Journal of Mathematics* 18 (2020), 135–144 | Hulls of cyclic codes over `F_2+vF_2` | Publisher issue metadata is verified; DOI and complete theorem-level overlap remain **VERIFY BEFORE MANUSCRIPT FINALIZATION**. |
| Tian, Gao, and Gao, *Quantum Information Processing* 23 (2024), Article 9, DOI `10.1007/s11128-023-04230-8` | Euclidean/Hermitian hull dimensions for constacyclic codes over `F_q+vF_q`, `v^2=v`, via a Gray map, with quantum constructions | The ring is a specific two-component non-chain ring; no overlap with the full affine theorem is inferred without a full-text check. |
| Yadav, Singh, Islam, Prakash, and Solé, *Computational and Applied Mathematics* 43 (2024), Article 269, DOI `10.1007/s40314-024-02789-1` | Possible Hermitian hull dimensions, LCD conditions, and quantum applications for a specified non-chain ring over `F_{q^2}` | The setting and Hermitian specialization are narrower/different; exact enumerator overlap is not established. |
| Jitman, Sangwisut, and Udomkavanich, *Discrete Mathematics* 343 (2020), Article 111621, DOI `10.1016/j.disc.2019.111621` | Hull types, fixed-2-dimension counts, and averages for odd-length cyclic codes over `Z_4` | This is a repeated-root/ring setting, not the reduced finite-field-component theorem. |
| Dougherty and Saltürk, *Advances in Mathematics of Communications* 19(1) (2025), 11–35, DOI `10.3934/amc.2023031` | Counts of linear/additive codes over rings of order four by hull type | It is relevant to enumeration, but not verified as a constacyclic square-free affine joint enumerator. |
| Zhang, Kong, and Zheng, *Entropy* 28(4) (2026), Article 407, DOI `10.3390/e28040407` | Galois hull dimensions and quantum constructions for a specific finite non-chain ring | It is a related, later ring-specific quantum application; it does not establish the proposed general transfer theorem from the verified record. |

The source PDF supplied with the repository is retained as a local research input. Because local PDF text extraction is unavailable, its final-text theorem labels must be checked against the publisher version and the accessible prepublication record before they are cited as exact labels.

### 2.2 Clause-by-clause comparison matrix

The matrix uses only the statuses **already established**, **partially addressed**, and **introduced/developed here**. “Introduced/developed here” means that the clause is a target of this blueprint after the stated proof and full-text audit; it is not a priority claim. A cell based only on an abstract or metadata record is followed by a verification warning in the row notes.

**Clauses:** (A) structural dual/hull generator; (B) finite-field fixed-hull-dimension enumeration; (C) average or prescribed small hull dimensions; (D) square-free affine product of finite-field components; (E) arbitrary factor-orbit boundary statistic with component weights; (F) joint code-dimension/hull-dimension enumerator; (G) compatible nontrivial twists and explicit incompatible-twist boundary; (H) conditional quantum application; (I) equivalence-class enumeration.

| Audited paper or record | A | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|---|
| Sangwisut et al. (2015) | **already established** — cyclic/negacyclic finite-field hull formulas | **already established** — fixed hull dimensions in that setting | **partially addressed** — not the present Galois-average package | **introduced/developed here** — affine product is outside the verified scope | **introduced/developed here** — the present weighted orbit formulation is not verified there | **introduced/developed here** — no verified bivariate code/hull enumerator | **partially addressed** — Euclidean/Hermitian cyclic/negacyclic cases only | **partially addressed** — hull applications are background, not this affine theorem | **introduced/developed here** — no quotient by equivalence in the proposed main count |
| Debnath et al. (2023) finite-field paper | **already established** — finite-field constacyclic formula | **already established** under stated `q` restrictions — exact prescribed-dimension counts are stated in the abstract | **partially addressed** — not the present all-component moment package | **introduced/developed here** — affine product extension is not verified in that record | **partially addressed** — factor arrangements are used, but the present cyclic-boundary formulation needs comparison | **introduced/developed here** — no verified joint code/hull transfer product | **partially addressed** — finite-field constacyclic twists are treated, but the proposed compatible/incompatible diagnostic must be compared | **partially addressed** — not the main contribution of that paper | **introduced/developed here** — labeled codes only |
| Jitman–Sangwisut (2018) | **partially addressed** — Hermitian constacyclic hull setting | **partially addressed** — average, not fixed-dimension multiplicities | **already established** — average and bounds | **introduced/developed here** | **introduced/developed here** | **introduced/developed here** | **partially addressed** — Hermitian specialization | **partially addressed** — no affine transfer claim | **introduced/developed here** |
| Liu–Pan (2020) | **already established** — general Galois-hull methods | **partially addressed** — general linear-code results, not this constacyclic count | **partially addressed** — invariance/constructive results rather than this distribution | **introduced/developed here** | **introduced/developed here** | **introduced/developed here** | **partially addressed** — Galois duality is general | **partially addressed** — applications are not the present quantum section | **introduced/developed here** |
| Debnath et al. (2026) affine-algebra paper | **already established** — affine `k`-Galois dual/hull generators are its stated scope | **partially addressed** — exact hull formula is stated, but an all-code count is not verified from the abstract | **partially addressed** — LCD and examples, not the present distribution/moments | **already established** — square-free affine algebra is the source setting | **introduced/developed here** — arbitrary weighted factor-orbit boundary theorem requires full-text comparison | **introduced/developed here** — no exact bivariate transfer product verified | **partially addressed** — `lambda`-constacyclic and compatibility details require full-text comparison | **already established** — quantum examples are explicitly stated | **introduced/developed here** — source future-work language must be checked |
| Debnath–Prakash (2025) average paper | **partially addressed** | **partially addressed** | **already established** — average dimensions | **partially addressed** — a particular ring `R_{m,q}` is treated | **introduced/developed here** | **introduced/developed here** | **partially addressed** — Galois constacyclic setting | **partially addressed** — LCD constructions/examples | **introduced/developed here** |
| Debnath et al. (2026) small-hull paper | **partially addressed** | **partially addressed** — dimensions one and two only | **already established** — small-dimension existence conditions | **introduced/developed here** | **introduced/developed here** | **introduced/developed here** | **partially addressed** — finite-field constacyclic scope | **already established** — EAQECC applications | **introduced/developed here** |
| Tian–Gao–Gao (2024) | **partially addressed** — specific non-chain ring | **partially addressed** — ring-specific results, not the proposed all-code theorem | **partially addressed** | **partially addressed** — two idempotent components under a special Gray map | **introduced/developed here** | **introduced/developed here** | **partially addressed** — Euclidean/Hermitian only | **already established** — quantum constructions | **introduced/developed here** |
| Yadav et al. (2024) | **partially addressed** — Hermitian generators/conditions in a specific ring | **partially addressed** | **already established** — possible dimensions/LCD conditions in that setting | **partially addressed** — restricted non-chain ring | **introduced/developed here** | **introduced/developed here** | **partially addressed** — Hermitian specialization | **already established** — quantum applications | **introduced/developed here** |
| Jitman–Sangwisut (2020) over `F_2+vF_2` | **partially addressed** — ring-specific cyclic hulls | **partially addressed** — theorem-level fixed-type overlap requires full-text check | **partially addressed** — average/specific dimensions require full-text check | **partially addressed** — a two-idempotent ring is related but not the arbitrary affine product | **introduced/developed here** | **introduced/developed here** | **partially addressed** — Euclidean cyclic setting | **partially addressed** | **introduced/developed here** |
| Jitman–Sangwisut–Udomkavanich (2020) over `Z_4` | **already established** — cyclic hull generators | **already established** — fixed 2-dimension enumeration | **already established** — average 2-dimension | **introduced/developed here** — reduced affine-field components are different | **introduced/developed here** | **introduced/developed here** | **partially addressed** — Euclidean cyclic case | **partially addressed** | **introduced/developed here** |
| Dougherty–Saltürk (2025) | **partially addressed** — hull/type framework over order-four rings | **partially addressed** — counts by hull type, not this factor family | **partially addressed** | **introduced/developed here** | **introduced/developed here** | **introduced/developed here** | **partially addressed** — different duality settings | **partially addressed** | **introduced/developed here** |
| Zhang–Kong–Zheng (2026) | **partially addressed** — specific finite non-chain ring | **partially addressed** | **partially addressed** | **introduced/developed here** | **introduced/developed here** | **introduced/developed here** | **partially addressed** — Galois ring-specific scope | **already established** — quantum applications | **introduced/developed here** |

**Matrix interpretation and contribution boundary.** The verified overlap is substantial: finite-field cyclic/negacyclic and constacyclic papers already establish hull formulas and, in several settings, fixed-dimension counts; average and small-hull papers already establish statistical or restricted-dimension results; and affine/non-chain-ring papers already establish structural hull formulas and quantum applications. Therefore the manuscript must not claim priority for exact hull-dimension enumeration in coding theory. The defensible contribution, subject to the unresolved full-text checks, is narrower: prove and validate the explicitly stated square-free affine **product** theorem and its **joint code-dimension/hull-dimension transfer enumerator**, while identifying precisely which finite-field cases reduce to established results. If an audited source already contains the same product or joint enumerator, this contribution statement must be downgraded and the manuscript redesigned.

### 2.3 Title review

The retained title is:

> **Exact Enumeration of `k`-Galois Hull Dimensions of Constacyclic Codes over Square-Free Affine Algebras**

It accurately names the object being counted, the code family, and the reduced-algebra scope. It does not claim priority, a quantum-code advance, or an equivalence-class count. It is acceptable only if the main theorem really gives coefficient-level multiplicities under (H1)–(H9). If the final audit shows that the product enumerator is already published, use the title only for a rigorously distinct extension or replace it with a narrower theorem title.

A bivariate alternative is:

> **Joint Enumeration of Code and `k`-Galois Hull Dimensions for Constacyclic Codes over Square-Free Affine Algebras**

The paper should choose between these titles only after the theorem and comparison audit are complete.

### 2.4 Current positioning

Do not position the proposed paper merely as:

- another ring-specific hull formula;
- an average-dimension calculation only;
- a table of quantum-code parameters;
- a repeated statement of a dual-generator formula.

The safe positioning sentence is: “The present work focuses on a proved, coefficient-level joint enumeration of code dimension and `k`-Galois hull dimension for labeled constacyclic factor selections over square-free affine algebras, conditional on the comparison audit described above.”

---

## 3. Rigorous mathematical setting

### 3.1 Affine algebra

Let

\[
q=p^e,
\qquad 0\le k<e,
\]

and

\[
A=\mathbb F_q[X_1,\ldots,X_\ell]
 /\langle t_1(X_1),\ldots,t_\ell(X_\ell)\rangle,
\]

where each `t_i` is monic and square-free over `F_q`.

Because the quotient is finite, commutative, and reduced, it decomposes as

\[
A\cong \prod_{s=1}^{N}K_s,
\qquad K_s\cong\mathbb F_{q^{m_s}}.
\tag{3.1}
\]

Let `e_s` denote the primitive orthogonal idempotent corresponding to `K_s`.

### 3.2 The Galois inner product on each component

On `K_s^n`, use

\[
\langle x,y\rangle_{s,k}
=\sum_{i=0}^{n-1}x_i y_i^{p^k}.
\tag{3.2}
\]

The map

\[
\sigma_{s,k}:K_s\to K_s,
\qquad a\mapsto a^{p^k}
\]

is an automorphism. The main reciprocal and dual-generator formulas use `\sigma_{s,k}`, not its inverse. The inverse `\rho_s=\sigma_{s,k}^{-1}` may be introduced only in an alternative-convention remark.

### 3.3 Constacyclic polynomial

Let

\[
\lambda=(\lambda_1,\ldots,\lambda_N)\in A^\times,
\qquad \lambda_s\in K_s^\times.
\]

For the main theorem assume `n\ge1`,

\[
\gcd(n,p)=1
\tag{3.4}
\]

and the same-twist compatibility condition

\[
\lambda_s^{1+p^k}=1
\qquad (1\le s\le N).
\tag{3.5}
\]

Define

\[
M_s(x)=x^n-\lambda_s.
\]

Since `p` does not divide `n` and `lambda_s` is nonzero,

\[
\gcd(M_s,M_s')=1,
\]

so `M_s` is square-free.

Factor it over `K_s` as

\[
M_s(x)=\prod_{f\in\mathcal F_s}f(x),
\tag{3.6}
\]

where `F_s` is the set of distinct monic irreducible factors.

### 3.4 Component codes

The polynomial CRT gives

\[
A[x]/\langle x^n-\lambda\rangle
\cong
\prod_{s=1}^{N}K_s[x]/\langle M_s(x)\rangle.
\tag{3.7}
\]

A `lambda`-constacyclic `A`-code is therefore a tuple of ideals `C_s` in the component quotients.

For `J_s subseteq F_s`, define

\[
g_{J_s}(x)=\prod_{f\in J_s}f(x),
\qquad
C_s(J_s)=\langle g_{J_s}(x)\rangle.
\tag{3.8}
\]

Every component ideal has exactly one such factor-selection set. Therefore

\[
|\mathscr C(A,n,\lambda)|
=2^{\sum_s|\mathcal F_s|}.
\tag{3.9}
\]

The component dimensions are

\[
\dim_{K_s}C_s(J_s)
=n-\sum_{f\in J_s}\deg_{K_s}f,
\tag{3.10}
\]

and

\[
\dim_{\mathbb F_q}C
=\sum_s m_s\dim_{K_s}C_s.
\tag{3.11}
\]

### 3.5 Why square-free is a main hypothesis

Square-free `t_i` are assumed so that the affine algebra is reduced. Over the perfect field `\mathbb F_q`, the resulting finite reduced algebra is a product of finite fields, and primitive idempotents give independent component codes. The additional condition `\gcd(n,p)=1` makes every `x^n-\lambda_s` square-free because its derivative is `n x^{n-1}` and each root is nonzero. Consequently, every component ideal is represented by a subset of distinct irreducible factors.

In repeated-root cases, nilpotents and factor multiplicities appear. Ideals need not be classified by binary factor inclusion alone, the lcm support must be replaced by multiplicity data, and the binary orbit-boundary model is not valid without a separate repeated-root theory. Repeated-root cases are future work.

---

### 3.6 Collected hypotheses for the principal enumeration theorem

No essential assumption is hidden in later sections. The principal theorem is a formal proof target under all of the following hypotheses:

(H1) `q=p^e` is a prime power and `0\le k<e`;

(H2) `A=\mathbb F_q[X_1,\ldots,X_\ell]/\langle t_1(X_1),\ldots,t_\ell(X_\ell)\rangle`, with each `t_i` monic and square-free;

(H3) the square-free affine algebra decomposes as `A\cong\prod_{s=1}^N K_s`, where `K_s=\mathbb F_{q^{m_s}}`;

(H4) `n\ge1` and `\gcd(n,p)=1`;

(H5) `\lambda\in A^\times` with components `\lambda_s\in K_s^\times`;

(H6) every component satisfies `\lambda_s^{1+p^k}=1`;

(H7) `M_s(x)=x^n-\lambda_s` is factored into distinct monic irreducibles `\mathcal F_s`;

(H8) the codes counted are exactly the distinct factor-selection ideals indexed by subsets `J_s\subseteq\mathcal F_s`, with no quotient by an equivalence or isometry group;

(H9) dimensions are reported over `K_s` componentwise and over `\mathbb F_q` globally, with weight `w_O=m_s d_O`.

Under (H1)–(H9), the proof must establish the factor permutation, dual-generator identity, hull-support formula, boundary formula, transfer-matrix product, total count, exact distribution, LCD count, and moment formulas.

### 3.7 Compatible and incompatible twists

The compatible case is precisely (H6). Then the root action `\alpha\mapsto\alpha^{-p^k}` preserves the roots of `x^n-\lambda_s`, so the factor permutation and the main enumerator are defined.

If `\lambda_s^{1+p^k}\ne1`, the component `k`-Galois dual is a `\lambda_s^{-p^k}`-constacyclic code rather than a `\lambda_s`-constacyclic code. Its factors belong to a different modulus in general, so the same-factor-set orbit enumerator is not valid. This case is retained only as a diagnostic and as future work for a two-modulus/bipartite theory.

## 4. Definition and proof of the factor permutation

### 4.1 Normalized `k`-Galois reciprocal

For a monic polynomial

\[
f(x)=\sum_{i=0}^{d}f_i x^i\in K_s[x],
\qquad f_0\ne0,
\]

define

\[
f^{\#_{s,k}}(x)
=f_0^{-p^k}\sum_{i=0}^{d}f_i^{p^k}x^{d-i},
\tag{4.1}
\]

This polynomial is monic. On monic polynomials with nonzero constant term, the operation is multiplicative:

\[
(fg)^{\#_{s,k}}
=f^{\#_{s,k}}g^{\#_{s,k}}.
\tag{4.2}
\]

The operation preserves irreducibility because it is the composition of a field automorphism on coefficients with reciprocal reversal. It also preserves degree, so every `tau`-orbit consists of factors of one common degree.

### 4.2 Definition of `tau`

Define

\[
\boxed{
\tau_{s,k}:\mathcal F_s\to\mathcal F_s,
\qquad
\tau_{s,k}(f)=f^{\#_{s,k}}.
}
\tag{4.3}
\]

We now prove that the codomain really is `F_s`.

Let `alpha` be a root of `f`. The roots of `f^{#_{s,k}}` are

\[
\alpha^{-p^k}.
\]

Since `alpha^n=lambda_s`,

\[
(\alpha^{-p^k})^n
=\lambda_s^{-p^k}
=\lambda_s
\]

by (3.5). Thus every root of `f^{#_{s,k}}` is a root of `M_s`; hence

\[
\tau_{s,k}(\mathcal F_s)\subseteq\mathcal F_s.
\]

The operation is invertible, so the inclusion is equality:

\[
\boxed{\tau_{s,k}(\mathcal F_s)=\mathcal F_s.}
\tag{4.4}
\]

Thus `tau_{s,k}` is a permutation of the finite factor set.

### 4.3 `tau` need not be an involution

Do not assume `tau^2=id` in the general `k`-Galois case. On roots, repeated application uses

\[
\alpha\longmapsto \alpha^{-p^k}
\longmapsto \alpha^{p^{2k}}
\longmapsto\cdots,
\]

up to the factor identification by the `K_s`-Frobenius action. The resulting permutation can have orbit lengths larger than two.

Special cases:

- `k=0`: `p^k=1`, so this becomes the ordinary reciprocal map and is an involution.
- If the chosen Galois automorphism has order two on `K_s`, the corresponding Hermitian-type operation is also an involution.
- These are special cases only; the main theorem allows arbitrary finite orbit lengths.

Let

\[
O=(f_0,f_1,\ldots,f_{a_O-1})
\]

be a `tau_{s,k}`-orbit, indexed so that

\[
\tau_{s,k}(f_i)=f_{i+1\pmod {a_O}}.
\tag{4.5}
\]

All factors in one orbit have the same degree. Set

\[
d_O=\deg_{K_s}f_i,
\qquad
w_O=m_s d_O.
\tag{4.6}
\]

The weight `w_O` is the contribution measured over `F_q`.

---

## 5. Component dual and hull support — rigorous derivation

**Source scope note.** The finite-field dual-generator/lcm statement is Theorem 1 in Section 2.2 of Debnath–Prakash–Islam (2023), and the affine component generator statement is Theorem 5 of the 2026 affine-algebra paper. The component-field version below must be proved under the convention audit; it is not accepted merely by citation.


Fix one component `s` and omit the subscript `s` temporarily.

Let

\[
M(x)=\prod_{f\in\mathcal F}f(x),
\qquad
g_J(x)=\prod_{f\in J}f(x),
\qquad
h_J(x)=\frac{M(x)}{g_J(x)}
=\prod_{f\in\mathcal F\setminus J}f(x).
\]

Because `M` is square-free, `g_J` and `h_J` are coprime and all factor selections are unambiguous.

### Lemma 5.1 — dual factor support

Under the component inner product (3.2), the `k`-Galois dual of `C(J)=<g_J>` is generated by

\[
 h_J^{\#_{s,k}}.
\tag{5.1}
\]

By multiplicativity of `#`, its factor support is

\[
\operatorname{Supp}(h_J^{\#_{s,k}})
=\tau_{s,k}(\mathcal F\setminus J).
\tag{5.2}
\]

This is the component-field version of the standard constacyclic dual-generator calculation; the displayed reciprocal uses the second-slot exponent `p^k` from the convention audit. Any inverse-semilinear notation belongs only to the explicitly labeled alternative-convention remark.

### Lemma 5.2 — intersection/lcm support

In `K_s[x]/<M>`, the intersection of the ideals generated by `g_J` and `h_J^{#}` is generated by their least common multiple:

\[
\operatorname{Hull}_k(C(J))
=\langle\operatorname{lcm}(g_J,h_J^{\#_{s,k}})\rangle.
\tag{5.3}
\]

The factor support of this lcm is

\[
J\cup\tau_{s,k}(\mathcal F\setminus J).
\]

Therefore the factors omitted from the lcm are

\[
\begin{aligned}
\mathcal F\setminus
\bigl(J\cup\tau_{s,k}(\mathcal F\setminus J)\bigr)
&=(\mathcal F\setminus J)
\cap\bigl(\mathcal F\setminus\tau_{s,k}(\mathcal F\setminus J)\bigr)\\
&=(\mathcal F\setminus J)\cap\tau_{s,k}(J).
\end{aligned}
\tag{5.4}
\]

The second equality uses that `tau` is a bijection of `F`.

### Theorem 5.3 — component hull dimension

For `J_s subseteq F_s`,

\[
\boxed{
\dim_{K_s}\operatorname{Hull}_k(C_s(J_s))
=
\sum_{f\in
(\mathcal F_s\setminus J_s)\cap\tau_{s,k}(J_s)}
\deg_{K_s}f.
}
\tag{5.5}
\]

The ring-code version is obtained by multiplying the `s`-component dimension by `m_s` and summing:

\[
\dim_{\mathbb F_q}\operatorname{Hull}_k(C)
=
\sum_s m_s\dim_{K_s}\operatorname{Hull}_k(C_s).
\tag{5.6}
\]

This derivation fixes the `tau` versus `tau^{-1}` ambiguity. With the definition `tau(f)=f^{#}`, the correct support is (5.5). If a paper defines its factor permutation as the inverse map instead, the inverse appears in the notation; the mathematics is the same only after that redefinition.

**Proof obligations.** The manuscript must provide complete proofs, not computational substitutions, for the normalized reciprocal properties; `\tau_{s,k}(\mathcal F_s)=\mathcal F_s`; the identity `C_s(J_s)^{\perp_k}=\langle h_{J_s}^{\#_{s,k}}\rangle`; the lcm intersection; (5.5); and the passage from component `K_s`-dimension to global `\mathbb F_q`-dimension.

---

## 6. Orbit boundary statistic

Fix an orbit

\[
O=(f_0,\ldots,f_{a-1}),
\qquad \tau(f_i)=f_{i+1}.
\]

For a selected factor set `J`, define

\[
\varepsilon_i=
\begin{cases}
1,&f_i\in J,\\
0,&f_i\notin J.
\end{cases}
\]

The factor `f_{i+1}` belongs to the component hull support (5.4) exactly when

- `f_i` is selected, so `epsilon_i=1`; and
- `f_{i+1}` is not selected, so `epsilon_{i+1}=0`.

Therefore define

\[
\boxed{
 b_O(\varepsilon)
=\sum_{i=0}^{a-1}
\varepsilon_i(1-\varepsilon_{i+1}),
\qquad \varepsilon_a=\varepsilon_0.
}
\tag{6.1}
\]

This counts the number of `1 -> 0` transitions. Because every factor in `O` has degree `d_O`, the orbit contribution to the `F_q`-dimension of the hull is

\[
 w_O b_O(\varepsilon),
\qquad w_O=m_s d_O.
\tag{6.2}
\]

Summing over all components and all orbits gives the rigorously derived global formula:

\[
\boxed{
\dim_{\mathbb F_q}\operatorname{Hull}_k(C)
=\sum_{s=1}^{N}\sum_{O\in\mathcal O_s}
 w_O b_O(\varepsilon_O).
}
\tag{6.3}
\]

A convention using `0 -> 1`, namely `sum_i(1-epsilon_i)epsilon_{i+1}`, gives the same numerical count on a cyclic binary word, but (6.1) is the convention tied directly to the support set (5.4) and will be used everywhere.

---

## 7. Transfer matrix and joint enumerator

### 7.1 One-orbit matrix for the actual code dimension

For an orbit of length `a` and weight `w`, if `epsilon_i=1`, the factor is selected in the generator polynomial and therefore contributes zero to the code dimension. If `epsilon_i=0`, the factor is not selected and contributes `w` to the code dimension. Hence the exponent of `u` below tracks `dim_{F_q}(C)`, not the codimension, while the exponent of `z` tracks `dim_{F_q}(Hull_k(C))`.

Thus, for a transition from state `r=epsilon_i` to state `t=epsilon_{i+1}`, assign:

- `u^w` if the destination factor is unselected (`t=0`);
- `z^w` if the transition is `1 -> 0`, because that destination factor is in the hull support.

The correct code-dimension transition weight is

\[
T_w(u,z)_{r,t}
=u^{w(1-t)}z^{wr(1-t)}.
\]

With rows and columns indexed by `0,1`, this is

\[
\boxed{
T_w(u,z)=
\begin{pmatrix}
 u^w & 1\\
 u^w z^w & 1
\end{pmatrix}.
}
\tag{7.1}
\]

The four transitions are:

| transition | code-dimension/hull weight |
|---|---:|
| `0 -> 0` | `u^w` |
| `0 -> 1` | `1` |
| `1 -> 0` | `u^w z^w` |
| `1 -> 1` | `1` |

For comparison, the matrix

\[
T_w^{\mathrm{codim}}(u,z)=
\begin{pmatrix}
1&u^w\z^w&u^w
\end{pmatrix}
\tag{7.2}
\]

is also valid, but its `u`-exponent tracks the selected-factor degree, i.e. the `F_q`-codimension of the code. If `L=n\dim_{\mathbb F_q}A` is the ambient length over `F_q`, then the corresponding global enumerators satisfy

\[
\mathscr E_{\mathrm{dim}}(u,z)
=u^L\mathscr E_{\mathrm{codim}}(u^{-1},z).
\]

It must not be called a code-dimension enumerator without this substitution and ambient-dimension shift. The revised paper uses `T_w` for `\dim_q(C)`.

For a cyclic binary word `(epsilon_0,...,epsilon_{a-1})`, the product

\[
\prod_{i=0}^{a-1}
T_w(u,z)_{\varepsilon_i,\varepsilon_{i+1}}
\]

is exactly

\[
 u^{w\sum_i(1-\varepsilon_i)}
 z^{w\sum_i\varepsilon_i(1-\varepsilon_{i+1})}.
\tag{7.3}
\]

The first exponent is the component code-dimension contribution; the second is the hull contribution.

### 7.2 Why the trace is required

The matrix product `(T_w^a)_{r,r}` sums all length-`a` walks that start at state `r` and return to the same state. Summing over `r=0,1` closes the binary word around the orbit:

\[
\operatorname{tr}(T_w(u,z)^a)
=\sum_{\varepsilon_0,\ldots,\varepsilon_{a-1}\in\{0,1\}}
 u^{w\sum_i(1-\varepsilon_i)}
 z^{w b_O(\varepsilon)}.
\tag{7.4}
\]

Without the trace, the edge from `epsilon_{a-1}` back to `epsilon_0` would be omitted, so open binary strings would be counted instead of cyclic selections.

### 7.3 Principal transfer-matrix theorem and total count

The principal theorem is a formal proof target under (H1)–(H9), not an already established general theorem. Define

\[
\mathscr E(u,z)
=\sum_{C\in\mathscr C(A,n,\lambda)}
 u^{\dim_{\mathbb F_q}C}
 z^{\dim_{\mathbb F_q}\operatorname{Hull}_k(C)}.
\tag{7.5}
\]

The trace identity (7.4) must be proved first. It follows by expanding matrix products over closed walks and assigning the destination-factor weight to each transition. Therefore the target joint enumerator is

\[
\boxed{
\mathscr E(u,z)
=\prod_{s=1}^{N}
 \prod_{O\in\mathcal O_s}
 \operatorname{tr}\bigl(T_{w_O}(u,z)^{a_O}\bigr).
}
\tag{7.6}
\]

Here `T_w` is exactly the matrix in (7.1), with rows and columns indexed by the binary selection state. The formula counts labeled factor-selection codes, not equivalence classes.

#### Total-code-count theorem

Under (H1)–(H9), the map from the tuple of subsets `(J_1,\ldots,J_N)` to the corresponding component/product ideal is a bijection. Hence

\[
\boxed{
|\mathscr C(A,n,\lambda)|=2^{\sum_s|\mathcal F_s|}.
}
\tag{7.7}
\]

The generating-function sanity check is

\[
\boxed{
\mathscr E(1,1)=2^{\sum_s|\mathcal F_s|}.
}
\tag{7.8}
\]

Equivalently, the sum of all coefficients in the joint distribution is the total number of distinct codes. This identity is asserted only under the binary factor-selection hypotheses; it is not a statement about repeated-root ideals or quotient-by-equivalence counts.

Setting `z=1` gives

\[
\mathscr E(u,1)=\prod_s\prod_{f\in\mathcal F_s}(1+u^{m_s\deg f}),
\tag{7.9}
\]

which independently checks the code-dimension marginal. Setting `u=1` gives the hull-distribution polynomial in Section 8.

#### Why transfer matrices avoid direct code enumeration

Direct enumeration tests all `2^{\sum_s|\mathcal F_s|}` factor selections. The transfer method instead factors the calculation by `\tau`-orbits and computes one `2\times2` polynomial-matrix power per orbit, followed by polynomial products. Factorization of every `M_s` and coefficient extraction are still required, and the cost depends on factorization, orbit lengths, weights, truncation, and polynomial arithmetic. No unconditional polynomial-time claim is made.

This is a transfer-matrix theorem over labeled factor orbits, not an equivalence-class count.

---

## 8. Exact orbit polynomial and hull distribution

### 8.1 Derivation and integrality of the orbit polynomial

Set `u=1`. For a cyclic binary word of length `a`, let `b` be the number of `1\to0` transitions. If `b=0`, the word is constant and there are two words. If `b\ge1`, there are `2b` transition positions. Choosing those positions on the indexed cycle and choosing which alternating boundary direction is `1\to0` gives

\[
N(a,b)=2\binom{a}{2b}.
\tag{8.1}
\]

Equivalently, the run-composition argument gives

\[
N(a,b)=\frac{a}{b}\binom{a-1}{2b-1}
=2\binom{a}{2b}\in\mathbb Z,
\qquad 1\le b\le\left\lfloor\frac a2\right\rfloor.
\tag{8.2}
\]

The second equality is the explicit integrality proof: `\binom{a}{2b}=\frac{a}{2b}\binom{a-1}{2b-1}`. Thus

\[
\boxed{
P_{a,w}(z)=2+\sum_{b=1}^{\lfloor a/2\rfloor}2\binom{a}{2b}z^{bw}.
}
\tag{8.3}
\]

This is the same validated formula as the composition form. At `z=1`, `P_{a,w}(1)=2^a` by the binomial identity.

### 8.2 Independent small-orbit checks

Directly listing all binary words gives:

| orbit length | boundary counts | orbit polynomial |
|---:|---|---|
| `1` | `0: 2` | `P_{1,w}=2` |
| `2` | `0: 2, 1: 2` | `P_{2,w}=2+2z^w` |
| `3` | `0: 2, 1: 6` | `P_{3,w}=2+6z^w` |
| `4` | `0: 2, 1: 12, 2: 2` | `P_{4,w}=2+12z^w+2z^{2w}` |
| `5` | `0: 2, 1: 20, 2: 10` | `P_{5,w}=2+20z^w+10z^{2w}` |

The coefficient sums are `2,4,8,16,32`, respectively. These cases are also checked by the transfer matrix and by direct enumeration in the validation methodology.

### 8.3 Exact hull-dimension distribution

Under the square-free and compatible-twist hypotheses, define

\[
H_{A,n,\lambda,k}(z)
=\mathscr E(1,z)
=\sum_C z^{\dim_{\mathbb F_q}\operatorname{Hull}_k(C)}.
\tag{8.4}
\]

Then

\[
\boxed{
H_{A,n,\lambda,k}(z)
=\prod_{s=1}^{N}\prod_{O\in\mathcal O_s}P_{a_O,w_O}(z).
}
\tag{8.5}
\]

The exact number of codes with hull dimension `h` is

\[
\boxed{
N_h=[z^h]H_{A,n,\lambda,k}(z).
}
\tag{8.6}
\]

This coefficient theorem, rather than a list of possible dimensions only, is the central enumerative result.

---

## 9. LCD count, mean, and variance

### 9.1 Uniform probability model

Unless otherwise stated, a random `\lambda`-constacyclic code is selected uniformly from the finite set `\mathscr C(A,n,\lambda)` of all distinct codes under (H1)–(H9). The factor-selection bijection makes every factor indicator an independent Bernoulli random variable with parameter `1/2`. Consequently, the random contributions of distinct factor orbits are independent. They are not necessarily identically distributed because orbit lengths, component degrees, and orbit weights may differ.

All expectations and variances below refer to this uniform code-selection model. The notation `\dim_q` means `\dim_{\mathbb F_q}`; component dimensions are written `\dim_{K_s}`.

### 9.2 LCD count as a corollary

All weights `w_O` are positive. Hence (6.3) gives

\[
\operatorname{Hull}_k(C)=0
\iff b_O(\varepsilon_O)=0
\quad\text{for every orbit }O.
\]

A cyclic binary word has zero `1 -> 0` transitions if and only if it is constant. Therefore every orbit has exactly two admissible selections:

- all factors unselected;
- all factors selected.

Thus, under hypotheses (3.1)–(3.5),

\[
\boxed{
\#\{C:\operatorname{Hull}_k(C)=0\}
=2^{\sum_s|\mathcal O_s|}.
}
\tag{9.1}
\]

This is a corollary of the support/boundary theorem, not an independent assumption.

### 9.3 Indicator-variable calculation

For one orbit of length `a`, let

\[
X_i=\varepsilon_i(1-\varepsilon_{i+1}),
\qquad B=\sum_{i=0}^{a-1}X_i.
\]

#### Fixed orbit: `a=1`

Here `X_0=epsilon_0(1-epsilon_0)=0`, so

\[
\mathbb E[B]=0,
\qquad \operatorname{Var}(B)=0.
\tag{9.2}
\]

Fixed-point orbits contribute zero to both mean and variance.

#### Orbit length `a>=2`: mean

Each `X_i` requires two distinct independent bits, so

\[
\mathbb E[X_i]=\frac14,
\qquad
\mathbb E[B]=\frac a4.
\tag{9.3}
\]

#### Orbit length `a=2`: variance

The two indicators are

\[
X_0=\varepsilon_0(1-\varepsilon_1),
\qquad
X_1=\varepsilon_1(1-\varepsilon_0).
\]

They are mutually exclusive. Thus `B` is `0` for `00,11` and `1` for `10,01`, each with probability `1/2`. Therefore

\[
\operatorname{Var}(B)=\frac14.
\tag{9.4}
\]

#### Orbit length `a>=3`: variance

Each indicator has

\[
\operatorname{Var}(X_i)=\frac14-\frac1{16}=\frac3{16}.
\]

For neighboring directed edges, `X_i X_{i+1}=0`, hence

\[
\operatorname{Cov}(X_i,X_{i+1})=-\frac1{16}.
\]

For non-neighboring edges, the involved bits are disjoint and the covariance is zero. On a cycle of length `a>=3` there are `a` neighboring unordered pairs. Hence

\[
\begin{aligned}
\operatorname{Var}(B)
&=a\frac3{16}+2a\left(-\frac1{16}\right)\\
&=\frac a{16}.
\end{aligned}
\tag{9.5}
\]

### 9.4 Global moments

Under the square-free and compatible-twist hypotheses, different factor orbits use independent selection bits. Therefore:

\[
\boxed{
\mathbb E\bigl[\dim_{\mathbb F_q}\operatorname{Hull}_k(C)\bigr]
=\sum_{s,O:\,a_O\ge2}\frac{a_Ow_O}{4}.
}
\tag{9.6}
\]

and

\[
\boxed{
\operatorname{Var}\bigl(\dim_{\mathbb F_q}\operatorname{Hull}_k(C)\bigr)
=\sum_{s,O:\,a_O=2}\frac{w_O^2}{4}
+\sum_{s,O:\,a_O\ge3}\frac{a_Ow_O^2}{16}.
}
\tag{9.7}
\]

These formulas can also be checked by differentiating `H(z)/H(1)` at `z=1`; the indicator proof explains the exceptional `a=2` term.

---

## 10. Pilot example — computationally validated

### 10.1 Ring decomposition

Take

\[
A=\mathbb F_4[u,v]/\langle u^2-u,v^2-v\rangle.
\]

Both polynomials split into distinct linear factors over `F_4`, so

\[
A\cong\mathbb F_4^4.
\]

Thus `N=4` and `m_s=1` for every component.

Choose

\[
n=5,
\qquad \lambda=1,
\qquad q=4=2^2,
\qquad k=1.
\]

The principal second-slot exponent is

\[
p^k=2.
\]

### 10.2 Factorization over `F_4`

Let `omega` satisfy

\[
\omega^2+\omega+1=0.
\]

In characteristic two,

\[
x^5-1=x^5+1
\]

and direct factorization gives

\[
\boxed{
 x^5-1
=(x+1)(x^2+\omega x+1)(x^2+(\omega+1)x+1).
}
\tag{10.1}
\]

The two quadratic factors are irreducible over `F_4` and the factorization is square-free.

### 10.3 Explicit Hermitian factor action

For

\[
f_1=x^2+\omega x+1,
\qquad
f_2=x^2+(\omega+1)x+1,
\]

formula (4.1) with exponent `p^k=2` gives

\[
f_1^{\#}=x^2+\omega^2x+1
=x^2+(\omega+1)x+1=f_2,
\]

and similarly

\[
f_2^{\#}=f_1.
\]

Also

\[
(x+1)^{\#}=x+1.
\]

Therefore each component has exactly:

- one fixed orbit of weight `1`;
- one orbit of length `2` and weight `2`.

This action is not assumed; it is explicitly computed.

### 10.4 Component joint enumerator

Here `u` tracks **code dimension**, so an unselected factor contributes its weight and a selected factor contributes zero code-dimension weight. The fixed factor therefore contributes

\[
u+1.
\]

For the quadratic 2-cycle, the four binary selections give:

- `00`: code-dimension weight `u^4`, hull weight `1`;
- `01` and `10`: code-dimension weight `u^2`, hull weight `z^2` each;
- `11`: code-dimension weight `1`, hull weight `1`.

Thus the quadratic orbit contributes

\[
u^4+2u^2z^2+1.
\]

Therefore

\[
\boxed{
\mathscr E_{\mathrm{component}}(u,z)
=(u+1)(u^4+2u^2z^2+1).
}
\tag{10.2}
\]

This happens to equal `(1+u)(1+2u^2z^2+u^4)` because the factor-degree polynomial is palindromic in this particular example. That coincidence must not be used to justify the uncorrected matrix in general.

For four independent components:

\[
\boxed{
\mathscr E_A(u,z)
=\bigl((1+u)(1+2u^2z^2+u^4)\bigr)^4.
}
\tag{10.3}
\]

Putting `u=1` gives

\[
H_A(z)=2^8(1+z^2)^4,
\tag{10.4}
\]

so the predicted hull distribution is:

| hull dimension `h` | number of codes |
|---:|---:|
| `0` | `256` |
| `2` | `1024` |
| `4` | `1536` |
| `6` | `1024` |
| `8` | `256` |

The total is `4096=8^4`, as required because each component has three irreducible factors and hence eight ideals.

### 10.5 Independent computational verification

The repository contains:

```text
code/validate_pilot.py
```

It uses no third-party package. It implements `F_4`, polynomial arithmetic, the factor action, direct generator-row code construction, direct `k=1` hull testing, and enumeration of all four-component choices.

Run:

```bash
python code/validate_pilot.py
```

Verified output:

```text
orbit polynomial checks: a=1,...,5 PASS
factorisation: x + 1 * x^2 + (a)x + 1 * x^2 + (a+1)x + 1
Hermitian factor action: fixed linear factor; quadratic factors swapped
component joint histogram: {(0, 0): 1, (1, 0): 1, (2, 2): 2,
                           (3, 2): 2, (4, 0): 1, (5, 0): 1}
ring joint histogram terms: 65
ring hull histogram: {0: 256, 2: 1024, 4: 1536, 6: 1024, 8: 256}
PASS: direct hulls, factor action, orbit formula, and enumerator agree
```

Thus the following four objects agree in the pilot:

1. direct factorization and `tau` action;
2. direct hull calculation for every component selection;
3. the orbit-boundary formula;
4. the transfer-matrix/joint enumerator and its four-component product.

The quantum application is not needed for this validation.

### 10.6 Additional verified examples: long `tau`-orbit and `m_s>1`

The existing `F_4` pilot above is retained. The following two examples are additional validations; they do not replace or alter the original pilot.

#### Example A — a genuine non-involutory `k`-Galois orbit with `m_s=1`

Take

\[
q=8=2^3,
\qquad K=\mathbb F_8,
\qquad n=7,
\qquad \lambda=1,
\qquad k=1.
\]

Here `m_s=1`. Under the principal second-slot convention, the coefficient exponent is

\[
p^k=2.
\]

Since `F_8^*` has order `7`, `x^7-1` splits into seven distinct linear factors. If `alpha` is a primitive seventh root and

\[
f_j(x)=x-\alpha^j,
\qquad 0\le j\le6,
\]

then

\[
\tau(f_j)=f_{-2j}=f_{5j}\quad\text{(indices modulo 7)}.
\]

The factor permutation is

\[
[0,5,3,1,6,4,2],
\]

with orbits

\[
\{0\},
\qquad
\{1,5,4,6,2,3\}.
\]

Thus there is a genuine orbit of length `6`, even though `m_s=1`. This is not an Euclidean or ordinary Hermitian pair case: `q=8` has odd extension exponent `e=3` and `k=1`.

Every factor has degree `1`, so every orbit weight is `1`. The theoretical hull enumerator is

\[
H_A(z)
=P_{1,1}(z)P_{6,1}(z)
=2\bigl(2+30z+30z^2+2z^3\bigr)
=4+60z+60z^2+4z^3.
\tag{10.5}
\]

The transfer-matrix joint enumerator is

\[
\mathscr E_A(u,z)
=(u+1)
\operatorname{tr}\left(
\begin{pmatrix}u&1\\uz&1\end{pmatrix}^{6}
\right).
\tag{10.6}
\]

The direct generator-matrix computation agrees exactly with both (10.5) and (10.6):

\[
\#\{C:\dim\operatorname{Hull}_1(C)=h\}
=\begin{cases}
4,&h=0,\\
60,&h=1,\\
60,&h=2,\\
4,&h=3,\\
0,&\text{otherwise.}
\end{cases}
\]

There are `2^7=128` codes. The direct joint histogram is stored in the validator output. The mean and variance predicted by the orbit calculation are

\[
\mathbb E[h]=\frac{6}{4}=\frac32,
\qquad
\operatorname{Var}(h)=\frac{6}{16}=\frac38.
\]

The inverse-exponent convention would list the inverse permutation, but it has the same orbit lengths and the same boundary histogram. The manuscript must report the principal ordered permutation above.

#### Example B — an extension-field component with `m_s=2`

Let `omega` satisfy `omega^2+omega+1=0` over `F_4`, and take

\[
A=\mathbb F_4[u]/\langle u^2+u+\omega\rangle.
\]

The polynomial `u^2+u+omega` is irreducible over `F_4` because the absolute trace of `omega` from `F_4` to `F_2` is `1`. Therefore

\[
A\cong K=\mathbb F_{16}=\mathbb F_{4^2},
\qquad m_s=2.
\]

Choose

\[
q=4=2^2,
\qquad n=5,
\qquad \lambda=1,
\qquad k=1.
\]

The principal coefficient exponent is

\[
p^k=2.
\]

Since `5` divides `15=|F_{16}^*|`, `x^5-1` splits into five linear factors over `F_{16}`. If `alpha` is an element of order `5`, then

\[
\tau(f_j)=f_{-2j}=f_{3j}\quad\text{(indices modulo 5)}.
\]

The factor permutation is

\[
[0,3,1,4,2],
\]

with orbit lengths `1` and `4`. Every factor has `K`-degree `1`, but its `F_4`-dimension weight is

\[
w=m_s\deg_K(f)=2.
\]

Therefore

\[
H_B(z)
=P_{1,2}(z)P_{4,2}(z)
=2\bigl(2+12z^2+2z^4\bigr)
=4+24z^2+4z^4.
\tag{10.7}
\]

The transfer-matrix joint enumerator is

\[
\mathscr E_B(u,z)
=(u^2+1)
\operatorname{tr}\left(
\begin{pmatrix}u^2&1\\u^2z^2&1\end{pmatrix}^{4}
\right).
\tag{10.8}
\]

The direct computation over `F_{16}`, with dimensions converted to `F_4`-dimensions by multiplying by `m_s=2`, agrees exactly with the orbit formula and transfer matrix:

\[
\#\{C:\dim_{\mathbb F_4}\operatorname{Hull}_1(C)=h\}
=\begin{cases}
4,&h=0,\\
24,&h=2,\\
4,&h=4,\\
0,&\text{otherwise.}
\end{cases}
\]

There are `2^5=32` codes. The predicted moments are

\[
\mathbb E[h]=\frac{4\cdot2}{4}=2,
\qquad
\operatorname{Var}(h)=\frac{4\cdot2^2}{16}=1.
\]

The inverse-exponent convention again reverses the ordered 4-cycle but leaves its length, weight, and histogram unchanged.

#### Reproducible computation

Both additional examples are verified by:

```text
code/validate_long_orbit_examples.py
```

Run:

```bash
python code/validate_long_orbit_examples.py
```

The script compares, for each example:

1. direct factorization and explicit `tau` permutation;
2. direct generator-matrix Galois hull dimensions for every factor selection;
3. the orbit-boundary joint histogram;
4. the `2 x 2` transfer-matrix joint enumerator.

The exact output is:

```text
Example A (m_s=1, orbit length 6):
  principal reciprocal exponent p^k=2
  tau permutation on root indices: [0, 5, 3, 1, 6, 4, 2]
  orbit lengths: [1, 6]
  orbit-boundary == transfer: True
  direct == theory: True
  hull histogram: {0: 4, 1: 60, 2: 60, 3: 4}
  PASS
Example B (m_s=2, orbit length 4):
  principal reciprocal exponent p^k=2
  tau permutation on root indices: [0, 3, 1, 4, 2]
  orbit lengths: [1, 4]
  orbit-boundary == transfer: True
  direct == theory: True
  hull histogram: {0: 4, 2: 24, 4: 4}
  PASS
ALL LONG-ORBIT AND m_s>1 VALIDATIONS PASS
```

### 10.7 Nontrivial compatible-constacyclic validation

To test the `lambda`-constacyclic part of the framework beyond `lambda=1`, use

\[
q=4=2^2,
\qquad K=\mathbb F_4,
\qquad n=5,
\qquad \lambda=\omega\ne1,
\qquad k=1,
\]

where `omega^2+omega+1=0`. The principal coefficient exponent is `p^k=2`, and

\[
\lambda^{1+p^k}=\omega^3=1.
\]

The factorization verified by the script is

\[
x^5-\omega
=(x+\omega+1)(x^2+x+\omega)(x^2+\omega x+\omega).
\tag{10.9}
\]

The factors are distinct and the two quadratic factors have no root in `F_4`, so the displayed factorization is square-free and irreducible-factor complete. The `k`-Galois factor permutation is

\[
[0,2,1],
\]

with orbit lengths `[1,2]`. All `2^3=8` factor-selection codes are constructed directly. For every code the script checks the direct nullspace dual against the generator `h^{#}`, checks the hull, and compares the result with both the boundary formula and the transfer matrix.

The direct joint histogram is

\[
\{(0,0):1,(1,0):1,(2,2):2,(3,2):2,(4,0):1,(5,0):1\},
\]

so the hull histogram is

\[
\{0:4,\;2:4\}.
\]

The corresponding joint enumerator is

\[
\mathscr E_{\omega}(u,z)
=(u+1)(u^4+2u^2z^2+1).
\tag{10.10}
\]

This is a nontrivial compatible constacyclic test; it is not the `lambda=1` cyclic pilot.

Run:

```bash
python code/validate_nontrivial_constacyclic.py
```

The script reports `8 of 8` direct dual-generator checks and exact agreement between direct enumeration, orbit-boundary enumeration, and transfer-matrix enumeration.

### 10.8 Incompatible-twist boundary diagnostic

The compatible-twist hypothesis is not silently extended. For a diagnostic, take

\[
q=4,
\qquad n=5,
\qquad \lambda=\omega,
\qquad k=0,
\qquad p^k=1.
\]

Then

\[
\lambda^{1+p^k}=\omega^2\ne1,
\]

and

\[
\lambda'
=\lambda^{-p^k}=\lambda^{-1}=\omega^2\ne\omega.
\]

For the code

\[
C=\langle x^2+x+\omega\rangle
\subseteq \mathbb F_4[x]/\langle x^5-\omega\rangle,
\]

the direct Euclidean dual agrees with the code generated by `h^{#}` and is `lambda'`-constacyclic, but is not `lambda`-constacyclic. No transfer-matrix enumeration is attempted for this case.

Run:

```bash
python code/diagnose_incompatible_twist.py
```

The diagnostic reports:

```text
lambda^(1+p^k)=3 != 1
lambda^(-p^k)=3 != lambda
direct dual equals <h^(#)>: True
direct dual is lambda^(-p^k)-constacyclic: True
direct dual is lambda-constacyclic: False
No transfer-matrix enumeration was attempted.
```

**Limitation statement:**

> The present transfer-matrix theorem assumes the compatible-twist condition. When compatibility fails, the `k`-Galois dual of a `lambda`-constacyclic component has twist `lambda^{-p^k}`. A separate two-polynomial or bipartite formulation is required; the same-factor-set transfer theorem is not applied.

### 10.9 N1 and N2 validation obligations

#### N1 — 32,768-code exhaustive test

The blueprint retains the N1 test with

\[
q=16,\qquad n=15,\qquad 2^{15}=32,768\text{ factor selections}.
\]

The complete twist, `k`, factor-orbit data, histogram, and direct-dual checks must be recorded from the validator. They are not supplied in the current workspace and are therefore **VERIFY BEFORE MANUSCRIPT FINALIZATION**. No numerical N1 conclusion is asserted here.

#### N2 — `\mathbb F_{16}` nontrivial-twist convention test

The blueprint retains N2 as an extension-field, nontrivial-twist test in which

\[
\sigma_{s,k}=p^k\ne\rho_s=\sigma_{s,k}^{-1}.
\]

Its purpose is to verify that the second-slot inner product, the `p^k` normalized reciprocal, the direct dual, and the compatibility condition are used consistently. The exact `n`, `\lambda`, `k`, factorization, orbit data, and output must be supplied by the validator and are **VERIFY BEFORE MANUSCRIPT FINALIZATION**.

### 10.10 Computational verification table

| Test | Parameters and status | Exhaustive scope | Result status |
|---|---|---:|---|
| Original `F_4` pilot | `q=4`, `n=5`, `\lambda=1`, `k=1`, four `F_4` components | `8^4=4096` ring codes plus all component choices | PASS: validated histograms and enumerator |
| Example A | `q=8`, `n=7`, `\lambda=1`, `k=1`; orbit lengths `[1,6]` | `2^7=128` codes | PASS: direct/boundary/transfer agreement; hull histogram `{0:4,1:60,2:60,3:4}` |
| Example B | `q=4`, `K=F_{16}`, `m_s=2`, `n=5`, `\lambda=1`, `k=1`; orbit lengths `[1,4]` | `2^5=32` codes | PASS: direct/boundary/transfer agreement; hull histogram `{0:4,2:24,4:4}` |
| Compatible nontrivial twist | `q=4`, `n=5`, `\lambda=\omega`, `k=1`; orbit lengths `[1,2]` | `2^3=8` codes | PASS: 8/8 dual checks; hull histogram `{0:4,2:4}` |
| Incompatible diagnostic | `q=4`, `n=5`, `\lambda=\omega`, `k=0`; `\lambda^{1+p^k}\ne1` | one selected diagnostic code; no enumerator | PASS diagnostic only: dual twist differs |
| N1 | `q=16`, `n=15`, 32,768-code test | `2^{15}` | VERIFY BEFORE MANUSCRIPT FINALIZATION |
| N2 | `K=F_{16}` nontrivial twist with `\sigma\ne\rho` | validator-specified | VERIFY BEFORE MANUSCRIPT FINALIZATION |

The table separates theorem/proof claims, finite computational checks, and diagnostic/future-work items. Computational verification never substitutes for a general proof.

## 11. Brute-force validation protocol for the paper

The general hull-support theorem, orbit-boundary formula, transfer-matrix theorem, and distribution theorem are mathematical results that require general proofs. The scripts below provide only finite-instance validation.

> **Validation distinction:** The computational experiments provide exhaustive verification for the stated finite parameter sets; they are not substitutes for the general proofs.

For each small parameter set:

1. construct `A` and its component fields `K_s`;
2. factor every `M_s=x^n-lambda_s`;
3. compute `tau_{s,k}` using (4.1);
4. enumerate every factor-selection tuple `(J_1,...,J_N)`;
5. construct each component code from its generator polynomial;
6. compute the Galois dual by the defining inner product;
7. compute the intersection with the code;
8. record `dim_q(C)` and `dim_q(Hull_k(C))`;
9. compare with (5.5), (6.3), and (7.4);
10. compare the complete histogram with coefficients of `E(u,z)`.

For a direct linear-algebra check, the dual can be computed as the nullspace of the constraint matrix obtained from

\[
\sum_i x_i c_i^{p^k}=0
\]

for each generator row `c` of the code. The calculation must be over the correct component field, then weighted by `m_s` when reported over `F_q`.

Minimum test family:

- the existing verified `F_4` pilot (unchanged);
- Example A with `q=8`, `m_s=1`, and an orbit of length `6`;
- Example B with `q=4`, `m_s=2`, and an orbit of length `4`;
- a product of split components;
- unequal extension degrees `m_s`;
- a fixed factor plus a 2-cycle;
- the nontrivial compatible `lambda=omega` example in Section 10.7;
- the incompatible-twist diagnostic in Section 10.8 (diagnostic only; no enumerator);
- Euclidean and order-two Hermitian-type special cases.

The computational experiment validates only the listed finite instances; it does not replace the mathematical proof of the general theorem.

---

## 12. Phase-by-phase execution plan

### Phase 0 — Mathematical and literature audit

**Duration:** 2–3 days

Tasks:

- Read the supplied paper and mark results as `cite`, `use as lemma`, or `do not reproduce`.
- Record the extension-field convention-translation issue explicitly and keep `p^k` principal.
- Freeze the main hypotheses: square-free algebra, `gcd(n,p)=1`, and (3.5).
- Search recent literature for exact multiplicity/joint enumerator results.
- Keep “inequivalent codes” and quantum constructions outside the main claim until proved.

**Deliverable:** gap matrix plus one-page problem statement.

**Go/no-go:** If exact same joint enumerator already exists, change the contribution before drafting.

### Phase 1 — Algebra and notation

**Duration:** 4–6 days

- Prove or cite the product decomposition (3.1).
- Define `K_s`, `m_s`, `e_s`, component dimensions, and the componentwise inner product.
- State the split case separately so readers can compare with the supplied paper.
- Verify (3.7) and square-freeness.

**Deliverable:** clean preliminaries section and notation table.

### Phase 2 — `tau` construction

**Duration:** 5–7 days

- Define (4.1) precisely.
- Prove irreducibility preservation.
- Prove (4.4) from the root action and compatibility.
- Compute the permutation and all orbit lengths.
- Do not collapse general orbits to pairs.

**Deliverable:** factor-action lemma and reproducible factor-orbit routine.

### Phase 3 — Component hull support

**Duration:** 5–8 days

- Define `g_J` and `h_J`.
- Prove the dual support is `tau(F\J)`.
- Prove the hull is generated by the lcm.
- Derive exactly `(F\J) cap tau(J)`.
- Check the result on small direct examples.

**Deliverable:** Theorem 5.3 with a complete proof.

### Phase 4 — Orbit boundaries and transfer matrix

**Duration:** 4–6 days

- Establish (6.1) from the support set.
- Derive all four entries of (7.1).
- Prove the trace/closed-walk identity.
- Under the square-free and compatible-twist hypotheses, multiply the independent orbit/component factors.

**Deliverable:** joint enumerator theorem.

### Phase 5 — Explicit distribution and moments

**Duration:** 4–6 days

- Derive (8.1), not just quote it.
- Check `a=1,2,3,4,5` directly.
- Derive LCD count as a boundary corollary.
- Derive mean and variance, with the `a=1` and `a=2` cases separated.

**Deliverable:** exact distribution and statistical corollaries.

### Phase 6 — Exhaustive validation

**Duration:** 7–10 days

- Run the existing pilot, long-orbit, extension-field, and nontrivial-`lambda` scripts.
- Run the incompatible-twist diagnostic without invoking the enumerator.
- Compare direct hull ranks and generating functions.
- Store exact outputs, software version, and finite-field conventions.

**Deliverable:** reproducibility folder and validation table.

### Phase 7 — Optional Burnside section

**Duration:** 10–14 days, only if feasible

- Define a finite equivalence group.
- Prove it preserves the code family and hull dimension.
- Define the action on factor selections.
- Determine fixed-code sets.
- Apply Burnside only after the group action is complete.

If this is incomplete, move it to future work and do not frame the title as a Burnside/Pólya result.

### Phase 8 — Optional quantum application

**Duration:** 4–6 days

- Select one exact quantum construction theorem.
- State all hypotheses.
- Verify field/Gray-image compatibility.
- Compute minimum distance independently.
- Report only parameters justified by the theorem.

### Phase 9 — Writing and proof audit

**Duration:** 7–10 days

- Run a symbol-before-use check.
- Run a theorem-dependency check.
- Reproduce every table from code.
- Perform phrase-level similarity audit against the source.
- Separate proven results, computational evidence, conjectures, and future work.

---

## 13. Complexity statement — cautious version

Let

- `N` be the number of simple components;
- `r=sum_s |O_s|` be the total number of factor orbits;
- `a_max` be the maximum orbit length;
- `w_max` be the maximum orbit weight;
- `D_u,D_z` be chosen truncation degrees in `u,z`.

The direct enumeration of all factor selections has `2^{sum_s |F_s|}` cases. The transfer-matrix method avoids this explicit enumeration.

At the level of polynomial operations:

- each orbit contribution is a power of a `2 x 2` matrix of bivariate polynomials;
- repeated squaring uses `O(log a_O)` matrix multiplications per orbit;
- with dense truncated bivariate multiplication, a coarse multiplication bound is `O(D_u^2 D_z^2)` coefficient operations per polynomial product;
- the final product over `r` orbit factors requires additional polynomial convolutions of the same type.

Thus the transfer computation is much smaller than explicit factor-subset enumeration for many instances, but the exact arithmetic/bit complexity depends on:

- the cost of factoring `M_s`;
- orbit lengths and weights;
- coefficient growth;
- truncation limits;
- dense versus sparse polynomial representation.

The paper must **not** claim an unconditional polynomial-time algorithm in the full input size unless a precise encoding and complexity proof is added.

---

## 14. Possible Extension: Equivalence-Class Enumeration

All counts in `\mathscr E`, `H`, and the total-count identity are counts of distinct labeled `A`-submodules/factor-selection tuples. Two codes related by a coordinate permutation, monomial map, algebra automorphism, or another isometry are still counted separately. No equivalence-class count is claimed by the main theorem.

This is not part of the main theorem. Burnside enumeration remains future work unless the group action, fixed-point sets, and preservation of hull dimension are completely developed and proved.

Define a finite group of allowed equivalences, for example

\[
\Gamma_{A,n,\lambda,k}
=\{\phi:A^n\to A^n:
\phi \text{ is an A-linear monomial map},
\phi T_\lambda=T_\lambda\phi,
\langle\phi x,\phi y\rangle_k=\langle x,y\rangle_k\}.
\tag{14.1}
\]

Here `T_lambda` is the constacyclic shift. To use Burnside rigorously, the paper must establish:

1. `Gamma` is finite;
2. it acts on the set of codes under study;
3. it preserves the Galois hull dimension;
4. the fixed-code set of each element can be computed.

For `gamma in Gamma`, define

\[
\mathscr E_\gamma(u,z)
=\sum_{C:\gamma C=C}
 u^{\dim_{\mathbb F_q} C}z^{\dim_{\mathbb F_q}\operatorname{Hull}_k(C)}.
\]

Then, if all four points above have been proved,

\[
N_h^{\mathrm{equiv}}
=\frac1{|\Gamma|}
\sum_{\gamma\in\Gamma}[z^h]\mathscr E_\gamma(1,z).
\tag{14.2}
\]

This is a Burnside formula. The main transfer-matrix result should not be framed as a Pólya/Burnside equivalence-class method merely because `tau` has cycles.

If the full group action cannot be established, present (14.1)–(14.2) only as a future-work direction.

---

## 15. Quantum-code application — conditional and secondary

The classical enumerator is the main result. A quantum section should be included only after the classical proof and validation are complete.

The hull enumerator determines the hull-dimension distribution but does not by itself determine the minimum distance. No quantum distance may be inferred from `h` alone.

For a selected classical field code or verified Gray image `D`, record:

\[
[L,K,d]_q,
\qquad h=\dim_q\operatorname{Hull}_k(D).
\]

The paper must then name one exact quantum construction theorem and verify its hypotheses, including:

- which inner product is used;
- whether dual-containment, hull, or a related condition is required;
- whether the map from the ring code to `D` preserves the relevant dual/hull relation;
- how the quantum dimension is obtained;
- how the minimum distance is obtained;
- how the entanglement parameter is obtained.

No quantum parameter formula is part of the present theorem. If an application is retained, it must name the exact construction theorem and independently verify `K`, `h`, the entanglement parameter, and `d`. Hull dimension alone does not determine minimum distance. Any candidate EAQECC parameter display is **VERIFY BEFORE MANUSCRIPT FINALIZATION** and must be removed unless the cited theorem applies.


The joint enumerator can help filter classical candidates by `(K,h)`, but it does not determine `d`. Minimum distance must be calculated or bounded independently.

No claim of superior quantum parameters should be made without comparison with the current table/database and a recorded access date.

---

## 16. Recommended final paper structure

The manuscript should follow this logical flow:

1. **Introduction:** existing hull theory, audited gap, square-free affine structure, extension components, arbitrary orbit lengths, bivariate enumeration, and transfer matrices; no unsupported priority claims.
2. **Preliminaries and square-free affine algebra decomposition:** finite fields, component CRT, dimensions, constacyclic ideals, square-free/repeated-root boundary.
3. **`k`-Galois reciprocal and factor permutation:** second-slot convention, `p^k` reciprocal, root action, compatibility, and proof that `\tau_{s,k}(\mathcal F_s)=\mathcal F_s`.
4. **Component dual and hull characterization:** dual generator, lcm hull, support formula, and dimension transfer.
5. **Orbit boundary statistic:** binary selections, `1\to0` orientation, weights, and proof.
6. **Transfer-matrix joint enumerator:** derivation of `T_w`, trace identity, product enumerator, total-count identity, and coefficient sanity checks.
7. **Exact orbit polynomial and hull distribution:** closed coefficients, integrality, `H(z)=\mathscr E(1,z)`, and exact multiplicities.
8. **LCD count, mean and variance:** uniform probability model, independence without an i.i.d. claim, fixed orbit and two-cycle cases.
9. **Examples and exhaustive validation:** pilot, long orbit, extension component, compatible nontrivial twist, N1, N2, and incompatible diagnostic.
10. **Complexity and limitations:** factorization, coefficient arithmetic, square-free scope, incompatible twists, repeated roots, and proof status.
11. **Conclusion:** conservative results and future work.

Burnside/equivalence enumeration and quantum applications are optional future-work sections, not part of the main eleven-section theorem sequence.

---

## 17. Proof-dependency order

The theoretical dependency must be presented in this order:

```text
Componentwise k-Galois inner product
        |
        v
Second-slot Frobenius and normalized reciprocal
        |
        v
Definition of tau_{s,k}
        |
        v
Proof tau_{s,k}(F_s)=F_s
        |
        v
Component factor-selection classification
        |
        v
Dual factor support
        |
        v
Hull lcm and component support
        |
        v
Orbit boundary statistic
        |
        v
Transfer matrix and cyclic trace
        |
        v
Explicit orbit polynomial
        |
        v
Joint enumerator
        |
        v
Exact distribution
        |
        v
LCD count, mean, variance
        |
        v
Brute-force validation
        |
        +--> optional Burnside
        +--> optional quantum application
```

No later formula should be used before the definition and lemma on which it depends.

### 17.1 Proof-completeness ledger

Every item below requires a manuscript proof or a precise standard citation. A finite validator can check an instance but cannot discharge any item.

| Result | Required proof content | What computation may and may not do |
|---|---|---|
| Reduced affine decomposition (3.1) and polynomial CRT (3.7) | Prove reduced finite algebras over finite fields are products of finite fields, identify the idempotents, and prove the componentwise quotient isomorphism | A factorization script may exhibit examples only; it cannot prove the general decomposition. |
| Factor-selection classification (3.8)–(3.10) | Use the principal-ideal correspondence in the square-free quotient to prove uniqueness of every subset `J_s` and the dimension formula | Enumeration may verify the count for a finite modulus only. |
| Normalized reciprocal (4.1)–(4.2) | Prove monicity, multiplicativity, degree preservation, irreducibility preservation, and invertibility under the second-slot exponent `p^k` | A script may compare factors but cannot replace these polynomial arguments. |
| Factor permutation (4.3)–(4.6) | Prove the root action `alpha -> alpha^{-p^k}`, use `lambda_s^{1+p^k}=1`, and prove the inclusion is a bijection | An orbit listing validates only the selected finite field. |
| Dual-generator Lemma 5.1 | Derive the semilinear dual from the defining inner product, track the constacyclic twist, normalize the reciprocal, and prove equality of ideals | Direct nullspaces are regression tests only. |
| Hull lcm Lemma 5.2 and Theorem 5.3 | Prove ideal intersection equals the lcm ideal in the square-free quotient, derive the support complement, and convert `K_s`-dimensions to `F_q`-dimensions | Direct hull ranks may check (5.5) for examples only. |
| Boundary formula (6.1)–(6.3) | Establish the factor-by-factor support equivalence and the `1 -> 0` orientation, including cyclic closure | Word enumeration checks coefficients only. |
| Transfer theorem (7.1)–(7.9) | Derive all four transition weights, expand the trace as closed walks, prove independence across orbit/component selections, and prove the total-count and marginal identities | Matrix code can validate finite polynomials but cannot prove factorization. |
| Orbit polynomial (8.1)–(8.6) | Give the cyclic transition-count argument, prove `N(a,b)=2\binom{a}{2b}` including integrality, and extract coefficients | Small `a` tables are sanity checks only. |
| LCD, mean, and variance corollaries (9.1)–(9.7) | Prove zero boundary iff constant binary word and derive the independent-indicator moments, separating `a=1` and `a=2` | Exhaustive histograms may confirm moments for listed parameters only. |

The manuscript must state which results are imported, which are reproved under the principal convention, and which are computational validations. No table or code output may be cited as a proof of a general theorem.

---

## 18. Risk register and mathematically safe fallbacks

### Risk 1: General extension-field convention conflicts with source notation

Use the rigorous component version (3.2)–(3.5). The principal exponent is always `p^k` because the Frobenius acts on the second slot. If a source uses an inverse or first-slot convention, define `rho_s` only in a labeled comparison and translate the source formula before using it.

### Risk 2: `tau` has long cycles and the intended application only has pairs

Keep arbitrary cycles in the theorem. Treat fixed points and 2-cycles as special corollaries.

### Risk 3: Incompatible twist

If `lambda_s^{1+p^k} != 1`, the dual is a `lambda_s^{-p^k}`-constacyclic code. Do not force it into the same factor set. Either develop a two-polynomial/bipartite version or state it as future work.

### Risk 4: Full Burnside group is difficult

Remove it from the main paper and keep the labeled-code enumerator. Do not frame the title as an equivalence-class result.

### Risk 5: Quantum distance is not controlled

Report the classical distribution only, or compute distance independently. Hull dimension alone is not a distance theorem.

### Risk 6: A future paper already has the same enumerator

Possible genuinely different extensions are:

1. extension-field-weighted joint enumerators;
2. rigorous inequivalent-code counts;
3. repeated-root factor multiplicities;
4. asymptotic distribution under a specified family.

Each alternative requires a fresh literature audit.

---

## 19. Originality and reproducibility checklist

- [ ] The title does not overclaim an equivalence-class enumeration method.
- [ ] `K_s` and `m_s` are defined before use.
- [ ] The principal Frobenius is `sigma_{s,k}(a)=a^{p^k}`; any inverse exponent is confined to the alternative-convention note, including the `k=0` case.
- [ ] The split case `m_s=1` is explicitly identified.
- [ ] `tau_{s,k}` is defined by equation (4.1).
- [ ] `tau(F_s)=F_s` is proved from the root action and compatibility.
- [ ] General orbit lengths are allowed.
- [ ] The hull support is derived as `(F\J) cap tau(J)`.
- [ ] The boundary orientation is fixed as `1 -> 0`.
- [ ] The transfer matrix entries are explained one by one.
- [ ] The trace/closed-walk argument is included.
- [ ] `P_{a,w}` is derived and checked for `a=1,...,5`.
- [ ] LCD count is stated as a corollary.
- [ ] Mean and variance include fixed-orbit and 2-cycle cases.
- [ ] Existing `F_4` pilot remains unchanged mathematically and is computationally validated.
- [ ] The `q=8`, orbit-length-6 example is computationally validated.
- [ ] The `m_s=2` extension-field example is computationally validated.
- [ ] The nontrivial compatible `lambda=omega` constacyclic example is computationally validated.
- [ ] The incompatible-twist diagnostic confirms the different dual twist and uses no enumerator.
- [ ] Direct hull histograms equal theoretical histograms on every stated finite instance.
- [ ] The computational results are explicitly separated from general mathematical proofs.
- [ ] Complexity language is cautious.
- [ ] Burnside is conditional and has a defined group/action if included.
- [ ] Quantum parameters are conditional on an explicit construction theorem.
- [ ] No computational observation is presented as a proof.
- [ ] Source wording, examples, and theorem order are not cosmetically copied.

---

## 20. Revised 9-week timeline

| Week | Target | Output |
|---:|---|---|
| 1 | Mathematical audit and literature search | hypotheses, gap matrix, notation freeze |
| 2 | Component-field and convention setup | Section 2–3 draft |
| 3 | Precise factor permutation | Lemmas for `tau(F)=F` and orbit lengths |
| 4 | Dual/hull support proof | Section 4–5 draft |
| 5 | Boundary statistic and transfer matrix | Main enumerator theorem |
| 6 | Explicit coefficients and moments | Distribution/corollaries |
| 7 | Exhaustive computational validation | scripts and exact tables |
| 8 | Optional Burnside or quantum section | only if fully justified |
| 9 | Full proof audit and originality review | submission-ready blueprint/manuscript |

If an optional section is incomplete at Week 8, omit it rather than weakening the main theorem.

---

## 20A. Verified references and literature records

Only records with publisher metadata currently verified are listed. Any additional bibliography entry must be completed before manuscript finalization.

1. I. Debnath, O. Prakash, and H. Islam, “Galois hulls of constacyclic codes over finite fields,” *Cryptography and Communications*, 15(1) (2023), 111–127. DOI: 10.1007/s12095-022-00591-6. The associated correction is: I. Debnath, O. Prakash, and H. Islam, “Correction to: Galois hulls of constacyclic codes over finite fields,” *Cryptography and Communications*, 15 (2023), 129–130. DOI: 10.1007/s12095-022-00602-6.

2. I. Debnath, H. Islam, E. Martínez-Moro, and O. Prakash, “Galois hulls of constacyclic codes over affine algebra rings,” *Discrete Mathematics*, 349(2) (2026), Article 114750. DOI: 10.1016/j.disc.2025.114750.

3. I. Debnath and O. Prakash, “Average dimensions of Galois hulls of constacyclic codes,” *Advances in Mathematics of Communications*, 19(6) (2025), 1569–1604. DOI: 10.3934/amc.2025010.

4. I. Debnath, H. Islam, S. Yadav, and O. Prakash, “Study of small Galois hull dimensions of constacyclic codes,” *Advances in Mathematics of Communications*, 22 (2026), 1–18. DOI: 10.3934/amc.2025054.

5. E. Sangwisut, S. Jitman, S. Ling, and P. Udomkavanich, “Hulls of cyclic and negacyclic codes over finite fields,” *Finite Fields and Their Applications*, 33 (2015), 232–257. DOI: 10.1016/j.ffa.2014.12.008.

6. S. Jitman and E. Sangwisut, “The average dimension of the Hermitian hull of constacyclic codes over finite fields of square order,” *Advances in Mathematics of Communications*, 12(3) (2018), 451–463. DOI: 10.3934/amc.2018027.

7. S. Jitman and E. Sangwisut, “Hulls of cyclic codes over the ring `\mathbb F_2+v\mathbb F_2`,” *Thai Journal of Mathematics*, 18 (2020), 135–144. DOI: **VERIFY BEFORE MANUSCRIPT FINALIZATION** — no DOI was confirmed in the publisher record.

8. Z. Tian, J. Gao, and Y. Gao, “Hulls of constacyclic codes over finite non-chain rings and their applications in quantum codes construction,” *Quantum Information Processing*, 23 (2024), Article 9. DOI: 10.1007/s11128-023-04230-8.

9. S. Yadav, A. Singh, H. Islam, O. Prakash, and P. Solé, “Hermitian hull of constacyclic codes over a class of non-chain rings and new quantum codes,” *Computational and Applied Mathematics*, 43 (2024), Article 269. DOI: 10.1007/s40314-024-02789-1.

10. H. Liu and X. Pan, “Galois hulls of linear codes over finite fields,” *Designs, Codes and Cryptography*, 88(2) (2020), 241–255. DOI: 10.1007/s10623-019-00681-2.

11. B. Chen, Y. Fan, L. Lin, and H. Liu, “Constacyclic codes over finite fields,” *Finite Fields and Their Applications*, 18(6) (2012), 1217–1231. DOI: 10.1016/j.ffa.2012.10.001.

12. H. Li, X. Hou, J. Gao, F. Ma, and J. Mi, “Hulls of `\mathbb Z_4`-double cyclic codes,” *Computational and Applied Mathematics*, 44 (2025), Article 423. DOI: 10.1007/s40314-025-03385-7.

13. A. K. Shukla, O. P. Pandey, V. Mishra, S. Pathak, and A. K. Upadhyay, “Hulls of `\mathbb Z_p\mathbb Z_p[v]`-cyclic codes and construction of EAQECCs,” *Advances in Mathematics of Communications*, 20 (2026), 209–238. DOI: 10.3934/amc.2025037.

14. S. Jitman, E. Sangwisut, and P. Udomkavanich, “Hulls of cyclic codes over `\mathbb Z_4`,” *Discrete Mathematics*, 343(1) (2020), Article 111621. DOI: 10.1016/j.disc.2019.111621.

15. S. T. Dougherty and E. Saltürk, “The number of codes over rings of order 4 containing a hull of given type,” *Advances in Mathematics of Communications*, 19(1) (2025), 11–35. DOI: 10.3934/amc.2023031.

16. Y. Ding and X. Lu, “Galois hulls of cyclic codes over finite fields,” *IEICE Transactions on Fundamentals of Electronics, Communications and Computer Sciences*, 103-A(1) (2020), 370–375. DOI: 10.1587/transfun.2019EAL2087.

17. Y. Fan and L. Zhang, “Galois self-dual constacyclic codes,” *Designs, Codes and Cryptography*, 84(3) (2017), 473–492. DOI: 10.1007/s10623-016-0282-8.

18. K. Guenda, S. Jitman, and T. A. Gulliver, “Constructions of good entanglement-assisted quantum error correcting codes,” *Designs, Codes and Cryptography*, 86(1) (2018), 121–136. DOI: 10.1007/s10623-017-0330-z.

19. C. Carlet, C.-J. Li, and S. Mesnager, “Linear codes with small hulls in semi-primitive case,” *Designs, Codes and Cryptography*, 87 (2019), 3063–3075. DOI: 10.1007/s10623-019-00663-4.

20. E. Zhang, B. Kong, and X. Zheng, “Quantum Codes from Galois Hulls of Constacyclic Codes over a Finite Non-Chain Ring,” *Entropy*, 28(4) (2026), Article 407. DOI: 10.3390/e28040407.


## 21. Immediate next actions

1. Keep `code/validate_pilot.py`, `code/validate_long_orbit_examples.py`, `code/validate_nontrivial_constacyclic.py`, and `code/diagnose_incompatible_twist.py` under version control and attach all outputs to the research notes.
2. Prove and implement the `K_s` version with the principal second-slot exponent `p^k`; use `rho_s` only in an explicitly labeled alternative-convention check.
3. Retain Example A as the genuine long-orbit test; do not infer long-cycle behavior from the `F_4`, Hermitian, 2-cycle pilot.
4. Prove Lemma 5.1 and Theorem 5.3 in full before writing the transfer-matrix section.
5. Derive the `a=1,...,5` orbit polynomials in the paper or an appendix.
6. Keep Burnside and quantum applications explicitly optional until their hypotheses are checked.
7. Complete the publisher-level literature audit, verify all references/DOIs, and resolve every `VERIFY BEFORE MANUSCRIPT FINALIZATION` marker before submission.
8. Add and run the N1 and N2 validators before reporting those examples as computationally verified.
9. Run a final global search for any inverse-`rho_s` formula that has leaked into the principal theory.

## 22. Global proof and notation quality-control checklist

Before manuscript submission, verify all of the following:

- `\sigma_{s,k}=p^k` is used in the second slot, normalized reciprocal, dual generator, root action, and compatibility condition.
- `\rho_s` appears only in explicitly labeled alternative-convention comparisons, including the N2 diagnostic obligation.
- The proof of `\tau_{s,k}(\mathcal F_s)=\mathcal F_s` is complete.
- Reciprocal multiplicativity, irreducibility preservation, and invertibility are proved.
- The dual-generator identity `\langle h_J^{\#_{s,k}}\rangle` is proved, not inferred from computations.
- The lcm hull formula and hull-support characterization are proved.
- The component hull theorem and the orbit-boundary formula are proved.
- The transfer matrix has the `0\to0`, `0\to1`, `1\to0`, and `1\to1` entries in the stated orientation.
- Orbit indexing closes cyclically and the trace identity is proved.
- The closed coefficient formula is shown integral by `N(a,b)=2\binom a{2b}`.
- LCD, mean, and variance formulas are proved, including the `a=2` exception.
- `K_s`-dimensions and `\mathbb F_q`-dimensions are never conflated.
- Code dimension is not confused with selected-factor codimension.
- The transfer-matrix orientation assigns the destination-factor weight and closes the orbit with a trace.
- Orbit indices, component indices, and the product over `s,O` are defined before use.
- The compatibility condition is checked componentwise; the incompatible twist is `\lambda_s^{-p^k}` and receives no compatible enumerator.
- Total counts refer to distinct labeled codes; equivalence classes are separate.
- All reference metadata and DOI values are checked against the publisher records; unresolved items carry the exact verification marker.
- Every symbol is defined before use, every theorem cites or proves its dependencies, and every comparison status is supported by the audit record.
- No finite computation is described as a proof.
- No unsupported priority or quantum-distance claim remains.

### Final success criterion

The paper is mathematically ready only when:

- the direct factor action, component hull support, boundary formula, transfer matrix, explicit orbit polynomial, joint enumerator, moments, and LCD count all agree;
- the pilot and additional small cases pass exact brute-force checks;
- every optional claim is either proved with hypotheses or clearly marked as future work.

Current status must be reported conservatively: the general formulas are mathematical proof targets/results to be written rigorously; the scripts provide exhaustive computational validation for the listed finite instances; the final literature audit remains submission-dependent; Burnside/equivalence enumeration and quantum constructions remain optional unless their hypotheses are fully established.
