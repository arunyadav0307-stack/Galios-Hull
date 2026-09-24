# Phase-9 Reviewer-Style Adversarial Audit

**Audit date:** 2026-09-24
**Status:** architecture objections only; the manuscript is not rewritten here.

The reviewers below are deliberately adversarial. Each objection is paired with the required architectural revision, not with an unsupported answer.

## Reviewer A — Algebraic coding theory

### A1. The ambient algebra and code family may be underspecified

- **Likely objection:** the reader cannot tell whether `A`, a generic ring `R`, or a component quotient is the code alphabet.
- **Mathematical vulnerability:** mixing the affine algebra with `K_s[x]/<x^n-lambda_s>` could invalidate dimension statements.
- **Missing definition:** fixed labeled CRT decomposition and the distinction between component code and global product code.
- **Missing proof:** factor-selection injectivity and the global `F_q` dimension weight.
- **Unclear notation:** bare `F_s` and `R` can be mistaken for a factor set and ambient ring.
- **Literature concern:** an adjacent non-chain ring result must not be presented as the same algebra.
- **Required revision:** use `A`, `K_s`, and `mathcal F_s` consistently; state Proposition 3.1 and Lemma 3.2 before any code enumeration; include Table 1.

### A2. The semilinear convention may be hidden in reciprocal notation

- **Likely objection:** a displayed reciprocal could be read as an ordinary or candidate-first reciprocal.
- **Mathematical vulnerability:** the exponent `p^k` versus `p^(d_s-k)` changes the dual twist and root action.
- **Missing definition:** code-first second-slot pairing, `sigma`, `rho`, and normalized reciprocal in one location.
- **Missing proof:** applying `rho` to the defining equations before invoking the ordinary reciprocal lemma.
- **Unclear notation:** `k` could be read as a field exponent rather than a Frobenius iteration.
- **Literature concern:** the primary accessible source uses the opposite dual slot.
- **Required revision:** make Proposition 4.CF a separate boxed proposition and retain the exact relation `D_candidate=sigma^2(D_code-first)`.

### A3. The compatibility condition may be over-applied

- **Likely objection:** the paper may state a same-factor-set result while silently including incompatible twists.
- **Mathematical vulnerability:** the reciprocal maps `x^n-lambda_s` to a different modulus when compatibility fails.
- **Missing definition:** same-factor-set compatibility versus a two-modulus diagnostic.
- **Missing proof:** root-image calculation and equivalence of the compatibility condition.
- **Unclear notation:** candidate-first and code-first twists may be conflated.
- **Literature concern:** source formulas use source-specific twist conventions.
- **Required revision:** state compatibility in Assumptions 19–20, Theorem 4.7, and the limitations section; keep N2-B diagnostic only.

### A4. The hull support may be mistaken for a subspace equality

- **Likely objection:** `tau(J)\J` could be read as identifying hulls under both pairings.
- **Mathematical vulnerability:** candidate-first/code-first hull subspaces need not coincide for a fixed code.
- **Missing definition:** dual code versus hull subspace versus factor support.
- **Missing proof:** lcm/intersection support under the code-first convention.
- **Unclear notation:** `H` as a dimension and `H_k(C)` as a subspace.
- **Literature concern:** an adjacent paper’s code-first-looking formula cannot erase the distinction.
- **Required revision:** use `H_k(C)` for the code-first hull and `H` only as coefficient exponent; add the Gram branch separately.

### A5. Ring extensions may be claimed beyond the proof

- **Likely objection:** the square-free proof does not cover repeated roots or nilpotent chain-ring layers.
- **Mathematical vulnerability:** binary factor support fails when multiplicities matter.
- **Missing definition:** `gcd(n,p)=1` and simple-root use.
- **Missing proof:** none; this is an exclusion.
- **Unclear notation:** `A` could be mistaken for an arbitrary finite ring.
- **Literature concern:** chain-ring and non-chain records are adjacent, not transferable.
- **Required revision:** Table 5 must list repeated roots and unrestricted rings as outside scope.

## Reviewer B — Combinatorics and enumeration

### B1. The cyclic word convention may be ambiguous

- **Likely objection:** it is unclear whether `epsilon_i=1` means selected or unselected and which boundary is counted.
- **Mathematical vulnerability:** reversing the orientation changes factor support labels.
- **Missing definition:** cyclic indexing, selection convention, and `b_O`.
- **Missing proof:** one `1->0` edge per one-run and paired transition count.
- **Unclear notation:** `a_O` and `w_O` could be confused with word length and scalar weight.
- **Required revision:** introduce the convention before the orbit polynomial and mark the `1->0` orientation in Figure 3.

### B2. The orbit-polynomial coefficient needs a transparent derivation

- **Likely objection:** `a/b binom(a-1,2b-1)` appears without explaining integrality or the factor of two.
- **Mathematical vulnerability:** a missing factor would corrupt every distribution.
- **Missing definition:** constant versus nonconstant cyclic words and the `2b` transition edges.
- **Missing proof:** show `2 binom(a,2b)=(a/b) binom(a-1,2b-1)`.
- **Unclear notation:** `b` is both a summation index and visually close to `b_O`.
- **Required revision:** use `r` for the number of one-runs in the proof, retain `b_O` for the statistic, and include the symbolic `a=1,...,5` check.

