# Phase 3 Adversarial Manuscript-Level Audit

## 1. Audit Scope

This audit treats the proposed paper as if it were being reviewed by a hostile expert referee. It rechecks the Phase-2 proof audit rather than accepting its statuses, reads the current blueprint and all validation material, inspects the available source record, and runs an independent implementation that does not import the existing validator modules.

The audit covers the 19 mathematical claims, every stated hypothesis, the factor-selection counting model, the hull-support orientation, edge cases, literature-dependent statements, N1, manuscript-level scope, quantum/Burnside boundaries, the ZIP, and reproducibility. It distinguishes proof from finite evidence throughout.

No general result is accepted merely because a prior validator passed or because the Phase-2 report marked it conditionally proved.

## 2. Repository State

The Phase-3 prompt identifies `5e4ea83 — Add rigorous Phase-2 proof audit` as the current Phase-2 commit. The checkout at audit start was different:

- branch: `arena/01a0c9d2-galios-hull`;
- actual `HEAD`: `5f064ca — Delete Corrections_Request_for_Arena_Galois_Hull_Blueprint.docx`;
- the object IDs `5e4ea83` and `7e4fbbb` were not present in the local Git object database at that time;
- the Phase-1/Phase-2 research files were present as untracked working-tree files rather than as the claimed Phase-2 commit;
- the only tracked file at audit start was the source PDF.

This was a reproducibility and provenance discrepancy, not evidence that the mathematics was false. The remote branch was fetched before publication; it revealed the claimed Phase-2 history, including `5e4ea83` and `7e4fbbb`. The Phase-3 commit `96752c7` was then merged with that history in `4ec522b`, and the fixed branch was pushed successfully. The final repository therefore preserves the historical Phase-2 commit and the Phase-3 artifacts without fabricating history.

The available materials inspected were:

- `new-paper-blueprint.md`;
- `validation/VALIDATION_REPORT.md`;
- `validation/PHASE2_PROOF_AUDIT.md`;
- all six original validators;
- all Phase-2 captures;
- `validation/phase2_counterexample_search.py` and its output;
- the source PDF;
- the rebuilt ZIP, README, and manifest;
- all local mathematical and validation specifications.

## 3. Frozen Mathematical Convention

The audit retained the required convention:

\[
\sigma_{s,k}(a)=a^{p^k},
\qquad
\rho_{s,k}(a)=a^{p^{e m_s-k}},
\]

on `K_s=F_{q^{m_s}}=F_{p^{e m_s}}`, with

\[
\langle x,y\rangle_{s,k}=\sum_i x_i y_i^{p^k}
\]

and the code in the first slot of the dual definition:

\[
C_s^{\perp_k}=\{x:\langle c,x\rangle_{s,k}=0\text{ for all }c\in C_s\}.
\]

The principal reciprocal, dual twist, and compatibility condition remain

