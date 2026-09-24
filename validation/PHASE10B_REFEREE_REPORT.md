# PHASE 10B — Adversarial Mathematical Manuscript Audit

**Audit date:** 2026-09-24
**Repository:** `arunyadav0307-stack/Galios-Hull`
**Branch:** `arena/01a0c9d2-galios-hull`
**Audited HEAD:** `bd99ee6a486e104b3034ddeac9db05fb09d18155`
**Mandatory base:** `bd99ee6a486e104b3034ddeac9db05fb09d18155`
**Previous phase:** Phase 10A — full manuscript drafting
**Phase-10A verdict:** Complete first draft — ready for manuscript audit

**Phase-10B verdict:** **C. MATERIAL THEOREM/PROOF ERROR REQUIRES REPAIR**

The component algebra, code-first duality, reciprocal action, hull-support orientation, orbit polynomial, transfer matrix, and corollaries pass the independent checks below. However, the central global theorem is not self-contained as written: the manuscript never defines the global code-first pairing/hull on the affine product algebra or proves the direct-product dual/hull decomposition that its global dimension formula uses. The enumerator is mathematically plausible under the natural missing bridge, but the central theorem is not currently proved in the manuscript's stated global setting.

No manuscript or bibliography content was modified during Phase 10B. Only this referee report is added.

## 1. Executive Summary

### Positive findings

- The frozen code-first convention is used consistently in the displayed component formulas.
- The relation
  `D_candidate(C)=sigma_k^2(D_code-first(C))`
  is stated separately and is not replaced by a subspace-equality claim.
- The inverse-Frobenius reciprocal and root action are algebraically consistent.
- The compatibility condition is used for same-factor-set closure, not for the incompatible diagnostic cases.
- The hull-support orientation is `tau(J_s)\setminus J_s`, equivalently the forward `1`-to-`0` boundary, and matches exhaustive binary checks.
- The orbit polynomial and transfer matrix agree for orbit lengths 1 through 8 and several weights.
- The `a=2` variance exception is correct.
- Citation keys, bibliography entries, labels, internal references, braces, and LaTeX environments pass static checks.
- The narrow literature and contribution boundaries are preserved; no firstness or priority claim is made.

### Material finding

**M1 — MAJOR:** The manuscript proves component statements but uses a global hull dimension in Theorem 8.1 without defining the global pairing or proving that the global dual and hull decompose componentwise. This is a central proof bridge, not merely a notation preference.

### Final recommendation

The manuscript should not advance to final polishing until M1 is repaired and the localized proof/citation issues below are addressed. The minimum repair does not require redesigning the enumerator, but it does require an explicit global definition and a direct-product lemma.

## 2. Manuscript Scope

The complete `manuscript/main.tex` was read from the document preamble through the generated bibliography command, together with all 13 bibliography records in `manuscript/references.bib`. The draft contains 12 primary sections, six Section-9 subsections, five figure placeholders, four data tables, one labeled central theorem, six formal corollaries, and separate convention/Gram propositions.

The frozen Phase-9 documents were cross-checked, including the section architecture, theorem dependency graph, assumptions, notation audit, claim matrix, contribution boundary, central-result comparison, novelty boundary, literature ledger, transfer matrix, reviewer objections, and Phase-10A audit. Earlier validation captures and audit files were preserved.

At the beginning of this audit, the shallow local checkout was at an older commit with the Phase-10A files untracked, while the remote branch resolved to the mandatory base. The remote base was fetched and the local branch was reset to `bd99ee6a486e104b3034ddeac9db05fb09d18155`. Every pre-existing Phase-10A file was byte-identical to the remote-base tree, no content was lost, and the resulting worktree was clean before the audit.

## 3. Mathematical Correctness

The central component-level mathematics is correct under the hypotheses stated in Sections 2–5. The global theorem has a missing definition/proof bridge described in M1.

No counterexample was found for the reciprocal, root action, compatibility criterion, component hull support, orbit polynomial, transfer matrix, total count, LCD count, mean, or variance. This conclusion is conditional on repairing the global product pairing/hull definition.

### Proof-completeness table

The severity column uses the requested proof-audit scale: `LOW`, `MEDIUM`, `HIGH`, and `MATERIAL`.

