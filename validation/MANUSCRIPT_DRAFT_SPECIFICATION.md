# Manuscript Draft Specification — Phase 7

**Working title:** *Exact Enumeration of `k`-Galois Hull Dimensions of Constacyclic Codes over Square-Free Affine Algebras*
**Audit date:** 2026-09-24
**Source workflow:** Markdown specification only. No genuine `.tex` or `.bib` source exists in the audited checkout, and none is fabricated here.
**Manuscript-readiness verdict:** `NOT READY — MATERIAL GAPS REMAIN`

This document is the publication-facing specification to be used if a manuscript source is later prepared. It separates imported background, self-contained proofs, finite computations, and future work. It is not a claim that the manuscript is ready for submission.

## 1. Non-negotiable manuscript rules

1. Use the frozen code-first convention throughout the main theorem:
   \[
   \langle c,x\rangle_{s,k}=\sum_i c_i x_i^{p^k},\qquad
   \sigma_{s,k}(a)=a^{p^k},\qquad
   \rho_{s,k}(a)=a^{p^{e m_s-k}}.
   \]
2. Define the dual by `\langle c,x\rangle_{s,k}=0` with the codeword in the first slot and the candidate in the second slot.
3. Keep the candidate-first comparison separate. State
   \[
   D_{\mathrm{candidate}}(C)=\sigma_{s,k}^{2}(D_{\mathrm{code-first}}(C))
   \]
   under the finite-field hypotheses, and do not identify the two dual codes, hull subspaces, factor supports, or dual-generator supports.
4. Use `rho` in the principal reciprocal, root action, compatibility condition, dual generator, and compatible predicted twist.
5. Call the product a labeled-code enumerator. It is not a Burnside/Pólya quotient enumeration.
6. Use only fully specified reproducible examples. Every displayed computational count must identify the field, component, `n`, `k`, twist, factorization/orbit data, selection range, command, and captured output.
7. Keep repeated-root cases, incompatible same-factor-set transfer, equivalence classes, unconditional quantum claims, quantum distances, and journal outcomes outside the central theorem.
8. Do not claim “first,” “novel,” “unique,” “best,” or “state of the art.” The exact novelty boundary remains `NOT ESTABLISHED`.
9. Cite a source theorem number only after the cited version and number have been directly checked. The final publisher record and the readable preprint are separate citations.

## 2. Abstract — approved conservative draft

> We study the exact distribution of `k`-Galois hull dimensions of labeled `lambda`-constacyclic codes over a square-free affine algebra. The square-free hypothesis decomposes the algebra into finite-field components, and the simple-root hypothesis identifies each component code with a binary selection of irreducible factors of a constacyclic polynomial. With the code-first second-slot pairing
> \[
> \langle c,x\rangle_{s,k}=\sum_i c_i x_i^{p^k}
> \]
> and inverse Frobenius `rho_{s,k}(a)=a^{p^{e m_s-k}}`, we derive the normalized reciprocal, factor permutation, and hull-support statistic. Under explicit compatibility, component, and labeled-factor hypotheses, a cyclic transfer-matrix calculation gives the bivariate enumerator
> \[
> \mathscr E(u,z)=\prod_s\prod_O\operatorname{tr}\bigl(T_{w_O}(u,z)^{a_O}\bigr),
> \qquad
> T_w(u,z)=\begin{pmatrix}u^w&1\\u^wz^w&1\end{pmatrix},
> \]
> where `u` records `F_q`-code dimension and `z` records `F_q`-hull dimension. Specializations give the labeled-code count, hull distribution, LCD count, mean, and variance, including the two-cycle boundary case. We also prove the relation between the candidate-first literature convention and the code-first convention without identifying their dual or hull subspaces. Fully specified exhaustive computations over selected small fields validate the stated finite instances; they do not replace the general proofs. Related literature is audited conservatively, and no priority claim is made.

The abstract must not include a source theorem number, an unverified numerical example, a quantum distance, an equivalence-class count, an unsupported complexity bound, or a priority statement.

## 3. Introduction specification

### 3.1 Motivation

Introduce hulls as intersections of a code with a dual and explain their relevance to code equivalence/automorphism computations and to conditional entanglement-assisted constructions. Use R5 and R7 from `validation/FINAL_REFERENCE_AUDIT.md` only for the scope actually checked.

### 3.2 Audited literature position

The introduction must distinguish four layers:

- **Established background:** finite-field hull definitions, cyclic/negacyclic factor methods, square-free CRT, and general Galois-hull matrix methods.
- **Checked related results:** finite-field constacyclic hull formulas/counts (R3/R4), cyclic and negacyclic hull enumerations (R5), Hermitian averages (R6), Galois-hull invariance context (R7), affine-algebra hull scope (R1/R2), and ring-specific averages or Hermitian results (R8/R9).
- **Present derivations:** the code-first inverse-Frobenius convention, component support, weighted orbit boundary, transfer matrix, joint enumerator, and corollaries.
- **Future work:** quotient enumeration, repeated roots, incompatible twists, and independently verified quantum constructions.

Use the following safe gap statement:

> “The checked records contain structural, fixed-hull-dimension, average-dimension, and affine-algebra results. This manuscript focuses on a self-contained exact joint enumeration for labeled factor selections under a fixed code-first convention. The audit did not establish an exact prior theorem identical to the weighted bivariate product, so no priority claim is made.”

### 3.3 Contribution list

The contribution list may contain only:

1. a precisely defined code-first convention and an explicit candidate-first comparison;
2. a proof of the inverse-Frobenius factor action under the stated compatibility condition;
3. a component hull-support characterization;
4. a weighted cyclic-boundary formula;
5. a bivariate transfer-matrix product for labeled code/hull dimensions;
6. exact distribution, LCD, mean, and variance corollaries;
7. reproducible validation for fully specified finite instances.

Each item must be labeled as a theorem, corollary, or computational validation. Do not call the list “new contributions” in the absence of a completed priority audit.

## 4. Preliminaries and fixed notation

Define:

- `q=p^e`, the base field `F_q`, and labeled components `K_s=F_{q^{m_s}}=F_{p^{d_s}}` with `d_s=e m_s`;
- the square-free affine algebra and its CRT/idempotent decomposition;
- `n>=1`, `gcd(n,p)=1`, and nonzero component twists `lambda_s`;
- the simple-root quotient `K_s[x]/<x^n-lambda_s>`;
- monic irreducible factor sets `F_s`, selected subsets `J_s`, generator `g_{J_s}`, check polynomial `h_{J_s}`, and the component/global dimension convention;
- orbit weights `w_O=m_s deg(f)` when the factor orbit has common factor degree;
- `sigma`, `rho`, the principal normalized reciprocal, and the two dual definitions.

The compatibility condition for the main same-factor-set theorem is

\[
\lambda_s^{1+p^{d_s-k}}=1.
\]

The candidate-first family comparison has its corresponding `p^k` condition. The two conditions must not be silently conflated.

## 5. Theorem architecture

The paper retains the 19-result architecture below. The first 19 items are the main conditional chain; the candidate-first/code-first transformation and Gram invariance are separate propositions, not replacements for items 3–9.

| No. | Manuscript result | Required statement |
|---:|---|---|
| 1 | Affine decomposition | The reduced square-free affine algebra is a product of labeled finite fields with explicit idempotents. |
| 2 | Component code classification | Simple-root component constacyclic ideals correspond bijectively to factor selections. |
| 3 | Code-first pairing and dual translation | The second-slot pairing yields the code-first dual equation and the inverse-Frobenius change of variables. |
| 4 | Normalized reciprocal | Define and prove the monicity, degree, multiplicativity, irreducibility preservation, and inverse properties of the `rho` reciprocal. |
| 5 | Root action | The reciprocal sends a root by `alpha -> alpha^{-p^{d_s-k}}`. |
| 6 | Compatible factor permutation | Under the compatibility condition, the action permutes the same factor set. |
| 7 | Dual generator | The code-first dual of a selected component code is generated by the normalized reciprocal of its check polynomial with the principal dual twist. |
| 8 | Same-twist criterion | State the compatible/incompatible twist distinction and the exact predicted dual twist. |
| 9 | Hull support | The lcm/intersection formula gives the component hull support. |
| 10 | Cyclic boundary statistic | The hull dimension is the weighted `1 -> 0` boundary sum on the orbit-selection word. |
| 11 | Orbit polynomial | Derive the exact coefficient formula for a single orbit, including integrality. |
| 12 | Transfer matrix | Derive all four entries of `T_w(u,z)`. |
| 13 | Closed-walk trace | Prove that the trace of `T_w^{a}` sums cyclic selection words exactly once. |
| 14 | Global joint enumerator | Multiply component/orbit factors under the fixed labeled product model. |
| 15 | Total labeled-code count | Set `u=z=1` and recover the number of distinct labeled factor selections. |
| 16 | Hull distribution | Set `u=1` and extract every exact hull-dimension multiplicity. |
| 17 | LCD count | Characterize zero boundary and derive the product count. |
| 18 | Mean | Derive the weighted boundary expectation under the uniform labeled-selection model. |
| 19 | Variance | Derive the variance, including the exceptional two-cycle covariance case. |

