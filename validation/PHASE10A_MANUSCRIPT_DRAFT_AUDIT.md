# Phase 10A — Full Manuscript Draft Audit

**Audit date:** 2026-09-24
**Branch:** `arena/01a0c9d2-galios-hull`
**Mandatory base:** `e4548cfc3d7563a26bb1f3357b235e683e96d73c`
**Previous decision:** Phase 9 — `A. MANUSCRIPT ARCHITECTURE FROZEN — READY FOR DRAFTING`
**Phase-10A decision:** `A. COMPLETE FIRST DRAFT — READY FOR MANUSCRIPT AUDIT`

**Draft title:** `Exact Joint Enumeration of k-Galois Hull Dimensions for Labeled Constacyclic Codes over Square-Free Affine Algebras`

This phase creates the first complete journal-style LaTeX draft from the frozen architecture. It does not redesign the mathematical framework, create a submission package, or assert submission readiness.

## 1. Starting-state verification

| Check | Result |
|---|---|
| Starting `HEAD` | `e4548cfc3d7563a26bb1f3357b235e683e96d73c` |
| Branch | `arena/01a0c9d2-galios-hull` |
| Initial worktree | clean |
| Phase-1 through Phase-9 evidence | preserved |
| Historical audits | not deleted or overwritten |
| Frozen architecture files | read and followed |
| Final `.tex`/`.bib` before Phase 10A | absent, as required by Phase 9 |

## 2. Files created

- `manuscript/main.tex`
- `manuscript/references.bib`
- `validation/PHASE10A_MANUSCRIPT_DRAFT_AUDIT.md`

No `manuscript/sections/`, `manuscript/figures/`, or `manuscript/tables/` directories were needed because the first draft is self-contained in `main.tex` and uses mathematical figure placeholders.

No cover letter, submission form, response-to-reviewers document, graphical abstract, or publisher-format package was created.

## 3. Section completion status

| Manuscript component | Status |
|---|---|
| Title | complete; default Phase-9 title used |
| Abstract | complete; contains setting, assumptions, enumerator, orbit product, trace, and consequences |
| Keywords | complete; seven mathematically precise keywords |
| 1. Introduction | complete; motivation, literature scope, question, contribution, organization |
| 2. Preliminaries | complete; fields, algebra, factors, codes, pairing, hull |
| 3. Affine decomposition and factor selections | complete; propositions and proofs |
| 4. `k`-Galois duality | complete; reciprocal, root action, generator, compatibility, convention comparison, Gram result |
| 5. Hull support and orbit structure | complete; lcm support, boundary statistic, dimension conversion |
| 6. Exact orbit enumeration | complete; transition count and orbit polynomial |
| 7. Transfer matrix | complete; entries, destination weighting, trace proof |
| 8. Global joint generating polynomial | complete; Theorem 8.1 and coefficient interpretation |
| 9. Consequences | complete; six requested subsections |
| 10. Computational validation | complete; validated cases and reproducibility separation |
| 11. Limitations and extensions | complete; all mandatory exclusions |
| 12. Conclusion | complete; result, evidence, scope, future work |
| References | complete through `references.bib`; all entries cited |
| Figures | five LaTeX placeholders with captions and labels; no fabricated graphics |
| Tables | four actual tables: notation, literature, computation, scope |

## 4. Theorem inventory

The draft follows the validated theorem order:

1. square-free affine component decomposition;
2. factor-selection parametrization;
3. ordinary-dual translation for the code-first pairing;
4. normalized inverse-Frobenius reciprocal;
5. root action;
6. compatible factor permutation;
7. ordinary constacyclic reciprocal lemma;
8. code-first dual generator;
9. compatibility and same-twist condition;
10. hull support;
11. cyclic boundary statistic;
12. local orbit polynomial;
13. local transfer matrix and trace;
14. global exact labeled joint enumerator, stated as Theorem `\ref{thm:central}`;
15. total labeled-code count;
16. code-dimension distribution;
17. hull-dimension distribution;
18. LCD count;
19. mean hull dimension;
20. variance with the separate length-two case;
21. candidate-first/code-first transformation proposition;
22. same-code hull-dimension/LCD Gram proposition.

The additional ordinary reciprocal lemma is a standard intermediate proof step, not a new contribution. The candidate-first transformation and Gram proposition remain separate from the code-first support chain.

## 5. Citation inventory

The bibliography contains 13 entries, all cited in `main.tex`:

- final publisher metadata and readable preprint for the primary affine-algebra record;
- finite-field constacyclic record and its correction;
- finite-field cyclic/negacyclic hull enumeration;
- finite-chain-ring cyclic serial hull enumeration;
- two `Z4` hull records;
- restricted non-chain/direct-product Galois-hull structure;
- double cyclic and double/four circulant enumeration;
- average- and small-dimension Galois-hull records.

