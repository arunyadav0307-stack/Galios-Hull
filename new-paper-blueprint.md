# Exact Enumeration of `k`-Galois Hull Dimensions of Constacyclic Codes over Square-Free Affine Algebras

> **Status:** Revised mathematical blueprint after an explicit audit of the factor action, hull support, transfer matrix, orbit polynomial, moments, pilot example, complexity statement, Burnside section, and quantum-code claims.
>
> **Base paper:** `Galois hulls of constacyclic codes over affine algebra rings` (the supplied PDF).
>
> **Positioning:** The main object is an exact **enumerator**. The phrase “cycle-index method” has been removed from the title because factor cycles alone do not constitute a Pólya cycle-index construction.

---

## 0. Audit findings — what was corrected and why

The previous framework had the right research direction, but several statements needed to be made conditional or proved more carefully.

### Correction A — title and positioning

The earlier title used “Cycle-Index Method.” The revised title is:

> **Exact Enumeration of `k`-Galois Hull Dimensions of Constacyclic Codes over Square-Free Affine Algebras**

A shorter alternative, if the bivariate result is emphasized, is:

> **Joint Enumeration of Code and `k`-Galois Hull Dimensions for Constacyclic Codes over Square-Free Affine Algebras**

The actual framework uses factor orbits, transfer matrices, and generating functions. A genuine Burnside/Pólya cycle-index construction is only optional and is not assumed in the main theorem.

### Correction B — extension-field components need their own inverse Frobenius

If

\[
A\cong\prod_{s=1}^{N}K_s,
\qquad K_s=\mathbb F_{q^{m_s}},
\]

then the map `a -> a^(p^k)` on `K_s` has inverse

\[
a\longmapsto a^{p^{e m_s-k}},
\]

not always `a -> a^(p^{e-k})`. The latter is the correct exponent in the split case `m_s=1`.

Therefore the rigorous general framework below uses

\[
\rho_s=p^{e m_s-k}
\]

as the inverse-Frobenius exponent on `K_s`. In the pilot example every component is `F_4`, so `m_s=1` and `rho_s=2^{2-1}=2` exactly.

This correction is mathematically necessary because the supplied paper sometimes writes the simple components as if their coefficients were in `F_q`, even though a general square-free quotient can contain extension-field components.

### Correction C — the factor permutation is now explicit

For a monic factor

\[
f(x)=\sum_{i=0}^{d}f_i x^i,
\qquad f_0\ne0,
\]

define the normalized `k`-Galois reciprocal over `K_s` by

