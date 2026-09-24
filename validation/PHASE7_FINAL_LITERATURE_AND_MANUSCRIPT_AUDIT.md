# Phase 7 Final Literature, Novelty, N1, and Manuscript Audit

**Date:** 2026-09-24
**Branch:** `arena/01a0c9d2-galios-hull`
**Base before Phase 7:** `3c064a06a7fa32a402b3dd965bc239967c912c62`
**Purpose:** close the final source checks, freeze the conservative novelty boundary, exclude the underspecified validation artifact from manuscript evidence, and specify a mathematically rigorous manuscript without changing the Phase-6 mathematics.

## 1. Executive decision

The Phase-6 mathematics is frozen and unchanged. The 19-result conditional theorem chain, the separate candidate-first/code-first transformation proposition, the separate Gram-matrix invariance proposition, the inverse-Frobenius code-first convention, the support orientation, and the compatible same-factor-set transfer conditions remain the governing statements.

The publisher record for the primary article was independently reopened. Its title, authors, venue, volume/issue, date, article number, DOI, abstract, introduction, and section snippets are accessible. The readable arXiv preprint and the supplied local PDF provide the theorem-bearing source record. The final publisher full text is still access controlled, and the corrected full text of the finite-field comparison paper is still not readable here. Exact final/corrected theorem transfer is therefore not closed.

The final manuscript-readiness verdict is:

> **NOT READY — MATERIAL GAPS REMAIN**

This is the required conservative verdict while central final/corrected literature transfer and the exact external novelty boundary remain unresolved. It is not a mathematical disproof of the internal theorem chain.

## 2. Frozen mathematical convention

For `K_s=F_{q^{m_s}}=F_{p^{d_s}}` with `d_s=e m_s`, retain

\[
\sigma_{s,k}(a)=a^{p^k},
\qquad
\rho_{s,k}(a)=a^{p^{d_s-k}}=\sigma_{s,k}^{-1}(a).
\]

The principal code-first pairing and dual are

\[
\langle c,x\rangle_{s,k}=\sum_i c_i\sigma_{s,k}(x_i),
\qquad
D_{\mathrm{code-first}}(C)=\{x:\langle c,x\rangle_{s,k}=0\text{ for all }c\in C\}.
\]

The comparison candidate-first dual remains

\[
D_{\mathrm{candidate}}(C)=\{y:\sum_i y_i\sigma_{s,k}(c_i)=0\text{ for all }c\in C\}.
\]

The separate transformation identity is

\[
D_{\mathrm{candidate}}(C)=\sigma_{s,k}^{2}\bigl(D_{\mathrm{code-first}}(C)\bigr).
\]

The dual codes, generators, hull subspaces, factor supports, and support orientations are not identified. The restricted Gram argument proves equality only of same-code hull dimensions and LCD decisions. The main reciprocal, root action, compatibility condition, predicted incompatible twist, and support formula remain the inverse-Frobenius code-first formulas.

## 3. Final source checks

### 3.1 Primary publisher check

Directly checked:

