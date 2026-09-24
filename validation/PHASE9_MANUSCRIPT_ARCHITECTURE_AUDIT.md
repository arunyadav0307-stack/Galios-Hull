# Phase 9 Manuscript Architecture and Mathematical Writing Audit

**Audit date:** 2026-09-24
**Branch:** `arena/01a0c9d2-galios-hull`
**Mandatory base commit:** `2be1c505c4d79741bc5378bc20de0cd2d17b05e8`
**Previous decision:** Phase 8 — `B. READY WITH NARROWED CONTRIBUTION CLAIMS`
**Phase-9 scope:** architecture and mathematical writing only; no final manuscript source is created.

## 1. Starting-state verification

The required starting state was checked before Phase-9 edits:

| Check | Result |
|---|---|
| Local `HEAD` | `2be1c505c4d79741bc5378bc20de0cd2d17b05e8` |
| Branch | `arena/01a0c9d2-galios-hull` |
| Remote branch | synchronized to the same commit after an explicit branch ref fetch |
| Initial worktree | clean |
| Phase-1 evidence | preserved in original validator captures and `VALIDATION_REPORT.md`; no Phase-1 audit Markdown file exists |
| Phase-2 through Phase-8 audits | present and preserved |
| Phase-8 comparison/contribution/reference files | present and preserved |
| Historical audits | not deleted or overwritten |

The absence of a `validation/PHASE1*.md` file is recorded rather than repaired by fabrication. The Phase-1 validator outputs, later audit references, and historical report sections remain the evidence source for that phase.

## 2. Evidence reconciliation

The architecture was derived from the following records:

| Evidence layer | Architectural consequence |
|---|---|
| Phase-2 proof audit | The 19 conditional results, reciprocal orientation, orbit polynomial, transfer trace, distribution, LCD, mean, and variance are the mathematical spine. |
| Phase-3 adversarial audit | Definitions, edge cases, N1 exclusion, literature caution, and theorem-by-theorem writing safeguards are mandatory. |
| Phase-4 literature/convention audit | Candidate-first and code-first conventions require a separate explicit transformation and source qualification. |
| Phase-5 invariance audit | Same-code hull dimensions and LCD decisions may be equal without equality of dual/hull subspaces or factor supports. |
| Phase-6 consolidation | The theorem chain, assumptions, independent end-to-end evidence, and exclusions form one acyclic package. |
| Phase-7 manuscript audit | The manuscript remains a Markdown specification; no `.tex` or `.bib` source is fabricated; examples must be fully specified. |
| Phase-8 literature audit | Exact hull enumeration is known in narrower settings; transfer machinery is standard; the external priority boundary remains `NOT ESTABLISHED`. |
| Current blueprint and draft specification | The detailed theorem statements, formulas, examples, limitations, and source policy are retained and reorganized, not broadened. |

## 3. Frozen contribution statement

The following is the default manuscript contribution statement:

> Under explicit square-free, simple-root, compatible-twist, fixed-component, and labeled-factor hypotheses, we derive a self-contained exact joint generating polynomial for code dimension and code-first `k`-Galois hull dimension. The polynomial factors over factor orbits and is represented by a weighted two-state transfer matrix and cyclic trace. No priority claim is made.

The wording may be shortened for an abstract, but its mathematical scope must not be broadened. The paper may say “we derive,” “we establish,” “we obtain,” or “under the stated hypotheses.” It must not use unsupported priority language.

## 4. Title audit

The following five candidates were evaluated qualitatively against mathematical accuracy, scope accuracy, no-overclaim safety, journal suitability, searchability, and conciseness. They are not ranked.

| Candidate title | Accuracy | Scope | No overclaim | Journal suitability | Searchability | Conciseness | Reason |
|---|---|---|---|---|---|---|---|
| **Exact Joint Enumeration of `k`-Galois Hull Dimensions for Labeled Constacyclic Codes over Square-Free Affine Algebras** | Pass | Pass; labeled and square-free are explicit | Pass | Pass | Strong terms: exact, `k`-Galois hull, constacyclic, affine | Moderate | **Recommended default.** It names the central object and the most important counting qualification without a priority claim. |
| **A Transfer-Matrix Enumerator for `k`-Galois Hulls of Constacyclic Codes over Square-Free Affine Algebras** | Pass | Pass, but labeled scope moves to the abstract | Pass | Pass | Strong transfer/hull terms | Good | Acceptable alternative when the paper’s combinatorial representation is foregrounded. |
| **Labeled Code and `k`-Galois Hull Generating Polynomials for Constacyclic Codes over Square-Free Affine Algebras** | Pass | Very precise | Pass | Pass | Strong generating-polynomial terms | Moderate | Acceptable alternative emphasizing the bivariate object rather than the proof device. |
| **Factor-Orbit Enumeration of `k`-Galois Hull Dimensions in Simple-Root Constacyclic Codes** | Pass | Narrower and accurate if the affine setting is stated in the subtitle/abstract | Pass | Pass | Strong orbit and hull terms | Good | Acceptable alternative for a combinatorics-facing venue; it omits affine algebra from the title. |
| **Joint Code-Dimension and `k`-Galois Hull-Dimension Enumeration via Cyclic Transfer Matrices** | Pass | Accurate only with the square-free affine setting in the abstract | Pass | Pass | Strong dimension/transfer terms | Good | Acceptable alternative when the exact joint statistic is the main search phrase. |

