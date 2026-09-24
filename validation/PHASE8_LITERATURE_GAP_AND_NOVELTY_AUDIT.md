# Phase-8 Literature Gap, Theorem-Transfer, and Novelty Audit

**Date:** 2026-09-24
**Branch:** `arena/01a0c9d2-galios-hull`
**Mandatory base:** `703260d610b4980df25610694bbe6a04f937abbc`
**Starting Phase-8 state:** clean and synchronized at the mandatory base; historical Phase-1 through Phase-7 evidence unchanged before this audit.

## 1. Executive decision

> **B. READY WITH NARROWED CONTRIBUTION CLAIMS**

This is the Phase-8 decision. It does **not** mean that an external priority claim has been established. It means that the internal theorem package supports manuscript drafting only as a bounded, conditional, self-contained labeled-enumerator contribution, with the literature limits and no-priority language in `CONTRIBUTION_BOUNDARY.md`.

The audit rejects `A` because the exact prior-theorem boundary and complete final/corrected source transfer remain unresolved. It rejects `C` because a defensible narrower contribution survives: the exact weighted joint product is proved internally for the stated square-free affine/code-first/labeled family, while no checked source was verified to state that complete product. It rejects `D` and `E` because no mathematical overlap or error requiring reformulation/repair was found under the frozen hypotheses.

## 2. Frozen framework and non-negotiable distinctions

The audit preserves:

```text
sigma(a)=a^(p^k),
rho(a)=a^(p^(e*m_s-k)),
lambda_s^(1+p^(e*m_s-k))=1,
D_candidate(C)=sigma_k^2(D_code-first(C)).
```

The candidate-first and code-first dual codes remain distinct objects. The audit does not identify dual codes, hull subspaces, factor supports, dimensions, LCD claims, or enumerators without the exact theorem/condition that justifies the comparison. The separate Gram result concerns same-code hull dimensions and LCD decisions; it is not a support equality.

The principal count remains over distinct labeled factor selections. It is not an equivalence-class count.

## 3. Literature-search method and evidence hierarchy

The Phase-8 search deliberately included exact and adjacent formulations:

- finite-field cyclic, negacyclic, and constacyclic prescribed-hull counts;
- Galois hulls and `k`-Galois conventions;
- finite chain rings and `Z4` cyclic codes;
- non-chain/direct-product rings and affine algebras;
- double cyclic, double circulant, and four circulant exact enumerations;
- transfer matrices, closed-walk traces, cyclic binary transitions, runs, and generating functions.

Original/publisher or readable full theorem text was preferred. Abstracts and publisher snippets were retained only for scoped claims. No search result was used to fabricate a theorem number, quotation, factorization, histogram, DOI, or priority statement.

The detailed source comparison is in `validation/CENTRAL_RESULT_COMPARISON.md`. The contribution boundary is in `validation/CONTRIBUTION_BOUNDARY.md`.

## 4. Strongest verified findings

### 4.1 Primary affine-algebra record