- [ScienceDirect publisher record](https://www.sciencedirect.com/science/article/abs/pii/S0012365X25003589?via%3Dihub): title, authors, *Discrete Mathematics* 349(2), February 2026, article 114750, DOI `10.1016/j.disc.2025.114750`, abstract, introduction, section snippets, and access restriction.
- [Readable arXiv HTML](https://arxiv.org/html/2412.08512): source pairing, candidate-first dual definition, displayed reciprocal/twist, affine structural statements, hull formula display, and conditional quantum section.
- Local supplied PDF: `Galios hulls of constacclic codes over affine algebra rings'.pdf`; SHA-256 `0db90bfbeda69ad1af231b81d92f24be3589ed15ac2e0ade6605ba7ad0ddc039`; structural markers checked by `validation/source_pdf_theorem_check.py` and its capture.

The publisher page confirms the final article identity and broad scope. It does not expose the complete final theorem text in this environment. The readable preprint is not silently treated as identical to the final/corrected version.

### 3.2 Related-source checks

- [Springer finite-field article](https://link.springer.com/article/10.1007/s12095-022-00591-6): title, authors, publication data, abstract, DOI, and correction link checked.
- [Springer correction](https://link.springer.com/article/10.1007/s12095-022-00602-6): correction identity and DOI checked; complete corrected content not accessible.
- [ScienceDirect cyclic/negacyclic article](https://www.sciencedirect.com/science/article/pii/S107157971400166X): authors, DOI, abstract, outline, Theorem 1, Theorem 2, and Lemma 3 checked on the open publisher page.
- [AIMS Hermitian-average article](https://www.aimsciences.org/article/doi/10.3934/amc.2018027): authors, metadata, abstract, and introduction checked; full text access restricted.
- [Springer Galois-hull article](https://link.springer.com/article/10.1007/s10623-019-00681-2): metadata, abstract, and publication data checked; full text access restricted.
- [AIMS 2025 average article](https://www.aimsciences.org/article/doi/10.3934/amc.2025010): authors, metadata, abstract, and introduction checked; full text access restricted.
- [Springer non-chain Hermitian article](https://link.springer.com/article/10.1007/s40314-024-02789-1): metadata, authors, abstract, and scope checked.

The exact evidence and safe use of every reference are in `validation/FINAL_REFERENCE_AUDIT.md`.

## 4. Final literature claim and transfer closure

The historical Phase-4 ledger and Phase-6 matrix are preserved. Their Phase-7 final sections are now the controlling records:

- `validation/LITERATURE_CLAIM_LEDGER.md` — final claim statuses use only the required literature-status vocabulary.
- `validation/LITERATURE_TRANSFER_MATRIX.md` — final transfer statuses use only `DIRECT`, `DIRECT AFTER CONVENTION TRANSFORMATION`, `PARTIAL`, `NOT TRANSFERABLE`, and `UNVERIFIED`.
- `validation/FINAL_REFERENCE_AUDIT.md` — source-by-source identity, access, DOI, and manuscript-use audit.

Final conclusions:

1. The primary article's publisher identity and broad subject scope are `VERIFIED`.
2. The readable source convention is `VERIFIED` and is candidate-first.
3. The displayed source rho formulas have a `CONVENTION MISMATCH` with the literal candidate-first equations for non-involutory parameters; they become the frozen code-first formulas only after the explicit transformation and component exponent replacement.
4. Related finite-field, cyclic/negacyclic, average, and ring-specific records are only partial/background transfer unless the table says otherwise.
5. No external theorem is used as a substitute for the present weighted bivariate proof.
6. Exact final/corrected central theorem transfer is `VERIFY BEFORE MANUSCRIPT FINALIZATION`/`SOURCE UNAVAILABLE` in the final claim ledger and remains a material gap.

## 5. Novelty boundary

`validation/NOVELTY_BOUNDARY.md` classifies every central clause using only the required novelty statuses. The safe conclusion is:

- CRT, simple-root factor selection, and basic reciprocal tools are known or standard tools.
- The code-first convention transformation and the explicit separation of dual/hull objects are extensions of the checked comparison framework.
- The support/boundary and transfer product are combinations/adaptations with a potentially distinct formulation.
- An exact external match or priority boundary for the weighted bivariate labeled enumerator is **NOT ESTABLISHED**.
- Burnside/Pólya quotient enumeration, repeated roots, and unconditional quantum results are `FUTURE WORK`.

The permitted manuscript sentence is the conservative positioning paragraph in `NOVELTY_BOUNDARY.md`. Priority language is prohibited.

## 6. N1 exclusion and exact status

The internal validation artifact N1 remains:

> **UNSPECIFIED — CANNOT VALIDATE**

Only the following values are known: `q=16`, `n=15`, and `32768=2^15` proposed selections. The record does not specify `k`, the twist, component-field interpretation, factorization, factor labels, orbit permutation, expected histogram, or output format. No implementation or output was found in the repository search.

N1 is **EXCLUDED** from:

- the manuscript abstract;
- the introduction and literature review;
- the theorem statements and proof dependencies;
- every manuscript computational example and results table;
- the manuscript specification;
- all manuscript evidence for the transfer enumerator, novelty, or reproducibility.

The item remains only in the internal blueprint/audit history so that its unresolved status and the no-fabrication decision are auditable. No N1 parameter, histogram, factorization, or PASS claim is created.

## 7. Manuscript specification closure

`validation/MANUSCRIPT_DRAFT_SPECIFICATION.md` is the authorized manuscript-facing plan because no genuine manuscript source workflow exists. It contains:

- a conservative abstract;
- introduction and literature-review wording;
- fixed preliminaries and convention rules;
- the 19-result theorem architecture;
- separate candidate-first/code-first and Gram-invariance propositions;
- an acyclic proof-dependency graph;
- a fully specified computational-example policy;
- mandatory limitations and conclusion language;
- reference and submission checklists.

The specification does not fabricate `.tex` or `.bib` files and contains no N1 evidence.

## 8. Theorem and proof audit

The Phase-6 theorem chain remains frozen:

1. square-free affine decomposition;
2. factor-selection classification;
3. code-first second-slot pairing;
4. normalized inverse-Frobenius reciprocal;
5. root action;
6. compatible factor permutation;
7. dual generator;
8. compatibility/same-twist criterion;
9. hull support;
10. cyclic boundary statistic;
11. orbit polynomial;
12. transfer matrix;
13. closed-walk trace;
14. global joint enumerator;
15. total labeled-code count;
16. exact hull distribution;
17. LCD count;
18. mean;
19. variance.

The separate transformation and Gram propositions are not used to collapse the two conventions. The proof dependency graph in the manuscript specification is acyclic. The conditional assumptions remain square-free, simple-root, compatible-twist, labeled-component, and explicitly weighted.

## 9. Phase-7 status table

The table uses only the required Phase-7 status values: `RESOLVED`, `RESOLVED WITH CONDITIONS`, `VERIFY`, `UNRESOLVED`, `EXCLUDED`, `FUTURE WORK`, and `NOT APPLICABLE`.

| Audit item | Status | Evidence or condition |
|---|---|---|
| Frozen code-first convention and formulas | `RESOLVED` | Phase-2 through Phase-6 proofs and validators preserved; no mathematical change made. |
| Candidate-first/code-first distinction | `RESOLVED` | Separate transformation identity and separate Gram invariance proof retained. |
| Primary publisher identity and DOI | `RESOLVED WITH CONDITIONS` | Publisher record verified; complete final theorem text remains access controlled. |
| Readable source convention and displayed formulas | `RESOLVED WITH CONDITIONS` | arXiv HTML and local PDF structural check agree; final-version transfer remains conditional. |
| Corrected finite-field source theorem transfer | `UNRESOLVED` | Correction record verified; corrected full theorem text not accessible. |
| Central literature transfer | `UNRESOLVED` | No exact final/corrected source theorem is safely transferable without additional checking. |
| Novelty boundary | `UNRESOLVED` | Conservative clause classifications recorded; no priority audit completed. |
| N1 artifact | `EXCLUDED` | Exact record remains `UNSPECIFIED — CANNOT VALIDATE`; no manuscript evidence. |
| 19-result theorem architecture | `RESOLVED WITH CONDITIONS` | Conditional proofs and dependency graph are preserved. |
| Fully specified computations | `RESOLVED WITH CONDITIONS` | Existing captures and independent Phase-6 validator cover only listed finite instances. |
| Repeated-root and incompatible transfer | `FUTURE WORK` | Outside the main theorem. |
| Burnside/Pólya quotient enumeration | `FUTURE WORK` | No group action or quotient count proved. |
| Unconditional quantum claims | `FUTURE WORK` | No distance/Gray-map/construction theorem transferred. |
| Manuscript specification | `RESOLVED WITH CONDITIONS` | Markdown specification created; genuine source workflow still absent. |
| Package/ZIP after Phase-7 edits | `RESOLVED WITH CONDITIONS` | Final archive passed `unzip -t`, manifest/content, Git-metadata exclusion, source-PDF hash, required-file, manuscript-specification exclusion, and clean extracted-suite checks; 53 manifest files. |

## 10. Reproducibility and package plan

Before the Phase-7 commit:

1. run every existing root validator and the independent Phase-6 end-to-end check with `PYTHONDONTWRITEBYTECODE=1`;
2. run the source-PDF checker and confirm the recorded hash;
3. confirm no manuscript-facing file contains N1 evidence;
4. check the final ledger and transfer statuses against their allowed vocabularies;
5. rebuild `Galios-Hull-main-files.zip` using the existing package convention, including the four Phase-7 documents and updated blueprint/ledgers;
6. extract the archive into a clean temporary directory, compare manifest/content, exclude Git metadata, verify the source-PDF hash, and rerun the extracted validation suite;
7. record the new archive SHA-256 and member count in the final report.

No historical audit or capture is deleted or weakened.

## 11. Final audit conclusion

Phase 7 resolves the source identity, accessible source scope, convention record, reference metadata, manuscript structure, N1 exclusion policy, and conservative novelty boundary. It does not manufacture the inaccessible final/corrected theorem text or a novelty priority result. The package can be finalized with the exact verdict:

> **NOT READY — MATERIAL GAPS REMAIN**
