# Phase-7 Novelty Boundary

**Audit date:** 2026-09-24
**Scope:** exact labeled-code enumeration of `k`-Galois hull dimensions for simple-root constacyclic components of a square-free affine algebra.
**Decision:** no priority, “first,” “new,” or state-of-the-art claim is authorized by this audit.

## 1. Status vocabulary

Novelty statuses are restricted to:

`KNOWN`, `STANDARD TOOL`, `ADAPTED`, `COMBINATION`, `EXTENSION`, `POTENTIALLY DISTINCT`, `NOT ESTABLISHED`, and `FUTURE WORK`.

The status describes the most conservative boundary supported by the checked records. `POTENTIALLY DISTINCT` is not a priority claim. `NOT ESTABLISHED` means that the audit did not establish either exact prior identity or a defensible priority boundary.

## 2. Clause-by-clause boundary

| ID | Present-work clause | Boundary classification | Why this is the safe classification | Manuscript treatment |
|---|---|---|---|---|
| NB-01 | Square-free finite affine algebra decomposes into labeled finite-field components and primitive idempotents. | `STANDARD TOOL` | This is the CRT/reduced finite-algebra framework used by the checked primary source and standard algebra. | State hypotheses and prove the decomposition needed here; do not present it as a new idea. |
| NB-02 | A simple-root constacyclic component code is a binary selection of irreducible factors. | `STANDARD TOOL` | Principal-ideal and unique-factorization facts are standard in the square-free quotient. | Reprove the exact component statement and distinguish labeled codes from equivalence classes. |
| NB-03 | The second-slot pairing `sum c_i sigma(x_i)` is translated to the code-first dual using `rho=sigma^{-1}`. | `EXTENSION` | The present code-first statement and its explicit relation to the checked candidate-first source are derived independently. | State as a separate convention proposition; retain both duals and the formula `D_candidate=sigma^2(D_code-first)`. |
| NB-04 | Candidate-first and code-first duals are not identified; their hull subspaces and factor supports may differ. | `EXTENSION` | The distinction and semilinear conjugacy are not a synonym for equality. The Gram argument proves only same-code hull-dimension/LCD invariance. | Make the limitation explicit in preliminaries, theorem statements, and conclusion. |
| NB-05 | The inverse-Frobenius reciprocal, root action, and compatible factor permutation are used on extension components with exponent `d_s=e m_s`. | `ADAPTED` | Reciprocal/root and constacyclic tools are known, but the component exponent and frozen convention are specialized to this framework. | Prove all hypotheses, including the compatibility condition. |
| NB-06 | The hull support is the weighted cyclic `1 -> 0` boundary statistic on factor-selection words. | `COMBINATION` | It combines factor-support duality, lcm intersection, factor permutation, and component weights. The checked literature records narrower settings. | Claim only the proved conditional result, not an externally established priority. |
| NB-07 | The trace transfer matrix `T_w(u,z)` enumerates code and hull dimensions jointly on each factor orbit. | `POTENTIALLY DISTINCT` | The audit found related fixed-hull, average, and ring-specific results, but no checked exact theorem identical to the labeled bivariate product. Exact prior overlap remains open. | Use cautious wording: “we derive/prove”; do not say “first” or “novel.” |
| NB-08 | The product over components and factor orbits gives the global labeled `u,z` enumerator. | `NOT ESTABLISHED` | The present proof is self-contained, but the external literature comparison is not exhaustive at final/corrected theorem level. | Treat as a present-work theorem under stated hypotheses, while leaving external priority unresolved. |
| NB-09 | Total count, exact hull distribution, LCD count, mean, and variance follow as specializations/corollaries. | `COMBINATION` | These are consequences of the transfer product and cyclic-boundary moments, not independent claims of literature priority. | Present as proved corollaries and finite checks. |
| NB-10 | The exceptional two-cycle variance is handled separately from the `a/16` formula. | `ADAPTED` | This is a boundary-case correction within the present orbit calculation. | Include the proof and a sanity check; do not use “new correction” language. |
| NB-11 | Compatible nontrivial twists are included; incompatible twists are excluded from the same-factor-set transfer theorem. | `ADAPTED` | The twist condition is forced by the root action; the diagnostic is not a general incompatible-twist enumerator. | State the exclusion prominently in the theorem scope and limitations. |
| NB-12 | Component dimensions are converted to `F_q` weights `w_O=m_s d_O`. | `ADAPTED` | The weighted global product is specific to the labeled extension-component assembly. | Define weights before the transfer matrix and test only fully specified instances. |
| NB-13 | Burnside/Pólya enumeration of equivalence classes. | `FUTURE WORK` | No group action, stabilizer calculation, or quotient count is established in the frozen theorem chain. | Keep outside the central theorem and do not call labeled counts equivalence-class counts. |
| NB-14 | Repeated-root affine or constacyclic enumeration. | `FUTURE WORK` | The main proof assumes `gcd(n,p)=1` and square-free/simple-root factors. | Exclude from title-level scope and conclusion claims. |
| NB-15 | Unconditional quantum-code parameters, distance, optimality, or journal outcomes. | `FUTURE WORK` | Hull dimension alone does not provide a quantum distance or a complete Gray-map/construction verification. | Keep quantum discussion conditional or omit it from the central manuscript. |
| NB-16 | N1-specific numerical validation. | `NOT ESTABLISHED` | Only `q=16`, `n=15`, and `2^15=32768` are known; `k`, twist, factorization, orbit data, and expected output are unspecified. | Exclude N1 from all manuscript evidence; retain only in the internal validation audit. |
| NB-17 | A claim that the whole contribution is first or unique. | `NOT ESTABLISHED` | The source search is not an exhaustive priority search and final/corrected theorem transfer is unresolved. | Prohibited. Use the safe positioning statement below. |

## 3. Safe manuscript positioning

The manuscript may say, in substance:

> “Under explicit square-free, simple-root, compatible-twist, and labeled-component hypotheses, we derive an exact joint enumerator for code dimension and code-first `k`-Galois hull dimension by combining the factor-orbit boundary description with a cyclic transfer-matrix calculation. The literature audit records related hull-dimension, fixed-dimension, average-dimension, and affine-algebra results, but does not establish an exact prior theorem identical to the present weighted bivariate product. We therefore make no priority claim.”

It must not say “first,” “new,” “novel,” “best,” “complete classification of all codes” without the labeled qualifier, or “the literature has not considered” unless a new exhaustive search supports that sentence.

## 4. Boundary conclusion

The mathematical package is a conditional, self-contained extension/combination of known tools with a **potentially distinct** bivariate factor-orbit transfer formulation. The exact novelty boundary is **NOT ESTABLISHED**. This is a deliberate publication-safety conclusion, not a negative mathematical result.
