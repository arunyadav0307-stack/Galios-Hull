# PHASE_STATUS

**Last updated:** 2026-10-20 (UTC) · **Branch:** `arena/1625045b-galios-hull`
**Status vocabulary:** PASS · FAIL · BLOCKED · PROVISIONAL. A status is assigned only
where evidence exists, and every row names the evidence.

---

## Phase 0 — Workspace inspection and source integrity

| Requirement | Status | Evidence |
|---|---|---|
| Locate the exact uploaded PDF | **PASS** | source `0db90bfb…c039`, 291 546 B, 27 pp; blueprint `abcecc47…ae23`, 7 pp |
| Record filename and hash | **PASS** | `SOURCE_INVENTORY.md` §1–2 |
| Identify the source unambiguously | **FAIL on the brief, PASS on the artifact** | The brief names Yadav et al. (2024); the PDF is Debnath–Islam–Martínez-Moro–Prakash, arXiv:2412.08512v1 → *Discrete Math.* **349**(2) (2026) 114750. `SOURCE_PAPER_METADATA.md` §2 |
| Inventory prior manuscripts | **PASS** | `SOURCE_INVENTORY.md` §3 |
| Check tool availability | **PASS** | `ENVIRONMENT_CAPABILITIES.md`: Python 3.11.2, `pypdf` 6.21.1; **no Magma, Sage, GAP, LaTeX, sympy, numpy** |
| Create a clean project directory | **PASS** | `research_project/`; originals re-hashed and unchanged |
| No file inferred from a planned name | **PASS** | every cited path created by an explicit tool call |

**Gate 0: PASS**, with the bibliographic mismatch escalated.

---

## Phase 1 — Complete source-paper audit

| Requirement | Status | Evidence |
|---|---|---|
| Extract every numbered result | **PASS** | `SOURCE_THEOREM_REGISTER.md`: 10 theorems, 9 lemmas, 5 corollaries, 2 remarks, 3 examples, 1 table; counts check mechanically |
| Record hypotheses, notation, consequences | **PASS** | register + `SOURCE_NOTATION_GLOSSARY.md` |
| Verify the ring decomposition | **PASS** | p.4–5 re-read; §3.1 of the verification report gives a self-contained proof that `A ≅ F_{q²}⊕F_{q²}` in the paper's own examples |
| Check generator polynomials and `#` | **PASS** | all factorisations reproduced |
| Check the hull-dimension formula | **PASS with restatement** | Theorem 8 is correct as `Σ_S dim_{A_S}`; its label `q-dimension` is wrong when `|S(ν)|>1` |
| Check LCD / dual-containing criteria | **PASS** | `[S1]` Thm 6 is componentwise |
| Check the Gray-map properties | **FAIL** for arXiv v1 | `ψ : A → F_q^{|Ŝ|}` cannot be bijective: `|A| = q^4`, `|F_q^2| = q^2` |
| Recalculate the examples | **PASS** | `SOURCE_EXAMPLE_RECALCULATION.md`, `verification/` |
| Identify unverified arguments | **PASS** | F2–F5, F8, F9, F11 |

**Gate 1: PASS** (the mathematics is understood), with one **M-level defect** (F11).

---

## Phase 1B — Independent computational verification