| Result | Hypotheses | Proof present? | Proof validity | Dependencies | Missing step or limitation | Severity |
|---|---|---:|---|---|---|---|
| Code-first dual translation | Finite-field-linear `C\subseteq K_s^n`; component Frobenius | Yes | Valid | Pairing definition | None at component level | LOW |
| Square-free affine decomposition | Monic square-free positive-degree relations over `F_q` | Yes | Essentially valid | Section 2 presentation | The finite-etale tensor-product step and idempotents are stated tersely | LOW |
| Factor-selection parametrization | `gcd(n,p)=1`, `lambda_s\ne0`, simple-root factorization | Yes | Valid componentwise | Square-free quotient | The global product code `C(J)` is not explicitly defined under CRT | MEDIUM; contributes to M1 |
| Normalized inverse-Frobenius reciprocal | Monic `f`, `f_0\ne0`, finite-field automorphism | Yes | Valid | Code-first translation | Irreducibility preservation and the inverse construction are asserted rather than fully expanded | MEDIUM |
| Root action | `f(alpha)=0`; nonzero constant term | Yes | Valid | Reciprocal lemma | `alpha\ne0` is implicit from `f_0\ne0` | LOW |
| Compatible factor permutation | `lambda_s^(1+p^(d_s-k))=1` | Yes | Valid | Root action and reciprocal invertibility | None material; non-involutory cycles are explicitly allowed | LOW |
| Ordinary constacyclic reciprocal | `M=x^n-a`, `a\ne0`, monic `G\mid M` | Yes | Correct but compressed | Standard Euclidean dual calculation | Boundary-shift orthogonality for the `a^{-1}` twist needs a fuller proof or verified citation | MEDIUM |
| Code-first dual generator | Simple-root component code and code-first pairing | Yes | Valid if ordinary lemma is accepted | Translation, reciprocal, ordinary reciprocal | The proof should explicitly say that `rho(C)` has generator `rho(g)` and check polynomial `rho(h)` | MEDIUM |
| Same-twist compatibility criterion | Component dual twist `lambda_s^{-p^(d_s-k)}` | Yes | Valid | Dual-generator theorem | None | LOW |
| Candidate-first/code-first transformation | Finite-field-linear code; no constacyclic hypothesis | Yes | Valid | Code-first translation | Global componentwise version is not stated | LOW at component level |
| Gram hull/LCD invariance | Finite-field-linear code with row basis `B` | Yes | Valid | Rank-nullity | Clarify that right and left nullities are taken over `K_s` | LOW |
| Component hull support | Compatible same-factor-set component | Yes | Valid | Dual generator and lcm/intersection | `supp` is not formally defined as surviving CRT components | MEDIUM |
| Weighted cyclic boundary statistic | Equal degree along a reciprocal orbit | Yes | Valid | Component support and orbit degree preservation | Global use again depends on the missing product-hull bridge | MEDIUM |
| Cyclic run interpretation | Indexed cyclic binary word | Yes | Valid | Boundary formula | None | LOW |
| One-orbit polynomial | Indexed cyclic binary words of length `a` | Yes | Valid | Boundary statistic | The displayed examples stop at `a=5`; independent checks extend to `a=8` | LOW |
| Weighted transfer matrix | State `0` unselected, state `1` selected; destination weighting | Yes | Valid | Boundary statistic | None | LOW |
| Local trace identity | Indexed closed walks; fixed orbit positions | Yes | Valid | Transfer matrix | None; trace counts indexed words, not necklaces | LOW |
| Theorem 8.1 global enumerator | All component assumptions, compatibility, equal orbit degree, labeled selections | Yes, but incomplete | Component product is valid; global conclusion is not self-contained | Component theorem, trace identity, CRT | Define the global pairing/hull and prove direct-product dual/hull decomposition | MATERIAL — M1 |
| Total labeled-code count | Theorem 8.1 and injective selections | Yes | Valid conditional on M1 | Global product | Downstream of M1 | MEDIUM |
| Code-dimension distribution | Factor-selection dimension formula | Yes | Valid | Theorem 8.1 | Downstream of M1 | MEDIUM |
| Hull-dimension distribution | Theorem 8.1 and local traces | Yes | Valid conditional on M1 | Global product | Downstream of M1 | MEDIUM |
| LCD count | Positive weights; zero boundary iff constant word | Yes | Valid conditional on M1 | Hull support | Downstream of M1 | MEDIUM |
| Mean hull dimension | Uniform labeled selections; independent orbit bits | Yes | Valid conditional on M1 | Global product | Downstream of M1 | MEDIUM |
| Variance, including `a=2` | Uniform selections; distinguish lengths 1, 2, and at least 3 | Yes | Valid conditional on M1 | Boundary indicators | Downstream of M1 | MEDIUM |