The bibliography uses only metadata recorded in the Phase-7/8 reference audits. No DOI, theorem number, quotation, publisher text, or journal outcome was fabricated. The corrected finite-field record is cited together with its correction, while the accessible preprint and final publisher record are cited separately.

## 6. Formula inventory

The draft includes and uses the frozen formulas:

- `q=p^e`, `K_s=F_(q^(m_s))=F_(p^(d_s))`, `d_s=e m_s`;
- `sigma(a)=a^(p^k)`;
- `rho(a)=a^(p^(d_s-k))`;
- the code-first second-slot pairing;
- the normalized inverse-Frobenius reciprocal;
- compatibility `lambda_s^(1+p^(d_s-k))=1`;
- `D_candidate(C)=sigma_k^2(D_code-first(C))`;
- hull support `(mathcal F_s\J_s) intersection tau(J_s)=tau(J_s)\J_s`;
- `b_O=sum_i epsilon_i(1-epsilon_(i+1))`;
- `P_(a,w)(z)=2+sum_r 2 binom(a,2r)z^(rw)` and its equivalent requested form;
- `T_w(u,z)=[[u^w,1],[u^w z^w,1]]`;
- the central product `E(u,z)`;
- total count, code and hull distributions, LCD count, mean, and variance;
- the separate `a=2` variance term `w^2/4`.

## 7. Assumption consistency

The draft is restricted to the single-source assumptions in `MANUSCRIPT_ASSUMPTIONS.md`:

- square-free affine decomposition;
- `gcd(n,p)=1` and simple roots;
- fixed labeled components and factor selections;
- compatible same-factor-set twists;
- code-first second-slot pairing;
- equal factor degree within each reciprocal orbit;
- global `F_q` dimension weights.

Repeated roots, incompatible twists, equivalence classes, Burnside/Pólya counting, unrestricted rings, unconditional quantum claims, and N1 are explicitly excluded.

## 8. Notation consistency

The draft uses `A` for the affine algebra, `K_s` for component fields, and `mathcal F_s` for factor sets. It does not use ambiguous bare `F_s` for a factor set. The main theorem uses `K` and `H` only for coefficient exponents, while `k` remains the Frobenius iteration parameter. `u` records code dimension and `z` records hull dimension.

## 9. Unsupported-claim scan

The manuscript contains no unsupported use of:

- `first-ever`;
- `unprecedented`;
- `state-of-the-art`;
- `novel`;
- `best`;
- `optimal`.

The legitimate occurrences of “first” belong to `code-first`, `candidate-first`, ordinary slot descriptions, or proof-order prose. The legitimate occurrence of “unique” is the algebraic phrase “unique factorization.” The occurrences of “only” are scope qualifiers such as “background only” or “diagnostic only,” not exclusivity or priority claims. None is a priority claim. The draft explicitly says that no priority claim is made.

## 10. N1 scan

The abstract contains no N1 reference. Section 10 does not use N1 as a computational case. Section 11 mentions N1 only to state that the artifact is excluded and remains `UNSPECIFIED — CANNOT VALIDATE`. No N1 parameter, factorization, histogram, twist, orbit decomposition, or output is included.

## 11. Reference consistency

A structural citation check reports:

- bibliography keys: `13`;
- citation keys used by `main.tex`: `13`;
- missing citation entries: `0`;
- uncited bibliography entries: `0`.

## 12. LaTeX structural validation

The environment does not provide `pdflatex`, `bibtex`, or `latexmk`. Therefore no compilation success is claimed.

Structural validation passed:

- balanced braces;
- matched `begin`/`end` environments;
- five figure placeholders;
- four verified data tables;
- required 12 primary sections plus generated References heading;
- six Section-9 subsections with six formal corollaries;
- the central Theorem 8.1 label and separate convention/Gram propositions;
- citation/BibTeX consistency;
- no final figure files required by the placeholder draft;
- no malformed control-character insertion.

A later manuscript-audit phase must compile the source in a LaTeX-enabled environment and resolve any engine- or package-specific warnings.

## 13. Remaining drafting gaps

1. Replace figure placeholders with reviewed production figures if the target journal permits them.
2. Perform a LaTeX-enabled compilation and resolve layout, bibliography, and cross-reference warnings.
3. Recheck the final/corrected literature texts before submission-oriented writing.
4. Conduct a final human mathematical edit of every proof and source attribution.
5. Keep quantum material conditional or remove it if the target journal requires a purely classical coding-theory focus.

## 14. Phase-10A decision

Exactly one decision is selected:

> **A. COMPLETE FIRST DRAFT — READY FOR MANUSCRIPT AUDIT**

The draft is complete enough for a dedicated manuscript audit. This decision does not mean submission-ready, accepted, or externally validated as a priority result.