The readable arXiv source [arXiv:2412.08512](https://arxiv.org/html/2412.08512) gives the closest structural setting: a square-free affine algebra decomposed into finite-field components, constacyclic component codes, Galois duals/hulls, hull-dimension formulas, LCD conditions, and conditional quantum applications. Its conclusion explicitly identifies enumeration of non-isometric constacyclic codes with a prescribed Galois hull dimension over the affine algebra as an open future problem.

That statement is strong evidence that this source does not itself provide the complete all-code enumeration sought here. It is not a universal absence or priority theorem. The final *Discrete Mathematics* record is bibliographically identified at DOI `10.1016/j.disc.2025.114750`, but its full theorem text remains access-controlled in this environment.

The source convention is candidate-first in the displayed dual equation. Its displayed rho-based formulas therefore cannot be imported literally as candidate-first formulas in non-involutory cases. The frozen transformation is retained, and the present code-first theorem is independently proved.

### 4.2 Exact hull enumeration is already known in narrower families

The following are verified or source-level confirmed adjacent results:

- Sangwisut–Jitman–Ling–Udomkavanich give exact cyclic/negacyclic finite-field hull dimensions and fixed-dimension counts.
- The 2023 finite-field constacyclic article reports a Galois hull formula and prescribed-dimension counts under restrictions; its correction must be read before exact theorem import.
- Talbi et al. give cyclic serial chain-ring hull parameters and Proposition 8 counts for a fixed `q`-dimension of the Euclidean hull.
- Jitman–Sangwisut–Udomkavanich and Pathak–Sharma give fixed 2-dimension enumerations for cyclic `Z4` families.
- Gao–Wu–Fu give fixed-hull enumeration for double cyclic codes over `Z_2`.
- Aliabadi–Kalaycı–Zadehdabbagh give prescribed-hull enumeration for double and four circulant codes over finite fields.

Therefore the manuscript must not claim that exact hull-dimension enumeration, reciprocal-pair counting, CRT decomposition, or generating functions are individually new.

### 4.3 Non-chain/direct-product records are structurally close but not exact matches

The 2024 finite non-chain-ring record over `F_q+vF_q` and the open 2026 *Entropy* paper over a restricted CRT/direct-product ring both establish componentwise code/dual/hull structure and lcm/Gram formulas. The 2026 source uses a code-first-looking definition and proves additive component hull dimensions, but it does not state the complete weighted labeled `trace(T^a)` product. Its quantum constructions are outside the present classical theorem.

The 2025 average-dimension record over `R_{m,q}=F_q[u]/<u^m-u>` and the 2026 small-hull paper further show that average and prescribed-small-dimension Galois-hull results are active adjacent topics. They do not provide the exact target product in the checked text.

## 5. Central enumerator status

There are two separate statuses.

### Internal mathematical status

`E(u,z)=product_s product_O trace(T_(w_O)^(a_O))` is **PROVED WITH CONDITIONS** by the preserved 19-result theorem architecture and independently checked finite instances. The conditions are square-free affine decomposition, simple roots, fixed component labels, code-first convention, compatible same-factor-set twists, equal factor degree within each orbit, and labeled factor selections.

The specializations for total count, exact hull distribution, LCD count, mean, and variance are conditional corollaries. The exceptional two-cycle variance case remains explicit.

### External literature status

No checked source was verified to state the complete target product for the exact combination of labeled square-free affine components, code-first extension-field action, compatible twists, weighted boundary support, and bivariate code/hull dimensions. This is `UNVERIFIED` as an external exact match, not a claim that no such source exists.

## 6. Hull-enumeration status

The broad claim “hull enumeration” is `KNOWN` in narrower fields, constacyclic families, chain rings, `Z4`, double cyclic, and double/four circulant settings. The narrower claim that remains defensible is:

> We derive the exact joint labeled code-dimension/hull-dimension polynomial for the specified square-free affine factor-selection family under the frozen code-first convention.

This is not a claim that the first fixed-dimension distribution has been found. It is an application-specific exact formula whose external priority is not established.

## 7. Convention-transfer status

| Transfer item | Status | Decision |
|---|---|---|
| Candidate-first source dual to frozen code-first dual | `DIRECT AFTER CONVENTION TRANSFORMATION` | Use `D_candidate=sigma^2(D_code-first)` and keep subspaces distinct. |
| Primary source displayed rho reciprocal/twist as literal candidate-first theorem | `NOT TRANSFERABLE` | Do not import as printed in non-involutory cases. |
| Primary affine structural component/lcm results after slot and exponent conversion | `PARTIAL` | Inform background; prove the frozen result independently. |
| Finite-field cyclic/negacyclic fixed-dimension counts | `PARTIAL` | Transfer only the narrower background facts. |
| Chain-ring Proposition 8 fixed-dimension count | `PARTIAL` | Chain-ring nilpotent-layer hypotheses do not become square-free affine hypotheses. |
| Non-chain/direct-product component hull decomposition | `PARTIAL` | Structural comparison only; no target enumerator transfer. |
| Standard transfer-matrix powers and trace of closed walks | `DIRECT` | Standard combinatorial identity, not an external hull theorem. |
| Exact external theorem equal to the central weighted product | `UNVERIFIED` | No source is substituted for the internal proof. |

## 8. Explicit test of `b_O` and the transfer matrix

For a cyclic binary word `epsilon`, each summand `epsilon_i(1-epsilon_(i+1))` is one exactly at an oriented `1-to-0` edge. If the word is nonconstant, every one-run has exactly one exit edge and every zero-run has exactly one entry edge. Consequently

```text
b_O = number of 1-to-0 transitions
    = number of one-runs
    = number of zero-runs.
```

For constant all-zero and all-one words, `b_O=0`, as required. Thus `b_O` is the standard cyclic transition/run statistic, not a newly named combinatorial invariant.

The matrix

```text
T_w(u,z) = [[u^w, 1], [u^w z^w, 1]]
```

assigns the `u` weight to a selected source bit and the `z` weight to a `1-to-0` edge. Matrix multiplication enumerates weighted walks; `trace(T_w^a)` closes the last state to the first and counts each indexed cyclic selection word once. This is the standard finite-state transfer/closed-walk mechanism. The application-specific content is the identification of the code-first hull support with those weighted boundary edges and the product over the algebraic factor orbits.

## 9. Novelty classification

| Clause | Classification | Reason |
|---|---|---|
| CRT, simple-root factor selection, reciprocal/lcm basics | `STANDARD TOOL` / `KNOWN` | Established algebraic and coding ingredients. |
| Code-first convention transformation and explicit support/convention separation | `EXTENSION` | Independently derived and required by the frozen convention. |
| Boundary support as the weighted cyclic transition statistic | `COMBINATION` | Algebraic hull support and standard cyclic transitions are combined. |
| Two-state matrix and trace | `STANDARD TOOL` | General transfer-matrix/closed-walk machinery. |
| Exact weighted bivariate labeled product in the frozen family | `POTENTIALLY DISTINCT` as a formulation; `NOT ESTABLISHED` as a priority claim | No exact prior match was verified, but final/corrected source coverage is incomplete. |
| Fixed-dimension hull enumeration in general | `KNOWN` | Confirmed in multiple narrower families. |
| Burnside/Pólya, repeated roots, incompatible two-modulus transfer, unconditional quantum claims | `FUTURE WORK` | Outside the frozen theorem. |

## 10. N1 status

N1 remains exactly:

> **UNSPECIFIED — CANNOT VALIDATE**

Only `q=16`, `n=15`, and `32768=2^15` are known. No `k`, twist, component-field interpretation, factorization, orbit decomposition, expected histogram, or executable output is inferred or used as evidence.

## 11. Mathematical and convention validation

No Phase-8 mathematical code changes were needed. The prior independent checks remain the evidence:

- all Phase-1 through Phase-7 finite validators and captures;
- direct code-first dual and reciprocal checks;
- forward versus inverse support diagnostics on non-involutory cycles;
- transfer product versus exhaustive labeled selections;
- independent candidate-first/code-first transformation;
- restricted Gram-matrix hull-dimension/LCD check;
- compatible nontrivial twist checks;
- incompatible-twist diagnostics kept outside transfer;
- all 73 rank-two planes in `F_8^3` in the independent end-to-end check.

The Phase-8 audit adds literature and scope decisions only; it does not alter Theorems 1–19, the frozen convention, the Phase-5 verdict, or N1.

## 12. Manuscript decision and remaining gaps

The manuscript may be drafted only with the contribution boundary in `CONTRIBUTION_BOUNDARY.md`:

- present the exact product as a conditional self-contained labeled enumerator;
- acknowledge known fixed-dimension and adjacent ring/generalized-cyclic results;
- call the transition statistic and transfer mechanism standard;
- make no priority or firstness claim;
- retain the candidate-first/code-first transformation and source mismatch;
- retain N1 exclusion and all scope exclusions.

Remaining gaps are formally characterized rather than hidden:

1. the final publisher theorem text of the primary affine article is still inaccessible;
2. the corrected full theorem text of the 2023 finite-field constacyclic paper is still inaccessible;
3. no exhaustive priority search can certify `NOT ESTABLISHED` into a positive novelty claim;
4. N1 lacks a specification;
5. repeated roots, incompatible two-modulus transfer, equivalence classes, and quantum distance remain outside scope.

These gaps prevent verdict A but do not require mathematical reformulation or repair for verdict B.

## 13. Phase-8 status table

| Item | Status | Record |
|---|---|---|
| Central internal enumerator | `PROVED WITH CONDITIONS` | Existing theorem chain and finite evidence; no mathematical changes. |
| Exact prior match to central product | `UNVERIFIED` | No checked source states the complete product. |
| Broad hull-enumeration novelty | `KNOWN` | Many narrower exact counts exist. |
| Application-specific contribution boundary | `POTENTIALLY DISTINCT` | Safe only with no-priority language. |
| Candidate/code-first transformation | `DIRECT AFTER CONVENTION TRANSFORMATION` | Exact `sigma^2` relation retained. |
| Primary displayed reciprocal transfer | `NOT TRANSFERABLE` | Convention mismatch remains. |
| Standard `b_O` transition/run statistic | `STANDARD TOOL` | Elementary cyclic-word identity. |
| Standard transfer trace | `DIRECT` | General closed-walk identity. |
| N1 | `UNSPECIFIED — CANNOT VALIDATE` | Excluded from manuscript evidence. |
| Mathematical error | `NONE FOUND` | No repair required under hypotheses. |
| Final decision | `B. READY WITH NARROWED CONTRIBUTION CLAIMS` | See contribution boundary. |

## 14. Final recommendation

Proceed to a manuscript draft only as a **conditional exact labeled-enumerator paper with a narrowed contribution statement**. Do not submit or describe it as a first/novel hull-enumeration result until the remaining final/corrected source texts and a broader priority comparison have been independently resolved. Preserve every historical audit and every exclusion.

## 15. Literature claim ledger and citation controls

The historical `LITERATURE_CLAIM_LEDGER.md`, `LITERATURE_TRANSFER_MATRIX.md`, and `FINAL_REFERENCE_AUDIT.md` remain the controlling source records. Phase 8 appends rather than rewrites them. Every source claim must retain its evidence scope:

- theorem-bearing full text supports theorem-level statements only within the displayed hypotheses;
- publisher abstracts and records support scoped metadata and abstract-level scope, not an imported theorem;
- inaccessible final or corrected text remains `SOURCE UNAVAILABLE` or `VERIFY BEFORE MANUSCRIPT FINALIZATION` in the appropriate historical ledger;
- search snippets and citation aggregators are discovery aids only;
- no theorem number, quotation, DOI, factorization, histogram, or publisher wording may be inferred from an inaccessible record.

The permitted transfer vocabulary remains exactly `DIRECT`, `DIRECT AFTER CONVENTION TRANSFORMATION`, `PARTIAL`, `NOT TRANSFERABLE`, and `UNVERIFIED`. The permitted novelty vocabulary remains exactly `KNOWN`, `STANDARD TOOL`, `ADAPTED`, `COMBINATION`, `EXTENSION`, `POTENTIALLY DISTINCT`, `NOT ESTABLISHED`, and `FUTURE WORK`.

## 16. Validation, package, and historical-preservation record

Phase 8 introduced no mathematical or validator-code changes. The clean full suite is captured in `validation/phase8_full_validation.out` and has exit code `0` with zero stderr lines. It includes all prior finite, convention, enumerator, end-to-end, source-PDF, and N1-exclusion checks. N1 remains `UNSPECIFIED — CANNOT VALIDATE`.

The rebuilt `Galios-Hull-main-files.zip` contains the Phase-8 comparison, contribution boundary, audit, updated historical appendices, full-suite capture, package-verification capture, all prior evidence, the supplied source PDF, and the archive runner. `unzip -t`, exact manifest comparison, clean extraction, source-PDF hash, Git-metadata exclusion, required-file checks, and the clean extracted suite all pass. No historical audit or capture was deleted or weakened.

## 17. Final Phase-8 handoff checklist

Before commit and push, confirm all of the following:

1. the mandatory base and branch are recorded;
2. the frozen code-first formulas and `D_candidate(C)=sigma_k^2(D_code-first(C))` remain visible;
3. the 19-result architecture and separate convention/invariance propositions remain unchanged;
4. the central comparison has 19 required result rows and every transfer label is permitted;
5. exact hull enumeration is acknowledged as `KNOWN` in narrower families;
6. `b_O` and the transfer trace are called `STANDARD TOOL`, with their application classified separately;
7. the exact target product is `POTENTIALLY DISTINCT`/`NOT ESTABLISHED`, never a priority claim;
8. repeated roots, incompatible twists, Burnside/Pólya quotients, unconditional quantum claims, and N1 remain outside the central theorem;
9. the ZIP and clean extracted validator suite pass;
10. the commit message, if all checks remain green, is exactly `Complete literature gap and novelty stress test`.

**Final Phase-8 decision:** `B. READY WITH NARROWED CONTRIBUTION CLAIMS`.