## 4. Convention Audit

The manuscript consistently states

- `sigma_{s,k}(a)=a^(p^k)`;
- `rho_{s,k}(a)=a^(p^(d_s-k))=sigma_{s,k}^{-1}`;
- `d_s=e m_s`;
- `<x,y>_{s,k}=sum_i x_i y_i^(p^k)` with the code in the first slot and the candidate in the second slot.

The suppressed-index forms `sigma(a)=a^(p^k)`, `rho(a)=a^(p^(d_s-k))`, and `<x,y>_k=sum_i x_i y_i^(p^k)` are also present. A complete search found no accidental replacement of `rho` by `sigma` in the reciprocal or dual-generator formulas.

The candidate-first relation is stated as

`D_candidate(C)=sigma_k^2(D_code-first(C))`.

The manuscript explicitly says that the two dual subspaces, hull subspaces, factor supports, and generators are not thereby equal. The Gram proposition separately establishes same-code hull-dimension and LCD invariance. **Convention verdict: PASS at the component level.**

## 5. Algebraic Results

### 5.1 Square-free decomposition

The stated presentation by separate square-free univariate relations is a finite-etale `F_q`-algebra. The claimed decomposition into a product of finite fields is correct. The proof is terse about the tensor-product decomposition and does not display CRT idempotents, but no algebraic counterexample was found.

### 5.2 Factor selections and injectivity

For a simple-root quotient, the CRT product-of-fields description gives one ideal for every subset of irreducible factors. If `J\ne J'`, at least one factor component is zero for one principal ideal and the full field for the other, so the ideals differ. The dimension formula

`dim_{K_s} C_s(J_s)=n-sum_{f in J_s} deg(f)`

is correct. The component injectivity argument is valid.

The missing point is that the manuscript calls the global object `C(J)` without writing the CRT definition

`C(J)=prod_s C_s(J_s)`

or defining the corresponding global pairing and hull. This omission is the material global bridge M1.

### 5.3 Hidden hypotheses

The component results correctly use `lambda_s\in K_s^*`, `gcd(n,p)=1`, simple roots, finite-field linearity, compatibility for same-factor-set closure, and equal factor degree within each orbit. No repeated-root or unrestricted-ring implication was found.

## 6. Hull-Support Audit

For a component generator support `J_s`, the dual generator support is `tau_{s,k}(mathcal F_s\setminus J_s)`. In a square-free product of fields, the intersection ideal is generated by the lcm, so its surviving CRT components are

`(mathcal F_s\setminus J_s) intersection tau_{s,k}(J_s)`

which equals `tau_{s,k}(J_s)\setminus J_s` under the permutation hypothesis. If `tau(f_i)=f_{i+1}` and `epsilon_i=1` denotes selection, a surviving factor at position `i+1` occurs exactly for `epsilon_i=1` and `epsilon_{i+1}=0`. Thus the orientation is the forward `1`-to-`0` statistic, not the inverse orientation.

Independent exhaustive orientation checks for every binary word with orbit lengths `a=1,...,8` passed. The component support theorem is mathematically correct. The manuscript should define “factor support” explicitly to distinguish surviving CRT components from generator-factor support.

## 7. Combinatorial Enumeration Audit

The independent brute-force test enumerated all binary cyclic words for `a=1,...,8` and weights `w=1,2,3,5`. In every case it matched

`P_(a,w)(z)=2+sum_(r=1)^(floor(a/2)) 2 binom(a,2r) z^(rw)`

and the equivalent

`2+sum_(r=1)^(floor(a/2)) (a/r) binom(a-1,2r-1) z^(rw)`.

The transition count is even, the two constant words are included, and indexed cyclic words are counted without quotienting rotations. The tests also checked the `a=1` and `a=2` boundary cases and verified that hull dimension never exceeded code dimension for all tested words.

**Orbit-polynomial verdict: PASS.**