The recommended default is a recommendation for clarity, not a ranking of scientific merit. No candidate contains “first,” “new,” “novel,” “unique,” “best,” or “state of the art.”

## 5. Abstract and keyword audit

The structured abstract specification is in `MANUSCRIPT_SECTION_ARCHITECTURE.md`. It includes background, setting, construction, exact enumerator, transfer trace, consequences, conditions, and conservative contribution wording. It excludes N1, unsupported numerical examples, quantum distances, Burnside/Pólya, repeated roots, incompatible transfer, and priority claims.

Approved keywords are:

1. `k-Galois hulls`
2. `constacyclic codes`
3. `square-free affine algebras`
4. `exact labeled enumeration`
5. `generating polynomials`
6. `transfer matrices`
7. `finite-field decomposition`

“Quantum error correction” is not used as a default keyword because no independent quantum theorem is part of the central package.

## 6. Complete manuscript architecture

The proposed manuscript has the required sequence:

1. Introduction
2. Algebraic and Coding-Theoretic Preliminaries
3. Square-Free Affine Decomposition and Factor-Selection Codes
4. `k`-Galois Duality for Component Constacyclic Codes
5. Hull Support and Orbit Structure
6. Exact Orbit Enumeration
7. Transfer-Matrix Representation
8. Global Joint Generating Polynomial
9. Consequences: total count, hull distribution, LCD count, mean, variance
10. Computational Validation and Reproducibility
11. Limitations and Extensions
12. Conclusion
13. References

The detailed purpose, dependencies, proof obligations, citation policy, examples, figures, tables, and prohibited claims for every section are in `MANUSCRIPT_SECTION_ARCHITECTURE.md`. No modification to this order is mathematically necessary.

## 7. Central theorem audit

The single central theorem is proposed as **Theorem 8.1 — Exact labeled joint enumerator**. Under the assumptions in `MANUSCRIPT_ASSUMPTIONS.md`, let `mathcal O_s` be the cycles of `tau_(s,k)` on `mathcal F_s`, with orbit length `a_O`, common factor degree `d_O`, and global weight `w_O=m_s d_O`. If `epsilon_i=1` means that the orbit factor is selected in the generator, define

```text
K(C) = sum_(s,O,i) w_O(1-epsilon_i)
H_k(C) = sum_(s,O,i) w_O epsilon_i(1-epsilon_(i+1))
T_w(u,z) = [[u^w, 1], [u^w z^w, 1]]
```

Then

```text
E(u,z)
 = sum_(J_1,...,J_N) u^(K(C(J))) z^(H_k(C(J)))
 = product_s product_(O in mathcal O_s) trace(T_(w_O)(u,z)^(a_O)).
```

The coefficient `[u^K z^H]E(u,z)` is the number of distinct labeled factor-selection codes with global `F_q`-code dimension `K` and global code-first `F_q`-hull dimension `H`.

The theorem explicitly does **not** count equivalence classes, repeated-root codes, incompatible twists in a same-factor-set model, unrestricted finite-ring codes, or quantum-code parameters.

## 8. Proof-architecture audit

The central proof is ordered as follows:

1. component decomposition;
2. factor-selection parametrization;
3. code-first pairing and dual translation;
4. inverse-Frobenius reciprocal;
5. root action and compatible factor permutation;
6. code-first dual generator;
7. lcm/intersection hull support;
8. cyclic boundary statistic;
9. direct local orbit polynomial;
10. transfer matrix and trace identity;
11. independent orbit multiplication;
12. global enumerator;
13. corollaries.

The algebraic proof and combinatorial proof are separate. The local orbit theorem precedes the global product theorem. The candidate-first/code-first transformation and Gram invariance are separate branches and are not used to identify support sets.

## 9. Orbit-polynomial audit

For an indexed cyclic binary word of length `a`, `epsilon_i=1` means selected. The code-first statistic is

```text
b_O(epsilon)=sum_i epsilon_i(1-epsilon_(i+1)).
```

For a nonconstant word, transitions occur in pairs: each one-run has one `1->0` exit and each zero-run has one `0->1` entry. If there are `r` one-runs, there are `2r` transition edges. Choosing the transition edges and the starting bit gives

```text
N(a,r)=2 binom(a,2r)
      =(a/r) binom(a-1,2r-1).
```

The two constant words contribute `2`, so

```text
P_(a,w)(z)=2+sum_(r=1)^(floor(a/2)) 2 binom(a,2r) z^(rw).
```

This is symbolically checked for `a=1,...,5`; no unverified numerical example is introduced.

## 10. Transfer-matrix audit

The state is the current binary selection bit. For source state `r` and destination state `t`, assign