\[
f^{\#_{s,k}}(x)
=f_0^{-\rho_s}\sum_{i=0}^{d}f_i^{\rho_s}x^{d-i}.
\tag{0.1}
\]

Then

\[
\tau_{s,k}(f):=f^{\#_{s,k}}
\]

is the precise factor map used in the paper. Its root action is

\[
\alpha\longmapsto \alpha^{-\rho_s}
=\alpha^{-p^{e m_s-k}}.
\]

The compatibility condition for the same constacyclic polynomial is

\[
\lambda_s^{1+\rho_s}=1.
\tag{0.2}
\]

Under (0.2), `tau` maps the factor set to itself. It is a permutation, but it is **not assumed to be an involution**. General orbit lengths are allowed.

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

The new script `code/validate_long_orbit_examples.py` verifies:

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
\widetilde T_w(u,z)=
\begin{pmatrix}
 u^w&1\\
 u^w z^w&1
\end{pmatrix}.
\tag{0.6}
\]

The old matrix remains useful as a codimension enumerator, but it must not be used while claiming that `u` tracks `dim(C)`. The revised theorem uses `\widetilde T_w`. In the `F_4` pilot the final polynomial happens to be unchanged because the factor-degree polynomial is palindromic; the matrix interpretation is nevertheless different and must be stated correctly.

---

## 1. Research question and novelty

### What the supplied paper establishes

The supplied paper studies `k`-Galois duals and hulls of `lambda`-constacyclic codes over an affine algebra. Its main path is:

1. decompose the algebra using primitive idempotents;
2. reduce to component constacyclic codes;
3. describe dual and hull generators;
4. obtain a formula for the hull dimension of a selected code;
5. give LCD conditions and quantum-code examples.

### New research question

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

## 2. Current-literature positioning

A final novelty audit must be repeated immediately before submission. The relevant starting points are:

- the supplied affine-algebra paper: [arXiv:2412.08512](https://arxiv.org/html/2412.08512);
- related average-dimension work: [AIMS article](https://www.aimsciences.org//article/doi/10.3934/amc.2025010);
- recent small-hull work: [Study of small Galois hull dimensions](https://www.aimsciences.org/article/doi/10.3934/amc.2025054);
- recent non-chain-ring quantum work: [MDPI article](https://www.mdpi.com/1099-4300/28/4/407).

Do not position the new paper merely as:

- another ring-specific hull formula;
- an average-dimension calculation only;
- a table of EAQECCs;
- a repeated statement of the dual-generator formula.

The distinct target is **exact multiplicity and joint enumeration** in the square-free affine-algebra setting.

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

is an automorphism whose inverse is

\[
\sigma_{s,k}^{-1}(a)=a^{p^{e m_s-k}}.
\tag{3.3}
\]

Write

\[
\rho_s=p^{e m_s-k}.
\]

When `m_s=1`, this becomes the familiar exponent `p^{e-k}` used over `F_q`.

### 3.3 Constacyclic polynomial

Let

\[
\lambda=(\lambda_1,\ldots,\lambda_N)\in A^\times,
\qquad \lambda_s\in K_s^\times.
\]

For the main theorem assume

\[
\gcd(n,p)=1
\tag{3.4}
\]

and the same-twist compatibility condition

\[
\lambda_s^{1+\rho_s}=1
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

---

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
=f_0^{-\rho_s}\sum_{i=0}^{d}f_i^{\rho_s}x^{d-i},
\qquad \rho_s=p^{e m_s-k}.
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
\alpha^{-\rho_s}=\alpha^{-p^{e m_s-k}}.
\]

Since `alpha^n=lambda_s`,

\[
(\alpha^{-\rho_s})^n
=\lambda_s^{-\rho_s}
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
\alpha\longmapsto \alpha^{-p^{e m_s-k}}
\longmapsto \alpha^{p^{2(e m_s-k)}}
\longmapsto\cdots,
\]

up to the factor identification by the `K_s`-Frobenius action. The resulting permutation can have orbit lengths larger than two.

Special cases:

- `k=0`: the inverse-Frobenius operation is the identity on `K_s`, so this becomes the ordinary reciprocal map and is an involution.
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

This is the component-field version of the standard constacyclic dual-generator calculation; it uses the inverse of the semilinear map `a -> a^(p^k)`, namely the exponent `rho_s` from (3.3).

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
\widetilde T_w(u,z)_{r,t}
=u^{w(1-t)}z^{wr(1-t)}.
\]

With rows and columns indexed by `0,1`, this is

\[
\boxed{
\widetilde T_w(u,z)=
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
1&u^w\\z^w&u^w
\end{pmatrix}
\tag{7.2}
\]

is also valid, but its `u`-exponent tracks the selected-factor degree, i.e. the `F_q`-codimension of the code. If `L=n\dim_{\mathbb F_q}A` is the ambient length over `F_q`, then the corresponding global enumerators satisfy

\[
\mathscr E_{\mathrm{dim}}(u,z)
=u^L\mathscr E_{\mathrm{codim}}(u^{-1},z).
\]

It must not be called a code-dimension enumerator without this substitution and ambient-dimension shift. The revised paper uses `\widetilde T_w` for `\dim_q(C)`.

For a cyclic binary word `(epsilon_0,...,epsilon_{a-1})`, the product

\[
\prod_{i=0}^{a-1}
\widetilde T_w(u,z)_{\varepsilon_i,\varepsilon_{i+1}}
\]

is exactly

\[
 u^{w\sum_i(1-\varepsilon_i)}
 z^{w\sum_i\varepsilon_i(1-\varepsilon_{i+1})}.
\tag{7.3}
\]

The first exponent is the component code-dimension contribution; the second is the hull contribution.

### 7.2 Why the trace is required

The matrix product `(\widetilde T_w^a)_{r,r}` sums all length-`a` walks that start at state `r` and return to the same state. Summing over `r=0,1` closes the binary word around the orbit:

\[
\operatorname{tr}(\widetilde T_w(u,z)^a)
=\sum_{\varepsilon_0,\ldots,\varepsilon_{a-1}\in\{0,1\}}
 u^{w\sum_i(1-\varepsilon_i)}
 z^{w b_O(\varepsilon)}.
\tag{7.4}
\]

Without the trace, the edge from `epsilon_{a-1}` back to `epsilon_0` would be omitted, so open binary strings would be counted instead of cyclic selections.

### 7.3 Joint enumerator theorem

Define

\[
\mathscr E(u,z)
=\sum_{C\in\mathscr C(A,n,\lambda)}
 u^{\dim_{\mathbb F_q}C}
 z^{\dim_{\mathbb F_q}\operatorname{Hull}_k(C)}.
\tag{7.5}
\]

Under the square-free and compatible-twist hypotheses, the factor-selection choices on distinct `tau_{s,k}`-orbits and distinct simple components are independent. By (3.11), (6.3), and (7.4), the exponents add. Hence:

\[
\boxed{
\mathscr E(u,z)
=\prod_{s=1}^{N}
 \prod_{O\in\mathcal O_s}
 \operatorname{tr}\bigl(\widetilde T_{w_O}(u,z)^{a_O}\bigr).
}
\tag{7.6}
\]

This is a transfer-matrix product formula, not a claim of a Pólya cycle-index theorem.

Sanity specializations:

\[
\mathscr E(1,1)=2^{\sum_s|\mathcal F_s|},
\tag{7.7}
\]

and

\[
\mathscr E(u,1)
=\prod_s\prod_{f\in\mathcal F_s}
(1+u^{m_s\deg f}),
\tag{7.8}
\]

because setting `z=1` removes the transition statistic and leaves an independent selected/unselected factor choice.

---

## 8. Exact orbit polynomial and hull distribution

### 8.1 Derivation of the coefficient formula

Set `u=1`. For a cyclic binary word of length `a`, let `b` be the number of `1 -> 0` transitions.

- If `b=0`, the word has no change around the cycle. It is either all zero or all one, giving exactly `2` words.
- If `b>=1`, the word has exactly `b` positive runs of ones and `b` positive runs of zeros. The `2b` positive run lengths form a composition of `a` into `2b` positive parts, giving

\[
\binom{a-1}{2b-1}
\]

compositions. Choosing an indexed starting position and then forgetting which one of the `b` one-runs was declared the first gives the factor `a/b`.

Therefore the number of indexed cyclic binary words with exactly `b` boundaries is

\[
N(a,b)=\frac{a}{b}\binom{a-1}{2b-1},
\qquad 1\le b\le\left\lfloor\frac a2\right\rfloor.
\tag{8.1}
\]

Consequently:

\[
\boxed{
P_{a,w}(z)
=2+\sum_{b=1}^{\lfloor a/2\rfloor}
\frac{a}{b}\binom{a-1}{2b-1}z^{bw}.
}
\tag{8.2}
\]

At `z=1`, this has value `2^a`, as it must.

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
\tag{8.3}
\]

Then

\[
\boxed{
H_{A,n,\lambda,k}(z)
=\prod_{s=1}^{N}\prod_{O\in\mathcal O_s}P_{a_O,w_O}(z).
}
\tag{8.4}
\]

The exact number of codes with hull dimension `h` is

\[
\boxed{
N_h=[z^h]H_{A,n,\lambda,k}(z).
}
\tag{8.5}
\]

This coefficient theorem, rather than a list of possible dimensions only, is the central enumerative result.

---

## 9. LCD count, mean, and variance

### 9.1 LCD count as a corollary

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

### 9.2 Indicator-variable calculation

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

### 9.3 Global moments

Under the square-free and compatible-twist hypotheses, different factor orbits use independent selection bits. Therefore:

\[
\boxed{
\mathbb E\bigl[\dim_q\operatorname{Hull}_k(C)\bigr]
=\sum_{s,O:\,a_O\ge2}\frac{a_Ow_O}{4}.
}
\tag{9.6}
\]

and

\[
\boxed{
\operatorname{Var}\bigl(\dim_q\operatorname{Hull}_k(C)\bigr)
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

The inverse-Frobenius exponent is

\[
\rho=2^{2-1}=2.
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

formula (4.1) with `rho=2` gives

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

Here `m_s=1` and

\[
\rho=p^{e m_s-k}=2^{3-1}=4.
\]

Since `F_8^*` has order `7`, `x^7-1` splits into seven distinct linear factors. If `alpha` is a primitive seventh root and

\[
f_j(x)=x-\alpha^j,
\qquad 0\le j\le6,
\]

then

\[
\tau(f_j)=f_{-4j}=f_{3j}\quad\text{(indices modulo 7)}.
\]

The factor permutation is

\[
[0,3,6,2,5,1,4],
\]

with orbits

\[
\{0\},
\qquad
\{1,3,2,6,4,5\}.
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

Now

\[
\rho=p^{e m_s-k}=2^{2\cdot2-1}=8.
\]

Since `5` divides `15=|F_16^*|`, `x^5-1` splits into five linear factors over `F_16`. If `alpha` is an element of order `5`, then

\[
\tau(f_j)=f_{-8j}=f_{2j}\quad\text{(indices modulo 5)}.
\]

The factor permutation is

\[
[0,2,4,1,3],
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

The direct computation over `F_16`, with dimensions converted to `F_4`-dimensions by multiplying by `m_s=2`, agrees exactly with the orbit formula and transfer matrix:

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
  orbit lengths: [1, 6]
  orbit-boundary == transfer: True
  direct == theory: True
  hull histogram: {0: 4, 1: 60, 2: 60, 3: 4}
  PASS
Example B (m_s=2, orbit length 4):
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

where `omega^2+omega+1=0`. Here

\[
\rho=p^{e-k}=2,
\qquad
\lambda^{1+\rho}=\omega^3=1.
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

This is a genuinely nontrivial compatible constacyclic test; it is not the `lambda=1` cyclic pilot.

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
\qquad \rho=p^{e-k}=4.
\]

Then

\[
\lambda^{1+\rho}=\omega^5=\omega^2\ne1,
\]

and

\[
\lambda'=
\lambda^{-\rho}=\omega^2\ne\omega.
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
lambda^(1+rho)=3 != 1
lambda^(-rho)=3 != lambda
direct dual equals <h^(#)>: True
direct dual is lambda^(-rho)-constacyclic: True
direct dual is lambda-constacyclic: False
No transfer-matrix enumeration was attempted.
```

**Limitation statement:**

> The present transfer-matrix theorem assumes the compatible-twist condition. The incompatible-twist case requires a separate two-polynomial or bipartite formulation and is outside the present theorem.

---

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
- Record the extension-field inverse-Frobenius issue explicitly.
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

If this is incomplete, move it to future work and do not use “cycle-index” in the title.

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
 u^{\dim_q C}z^{\dim_q\operatorname{Hull}_k(C)}.
\]

Then, if all four points above have been proved,

\[
N_h^{\mathrm{equiv}}
=\frac1{|\Gamma|}
\sum_{\gamma\in\Gamma}[z^h]\mathscr E_\gamma(1,z).
\tag{14.2}
\]

This is a Burnside formula. The main transfer-matrix result should not be called a Pólya cycle-index method merely because `tau` has cycles.

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

A formula such as

\[
[[L,K-h,d;L-K-h]]_q
\]

must not be presented as universal. It may be written only as a conditional consequence of a cited construction theorem whose hypotheses have been checked for the particular `D`.

The joint enumerator can help filter classical candidates by `(K,h)`, but it does not determine `d`. Minimum distance must be calculated or bounded independently.

No “new best quantum code” claim should be made without comparison with the current table/database and a recorded access date.

---

## 16. Recommended paper structure

### 1. Introduction

- motivation for exact hull distributions;
- what the supplied paper proves;
- exact gap;
- contributions and hypotheses;
- no overclaim about Burnside or quantum codes.

### 2. Square-free affine algebras and component codes

- product decomposition;
- component fields and dimensions;
- constacyclic ideals;
- split versus extension-field convention.

### 3. The `k`-Galois factor permutation

- inner product;
- inverse Frobenius;
- normalized reciprocal;
- proof that `tau(F)=F`;
- arbitrary orbit lengths.

### 4. Component hull characterization

- generator/check polynomials;
- dual factor support;
- lcm intersection;
- exact support `(F\J) cap tau(J)`.

### 5. Orbit boundary formula

- binary selection words;
- orientation convention;
- weighted global dimension formula.

### 6. Joint enumerator and exact distribution

- transfer matrix;
- trace and cyclic closure;
- product theorem;
- explicit `P_{a,w}` formula;
- coefficient distribution.

### 7. Corollaries and moments

- LCD count;
- mean;
- variance;
- fixed-point and 2-cycle special cases.

### 8. Computational validation

- algorithms;
- pilot example;
- exhaustive tables;
- reproducibility files.

### 9. Optional Burnside section

Only if the group action is fully proved.

### 10. Optional quantum application

Only with a named construction theorem and verified hypotheses.

### 11. Conclusion and limitations

State clearly that the main theorem assumes square-free/simple-root data and compatible twists. Repeated-root polynomials, incompatible twists, and full isometry classification remain separate problems unless proved.

---

## 17. Proof-dependency order

The theoretical dependency must be presented in this order:

```text
Componentwise k-Galois inner product
        |
        v
Inverse Frobenius and normalized reciprocal
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

---

## 18. Risk register and mathematically safe fallbacks

### Risk 1: General extension-field convention conflicts with source notation

Use the rigorous component version (3.2)–(3.5). State explicitly that the supplied paper’s `p^{e-k}` formula is recovered when all components are `F_q`.

### Risk 2: `tau` has long cycles and the intended application only has pairs

Keep arbitrary cycles in the theorem. Treat fixed points and 2-cycles as special corollaries.

### Risk 3: Incompatible twist

If `lambda_s^{1+rho_s} != 1`, the dual is a `lambda_s^{-rho_s}`-constacyclic code. Do not force it into the same factor set. Either develop a two-polynomial/bipartite version or state it as future work.

### Risk 4: Full Burnside group is difficult

Remove it from the main paper and keep the labeled-code enumerator. Do not use “cycle-index” in the title.

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

- [ ] The title does not overclaim a cycle-index method.
- [ ] `K_s` and `m_s` are defined before use.
- [ ] The inverse Frobenius exponent is `p^{e m_s-k}` in the general component setting.
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
| 2 | Component-field and inverse-Frobenius setup | Section 2–3 draft |
| 3 | Precise factor permutation | Lemmas for `tau(F)=F` and orbit lengths |
| 4 | Dual/hull support proof | Section 4–5 draft |
| 5 | Boundary statistic and transfer matrix | Main enumerator theorem |
| 6 | Explicit coefficients and moments | Distribution/corollaries |
| 7 | Exhaustive computational validation | scripts and exact tables |
| 8 | Optional Burnside or quantum section | only if fully justified |
| 9 | Full proof audit and originality review | submission-ready blueprint/manuscript |

If an optional section is incomplete at Week 8, omit it rather than weakening the main theorem.

---

## 21. Immediate next actions

1. Keep `code/validate_pilot.py`, `code/validate_long_orbit_examples.py`, `code/validate_nontrivial_constacyclic.py`, and `code/diagnose_incompatible_twist.py` under version control and attach all outputs to the research notes.
2. Implement the general `K_s` version with `rho_s=p^{e m_s-k}` before testing any extension-field example.
3. Retain Example A as the genuine long-orbit test; do not infer long-cycle behavior from the `F_4`, Hermitian, 2-cycle pilot.
4. Prove Lemma 5.1 and Theorem 5.3 in full before writing the transfer-matrix section.
5. Derive the `a=1,...,5` orbit polynomials in the paper or an appendix.
6. Keep Burnside and quantum applications explicitly optional until their hypotheses are checked.
7. Repeat the literature audit at submission time.

### Final success criterion

The paper is mathematically ready only when:

- the direct factor action, component hull support, boundary formula, transfer matrix, explicit orbit polynomial, joint enumerator, moments, and LCD count all agree;
- the pilot and additional small cases pass exact brute-force checks;
- every optional claim is either proved with hypotheses or clearly marked as future work.

Current status must be reported conservatively: the general formulas are mathematical proof targets/results to be written rigorously; the scripts provide exhaustive computational validation for the listed finite instances; the final literature audit remains submission-dependent; Burnside/equivalence enumeration and quantum constructions remain optional unless their hypotheses are fully established.