### B3. The transfer matrix may count codimension instead of dimension

- **Likely objection:** a selected generator factor normally contributes to codimension.
- **Mathematical vulnerability:** the stated `u` variable could be reversed.
- **Missing definition:** destination-state weighting and the meaning of `epsilon=1`.
- **Missing proof:** expand the product of matrix entries to obtain `u^(sum w(1-epsilon_i))`.
- **Required revision:** Section 7 must derive all four entries and explicitly state that `u` records code dimension, not codimension.

### B4. The trace may overcount cyclic words

- **Likely objection:** traces can count a word once per choice of starting position if the object is an unindexed necklace.
- **Mathematical vulnerability:** the theorem counts labeled factor selections, so an orbit position is indexed even when the word has rotational symmetry.
- **Missing definition:** labeled orbit positions versus quotient necklaces.
- **Missing proof:** expand `(T^a)_(r,r)` and sum over the two initial states; do not quotient by rotation.
- **Required revision:** state explicitly that `trace(T^a)` counts indexed cyclic selections once and that Burnside/Pólya is excluded.

### B5. Independence and multiplication need proof-level separation

- **Likely objection:** the product over orbits could hide a dependence through the dual.
- **Mathematical vulnerability:** if hull support coupled distinct orbits, the product would fail.
- **Missing proof:** `tau` preserves each orbit and the support statistic is an orbit sum.
- **Required revision:** place the local orbit theorem before the global product theorem and include the factor-selection Cartesian-product argument.

### B6. Moments require the short-cycle exception

- **Likely objection:** applying `a/16` to `a=2` is false.
- **Mathematical vulnerability:** adjacent boundary indicators are mutually exclusive for a 2-cycle.
- **Required revision:** state length 1, length 2, and length at least 3 separately in Corollary 9.5 and Table 3.

## Reviewer C — Galois and finite-field coding theory

### C1. The source-convention comparison needs exact slot language

- **Likely objection:** the manuscript cites a source with a different dual definition as though it proves the present theorem.
- **Mathematical vulnerability:** candidate-first and code-first duals differ by `sigma^2` and can have different factor supports.
- **Missing definition:** two dual equations side by side.
- **Literature concern:** final publisher/corrected theorem text remains incomplete.
- **Required revision:** cite R1/R2 separately, state `DIRECT AFTER CONVENTION TRANSFORMATION`, and forbid literal source transfer.

### C2. The role of `k<e` versus `k<d_s` needs explanation

- **Likely objection:** a component field has degree `d_s=e m_s`, but the parameter is restricted by the base field.
- **Mathematical vulnerability:** readers may infer a missing range of component automorphisms.
- **Required revision:** state that the paper fixes a base-field `k` with `0<=k<e` and applies it componentwise; `rho` uses the inverse exponent modulo `d_s`. Any broader componentwise range is outside the frozen family.

### C3. Hull-dimension invariance is not support invariance

- **Likely objection:** the Gram result might be overstated.
- **Mathematical vulnerability:** same-code dimensions agree, but hull subspaces and factor supports need not.
- **Required revision:** keep Proposition 4.G separate from Theorems 4.6–5.1 and repeat the limitation in the conclusion.

### C4. The literature comparison may be too broad

- **Likely objection:** an abstract or publisher snippet is used as theorem-level evidence.
- **Literature concern:** R3/R4, R6, R8, R9, and metadata-only records have limited access.
- **Required revision:** use the reference audit’s allowed status vocabulary and cite only the checked scope; do not import formulas from restricted records.

### C5. The quantum motivation may overtake the classical result

- **Likely objection:** a hull enumerator is presented as a quantum-code construction or distance result.
- **Mathematical vulnerability:** no independent quantum distance theorem is part of the frozen chain.
- **Required revision:** keep quantum material to conditional motivation or omit it; no quantum keyword is used by default.

## Cross-reviewer revision checklist

- [ ] Use `A`, `K_s`, and `mathcal F_s` consistently.
- [ ] Put all hypotheses in Section 2 and link every theorem to them.
- [ ] State the two dual conventions and the `sigma^2` transformation in a separate proposition.
- [ ] Derive the `1->0` support and the orbit polynomial before the transfer matrix.
- [ ] Explain destination weighting in `T_w`.
- [ ] State indexed labeled counting and exclude necklaces/equivalence classes.
- [ ] Preserve the `a=2` variance exception.
- [ ] Cite literature by checked scope and preserve source-unavailable warnings.
- [ ] Exclude N1, repeated roots, incompatible transfer, Burnside/Pólya, and unconditional quantum claims.

No reviewer objection requires a mathematical repair under the frozen hypotheses. The objections require explicit exposition, notation, citation, and scope guardrails before drafting.
