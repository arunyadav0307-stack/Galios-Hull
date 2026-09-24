# Phase 2 Proof Audit

**Audit date:** 24 September 2026 (Asia/Calcutta local date; validator captures use UTC)

**Branch:** `arena/01a0c9d2-galios-hull`

**Scope:** rigorous first-principles audit of the general mathematical theory in `new-paper-blueprint.md`, Sections 3–9, with the frozen convention retained exactly. This report is a proof audit, not a claim that a finite validator proves a general theorem.

## 1. Scope, status vocabulary, and conclusion boundary

Phase 2 audits the affine decomposition, component constacyclic classification, code-first second-slot inner product, inverse-Frobenius reciprocal, root action, factor permutation, dual generator, compatibility, hull support, boundary statistic, orbit polynomial, transfer matrix, trace identity, global enumerator, total count, distribution, LCD count, mean, and variance.

The theorem numbering in Section 3 is the Phase-2 numbering for the 19 requested mathematical claims. It is made explicit in Section 3 of this report and in the Phase-2 ledger added to the blueprint. The status vocabulary for Theorems 1–19 is restricted to the seven requested values. Every one of the 19 results is marked `PROVED WITH CONDITIONS`, not unconditionally `PROVED`: the hypotheses are part of the theorem, and the compatible same-factor-set enumerator does not cover repeated roots, incompatible twists, equivalence classes, Burnside counts, or quantum distance claims.

The proofs below do not rely on the validator outputs or on an uninspected source PDF. The six existing validators and the new small counterexample search are recorded only as finite computational evidence in Section 15.

## 2. Frozen conventions and complete hypotheses

Let

\[
q=p^e,
\qquad e\ge 1,
\qquad 0\le k<e,
\]

where `p` is prime. For each component let

\[
K_s=\mathbb F_{q^{m_s}}=\mathbb F_{p^{e m_s}},
\qquad m_s\ge1.
\]

The component inner product is exactly

\[
\langle x,y\rangle_{s,k}
 =\sum_{i=0}^{n-1}x_i y_i^{p^k}
 =\sum_i x_i\sigma_{s,k}(y_i),
\qquad \sigma_{s,k}(a)=a^{p^k}.
\]

The code is in the first slot of the dual:

\[
C_s^{\perp_k}
 =\{x\in K_s^n:\langle c,x\rangle_{s,k}=0
   \text{ for every }c\in C_s\}.
\]

The inverse of `sigma` on `K_s` is

\[
\rho_{s,k}(a)=a^{p^{e m_s-k}}=\sigma_{s,k}^{-1}(a).
\]

The `k` and `e m_s-k` quantities are Frobenius iteration numbers. The actual field powers are `p^k` and `p^{e m_s-k}`. This distinction is part of the theorem statements, not merely an implementation convention.

The affine algebra is

\[
A=\mathbb F_q[X_1,\ldots,X_\ell]/
  \langle t_1(X_1),\ldots,t_\ell(X_\ell)\rangle,
\]

where `\ell\ge1` and every `t_i` is monic, square-free, and of positive degree. The positive-degree condition is explicit because a unit constant relation would give the zero quotient rather than the asserted nonzero product of fields. The resulting finite reduced algebra is written

\[
A\cong\prod_{s=1}^N K_s,
\qquad N\ge1.
\]

Let `n\ge1`, `\gcd(n,p)=1`, and let `lambda=(lambda_s)_s\in A^\times`. Thus every `lambda_s\in K_s^\times`. The principal enumerator assumes the componentwise compatibility condition

\[
\lambda_s^{1+p^{e m_s-k}}=1
\quad\text{for every }s.
\]

Set

\[
M_s(x)=x^n-\lambda_s.
\]

The codes counted are the distinct labeled factor-selection ideals, with no quotient by a monomial, ring, or isometry group. Component dimensions are over `K_s`; global dimensions and hull dimensions are over `F_q`. If `f` has `K_s`-degree `d`, its global weight is `m_s d`.

