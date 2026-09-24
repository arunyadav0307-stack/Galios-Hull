# Phase 5 Convention-Transformation and Invariance Audit

## 1. Objective

Phase 5 re-derives the candidate-first/code-first relationship without relying on the Phase-4 implementation and determines which quantities are equal, which are related by a semilinear isomorphism, and which are not invariant.

The central distinction is:

- the two dual **subspaces** are generally different;
- they are related by a coordinatewise Frobenius automorphism;
- the two hull **dimensions** and LCD decisions are equal for every finite-field-linear code under the two defining pairings;
- actual factor-labelled hull supports need not be equal;
- the present labeled code/hull enumerator is invariant when both conventions are evaluated on the same code family and the same dimension statistic is used.

The main result is therefore not that the conventions are identical. It is a proved transformation plus a proved numerical hull invariant, with explicit conditions for factor-orbit formulas and constacyclic twists.

## 2. Frozen Present Convention

Let

\[
K_s=\mathbb F_{q^{m_s}}=\mathbb F_{p^{d_s}},
\qquad d_s=e m_s,
\]

and let

\[
\sigma=\sigma_{s,k}:a\longmapsto a^{p^k},
\qquad
\rho=\rho_{s,k}:a\longmapsto a^{p^{d_s-k}}=\sigma^{-1}(a).
\]

The frozen code-first pairing is

\[
B_{\mathrm{code}}(c,x)=\langle c,x\rangle^{\mathrm{CF}}_{s,k}
 =\sum_i c_i\sigma(x_i).
\]

Its dual is

\[
D_{\mathrm{code}}(C)
 =\{x\in K_s^n:B_{\mathrm{code}}(c,x)=0\text{ for every }c\in C\}.
\]

The ordinary-Euclidean description is

\[
D_{\mathrm{code}}(C)=\rho(C^{\perp_E}).
\]

The principal normalized reciprocal is

