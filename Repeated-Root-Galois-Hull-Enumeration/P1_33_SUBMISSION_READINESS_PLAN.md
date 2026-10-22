# P1-33 — Submission Readiness Roadmap

**Baseline verified for this roadmap**

- Repository branch: `arena/ab8e330d-galios-hull`
- Current package commit: `a14a97d`
- Current manuscript source commit: `dfe1995d4b74c947df8c36b9d1f6d905a7d1660b`
- Current package: `Galios-Hull-Paper-Complete-Package-dfe1995.zip`
  - SHA-256: `147b144962e1daf80513683e9213260f0ac148584b3459d3e1daba3a2b6f80f4`
  - Packaged `.tex` and `.md` were verified byte-for-byte against the source at packaging time.
- Frozen blueprint: `02_THEOREM_BLUEPRINT.md`, SHA-256
  `ec2fd8d58f8d2a986314f83997d750d689f7c88e98ec8f87753ab4c9cf438cff` (unchanged).

This roadmap lists only work still remaining. It adds no new mathematical
result, does not reopen completed audits, changes no theorem or proof, and
makes no novelty or priority claim. Gate G1 remains **DEFERRED**.

## Responsibility split

| Owner | What can be done |
|---|---|
| **Arena now** | Maintain this roadmap and records; inspect an uploaded `.log`/PDF; make only minimal, reproducible compilation/layout fixes; perform the L1 comparison after a lawful full text is supplied; draft journal materials from verified facts; rebuild and verify the submission ZIP/manifest. |
| **Author / local system** | Run `pdflatex` on a TeX-equipped machine and upload the actual `.log` and PDF; visually proofread the rendered PDF; confirm journal choice; confirm factual declarations (funding, conflicts, contributions, ORCID, corresponding-author details). |
| **Lawful-access dependent** | Obtain the 2023 related paper (L1/DPI2023) through an author, institutional, library, or inter-library-loan channel. No paywall circumvention and no inference from abstracts. |

## A. Compilation and rendered-PDF review

| ID | Remaining task | Dependency | Owner | Exact deliverable | Objective completion criterion |
|---|---|---|---|---|---|
| A1 | Compile the current `.tex` twice with `pdflatex -interaction=nonstopmode -halt-on-error P1_15_MANUSCRIPT_DRAFT.tex`. | Current source at `dfe1995`. | Author / local system | Generated `.pdf` and complete `.log` from the second run, uploaded to the workspace. | Both runs finish with exit status 0; the uploaded log is from the current source; no unresolved LaTeX error remains. |
| A2 | Inspect the actual compiled PDF. | A1. | Author first; Arena after upload | A dated proofreading note or marked issue list covering page count, equations, margins/overfull displays, Theorem 8.4, Lemma 8.3, positioning table, EAQECC table, Examples 9.4 and 9.6, theorem/example numbering, cross-references, bibliography, title/author block, and page breaks. | Every listed item is checked against the rendered PDF; every issue found is either recorded as accepted or converted into a specific fix task. No visual claim is made from the `.tex` alone. |
| A3 | Fix only reproducible compilation/layout problems, if A1–A2 find any. | A specific error or visible defect from A1/A2. | Arena; author recompiles | Minimal source patch, a short fix note, rerun of affected validators, and a new author-side compile log/PDF. | The original error/defect no longer occurs in a fresh two-pass compile; mathematical statements and the frozen blueprint are unchanged. |
| A4 | Refresh the final package after the PDF review is closed. | A2, plus A3 if triggered. | Arena | Rebuilt final ZIP with regenerated `MANIFEST_SHA256.txt`. | Archive test passes; every manifest hash verifies; packaged `.tex`/`.md` match the then-current repository files byte-for-byte; no unverified or stale PDF is presented as the compiled paper. |

## B. Novelty — Gate G1 (DEFERRED)