## 8. Transfer-Matrix Audit

With source state `r=epsilon_i` and destination state `t=epsilon_(i+1)`, the four entries are:

- `(0,0)`: `u^w`;
- `(0,1)`: `1`;
- `(1,0)`: `u^w z^w`;
- `(1,1)`: `1`.

The destination weighting counts each factor exactly once, and the `1`-to-`0` transition receives the hull weight. The trace closes the indexed cycle with no rotational quotient.

Independent transfer expansion matched direct enumeration for `a=1,...,8`, all tested weights, and several multi-orbit products. **Transfer-matrix verdict: PASS.**

## 9. Global Enumerator Audit

At the component/orbit level, selections are independent and the product of local traces is exactly the correct generating function. Factor-selection injectivity prevents duplicate labeled codes, and no indexed selection is omitted.

The coefficient interpretation is therefore correct **after** the missing global bridge is supplied. As written, `H_k(C(J))` in Theorem 8.1 is not defined for the global code `C(J)`, and the proof does not establish that its dimension equals the sum of the component hull dimensions. **Global-enumerator verdict: CONDITIONAL; REPAIR REQUIRED (M1).**

## 10. Corollary Audit

Conditional on a corrected global direct-product pairing/hull lemma:

- `E(1,1)=2^(sum_s |mathcal F_s|)` is correct;
- `E(u,1)` gives the code-dimension distribution with unselected-factor weight `u^w`;
- `E(1,z)` gives the hull-dimension distribution;
- the LCD count is `2^(sum_s |mathcal O_s|)`;
- the mean is `sum_{a_O>=2} a_O w_O/4`;
- the variance has the separate `a_O=2` term `w_O^2/4` and the `a_O>=3` term `a_O w_O^2/16`.

No downstream corollary was independently contradicted. The corollaries inherit M1 because their global code/hull interpretation currently relies on Theorem 8.1.

## 11. Computational Validation

### Existing repository suite

The complete Phase-1 through Phase-10A validator suite was rerun with the clean-environment command used by the repository:

- exit code: `0`;
- stderr lines: `0`;
- output lines: `460`.

The F4, F8, F16, compatible-twist, N2-A, and N2-B diagnostics passed within their stated scopes. The convention and end-to-end captures report zero relation, reciprocal, support, transfer, Gram, and LCD failures in the tested cases.

### Independent Phase-10B checks

A separate brute-force implementation, not imported from the repository validators, checked:

- orbit polynomial and transfer expansion for `a=1,...,8` and weights `1,2,3,5`;
- direct versus product global enumerators for six multi-orbit systems;
- total counts for those systems;
- `tau(J)\setminus J` orientation for every binary word with `a=1,...,8`;
- `H\leq K` for all tested words.

Results:

- exit code: `0`;
- stderr lines: `0`;
- output lines: `23`;
- final line: `ALL_INDEPENDENT_SMALL_ORBIT_CHECKS_PASS`.

These computations validate the finite combinatorial layer; they do not repair the missing global pairing definition.

## 12. Literature Audit

The bibliography uses the source records and permitted scopes in the Phase-7/8 audits. The following source-to-claim table records the actual manuscript use.

| Bib key(s) | Manuscript claim | Source status in repository audit | Referee assessment |
|---|---|---|---|
| `debnathAffinePreprint`, `debnathAffine2026` | Closest affine-algebra structural record; component decomposition and Galois-hull context | Accessible theorem-bearing preprint plus publisher metadata; final text not fully accessible | Safe for structural context and convention warning; not imported as the central product theorem |
| `debnathConstacyclic2023`, `debnathCorrection2023` | Finite-field constacyclic Galois-hull formulas and restricted counts | Partially verified record plus verified correction metadata | Wording is appropriately restricted; no unverified theorem number is used |
| `sangwisut2015` | Cyclic/negacyclic hull formulas and fixed-dimension counts | Verified publisher-level scope and theorem-bearing record | Relevant narrower background; no affine transfer claimed |
| `talbi2021` | Cyclic serial finite-chain-ring enumeration | Readable theorem-bearing preprint; chain-ring hypotheses differ | Safe adjacent comparison; no transfer to reduced affine products |
| `jitmanZ4`, `pathakZ4` | Cyclic `Z4` hull enumeration | Verified metadata/scope in the reference audit | Safe narrower background |
| `zhang2026` | Restricted non-chain/direct-product component hull formulas | Open full-text record checked in Phase 8 | Used only as adjacent structural comparison; quantum title is not used for an unconditional claim |
| `gao2023` | Double cyclic prescribed-hull counts | Publisher-level theorem/abstract scope checked | Safe generalized-cyclic comparison only |
| `aliabadi2026` | Double/four circulant small-hull enumeration context | Open article and prescribed-hull scope checked | Safe different-family comparison |
| `debnathAverage2025` | Average-dimension Galois-hull context | Publisher metadata/abstract scope | Used only as neighboring average background |
| `debnathSmall2026` | Small-dimension Galois-hull context | Publisher metadata/abstract scope | Used only as neighboring background |

