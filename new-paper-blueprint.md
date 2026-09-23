# Exact Enumeration of `k`-Galois Hull Dimensions of Constacyclic Codes over Square-Free Affine Algebras

> **Blueprint status:** This is the corrected inverse-Frobenius blueprint. General statements are labeled as `THEOREM`, `LEMMA`, `PROPOSITION`, `PROOF TARGET`, or `FUTURE WORK`; finite runs are labeled `COMPUTATIONAL VALIDATION`; literature records carry an explicit verification category.
>
> **Principal convention:**
> \[
> \langle x,y\rangle_{s,k}=\sum_i x_i y_i^{p^k},
> \qquad
> \sigma_{s,k}(a)=a^{p^k},
> \qquad
> \rho_{s,k}(a)=a^{p^{e m_s-k}}.
> \]
> The dual is defined by `\langle c,x\rangle_{s,k}=0` with the code in the first slot, so the principal reciprocal, root action, compatibility, dual generator, and incompatible twist use `\rho_{s,k}`.
>
> **Evidence categories:** `THEOREM`, `LEMMA`, and `PROPOSITION` identify claims to be proved in the manuscript; `PROOF TARGET` identifies a result whose proof is still required; `COMPUTATIONAL VALIDATION` identifies only a finite reproducible run; `FUTURE WORK` identifies material outside the main theorem; and `VERIFY BEFORE MANUSCRIPT FINALIZATION` identifies unresolved literature or example data.
>
> **Scope:**
> \[
> A=\mathbb F_q[X_1,\ldots,X_\ell]/
> \langle t_1(X_1),\ldots,t_\ell(X_\ell)\rangle
> \]
> with monic square-free `t_i`, `\gcd(n,p)=1`, and compatible component twists for the main enumerator. Repeated-root algebras and equivalence-class counts are not silently included.
>
> **Positioning:** The proposed paper is an exact labeled-code enumerative study. It uses factor orbits and transfer matrices, not a Burnside/Pólya equivalence-class count, and makes no unsupported priority claim.
>
> **Base paper:** Debnath, Islam, Martínez-Moro, and Prakash, *Galois hulls of constacyclic codes over affine algebra rings*, *Discrete Mathematics* 349 (2026), Article 114750, DOI 10.1016/j.disc.2025.114750; see the reference-status table in Section 20A.

## Abstract (draft for manuscript)

We study the exact distribution of `k`-Galois hull dimensions of `lambda`-constacyclic codes over a square-free affine algebra. The square-free hypothesis decomposes the algebra into finite-field components and reduces each component code to a binary selection of irreducible factors of a simple-root constacyclic polynomial. With the second-slot convention

\[
\langle x,y\rangle_{s,k}=\sum_i x_i y_i^{p^k},
\qquad
\rho_{s,k}(a)=a^{p^{e m_s-k}},
\]

and the dual defined by `\langle c,x\rangle_{s,k}=0`, we define the normalized inverse-Frobenius `k`-Galois reciprocal, its factor permutation, and the resulting hull-support statistic. Under the explicitly collected hypotheses of Section 3, the main proof target is the bivariate enumerator

\[
\mathscr E(u,z)=\prod_s\prod_O\operatorname{tr}\bigl(T_{w_O}(u,z)^{a_O}\bigr),
\qquad
T_w(u,z)=\begin{pmatrix}u^w&1\\u^wz^w&1\end{pmatrix},
\]

where `u` records `F_q`-code dimension and `z` records `F_q`-hull dimension. Its specialization gives the exact hull-distribution polynomial, the total-code count, the LCD count, and closed mean and variance formulas, including the exceptional two-cycle variance. The paper distinguishes theorem-level proofs from exhaustive finite computations. The current `COMPUTATIONAL VALIDATION` suite confirms the listed `F_4`, `F_8`, `F_{16}`, compatible nontrivial-`\lambda`, incompatible-twist, and N2 finite instances. N1 remains explicitly `VERIFY BEFORE MANUSCRIPT FINALIZATION`; no N1 result is invented.

## Notation table and convention audit

| Symbol | Meaning | Scope or warning |
|---|---|---|
| `p` | characteristic prime | `q=p^e` |
| `q` | base-field size | `\mathbb F_q` |
| `e` | base-field extension degree | reserved for `q=p^e` |
| `k` | Galois parameter | `0\le k<e` |
| `\sigma_{s,k}` | second-slot coefficient Frobenius | `\sigma_{s,k}(a)=a^{p^k}` on `K_s` |
| `\rho_{s,k}` | inverse Frobenius on `K_s` | `\rho_{s,k}(a)=a^{p^{e m_s-k}}=\sigma_{s,k}^{-1}(a)` |
| `A` | square-free affine algebra | decomposes as `\prod_s K_s` |
| `K_s` | simple field component | `K_s=\mathbb F_{q^{m_s}}=\mathbb F_{p^{e m_s}}` |
| `m_s` | component degree | `[K_s:\mathbb F_q]` |
| `n` | constacyclic coordinate length | `n\ge1`, normally `\gcd(n,p)=1` |
| `N` | number of simple algebra components | `1\le s\le N` |
| `\ell` | number of affine variables | appears in the presentation of `A` |
| `\eta_s` | primitive orthogonal idempotent | identifies the component `K_s`; `e` is not used for idempotents |
| `\lambda_s` | component of the constacyclic unit | `\lambda_s\in K_s^\times` |
| `M_s(x)` | component constacyclic modulus | `x^n-\lambda_s` |
| `\mathcal F_s` | monic irreducible factors of `M_s` | use this symbol exclusively for the factor set |
| `\mathcal O_s` | set of `\tau_{s,k}`-orbits in `\mathcal F_s` | labeled factor orbits, not equivalence classes |
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

**Convention audit.** The inner product is

\[
\langle x,y\rangle_{s,k}=\sum_i x_i y_i^{p^k},
\qquad
\sigma_{s,k}(a)=a^{p^k}.
\]

The component dual is defined with the code in the first argument:

\[
C_s^{\perp_k}
=\{x\in K_s^n:\langle c,x\rangle_{s,k}=0\text{ for every }c\in C_s\}.
\]

Because `K_s=\mathbb F_{p^{e m_s}}`, the inverse automorphism is

\[
\rho_{s,k}(a)=a^{p^{e m_s-k}}=\sigma_{s,k}^{-1}(a).
\]

The principal normalized reciprocal, dual-generator identity, root action, and compatibility condition use `\rho_{s,k}`, not `\sigma_{s,k}`. The exponent `p^k` remains in the inner product itself. This argument order and inverse-Frobenius translation must be stated before the dual-generator proof and used consistently in every component and example.


---

## 0. Audit findings — what was corrected and why

The previous framework had the right research direction, but several statements needed to be made conditional or proved more carefully.

### Correction A — title and positioning

The earlier title invoked Pólya/Burnside orbit counting. The revised title is:

> **Exact Enumeration of `k`-Galois Hull Dimensions of Constacyclic Codes over Square-Free Affine Algebras**

A shorter alternative, if the bivariate result is emphasized, is:

> **Joint Enumeration of Code and `k`-Galois Hull Dimensions for Constacyclic Codes over Square-Free Affine Algebras**

The actual framework uses factor orbits, transfer matrices, and generating functions. A genuine Burnside/Pólya equivalence-class construction is only optional and is not assumed in the main theorem.

### Correction B — the second-slot inner product determines the inverse reciprocal

On `K_s`, write

\[
\sigma_{s,k}(a)=a^{p^k},
\qquad
\rho_{s,k}(a)=a^{p^{e m_s-k}}=\sigma_{s,k}^{-1}(a).
\]

The inner product remains

\[
\langle x,y\rangle_{s,k}=\sum_i x_i\sigma_{s,k}(y_i).
\]

The dual convention used in this blueprint is

\[
C_s^{\perp_k}=\{x:\langle c,x\rangle_{s,k}=0\text{ for all }c\in C_s\}.
\]

Applying `\rho_{s,k}` to the defining equation gives

\[
\sum_i c_i^{p^{e m_s-k}}x_i=0,
\]

so the normalized reciprocal in the component dual-generator formula uses the inverse Frobenius exponent `p^{e m_s-k}`. This is not a replacement of `p^k` in the inner product; it is the inverse-semilinear translation required by the specified dual convention.

### Correction C — the factor permutation is explicit under the inverse Frobenius

For a monic factor

\[
f(x)=\sum_{i=0}^{d}f_i x^i,
\qquad f_0\ne0,
\]