## 3. Theorem-by-theorem status ledger for Theorems 1–19

The numbering below is the canonical Phase-2 mapping of the 19 requested claims. The status column uses only the allowed status vocabulary.

| No. | Theorem claim audited | Status |
|---:|---|---|
| 1 | Affine decomposition into finite-field components | **PROVED WITH CONDITIONS** |
| 2 | Component constacyclic decomposition and factor-selection classification | **PROVED WITH CONDITIONS** |
| 3 | Second-slot `k`-Galois inner product and code-first dual translation | **PROVED WITH CONDITIONS** |
| 4 | Inverse-Frobenius normalized reciprocal | **PROVED WITH CONDITIONS** |
| 5 | Root action under the reciprocal | **PROVED WITH CONDITIONS** |
| 6 | Factor permutation on the compatible factor set | **PROVED WITH CONDITIONS** |
| 7 | Dual generator | **PROVED WITH CONDITIONS** |
| 8 | Compatibility and the same-twist criterion | **PROVED WITH CONDITIONS** |
| 9 | Hull support | **PROVED WITH CONDITIONS** |
| 10 | Cyclic `1\to0` boundary statistic | **PROVED WITH CONDITIONS** |
| 11 | Orbit polynomial | **PROVED WITH CONDITIONS** |
| 12 | Transfer matrix | **PROVED WITH CONDITIONS** |
| 13 | Closed-walk trace identity | **PROVED WITH CONDITIONS** |
| 14 | Global joint enumerator | **PROVED WITH CONDITIONS** |
| 15 | Total labeled-code count | **PROVED WITH CONDITIONS** |
| 16 | Exact hull-dimension distribution | **PROVED WITH CONDITIONS** |
| 17 | LCD count | **PROVED WITH CONDITIONS** |
| 18 | Mean hull dimension | **PROVED WITH CONDITIONS** |
| 19 | Variance of hull dimension | **PROVED WITH CONDITIONS** |

These statuses mean that the displayed identities follow from the hypotheses in Section 2 and the derivations in Sections 4–12. They do not upgrade the separate literature-comparison records, N1, the incompatible-twist diagnostics, the optional Burnside section, or the quantum application to theorem status.

## 4. Affine decomposition and component constacyclic decomposition

### 4.1 Proof of the affine product of fields

Factor each relation over `F_q` as

\[
t_i(X_i)=\prod_{j=1}^{r_i}t_{ij}(X_i),
\]

with the `t_{ij}` distinct monic irreducibles. The univariate Chinese remainder theorem gives

\[
\mathbb F_q[X_i]/(t_i)
 \cong \prod_{j=1}^{r_i}\mathbb F_q[X_i]/(t_{ij}),
\]

and each factor on the right is a finite field. Equivalently, each univariate quotient is a finite étale `F_q`-algebra: square-free is equivalent to separability over the perfect field `F_q`.

The displayed affine algebra is the tensor product over `F_q` of these univariate quotients. Distributing tensor products over finite products reduces it to finite tensor products of finite separable field extensions. A tensor product of finite separable extensions of a perfect field is finite étale, hence reduced and a finite product of finite fields. Therefore

\[
A\cong\prod_{s=1}^N K_s,
\qquad K_s\cong\mathbb F_{q^{m_s}}.
\]

The product has primitive orthogonal idempotents `eta_s` satisfying

\[
\eta_s^2=\eta_s,
\qquad \eta_s\eta_t=0\ (s\ne t),
\qquad \sum_s\eta_s=1.
\]

They identify the component projections. This proof uses separability of the univariate relations; it does not silently extend to repeated-root affine algebras.

### 4.2 Polynomial CRT and shifts

Applying polynomial extension and quotienting componentwise gives

\[
A[x]/(x^n-\lambda)
 \cong \prod_{s=1}^N K_s[x]/(x^n-\lambda_s).
\]

