# Phase 10D — Controlled Typesetting, Compilation, and Source-Level Publication Audit

**Audit date:** 2026-09-24 (Asia/Calcutta)
**Repository:** `arunyadav0307-stack/Galios-Hull`
**Branch:** `arena/01a0c9d2-galios-hull`
**Starting commit:** `873f970cc21d8f548d6708e7d73c4e6540119ba2`
**Starting commit message:** `Repair global affine-product pairing and hull decomposition`
**Phase-10C evidence preserved:** yes

## 1. Controlled starting-state result

The repository was inspected before modification. The branch and HEAD matched the required Phase-10C state, and the initial worktree was clean. The inspected manuscript, bibliography, Phase-10C audit/capture, dependency graph, table plan, assumptions, draft specification, code validators, and validation outputs were present.

No Phase-10C validation artifact was overwritten or deleted. The Phase-10C capture remains at `validation/phase10c_full_validation.out`.

## 2. Actual compilation result

The following tools were checked:

```text
pdflatex, bibtex, biber, latexmk, tectonic, xelatex, lualatex,
tex, pdftex, luatex, etex, context, context-cli
```

All were unavailable.

**ACTUAL LATEX COMPILATION NOT AVAILABLE IN THIS ENVIRONMENT**

Consequently:

- no LaTeX compilation command was executed;
- no PDF was generated or claimed;
- no bibliography engine was executed;
- compiler warnings, overfull boxes, underfull boxes, package conflicts at runtime, and final typeset output could not be assessed;
- this audit does not claim successful compilation.

The exact tool check and source-level results are captured in `validation/phase10d_source_audit.out`.

## 3. Controlled source edits

Only editorial/source-consistency changes were made to `manuscript/main.tex`:

1. Added explicit callouts for all four tables and all five figure placeholders.
2. Corrected the Introduction organization paragraph to mention Section 12, Conclusion.
3. Made the weighted boundary proposition explicitly refer to `C(J)` and `\operatorname{Hull}_{A,k}(C(J))`, without changing the frozen formula.
4. Replaced Markdown backticks around the N1 status with LaTeX-safe `\texttt{...}` markup.
5. Clarified that N1 is excluded as a computational case, while retaining the exact status `UNSPECIFIED — CANNOT VALIDATE`.
6. Replaced generic references to the global lemmas in the Theorem 8.1 proof with explicit cross-references to `lem:global-code`, `lem:global-dual`, and `lem:global-hull`.

No theorem architecture, hypothesis, formula, convention, enumerator, validation result, literature claim, or scope boundary was redesigned.

## 4. Architecture audit

The source contains the required mathematical section order:

1. Introduction
2. Algebraic and Coding-Theoretic Preliminaries
3. Square-Free Affine Decomposition and Factor-Selection Codes
4. `k`-Galois Duality for Component Constacyclic Codes
5. Hull Support and Orbit Structure
6. Exact Orbit Enumeration
7. Transfer-Matrix Representation
8. Global Joint Generating Polynomial
9. Consequences
10. Computational Validation and Reproducibility
11. Limitations and Extensions
12. Conclusion

The bibliography command supplies the References section through the standard LaTeX bibliography environment. No unrelated section was added and no mathematical section was reordered.

## 5. Package and command audit

The preamble contains no duplicate package declarations. The principal packages have clear uses:

- `fontenc`, `inputenc`, and `lmodern` for text/font handling;
- `amsmath`, `amssymb`, and `amsthm` for mathematical notation and theorem environments;
- `booktabs` for tables;
- `geometry` for page margins;
- `hyperref` for hyperlinks;
- `microtype` for typesetting refinement.

`array`, `enumitem`, and `mathtools` are retained from the existing draft; no source conflict was detected. `enumitem` is not materially used in the current source, but its presence is harmless and was not removed without an available compiler regression check.

All custom commands used in the manuscript are defined in the preamble. No undefined custom command was found by the source scan.

## 6. Environment, label, and cross-reference audit

The source-level audit passed:

- all `begin`/`end` environments balanced;
- theorem, lemma, proposition, corollary, proof, aligned, cases, figure, and table environments balanced;
- 15 labels, with no duplicate labels;
- 16 reference occurrences, with no undefined references;
- no unreferenced labels;
- all four table labels are called out;
- all five figure labels are called out;
- no `\includegraphics` command or missing external figure dependency;
- `git diff --check` passed.

The global Theorem 8.1 proof now explicitly references the repaired global-code, global-dual, global-hull, and global-dimension statements.

## 7. Displayed-equation and narrative audit

The source uses unnumbered display math for local definitions and calculations, while theorem-like statements carry the structural numbering. There are no equation labels or `\eqref` calls requiring an equation-number audit. This is internally consistent: the displayed formulas are introduced by surrounding prose and are contained within named propositions, lemmas, theorems, or corollaries where later reference is needed.

The following frozen displays were specifically checked for presence and narrative context:

- inverse-Frobenius reciprocal;
- root action;
- compatibility condition;
- component and global hull support;
- orbit polynomial;
- transfer matrix and trace identity;
- global A-valued pairing;
- global dual and hull decomposition;
- global code and hull dimensions;
- global generating polynomial and coefficient extraction;
- uniform measure;
- mean and variance.