define the normalized `k`-Galois reciprocal over `K_s` by

\[
f^{\#_{s,k}}(x)
=f_0^{-p^{e m_s-k}}
\sum_{i=0}^{d}f_i^{p^{e m_s-k}}x^{d-i}.
\tag{0.1}
\]

Then

\[
\tau_{s,k}(f):=f^{\#_{s,k}}
\]

has root action

\[
\alpha\longmapsto\alpha^{-p^{e m_s-k}}.
\]

The compatibility condition for the same constacyclic polynomial is

\[
\lambda_s^{1+p^{e m_s-k}}=1.
\tag{0.2}
\]

Under (0.2), `tau` maps `\mathcal F_s` to itself. It is a permutation, but it is **not assumed to be an involution**. General orbit lengths are allowed.

### Source theorem references and scope

The publisher/abstract audit confirms that the finite-field source treats Galois hulls of constacyclic codes and that the affine-algebra source treats square-free affine algebras, `k`-Galois duals, hull generators, dimensions, and LCD/quantum examples. Exact theorem labels, displayed exponents, and overlap with the present transfer enumerator are **THEOREM-LEVEL: VERIFY BEFORE MANUSCRIPT FINALIZATION** because the supplied PDF is not locally text-extractable and the publisher page exposes only an abstract/preview. The present blueprint makes the extension-component exponent explicit as `p^{e m_s-k}` and requires a direct proof under the dual argument order above. No source formula is imported without translating its argument order and Frobenius exponent.

### Correction D — the support set is fixed by derivation

With the convention `tau(f)=f^{#}`, the component hull support is

\[
(\mathcal F_s\setminus J_s)\cap\tau_{s,k}(J_s),
\tag{0.3}
\]

not an arbitrarily chosen inverse-image variant. The reason is derived in Section 5 below from the lcm of the generator and the inverse-Frobenius dual generator.

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

These agree with direct enumeration of all `2^a` binary words. The derivation is given in Section 8.

### Correction G — moments are derived, including the `a=2` exception

For an orbit of length `a=1`, the boundary indicator is identically zero. For `a=2`, the two cyclic transition indicators are mutually exclusive, so the variance is `1/4`, not `a/16=1/8`. For `a>=3`, the variance is `a/16`. The corrected formulas are in Section 9.

### Correction H — the pilot example was actually verified

The existing script `code/validate_pilot.py` performs an independent dependency-free computation over `F_4` and checks:

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
- an `F_{16}=F_{4^2}` component with `m_s=2`, `sigma=2`, `rho=8`, and a `tau`-orbit of length `4`;
- direct hull dimensions, orbit-boundary histograms, and transfer-matrix enumerators.

The separate N2 validator compares the direct dual with both reciprocal exponents and records A=B for all 32 selections.

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

Use cautious positioning such as: “The present work focuses on the exact joint enumeration of code dimension and `k`-Galois hull dimension through factor-orbit and transfer-matrix methods.” Make no priority or novelty claim unless a documented literature search supports the exact claim.

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

The matrix uses the statuses **publisher/abstract scope**, **partial publisher/abstract scope**, and **candidate present-work scope**. These are comparison statuses, not theorem-level verification or priority claims. Exact theorem overlap remains **THEOREM-LEVEL: VERIFY BEFORE MANUSCRIPT FINALIZATION** unless the reference-status table says otherwise.

**Clauses:** (A) structural dual/hull generator; (B) finite-field fixed-hull-dimension enumeration; (C) average or prescribed small hull dimensions; (D) square-free affine product of finite-field components; (E) arbitrary factor-orbit boundary statistic with component weights; (F) joint code-dimension/hull-dimension enumerator; (G) compatible nontrivial twists and explicit incompatible-twist boundary; (H) conditional quantum application; (I) equivalence-class enumeration.

| Audited paper or record | A | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|---|
| Sangwisut et al. (2015) | **publisher/abstract scope** — cyclic/negacyclic finite-field hull formulas | **publisher/abstract scope** — fixed hull dimensions in that setting | **partial publisher/abstract scope** — not the present Galois-average package | **candidate present-work scope** — affine product is outside the verified scope | **candidate present-work scope** — the present weighted orbit formulation is not verified there | **candidate present-work scope** — no verified bivariate code/hull enumerator | **partial publisher/abstract scope** — Euclidean/Hermitian cyclic/negacyclic cases only | **partial publisher/abstract scope** — hull applications are background, not this affine theorem | **candidate present-work scope** — no quotient by equivalence in the proposed main count |
| Debnath et al. (2023) finite-field paper | **publisher/abstract scope** — finite-field constacyclic formula | **publisher/abstract scope** under stated `q` restrictions — exact prescribed-dimension counts are stated in the abstract | **partial publisher/abstract scope** — not the present all-component moment package | **candidate present-work scope** — affine product extension is not verified in that record | **partial publisher/abstract scope** — factor arrangements are used, but the present cyclic-boundary formulation needs comparison | **candidate present-work scope** — no verified joint code/hull transfer product | **partial publisher/abstract scope** — finite-field constacyclic twists are treated, but the proposed compatible/incompatible diagnostic must be compared | **partial publisher/abstract scope** — not the main contribution of that paper | **candidate present-work scope** — labeled codes only |
| Jitman–Sangwisut (2018) | **partial publisher/abstract scope** — Hermitian constacyclic hull setting | **partial publisher/abstract scope** — average, not fixed-dimension multiplicities | **publisher/abstract scope** — average and bounds | **candidate present-work scope** | **candidate present-work scope** | **candidate present-work scope** | **partial publisher/abstract scope** — Hermitian specialization | **partial publisher/abstract scope** — no affine transfer claim | **candidate present-work scope** |
| Liu–Pan (2020) | **publisher/abstract scope** — general Galois-hull methods | **partial publisher/abstract scope** — general linear-code results, not this constacyclic count | **partial publisher/abstract scope** — invariance/constructive results rather than this distribution | **candidate present-work scope** | **candidate present-work scope** | **candidate present-work scope** | **partial publisher/abstract scope** — Galois duality is general | **partial publisher/abstract scope** — applications are not the present quantum section | **candidate present-work scope** |
| Debnath et al. (2026) affine-algebra paper | **publisher/abstract scope** — affine `k`-Galois dual/hull generators are its stated scope | **partial publisher/abstract scope** — exact hull formula is stated, but an all-code count is not verified from the abstract | **partial publisher/abstract scope** — LCD and examples, not the present distribution/moments | **publisher/abstract scope** — square-free affine algebra is the source setting | **candidate present-work scope** — arbitrary weighted factor-orbit boundary theorem requires full-text comparison | **candidate present-work scope** — no exact bivariate transfer product verified | **partial publisher/abstract scope** — `lambda`-constacyclic and compatibility details require full-text comparison | **publisher/abstract scope** — quantum examples are explicitly stated | **candidate present-work scope** — source future-work language must be checked |
| Debnath–Prakash (2025) average paper | **partial publisher/abstract scope** | **partial publisher/abstract scope** | **publisher/abstract scope** — average dimensions | **partial publisher/abstract scope** — a particular ring `R_{m,q}` is treated | **candidate present-work scope** | **candidate present-work scope** | **partial publisher/abstract scope** — Galois constacyclic setting | **partial publisher/abstract scope** — LCD constructions/examples | **candidate present-work scope** |
| Debnath et al. (2026) small-hull paper | **partial publisher/abstract scope** | **partial publisher/abstract scope** — dimensions one and two only | **publisher/abstract scope** — small-dimension existence conditions | **candidate present-work scope** | **candidate present-work scope** | **candidate present-work scope** | **partial publisher/abstract scope** — finite-field constacyclic scope | **publisher/abstract scope** — EAQECC applications | **candidate present-work scope** |
| Tian–Gao–Gao (2024) | **partial publisher/abstract scope** — specific non-chain ring | **partial publisher/abstract scope** — ring-specific results, not the proposed all-code theorem | **partial publisher/abstract scope** | **partial publisher/abstract scope** — two idempotent components under a special Gray map | **candidate present-work scope** | **candidate present-work scope** | **partial publisher/abstract scope** — Euclidean/Hermitian only | **publisher/abstract scope** — quantum constructions | **candidate present-work scope** |
| Yadav et al. (2024) | **partial publisher/abstract scope** — Hermitian generators/conditions in a specific ring | **partial publisher/abstract scope** | **publisher/abstract scope** — possible dimensions/LCD conditions in that setting | **partial publisher/abstract scope** — restricted non-chain ring | **candidate present-work scope** | **candidate present-work scope** | **partial publisher/abstract scope** — Hermitian specialization | **publisher/abstract scope** — quantum applications | **candidate present-work scope** |
| Jitman–Sangwisut (2020) over `F_2+vF_2` | **partial publisher/abstract scope** — ring-specific cyclic hulls | **partial publisher/abstract scope** — theorem-level fixed-type overlap requires full-text check | **partial publisher/abstract scope** — average/specific dimensions require full-text check | **partial publisher/abstract scope** — a two-idempotent ring is related but not the arbitrary affine product | **candidate present-work scope** | **candidate present-work scope** | **partial publisher/abstract scope** — Euclidean cyclic setting | **partial publisher/abstract scope** | **candidate present-work scope** |
| Jitman–Sangwisut–Udomkavanich (2020) over `Z_4` | **publisher/abstract scope** — cyclic hull generators | **publisher/abstract scope** — fixed 2-dimension enumeration | **publisher/abstract scope** — average 2-dimension | **candidate present-work scope** — reduced affine-field components are different | **candidate present-work scope** | **candidate present-work scope** | **partial publisher/abstract scope** — Euclidean cyclic case | **partial publisher/abstract scope** | **candidate present-work scope** |
| Dougherty–Saltürk (2025) | **partial publisher/abstract scope** — hull/type framework over order-four rings | **partial publisher/abstract scope** — counts by hull type, not this factor family | **partial publisher/abstract scope** | **candidate present-work scope** | **candidate present-work scope** | **candidate present-work scope** | **partial publisher/abstract scope** — different duality settings | **partial publisher/abstract scope** | **candidate present-work scope** |
| Zhang–Kong–Zheng (2026) | **partial publisher/abstract scope** — specific finite non-chain ring | **partial publisher/abstract scope** | **partial publisher/abstract scope** | **candidate present-work scope** | **candidate present-work scope** | **candidate present-work scope** | **partial publisher/abstract scope** — Galois ring-specific scope | **publisher/abstract scope** — quantum applications | **candidate present-work scope** |

**Matrix interpretation and contribution boundary.** The publisher/abstract audit indicates substantial overlap: finite-field cyclic/negacyclic and constacyclic records report hull formulas and, in several settings, fixed-dimension or average results; affine/non-chain-ring records report structural hull formulas and quantum applications. This is not theorem-level proof of absence or priority. The candidate present-work scope is narrower: prove and validate the explicitly stated square-free affine **product** theorem and its **joint code-dimension/hull-dimension transfer enumerator**, while identifying precisely which finite-field cases reduce to cited results. If a full-text audit finds the same product or joint enumerator, remove that candidate contribution and redesign the manuscript.

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

### PROPOSITION 3.1 — square-free affine decomposition

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

Let `\eta_s` denote the primitive orthogonal idempotent corresponding to `K_s`.

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

is an automorphism. Since `K_s=\mathbb F_{p^{e m_s}}`, its inverse is

\[
\rho_{s,k}:K_s\to K_s,
\qquad a\mapsto a^{p^{e m_s-k}}.
\tag{3.3}
\]

Define the component dual by placing the codeword in the first argument:

\[
C_s^{\perp_k}
=\{x\in K_s^n:\langle c,x\rangle_{s,k}=0\text{ for every }c\in C_s\}.
\]

Applying `\rho_{s,k}` to `\langle c,x\rangle_{s,k}=0` gives the ordinary linear equations

\[
\sum_i c_i^{p^{e m_s-k}}x_i=0.
\]

This is why the principal reciprocal and dual-generator formulas below use `p^{e m_s-k}`, while the inner product itself continues to use `p^k` on its second slot.

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
 \lambda_s^{1+p^{e m_s-k}}=1
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

where `\mathcal F_s` is the set of distinct monic irreducible factors.

### 3.4 Component codes

The polynomial CRT gives

\[
A[x]/\langle x^n-\lambda\rangle
\cong
\prod_{s=1}^{N}K_s[x]/\langle M_s(x)\rangle.
\tag{3.7}
\]

A `lambda`-constacyclic `A`-code is therefore a tuple of ideals `C_s` in the component quotients.

For `J_s\subseteq\mathcal F_s`, define

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

(H6) every component satisfies `\lambda_s^{1+p^{e m_s-k}}=1`;

(H7) `M_s(x)=x^n-\lambda_s` is factored into distinct monic irreducibles `\mathcal F_s`;

(H8) the codes counted are exactly the distinct factor-selection ideals indexed by subsets `J_s\subseteq\mathcal F_s`, with no quotient by an equivalence or isometry group;

(H9) dimensions are reported over `K_s` componentwise and over `\mathbb F_q` globally, with weight `w_O=m_s d_O`.

Under (H1)–(H9), the proof must establish the factor permutation, dual-generator identity, hull-support formula, boundary formula, transfer-matrix product, total count, exact distribution, LCD count, and moment formulas.

### 3.7 Compatible and incompatible twists

The compatible case is precisely (H6). Then the root action `\alpha\mapsto\alpha^{-p^{e m_s-k}}` preserves the roots of `x^n-\lambda_s`, so the factor permutation and the main enumerator are defined.

If `\lambda_s^{1+p^{e m_s-k}}\ne1`, the component `k`-Galois dual is a `\lambda_s^{-p^{e m_s-k}}`-constacyclic code rather than a `\lambda_s`-constacyclic code. Its factors belong to a different modulus in general, so the same-factor-set orbit enumerator is not valid. This case is retained only as a diagnostic and as future work for a two-modulus/bipartite theory.

## 4. Definition and proof of the factor permutation

### 4.1 Normalized `k`-Galois reciprocal

For a monic polynomial

\[
f(x)=\sum_{i=0}^{d}f_i x^i\in K_s[x],
\qquad f_0\ne0,
\]

define the principal normalized reciprocal by applying the inverse Frobenius `\rho_{s,k}` to the coefficients:

\[
f^{\#_{s,k}}(x)
=f_0^{-p^{e m_s-k}}
\sum_{i=0}^{d}f_i^{p^{e m_s-k}}x^{d-i}.
\tag{4.1}
\]

The polynomial is monic. It is the inverse-Frobenius coefficient image of the ordinary normalized reciprocal. Therefore it is multiplicative on monic polynomials with nonzero constant term:

\[
(fg)^{\#_{s,k}}
=f^{\#_{s,k}}g^{\#_{s,k}}.
\tag{4.2}
\]

The operation preserves degree and irreducibility because coefficient application by `\rho_{s,k}` is a field automorphism and reciprocal reversal preserves irreducibility for nonzero constant term. Its inverse is obtained by applying `\sigma_{s,k}` to the reciprocal, so the operation is bijective.

### 4.2 Definition of `\tau_{s,k}` and preservation of the factor set

Define

\[
\boxed{
\tau_{s,k}:\mathcal F_s\to\mathcal F_s,
\qquad
\tau_{s,k}(f)=f^{\#_{s,k}}.
}
\tag{4.3}
\]

The codomain is justified as follows. If `\alpha` is a root of `f`, then the roots of `f^{\#_{s,k}}` are

\[
\alpha^{-p^{e m_s-k}}.
\]

Since `\alpha^n=\lambda_s`,

\[
(\alpha^{-p^{e m_s-k}})^n
=\lambda_s^{-p^{e m_s-k}}
=\lambda_s
\]

under the compatibility condition

\[
\lambda_s^{1+p^{e m_s-k}}=1.
\]

Thus every root of `f^{\#_{s,k}}` is a root of `M_s`, and irreducibility preservation gives

\[
\tau_{s,k}(\mathcal F_s)\subseteq\mathcal F_s.
\]

Because the reciprocal operation is invertible, the inclusion is equality:

\[
\boxed{\tau_{s,k}(\mathcal F_s)=\mathcal F_s.}
\tag{4.4}
\]

Thus `\tau_{s,k}` is a permutation of the finite irreducible-factor set.

### 4.3 `\tau_{s,k}` need not be an involution

Do not assume `\tau_{s,k}^2=id` in the general extension-field case. On roots, repeated application starts with

\[
\alpha\longmapsto\alpha^{-p^{e m_s-k}},
\]

and the next application uses the same inverse-Frobenius exponent, followed by the factor identification induced by the field automorphism. The resulting factor permutation can have orbit lengths larger than two.

Special cases are only checks, not hypotheses:

- for `k=0`, the inverse Frobenius is the identity on `K_s`, so the action is ordinary reciprocal;
- when the relevant Frobenius has order two, the Hermitian-type action is an involution;
- in general, arbitrary finite orbit lengths are permitted.

Let

\[
O=(f_0,f_1,\ldots,f_{a_O-1})
\]

be a `\tau_{s,k}`-orbit, indexed so that

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

The weight `w_O` is the contribution measured over `\mathbb F_q`.

## 5. Component dual and hull support — rigorous derivation

**Source scope note.** The finite-field dual-generator/lcm statement is identified in the literature audit as a source result, but the component-field statement below must be proved under the present dual-slot and inverse-Frobenius convention. Citation is not a substitute for this proof.

Fix a component `s`, and let

\[
M_s(x)=\prod_{f\in\mathcal F_s}f(x),
\qquad
 g_{J_s}(x)=\prod_{f\in J_s}f(x),
\qquad
 h_{J_s}(x)=\frac{M_s(x)}{g_{J_s}(x)}
 =\prod_{f\in\mathcal F_s\setminus J_s}f(x).
\]

All these factors are monic. Since `M_s` is square-free, the factor supports are unambiguous and the ideal generated by a divisor of `M_s` has `K_s`-dimension `n-\deg_{K_s}` of that divisor.

### LEMMA 5.1 — inverse-Frobenius dual generator

Under

\[
C_s^{\perp_k}
=\{x\in K_s^n:\langle c,x\rangle_{s,k}=0\text{ for every }c\in C_s\},
\]

the dual of `C_s(J_s)=\langle g_{J_s}\rangle` is

\[
\boxed{
C_s(J_s)^{\perp_k}
=\left\langle h_{J_s}^{\#_{s,k}}\right\rangle.
}
\tag{5.1}
\]

**Proof target, with the required translation made explicit.** Let `\rho=\rho_{s,k}`. Applying `\rho` to `\langle c,x\rangle_{s,k}=0` gives

\[
0=\rho\left(\sum_i c_i\sigma_{s,k}(x_i)\right)
=\sum_i\rho(c_i)x_i.
\tag{5.2}
\]

Thus `C_s(J_s)^{\perp_k}` is the ordinary Euclidean dual of the coefficientwise `\rho`-image of `C_s(J_s)`. That image is the ideal generated by `\rho(g_{J_s})` in

\[
K_s[x]/\langle x^n-\rho(\lambda_s)\rangle.
\]

The compatibility condition gives `\rho(\lambda_s)=\lambda_s^{-1}`. For an ordinary `a`-constacyclic code generated by a divisor `G` of `x^n-a`, the shift calculation and the polynomial Euclidean-dual lemma give a dual generated by the normalized ordinary reciprocal of the check polynomial `(x^n-a)/G`. Apply this standard lemma with `a=\rho(\lambda_s)` and `G=\rho(g_{J_s})`; its check polynomial is `\rho(h_{J_s})`. The ordinary normalized reciprocal of `\rho(h_{J_s})` is exactly `h_{J_s}^{\#_{s,k}}` by (4.1). Translating back through the coefficientwise bijection proves (5.1). The manuscript must include the ordinary constacyclic dual lemma and its shift calculation, rather than cite the conclusion without this argument.

By multiplicativity of the normalized reciprocal,

\[
\operatorname{Supp}\left(h_{J_s}^{\#_{s,k}}\right)
=\tau_{s,k}(\mathcal F_s\setminus J_s).
\tag{5.3}
\]

### LEMMA 5.2 — intersection and lcm support

In the square-free quotient `K_s[x]/\langle M_s\rangle`,

\[
\operatorname{Hull}_k(C_s(J_s))
=C_s(J_s)\cap C_s(J_s)^{\perp_k}
=\left\langle
\operatorname{lcm}\left(g_{J_s},h_{J_s}^{\#_{s,k}}\right)
\right\rangle.
\tag{5.4}
\]

**Proof.** For divisors of the square-free modulus, membership in the ideal generated by a divisor is equivalent to divisibility by that divisor modulo `M_s`. A residue class lies in both ideals exactly when it is divisible by both generators, hence by their least common multiple; the lcm still divides `M_s` because both factor supports are subsets of `\mathcal F_s`. This proves (5.4).

The lcm support is

\[
J_s\cup\tau_{s,k}(\mathcal F_s\setminus J_s).
\]

Therefore the factors omitted from the lcm are

\[
\begin{aligned}
\mathcal F_s\setminus
\bigl(J_s\cup\tau_{s,k}(\mathcal F_s\setminus J_s)\bigr)
&=(\mathcal F_s\setminus J_s)\cap
\bigl(\mathcal F_s\setminus\tau_{s,k}(\mathcal F_s\setminus J_s)\bigr)\\
&=(\mathcal F_s\setminus J_s)\cap\tau_{s,k}(J_s),
\end{aligned}
\tag{5.5}
\]

where the second equality uses that `\tau_{s,k}` is a bijection of `\mathcal F_s`.

### THEOREM 5.3 — component and global hull dimensions

For every `J_s\subseteq\mathcal F_s`,

\[
\boxed{
\dim_{K_s}\operatorname{Hull}_k(C_s(J_s))
=\sum_{f\in(\mathcal F_s\setminus J_s)\cap\tau_{s,k}(J_s)}
\deg_{K_s}f.
}
\tag{5.6}
\]

**Proof.** The ideal generated by a divisor `d` of `M_s` has `K_s`-dimension `n-\deg d`, so (5.4) says that the hull dimension is the degree of the factors omitted from the lcm. Equation (5.5) identifies those factors, and summing their degrees gives (5.6). Under the product decomposition, the global hull is the product of the component hulls. Since `[K_s:\mathbb F_q]=m_s`,

\[
\boxed{
\dim_{\mathbb F_q}\operatorname{Hull}_k(C)
=\sum_s m_s\dim_{K_s}\operatorname{Hull}_k(C_s).
}
\tag{5.7}
\]

This also proves the passage from component dimensions to the global `\mathbb F_q` dimension.

**Proof-completeness requirement.** The final manuscript must show the ordinary constacyclic dual lemma used in Lemma 5.1, the coefficientwise `\rho` translation, the lcm ideal argument, and the component-to-global dimension step. A direct computation can validate these statements on finite examples but cannot replace them.

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

The factor `f_{i+1}` belongs to the component hull support (5.5) exactly when

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

A convention using `0 -> 1`, namely `sum_i(1-epsilon_i)epsilon_{i+1}`, gives the same numerical count on a cyclic binary word, but (6.1) is the convention tied directly to the support set (5.5) and will be used everywhere.

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

### PROOF TARGET — THEOREM 7.1: transfer-matrix joint enumerator and total count

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

#### PROPOSITION 7.2 — total labeled-code count

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

### PROOF TARGET — THEOREM 8.1: exact hull-dimension distribution

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

### 9.2 — PROPOSITION 9.1: LCD count as a corollary

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

### 9.4 — PROPOSITION 9.2: global moments

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

## 10. Computational validations — inverse-Frobenius convention

The computations in this section are **COMPUTATIONAL VALIDATION**, not proofs of the general theorems. Every direct dual check uses the declared order

\[
C_s^{\perp_k}=\{x:\langle c,x\rangle_{s,k}=0\text{ for every }c\in C_s\}.
\]

For a direct linear-algebra computation, applying `\rho_{s,k}` to the equations gives

\[
\sum_i c_i^{p^{e m_s-k}}x_i=0.
\]

Thus the validators transform code rows by `\rho_{s,k}` before solving ordinary nullspace equations, and they compare the result with the generator using the same inverse-Frobenius exponent. This is the required dual-slot convention. The general identities still require the proofs listed in Sections 4–9.

### 10.1 F4 pilot: four square-free components

Take

\[
A=\mathbb F_4[u,v]/\langle u^2-u,v^2-v\rangle
\cong\mathbb F_4^4,
\qquad m_s=1,
\]

and choose

\[
q=4=2^2,
\qquad n=5,
\qquad \lambda=1,
\qquad k=1.
\]

Here

\[
\sigma_{s,k}=2,
\qquad
\rho_{s,k}=2^{e m_s-k}=2.
\]

The two exponents coincide in this pilot, but the validator still records the code-in-the-first-slot definition. Let `\omega^2+\omega+1=0`. In characteristic two,

\[
x^5-1=x^5+1
=(x+1)(x^2+\omega x+1)(x^2+(\omega+1)x+1).
\tag{10.1}
\]

The quadratic factors are exchanged by the principal `\rho=2` reciprocal and `x+1` is fixed. Each component therefore has one orbit of weight `1` and one orbit of length `2` and weight `2`.

The component joint enumerator, with `u` tracking actual `\mathbb F_4`-code dimension, is

\[
\mathscr E_{\mathrm{component}}(u,z)
=(u+1)(u^4+2u^2z^2+1).
\tag{10.2}
\]

For the four independent components,

\[
\mathscr E_A(u,z)
=\bigl((1+u)(1+2u^2z^2+u^4)\bigr)^4,
\tag{10.3}
\]

and

\[
H_A(z)=2^8(1+z^2)^4.
\tag{10.4}
\]

The hull histogram is

| hull dimension `h` | number of codes |
|---:|---:|
| `0` | `256` |
| `2` | `1024` |
| `4` | `1536` |
| `6` | `1024` |
| `8` | `256` |

The total is `4096=8^4`.

Run:

```bash
python code/validate_pilot.py
```

The inverse-convention output is:

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

### 10.2 F8 long orbit: `m_s=1` but non-involutory action

Take

\[
q=8=2^3,
\qquad K_s=\mathbb F_8,
\qquad m_s=1,
\qquad n=7,
\qquad \lambda=1,
\qquad k=1.
\]

Here

\[
\sigma_{s,k}=2,
\qquad
\rho_{s,k}=2^{e m_s-k}=2^2=4.
\]

Since `\mathbb F_8^\times` has order `7`, `x^7-1` splits into seven distinct linear factors. If `\alpha` is primitive and `f_j=x-\alpha^j`, the principal root action is

\[
\alpha^j\longmapsto\alpha^{-4j}=\alpha^{3j},
\]

so the ordered factor permutation is

\[
[0,3,6,2,5,1,4]
\]

with orbit lengths `[1,6]`. Every orbit weight is `1`. Hence

\[
H_{F_8}(z)
=P_{1,1}(z)P_{6,1}(z)
=4+60z+60z^2+4z^3.
\tag{10.5}
\]

The joint transfer enumerator is

\[
\mathscr E_{F_8}(u,z)
=(u+1)\operatorname{tr}
\left(
\begin{pmatrix}u&1\\uz&1\end{pmatrix}^{6}
\right).
\tag{10.6}
\]

Run:

```bash
python code/validate_long_orbit_examples.py
```

The relevant output is:

```text
Example A (m_s=1, orbit length 6):
  q=8, e=3, m_s=1, k=1, n=7
  sigma exponent p^k=2
  principal reciprocal/direct-dual rho exponent p^(e*m_s-k)=4
  tau permutation on root indices: [0, 3, 6, 2, 5, 1, 4]
  orbit lengths: [1, 6]
  orbit-boundary == transfer: True
  direct == theory: True
  hull histogram: {0: 4, 1: 60, 2: 60, 3: 4}
  PASS
```

The mean and variance are `3/2` and `3/8`, respectively. The inverse principal action is used in both the direct dual and the factor permutation; the earlier `p^k=2` ordering is not the principal ordering for this example.

### 10.3 F16 extension component and N2 base data

Let

\[
A=\mathbb F_4[u]/\langle u^2+u+\omega\rangle
\cong K_s=\mathbb F_{16}=\mathbb F_{4^2},
\qquad m_s=2,
\]

where `\omega^2+\omega+1=0` over `\mathbb F_4`. Choose

\[
q=4=2^2,
\qquad n=5,
\qquad \lambda=1,
\qquad k=1.
\]

The two Frobenius exponents are

\[
\sigma_{s,k}=2,
\qquad
\rho_{s,k}=2^{e m_s-k}=2^3=8.
\]

The five linear factors have inverse-Frobenius factor permutation

\[
[0,2,4,1,3]
\]

and orbit lengths `[1,4]`. Every factor has `K_s`-degree `1`, so every factor weight over `\mathbb F_4` is `w=2`. Consequently,

\[
H_{F_{16}/F_4}(z)
=P_{1,2}(z)P_{4,2}(z)
=4+24z^2+4z^4,
\tag{10.7}
\]

and

\[
\mathscr E_{F_{16}/F_4}(u,z)
=(u^2+1)\operatorname{tr}
\left(
\begin{pmatrix}u^2&1\\u^2z^2&1\end{pmatrix}^{4}
\right).
\tag{10.8}
\]

The hull histogram is `{0:4,2:24,4:4}`, the total is `2^5=32`, and the predicted mean and variance are `2` and `1`.

The validator output is:

```text
Example B (m_s=2, orbit length 4):
  q=4, e=2, m_s=2, k=1, n=5
  sigma exponent p^k=2
  principal reciprocal/direct-dual rho exponent p^(e*m_s-k)=8
  tau permutation on root indices: [0, 2, 4, 1, 3]
  orbit lengths: [1, 4]
  orbit-boundary == transfer: True
  direct == theory: True
  hull histogram: {0: 4, 2: 24, 4: 4}
  PASS
ALL LONG-ORBIT AND m_s>1 VALIDATIONS PASS
```

### 10.4 Compatible nontrivial-`\lambda` validation

Take

\[
q=4=2^2,
\qquad K_s=\mathbb F_4,
\qquad n=5,
\qquad \lambda=\omega\ne1,
\qquad k=1.
\]

Here `m_s=1`, so `sigma=2` and `rho=2`; compatibility is

\[
\lambda^{1+\rho}=\omega^3=1.
\]

The verified factorization is

\[
x^5-\omega
=(x+\omega+1)(x^2+x+\omega)(x^2+\omega x+\omega).
\tag{10.9}
\]

The principal factor permutation is `[0,2,1]`, with orbit lengths `[1,2]`. All `2^3=8` factor selections are checked by direct nullspace duals using the declared slot order, by the inverse-Frobenius generator `h^{\#_{s,k}}`, by the hull-support boundary formula, and by the transfer matrix. The joint histogram is

\[
\{(0,0):1,(1,0):1,(2,2):2,(3,2):2,(4,0):1,(5,0):1\},
\]

and the hull histogram is `{0:4,2:4}`. The joint enumerator is

\[
\mathscr E_{\omega}(u,z)
=(u+1)(u^4+2u^2z^2+1).
\tag{10.10}
\]

Run:

```bash
python code/validate_nontrivial_constacyclic.py
```

Output:

```text
nontrivial compatible constacyclic example:
  q=4, n=5, lambda=omega != 1, k=1, sigma=2, rho=2
  factorisation: x + omega+1 * x^2 + x + omega * x^2 + (omega)x + omega
  square-free: True
  lambda^(1+rho)= 1 = 1
  tau permutation: [0, 2, 1]
  orbit lengths: [1, 2]
  direct dual-generator checks: 8 of 8
  direct == orbit-boundary: True
  orbit-boundary == transfer: True
  joint histogram: {(0, 0): 1, (1, 0): 1, (2, 2): 2,
                    (3, 2): 2, (4, 0): 1, (5, 0): 1}
  hull histogram: {0: 4, 2: 4}
PASS: nontrivial compatible constacyclic validation
```

### 10.5 Incompatible-twist boundary diagnostic

Take

\[
q=4=2^2,
\qquad K_s=\mathbb F_4,
\qquad n=5,
\qquad \lambda=\omega,
\qquad k=0.
\]

Here

\[
\sigma_{s,0}=1,
\qquad
\rho_{s,0}=2^{e m_s}=4,
\]

and `rho` is the identity on `\mathbb F_4`. Thus

\[
\lambda^{1+\rho}=\omega^2\ne1,
\qquad
\lambda^{-\rho}=\lambda^{-1}=\omega^2\ne\omega.
\]

For

\[
C=\langle x^2+x+\omega\rangle
\subseteq \mathbb F_4[x]/\langle x^5-\omega\rangle,
\]

the direct dual agrees with `\langle h^{\#_{s,k}}\rangle`, is `\lambda^{-\rho}`-constacyclic, and is not `\lambda`-constacyclic. No transfer-matrix enumeration is attempted.

Run:

```bash
python code/diagnose_incompatible_twist.py
```

Output:

```text
incompatible-twist diagnostic:
  q=4, n=5, lambda=omega, k=0, sigma=1, rho=4
  lambda^(1+rho)= 3 != 1
  lambda^(-rho)= 3 != lambda
  direct dual equals <h^(#)>: True
  direct dual is lambda^(-rho)-constacyclic: True
  direct dual is lambda-constacyclic: False
  No transfer-matrix enumeration was attempted.
PASS: incompatible twist correctly left outside the theorem
```

**Scope boundary.** If compatibility fails, the dual has twist `\lambda_s^{-p^{e m_s-k}}` in general, so its factors belong to a different modulus. The same-factor-set orbit enumerator is not applied. A two-modulus or bipartite extension is **FUTURE WORK**, not an unproved consequence of the compatible theorem.

### 10.6 N1 status: do not invent an output

N1 is retained as a required exhaustive test with

\[
q=16,
\qquad n=15,
\qquad 2^{15}=32,768\text{ factor selections}.
\]

Its complete `k`, twist, factorization, orbit data, histogram, and direct-dual output are not available in the current verified record. The manuscript must mark this item exactly:

> **VERIFY BEFORE MANUSCRIPT FINALIZATION**

No numerical N1 conclusion, histogram, or PASS claim is made here.

### 10.7 N2: direct dual, correct `rho=8`, incorrect `p^k=2`

N2 uses exactly

\[
K=\mathbb F_{16}=\mathbb F_{4^2},
\qquad q=4,
\qquad e=2,
\qquad m_s=2,
\qquad n=5,
\qquad \lambda=1,
\qquad k=1,
\]

so that

\[
\sigma_{s,k}(a)=a^2,
\qquad
\rho_{s,k}(a)=a^8.
\]

The validator compares:

- **A. Direct dual:** solve the declared equations `\langle c,x\rangle_{s,k}=0` for every codeword `c`; equivalently solve `\rho(c)\cdot x=0` after applying `rho` to the equations.
- **B. Correct reciprocal:** generate the dual with `h^{\#_{s,k}}` using exponent `8`.
- **C. Incorrect reciprocal:** generate the candidate dual with exponent `2`, namely the stale `p^k` formula.

The correct and incorrect ordered factor permutations are

\[
\tau_{\rho=8}=[0,2,4,1,3],
\qquad
\tau_{p^k=2}=[0,3,1,4,2].
\]

Run:

```bash
python code/validate_n2_extension_convention.py
```

The complete output is:

```text
N2 extension-field convention validation:
  K=F_16=F_(4^2), q=4, e=2, m_s=2, n=5, lambda=1, k=1
  sigma=p^k=2, rho=p^(e*m_s-k)=8
  correct rho reciprocal permutation: [0, 2, 4, 1, 3]
  incorrect p^k reciprocal permutation: [0, 3, 1, 4, 2]
  A direct dual from <c,x>_k checked: 32 of 32
  A equals B (rho=8 reciprocal): 32 of 32
  A equals C (incorrect p^k=2 reciprocal): 8 of 32
  A differs from C: 24 of 32
  example differing selections: [2, 3, 4]
PASS: A=B for all 32; C differs for at least one code
```

This is the required convention-separating validation. It is a finite **COMPUTATIONAL VALIDATION** of the declared orientation and does not replace the general dual-generator proof.

### 10.8 Computational verification table

| Test | Parameters and status | Exhaustive scope | Result status |
|---|---|---:|---|
| F4 pilot | `q=4`, `n=5`, `\lambda=1`, `k=1`, four `F_4` components | `8^4=4096` ring codes plus component checks | **COMPUTATIONAL VALIDATION**: PASS |
| F8 long orbit | `q=8`, `n=7`, `m_s=1`, `k=1`, `rho=4`; orbit lengths `[1,6]` | `2^7=128` codes | **COMPUTATIONAL VALIDATION**: PASS |
| F16 extension | `K=F_{16}=F_{4^2}`, `n=5`, `k=1`, `rho=8`; orbit lengths `[1,4]` | `2^5=32` codes | **COMPUTATIONAL VALIDATION**: PASS |
| Compatible nontrivial twist | `q=4`, `n=5`, `\lambda=\omega`, `k=1`; orbit lengths `[1,2]` | `2^3=8` codes | **COMPUTATIONAL VALIDATION**: PASS, 8/8 dual checks |
| Incompatible diagnostic | `q=4`, `n=5`, `\lambda=\omega`, `k=0`; incompatible | one selected code; no enumerator | **COMPUTATIONAL VALIDATION**: diagnostic PASS only |
| N1 | `q=16`, `n=15`, 32,768 selections | `2^{15}` | **VERIFY BEFORE MANUSCRIPT FINALIZATION** |
| N2 | `K=F_{16}=F_{4^2}`, `sigma=2`, `rho=8`, `n=5`, `\lambda=1` | all `32` selections and A/B/C comparison | **COMPUTATIONAL VALIDATION**: PASS |

Computational validation is evidence for the listed finite instances only. It never substitutes for the theorem-level proofs.

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

For a direct linear-algebra check, the dual can be computed from the defining constraints

\[
\sum_i c_i x_i^{p^k}=0
\]

for each generator row `c` of the code. Applying `\rho_{s,k}` gives the ordinary linear nullspace constraints

\[
\sum_i c_i^{p^{e m_s-k}}x_i=0.
\]

The calculation must be over the correct component field, then weighted by `m_s` when reported over `F_q`.

Minimum test family:

- the existing verified `F_4` pilot (unchanged);
- Example A with `q=8`, `m_s=1`, and an orbit of length `6`;
- Example B with `q=4`, `m_s=2`, and an orbit of length `4`;
- a product of split components;
- unequal extension degrees `m_s`;
- a fixed factor plus a 2-cycle;
- the nontrivial compatible `lambda=omega` example in Section 10.4;
- the incompatible-twist diagnostic in Section 10.5 (diagnostic only; no enumerator);
- N2 in Section 10.7, including A=B under rho and the incorrect p^k comparison;
- Euclidean and order-two Hermitian-type special cases.

The computational experiment validates only the listed finite instances; it does not replace the mathematical proof of the general theorem.

---

## 12. Phase-by-phase execution plan

### Phase 0 — Mathematical and literature audit

**Duration:** 2–3 days

Tasks:

- Read the supplied paper and mark results as `cite`, `use as lemma`, or `do not reproduce`.
- Record the extension-field convention-translation issue explicitly and keep `\rho_{s,k}` principal for the reciprocal and dual generator; retain `p^k` only in the second slot.
- Freeze the main hypotheses: square-free algebra, `gcd(n,p)=1`, and (3.5).
- Search recent literature for exact multiplicity/joint enumerator results.
- Keep “inequivalent codes” and quantum constructions outside the main claim until proved.

**Deliverable:** gap matrix plus one-page problem statement.

**Go/no-go:** If exact same joint enumerator already exists, change the contribution before drafting.

### Phase 1 — Algebra and notation

**Duration:** 4–6 days

- Prove or cite the product decomposition (3.1).
- Define `K_s`, `m_s`, `\eta_s`, component dimensions, and the componentwise inner product.
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

- Define `g_{J_s}` and `h_{J_s}`.
- Prove the dual support is `\tau_{s,k}(\mathcal F_s\setminus J_s)`.
- Prove the hull is generated by the lcm.
- Derive exactly `(\mathcal F_s\setminus J_s)\cap\tau_{s,k}(J_s)`.
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

- Run the existing pilot, long-orbit, extension-field, nontrivial-`lambda`, and N2 scripts.
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

The direct enumeration of all factor selections has `2^{sum_s |\mathcal F_s|}` cases. The transfer-matrix method avoids this explicit enumeration.

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
3. **`k`-Galois reciprocal and factor permutation:** second-slot inner product, inverse-Frobenius reciprocal `\rho_{s,k}`, root action, compatibility, and proof that `\tau_{s,k}(\mathcal F_s)=\mathcal F_s`.
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
Proof tau_{s,k}(\mathcal F_s)=\mathcal F_s
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
| Normalized reciprocal (4.1)–(4.2) | Prove monicity, multiplicativity, degree preservation, irreducibility preservation, and invertibility under the inverse-Frobenius exponent `p^{e m_s-k}` | A script may compare factors but cannot replace these polynomial arguments. |
| Factor permutation (4.3)–(4.6) | Prove the root action `alpha -> alpha^{-p^{e m_s-k}}`, use `lambda_s^{1+p^{e m_s-k}}=1`, and prove the inclusion is a bijection | An orbit listing validates only the selected finite field. |
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

Use the rigorous component version (3.2)–(3.5). The inner product uses `p^k` on its second slot, while the declared code-first dual translates the equations by `\rho_{s,k}`; the principal reciprocal, root action, compatibility, dual generator, and incompatible twist therefore use `p^{e m_s-k}`. Translate any source formula before using it.

### Risk 2: `tau` has long cycles and the intended application only has pairs

Keep arbitrary cycles in the theorem. Treat fixed points and 2-cycles as special corollaries.

### Risk 3: Incompatible twist

If `lambda_s^{1+p^{e m_s-k}} != 1`, the dual is a `lambda_s^{-p^{e m_s-k}}`-constacyclic code. Do not force it into the same factor set. Either develop a two-polynomial/bipartite version or state it as future work.

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
- [ ] The inner-product Frobenius is `\sigma_{s,k}(a)=a^{p^k}`, and the principal reciprocal/dual convention uses `\rho_{s,k}(a)=a^{p^{e m_s-k}}`, including the `k=0` case.
- [ ] The split case `m_s=1` is explicitly identified.
- [ ] `tau_{s,k}` is defined by equation (4.1).
- [ ] `\tau_{s,k}(\mathcal F_s)=\mathcal F_s` is proved from the root action and compatibility.
- [ ] General orbit lengths are allowed.
- [ ] The hull support is derived as `(\mathcal F_s\setminus J_s)\cap\tau_{s,k}(J_s)`.
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
- [ ] N2 confirms A=B for all 32 selections under rho=8 and records that the p^k=2 candidate differs on 24.
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
| 3 | Precise factor permutation | Lemmas for `\tau_{s,k}(\mathcal F_s)=\mathcal F_s` and orbit lengths |
| 4 | Dual/hull support proof | Section 4–5 draft |
| 5 | Boundary statistic and transfer matrix | Main enumerator theorem |
| 6 | Explicit coefficients and moments | Distribution/corollaries |
| 7 | Exhaustive computational validation | scripts and exact tables |
| 8 | Optional Burnside or quantum section | only if fully justified |
| 9 | Full proof audit and originality review | submission-ready blueprint/manuscript |

If an optional section is incomplete at Week 8, omit it rather than weakening the main theorem.

---

## 20A. Reference and literature verification ledger

**Audit date:** 23 September 2026. The DOI and publisher records were rechecked where a publisher landing page or abstract was available. The categories below must not be conflated:

- **THEOREM-LEVEL VERIFIED:** the relevant full text was inspected and the exact theorem/claim was checked. No external record below is assigned this category for the present blueprint unless a future full-text audit explicitly upgrades it.
- **PUBLISHER/ABSTRACT VERIFIED:** the DOI, bibliographic identity, and broad scope are confirmed on a publisher page or abstract; exact theorem overlap is not thereby verified.
- **METADATA-ONLY:** bibliographic/DOI metadata was located, but the publisher abstract or relevant full text was not checked in this audit.
- **DOI UNVERIFIED:** no reliable DOI was confirmed; do not insert one by inference.

Every theorem-level comparison and every claim that a source does or does not contain the present enumerator remains **VERIFY BEFORE MANUSCRIPT FINALIZATION** unless explicitly upgraded to **THEOREM-LEVEL VERIFIED**.

| Record | DOI and bibliographic check | Verification category | Safe use in this blueprint |
|---|---|---|---|
| Debnath, Prakash, Islam, “Galois hulls of constacyclic codes over finite fields,” *Cryptography and Communications* 15 (2023), 111–127 | `10.1007/s12095-022-00591-6`; publisher record confirms title, authors, volume/pages, DOI, and 2023 issue. The correction is `10.1007/s12095-022-00602-6`, publisher record confirms 15 (2023), 129–130. | **PUBLISHER/ABSTRACT VERIFIED**; exact theorem comparison **VERIFY BEFORE MANUSCRIPT FINALIZATION** | Cite only for the abstract-level finite-field constacyclic hull/counting scope until the correction and full text are checked theorem by theorem. |
| Debnath, Islam, Martínez-Moro, Prakash, “Galois hulls of constacyclic codes over affine algebra rings,” *Discrete Mathematics* 349(2) (2026), Article 114750 | `10.1016/j.disc.2025.114750`; ScienceDirect record confirms title, authors, February 2026 issue, article number, DOI, and abstract scope. | **PUBLISHER/ABSTRACT VERIFIED**; supplied PDF theorem labels **VERIFY BEFORE MANUSCRIPT FINALIZATION** | Use for the broad square-free affine `k`-Galois dual/hull/LCD/quantum scope; do not attribute an exact transfer enumerator or exact theorem numbering yet. |
| Debnath, Prakash, “Average dimensions of Galois hulls of constacyclic codes,” *Advances in Mathematics of Communications* 19(6) (2025), 1569–1604 | `10.3934/amc.2025010`; AIMS record confirms title, authors, volume/issue/pages, DOI, and abstract. | **PUBLISHER/ABSTRACT VERIFIED**; theorem-level overlap **VERIFY BEFORE MANUSCRIPT FINALIZATION** | Use for average-dimension and `R_{m,q}` scope, not as evidence for the present all-code bivariate product. |
| Debnath, Islam, Yadav, Prakash, “Study of small Galois hull dimensions of constacyclic codes,” *Advances in Mathematics of Communications* 22 (2026), 1–18 | `10.3934/amc.2025054`; AIMS record confirms title, authors, volume/pages, DOI, and abstract. | **PUBLISHER/ABSTRACT VERIFIED**; theorem-level overlap **VERIFY BEFORE MANUSCRIPT FINALIZATION** | Use for dimensions one and two and the conditional EAQECC scope only. |
| Sangwisut, Jitman, Ling, Udomkavanich, “Hulls of cyclic and negacyclic codes over finite fields,” *Finite Fields and Their Applications* 33 (2015), 232–257 | `10.1016/j.ffa.2014.12.008`; ScienceDirect record confirms title, authors, journal, volume/pages, DOI, and abstract describing hull dimensions and fixed-dimension enumerations. | **PUBLISHER/ABSTRACT VERIFIED**; exact theorem translation **VERIFY BEFORE MANUSCRIPT FINALIZATION** | Use for related cyclic/negacyclic finite-field scope; do not claim exact identity with the present Galois product theorem. |
| Jitman, Sangwisut, “The average dimension of the Hermitian hull of constacyclic codes over finite fields of square order,” *Advances in Mathematics of Communications* 12(3) (2018), 451–463 | `10.3934/amc.2018027` is retained from the bibliographic record; the publisher abstract/full-text check remains incomplete. | **METADATA-ONLY**; DOI/title and theorem scope **VERIFY BEFORE MANUSCRIPT FINALIZATION** | Use only as a lead for the Hermitian average-dimension comparison until the publisher record is checked directly. |
| Jitman, Sangwisut, “Hulls of cyclic codes over `\mathbb F_2+v\mathbb F_2`,” *Thai Journal of Mathematics* 18 (2020), 135–144 | No DOI was confirmed in the publisher record available to the audit. | **DOI UNVERIFIED**; theorem-level record **VERIFY BEFORE MANUSCRIPT FINALIZATION** | Retain the ring-specific comparison only with the exact marker; do not guess a DOI. |
| Tian, Gao, Gao, “Hulls of constacyclic codes over finite non-chain rings and their applications in quantum codes construction,” *Quantum Information Processing* 23 (2024), Article 9 | `10.1007/s11128-023-04230-8` retained from the publisher/index metadata; direct abstract-page recheck remains required. | **METADATA-ONLY**; publisher/abstract and theorem scope **VERIFY BEFORE MANUSCRIPT FINALIZATION** | Use only for a related two-component/non-chain quantum setting until the publisher page is checked directly. |
| Yadav, Singh, Islam, Prakash, Solé, “Hermitian hull of constacyclic codes over a class of non-chain rings and new quantum codes,” *Computational and Applied Mathematics* 43 (2024), Article 269 | `10.1007/s40314-024-02789-1`; Springer record confirms title, authors, volume/article, DOI, and abstract. | **PUBLISHER/ABSTRACT VERIFIED**; exact theorem overlap **VERIFY BEFORE MANUSCRIPT FINALIZATION** | Use for the specified Hermitian non-chain-ring scope; quantum claims remain conditional. |
| Liu, Pan, “Galois hulls of linear codes over finite fields,” *Designs, Codes and Cryptography* 88(2) (2020), 241–255 | `10.1007/s10623-019-00681-2`; Springer record confirms title, authors, volume/pages, DOI, and abstract. | **PUBLISHER/ABSTRACT VERIFIED**; exact theorem use checked only at abstract level | Use for general Galois-hull methods and invariance context, not for the constacyclic product enumerator. |
| Chen, Fan, Lin, Liu, “Constacyclic codes over finite fields,” *Finite Fields and Their Applications* 18(6) (2012), 1217–1231 | `10.1016/j.ffa.2012.10.001` retained from DOI metadata; direct publisher abstract check remains incomplete. | **METADATA-ONLY**; theorem scope **VERIFY BEFORE MANUSCRIPT FINALIZATION** | Use only for standard constacyclic background after direct verification. |
| Li, Hou, Gao, Ma, Mi, “Hulls of `\mathbb Z_4`-double cyclic codes,” *Computational and Applied Mathematics* 44 (2025), Article 423 | `10.1007/s40314-025-03385-7`; Springer record confirms title, article 423, volume/year, DOI, and abstract scope. | **PUBLISHER/ABSTRACT VERIFIED**; exact theorem overlap **VERIFY BEFORE MANUSCRIPT FINALIZATION** | Use for a related `\mathbb Z_4` double-cyclic enumeration, not for the reduced affine-field theorem. |
| Shukla, Pandey, Mishra, Pathak, Upadhyay, “Hulls of `\mathbb Z_p\mathbb Z_p[v]`-cyclic codes and construction of EAQECCs,” *Advances in Mathematics of Communications* 20 (2026), 209–238 | `10.3934/amc.2025037`; AIMS record confirms title/DOI and abstract scope. | **PUBLISHER/ABSTRACT VERIFIED**; exact theorem overlap **VERIFY BEFORE MANUSCRIPT FINALIZATION** | Use for a ring-specific quantum comparison only. |
| Jitman, Sangwisut, Udomkavanich, “Hulls of cyclic codes over `\mathbb Z_4`,” *Discrete Mathematics* 343(1) (2020), Article 111621 | `10.1016/j.disc.2019.111621` retained from bibliographic metadata; direct publisher abstract check remains incomplete. | **METADATA-ONLY**; theorem scope **VERIFY BEFORE MANUSCRIPT FINALIZATION** | Use only for ring-specific background after direct verification. |
| Dougherty, Saltürk, “The number of codes over rings of order 4 containing a hull of given type,” *Advances in Mathematics of Communications* 19(1) (2025), 11–35 | `10.3934/amc.2023031` retained from bibliographic metadata; direct publisher abstract check remains incomplete. | **METADATA-ONLY**; theorem scope **VERIFY BEFORE MANUSCRIPT FINALIZATION** | Use only for the broad order-four hull-type enumeration comparison. |
| Ding, Lu, “Galois hulls of cyclic codes over finite fields,” *IEICE Transactions on Fundamentals* 103-A(1) (2020), 370–375 | `10.1587/transfun.2019EAL2087` retained from bibliographic metadata; direct publisher abstract check remains incomplete. | **METADATA-ONLY**; theorem scope **VERIFY BEFORE MANUSCRIPT FINALIZATION** | Use only for cyclic Galois-hull background after direct verification. |
| Fan, Zhang, “Galois self-dual constacyclic codes,” *Designs, Codes and Cryptography* 84(3) (2017), 473–492 | `10.1007/s10623-016-0282-8` retained from bibliographic metadata; direct publisher abstract check remains incomplete. | **METADATA-ONLY**; theorem scope **VERIFY BEFORE MANUSCRIPT FINALIZATION** | Use for the origin/background of Galois constacyclic duality only after direct verification. |
| Guenda, Jitman, Gulliver, “Constructions of good entanglement-assisted quantum error correcting codes,” *Designs, Codes and Cryptography* 86(1) (2018), 121–136 | `10.1007/s10623-017-0330-z`; publisher record confirms title, authors, volume/pages, DOI, and abstract linking EAQECC entanglement to classical hulls. | **PUBLISHER/ABSTRACT VERIFIED**; use of exact construction theorem **VERIFY BEFORE MANUSCRIPT FINALIZATION** | Keep quantum discussion conditional and secondary; independently verify every parameter. |
| Carlet, Li, Mesnager, “Linear codes with small hulls in semi-primitive case,” *Designs, Codes and Cryptography* 87 (2019), 3063–3075 | `10.1007/s10623-019-00663-4` retained from bibliographic metadata; direct publisher abstract check remains incomplete. | **METADATA-ONLY**; theorem scope **VERIFY BEFORE MANUSCRIPT FINALIZATION** | Use only for general small-hull context after direct verification. |
| Zhang, Kong, Zheng, “Quantum Codes from Galois Hulls of Constacyclic Codes over a Finite Non-Chain Ring,” *Entropy* 28(4) (2026), Article 407 | `10.3390/e28040407`; MDPI record confirms title, authors, journal issue/article, DOI, and publisher page. | **PUBLISHER/ABSTRACT VERIFIED**; exact construction/theorem comparison **VERIFY BEFORE MANUSCRIPT FINALIZATION** | Use as a related ring-specific quantum record only; do not infer a classical minimum distance from the hull distribution. |

The supplied local PDF remains a source input, but its text is not locally extractable. The final manuscript must replace every provisional source theorem label with a checked theorem-level citation or remove the label. No DOI or theorem statement may be upgraded merely because it appears in a secondary citation.

## 21. Immediate next actions

1. Keep `code/validate_pilot.py`, `code/validate_long_orbit_examples.py`, `code/validate_nontrivial_constacyclic.py`, `code/diagnose_incompatible_twist.py`, and `code/validate_n2_extension_convention.py` under version control and attach all outputs to the research notes.
2. Prove and implement the `K_s` version with the declared code-first dual slot: `p^k` remains in the inner product and `rho_{s,k}` is principal for the reciprocal and dual generator.
3. Retain Example A as the genuine long-orbit test; do not infer long-cycle behavior from the `F_4`, Hermitian, 2-cycle pilot.
4. Prove Lemma 5.1 and Theorem 5.3 in full before writing the transfer-matrix section.
5. Derive the `a=1,...,5` orbit polynomials in the paper or an appendix.
6. Keep Burnside and quantum applications explicitly optional until their hypotheses are checked.
7. Complete the publisher-level literature audit, verify all references/DOIs, and resolve every `VERIFY BEFORE MANUSCRIPT FINALIZATION` marker before submission.
8. Run N2 and report its A=B/C comparison; keep N1 marked `VERIFY BEFORE MANUSCRIPT FINALIZATION` until its parameters and output exist.
9. Run a final global search for any stale `p^k` principal reciprocal, root action, compatibility, dual-generator, or incompatible-twist formula.

## 22. Global proof and notation quality-control checklist

Before manuscript submission, verify all of the following:

- `\sigma_{s,k}=p^k` is used only in the second slot of the declared inner product.
- `\rho_{s,k}=p^{e m_s-k}` is used consistently in the principal reciprocal, dual generator, root action, compatibility, incompatible twist, and direct-dual validator; N2 explicitly contrasts it with `p^k`.
- The proof of `\tau_{s,k}(\mathcal F_s)=\mathcal F_s` is complete.
- Reciprocal multiplicativity, irreducibility preservation, and invertibility are proved.
- The dual-generator identity `\langle h_{J_s}^{\#_{s,k}}\rangle` is proved, not inferred from computations.
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
- The compatibility condition is checked componentwise; the incompatible twist is `\lambda_s^{-p^{e m_s-k}}` and receives no compatible enumerator.
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

## CHANGELOG

- **Mathematical corrections:** Replaced the principal reciprocal, root action, compatibility condition, dual generator, and incompatible twist with the inverse-Frobenius `\rho_{s,k}` convention and made the code-first dual-slot proof explicit.
- **Notation corrections:** Replaced primitive idempotents by `\eta_s`, reserved `e` for `q=p^e`, and used `\mathcal F_s` exclusively for component factor sets.
- **Literature/reference corrections:** Added explicit theorem-level, publisher/abstract, metadata-only, and DOI-unverified categories; downgraded unresolved source theorem labels and DOI claims to `VERIFY BEFORE MANUSCRIPT FINALIZATION`.
- **Novelty corrections:** Removed unsupported priority language, kept labeled-code enumeration as the main scope, and left Burnside/equivalence classes and quantum applications conditional or future work.
- **Validation corrections:** Rebuilt the validators under the inverse convention, added N2, verified A=B for all 32 `\mathbb F_{16}` selections, recorded the incorrect `p^k=2` match count as 8/32, and retained N1 as unverified.
