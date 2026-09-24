# Phase-9 Manuscript Section Architecture

**Audit date:** 2026-09-24
**Base commit:** `2be1c505c4d79741bc5378bc20de0cd2d17b05e8`
**Status:** proposed architecture only; no final manuscript source is created.

## Front matter before Section 1

### Default title

**Exact Joint Enumeration of `k`-Galois Hull Dimensions for Labeled Constacyclic Codes over Square-Free Affine Algebras**

This title states the proved mathematical object, keeps the labeled-count qualification visible, and does not claim priority. The complete five-title audit is in `PHASE9_MANUSCRIPT_ARCHITECTURE_AUDIT.md`.

### Structured abstract specification

The abstract must contain, in this order:

1. **Background/problem:** hull dimensions and Galois hulls are important coding-theoretic quantities; exact distributions in the present setting require a careful component and convention treatment.
2. **Setting:** a fixed labeled square-free affine algebra decomposed into finite-field components, simple-root constacyclic moduli, and a fixed code-first `k`-Galois pairing.
3. **Construction:** factor selections, inverse-Frobenius reciprocal, compatible factor permutation, hull-support boundary, and orbit weights.
4. **Main result:** the exact bivariate polynomial `E(u,z)` for code dimension and code-first hull dimension.
5. **Transfer representation:** the two-state matrix `T_w(u,z)` and cyclic trace.
6. **Consequences:** total labeled-code count, hull distribution, LCD count, mean, and variance, including the two-cycle exception.
7. **Conditions:** square-free, simple-root, compatible-twist, fixed-component, equal-degree-within-orbit, and labeled-selection hypotheses.
8. **Conservative contribution:** “We derive a self-contained exact joint labeled enumerator under the stated hypotheses; no priority claim is made.”

The abstract must exclude N1, unsupported examples, quantum distances, Burnside/Pólya, repeated roots, incompatible transfer, and unsupported priority language.

### Keywords

`k-Galois hulls`; `constacyclic codes`; `square-free affine algebras`; `exact labeled enumeration`; `generating polynomials`; `transfer matrices`; `finite-field decomposition`.

Do not use “quantum error correction” as a keyword unless a separately verified quantum theorem is added in a later phase.

---

## 1. Introduction

- **Purpose:** motivate hulls and Galois hulls, position the problem against checked literature, state the exact question, list bounded contributions, and preview the paper.
- **Required definitions:** informal hull and `k`-Galois hull; labeled factor-selection language; no detailed proof notation before Section 2.
- **Required equations:** a short displayed code-first pairing; the central `E(u,z)` only as a preview; no unexplained reciprocal formula.
- **Required lemmas/propositions:** none; cite later results by proposed numbers only after the numbering is fixed.
- **Required theorem:** a prose statement of Theorem 8.1, not its proof.
- **Required proofs:** none.
- **Required examples:** none; do not use N1 or an incompletely specified numerical example.
- **Required figures:** optional Figure 1 workflow.
- **Required tables:** Table 2 literature comparison; a compact contribution/status table may be included.
- **Dependencies:** audited literature records R1–R9 and the contribution boundary; no later mathematical result is assumed for definitions.
- **Literature citations needed:** R1/R2 for the closest affine record and convention warning; R5 for checked finite-field cyclic/negacyclic enumeration; Talbi, Z4, double-cyclic/circulant and AIMS records for scoped adjacent results; transfer-matrix reference for standard machinery. Use exact statuses from the reference audit.
- **Claims that must not appear:** “first,” “novel,” “only,” “state of the art,” “no prior work,” unconditional quantum claims, or a claim that the literature gap is universal.

## 2. Algebraic and Coding-Theoretic Preliminaries