### 5.1 Separate convention-transformation proposition

State and prove, for any finite-field-linear code and without constacyclic hypotheses,

\[
D_{\mathrm{code-first}}(C)=\rho(C^{\perp_E}),
\qquad
D_{\mathrm{candidate}}(C)=\sigma(C^{\perp_E}),
\qquad
D_{\mathrm{candidate}}(C)=\sigma^2(D_{\mathrm{code-first}}(C)).
\]

Then list separately the possible differences in dual code, hull subspace, support, and generator. Do not replace this proposition by a claim of equality.

### 5.2 Separate invariance proposition

With a row basis `B` and restricted Gram matrix `G=B sigma(B)^T`, prove equality of the same-code hull dimensions and LCD decisions by rank-nullity. State precisely that this does not imply equality of hull subspaces or factor supports.

## 6. Proof-dependency graph

The graph must remain acyclic and must appear in the manuscript or a supplement in equivalent form:

```text
square-free CRT and labeled components
        |
        v
simple-root factor-selection classification
        |
        v
code-first second-slot pairing
        |
        v
inverse-Frobenius reciprocal and root action
        |
        v
compatibility and factor permutation
        |
        v
component dual generator
        |
        v
lcm hull and component support
        |
        v
orbit boundary statistic
        |
        v
single-orbit polynomial
        |
        v
transfer matrix and cyclic trace
        |
        v
global joint enumerator
        |
        v
hull distribution, LCD count, mean, variance
        |
        v
finite-instance validation
```

The convention-transformation proposition branches from the pairing definition and feeds only the comparison/invariance discussion. The Gram proposition branches from the two dual definitions and does not feed the code-first support proof. Optional future-work branches (quotient enumeration and quantum construction) must not be prerequisites of the main theorem.

## 7. Literature-review writing specification

The literature review must use the reference audit's exact scope language:

- R1: publisher identity and broad affine-algebra scope are verified; full final theorem transfer is not.
- R2: readable source convention and displayed formulas are verified; the candidate-first slot and inverse-Frobenius display require explicit conversion.
- R3/R4: finite-field constacyclic formula/count scope and correction record are checked; corrected theorem hypotheses are not imported without direct reading.
- R5: cyclic/negacyclic Euclidean and Hermitian hull formulas and fixed-dimension enumerations are checked in an open publisher record; this is narrower than the affine product.
- R6/R8: average-dimension records are background, not evidence for the joint enumerator.
- R7: general Galois-hull invariance/matrix context is background, not a constacyclic product theorem.
- R9 and other ring-specific quantum records are not used to support the classical central theorem.

Never write that a source “proves the present theorem,” “misses the present theorem,” or “is the first” unless the final/corrected full text and a documented exact comparison support that sentence.

## 8. Computational-example policy

Only the following fully specified evidence may be summarized in the manuscript:

| Example | Fixed data | Allowed claim |
|---|---|---|
| F4 pilot | `q=4`, `n=5`, `lambda=1`, `k=1`, four labeled `F_4` components, all `8^4=4096` selections | Direct-inner-product dual, reciprocal, hull, and enumerator checks pass for the listed finite instance. |
| F8 long orbit | `q=8`, `n=7`, `lambda=1`, `k=1`, rho iteration `2`, factor orbit lengths `[1,6]`, all `2^7=128` selections | Long-cycle boundary and direct-generator checks pass for the listed instance. |
| F16 extension component | `K=F_16=F_{4^2}`, `n=5`, `lambda=1`, `k=1`, rho iteration `3`, orbit lengths `[1,4]`, all `2^5=32` selections | Extension-field exponent handling and principal convention agree for the listed selections. |
| Compatible nontrivial twist | `q=4`, `n=5`, `lambda=omega`, `k=1`, compatible orbit lengths `[1,2]`, all `2^3=8` selections | The compatible nontrivial-twist formulas pass for the listed component. |
| Extension convention comparison | N2-A data and all 32 selections | Direct dual agrees with the principal reciprocal; the alternative is retained only as a comparator. |
| Incompatible extension diagnostic | N2-B data, all 8 selections, both candidate twists, no transfer enumeration | Incompatibility and convention behavior are diagnosed; this does not enlarge the main theorem. |
| Global product bridge | `A=F_4 x F_{16}` over `F_4`, `n=5`, `lambda=(omega,1)`, `k=1`, component orbit data `[(1,1),(2,2)]` and `[(1,2),(4,2)]`, all `2^3*2^5=256` labeled selections | Direct global A-valued pairing/nullspace, product dual/hull, `F_4`-dimension additivity, orbit boundary, and transfer products agree for the repaired bridge. |