No formula was silently changed for stylistic reasons.

## 8. Table audit

There are exactly four manuscript data tables, sequentially positioned in source order:

1. literature comparison;
2. core notation and assumptions;
3. computational validation;
4. scope boundaries.

Every table is introduced by prose, has a descriptive caption, has a label, and is called out in the surrounding text. The Phase-10C five-versus-four resolution remains intact: dependency and validation artifacts are not additional manuscript data tables.

## 9. Figure audit

There are exactly five intended figure positions. Each is a self-contained `\fbox`/`\parbox` placeholder with a caption and label, and each is now called out in the text:

1. workflow;
2. square-free decomposition;
3. factor orbit and hull-support mechanism;
4. transfer matrix;
5. local-to-global enumerator.

No external image file is referenced, no scientific diagram was fabricated, and no placeholder was redesigned. Since compilation is unavailable, final float placement and box dimensions remain unverified.

## 10. Bibliography audit

Static bibliography checks passed:

- 13 BibTeX entries;
- 13 cited keys;
- every cited key exists;
- every bibliography entry is cited;
- no duplicate BibTeX keys;
- balanced bibliography braces;
- every entry has `author`, `title`, and `year` fields;
- article entries have journal/volume data and DOI fields in the existing source records where recorded;
- preprint/misc entries retain their e-print/archive metadata;
- no new reference or DOI was introduced in Phase 10D.

The existing bibliography retains some abbreviated author-name fields in neighboring-literature records. Those records are carried under the prior literature audit and should receive a final publisher-metadata check before submission; no missing names were guessed in this phase.

Because BibTeX is unavailable, BibTeX parsing and rendered bibliography typography were not executed. Static key and brace validation is not a substitute for a bibliography run.

## 11. Claim-level source audit

The manuscript claims were classified as follows:

- **Mathematical derivation:** the conditional algebraic, duality, support, orbit, transfer, global product, and corollary results proved in the manuscript.
- **Computational evidence:** the explicitly listed finite validators and the Phase-10C global-product capture.
- **Cited literature:** scoped background and convention/source comparisons only.
- **Editorial/background:** motivation, organization, and limitations.
- **Unsupported/overstated:** no new instance identified.

The manuscript contains no firstness, first-ever, state-of-the-art, uniqueness, universal-absence, or unconditional quantum-performance claim. It explicitly states that no quantum distance, QECC parameter, optimality, or fault-tolerance conclusion follows from the hull enumerator alone.

The statement that the exact prior theorem identical to the weighted bivariate product was not verified is explicitly qualified as not being a universal absence claim.

## 12. Scope and N1 audit

The source continues to exclude:

- repeated-root codes;
- incompatible same-factor-set transfer;
- equivalence-class or quotient enumeration;
- Burnside/Pólya counting;
- unrestricted ring families;
- unconditional quantum-code distance or performance claims.

N1 remains exactly:

```text
UNSPECIFIED — CANNOT VALIDATE
```

The manuscript uses this only as a limitation statement and includes none of the unresolved `q=16`, `n=15`, or `32768=2^15` data as a reconstructed computational case. No factorization, twist, `k`, orbit structure, histogram, or numerical result was invented.

## 13. Section 10 computational-validation audit

The manuscript’s computational table retains the Phase-10C mixed-component test exactly:

```text
A = F_4 x F_16 over F_4,
m_1=1,
m_2=2,
n=5,
lambda=(omega,1),
k=1,
256 labeled selections.
```

It does not change the recorded results:

- 256 distinct canonical global code spaces;
- 256 global dual/nullspace checks;
- 256 global `F_4` dimension/hull checks;
- 1,280 affine-product shift checks;
- direct histogram equals component-product histogram;
- direct histogram equals orbit-boundary histogram;
- orbit-boundary histogram equals transfer histogram;
- uniform mean 3;
- uniform variance 2.

The Phase-10C capture remains the controlling computational evidence; the Phase-10D source audit adds no numerical claim.

## 14. Reproducibility audit

The manuscript identifies the finite-validation parameters, selection counts, validation scope, validator names, and capture location. It distinguishes direct validation from diagnostic-only incompatible cases and states that computations do not replace proofs.

The repository contains the referenced scripts under `code/` and the Phase-10C capture under `validation/`. Python source compilation passed during this audit. LaTeX and BibTeX reproducibility remains blocked solely by unavailable executables in the current environment.

## 15. Phase-10D verdict

**PASS WITH CONDITIONS — SOURCE AUDIT COMPLETE; ACTUAL TYPESETTING UNVERIFIED.**

The manuscript source is internally balanced, cross-referenced, scoped, and consistent with the frozen Phase-10C mathematics. The only unresolved Phase-10D publication check is an actual LaTeX/BibTeX run and inspection of its warnings, boxes, bibliography rendering, and final PDF, because no LaTeX toolchain is installed in this environment.

No compilation claim is made. Phase 10E/final review should run the standard compilation workflow in an environment with a genuine LaTeX toolchain, then check any remaining typesetting warnings and final bibliographic metadata against the existing literature audit.