| Test | Status | Evidence |
|---|---|---|
| Example 1 idempotents | **PASS** | `verification/verify_example1.out` |
| Examples 2–3 arithmetic | **PASS (within the paper's component model)** | `verification/verify_examples.out`; scope now stated |
| Corollary 3.5(1) | **PASS** — model-correct (`x²−1` splits) | `verification/verify_corollary_3_5.out`, Test 1 |
| Corollary 3.5(2) | **PASS in the `F_q`-model; FALSE as printed at `e'=0`** | Test 2 + `verification/independent_verification.out` PART D |
| Product factorisation | **PASS** | Test 3 |
| **Independent re-derivation from scratch** | **PASS** | `verification/independent_verification.out` — explicit algebra, real `A`-module, ALL CHECKS PASS |
| Magma cross-check | **BLOCKED** | unavailable |
| Table 1 (13 rows) | **PARTIAL** | 2 rows verified; 11 not |

---

## Phase 2 — Literature and novelty

| Requirement | Status | Evidence |
|---|---|---|
| Comparison matrix | **PASS** | 19 matrix entries; 31 verified references, now including the mass-formula and isometry-class lines |
| Read complete statements where possible | **PARTIAL** | 5 full texts, 13 abstracts, 8 metadata-only — disclosed |
| Check the constituent decomposition | **PASS** — standard | `[S1]` Thm 2/3 |
| Check the local enumerator | **PASS** — exists | `[D23]`, `[SJL15]` |
| Check enumeration over product rings | **PASS** — exists | `[S25]` (AMC **20** (2026) 209–238), `[GWF23]`, `[DP25b]`, `[LGM25]` |
| Check hull-constrained mass formulas | **PASS** — exist | Li–Shi ITT **70** (2024); Li–Shi–Ling ITT **71** (2025) 273–286 |
| Check isometry classes of constacyclic codes | **PASS** — exist | Chen–Fan–Lin–Liu FFA **18** (2012); *Cryptogr. Commun.* (2024) |
| Reference metadata verification | **PASS**, with two corrections | A1 (DOI), A2 (volume) |

**Gate 2: FAIL for the joint enumerator.** It is a product of known local results.
The gate is **not** failed for the whole area — one narrow intersection remains (§C1 of
the decision document).

---

## Phase 2.5 — Independent verification and direction decision (this turn)

| Requirement | Status | Evidence |
|---|---|---|
| Reopen the PDF and check F11, CRT, Gray map, quantum parameters at exact loci | **PASS** | `INDEPENDENT_VERIFICATION_REPORT.md` §1–§2, page-referenced |
| Distinguish contradiction from interpretation | **PASS** | three proven contradictions, three labelling issues, one undecidable |
| Independently verify literature precedents | **PASS** | §4; all from publisher pages, none copied from `[S1]` |
| Version-of-record comparison | **BLOCKED** | paywall; §5 |
| Audit own deliverables and scripts | **PASS** | §6; six errors found in our own record, all corrected |
| Decision document | **PASS** | `RESEARCH_DIRECTION_DECISION.md` |
| Final independent check (Tasks A/B/C) | **PASS with two corrections to our own record** | `FINAL_INDEPENDENT_MATHEMATICAL_CHECK.md`; `verification/final_check_A.out`, `verification/final_check_B.out`. Confirms the `F_4` Euclidean witness, **retracts** the `F_4` Hermitian claim, adds an `F_9` Hermitian witness (`2 → 0`), and re-derives F11 at component level. |
| Screening of C1's formulation (risk R1) | **PASS — negative result** | `C1_ISOMETRY_SCREENING.md`; `verification/isometry_hull_screening.out`, exit 0. The Galois hull dimension is **not** a class function on isometry classes, so the naive C1 count is ill-posed. |

---

## Phases 3–11

**BLOCKED.** The blueprint permits stopping when the novelty gate fails. No
`MATHEMATICAL_FRAMEWORK.md`, no `MAIN_THEOREMS_AND_PROOFS.md`, no `paper/main.tex`,
no PDF. Nothing pushed to Git.

---

## Unresolved issues

| ID | Issue | Why unresolved | Consequence |
|---|---|---|---|
| R-1 | Version of record of `[S1]` (*Discrete Math.* 349(2) 2026, 114750) — **body** unread | paywall | **Partially inspected 2026-10-20** (`verification/VOR_INSPECTION_2026-10-20.md`): abstract, full introduction and section snippets read; the version is materially longer than v1 (+Example 4, +Table 2, 45 refs) and **retains the "`q`-dimension" framing**. The body sentence that decides F11 was not seen; source-level comparison remains **BLOCKED**; **C3 cannot start** |
| R-2 | Full text of `[D23]` unread | paywall | the "restrictions on `q`" remain unknown (O2 stays **U**) |
| R-3 | Full texts of `[S25]`, Li–Shi–Ling, chain-ring isometry (2024) | paywall | caps C1's novelty evidence |
| R-4 | No Magma/Sage/GAP | environment | computations are self-written; validated against published numbers, but a CAS re-run is desirable |
| R-7 | C1's surviving formulations F1/F2 untested for content | not yet attempted | a one-week check decides whether C1 is abandoned |
| R-5 | No LaTeX | environment | no typeset artifact |
| R-6 | F11 needs the authors' or an editor's decision | outside our control | affects every quantum parameter in `[S1]` |
| R-7 | Decision on a correction note | **BLOCKED** on `§2` of the published article | see `FINAL_GO_NO_GO_DECISION.md` §6 and `FINAL_F11_VERIFICATION_LOG.md`: seven access routes tried and closed; one sentence decides it; the missing evidence is itemised in §1.1 of the log and six routes to it in §1.2 |

---

## Next step

A **user decision**, informed by `RESEARCH_DIRECTION_DECISION.md`:

1. obtain the version of record (blocks everything);
2. if the defect survives → **C3**, a short correction note;
3. if it does not → **C1** only in one of its two surviving formulations (F1:
   `Sim_k`-classes; F2: orbit/statistic pairs), and only after a one-week check that
   either produces a number that is not a restatement of an enumeration count.
   R1 is settled: the naive version ("count up to isometry") is ill-posed.

No manuscript until one of these produces a theorem.

---

## Deliverable index

| Phase | File |
|---|---|
| 0 | `SOURCE_INVENTORY.md`, `SOURCE_PAPER_METADATA.md`, `ENVIRONMENT_CAPABILITIES.md`, `PROJECT_PLAN.md` |
| 1 | `SOURCE_THEOREM_REGISTER.md`, `SOURCE_MATHEMATICAL_AUDIT.md`, `SOURCE_NOTATION_GLOSSARY.md`, `SOURCE_EXAMPLE_RECALCULATION.md` |
| 2 | `literature/LITERATURE_REVIEW.md`, `literature/LITERATURE_COMPARISON_MATRIX.csv`, `literature/NOVELTY_ASSESSMENT.md`, `literature/REFERENCE_VERIFICATION_REPORT.md`, `literature/LITERATURE_MAP.md`, `literature/CITATION_LEDGER.md` |
| 2 verdict | `JOINT_ENUMERATOR_FEASIBILITY.md` |
| 2.5 | **`INDEPENDENT_VERIFICATION_REPORT.md`**, **`RESEARCH_DIRECTION_DECISION.md`**, **`C1_ISOMETRY_SCREENING.md`**, this file |
| 2.6 | **`FINAL_INDEPENDENT_MATHEMATICAL_CHECK.md`** — Tasks A, B, C: calculations, scripts, outputs, exact loci, limitations, recommendation |
| compute | `code/gf.py`, `code/independent_verification.py`, `code/verify_*.py`, `verification/*.out` |