No cited source is used to support the central global product as an imported theorem. No theorem number, DOI, or publisher text is fabricated in the manuscript.

## 13. Citation Audit

Static citation checks report:

- bibliography entries: `13`;
- distinct citation keys in `main.tex`: `13`;
- missing bibliography entries: `0`;
- uncited bibliography entries: `0`;
- duplicate bibliography keys: `0`.

The bibliographic identities match the Phase-7 final reference audit at the stated level of verification. The main text does not cite a source theorem number. The standard transfer-matrix assertion is mathematically routine, but the architecture documents anticipated a transfer-matrix background citation and the bibliography contains none. This is a localized citation/presentation issue, not a central mathematical error.

## 14. Notation Audit

The manuscript uses `A`/`\mathcal A`, `K_s`, and `\mathcal F_s` consistently and avoids ambiguous bare `F_s` in the mathematical prose. It distinguishes `K_s` from coefficient exponents `K,H`, and it separates `H_k(C)` from the exponent `H`.

The following notation needs repair or clarification:

1. `C(J)` is used globally without an explicit CRT definition.
2. `\Hull_k(C)` is defined only for component `C\subseteq K_s^n`, then used for the global product code.
3. `operatorname{supp}` is used for surviving factor components without a formal definition distinguishing it from generator-factor support.
4. The manuscript uses four data tables, whereas the frozen Phase-9 table plan proposed a theorem-dependency table and a five-table numbering plan. The mathematical dependency chain is present in prose/theorem order, but the planned table architecture is not reproduced exactly.

## 15. Overclaim Audit

The following priority/marketing terms were searched in `main.tex`: `first-ever`, `unprecedented`, `state-of-the-art`, `novel`, `best`, `optimal`, and `superior`. None occurs.

Occurrences of “first” are limited to `code-first`, `candidate-first`, slot/proof-order language, or the ordinary phrase “first line.” The occurrence of “unique” is the mathematical phrase “unique factorization.” “Only” is used as a scope qualifier such as “background only” or “diagnostic only.” These are not priority claims.

The manuscript explicitly says that no priority claim is made and does not claim quantum distance, QECC performance, equivalence-class enumeration, or journal acceptance. **Overclaim verdict: PASS.**

## 16. N1 Audit

The entire manuscript and bibliography were searched. N1 occurs only in the limitations/validation-exclusion discussion in `main.tex`; it does not occur in `references.bib`.

No N1 numerical case, factorization, twist, orbit histogram, or experimental result is presented. The manuscript preserves the exact status:

`UNSPECIFIED — CANNOT VALIDATE`

The known N1 metadata recovered by the repository diagnostic is not used as a manuscript example or proof input. **N1 verdict: PASS.**

## 17. Major Issues

### M1 — MAJOR: Missing global pairing/hull decomposition

**Exact locations:** Sections 2–3, lines 116–129 and 225–258; Section 5, lines 456–462; Theorem 8.1, lines 573–601.

**Problem:** The manuscript defines `\langle x,y\rangle_{s,k}` and `\Hull_k(C)` only for a component code in `K_s^n`. It later refers to a global `C(J)` and `\dim_{\F_q}\Hull_k(C)` but never defines:

- the global code `C(J)` under the CRT identification;
- the global tuple twist `lambda=(lambda_s)`;
- the componentwise Frobenius on `A`;
- the global code-first pairing on `A^n`;
- the global dual and global hull;
- the lemma that the global dual/hull is the direct product of the component duals/hulls.