\[
f^{\#_{s,k}}(x)=f_0^{-p^{e m_s-k}}
 \sum_i f_i^{p^{e m_s-k}}x^{d-i},
\]

\[
\lambda_s^{-p^{e m_s-k}},
\qquad
\lambda_s^{1+p^{e m_s-k}}=1.
\]

A convention issue was found in the literature audit: the accessible source preprint literally defines its finite-field dual with the candidate in the first slot, `\langle\alpha,c\rangle_k=0`, while its displayed reciprocal uses the inverse-Frobenius exponent. The present paper's code-first convention is therefore not silently attributed to that source. An independent F8 probe in the new checker shows that the literal candidate-first equations select the sigma reciprocal in one nontrivial example, while the frozen code-first equations select the rho reciprocal. This is a literature-convention reconciliation issue, not a change to the frozen Phase-3 convention.

## 4. Master Assumption Audit

| Assumption | Required where and why | Explicit? | What breaks if removed |
|---|---|---|---|
| `q=p^e`, `e\ge1` | Defines the base Frobenius and admissible `k` | Yes | The exponents and Galois parameter are undefined |
| Characteristic `p` | All field-power and derivative arguments | Yes through `q=p^e` | The Frobenius and simple-root proof lose their meaning |
| `char(F_q)\ne2` | Not required | No restriction is needed; characteristic two is explicitly tested | No failure; imposing it would unnecessarily narrow the theorem |
| Monic square-free `t_i` | Reduced affine decomposition and primitive idempotents | Yes | Nilpotents or repeated components can appear; binary factor selection is no longer sufficient |
| Positive degree of each `t_i` | Nonzero finite product-of-fields decomposition | Yes after Phase 2 | A unit constant relation can give the zero quotient |
| Finite-field separability | Tensor-product/product-of-fields proof | Follows because finite fields are perfect | The reduced tensor-product conclusion would need another hypothesis |
| Field components `K_s=F_{q^{m_s}}` | Component codes, dimensions, Frobenius | Yes | Ring components cannot be treated as field ideals |
| Fixed componentwise Frobenius/idempotent labeling | Global componentwise inner product and independent product count | Now made explicit | A Frobenius permutation of components would require a coupled orbit theory |
| `lambda_s\in K_s^\times` | Constacyclic modulus and nonzero constant terms | Yes | The modulus may not define a unit constacyclic shift and reciprocal normalization can fail |
| `n\ge1` | Code length | Yes | No code length exists |
| `gcd(n,p)=1`, equivalently `gcd(n,q)=1` | Makes `x^n-lambda_s` square-free | Yes; equivalence now stated explicitly | Repeated-root factors occur and binary selections are incomplete |
| Primitive roots in an algebraic closure | Root-action proof only | Not a theorem hypothesis; roots are used in an algebraic closure | No failure; factor arguments can be phrased without choosing primitive roots |
| Order of `lambda` | Needed by some source cyclotomic formulas | Not needed by the present transfer theorem beyond unit/compatibility | Source-specific factor formulas cannot be imported without their order hypotheses |
| `0\le k<e` | Frozen base-field Galois parameter | Yes | The stated sigma/rho relation would need a new parameter convention |
| Reduction of Frobenius iteration modulo `e m_s` | Computational implementation | Explicit in the audit/checker | An API could apply the wrong automorphism |
| Compatibility `lambda_s^(1+p^(e m_s-k))=1` | Same-factor-set orbit enumerator | Yes | The dual has twist `lambda_s^{-p^(e m_s-k)}` and the compatible transfer theorem is invalid |
| Labeled factor selections | Injective code count and product enumerator | Yes | Quotienting by equivalence would require a group action and Burnside/Pólya analysis |
| Simple factor multiplicity one | Hull support as a binary set | Follows from `gcd(n,p)=1` | Multiplicity data and a repeated-root theory are required |
| Self-reciprocal/fixed factors | Edge cases of `tau` orbits | No extra assumption; handled | Treating them as 2-cycles would give a wrong hull contribution |
| Orbit lengths 1 and 2 | Boundary and variance exceptions | No restriction; handled separately | Using `a/16` for `a=2` is false |
| Orbit lengths greater than 2 | General transfer theorem | No restriction; explicitly allowed | Restricting to pairs would omit valid factors |
| Component independence | Product enumerator and moments | Follows from product decomposition plus labeled choices | Coupled choices would invalidate the product |
| Uniform probability on distinct labeled codes | Mean and variance | Yes | The moment formulas would describe a different measure |

No hidden `char(F_q)\ne2`, primitive-root existence inside the base field, or order condition on `lambda` is needed by the present general theorem. The source-paper order assumptions belong to its cyclotomic classification and are not silently imported.

## 5. Theorem 1 Audit

**A. Exact statement.** A finite affine quotient by separate monic square-free positive-degree relations decomposes as a finite product of fields `A\cong\prod_s K_s` with primitive orthogonal idempotents.

**B. Exact hypotheses.** `q=p^e`, positive-degree monic square-free `t_i`, finite number of variables, and the stated separate-variable ideal.

**C. Exact conclusion.** Each univariate quotient is a product of finite fields, and the tensor product of those finite separable algebras is again a finite product of finite fields.

**D. Dependency chain.** Univariate CRT → finite-field factors → finite-field perfection/separability → tensor-product finite étale algebra → primitive idempotents.

**E. Hidden assumptions.** Positive degree and the separate-variable form are essential. A componentwise Frobenius action is part of the global convention.

**F. Edge cases.** Characteristic two is allowed; repeated roots are not. Two identical irreducible factors in different variables can produce a product such as `F_{q^d}\otimes F_{q^d}`, which is a product of fields rather than necessarily one field.

**G. Counterexample search.** Small characteristic-two fields and the independent product check found no counterexample. The algebraic proof does not depend on those examples.

**H. Literature dependency.** None for the present proof. The source preprint gives an idempotent decomposition, but its exact notation is not needed.

**I. Computational support.** The F4 four-component pilot and the independent F4 × F4 product check support the component model only finitely.

**J. Referee risk.** Medium if the positive-degree and separability steps are omitted from a manuscript; low after the explicit proof.

**K. Final Phase-3 status.** `VALID WITH CONDITIONS`.

## 6. Theorem 2 Audit

**A. Exact statement.** Polynomial CRT identifies `A[x]/(x^n-lambda)` with the product of `K_s[x]/(x^n-lambda_s)`, and a ring constacyclic code is exactly a tuple of component constacyclic ideals.

**B. Exact hypotheses.** The product decomposition, `lambda\in A^\times`, and the componentwise shift.

**C. Exact conclusion.** The shift acts componentwise, the ideal/code correspondence is bijective, and dimensions add with weights `m_s`.

**D. Dependency chain.** Ring product → polynomial product → component shift → component ideals → product code.

**E. Hidden assumptions.** The code is an `A`-submodule, not an arbitrary additive code. The factor choices are labeled by component and factor.

**F. Edge cases.** Zero and full component codes are included; unequal `m_s` are allowed; component twists may differ subject to componentwise compatibility.

**G. Counterexample search.** The independent F4 × F4 enumerator gives `8^2=64` choices and confirms multiplication of component enumerators. No non-independent choice was found because the idempotents separate the ideals.

**H. Literature dependency.** None for the CRT proof.

**I. Computational support.** Existing F4 ring pilot and the independent product check.

**J. Referee risk.** Medium if “component independence” is stated without proving the idempotent reconstruction.

**K. Final Phase-3 status.** `VALID WITH CONDITIONS`.

## 7. Theorem 3 Audit

**A. Exact statement.** The form is first-linear and second-slot `sigma`-semilinear, nondegenerate, and the code-first annihilator is the ordinary Euclidean dual of the coefficientwise `rho`-image.

**B. Exact hypotheses.** `K_s=F_{p^{e m_s}}`, `0\le k<e`, and the componentwise definition.

**C. Exact conclusion.** `C^{\perp_k}=rho(C)^{\perp_E}=rho(C^{\perp_E})`; its dimension is `n-dim_K C`.

**D. Dependency chain.** Frobenius inverse → apply `rho` to defining equations → ordinary annihilator → dimension.

**E. Hidden assumptions.** This is not a symmetric bilinear form. The componentwise Frobenius convention is required. `C^{\perp_k}` is K-linear even though the form is semilinear.

**F. Edge cases.** For `k=0`, the form is Euclidean. In general, double dual is not automatically `C`: with the code-first convention, direct calculation gives

\[
(C^{\perp_k})^{\perp_k}=\rho^2(C),
\]

so involutive double-duality requires an additional condition such as `rho^2(C)=C` (or an involutive automorphism). The blueprint never uses double duality, but this caveat must be stated if a manuscript calls the operation an involutive duality.

**G. Counterexample search.** The F8 non-involutory setting supplies the relevant edge regime; the independent checker confirms dimension complements. A non-Frobenius-stable arbitrary linear code would witness the double-dual caveat, so no blanket double-dual claim is safe.

**H. Literature dependency.** The accessible source preprint defines the candidate-first annihilator, not the frozen code-first one. Its dimension statement cannot be used without convention translation.

**I. Computational support.** Direct defining-equation calculations in all existing validators and the independent checker.

**J. Referee risk.** High if double duality or source convention is stated without qualification.

**K. Final Phase-3 status.** `VALID WITH CONDITIONS`.

## 8. Theorem 4 Audit

**A. Exact statement.** The principal normalized reciprocal applies `rho` to coefficients and reverses/normalizes the polynomial.

**B. Exact hypotheses.** Monic polynomial with nonzero constant term over `K_s`.

**C. Exact conclusion.** The result is monic, multiplicative, irreducibility-preserving, degree-preserving, and bijective; its inverse is the corresponding `sigma` reciprocal.

**D. Dependency chain.** Field automorphism + ordinary reciprocal → normalization → multiplicativity/invertibility.

**E. Hidden assumptions.** Nonzero constant term is essential. The operation is not generally an involution.

**F. Edge cases.** The exact identity is

\[
(f^{\#_\rho})^{\#_\rho}=\rho^2(f),
\qquad
(f^{\#_\rho})^{\#_\sigma}=f.
\]

Thus “self-reciprocal” must mean fixed by the declared `tau`, not automatically fixed by applying the principal operation twice. Fixed points, 2-cycles, and longer cycles are all possible.

**G. Counterexample search.** The independent checker explicitly tests both identities on F4, F8, and F16 factors. F8 supplies a non-involutory orbit.

**H. Literature dependency.** None for the algebraic derivation; source notation requires reconciliation.

**I. Computational support.** Independent reciprocal implementation and all prior factor-action validators.

**J. Referee risk.** Medium; the old blueprint already warned that `tau` need not be an involution, but the square identity should be stated explicitly.

**K. Final Phase-3 status.** `VALID WITH CONDITIONS`.

## 9. Theorem 5 Audit

**A. Exact statement.** If `f(alpha)=0`, then a root of `f#` is `alpha^{-p^{e m_s-k}}`.

**B. Exact hypotheses.** `f_0\ne0`, algebraic closure containing `alpha`, and the frozen reciprocal.

**C. Exact conclusion.** Direct substitution proves the displayed root action.

**D. Dependency chain.** Reversal identity → coefficient Frobenius → root inversion.

**E. Hidden assumptions.** None beyond nonzero constant term and extension of Frobenius to the algebraic closure.

**F. Edge cases.** Fixed roots/factors, odd/even orbit lengths, and roots in extension fields are all allowed. The root need not lie in `K_s`.

**G. Counterexample search.** F8 length 7 yields a 6-cycle; F16 over F4 yields a 4-cycle; F4 cases yield fixed points and a 2-cycle. No directional failure was found.

**H. Literature dependency.** None for the proof.

**I. Computational support.** Existing and independent factor-action checks.

**J. Referee risk.** Low after the root substitution is included.

**K. Final Phase-3 status.** `VALID WITH CONDITIONS`.

## 10. Theorem 6 Audit

**A. Exact statement.** Under compatibility, `tau(f)=f#` is a permutation of the irreducible factors of `x^n-lambda_s`.

**B. Exact hypotheses.** The simple-root modulus, unit twist, and `lambda_s^{1+p^{e m_s-k}}=1`.

**C. Exact conclusion.** Root action preserves the modulus; irreducibility and invertibility give a bijection, and factor degrees are preserved.

**D. Dependency chain.** Theorem 4 → root action → compatibility → finite-set injection.

**E. Hidden assumptions.** Factors are distinct. Incompatible twists do not admit the same-factor-set orbit theorem.

**F. Edge cases.** `tau` can have lengths 1, 2, 3, 4, 6, or other finite lengths. It depends on the component field and `k`; the operation is common but the factor set depends on `lambda_s`.

**G. Counterexample search.** Independent F8 k=1 and k=2, F16 over F4, and nontrivial F4 twist cases all give permutations. No multiplicity counterexample is relevant under `gcd(n,p)=1`; repeated-root cases are outside scope.

**H. Literature dependency.** The source preprint gives a more specialized orbit arrangement with order hypotheses; it is not imported as the general proof.

**I. Computational support.** All factor-action outputs and independent checker.

**J. Referee risk.** Medium if the paper presents the source's cyclotomic orbit classification as necessary for the present abstract permutation.

**K. Final Phase-3 status.** `VALID WITH CONDITIONS`.

## 11. Theorem 7 Audit

**A. Exact statement.** For `C_s=<g_{J_s}>`, the code-first dual is generated by `h_{J_s}^{#}`.

**B. Exact hypotheses.** `M_s` simple-root, `g` a divisor, and the code-first dual convention; same-modulus use additionally requires compatibility.

**C. Exact conclusion.** Applying `rho` maps the defining dual to the ordinary dual of `rho(C_s)`. The ordinary constacyclic dual lemma gives the normalized reciprocal of `rho(h)`, exactly `h#`.

**D. Dependency chain.** Theorem 3 → ordinary constacyclic dual coefficient proof → reciprocal normalization → twist tracking.

**E. Hidden assumptions.** The ordinary lemma uses a nonzero constant term and the vector/polynomial convention. The dual twist is generally `lambda_s^{-p^{e m_s-k}}`, not automatically `lambda_s`.

**F. Edge cases.** Zero and full codes are covered by empty shift ranges; fixed factors and arbitrary generator subsets are covered; dimensions satisfy `dim C+dim C^perp=n`.

**G. Counterexample search.** All existing finite checks and the independent checker compare direct defining-equation duals with `h#` for every selection in the tested cases.

**H. Literature dependency.** The source theorem is not used as proof because of its displayed candidate-first definition/convention mismatch. The ordinary lemma is proved directly in Phase 2.

**I. Computational support.** F4, F8, F16, nontrivial twist, N2-A, N2-B, and independent checks.

**J. Referee risk.** High if the source theorem is cited without the present convention translation; low for the self-contained proof.

**K. Final Phase-3 status.** `VALID WITH CONDITIONS`.

## 12. Theorem 8 Audit

**A. Exact statement.** Same-twist compatibility is equivalent to preservation of the roots of `x^n-lambda_s` under the principal root action.

**B. Exact hypotheses.** `lambda_s\in K_s^\times`, `n\ge1`, and the frozen `rho` action.

**C. Exact conclusion.** The condition is necessary and sufficient:

\[
\lambda_s^{1+p^{e m_s-k}}=1.
\]

It is componentwise and depends on `k`.

**D. Dependency chain.** Root action → raise to the `n`th power → equality of twists.

**E. Hidden assumptions.** The twist is a unit and lies in the component field. No requirement that `lambda` lie in the base field is needed.

**F. Edge cases.** `lambda=1` is always compatible. Nontrivial compatible twists occur, e.g. F4 `lambda=omega`, `k=1`. Incompatible twists are not enumerated by the same-factor transfer theorem.

**G. Counterexample search.** F4, F8, F16, and incompatible F4/F16 diagnostics agree with the predicted twist. No compatibility counterexample was found.

**H. Literature dependency.** Source results impose order conditions for their specialized cyclotomic classification; the present condition is independently derived.

**I. Computational support.** N2-B checks both predicted twists and failure of the original twist.

**J. Referee risk.** Medium if the paper states compatibility only globally and omits the component index.

**K. Final Phase-3 status.** `VALID WITH CONDITIONS`.

## 13. Theorem 9 Audit

**A. Exact statement.** The component hull support is

\[
(\mathcal F_s\setminus J_s)\cap\tau_{s,k}(J_s).
\]

**B. Exact hypotheses.** Simple-root factorization, compatible factor permutation, and the dual generator from Theorem 7.

**C. Exact conclusion.** The intersection ideal is generated by the lcm, and omitted lcm factors are exactly the displayed support.

**D. Dependency chain.** Dual support `tau(F\J)` → lcm intersection → set complement → bijectivity of `tau`.

**E. Hidden assumptions.** The factor sets are sets, not multisets. The factor-selection map is labeled and injective.

**F. Edge cases.** Empty and full selections yield zero hull; fixed factors contribute no boundary; longer cycles distinguish the forward and inverse candidate formulas.

**G. Counterexample search.** The independent checker exhausts all selections for F4, F8, F16, and nontrivial compatible twist cases. It computes direct hull dimensions and compares them with the forward support; it also counts selections where the inverse candidate differs. The forward formula agrees; no counterexample was found.

**H. Literature dependency.** None for the set derivation; source lcm formulas are not used as a substitute.

**I. Computational support.** Independent direct-dual, intersection-dimension, and support checks, in addition to the Phase-1/2 validators.

**J. Referee risk.** Critical in principle, because reversing `tau` changes non-involutory cases; the explicit derivation and independent check reduce the risk.

**K. Final Phase-3 status.** `VALID WITH CONDITIONS`.

## 14. Theorem 10 Audit

**A. Exact statement.** On an orbit with `tau(f_i)=f_{i+1}`,

\[
b_O(\varepsilon)=\sum_i\varepsilon_i(1-\varepsilon_{i+1}).
\]

**B. Exact hypotheses.** Cyclic indexing and the forward support orientation.

**C. Exact conclusion.** Each term counts the destination factor `f_{i+1}` exactly when its predecessor is selected and it is unselected.

**D. Dependency chain.** Theorem 9 support → orbit indexing → binary indicators.

**E. Hidden assumptions.** The final edge from `a-1` to `0` must be included.

**F. Edge cases.** `a=1` has boundary zero; `a=2` has mutually exclusive directed transitions; for every cyclic word the number of `1\to0` and `0\to1` edges agrees.

**G. Counterexample search.** Existing Phase-2 search checked lengths 1–12; the independent checker checks the same orientations in all tested factor cases. The required 1–16 symbolic extension is addressed by the cyclic-word proof; no finite mismatch was found through length 12 in the stored new search.

**H. Literature dependency.** None.

**I. Computational support.** Phase-2 search and independent checker.

**J. Referee risk.** Low after cyclic closure is explicit; medium if an implementation uses open strings.

**K. Final Phase-3 status.** `VALID WITH CONDITIONS`.

## 15. Theorem 11 Audit

**A. Exact statement.**

\[
P_{a,w}(z)=2+\sum_{b=1}^{\lfloor a/2\rfloor}
 2\binom{a}{2b}z^{bw},
\]

equivalently the displayed `a/b` run formula.

**B. Exact hypotheses.** Indexed cyclic binary selections and positive orbit weight `w`.

**C. Exact conclusion.** There are two constant words for `b=0`, and `2 binom(a,2b)` words with `b\ge1` boundaries.

**D. Dependency chain.** Cyclic transition positions → even number of transitions → two starting labels.

**E. Hidden assumptions.** The indexed orbit is not quotiented by rotation. The formula is valid for `a=1` with an empty positive-boundary sum.

**F. Edge cases.** The formula gives `2`, `2+2z^w`, `2+6z^w`, and the stated `a=4,5` values. No `a\ge2` restriction is required.

**G. Counterexample search.** Existing search through length 12; independent transfer/direct checks through the tested orbit lengths and explicit coefficient comparisons.

**H. Literature dependency.** None.

**I. Computational support.** Phase-2 output and independent checker.

**J. Referee risk.** Low; the binomial form also proves integrality.

**K. Final Phase-3 status.** `VALID WITH CONDITIONS`.

## 16. Theorem 12 Audit

**A. Exact statement.**

\[
T_w(u,z)=\begin{pmatrix}u^w&1\\u^wz^w&1\end{pmatrix}.
\]

**B. Exact hypotheses.** Destination state `t=epsilon_{i+1}` records code dimension and source/destination `1,0` records the boundary.

**C. Exact conclusion.** The four entries correctly encode `0->0`, `0->1`, `1->0`, and `1->1`.

**D. Dependency chain.** Code dimension from unselected factors + Theorem 10 boundary → transition weights.

**E. Hidden assumptions.** `u` is dimension, not selected-factor codimension. The factor weight is `m_s deg(f)`.

**F. Edge cases.** All orbit lengths and positive weights are valid; fixed points produce `1+u^w`.

**G. Counterexample search.** Independent matrix arithmetic checks lengths through 8 in the Phase-2 search and every tested factor orbit in the Phase-3 checker; the checker uses its own polynomial matrix implementation.

**H. Literature dependency.** None.

**I. Computational support.** Independent checker and previous finite validators.

**J. Referee risk.** Medium because the earlier blueprint had a codimension matrix; the corrected matrix and marginal check remove the ambiguity.

**K. Final Phase-3 status.** `VALID WITH CONDITIONS`.

## 17. Theorem 13 Audit

**A. Exact statement.** `tr(T_w^a)` is the sum over indexed binary sequences with the cyclic closing edge.

**B. Exact hypotheses.** A labeled orbit indexing and ordinary matrix multiplication.

**C. Exact conclusion.** Each labeled binary selection contributes once; the trace does not quotient by rotations.

**D. Dependency chain.** Matrix-product expansion → closed walks → indexed selections.

**E. Hidden assumptions.** “Cyclic word” here means a cyclically closed indexed sequence, not a necklace or rotation equivalence class.

**F. Edge cases.** Periodic words are still counted according to the fixed factor labels; no rotational division occurs.

**G. Counterexample search.** Direct binary-word enumeration equals the independent trace for all tested lengths/weights.

**H. Literature dependency.** None.

**I. Computational support.** Phase-2 and Phase-3 outputs.

**J. Referee risk.** High if the manuscript uses “orbit” ambiguously to imply quotienting by rotation.

**K. Final Phase-3 status.** `VALID WITH CONDITIONS`.

## 18. Theorem 14 Audit

**A. Exact statement.**

\[
\mathscr E(u,z)=\prod_{s,O}\operatorname{tr}(T_{w_O}(u,z)^{a_O}).
\]

**B. Exact hypotheses.** Product algebra, simple-root factor sets, compatible `tau`, labeled factor selections, and additive component dimensions.

**C. Exact conclusion.** The product counts distinct labeled codes by actual `F_q` code and hull dimensions.

**D. Dependency chain.** Theorem 2 bijection → orbit partition → Theorems 9–13 → multiplication of independent selection sums.

**E. Hidden assumptions.** Two different factor-selection tuples cannot represent the same product ideal. This is true because the component ideals have unique monic divisor generators and the primitive idempotents recover each component.

**F. Edge cases.** Isomorphic components remain labeled and distinct; equivalence classes are not counted. Zero/full choices are included.

**G. Counterexample search.** The independent F4 × F4 product check and all component enumeration totals support injectivity. The ideal-theoretic proof is the controlling argument.

**H. Literature dependency.** None for the labeled theorem; novelty comparison remains open.

**I. Computational support.** Direct joint histograms equal independent transfer histograms in all tested cases.

**J. Referee risk.** Critical if the word “orbit” is mistaken for an equivalence quotient; otherwise medium.

**K. Final Phase-3 status.** `VALID WITH CONDITIONS`.

## 19. Theorem 15 Audit

**A. Exact statement.**

\[
|\mathscr C(A,n,\lambda)|=2^{\sum_s|\mathcal F_s|}
\quad\text{and}\quad
\mathscr E(1,1)=2^{\sum_s|\mathcal F_s|}.
\]

**B. Exact hypotheses.** Unique square-free divisor factor selections and labeled components.

**C. Exact conclusion.** Every empty, full, and intermediate selection is counted once.

**D. Dependency chain.** Principal-ideal classification → product bijection → trace specialization.

**E. Hidden assumptions.** No equivalence or isometry quotient.

**F. Edge cases.** Zero and full codes are included; fixed factors still have two choices.

**G. Counterexample search.** Totals 8, 32, 128, and 64 for the tested cases agree with direct enumeration.

**H. Literature dependency.** None.

**I. Computational support.** Existing and independent outputs.

**J. Referee risk.** Low with the labeled qualifier; high if presented as inequivalent-code counting.

**K. Final Phase-3 status.** `VALID WITH CONDITIONS`.

## 20. Theorem 16 Audit

**A. Exact statement.**

\[
H(z)=\mathscr E(1,z),
\qquad N_h=[z^h]H(z).
\]

**B. Exact hypotheses.** The global enumerator hypotheses.

**C. Exact conclusion.** Coefficients count exactly the codes with each global `F_q` hull dimension.

**D. Dependency chain.** Global joint enumerator → specialization → coefficient extraction.

**E. Hidden assumptions.** Hull exponents use `m_s`-weighted factor degrees; impossible dimensions simply have zero coefficients.

**F. Edge cases.** Maximum hull dimension is the sum of weighted orbit boundary maxima, not automatically the ambient dimension. Fixed orbits contribute no hull dimension.

**G. Counterexample search.** Direct histograms agree with transfer polynomials in all stored tests and the independent checker.

**H. Literature dependency.** The exact all-code coefficient package is not verified in the cited literature.

**I. Computational support.** Finite histograms only.

**J. Referee risk.** Medium if component and base-field dimensions are conflated.

**K. Final Phase-3 status.** `VALID WITH CONDITIONS`.

## 21. Theorem 17 Audit

**A. Exact statement.** Hull dimension zero is equivalent to being LCD with respect to the frozen `k`-Galois dual, and the count is `2^{sum orbit counts}`.

**B. Exact hypotheses.** The compatible labeled model and positive factor weights.

**C. Exact conclusion.** Every orbit selection must be constant, giving exactly two selections per orbit.

**D. Dependency chain.** Definition of `k`-Galois LCD → Theorem 10 → positivity of weights.

**E. Hidden assumptions.** “LCD” must be read as **`k`-Galois LCD**, not automatically Euclidean LCD. The blueprint should say this explicitly at the first use in the enumerator section.

**F. Edge cases.** Fixed factors are always harmless; incompatible twists are outside the count; zero/full codes are included.

**G. Counterexample search.** Direct hull dimensions and histograms agree in all finite cases.

**H. Literature dependency.** The source literature uses the same broad LCD terminology but does not prove this present labeled orbit count.

**I. Computational support.** Existing and independent enumerations.

**J. Referee risk.** Medium due terminology, not mathematics.

**K. Final Phase-3 status.** `VALID WITH CONDITIONS`.

## 22. Theorem 18 Audit

**A. Exact statement.** Under the uniform distribution on distinct labeled factor-selection codes,

\[
E[H]=\sum_{s,O:a_O\ge2}a_Ow_O/4.
\]

**B. Exact hypotheses.** Theorem 14's bijection and the uniform probability measure.

**C. Exact conclusion.** Each factor indicator is independent Bernoulli `1/2`, and each orbit contributes `a w/4` except fixed points.

**D. Dependency chain.** Product selection measure → indicators → boundary expectation.

**E. Hidden assumptions.** This is not an average over equivalence classes or over all ambient linear codes.

**F. Edge cases.** `a=1` contributes zero; unequal weights and components are allowed.

**G. Counterexample search.** Direct finite histograms give the stated means in the stored examples; the independent checker confirms the joint enumerators from which the means follow.

**H. Literature dependency.** No literature result is required.

**I. Computational support.** Finite histogram checks.

**J. Referee risk.** Medium if the probability space is not stated immediately before the formulas.

**K. Final Phase-3 status.** `VALID WITH CONDITIONS`.

## 23. Theorem 19 Audit

**A. Exact statement.**

\[
\operatorname{Var}(H)=
\sum_{a_O=2}w_O^2/4+
\sum_{a_O\ge3}a_Ow_O^2/16.
\]

**B. Exact hypotheses.** Uniform independent labeled factor selections and the cyclic boundary indicators.

**C. Exact conclusion.** The `a=2` contribution is `w^2/4`; the `a\ge3` contribution is `a w^2/16`; fixed points contribute zero.

**D. Dependency chain.** Indicator variance/covariance → orbit independence → weighted sum.

**E. Hidden assumptions.** For `a=2`, the two directed edges are not a generic cycle-neighbor pattern and are mutually exclusive; the exception is necessary.

**F. Edge cases.** The formula handles lengths 1, 2, odd, even, and longer cycles.

**G. Counterexample search.** Exhaustive finite histograms and the independent transfer/direct enumerator checks agree; no variance mismatch was found.

**H. Literature dependency.** None.

**I. Computational support.** Stored examples include 2-, 4-, and 6-cycles.

**J. Referee risk.** Medium if a derivative calculation silently substitutes `a/16` for `a=2`.

**K. Final Phase-3 status.** `VALID WITH CONDITIONS`.

## 24. Critical Hull-Support Audit

This was repeated independently rather than accepted from Phase 2.

For `g` support `J`, the check polynomial has support `F\J`. The direct code-first dual has generator support `tau(F\J)`. The lcm intersection support is therefore

\[
J\cup\tau(F\setminus J),
\]

and its omitted factors are

\[
F\setminus[J\cup\tau(F\setminus J)]
=(F\setminus J)\cap\tau(J).
\]

If `tau(f_i)=f_{i+1}`, a supported destination factor requires `epsilon_i=1` and `epsilon_{i+1}=0`, giving the forward `1\to0` statistic.

The inverse candidate

\[
(F\setminus J)\cap\tau^{-1}(J)
\]

was also tested. It agrees in involutory cases, such as a 2-cycle, but differs for selected subsets of the F8 6-cycle. The captured independent run found `0` orientation-support differences for each F4 case, `90` for each F8 6-cycle case, and `16` for the F16-over-F4 4-cycle case. The inverse candidate produced `0` dimension matches failures only because the tested orbit factors have equal weights; it nevertheless gives the wrong labeled support in those cases. The forward formula agrees with direct hull dimensions in every tested selection.

**Result:** `PASS WITH CONDITIONS`. The formula is correct under the stated code-first, simple-root, compatible, labeled hypotheses; the inverse formula must not be substituted in non-involutory cases.

## 25. N1 Audit

The repository-wide search finds only the Phase-2 N1 record:

\[
q=16,
\qquad n=15,
\qquad 2^{15}=32{,}768.
\]

No `k`, `lambda`, component interpretation, factorization, orbit decomposition, expected histogram, or executable N1 code can be reconstructed from the current materials. The source preprint and the available blueprint do not specify a unique intended N1 experiment. No fake data or inferred `lambda=1`/`k` choice was created.

Required explicit label:

**N1: `UNSPECIFIED — CANNOT VALIDATE`.**

This is a material audit gap and remains separate from the proved conditional theory.

## 26. Literature Audit

The accessible arXiv preprint `arXiv:2412.08512` was inspected directly. It supports the broad facts that the source studies square-free affine algebras, `k`-Galois hulls, idempotent decompositions, dual/hull generators, LCD conditions, and quantum examples. It also explicitly states a candidate-first dual definition in its finite-field preliminaries. Its displayed reciprocal uses the inverse-Frobenius exponent. The independent F8 convention probe shows that this requires reconciliation before the source theorem can be used under the present code-first convention.

| Claim used by the blueprint | Record checked | Status | Safe use |
|---|---|---|---|
| Source paper studies square-free affine algebra `k`-Galois hulls and idempotents | arXiv:2412.08512 and publisher record | **PARTIALLY VERIFIED** | Broad background only |
| Source paper's exact dual-generator theorem transfers directly to the present code-first convention | arXiv HTML displays candidate-first definition and inverse-Frobenius formula | **SOURCE CONVENTION REQUIRES VERIFICATION** | Do not import as proof; use the self-contained Phase-2 derivation |
| Finite-field constacyclic Galois hull formula/counting exists | DOI `10.1007/s12095-022-00591-6`, Springer/ACM records and correction record | **PARTIALLY VERIFIED** | Background and comparison only; check the correction and exact hypotheses |
| Cyclic/negacyclic finite-field hull dimensions and fixed-dimension counts exist | DOI `10.1016/j.ffa.2014.12.008`, accessible abstract/record | **PARTIALLY VERIFIED** | Related finite-field background; not proof of the present product enumerator |
| Hermitian constacyclic average formulas exist | DOI `10.3934/amc.2018027`, publisher abstract | **VERIFIED AT ABSTRACT SCOPE** | Average-dimension comparison only |
| General Galois-hull methods exist | DOI `10.1007/s10623-019-00681-2`, publisher metadata/record | **PARTIALLY VERIFIED** | General background only |
| Affine-algebra source exact theorem labels and exact overlap | Local PDF structurally present, theorem text unavailable locally; arXiv preprint accessible | **VERIFY** | No exact theorem citation or priority claim |
| Ring-specific quantum/hull papers establish this transfer enumerator | Multiple listed records | **NOT VERIFIED** | Do not make that claim |
| Any cited paper establishes the present labeled bivariate transfer product | Search/records inspected; no exact theorem verified | **VERIFY** | Candidate contribution only, with no priority wording |

The literature audit does not fabricate DOI data. Records already marked metadata-only or DOI-unverified in Section 20A remain so. The local PDF has valid structural markers but that is not theorem-level inspection.

## 27. Novelty Audit

Known ingredients include finite-field Galois hulls, constacyclic reciprocal formulas, square-free affine/idempotent decompositions, lcm hull generators, and finite-field hull enumerations in related settings. The proposed contribution is more narrowly described as a conditional, coefficient-level **labeled factor-selection** joint enumerator with weighted factor-orbit transfer matrices, plus the derived LCD and moment formulas.

No “first,” “novel,” “best,” or “state-of-the-art” claim is supported by this audit. The safest statement is:

> Subject to the unresolved full-text comparison, this work gives a self-contained conditional derivation and finite validation of a labeled code-dimension/hull-dimension transfer enumerator for square-free affine products under compatible twists.

The exact novelty boundary remains `VERIFY` because the source preprint already contains related hull-generator and dimension theory, and the finite-field literature contains fixed-hull-dimension enumeration.

## 28. Scope Audit

The proved scope is narrower than “all constacyclic codes” without qualification. It covers:

- every finite base field `F_q`;
- every `n\ge1` with `gcd(n,q)=1`;
- every admissible `0\le k<e`;
- every unit component twist satisfying compatibility;
- every square-free positive-degree separate-variable affine quotient;
- simple-root factor selections with labeled components and factors;
- arbitrary factor orbit lengths.

It does not cover, without new work:

- repeated-root lengths or repeated-root affine relations;
- incompatible twists in the same-factor enumerator;
- equivalence classes/non-isometric codes;
- quantum minimum distance or unconditional quantum parameters;
- unverified source-literature theorem transfers;
- the unspecified N1 experiment.

The blueprint generally states these restrictions. Phase-3 corrections make the `gcd(n,q)=1` equivalence, componentwise Frobenius labeling, and `k`-Galois LCD terminology explicit.

## 29. Edge-Case Audit

| Edge case | Result |
|---|---|
| `k=0` | Euclidean component form; rho is the identity automorphism, although the iteration representation is `e m_s`; valid under compatibility |
| `k=e m_s-1` | In the admissible base-field range this is available when `m_s=1`; the F8 `k=2` independent check covers the analogous last Frobenius step |
| Smallest extension degree | `m_s=1` is covered by F4/F8 |
| `lambda=1` | Compatible and extensively checked |
| Nontrivial compatible `lambda` | F4 `lambda=omega`, `k=1`, checked |
| Incompatible `lambda` | F4 and F16 diagnostics; no same-factor enumerator used |
| Zero code | Empty shift ranges and full generator handled |
| Full code | Generator `1`, check polynomial `M`, handled |
| Orbit length 1 | Boundary zero and two choices |
| Orbit length 2 | Exceptional variance `1/4` handled |
| Orbit length >2 | F8 length 6 and F16 length 4 checked |
| Self-reciprocal/fixed factor | Fixed orbit contributes no hull boundary |
| Empty hull | Exactly constant selection on every orbit |
| Maximal hull | Bounded by weighted cyclic boundary maxima, not assumed to be ambient dimension |
| Odd/even orbit length | Binomial formula and transfer trace handle both |

The finite scripts do not exhaust every length through 16, but the cyclic proof is length-general and the independent checks cover the structurally distinct orbit regimes requested.

## 30. Dimension and Counting Audit

For every independently checked factor selection:

\[
\dim_{K_s}C_s+\dim_{K_s}C_s^{\perp_k}=n.
\]

The checker computes the direct dual by nullspace of the defining equations and computes

\[
\dim(C\cap C^{\perp_k})
=\dim C+\dim C^{\perp_k}-\dim(C+C^{\perp_k}).
\]

It compares this dimension with the forward factor-support degree and with the `z` exponent. It compares the actual code dimension, multiplied by `m_s`, with the `u` exponent. The tested zero/full/intermediate selections have no off-by-one or complement discrepancy.

The general reason is the unique divisor generator in the square-free quotient; finite rank calculations are regression evidence only.

**Result:** `PASS WITH CONDITIONS`.

## 31. Duplicate-Code Audit

The factor-selection-to-code map is injective under the stated labeled model:

1. each component ideal has a unique monic divisor generator of `M_s`;
2. that divisor uniquely determines `J_s`;
3. primitive idempotent projection recovers each component ideal;
4. two different tuples therefore give different product ideals.

Isomorphic field components are not identified. Rotations of an orbit are not identified. Thus the count is not a necklace count or an isometry count.

The independent F4 × F4 product check returns 64 codes from two independent 8-code components, supporting the proof.

**Result:** `PASS WITH CONDITIONS`.

## 32. Independent Computational Cross-Check

Added:

`validation/phase3_independent_enumerator_check.py`

It does not import any existing validator and independently implements:

- characteristic-two finite-field arithmetic for F4, F8, and F16;
- polynomial factorization for the tested small degrees;
- normalized reciprocal and its inverse;
- direct code-first semilinear dual nullspaces;
- direct hull dimensions;
- factor-support and forward/inverse orientation comparisons;
- independent orbit decomposition;
- independent polynomial transfer-matrix multiplication;
- global product multiplication;
- the incompatible F4 diagnostic;
- a literal candidate-first source-convention probe.

The captured output is in `validation/phase3_independent_enumerator_check.out`. The exact run was recorded at `2026-09-24T09:41:56+00:00` with Python `3.11.2`:

```text
env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 LC_ALL=C PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="" python validation/phase3_independent_enumerator_check.py
```

It exits `0` and reports:

- F4 `lambda=1`, 8 selections, 8 unique codes, 0 selection collisions;
- F4 nontrivial `lambda`, 8 selections, 8 unique codes, 0 selection collisions;
- F8 `k=1`, 128 selections and a 6-cycle, with 90 forward/inverse support differences;
- F8 `k=2`, 128 selections and a 6-cycle, with 90 forward/inverse support differences;
- F16 over F4, 32 selections and a 4-cycle, with 16 forward/inverse support differences;
- F4 × F4 labeled product total 64, 0 product collisions;
- direct/principal reciprocal agreement for every tested selection;
- direct hull/support and transfer agreement;
- candidate-first sigma/rho convention distinction;
- incompatible-twist behavior.

This is computational evidence only and does not replace the proofs.

## 33. Quantum Claim Audit

The blueprint correctly separates the classical enumerator from quantum applications. It explicitly states that hull dimension does not determine minimum distance and that a quantum construction theorem, Gray-map relation, dimension, entanglement parameter, and distance must be checked independently.

No unconditional quantum parameter is proved by the current framework. Quantum applications are therefore:

**`FUTURE WORK` / conditional application.**

## 34. Burnside/Pólya Scope Audit

The main theorem counts labeled factor selections. The trace closes an indexed orbit; it does not quotient by rotations or any code-equivalence group. The blueprint's Burnside section is conditional and requires a finite group, an action on codes, hull preservation, and fixed-code calculations.

No Burnside/Pólya equivalence-class result is claimed.

**Result:** `FUTURE WORK` for the optional extension.

## 35. Manuscript-Structure Audit

The blueprint has a coherent mathematical order: algebra, convention, reciprocal, dual/hull support, boundary, transfer, distribution, moments, validation, limitations, and optional applications. The abstract and conclusion now distinguish conditional theorem results from finite validation and keep N1 unresolved.

The following manuscript-level corrections are required before submission:

- state the componentwise Frobenius/idempotent convention in the preliminaries;
- state `gcd(n,q)=1` equivalently to `gcd(n,p)=1`;
- state the `#_rho^2=rho^2` caveat and do not imply involutive duality;
- call the count `k`-Galois LCD count where ambiguity is possible;
- replace source-paper theorem-level wording with convention-qualified citations;
- preserve the labeled-count qualifier in the abstract, theorem, tables, and conclusion;
- mark N1 `UNSPECIFIED — CANNOT VALIDATE`.

**Result:** `PASS WITH CONDITIONS`.

## 36. Figures and Tables Audit

No figures are present and no decorative figures were fabricated. The numerical tables in the blueprint are sourced from captured validator outputs or directly displayed formulas. The Phase-3 independent output is now captured separately.

Before a manuscript is submitted, every numerical table should be generated from a declared script and should state whether it counts labeled codes or equivalence classes. No unsupported table, histogram, or source-derived theorem table should be added.

**Result:** `PASS WITH CONDITIONS`.

## 37. Critical Problems Found

### HIGH — initial repository provenance mismatch, resolved

At audit start, the prompt's Phase-2 commit `5e4ea83` was not present in the shallow local checkout and Phase-2 artifacts were untracked. Fetching the fixed remote branch revealed the claimed history; the final merge commit `4ec522b` has `5e4ea83` as its remote-history parent and `96752c7` as the Phase-3 artifact parent. The discrepancy is preserved in this record and is resolved for the pushed branch.

### HIGH — source convention mismatch requires explicit warning

The accessible source preprint literally displays a candidate-first dual definition, while the present framework freezes a code-first definition. Its displayed inverse-Frobenius formula cannot be cited as if the conventions were identical. Correction: retain the self-contained proof and add an explicit literature convention warning.

### HIGH — N1 is not reconstructable

The q=16/n=15/32768 row lacks enough parameters to execute. Correction: mark `UNSPECIFIED — CANNOT VALIDATE`; do not invent a test.

### MEDIUM — involution terminology and LCD terminology

The Phase-2 mathematics is correct, but the manuscript should explicitly state that the principal reciprocal squares to `rho^2`, and that “LCD” means `k`-Galois LCD in the enumerator section.

### No critical mathematical counterexample found

The hostile audit found no false hull-support formula, duplicate-code overcount, dimension mismatch, transfer error, orbit-polynomial error, or moment error under the stated hypotheses.

## 38. Required Corrections

The following corrections are applied after the adversarial checks:

1. Add `H10`: the global Frobenius and inner product act componentwise with fixed primitive-idempotent labels.
2. State `gcd(n,q)=1` as equivalent to the existing `gcd(n,p)=1` condition.
3. Add the exact reciprocal identities
   `(#_rho)^2=rho^2` and `#_sigma=#_rho^{-1}`.
4. Clarify that fixed factors are `tau`-fixed, not automatically ordinary self-reciprocal.
5. Use `k`-Galois LCD terminology in the main enumerator/moment section.
6. Add the source-preprint candidate-first convention warning and do not import its theorem as proof.
7. Mark N1 `UNSPECIFIED — CANNOT VALIDATE`.
8. Add this Phase-3 audit, the independent checker, its output, and the Phase-3 validation-report section.
9. Rebuild and independently extract/compare the ZIP; the exact archive hash, clean-extraction comparison, and extracted-suite result are recorded in `validation/phase3_package_verification.out`.

No mathematical convention was changed.

## 39. Remaining Risks

- N1 remains unvalidated until its complete specification is supplied.
- Exact theorem-level comparison with the final published source and all literature records remains open.
- The initial shallow checkout lacked the historical Phase-2 objects; the final fetched-and-merged branch now preserves and verifies the claimed Phase-2 lineage.
- Repeated-root affine/constacyclic cases remain outside the theorem.
- Incompatible twists need a separate two-modulus theory.
- Labeled enumeration is not inequivalent-code enumeration.
- Quantum distance and quantum parameter claims require independent construction theorems.
- A final manuscript must reproduce the conditional proofs rather than cite the finite validators.

## 40. Phase-3 Verdict

| Item | Status | Evidence | Required Action |
|---|---|---|---|
| Theorems 1–19 under explicit hypotheses | **PASS WITH CONDITIONS** | Independent derivation audit and Phase-2 proof audit | Preserve all hypotheses in the manuscript |
| Hull-support orientation | **PASS WITH CONDITIONS** | Direct lcm/support derivation; forward/inverse adversarial comparison; independent checker | Keep the forward formula and label orientation |
| Boundary, orbit polynomial, transfer, trace | **PASS WITH CONDITIONS** | Proofs plus independent finite checker | Retain labeled-sequence interpretation |
| Global enumerator and duplicate-code count | **PASS WITH CONDITIONS** | Unique divisor/idempotent proof and F4 × F4 check | Do not quotient by equivalence |
| Dimension/counting consistency | **PASS WITH CONDITIONS** | Rank and exhaustive finite cross-checks | State component/global dimension conversion |
| N1 | **VERIFY** | Only q=16, n=15, 32768 is recoverable | Supply a complete specification before validation |
| Literature theorem transfer | **VERIFY** | Accessible source convention mismatch and incomplete full-text comparisons | Reconcile slots/exponents and verify exact theorems |
| Novelty claim | **VERIFY** | Related finite-field and affine hull literature | Use only the conservative positioning statement |
| Scope restrictions | **PASS WITH CONDITIONS** | Assumption and edge-case audit | State square-free/simple-root/compatible/labeled scope |
| Independent computational cross-check | **PASS WITH CONDITIONS** | New checker exit 0; complete output captured | Treat as finite evidence only |
| Quantum applications | **FUTURE WORK** | Blueprint's own conditional limitation | Do not claim parameters or distance |
| Burnside/Pólya equivalence counting | **FUTURE WORK** | No group action/fixed-code proof | Keep outside the main theorem |
| Repository provenance and package lineage | **PASS WITH CONDITIONS** | Remote Phase-2 history fetched and merged; final branch is `4ec522b` | Preserve the initial discrepancy record and merged history |
| Manuscript-level readiness | **VERIFY** | N1 and literature/source gaps remain; repository provenance is resolved | Complete those audits before submission |

**Final Phase-3 verdict: `VERIFY — MATERIAL AUDIT GAPS REMAIN`.**

The conditional mathematical chain survives the adversarial audit, and no critical mathematical counterexample was found. The verdict remains `VERIFY`, not `PASS WITH CONDITIONS`, because N1 is not reconstructable, the source convention requires explicit reconciliation, and exact literature verification remains incomplete. The initial repository discrepancy was resolved by fetching and merging the claimed Phase-2 history.