```text
T_w(u,z)_(r,t)=u^(w(1-t)) z^(w r(1-t)).
```

Thus the matrix is

```text
T_w(u,z)=[[u^w,1],[u^w z^w,1]].
```

The destination weight counts each factor once and makes `u` the code-dimension exponent. The `1->0` transition carries the hull factor. Expanding the matrix power and summing diagonal entries closes the indexed cycle, yielding `trace(T_w^a)`. This is standard transfer/closed-walk machinery; the application-specific content is the algebraic identification of the hull support.

## 11. Global enumerator and corollary audit

The product is valid because selections are independent over the fixed labeled component factor sets and `tau` preserves each orbit. The corollaries are derived only after Theorem 8.1:

- `E(1,1)` gives the total labeled-code count `2^(sum_s |mathcal F_s|)`;
- `[z^H]E(1,z)` gives the exact hull distribution;
- the `z=0` specialization gives the LCD count `2^(sum_s |mathcal O_s|)`;
- logarithmic derivatives or independent orbit indicators give
  `E[H_k]=sum_(O:a_O>=2) a_O w_O/4`;
- the variance is
  `sum_(O:a_O=2) w_O^2/4 + sum_(O:a_O>=3) a_O w_O^2/16`.

The variance exception is mandatory; applying `a/16` to `a=2` is prohibited. Length-one orbits contribute zero to both displayed moments.

## 12. Convention and literature-writing audit

The manuscript must state, in one visible subsection:

```text
sigma(a)=a^(p^k)
 rho(a)=a^(p^(e*m_s-k))
 <x,y>_k=sum_i x_i y_i^(p^k)
 D_candidate(C)=sigma_k^2(D_code-first(C)).
```

The convention transformation is a separate proposition. The restricted Gram result explains equal same-code hull dimensions and LCD decisions. It does not identify dual codes, hull subspaces, supports, or generators.

The literature review must use the statuses and safe-use language from the Phase-8 reference audit. The final/corrected source gaps remain visible. The exact external prior-match boundary remains `NOT ESTABLISHED`.

## 13. Computational, figure, table, and citation architecture

- `MANUSCRIPT_SECTION_ARCHITECTURE.md` specifies the six fully defined computational cases and separates validation from diagnostics.
- `MANUSCRIPT_FIGURE_PLAN.md` designs five figures without generating them.
- `MANUSCRIPT_TABLE_PLAN.md` designs five tables without unverifiable data.
- `MANUSCRIPT_CLAIM_MATRIX.md` is the final wording guardrail.
- `PHASE9_REVIEWER_OBJECTIONS.md` records algebraic, combinatorial, and Galois/finite-field concerns before drafting.

N1 is absent from all proposed manuscript examples, figures, tables, claims, and citations.

## 14. Q1-level logical check

| Criterion | Status | Evidence |
|---|---|---|
| Clear problem statement | PASS | Introduction architecture states the exact labeled joint-enumerator question. |
| Explicit hypotheses | PASS | Single-source assumptions file; every result has scoped conditions. |
| Rigorous definitions | PASS | Notation audit and Section 2 plan. |
| Theorem-proof structure | PASS | 19-result map and proof order. |
| No circular reasoning | PASS | Acyclic graph with separate branches. |
| Literature positioning | PASS WITH CONDITIONS | Phase-8 comparison preserved; final/corrected records remain incomplete. |
| Reproducibility | PASS WITH CONDITIONS | Fully specified cases and existing captures; no N1. |
| Limitations | PASS | Section 11 and claim matrix. |
| Contribution precision | PASS | Frozen safe statement; no priority language. |
| Figure/table controls | PASS | Five planned figures and five planned tables, no fabricated data. |
| Submission readiness | NOT ASSESSED / NOT CLAIMED | Phase 9 does not produce a final manuscript or guarantee acceptance. |

## 15. Phase-9 decision gate

Exactly one Phase-9 decision is selected:

> **A. MANUSCRIPT ARCHITECTURE FROZEN — READY FOR DRAFTING**

The gate is satisfied because:

- the theorem dependency graph is acyclic;
- the assumptions are consolidated in one file;
- notation conflicts are identified and resolved by the recommended `A`/`K_s`/`mathcal F_s` choices;
- the central theorem states the setting, selection space, orbit data, variables, product, and coefficient interpretation;
- the candidate-first/code-first and Gram branches remain separate;
- the contribution boundary is stable and conservative;
- literature claims preserve Phase-8 evidence statuses;
- computational evidence is reproducible for fully specified cases;
- limitations and prohibited claims are explicit.

This decision means ready to begin a draft from the architecture. It does **not** mean submission-ready, accepted, novel by priority, or complete at the final/corrected source-verification level.

## 16. Required next phase

Phase 10 may draft the manuscript from this architecture, but before submission it must still:

1. recheck final/corrected source texts;
2. prepare actual `.tex`/`.bib` only through a real source workflow;
3. perform a final notation and citation pass;
4. rerun the full validation/package suite;
5. preserve the no-priority and no-N1 guardrails.
