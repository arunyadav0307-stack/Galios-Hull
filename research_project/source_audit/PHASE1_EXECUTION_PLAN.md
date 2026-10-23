# PHASE 1 EXECUTION PLAN (preparatory — no Phase 1 content yet)

**Prepared:** 2026-10-23 · **Status:** ready to execute; **blocked only on the source PDF**
**Governing text:** blueprint, Phase 1 (§1A extraction, §1B checks) and Gate 1.

This document fixes *how* Phase 1 will be done, so that when the Yadav et al. PDF
is accepted nothing has to be improvised. It contains no mathematics about the
paper and makes no claim about it. `PROJECT_PLAN.md` holds the phase table; this
file holds the Phase 1 work specification only.

---

## 1. Entry condition (all three must hold)

| # | Condition | Checked by |
|---|---|---|
| E-1 | A PDF in the repository passes the identity test for DOI `10.1007/s40314-024-02789-1` | `tools/find_and_verify_source.py` → `GATE 0: PASS` |
| E-2 | Its SHA-256 is recorded in `source_audit/SOURCE_PDF_MANIFEST.csv` | `--record` flag |
| E-3 | Its **version** is stated: version of record (Springer) or author deposit (HAL `hal-04825601v1`) | manual, recorded in the manifest's notes column |

E-3 is not optional. The publisher abstract numbers "Corollaries 2 and 3" and
"Theorems 8 and 9"; the HAL deposit's abstract numbers "Corollaries 3.2 and 3.3".
A theorem register built without a version tag would silently mix two documents.

## 2. Corpus step (mechanical, runs first)

```bash
python3 research_project/tools/extract_source_text.py
```

Produces, under `source_audit/source_text/` (git-ignored, regenerable):

| File | Content |
|---|---|
| `pages/page_NNN.txt` | text of page NNN, exactly as extracted |
| `PAGE_INDEX.csv` | page, characters, lines, empty-flag |
| `HEADING_INDEX.csv` | every line beginning Theorem / Lemma / Proposition / Corollary / Definition / Example / Remark / Table / Algorithm, with page, kind, number and a `confidence` flag (`high` = a number was parsed, `low` = needs manual triage) |
| `CORPUS_META.txt` | source path, SHA-256, page count, PDF metadata, and the DRAFT stamp |

`HEADING_INDEX.csv` is a **finding aid**, not a result: it is line-level pattern
matching and will contain false positives (running text beginning "examples of…",
cross-references such as "Table [15]"). Every entry must be opened and read before
it is entered in the register.

## 3. Deliverable specifications (blueprint §1A/§1B)

### 3.1 `SOURCE_THEOREM_REGISTER.md`

One entry per numbered statement in the paper. Required fields, no omissions:

| Field | Rule |
|---|---|
| `ID` | `S1-T5` = source paper, Theorem 5. Use the paper's own numbering, and record the version tag. |
| `Kind` | theorem / lemma / proposition / corollary / definition / example / remark / table |
| `Page` | the PDF page of the *statement* (and of the *proof* if elsewhere) |
| `Verbatim statement` | quoted, with the paper's own symbols; no paraphrase in this field |
| `Hypotheses` | every hypothesis, including inherited global assumptions (`e` divides `q+1`, order of `α_l`, `gcd(n,p)`, characteristic, ring relations) |
| `Conclusion` | the mathematical content in one sentence |
| `Proof method` | CRT decomposition / idempotents / generator polynomials / conjugation-reciprocal / counting / Gray map / direct computation / none |
| `Classification` | possible dimensions / exact counts / LCD / dual-containing / Gray map / quantum parameters / structural |
| `Uses in this project` | which later phase may rely on it, or "none" |
| `Status` | `VERIFIED` (re-read against page and re-derived where feasible), `QUOTED` (read, not independently checked), `UNCLEAR` (ambiguity found), `SUSPECT` (conflicts with another statement) |

A register entry with an empty hypothesis field is a defect, not a shortcut.

### 3.2 `SOURCE_MATHEMATICAL_AUDIT.md`

The §1B checklist, each item with verdict and evidence:

1. ring decomposition and its assumptions (does $\mathcal R_e$ really split as the paper says? under exactly which hypotheses?)
2. idempotents $\eta_l$ and their properties
3. generator-polynomial structure: factorisation of $x^n-\alpha_l$, multiplicities, conjugate-reciprocal pairs
4. hull-dimension formula: derivation re-done independently
5. Hermitian LCD criterion: is it necessary, sufficient, or both?
6. dual-containing conditions
7. the Gray map: well-definedness, injectivity, length, dimension, and **whether it preserves what is claimed of it** (the blueprint forbids assuming distance or hull behaviour is preserved)
8. unclear or unverified arguments, listed explicitly
9. internal conflicts between statements

Verdict vocabulary per item: `CONFIRMED` · `CONFIRMED WITH CORRECTION` · `UNVERIFIED` · `CONTRADICTED` · `NOT APPLICABLE`.

### 3.3 `SOURCE_NOTATION_GLOSSARY.md`

Every symbol the paper uses, with: symbol, meaning, domain (field/ring/set), scope of
quantifiers, first page of use, and any overload (e.g. is `e` the ring exponent or the
field degree? is `m` the same in every section?). Overloads are recorded, not
resolved silently.

### 3.4 `SOURCE_EXAMPLE_RECALCULATION.md`

For each worked example and each table row:

| Field | Rule |
|---|---|
| Example/row | the paper's label |
| What the paper asserts | verbatim numbers |
| Recomputation | exact arithmetic, code or hand, recorded |
| Agreement | `MATCH` / `MISMATCH` / `NOT REPRODUCIBLE` |
| Script | path under `code/` if computed |
| Note | any assumption needed to reproduce the number |

A mismatch is reported as a finding, never adjusted to fit.

## 4. Evidence standard for every Phase 1 claim

* Every factual sentence carries `p.N` (PDF page) and, where useful, the quoted
  fragment.
* Computations are reproducible: the script and its output are stored, and the
  command is in the document.
* Where a statement could not be checked, it is marked `UNVERIFIED` with the reason.
* No claim rests on the Debnath et al. preprint, on the prior `k`-Galois manuscript,
  or on any prior audit document. Those are Phase 2 material at the earliest, and
  only as related work.

## 5. Explicitly out of scope for Phase 1

* no enumerator, no generating function, no novelty statement, no literature
  comparison, no quantum-code construction;
* no correction or improvement of the paper's results;
* no manuscript text.

Gate 1 is passed when the register is complete, the audit's §1B items each have a
verdict with evidence, and the glossary and example recalculation are consistent
with the register — not when the files exist.

## 6. Failure modes anticipated, with the response

| Situation | Response |
|---|---|
| Only the HAL author version is supplied | proceed, tag every entry `HAL-v1`, and mark any statement that depends on numbering as `VERSION-DEPENDENT`; the version of record is still wanted for Phase 10 |
| A number in the paper cannot be reproduced | record `MISMATCH`, keep both numbers, do not "fix" either |
| A proof step is unjustified | record it as `UNVERIFIED` with the exact step, and continue; it becomes input to Phase 2/5 |
| PDF text extraction is garbled (ligatures, split formulas) | quote from the page image side by side, note extraction defects in the register entry |
| The paper's hypotheses differ from the blueprint's summary of them | the paper wins; record the difference in `SOURCE_MATHEMATICAL_AUDIT.md` §1 and flag it for the Gate 1 report |

## 7. Command sequence when the PDF arrives

```bash
cd /home/user/Galios-Hull
bash research_project/tools/accept_source_and_prepare.sh /path/to/yadav.pdf
#   -> stages, identifies, records SHA-256, builds the corpus, runs preflight
# then, by hand:
#   state the version in SOURCE_PDF_MANIFEST.csv
#   write SOURCE_THEOREM_REGISTER.md  (Phase 1 §1A)
#   write SOURCE_MATHEMATICAL_AUDIT.md, SOURCE_NOTATION_GLOSSARY.md,
#         SOURCE_EXAMPLE_RECALCULATION.md  (Phase 1 §1B)
#   run preflight again; report Gate 1
```

`preflight.py` refuses to report READY while any Phase 1 deliverable exists without
the source PDF, and reports the gate state without recording anything.