| ID | Remaining task | Dependency | Owner | Exact deliverable | Objective completion criterion |
|---|---|---|---|---|---|
| B1 | Obtain a lawful, theorem-bearing full text of L1/DPI2023 (2023). | Author/institutional/library access. | Author, with Arena recording provenance | The lawful copy placed in the workspace, plus a provenance note giving source, date, version, and page range. | The copy is complete enough to cite theorem numbers and pages; acquisition did not rely on paywall circumvention. |
| B2 | Perform the theorem-level comparison for L1-Q1–Q6: length scope; hull formula; marginal versus joint counting; `B_i`/orbit bookkeeping; moments; finite-field versus product/affine scope. | B1. | Arena | Updated L1 extraction/comparison record and, if justified by quoted theorem text, an updated overlap matrix. | Each of L1-Q1–Q6 is answered from identified theorem/page evidence, or explicitly left unresolved with the missing evidence named; abstract-only inference is not used. |
| B3 | Re-vote Gate G1 and settle literature-positioning wording. | B2. | Author decision recorded by Arena | Dated Gate G1 decision note and, only if the decision requires it, minimal manuscript wording changes. | The decision follows the B2 evidence. Novelty, priority, or non-overlap is claimed only where the inspected theorem-level evidence supports the exact wording. |
| B4 | Correct comparative statements if B2 shows a conflict or duplication. | B2–B3. | Arena | Minimal cited correction to the introduction/positioning text, with validators rerun if numbering or references change. | No comparative sentence exceeds the evidence in B2; mathematical results are not altered without a separate proof review. |

Until B1–B3 are complete, the manuscript must continue to avoid novelty,
priority, and non-overlap claims relative to L1/DPI2023.

## C. Journal preparation

Journal selection and final submission preparation start only after A2 and
B3, because the target journal's rules and the permitted contribution wording
depend on both.

| ID | Remaining task | Dependency | Owner | Exact deliverable | Objective completion criterion |
|---|---|---|---|---|---|
| C1 | Select the target journal. | A2 and B3. | Author decision; Arena prepares the comparison | Shortlist with scope fit, article type/length limits, template, anonymity model, reference style, fees if any, and current indexing/quartile checked from the journal's official pages; one author-confirmed target. | One journal is selected from verified journal instructions; no suitability claim rests on unverified journal data. |
| C2 | Adapt the manuscript to the selected journal's format. | C1. | Arena; author recompiles | Journal-formatted source, separate title page or anonymised copy if required, and a fresh compile log/PDF. | The formatted source compiles twice without unresolved errors and satisfies the journal's stated file, anonymity, length, and reference requirements. |
| C3 | Prepare the cover letter. | B3 and C1. | Arena drafts; author approves | Cover letter file addressed to the selected journal. | It states the contribution accurately, contains no novelty/priority wording beyond the Gate G1 decision, and names the article type and any journal-required disclosures. |
| C4 | Prepare declarations and author metadata. | C1; author-supplied facts. | Author confirms; Arena drafts | Declarations for competing interests, funding, author contributions, data/code availability, generative-AI use if the journal requires it, plus ORCID/corresponding-author details as applicable. | Every factual statement is author-confirmed; nothing about funding, conflicts, identity, or contributions is invented. |
| C5 | Deposit or package the reproducibility materials. | A4; journal policy from C1. | Arena prepares; author approves/releases | Either a public code deposit with DOI/URL or a journal supplementary-material bundle containing the validators and saved outputs. | The cited DOI/URL or supplementary bundle resolves to the same validator files whose outputs are reported; the manuscript statement matches the actual deposit. |
| C6 | Build the final submission bundle. | C1–C5. | Arena | Final ZIP (and any separate journal upload files) with regenerated SHA-256 manifest. | Archive test passes; all manifest hashes verify; bundle contents match the journal checklist item-for-item; the included PDF, if any, is the actual compiled PDF from C2. |

## Current blockers

1. **Compilation blocker:** no compiled `.log`/PDF from source `dfe1995` has
   been reviewed; the preparation sandbox has no TeX compiler.
2. **Novelty blocker:** L1-Q1–Q6 remain unresolved at theorem level because no
   lawful full text of the 2023 related paper has been inspected. Gate G1 is
   **DEFERRED**.
3. **Submission blocker:** no target journal has been selected, and cover
   letter, declarations, author-confirmed metadata, and code/data deposit
   remain unprepared.

## Recommended next action

**Compile the current `.tex` twice on the author's TeX-equipped system and
upload the resulting `.log` and `.pdf` for the A2 rendered-PDF review.**
This is the shortest unblocking step: it requires no new research, changes no
mathematics, and converts the compilation status from assumed to evidenced.