- **Purpose:** establish the single notation and assumption block used by every later theorem.
- **Required definitions:** `q=p^e`, `K_s=F_(q^(m_s))`, `d_s=e m_s`, affine algebra `A`, component labels, `n`, `lambda_s`, `M_s`, `mathcal F_s`, `J_s`, generator/check polynomials, component/global dimensions, `sigma`, `rho`, both dual conventions, and hull notation.
- **Required equations:** `rho=sigma^(-1)`; code-first pairing; code-first dual; candidate-first dual; compatibility condition; the ordinary Euclidean comparison identities.
- **Required lemmas/propositions:** finite-field automorphism facts and simple-root criterion may be stated as preliminary lemmas; the full convention transformation is reserved for Section 4.
- **Required theorem:** none beyond the definitions; avoid hiding the main theorem here.
- **Required proofs:** prove or cite only elementary field/semilinearity facts needed immediately.
- **Required examples:** none; use symbolic notation.
- **Required figures:** Figure 2 may be introduced after the CRT definition.
- **Required tables:** Table 1 notation and assumptions.
- **Dependencies:** `MANUSCRIPT_ASSUMPTIONS.md` and `MANUSCRIPT_NOTATION_AUDIT.md`.
- **Literature citations needed:** R1/R2 for source terminology only; standard algebraic coding references may be added later only after direct verification.
- **Claims that must not appear:** arbitrary finite-ring coverage, repeated-root coverage, a claim that `R` is the main symbol, or an identification of the two duals.

## 3. Square-Free Affine Decomposition and Factor-Selection Codes

- **Purpose:** prove the labeled CRT decomposition and establish the exact finite selection space.
- **Required definitions:** factorization of each affine relation, CRT idempotents, component quotient, `M_s`, `mathcal F_s`, `J_s`, `g_(J_s)`, `h_(J_s)`, and global code `C(J)`.
- **Required equations:** `A ~= product_s K_s`; `M_s=product_(f in mathcal F_s) f`; `g_(J_s)=product_(f in J_s)f`; component and global dimension formulas; total selection count.
- **Required lemmas/propositions:** Proposition 3.1 (affine decomposition); Lemma 3.2 (factor-selection/ideal bijection and component constacyclic decomposition).
- **Required theorem:** Result 2 may be stated as the factor-selection classification lemma; no hull theorem yet.
- **Required proofs:** CRT decomposition, simple-root principal-ideal classification, uniqueness/injectivity of labeled selections, and dimension conversion from `K_s` to `F_q`.
- **Required examples:** no numerical factorization unless already specified in a validator capture; a symbolic one-component example is sufficient.
- **Required figures:** Figure 2.
- **Required tables:** Table 1; Table 3 theorem map may list the two results.
- **Dependencies:** Section 2 and the square-free/simple-root assumptions.
- **Literature citations needed:** R1/R2 for affine component context; R5 or standard cyclic factor literature for adjacent factor methods, without attributing the present theorem.
- **Claims that must not appear:** equivalence-class enumeration, repeated-root ideal classification, or “new CRT decomposition.”

## 4. `k`-Galois Duality for Component Constacyclic Codes

- **Purpose:** derive the frozen code-first dual, inverse-Frobenius reciprocal, root action, factor permutation, dual generator, and compatibility condition; reconcile the candidate-first source convention in a separate branch.
- **Required definitions:** normalized reciprocal `f^(#_(s,k))`, code-first and candidate-first duals, `D_code-first`, `D_candidate`, and component dual twists.
- **Required equations:** `sigma(a)=a^(p^k)`; `rho(a)=a^(p^(d_s-k))`; pairing `sum_i x_i y_i^(p^k)`; `D_candidate=sigma^2(D_code-first)`; root map `alpha -> alpha^(-p^(d_s-k))`; compatibility `lambda_s^(1+p^(d_s-k))=1`; code-first dual twist `lambda_s^(-p^(d_s-k))`.
- **Required lemmas/propositions:** Lemma 4.3 reciprocal properties; Lemma 4.4 root action; Proposition 4.5 factor permutation; Theorem 4.6 dual generator; Proposition 4.7 compatibility; separate Proposition 4.CF convention transformation; separate Proposition 4.G Gram hull-dimension/LCD invariance.
- **Required theorem:** Theorem 4.6 is the component dual-generator result; the convention and Gram propositions are explicitly separate.
- **Required proofs:** apply `rho` to defining equations; prove normalized reciprocal monicity/multiplicativity/irreducibility preservation; derive root action and twist; prove lcm-compatible dual generator; prove convention transformation and Gram result independently.
- **Required examples:** one symbolic non-involutory orbit explanation; finite F8/F16 cases belong in Section 10.
- **Required figures:** none mandatory; Figure 3 may preview the induced orbit only after Section 5.
- **Required tables:** Table 3 may show branch separation.
- **Dependencies:** Sections 2 and 3.
- **Literature citations needed:** R2 for the accessible source convention; R1/R5/R7 only for scoped background; cite R4 with R3 if the finite-field record is mentioned.
- **Claims that must not appear:** literal transfer of the source reciprocal under the wrong slot, dual-code equality, hull-subspace equality, or compatibility-free same-factor-set enumeration.