For every example, cite the exact script and `.out` capture. State “finite computational validation,” not “proof.” Do not include a computational item whose parameters or expected output are incomplete.

## 9. Limitations section — mandatory text items

The limitations section must state:

- the theorem is square-free and simple-root, with `gcd(n,p)=1`;
- component labels are fixed and counts are for distinct labeled factor selections;
- compatible twists are required for the same-factor-set enumerator;
- the candidate-first and code-first dual codes/supports are not generally equal;
- exact external theorem transfer remains conditional on the final/corrected source-level check;
- the exact novelty boundary is not established;
- repeated roots, incompatible two-modulus transfer, Burnside/Pólya quotient counts, and unconditional quantum claims are outside scope;
- finite validators do not replace proofs;
- no minimum distance or quantum parameter follows from a hull dimension alone;
- no result is asserted for an incompletely specified computational artifact.

## 10. Conclusion specification

The conclusion may claim that the stated conditional theorem chain yields an exact labeled joint enumerator and its corollaries, and that the listed finite checks are reproducible. It must repeat the code-first convention and the distinction between mathematical proof and computation. It must not claim priority, final journal acceptance, quantum distance, quotient enumeration, or applicability beyond the stated square-free/simple-root/compatible hypotheses.

## 11. Reference and source checklist before submission

- [ ] Replace every provisional source theorem citation with a directly checked final/corrected version or remove it.
- [ ] Include the correction record whenever R3 is cited.
- [ ] Preserve the candidate-first/code-first transformation in the main text.
- [ ] Check every DOI against the final reference audit; do not add a DOI marked `DOI UNVERIFIED`.
- [ ] Reproduce all 19 theorem dependencies and the two separate propositions.
- [ ] Re-run the listed validators in a clean environment and cite the captured output.
- [ ] Ensure all tables are labeled as labeled-code tables and all quantum claims are conditional.
- [ ] Keep the manuscript readiness verdict at `NOT READY — MATERIAL GAPS REMAIN` until the central transfer and exact novelty boundary are closed.

---

# Phase-8 manuscript amendment: verified literature boundary

**Amendment date:** 2026-09-24
**Current drafting decision:** `B. READY WITH NARROWED CONTRIBUTION CLAIMS`

The Phase-7 specification and its historical `NOT READY — MATERIAL GAPS REMAIN` verdict are preserved above. This amendment records only verified Phase-8 conclusions and does not create a full manuscript source.

## 12. Verified literature position for the revised introduction

The introduction must now say explicitly that exact hull-dimension enumeration is already known in narrower finite-field cyclic/negacyclic, restricted finite-field constacyclic, finite-chain-ring, `Z4`, double cyclic, and double/four circulant settings. It must also acknowledge adjacent componentwise hull/lcm results over restricted non-chain/direct-product rings and average/small-dimension Galois-hull studies.

The primary affine-algebra source is the closest structural record. Its readable conclusion states that enumeration of non-isometric constacyclic codes with a prescribed Galois hull dimension over that affine algebra remains an open problem. This supports the statement that the accessible primary source does not provide the present all-selection enumerator, but it must not be inflated into a universal absence or priority claim. The final publisher text and the corrected full text of the 2023 finite-field constacyclic record remain to be checked before final submission.

Use this approved wording:

> “Exact hull-dimension enumeration is available in several narrower finite-field, constacyclic, chain-ring, `Z4`, and generalized-cyclic settings. Related affine and non-chain records establish component hull formulas, averages, or small-dimension results. Under the square-free, simple-root, compatible-twist, and labeled-component hypotheses stated here, we derive a self-contained exact joint enumerator for code and code-first `k`-Galois hull dimensions. The audit did not verify an exact prior theorem identical to this weighted bivariate product; no priority claim is made.”

## 13. Revised contribution list

The contribution list must use “we derive” or “we prove,” not “new contributions.” It may contain:

1. the frozen code-first second-slot convention and the explicit candidate-first transformation;
2. the inverse-Frobenius extension-component reciprocal and compatible factor action;
3. the lcm hull-support formula and its weighted cyclic boundary expression;
4. the exact labeled bivariate code/hull enumerator for the stated square-free affine family;
5. the total count, hull distribution, LCD count, mean, and variance corollaries;
6. reproducible finite validation of the stated instances.