\[
f^{\#_\rho}(x)=f_0^{-\rho}\sum_i\rho(f_i)x^{d-i},
\]

where `f_0^{-rho}` means the inverse of `rho(f_0)`. The principal dual twist is

\[
\lambda^{-p^{d_s-k}}=\rho(\lambda^{-1}),
\]

and the frozen same-factor-set compatibility condition is

\[
\lambda^{1+p^{d_s-k}}=1.
\]

No frozen definition is changed in Phase 5.

## 3. Candidate-First Convention

The accessible source HTML, arXiv:2412.08512v1, Section 2.2, displays

\[
\langle\alpha,\beta\rangle_k
 =\sum_i\alpha_i\beta_i^{p^k}
\]

and defines the dual by placing the candidate in the first slot:

\[
D_{\mathrm{cand}}(C)
 =\{y\in K_s^n:
   \sum_i y_i\sigma(c_i)=0\text{ for every }c\in C\}.
\]

Thus, in the source's dual equation, Frobenius acts on the codeword, not on the candidate. The notation `D_cand` is used throughout this Phase; `D_code` is the frozen code-first dual. These names replace ambiguous phrases such as “candidate dual” and “alternative dual.”

The candidate-first pairing is linear in its first argument and sigma-semilinear in its second argument. Its dual is still a `K_s`-linear subspace because multiplication of a candidate by a scalar multiplies every defining equation by that scalar.

## 4. Exact Dual Transformation

Let `y` satisfy the candidate-first equations:

\[
\sum_i y_i\sigma(c_i)=0
\qquad\text{for every }c\in C.
\]

Set

\[
x=\rho^2(y),
\qquad\text{so that }y=\sigma^2(x).
\]

Apply `rho` to one defining equation. Since `rho` is a field automorphism, it preserves zero and distributes over the sum:

\[
0=\rho\left(\sum_i\sigma^2(x_i)\sigma(c_i)\right)
 =\sum_i\rho(\sigma^2(x_i))\rho(\sigma(c_i)).
\]

The maps commute and `rho sigma` is the identity, so

\[
\rho(\sigma^2(x_i))=\sigma(x_i),
\qquad
\rho(\sigma(c_i))=c_i.
\]

Consequently

\[
0=\sum_i\sigma(x_i)c_i
 =\sum_i c_i\sigma(x_i),
\]

which is exactly the code-first defining equation for `x`. Hence

\[
y\in D_{\mathrm{cand}}(C)
 \Longrightarrow
\rho^2(y)\in D_{\mathrm{code}}(C),
\]

or

\[
D_{\mathrm{cand}}(C)\subseteq\sigma^2(D_{\mathrm{code}}(C)).
\]

For the reverse inclusion, take `x` in `D_code(C)` and set `y=sigma^2(x)`. Reversing the same calculation gives

\[
\sum_i y_i\sigma(c_i)
 =\sigma^2\left(\sum_i c_i\sigma(x_i)\right)=0.
\]

Therefore

\[
\boxed{
D_{\mathrm{cand}}(C)=\sigma^2(D_{\mathrm{code}}(C)).
}
\]

The same identity follows independently from ordinary Euclidean duality:

\[
D_{\mathrm{code}}(C)=\rho(C^{\perp_E}),
\qquad
D_{\mathrm{cand}}(C)=\sigma(C^{\perp_E}),
\]

and `sigma^2 rho=sigma`.

Here `sigma^2` means the field map

\[
a\longmapsto a^{p^{2k}},
\]

with the Frobenius iteration reduced modulo `d_s=e m_s` when represented as a field automorphism. It is not the scalar exponent `2p^k`; it is the composition of two Frobenius automorphisms.

**Theorem status: PROVED.**

## 5. Frobenius-Automorphism Properties

Let `T=sigma^2`, applied coordinatewise to `K_s^n`. Then:

1. `T` is a field automorphism on every component field.
2. `T^{-1}=rho^2`.
3. `T` is bijective and preserves zero coordinates, so it preserves ordinary coordinate support.
4. `T` maps `K_s`-linear codes to `K_s`-linear codes semilinearly:
   `T(a c)=T(a)T(c)`, and `T(K_s)=K_s`.
5. `T` preserves `K_s`-dimension and therefore also the corresponding `\mathbb F_q`-dimension after component weighting.
6. Coefficientwise `T` maps an irreducible factor to an irreducible factor of the transformed modulus and preserves factor degree.
7. It can permute factor labels and need not fix an individual factor or an individual factor selection.

Thus the duals in Section 4 are semilinearly isomorphic, not generally equal. Coordinate support is preserved, but factor-labelled support is acted on by the induced factor permutation.

**Theorem status: PROVED.**

## 6. Constacyclic-Twist Transformation

Use the constacyclic shift

\[
S_\lambda(c_0,\ldots,c_{n-1})
 =(\lambda c_{n-1},c_0,\ldots,c_{n-2}).
\]

Coordinatewise application of `T` gives

\[
T(S_\lambda c)=S_{T(\lambda)}T(c)
 =S_{\sigma^2(\lambda)}T(c).
\]

Therefore

\[
C\text{ is }\lambda\text{-constacyclic}
 \Longrightarrow
T(C)\text{ is }\sigma^2(\lambda)\text{-constacyclic}.
\]

The two dual twists are derived separately:

\[
\begin{aligned}
\text{code-first dual twist}
  &=\rho(\lambda^{-1})
   =\lambda^{-p^{d_s-k}},\\
\text{candidate-first dual twist}
  &=\sigma(\lambda^{-1})
   =\lambda^{-p^k}.
\end{aligned}
\]

They transform consistently because

\[
T\big(\rho(\lambda^{-1})\big)
 =\sigma^2\rho(\lambda^{-1})
 =\sigma(\lambda^{-1}).
\]

The two compatibility conditions are equivalent:

\[
\lambda\rho(\lambda)=1
\Longleftrightarrow
\rho(\lambda)=\lambda^{-1}
\Longleftrightarrow
\sigma(\lambda)=\lambda^{-1}
\Longleftrightarrow
\lambda\sigma(\lambda)=1.
\]

Under this common compatibility condition,

\[
\sigma^2(\lambda)=\lambda,
\]

so the compatible `lambda`-constacyclic family is stable as a family under `T`. Without compatibility, the two twist parameters generally differ and the candidate-first dual is not a code in the same factor modulus as the frozen dual.

**Theorem status: PROVED WITH CONDITIONS.**

## 7. Dual-Code Relationship Theorem

**Theorem A — Relation between the two Galois duals.** Let `K_s` be a finite field, let `sigma` be an automorphism, let `rho=sigma^{-1}`, and let `C` be any `K_s`-linear subspace of `K_s^n`. Define the two duals by the equations in Sections 2 and 3. Then

\[
D_{\mathrm{cand}}(C)=T(D_{\mathrm{code}}(C)),
\qquad T=\sigma^2.
\]

Both duals have dimension

\[
\dim_{K_s}D_{\mathrm{cand}}(C)
 =\dim_{K_s}D_{\mathrm{code}}(C)
 =n-\dim_{K_s}C.
\]

The proof is the two-inclusion derivation in Section 4. The dimension statement also follows because `T` is bijective; nondegeneracy of either semilinear pairing gives the usual codimension.

The theorem does **not** assert `D_cand(C)=D_code(C)`. Equality requires the additional invariance condition `T(D_code(C))=D_code(C)`.

**Theorem status: PROVED.**

## 8. Frobenius-Invariance of the Code Family

For a compatible simple-root modulus `x^n-lambda`, `T` permutes the irreducible factors of the same modulus. If a code is represented by a selected factor set `J`, then coefficientwise `T` maps it to the code represented by the induced selection `T(J)`. Hence

\[
T(C_J)=C_J
\quad\Longleftrightarrow\quad
T(J)=J
\]

up to the usual equality of principal ideals.

Not every selected factor set is a union of `T`-orbits. In the independent search:

- F8, `lambda=1`, `k=1`: 120 of 128 selections were not `T`-invariant;
- F8, `lambda=1`, `k=2`: 120 of 128 selections were not `T`-invariant;
- F16, `lambda=1`, `k=1`: 24 of 32 selections were not `T`-invariant;
- F16, `lambda=1`, `k=3`: 24 of 32 selections were not `T`-invariant.

The first reported non-invariant selection is mask `2` in each of those cases. F4 with `k=1` and F16 with `k=2` have `T=1` on the component field, so every tested code is invariant there.

Thus the compatible constacyclic **family** is Frobenius-stable, but an individual code is Frobenius-invariant only for a restricted union-of-orbits selection.

**Theorem status: PROVED WITH CONDITIONS.**

## 9. Hull Transformation

Write

\[
H_{\mathrm{code}}(C)=C\cap D_{\mathrm{code}}(C),
\qquad
H_{\mathrm{cand}}(C)=C\cap D_{\mathrm{cand}}(C).
\]

For every code, applying the bijection `T` to an intersection gives the exact identity

\[
T(H_{\mathrm{code}}(C))
 =T(C)\cap T(D_{\mathrm{code}}(C))
 =T(C)\cap D_{\mathrm{cand}}(C).
\]

Equivalently,

\[
T^{-1}(H_{\mathrm{cand}}(C))
 =T^{-1}(C)\cap D_{\mathrm{code}}(C).
\]

The tempting formula

\[
H_{\mathrm{cand}}(C)=T(H_{\mathrm{code}}(C))
\]

is valid if `T(C)=C`, but is not valid for a general code. When `T(C)\ne C`, the right-hand side of the exact identity contains `T(C)`, not `C`.

The F8 and F16 searches exhibit selections for which the actual hull subspaces differ. Therefore the hulls are not generally equal as subspaces and are not generally related by `T` while keeping the same code `C` fixed.

**Theorem status: PROVED WITH CONDITIONS.**

## 10. Hull-Dimension Invariance

There is nevertheless a general dimension theorem that does not require `T(C)=C`.

Let `C` have a `K_s`-basis `c_1,\ldots,c_r` and define the restricted code-first Gram matrix

\[
G_{ij}=B_{\mathrm{code}}(c_i,c_j)
 =\sum_\ell (c_i)_\ell\sigma((c_j)_\ell).
\]

For `x=\sum_j b_jc_j`, the code-first hull equations are

\[
B_{\mathrm{code}}(c_i,x)=0
\quad\Longleftrightarrow\quad
G\,\sigma(b)=0.
\]

Since coordinatewise `sigma` is bijective, the solution space has dimension

\[
 r-\operatorname{rank}(G).
\]

For the candidate-first hull, write `x=\sum_i a_i c_i`. Its equations are

\[
B_{\mathrm{cand}}(x,c_j)=0
\quad\Longleftrightarrow\quad
G^{\mathsf T}a=0.
\]

Therefore

\[
\dim H_{\mathrm{code}}(C)
 =r-\operatorname{rank}(G)
 =r-\operatorname{rank}(G^{\mathsf T})
 =\dim H_{\mathrm{cand}}(C).
\]

This proof applies to every `K_s`-linear code, including codes that are not constacyclic and codes that are not Frobenius-invariant. It explains why equality of hull dimensions survived the non-invariant F8 and F16 selections. It does not turn the hull subspaces or their factor supports into equal objects.

For a square-free affine product, apply the argument componentwise and sum the component dimensions with the declared `\mathbb F_q` weights.

**Theorem status: PROVED.**

## 11. LCD Invariance

By Section 10,

\[
\dim H_{\mathrm{code}}(C)=0
\Longleftrightarrow
\dim H_{\mathrm{cand}}(C)=0.
\]

Hence

\[
H_{\mathrm{code}}(C)=\{0\}
\Longleftrightarrow
H_{\mathrm{cand}}(C)=\{0\}.
\]

The two conventions always give the same LCD decision for the same finite-field-linear code, although the zero-hull property does not imply equality of the nonzero hull subspaces in other cases.

**Theorem status: PROVED.**

## 12. Hull-Support Comparison

Assume the compatible simple-root case so that both dual generators lie in the same factor set `F`. For a selected generator-factor support `J`, let `tau_rho` be the factor permutation induced by the code-first reciprocal and `tau_sigma` the one induced by the candidate-first reciprocal. The factor supports of the two hull generators are

\[
S_{\mathrm{code}}=(F\setminus J)\cap\tau_\rho(J),
\qquad
S_{\mathrm{cand}}=(F\setminus J)\cap\tau_\sigma(J).
\]

These supports are not generally equal. More explicitly, the actual factor support of each dual generator is

\[
D_{\mathrm{code}}^{\mathrm{fac}}=\tau_\rho(F\setminus J),
\qquad
D_{\mathrm{cand}}^{\mathrm{fac}}=\tau_\sigma(F\setminus J).
\]

The factor support of the corresponding hull generator is

\[
J\cup D_{\mathrm{code}}^{\mathrm{fac}}
\quad\text{or}\quad
J\cup D_{\mathrm{cand}}^{\mathrm{fac}},
\]

and the complementary factor sets used to measure hull dimension are

\[
S_{\mathrm{code}}=(F\setminus J)\cap\tau_\rho(J),
\qquad
S_{\mathrm{cand}}=(F\setminus J)\cap\tau_\sigma(J).
\]

The independent exhaustive results include:

- F8, `lambda=1`, `k=1`: 120/128 dual-generator support differences and 90/128 hull-generator/complement-support differences;
- F8, `lambda=1`, `k=2`: 120/128 dual-generator support differences and 90/128 hull-generator/complement-support differences;
- F16, `lambda=1`, `k=1`: 24/32 dual-generator support differences and 16/32 hull-generator/complement-support differences;
- F16, `lambda=1`, `k=3`: 24/32 dual-generator support differences and 16/32 hull-generator/complement-support differences.

The weighted sizes nevertheless agree because `tau_sigma=tau_rho^{-1}`, each permutation preserves factor degree, and on a cyclic binary word the number of `1\to0` transitions equals the number of `0\to1` transitions. Thus the present hull-dimension statistic is invariant, while the factor-labelled dual and hull supports are convention-specific.

For incompatible twists there is no same-factor-set support comparison: the candidate-first and code-first duals belong to different constacyclic twist families. Their abstract hull dimensions and LCD decisions still agree by Section 10.

**Theorem status: PROVED WITH CONDITIONS.**

## 13. Factor-Permutation Comparison

For a root `alpha` of the compatible modulus, the two reciprocal root actions are

\[
rho\text{-action}:\quad \alpha\longmapsto\alpha^{-p^{d_s-k}},
\]

and

\[
sigma\text{-action}:\quad \alpha\longmapsto\alpha^{-p^k}.
\]

Their composition is the identity:

\[
(\alpha^{-p^{d_s-k}})^{-p^k}=\alpha,
\qquad
(\alpha^{-p^k})^{-p^{d_s-k}}=\alpha.
\]

After passing from roots to irreducible factors,

\[
\boxed{\tau_\sigma=\tau_\rho^{-1}.}
\]

The Phase-5 implementation found zero failures of both compositions in every compatible case. The coefficientwise `T=sigma^2` action on a code's factor selection is a different, non-reciprocal factor permutation; it explains the individual-code Frobenius-invariance failures.

**Theorem status: PROVED.**

## 14. Reciprocal Comparison

For a monic polynomial `f` with nonzero constant term, define `R_phi(f)` by the normalized reciprocal using a field automorphism `phi`:

\[
R_\phi(f)(x)=\phi(f_0)^{-1}
 \sum_i\phi(f_i)x^{\deg f-i}.
\]

The code-first and candidate-first operations are `R_rho` and `R_sigma`. Direct coefficient calculation gives

\[
R_\sigma(R_\rho(f))=f,
\qquad
R_\rho(R_\sigma(f))=f,
\]

while

\[
R_\rho(R_\rho(f))=\rho^2(f),
\qquad
R_\sigma(R_\sigma(f))=\sigma^2(f).
\]

The normalizing constants are essential; these are exact equalities for the normalized monic operation, not equality only up to an unspecified scalar. The two operations preserve degree and map irreducible factors to irreducible factors of the corresponding transformed modulus. They are generally different maps, and their induced factor permutations are inverse rather than equal.

**Theorem status: PROVED.**

## 15. Enumerator Comparison

Let `\mathcal C_\lambda` be the same set of labeled factor-selection codes for a compatible simple-root `lambda`-constacyclic modulus. Define

\[
E_{\mathrm{code}}(u,z)
 =\sum_{C\in\mathcal C_\lambda}
   u^{\dim C}z^{\dim H_{\mathrm{code}}(C)},
\]

and define `E_cand` by replacing `H_code` with `H_cand` while keeping the same code `C` and the same labels. Section 10 gives equality term by term:

\[
\boxed{E_{\mathrm{code}}(u,z)=E_{\mathrm{cand}}(u,z).}
\]

This is an enumerator invariance theorem, not a dual-code equality theorem. It requires that both polynomials enumerate the same code collection and use hull dimension rather than the factor-labelled support itself. If a candidate-first literature formula is applied with a different twist family or to a different parameterized code collection, the identification must first be made explicit.

The present paper's main enumeration is therefore valid for the frozen code-first convention. Its numerical bivariate output is also the same under the candidate-first pairing on the same compatible labeled code set, but its support formula and dual-generator labels are not the same.

**Theorem status: PROVED WITH CONDITIONS.**

## 16. Total-Code Count Comparison

The total count is the number of codes being enumerated, not the number of dual subspaces. For a square-free component with factor set `F`, the labeled factor-selection count is

\[
|\mathcal C_\lambda|=2^{|F|}.
\]

Changing the dual pairing does not change `C` or the selected factors. Hence the total-code count is exactly equal under the two hull conventions. Under the compatible `T` action, `T` merely permutes the factor selections and also preserves the count.

This remains a labeled count; it is not a rotation, isomorphism, or equivalence-class count.

**Theorem status: PROVED WITH CONDITIONS.**

## 17. Dimension Distribution Comparison

The code dimension is determined by the selected factor degrees:

\[
\dim_{K_s}C_J=n-\sum_{f\in J}\deg(f).
\]

It is independent of which dual pairing is used. Therefore the code-dimension distribution agrees term by term for the same labeled selections. The independent search found identical dimension histograms in every tested F4, F8, and F16 case, including compatible and incompatible twists.

A Frobenius reindexing of factor selections also preserves factor degrees, so the result is unchanged if the comparison is expressed through the semilinear family map `T`.

**Theorem status: PROVED.**

## 18. Mean/Variance Comparison

Sections 10 and 15 imply equality of the full hull-dimension distribution for the same code family. Consequently the total, mean, second moment, and variance of hull dimension are equal:

\[
\mathbb E_{\mathrm{code}}[H]=\mathbb E_{\mathrm{cand}}[H],
\qquad
\operatorname{Var}_{\mathrm{code}}(H)
 =\operatorname{Var}_{\mathrm{cand}}(H).
\]

This includes the exceptional short-orbit variance behavior already derived in the present transfer method. It is not necessary for this numerical conclusion that the two oriented supports be equal. Equal weighted boundary counts and the general Gram theorem provide the required invariance.

**Theorem status: PROVED WITH CONDITIONS.**

## 19. Counterexample Search

Added `validation/phase5_convention_counterexamples.py`. The search uses fresh finite-field, polynomial, row-reduction, direct-dual, intersection, reciprocal, twist, and support code. It does not import Phase-3 or Phase-4 implementations.

The exhaustive cases include:

- F4: `k=0,1`, `lambda=1`, and a compatible nontrivial twist;
- F8: `k=0,1,2`, `lambda=1`, and incompatible twists where available;
- F16: `k=0,1,2,3`, `lambda=1`, compatible nontrivial twists, and incompatible twists where available;
- all factor selections of the listed small odd lengths;
- a deterministic sample of 1,182 arbitrary rank-2 codes in `F8^3`.

The search found:

- no failure of `D_cand=T(D_code)`;
- no hull-dimension counterexample;
- no LCD-decision counterexample;
- no reciprocal-composition failure;
- no factor-permutation inverse failure;
- no constacyclic twist-transformation failure;
- many individual-code Frobenius-invariance failures;
- many dual-code and hull-subspace differences;
- many factor-support differences in compatible non-involutory cases.

The arbitrary-code sample found zero hull-dimension and LCD counterexamples. This finite result agrees with the general Gram-matrix proof; it is not used as that proof.

**Theorem status: COMPUTATIONALLY VERIFIED ONLY.**

## 20. Independent Computational Verification

The two direct dual implementations are separate:

1. the code-first solver substitutes `y=sigma(x)`, solves the defining ordinary coefficient equations for `y`, and applies the explicitly computed inverse Frobenius;
2. the candidate-first solver independently Frobenius-transforms the codeword rows and solves the candidate equations directly.

The candidate result is not constructed by transforming the code-first result. The transformation is computed only afterward as a comparison. Hull dimensions are computed from independent intersections, LCD decisions are computed from those dimensions, and factor supports are computed from independently implemented reciprocal permutations.

The captured command is:

```text
env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 LC_ALL=C PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="" python validation/phase5_convention_counterexamples.py
```

The complete stdout, timestamp, Python version, stderr, and exit code are in `validation/phase5_convention_counterexamples.out`.

**Theorem status: COMPUTATIONALLY VERIFIED ONLY.**

## 21. Literature Implication

The source's candidate-first definition and its displayed inverse-Frobenius reciprocal/twist must still be described separately. The source formula is not a literal candidate-first dual-generator formula for non-involutory `sigma`; it becomes the frozen code-first formula after the convention conversion.

Phase 5 adds a precise numerical-transfer result: once the same code family and hull-dimension statistic are fixed, the candidate-first and code-first hull distributions, LCD count, mean, and variance agree by the general Gram theorem. This does not authorize attribution of the present code-first factor-support theorem to the source. Source theorem transfer still requires matching its hypotheses, component exponent, twist, and convention.

The local source-PDF readability and final-publisher-text limitations recorded in Phase 4 remain unchanged.

**Theorem status: PROVED WITH CONDITIONS.**

## 22. Manuscript Integration

A dedicated subsection titled **Convention Reconciliation with Existing Literature** was added to `new-paper-blueprint.md`. It states:

1. the source candidate-first inner product and dual equation;
2. the present code-first second-slot definition;
3. the exact transformation `D_cand=T(D_code)` with `T=sigma^2`;
4. that dual codes are semilinearly isomorphic but not generally equal;
5. that hull subspaces and factor supports are not generally equal;
6. that hull dimensions and LCD decisions are equal for every finite-field-linear code;
7. that the main theorem uses the frozen code-first convention;
8. that the literature theorem is convention-qualified and cannot be transferred as printed without conversion.

The blueprint's main enumerator remains the code-first inverse-Frobenius support formula. Candidate-first forward/inverse support is documented as a comparison and is not silently substituted for the principal formula.

**Theorem status: PROVED WITH CONDITIONS.**

## 23. Remaining Mathematical Gaps

The central Phase-5 invariance questions are resolved with the conditions stated above. Remaining publication-critical items are outside the central dual/hull-dimension theorem:

1. the final publisher PDF/theorem-level source comparison remains limited by local PDF extraction;
2. N1 remains `UNSPECIFIED — CANNOT VALIDATE`;
3. incompatible twists do not admit the same-factor-set support/enumerator transfer formula;
4. repeated-root cases are outside the simple-root theorem;
5. Burnside/Pólya equivalence counting remains future work;
6. quantum distance and full QECC parameter claims remain conditional.

No counterexample was found to the general hull-dimension or LCD invariance theorem, and no unproved equality of dual codes or factor supports is claimed.

## 24. Final Phase-5 Verdict

### Required invariance table

| Quantity | Candidate-first | Code-first | Equal? | Isomorphic? | Condition |
|---|---|---|---|---|---|
| Dual code | `D_cand=σ²(D_code)` | `D_code` | No, generally | Yes, via coordinatewise `σ²` | Equal only if the relevant dual is `σ²`-invariant |
| Dual dimension | `n-dim C` | `n-dim C` | Yes | N/A | Any `K_s`-linear `C` |
| Constacyclic twist | `σ(λ^{-1})` | `ρ(λ^{-1})` | Not generally | Yes, `σ²` maps one to the other | Equal when `σ²(λ)=λ`; common compatibility implies this |
| Reciprocal | `R_σ` | `R_ρ` | Not generally | Inverse operations | `R_σR_ρ=R_ρR_σ=1` on normalized monic inputs |
| Root action | `α↦α^{-p^k}` | `α↦α^{-p^{d_s-k}}` | Not generally | Inverse actions | Same compatible factor set |
| Factor permutation | `τ_σ` | `τ_ρ` | Not generally | `τ_σ=τ_ρ^{-1}` | Same compatible factor set |
| Hull subspace | `C∩D_cand` | `C∩D_code` | No, generally | Only if `σ²(C)=C` | Exact transformed identity uses `σ²(C)` |
| Hull dimension | `dim(C∩D_cand)` | `dim(C∩D_code)` | Yes | N/A | Any `K_s`-linear `C` |
| LCD property | Hull dimension zero | Hull dimension zero | Yes | N/A | Any `K_s`-linear `C` |
| Hull support | `(F\J)∩τ_σ(J)` | `(F\J)∩τ_ρ(J)` | No, generally | Inverse-labelled orientation only | Weighted sizes agree on degree-preserving cycles |
| Total code count | `2^{|F|}` | `2^{|F|}` | Yes | N/A | Same labeled code family |
| Dimension distribution | Factor-degree distribution | Factor-degree distribution | Yes | N/A | Same selections; Frobenius preserves factor degree |
| Hull distribution | `E_cand(1,z)` | `E_code(1,z)` | Yes | N/A | Same code family and hull-dimension statistic |
| Joint enumerator | `E_cand(u,z)` | `E_code(u,z)` | Yes | N/A | Same labeled codes, compatible main model |
| Mean | `E_cand[H]` | `E_code[H]` | Yes | N/A | Follows from hull-distribution equality |
| Variance | `Var_cand(H)` | `Var_code(H)` | Yes | N/A | Follows from hull-distribution equality |

The exact mathematical conclusion is: the conventions are not identical, their duals are related by a coordinatewise Frobenius automorphism, their hull subspaces and factor-labelled supports are not generally invariant, but hull dimensions, LCD decisions, and the same-family dimension/hull enumerator are proved invariant.

**Phase-5 verdict: `PASS WITH CONDITIONS — INVARIANCE PROVED UNDER EXPLICIT CONDITIONS`.**