## 5. Hull Support and Orbit Structure

- **Purpose:** turn the dual generator into the exact lcm/intersection support and then into the cyclic boundary statistic.
- **Required definitions:** `tau_(s,k)`, `mathcal O_s`, `a_O`, `d_O`, `w_O`, `epsilon_i`, `b_O`, and `H_k(C)`.
- **Required equations:** `tau(J_s)\J_s`; lcm/intersection support; `b_O=sum epsilon_i(1-epsilon_(i+1))`; `H_k(C)` dimension as `sum w_O b_O`.
- **Required lemmas/propositions:** Theorem 5.1 hull support; Proposition 5.2 boundary statistic and equal-degree orbit weighting.
- **Required theorem:** Result 9 is the lcm support theorem; Result 10 is the boundary proposition.
- **Required proofs:** lcm support, set identity, degree preservation, one `1-to-0` edge per one-run, paired transitions, and exclusion of unequal within-orbit weights.
- **Required examples:** symbolic orbit words of lengths 1–4; no unverified field factorization.
- **Required figures:** Figure 3.
- **Required tables:** optional symbolic orbit table in Section 6 rather than a numerical data table.
- **Dependencies:** Section 4’s factor permutation and dual generator.
- **Literature citations needed:** R1/R5/R7 for adjacent lcm/hull context; combinatorics reference for standard run/transition language.
- **Claims that must not appear:** the statistic itself is new, candidate-first and code-first supports are equal, or unequal weights within one orbit are harmless.

## 6. Exact Orbit Enumeration

- **Purpose:** derive the local polynomial independently of the matrix representation and establish coefficient integrity.
- **Required definitions:** indexed cyclic binary words, constant/nonconstant words, number of one-runs, `P_(a,w)(z)`.
- **Required equations:** `b_O`; `P_(a,w)(z)=2+sum 2 binom(a,2r)z^(rw)` and equivalent `(a/r)binom(a-1,2r-1)` form; values for `a=1,...,5`.
- **Required lemmas/propositions:** Proposition 6.1 orbit polynomial.
- **Required theorem:** no external theorem; the local result is a direct combinatorial proposition.
- **Required proofs:** choose the `2r` transition edges, explain the two starting-bit assignments, show the factor-of-two, prove integrality, and verify `P_(a,w)(1)=2^a`.
- **Required examples:** the symbolic `a=1,...,5` table only.
- **Required figures:** none mandatory.
- **Required tables:** optional small-orbit symbolic table.
- **Dependencies:** Proposition 5.2.
- **Literature citations needed:** standard cyclic-word/transfer reference only if used; the derivation is self-contained.
- **Claims that must not appear:** a new combinatorial invariant or an unverified numerical histogram.

## 7. Transfer-Matrix Representation