The isomorphism sends a residue class to its component residue classes. With the declared componentwise Frobenius convention, the global inner product is the tuple of component inner products, so an inner product is zero in `A` exactly when every component inner product is zero. The constacyclic shift

\[
T_\lambda(c_0,\ldots,c_{n-1})
 =(\lambda c_{n-1},c_0,\ldots,c_{n-2})
\]

acts componentwise as `T_{lambda_s}`. Consequently an `A`-linear `lambda`-constacyclic code is exactly a tuple of ideals `C_s` in the component quotients. The idempotents give the inverse correspondence

\[
C=\bigoplus_s\eta_s C_s
 \cong \prod_s C_s.
\]

### 4.3 Factor-selection classification

Because `\gcd(n,p)=1` and every `lambda_s` is nonzero,

\[
M_s'(x)=n x^{n-1}
\]

has no common root with `M_s`; hence `M_s` is square-free. Write

\[
M_s=\prod_{f\in\mathcal F_s}f
\]

as a product of distinct monic irreducibles. The principal ideals of `K_s[x]/(M_s)` correspond to monic divisors of `M_s`. For a subset `J_s\subseteq\mathcal F_s`, put

\[
g_{J_s}=\prod_{f\in J_s}f,
\qquad C_s(J_s)=\langle g_{J_s}\rangle.
\]

Every ideal has exactly one such monic divisor, so the subset is unique. The residue classes

\[
g_{J_s},xg_{J_s},\ldots,x^{n-\deg g_{J_s}-1}g_{J_s}
\]

form a `K_s`-basis of the ideal, and therefore

\[
\dim_{K_s}C_s(J_s)=n-\deg g_{J_s}
 =n-\sum_{f\in J_s}\deg f.
\]

The product code is uniquely determined by the tuple of subsets, so the number of distinct labeled codes is

\[
2^{\sum_s|\mathcal F_s|}.
\]

This is labeled-factor counting, not equivalence-class counting.

## 5. Inner product and code-first dual translation

For fixed `s`, `sigma` is a field automorphism. The form is additive in both arguments and satisfies

\[
\langle c,ay\rangle_{s,k}
 =\sigma(a)\langle c,y\rangle_{s,k},
\qquad
\langle ac,y\rangle_{s,k}=a\langle c,y\rangle_{s,k}.
\]

It is not being treated as an ordinary `K_s`-bilinear form when `k\ne0`; it is semilinear in the second slot. It is nondegenerate: if `y_j\ne0`, choose `c` supported in coordinate `j` with `c_j=\sigma(y_j)^{-1}` to obtain inner product `1`. The code-first annihilator is nevertheless a `K_s`-linear subspace, because multiplying a candidate `x` by `a` multiplies every defining equation by the nonzero scalar `sigma(a)`.

The inverse exponent is correct because

\[
\rho_{s,k}(\sigma_{s,k}(a))
 =a^{p^{k+e m_s-k}}
 =a^{p^{e m_s}}=a.
\]

For every defining equation, applying `rho` gives

\[
0=\rho\left(\sum_i c_i\sigma(x_i)\right)
 =\sum_i\rho(c_i)x_i.
\]

Thus, if `R(C)` denotes the coordinatewise `rho`-image of `C`, then

\[
C^{\perp_k}=R(C)^{\perp_E},
\]

where the right side is the ordinary Euclidean annihilator. This is an equality of sets obtained from the defining equations; it is not a reciprocal-based definition of the dual.

If `C` is `lambda`-constacyclic, `R(C)` is `rho(lambda)`-constacyclic, since `rho` commutes with the shift except for changing the scalar `lambda` to `rho(lambda)`. This twist tracking is used in Section 7.

## 6. Inverse-Frobenius reciprocal, root action, factor permutation, and compatibility

### 6.1 Reciprocal

For a monic polynomial

\[
f(x)=\sum_{i=0}^d f_i x^i,
\qquad f_0\ne0,
\]

define