The proof of Theorem 8.1 says that “both dimensions are additive,” but this is the exact bridge that must be proved. Without it, the global hull dimension appearing in the coefficient interpretation is undefined or ambiguous, and the central theorem is not self-contained.

**Impact:** The component orbit product may be correct, but the stated theorem about codes over the affine product algebra is not established as written. All global corollaries inherit the gap.

**Minimum repair:** Add a global definition and a direct-product lemma before Theorem 8.1. For example, under `A\cong\prod_sK_s`, define `lambda=(lambda_s)`, `C(J)=\prod_s C_s(J_s)`, the componentwise map `sigma_A`, and an explicitly chosen global pairing (A-valued componentwise pairing or a stated Fq-valued trace pairing). Prove which pairing is intended and prove

`D_{A,code-first}(C(J))=\prod_sD_{s,code-first}(C_s(J_s))`

and

`Hull_{A,k}(C(J))=\prod_s Hull_{s,k}(C_s(J_s))`.

Then the weighted `F_q` dimension sum used in Theorem 8.1 follows.

This repair must be made and re-audited before a final-polishing verdict.

## 18. Minor Issues

### m1 — MEDIUM proof exposition: ordinary reciprocal lemma

The ordinary constacyclic reciprocal lemma is correct in the stated setting, but its proof compresses the boundary-shift calculation into one sentence. It should either give the coefficient calculation for the `a^{-1}` constacyclic shift or cite a directly verified standard result without importing an unverified theorem number.

### m2 — MEDIUM proof exposition: normalized reciprocal

The manuscript asserts irreducibility preservation and invertibility of the normalized inverse-Frobenius reciprocal. These are correct finite-field facts, but the inverse formula and the reduction to the ordinary reciprocal should be displayed or proved in one additional paragraph.

### m3 — EDITORIAL notation: factor support

Define `operatorname{supp}` as the set of CRT factor components surviving in the ideal. Otherwise a reader may interpret it as the set of factors in the generator, reversing the lcm argument.

### m4 — EDITORIAL citation: transfer-matrix background

The claim that the transfer matrix and closed-walk trace are standard is reasonable, but the Phase-9 architecture anticipated a checked transfer-matrix reference. Add a verified general reference or phrase the statement as an elementary identity proved in Section 7 without literature attribution.

### m5 — EDITORIAL architecture: table plan

The frozen Phase-9 table plan proposed a dependency-map table and five table slots, while the Phase-10A draft uses Table 3 for computation and Table 4 for scope. This does not invalidate the mathematics, but the report should either reconcile the plan or state that the four-table Phase-10A requirement supersedes it.

### m6 — EDITORIAL global notation

The manuscript should state whether the global pairing is A-valued componentwise or reduced to an `F_q`-valued trace pairing. These choices can have different annihilator interpretations unless the intended identification is made explicit.

## 19. Required Revisions

### Required before final polishing

1. Repair M1 by defining the global affine-algebra code, global Frobenius/pairing, global dual, and global hull.
2. Prove the direct-product dual/hull decomposition and the `F_q` dimension-weight additivity.
3. Recheck Theorem 8.1 and every global corollary after that repair.
4. Expand or properly source the ordinary constacyclic reciprocal lemma.
5. Expand the normalized reciprocal inverse/irreducibility argument.
6. Define factor support precisely.
7. Resolve the transfer-matrix citation choice and the Phase-9 table-plan discrepancy.
8. Run a LaTeX-enabled compilation after repair; current static checks do not replace compilation.
9. Rerun all Phase-1 through Phase-10B checks and rebuild the archive after manuscript repair.

### Changes deliberately not made in Phase 10B

No automatic edits were applied to `manuscript/main.tex` or `manuscript/references.bib`. In particular, the central theorem, duality formulas, support orientation, orbit polynomial, transfer matrix, and variance formula were not silently changed.

## 20. Final Verdict

**C. MATERIAL THEOREM/PROOF ERROR REQUIRES REPAIR**

The verdict is driven by M1: the global hull object and the direct-product bridge used by Theorem 8.1 are missing from the manuscript. The component mathematics and independent finite checks are strong, and no counterexample was found to the intended enumerator after the natural global completion. Nevertheless, a journal referee cannot mark the actual manuscript mathematically verified while its central global quantity is undefined and its additivity is asserted rather than proved.