The transfer matrix, trace, cyclic transition statistic, CRT, reciprocal, and fixed-dimension hull-enumeration background must be described as standard or previously available ingredients. The application-specific conjunction is potentially distinct, not established as a priority result.

## 14. Required limitations added by Phase 8

The limitations section must add:

- fixed-hull enumeration already exists in multiple narrower families;
- the exact external prior-match/priority boundary is `NOT ESTABLISHED`;
- the primary final publisher text and corrected finite-field full text were not available for complete theorem-level transfer;
- `b_O` and the transfer trace are standard combinatorial tools;
- the central count is labeled, not inequivalent-code enumeration;
- N1 remains `UNSPECIFIED — CANNOT VALIDATE` and is excluded.

## 15. Current manuscript recommendation

A draft may proceed only as a conditional exact labeled-enumerator paper with the safe boundary in `validation/CONTRIBUTION_BOUNDARY.md`. It must not proceed as a priority paper or as a claim that exact hull enumeration, CRT decomposition, or transfer matrices are themselves new. Before submission, complete the final/corrected source-text checks and any journal-specific differentiation review.

---

# Phase-9 manuscript architecture amendment

**Amendment date:** 2026-09-24
**Base commit:** `2be1c505c4d79741bc5378bc20de0cd2d17b05e8`
**Phase-9 decision:** `A. MANUSCRIPT ARCHITECTURE FROZEN — READY FOR DRAFTING`

The historical Phase-7 and Phase-8 specification remains unchanged above. Phase 9 converts it into a detailed drafting architecture without creating a final manuscript source. The controlling files are:

- `validation/PHASE9_MANUSCRIPT_ARCHITECTURE_AUDIT.md` — title, abstract, contribution, Q1-logic, and decision gate;
- `validation/MANUSCRIPT_SECTION_ARCHITECTURE.md` — section-by-section writing and proof obligations;
- `validation/THEOREM_DEPENDENCY_GRAPH.md` — acyclic theorem order and proposed numbering;
- `validation/MANUSCRIPT_ASSUMPTIONS.md` — single assumption source of truth;
- `validation/MANUSCRIPT_NOTATION_AUDIT.md` — notation and first-use controls;
- `validation/MANUSCRIPT_CLAIM_MATRIX.md` — allowed and forbidden wording;
- `validation/MANUSCRIPT_FIGURE_PLAN.md` — five figure designs only;
- `validation/MANUSCRIPT_TABLE_PLAN.md` — five table designs only;
- `validation/PHASE9_REVIEWER_OBJECTIONS.md` — algebraic, combinatorial, and Galois/finite-field objections.

## Phase-9 default title and keywords

The recommended default title is:

> **Exact Joint Enumeration of `k`-Galois Hull Dimensions for Labeled Constacyclic Codes over Square-Free Affine Algebras**

Acceptable alternatives and their evaluations are recorded in `PHASE9_MANUSCRIPT_ARCHITECTURE_AUDIT.md`. The approved keywords are `k-Galois hulls`, `constacyclic codes`, `square-free affine algebras`, `exact labeled enumeration`, `generating polynomials`, `transfer matrices`, and `finite-field decomposition`.

## Phase-9 central theorem writing rule

The draft must state one central Theorem 8.1 under the consolidated square-free, simple-root, compatible-twist, fixed-component, equal-degree-within-orbit, and labeled-selection hypotheses:

```text
E(u,z)
 = sum_(J_1,...,J_N) u^(K(C(J))) z^(H_k(C(J)))
 = product_s product_(O in mathcal O_s) trace(T_(w_O)(u,z)^(a_O)),
T_w(u,z) = [[u^w, 1], [u^w z^w, 1]].
```

Here `u` records global `F_q`-code dimension, `z` records global code-first `F_q`-hull dimension, `epsilon_i=1` means a selected generator factor, and `[u^K z^H]E` counts distinct labeled factor selections with dimensions `K,H`. The theorem does not count equivalence classes, repeated-root codes, incompatible same-factor-set families, unrestricted ring codes, or quantum parameters.

The convention-transformation proposition and Gram-matrix hull/LCD invariance proposition remain separate branches. The draft must retain

```text
sigma(a)=a^(p^k),
rho(a)=a^(p^(e*m_s-k)),
D_candidate(C)=sigma_k^2(D_code-first(C)).
```

Phase 9 does not change the mathematical formulas, literature statuses, N1 exclusion, Phase-5 verdict, or Phase-8 contribution boundary. It only freezes the writing order and guardrails. This is readiness for drafting, not submission readiness.