\[
f^{\#_{s,k}}(x)
 =\rho(f_0)^{-1}\sum_{i=0}^d\rho(f_i)x^{d-i}
 =f_0^{-p^{e m_s-k}}
   \sum_{i=0}^d f_i^{p^{e m_s-k}}x^{d-i}.
\]

The leading coefficient is `rho(f_0)^{-1}rho(f_0)=1`, so the result is monic. If `f` and `g` have nonzero constant terms, reversal satisfies `rev(fg)=rev(f)rev(g)` and coefficientwise `rho` is multiplicative. Normalizing the constant term therefore gives

\[
(fg)^{\#}=f^{\#}g^{\#}.
\]

A field automorphism preserves irreducibility. Ordinary reversal preserves irreducibility for a polynomial with nonzero constant term: a factorization of its reversal would reverse to a factorization of the original polynomial. Thus `#` preserves degree and irreducibility. Its inverse is the corresponding normalized reciprocal using `sigma`, so `#` is bijective on monic nonzero-constant polynomials.

### 6.2 Root action

If `f(alpha)=0`, then

\[
\begin{aligned}
f^{\#}(\alpha^{-p^{e m_s-k}})
 &=\rho(f_0)^{-1}
   \sum_i\rho(f_i)\alpha^{-(d-i)p^{e m_s-k}}\\
 &=\rho(f_0)^{-1}\rho\left(
   \sum_i f_i\alpha^{-(d-i)}\right)\\
 &=\rho(f_0)^{-1}\rho\left(\alpha^{-d}f(\alpha)\right)=0.
\end{aligned}
\]

The root map is therefore

\[
\boxed{\alpha\longmapsto\alpha^{-p^{e m_s-k}}}.
\]

This is derived from the normalized reciprocal and is not postulated from a finite example.

### 6.3 Compatibility and factor permutation

If `alpha^n=lambda_s`, then its image has

\[
(\alpha^{-p^{e m_s-k}})^n
 =\lambda_s^{-p^{e m_s-k}}.
\]

The image is a root of the same modulus `x^n-lambda_s` exactly when

\[
\lambda_s^{-p^{e m_s-k}}=\lambda_s,
\]

which is equivalent to

\[
\lambda_s^{1+p^{e m_s-k}}=1.
\]

Under this compatibility condition, the roots of every irreducible factor of `M_s` map to roots of `M_s`. Irreducibility preservation shows that `f#` is another member of `mathcal F_s`, and bijectivity gives

\[
\tau_{s,k}(f)=f^{\#_{s,k}},
\qquad
\tau_{s,k}(\mathcal F_s)=\mathcal F_s.
\]

The map is a permutation and need not be an involution. Fixed points, 2-cycles, and longer cycles are all allowed. If compatibility fails, the same root calculation gives the different modulus

\[
x^n-\lambda_s^{-p^{e m_s-k}}.
\]

The same-factor-set orbit theorem is not applied in that case.

## 7. Dual generator and the ordinary constacyclic lemma

Let

\[
M=x^n-a,
\qquad G\mid M,
\qquad H=M/G,
\]

with `G` monic of degree `r` and `H` of degree `n-r`. Let `h_0=H(0)\ne0` and define the normalized ordinary reciprocal

\[
H^*(x)=h_0^{-1}\sum_{i=0}^{n-r}H_i x^{n-r-i}.
\]

The ordinary Euclidean dual of the `a`-constacyclic ideal `<G>` is `<H^*>` in the `a^{-1}`-constacyclic quotient. Here is the coefficient proof needed for the audit.

For `0\le j<n-r` and `0\le t<r`, the coefficient vector of `x^jG` and the coefficient vector of `x^tH^*` have Euclidean inner product

\[
\frac1{h_0}[x^{n-r-j+t}](GH).
\]

Indeed, writing coefficients out changes the dot product into the coefficient convolution of `G` and `H` at the displayed exponent. The exponent lies between `1` and `n-1`, while

\[
GH=x^n-a
\]

has no coefficient in those degrees. All these shifts are therefore orthogonal. The shifts `x^jG` for `0\le j<n-r` form a basis of `<G>` and the shifts `x^tH^*` for `0\le t<r` form a basis of `<H^*>`. Their dimensions are `n-r` and `r`, respectively, so orthogonality and dimension equality prove the ordinary dual identity. The endpoint cases `G=1` and `G=M` are included with empty shift ranges.

Now return to the Galois dual. Let

\[
G=g_{J_s},
\qquad H=h_{J_s},
\qquad a=\rho(\lambda_s).
\]

The code `R(C_s)` is generated by `rho(G)` in the `a`-constacyclic quotient, and its check polynomial is `rho(H)`. The ordinary lemma gives the generator

\[
(\rho(H))^*=\rho(H(0))^{-1}\sum_i\rho(H_i)x^{\deg H-i}
 =H^{\#_{s,k}}.
\]

By Section 5, the ordinary dual of `R(C_s)` is exactly `C_s^{\perp_k}`. Therefore

\[
\boxed{C_s(J_s)^{\perp_k}=\langle h_{J_s}^{\#_{s,k}}\rangle.}
\]

The dual twist is

\[
\bigl(\rho(\lambda_s)\bigr)^{-1}
 =\lambda_s^{-p^{e m_s-k}}.
\]

Under compatibility, `rho(lambda_s)=lambda_s^{-1}`, so the dual has the original twist `lambda_s` and its generator support is `tau(mathcal F_s\setminus J_s)`. Without compatibility, the generator belongs to the different dual-twist modulus and cannot be inserted into the compatible factor orbit set.

## 8. Independent hull-support orientation derivation

This is an independent derivation of the orientation, starting from the two generator supports and not from a preselected boundary formula.

The generator support is

\[
\operatorname{Supp}(g_{J_s})=J_s.
\]

The check polynomial has support `mathcal F_s\setminus J_s`; the dual generator therefore has support

\[
\operatorname{Supp}(h_{J_s}^{\#})
 =\tau_{s,k}(\mathcal F_s\setminus J_s).
\]

In the square-free quotient, the intersection of two principal divisor ideals is generated by the least common multiple. Hence its support is

\[
J_s\cup\tau_{s,k}(\mathcal F_s\setminus J_s).
\]

The hull dimension is the degree of the factors omitted from this union. Since `tau` is a bijection,

\[
\begin{aligned}
\mathcal F_s\setminus
 \left[J_s\cup\tau(\mathcal F_s\setminus J_s)\right]
 &= (\mathcal F_s\setminus J_s)
    \cap\left(\mathcal F_s\setminus\tau(\mathcal F_s\setminus J_s)\right)\\
 &= (\mathcal F_s\setminus J_s)\cap\tau(J_s).
\end{aligned}
\]

Therefore the hull support is exactly

\[
\boxed{(\mathcal F_s\setminus J_s)\cap\tau_{s,k}(J_s).}
\]

Now orient an orbit as

\[
O=(f_0,\ldots,f_{a-1}),
\qquad \tau(f_i)=f_{i+1\pmod a}.
\]

The destination factor `f_{i+1}` is in the support above exactly if `f_{i+1}` is unselected and its predecessor `f_i` is selected. Thus

\[
f_{i+1}\text{ contributes}
\iff \varepsilon_i=1,
      \quad\varepsilon_{i+1}=0.
\]

This independently forces the `1\to0` orientation; it is not an inverse-image convention chosen to fit a transfer matrix.

## 9. Boundary statistic and dimension conversion

Define

\[
b_O(\varepsilon)
 =\sum_{i=0}^{a-1}\varepsilon_i(1-\varepsilon_{i+1}),
\qquad \varepsilon_a=\varepsilon_0.
\]

Every factor in an orbit has the same degree because `tau` preserves degree. If that degree is `d_O`, its `F_q`-weight is

\[
w_O=m_s d_O.
\]

The component hull dimension is the sum of the degrees of the support factors, so the orbit contribution to global dimension is `w_O b_O`. The product decomposition of the code and the componentwise inner product give

\[
\dim_{\mathbb F_q}\operatorname{Hull}_k(C)
 =\sum_{s=1}^N\sum_{O\in\mathcal O_s}
   w_O b_O(\varepsilon_O).
\]

The cyclic closure is essential: the term at `i=a-1` tests the edge from `f_{a-1}` to `f_0`. A `0\to1` convention has the same numerical total on a cyclic binary word, but the displayed support derivation fixes `1\to0` as the canonical orientation.

## 10. Transfer matrix, trace identity, and global enumerator

For an orbit of weight `w`, a selected factor contributes zero to code dimension and an unselected factor contributes `w`. For a transition from state `r=epsilon_i` to destination state `t=epsilon_{i+1}`, assign

\[
T_w(u,z)_{r,t}
 =u^{w(1-t)}z^{wr(1-t)}.
\]

Therefore, with rows and columns ordered `0,1`,

\[
T_w(u,z)=
\begin{pmatrix}
 u^w&1\\
 u^wz^w&1
\end{pmatrix}.
\]

The four entries are respectively `0->0: u^w`, `0->1:1`, `1->0:u^wz^w`, and `1->1:1`. Destination weighting is deliberate: each factor is counted once when its state is the destination of the preceding edge.

For a labeled cyclic binary selection `epsilon_0,...,epsilon_{a-1}`, the product of its edge weights is

\[
\prod_i T_w(u,z)_{\varepsilon_i,\varepsilon_{i+1}}
 =u^{w\sum_i(1-\varepsilon_i)}
  z^{w\sum_i\varepsilon_i(1-\varepsilon_{i+1})}.
\]

Expanding a matrix power as a sum over intermediate states gives

\[
(T_w^a)_{r,r}
 =\sum_{\substack{\varepsilon_0=r,\,\varepsilon_a=r}}
  \prod_{i=0}^{a-1}T_w{}_{\varepsilon_i,\varepsilon_{i+1}}.
\]

Summing over `r=0,1` closes the cycle and counts every indexed binary selection exactly once. Hence

\[
\operatorname{tr}(T_w^a)
 =\sum_{\varepsilon\in\{0,1\}^a}
  u^{w\sum_i(1-\varepsilon_i)}z^{w b_O(\varepsilon)}.
\]

Selections on distinct factor orbits are independent coordinates in the subset bijection, and component dimensions and hull dimensions add. Multiplying the orbit sums therefore proves the global joint enumerator

\[
\boxed{
\mathscr E(u,z)
 =\prod_{s=1}^N\prod_{O\in\mathcal O_s}
   \operatorname{tr}(T_{w_O}(u,z)^{a_O}).
}
\]

This counts distinct labeled codes. It is not a quotient by an equivalence group.

At `u=z=1`, each orbit has `2^{a_O}` selections, so

\[
\mathscr E(1,1)=2^{\sum_s|\mathcal F_s|}.
\]

The same total follows directly from the factor-selection bijection. At `z=1`, the factor choices give the independent marginal

\[
\mathscr E(u,1)=\prod_s\prod_{f\in\mathcal F_s}
 (1+u^{m_s\deg f}),
\]

which is a second algebraic check of the code-dimension interpretation.

## 11. Orbit polynomial and its integrality

Set `u=1` for one orbit of length `a`. If `b=0`, the cyclic word is constant, giving two words. For `b\ge1`, the `2b` transition edges can be chosen in `\binom a{2b}` ways. Because the number of transitions is even, either starting bit produces a consistent cyclic labeling, and the two labelings have exactly `b` transitions of each orientation. Thus

\[
N(a,b)=2\binom a{2b}.
\]

Equivalently,

\[
N(a,b)=\frac a b\binom{a-1}{2b-1}
       =2\binom a{2b},
\]

because

\[
\binom a{2b}=\frac a{2b}\binom{a-1}{2b-1}.
\]

This proves integrality without relying on a rational-looking run formula. The orbit polynomial is therefore

\[
\boxed{
P_{a,w}(z)=2+
 \sum_{b=1}^{\lfloor a/2\rfloor}
 2\binom a{2b}z^{bw}.
}
\]

At `z=1`, the binomial identity gives `P_{a,w}(1)=2^a`. The first values are

\[
P_{1,w}=2,\quad
P_{2,w}=2+2z^w,\quad
P_{3,w}=2+6z^w,
\]

\[
P_{4,w}=2+12z^w+2z^{2w},\quad
P_{5,w}=2+20z^w+10z^{2w}.
\]

## 12. Distribution, LCD count, mean, and variance

The exact distribution is the specialization

\[
H_{A,n,\lambda,k}(z)=\mathscr E(1,z)
 =\prod_{s,O}P_{a_O,w_O}(z),
\]

and the number of codes of hull dimension `h` is

\[
N_h=[z^h]H_{A,n,\lambda,k}(z).
\]

For the uniform distribution on labeled factor selections, all individual factor indicators are independent Bernoulli variables with parameter `1/2`. Distinct orbit contributions are consequently independent, though not necessarily identically distributed.

All weights are positive. Thus hull dimension zero is equivalent to `b_O=0` for every orbit. A cyclic binary word has no `1\to0` edge exactly when it is constant, so each orbit has two LCD selections. Therefore

\[
\#\{C:\operatorname{Hull}_k(C)=0\}
 =2^{\sum_s|\mathcal O_s|}.
\]

For one orbit let

\[
X_i=\varepsilon_i(1-\varepsilon_{i+1}),
\qquad B=\sum_iX_i.
\]

For `a=1`, `B=0` identically. For `a\ge2`, `E[X_i]=1/4`, hence `E[B]=a/4`. For `a=2`, the two indicators are mutually exclusive, so `B` is Bernoulli with parameter `1/2` and `Var(B)=1/4`. For `a\ge3`, each `Var(X_i)=3/16`; neighboring directed edges have covariance `-1/16`; non-neighboring edges have covariance zero. There are `a` neighboring unordered pairs, so

\[
\operatorname{Var}(B)
 =a\frac3{16}+2a\left(-\frac1{16}\right)
 =\frac a{16}.
\]

Multiplying by the orbit weights and summing independent orbit contributions gives

\[
\boxed{
\mathbb E[\dim_{\mathbb F_q}\operatorname{Hull}_k(C)]
 =\sum_{s,O:\,a_O\ge2}\frac{a_Ow_O}{4},
}
\]

and

\[
\boxed{
\operatorname{Var}(\dim_{\mathbb F_q}\operatorname{Hull}_k(C))
 =\sum_{s,O:\,a_O=2}\frac{w_O^2}{4}
  +\sum_{s,O:\,a_O\ge3}\frac{a_Ow_O^2}{16}.
}
\]

The `a=2` exception is necessary; replacing it by `a/16` would be false.

## 13. Exact N1 identification and resolution

The repository's N1 label refers only to the unresolved row in blueprint Section 10.6 and its corresponding validation table row:

\[
q=16,
\qquad n=15,
\qquad 2^{15}=32{,}768\text{ proposed factor selections}.
\]

A repository-wide search found no `N1` implementation, no N1 output, and no additional verified N1 specification. In particular, the current record does **not** state the required `k`, `lambda`, component field interpretation, factorization, orbit permutation, or expected histogram. The number `2^{15}` alone is not enough to infer those missing choices, and no interpretation is invented here.

Resolution: N1 is not an executable test in the current package. It is an underspecified validation-specification obligation, retained as `VERIFY BEFORE MANUSCRIPT FINALIZATION`. A future N1 implementation may be accepted only after recording, at minimum, `p,e,k`, the precise component(s), `lambda`, `M_s` factorization, factor labels, orbit data, direct-dual convention, expected total, and complete output. No N1 histogram, PASS, or theorem conclusion is claimed in Phase 2.

## 14. Active counterexample search

The new reproducible search `validation/phase2_counterexample_search.py` checks the combinatorial identities independently of the existing field validators. It exhausts every binary word for lengths `1` through `12` and checks:

1. the orbit-polynomial coefficient identity `N(a,b)=2 binom(a,2b)`;
2. the transfer trace against direct word enumeration for lengths `1` through `8` and weights `1,2,3`;
3. the independently derived hull-support/boundary orientation for every binary word of lengths `1` through `12`.

Its captured output is in `validation/phase2_counterexample_search.out`. It reports no combinatorial counterexample in that range. This is computational evidence only.

The existing finite family also exercises the requested field and extension regimes: `F_4` with nonzero `k`, the exact `F_4`, `k=0` diagnostic, `F_8` with an orbit of length `6`, `F_{16}=F_{4^2}` with `m_s=2` and an orbit of length `4`, the compatible nontrivial twist over `F_4`, N2-A with all 32 selections, and N2-B with all 8 selections and incompatible twists. The factor actions include fixed points, 2-cycles, 4-cycles, and a 6-cycle. These runs found no finite counterexample within their stated scopes; they do not prove the general theory.

## 15. Validation regression, Phase-1 comparison, and evidence files

Phase 1 evidence is retained unchanged in the original six `validation/*.out` files and in the pre-existing sections of `validation/VALIDATION_REPORT.md`. After the Phase-2 edits, all six existing validators were rerun in the same clean environment. The Phase-2 captures are:

- `validation/phase2_validate_pilot.out` — exit `0`, PASS;
- `validation/phase2_validate_long_orbit_examples.out` — exit `0`, PASS;
- `validation/phase2_validate_nontrivial_constacyclic.out` — exit `0`, PASS;
- `validation/phase2_diagnose_incompatible_twist.out` — exit `0`, DIAGNOSTIC ONLY;
- `validation/phase2_validate_n2_extension_convention.out` — exit `0`, PASS;
- `validation/phase2_diagnose_n2_incompatible_twist.out` — exit `0`, PASS — DIAGNOSTIC;
- `validation/phase2_counterexample_search.out` — exit `0`, no counterexample in its finite search range.

The Phase-2 report section added to `validation/VALIDATION_REPORT.md` compares each Phase-2 capture with the corresponding Phase-1 capture. The expected stdout, finite counts, direct/principal agreements, alternative-comparator discrepancies, and diagnostic boundaries are unchanged. No validator output is used as a general proof, and N1 is not silently counted as a passing run.

## 16. Remaining limitations, source status, and Phase-2 verdict

The mathematical claims in Theorems 1–19 are now proved in this report under explicit hypotheses. The following items remain outside that conditional theorem result:

- N1 lacks an executable, fully specified definition and output;
- the supplied source PDF is structurally available but its theorem-level text was not locally extractable, so no literature theorem is upgraded from publisher/abstract or metadata status;
- no manuscript `.tex` or `.bib` source exists in the repository;
- incompatible twists require a two-modulus/bipartite theory and are diagnostic only;
- Burnside/Pólya equivalence-class counting is future work unless a group action and fixed-code calculation are separately proved;
- quantum applications and minimum-distance claims are future/conditional, and no distance is inferred from hull dimension;
- all counts in the proved enumerator are labeled-code counts, not equivalence classes.

**Phase-2 verdict: `PASS WITH CONDITIONS`.** The requested general theory has a complete conditional proof audit, the frozen inverse-Frobenius convention and hull-support orientation are derived independently, N1 is identified without invention and explicitly unresolved, the finite counterexample search and all six validator regressions are captured, and the remaining conditions are recorded rather than hidden. This is not an unconditional `PASS` while N1 specification, source-PDF theorem verification, and manuscript-source evidence remain unavailable.