- **Purpose:** give the finite-state representation of the same local orbit sum and prove the trace identity.
- **Required definitions:** states `0,1`, source/destination convention, `T_w(u,z)`.
- **Required equations:** `T_w(u,z)=[[u^w,1],[u^w z^w,1]]`; entry formula `T_(r,t)=u^(w(1-t))z^(w r(1-t))`; trace expansion.
- **Required lemmas/propositions:** Proposition 7.2 matrix derivation; Theorem 7.3 closed-walk trace.
- **Required theorem:** trace counts indexed cyclic selections exactly once.
- **Required proofs:** derive all four entries, multiply edge weights, close the cycle, and distinguish indexed labeled words from necklaces.
- **Required examples:** symbolic `a=2` or `a=3` expansion; use no unsupported computed coefficients.
- **Required figures:** Figure 4.
- **Required tables:** none mandatory.
- **Dependencies:** Sections 5 and 6.
- **Literature citations needed:** transfer-matrix reference as standard combinatorial machinery; no hull theorem is imported from it.
- **Claims that must not appear:** the transfer matrix or trace is itself novel, or that it counts equivalence classes.

## 8. Global Joint Generating Polynomial

- **Purpose:** multiply independent orbit sums and state the single central theorem.
- **Required definitions:** `K(C)` and `H_k(C)` as global dimensions; `E(u,z)`; coefficient notation.
- **Required equations:** the sum over labeled selections; the product of orbit traces; `[u^K z^H]E`; `E(u,1)` and `E(1,1)` checks.
- **Required lemmas/propositions:** independence/product lemma may be stated immediately before the central theorem.
- **Required theorem:** Theorem 8.1, the exact global labeled joint enumerator.
- **Required proofs:** separate algebraic reduction, local orbit enumeration, transfer trace, and global multiplicativity; do not use later corollaries.
- **Required examples:** no new numerical example; point to Section 10 for fully specified checks.
- **Required figures:** Figure 5.
- **Required tables:** Table 3 theorem map.
- **Dependencies:** Sections 3, 5, 6, and 7.
- **Literature citations needed:** literature comparison is background only; no source is cited as proof of the complete product.
- **Claims that must not appear:** unrestricted ring coverage, repeated-root coverage, incompatible-twist coverage, quotient enumeration, or a priority claim.

## 9. Consequences

- **Purpose:** derive all requested specializations from Theorem 8.1 without presenting them as independent discoveries.
- **Required definitions:** uniform distribution on the finite labeled selection space; `K` and `H` coefficient exponents.
- **Required equations:** `E(1,1)=2^(sum_s |mathcal F_s|)`; `[z^H]E(1,z)`; LCD count `2^(sum_s |mathcal O_s|)`; `E[H_k]=sum_(O:a_O>=2) a_O w_O/4`; and `Var(H_k)=sum_(O:a_O=2)w_O^2/4+sum_(O:a_O>=3)a_Ow_O^2/16`.
- **Required lemmas/propositions:** Corollaries 9.1–9.5; an indicator lemma for a single orbit may precede the moments.
- **Required theorem:** no new central theorem; every result must be labeled a corollary or calculation from `E`.
- **Required proofs:** specialize `E`, use zero-boundary constant words for LCD, and compute indicator expectations/covariances separately for orbit lengths 1, 2, and at least 3.
- **Required examples:** symbolic orbit formulas only; numerical outputs belong to Section 10.
- **Required figures:** none mandatory.
- **Required tables:** Table 3 may list the corollary dependencies.
- **Dependencies:** Theorem 8.1 and Proposition 5.2.
- **Literature citations needed:** adjacent average/LCD records may be cited as context, not as sources of the present formulas.
- **Claims that must not appear:** that the corollaries establish priority, that `a/16` applies to `a=2`, or that hull dimension gives a quantum distance.

## 10. Computational Validation and Reproducibility

- **Purpose:** distinguish theorem proof, independent validation, and diagnostics.
- **Required definitions:** “finite computational validation” and “diagnostic only.”
- **Required equations:** no new equations beyond checks of `E`, support, Gram rank, and reciprocal action.
- **Required lemmas/propositions:** none; computations do not replace proofs.
- **Required theorem:** none.
- **Required proofs:** none; explain the independent routes and their scope.
- **Required examples:** F4 pilot; F8 long orbit; F16 extension component; compatible nontrivial twist; N2-A; N2-B incompatible diagnostic. Each row must give all parameters and capture path.
- **Required figures:** none mandatory.
- **Required tables:** Table 4.
- **Dependencies:** all mathematical sections; scripts and captures in `code/` and `validation/`.
- **Literature citations needed:** none for the computations; cite the source-PDF audit only if discussing source comparison.
- **Claims that must not appear:** N1, general proof by computation, fabricated factorization/histogram, unsupported quantum parameters, or an “all cases” claim beyond the listed tests.

## 11. Limitations and Extensions

- **Purpose:** make every boundary explicit and prevent readers from extending the theorem beyond its hypotheses.
- **Required definitions:** repeated-root, incompatible-twist, labeled versus equivalence-class enumeration, Burnside/Pólya, and conditional quantum application.
- **Required equations:** optionally display the incompatible dual twist `lambda_s^(-p^(d_s-k))`; no unsupported extension formula.
- **Required lemmas/propositions:** none; future work is not a proved result.
- **Required theorem:** none.
- **Required proofs:** none.
- **Required examples:** none; N1 is explicitly excluded.
- **Required figures:** none.
- **Required tables:** Table 5 scope and exclusions.
- **Dependencies:** assumptions, literature audit, and claim matrix.
- **Literature citations needed:** R1/R2/R3/R4 and Phase-8 comparison for source-access limitations; quantum records only as conditional background.
- **Claims that must not appear:** that excluded cases are impossible, that the primary source is the only prior work, or that a hull dimension determines a quantum distance.

## 12. Conclusion

- **Purpose:** restate the conditional mathematical result, the labeled-count interpretation, the convention distinction, finite-validation scope, and remaining literature limitations.
- **Required definitions:** no new definitions.
- **Required equations:** central `E(u,z)` and `D_candidate=sigma^2(D_code-first)` may be repeated for clarity.
- **Required lemmas/propositions:** none.
- **Required theorem:** refer to Theorem 8.1 and Corollaries 9.1–9.5.
- **Required proofs:** none; summarize dependencies rather than reprove.
- **Required examples:** no new example.
- **Required figures:** none.
- **Required tables:** none mandatory.
- **Dependencies:** all previous sections.
- **Literature citations needed:** no new citation; preserve the conservative source boundary.
- **Claims that must not appear:** submission readiness, priority, final journal outcome, unconditional quantum result, or coverage of excluded cases.

## 13. References

- **Purpose:** list only sources whose bibliographic identity and use are supported by `FINAL_REFERENCE_AUDIT.md`.
- **Required definitions:** none.
- **Required equations:** none.
- **Required lemmas/propositions/theorems:** none.
- **Required proofs:** none.
- **Required examples:** none.
- **Required figures:** none.
- **Required tables:** an optional reference-status appendix, not a substitute for citations.
- **Dependencies:** final reference audit and literature claim ledger.
- **Literature citations needed:** R1–R14 according to their recorded statuses; include R4 correction whenever R3 is cited; do not use R10/R12/R13 as theorem evidence without fresh checking.
- **Claims that must not appear:** guessed DOI, unverified theorem number, publisher outcome, unsupported priority, or a reference presented as proof when only an abstract/record was checked.

## Proof-writing order within the draft

1. State assumptions and notation.
2. Prove decomposition and factor selection.
3. Define and reconcile dual conventions separately.
4. Derive reciprocal, root action, factor permutation, and dual generator.
5. Prove hull support and boundary statistic.
6. Count one orbit directly.
7. Derive transfer matrix and trace.
8. State and prove the global enumerator.
9. Derive all corollaries.
10. Present finite validation, limitations, and literature boundary.

This order is the writing implementation of the acyclic graph in `THEOREM_DEPENDENCY_GRAPH.md`.
