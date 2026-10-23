# PHASE STATUS

**Updated:** 2026-10-23 (UTC) · **Branch:** `arena/831a2e65-galios-hull`
· **Base commit:** `33aeb795a53e72d87856b6a255652c2acad41b0b`
**Vocabulary:** `PASS` · `FAIL` · `BLOCKED` · `PROVISIONAL` — each status names its evidence.
A document existing is never, by itself, evidence of a passed gate.

---

## Phase 0 — Workspace inspection and source integrity

| # | Blueprint requirement | Status | Evidence |
|---|---|---|---|
| 0.1 | Locate the exact uploaded PDF | **PASS** | `source_audit/SOURCE_INVENTORY.md` §1; `logs/phase0_evidence.out` §2–§4 |
| 0.2 | Record the source filename and SHA-256 | **PASS** | `Galios hulls of constacclic codes over affine algebra rings'.pdf`, 291 546 B, `0db90bfb…c039`; `FILE_MANIFEST.csv` row 1 |
| 0.3 | Identify the source unambiguously | **FAIL against the brief / PASS against the artifact** | the PDF is Debnath–Islam–Martínez-Moro–Prakash, arXiv:2412.08512v1 → *Discrete Math.* **349**(2) (2026) 114750. The blueprint names Yadav et al., CAM **43** (2024) 269. `SOURCE_PAPER_METADATA.md`; `SOURCE_IDENTITY_BLOCKER.md` |
| 0.4 | Inventory prior manuscripts, blueprints, audits, code, conflicting versions | **PASS** | `SOURCE_INVENTORY.md` §2–§3; `PRIOR_ART_REGISTER.md` (two streams, 155 + 102 files, 5 conflicts logged) |
| 0.5 | Verify archive integrity rather than assume it | **PASS** | `zipfile.testzip() is None` for both; 101/101 manifest entries re-hash; `logs/phase0_evidence.out` §3, §5 |
| 0.6 | Check availability of Python, Magma, finite-field libraries, LaTeX, bibliography tools, PDF utilities | **PASS** | `ENVIRONMENT_CAPABILITIES.md`; probes in `logs/phase0_evidence.out` §7 |
| 0.7 | Create a clean project directory; never infer a file from a planned name | **PASS** | `research_project/` created; every path in this report exists and is listed in §Deliverables below |
| 0.8 | Preserve original files | **PASS** | no root artifact modified or deleted; `git status` shows only the new `research_project/` tree; extraction was to a separate directory |
| 0.9 | Separate verified facts, unresolved issues, assumptions | **PASS** | `PROJECT_PLAN.md` §5–§6; §Unresolved below |

### Gate 0 verdict

> **BLOCKED.** The research environment is identified and usable (PASS), but the
> *exact source PDF named by the blueprint* is not present and cannot be obtained
> by this agent. The only PDF available is a different paper that cites the named
> one as reference [43].

The blueprint's Gate 0 wording is explicit: *"The exact source PDF and the usable
research environment are identified. If the PDF cannot be accessed, stop and
request it."* The condition is therefore not met on the source side, and the
blueprint's own instruction is to stop and request the document.

**Escalation:** `source_audit/SOURCE_IDENTITY_BLOCKER.md` §4–§7 (four options, one
recommendation, one question for the user).

## Phases 1–11

**Not started.** No Phase 1 artefact exists, no theorem register has been written
for either candidate source, and no novelty claim has been made. Phase 1 is
`BLOCKED` on the Gate 0 decision, not on capability: the paper that *is* present
is fully readable (27 pp., searchable text), so Phase 1 could start immediately
under Option 2 of the blocker document.

## What Phase 0 established (facts, not interpretations)

1. The repository contains exactly three tracked files and one commit; all three
   files open and hash cleanly.
2. The uploaded PDF is a 27-page arXiv v1 preprint of a published *Discrete
   Mathematics* article, with a complete text layer and correct internal metadata.
3. That PDF is **not** the paper named in the blueprint; it cites that paper as
   [43] and the named paper's full text is absent.
4. The named paper exists bibliographically (Springer, CAM 43:269, 2024-06-04,
   DOI `10.1007/s40314-024-02789-1`) but is paywalled; no open copy was found.
5. The two committed ZIPs contain a large prior body of work: a 102-file finished
   manuscript package (19-page PDF, byte-identical between archives, manifest
   101/101) and a 51-file later audit that declares the manuscript stage blocked
   and the novelty gate failed.
6. No LaTeX, Magma, Sage, GAP or PDF utilities are installed; Python 3.11.2 with
   `pypdf` is available, and `sympy`/`numpy`/`galois` can be installed from PyPI
   (session-local only).

## Unresolved issues

| ID | Issue | Type | Consequence |
|---|---|---|---|
| U-1 | Which paper is the source of record? | **blocking decision** | Phases 1–6 cannot be specified until resolved |
| U-2 | Yadav et al. full text inaccessible (paywall; no arXiv copy) | external | Phase 1 cannot audit Object C without the document |
| U-3 | Prior package's branch/commit (`arena/01a0c9d2…`, `360c1ef9…`) absent from this repo | provenance | prior work usable as content only, never as history |
| U-4 | Prior archive holds both a "completed" manuscript and an audit declaring that stage blocked | internal conflict | neither is authoritative; re-derivation required |
| U-5 | Published version of Object A (45 refs) differs from v1 (44 refs) | versioning | all Object A claims in this project must be tagged "arXiv v1" |
| U-6 | No LaTeX / CAS | environment | Phase 9 PDF and Phase 7 external CAS cross-check impossible; must be declared, not simulated |

## Assumptions currently relied upon

| ID | Assumption | Basis | Reversible? |
|---|---|---|---|
| A-1 | The PDF blueprint governs, not the 153 KB markdown blueprint in prior art | user instruction | no |
| A-2 | The uploaded PDF is the intended artifact even though it is not the named paper | it is the only research PDF supplied | yes — user may supply Object C |
| A-3 | Prior audits are inputs, not authority | project rule §3 of `PROJECT_PLAN.md` | no |
| A-4 | `prior_art/` may be excluded from Git because it is a byte-identical extraction of committed ZIPs | `FILE_MANIFEST.csv` | yes |

## Next step

**User decision required** (`SOURCE_IDENTITY_BLOCKER.md` §7):

1. supply Yadav et al. (2024) → Phase 1 audits Object C exactly as the blueprint
   specifies; or
2. authorise re-scoping to Debnath et al. (2024/2026) → Phase 1 audits Object A
   with a written deviation register; or
3. reframe around the F11 defect; or
4. stop at Phase 0.

No Phase 1 work will be started before that answer is recorded here.

---

## Deliverables produced in Phase 0

| Blueprint deliverable | Path | Bytes | SHA-256 |
|---|---|---:|---|
| `PROJECT_PLAN.md` | `research_project/PROJECT_PLAN.md` | 8 651 | `50ecc6be031f4d8d9a74257e2d84f4ef444b3b4244d5f4b8ff5dbb096496a499` |
| `SOURCE_INVENTORY.md` | `research_project/source_audit/SOURCE_INVENTORY.md` | 10 231 | `3e0a0d6162f1d9f061c33913410a74c5fc1a2a000f07e47b21860ea015db95eb` |
| `SOURCE_PAPER_METADATA.md` | `research_project/source_audit/SOURCE_PAPER_METADATA.md` | 7 116 | `4c1d77637a2ee3f9332cfe5497cbeb52c0a9bc43eb4be195fe59117dcddef3ac` |
| `ENVIRONMENT_CAPABILITIES.md` | `research_project/source_audit/ENVIRONMENT_CAPABILITIES.md` | 5 772 | `de4cb331f1db6dff257bef2b2c39eb2964dba0c451c0a38273964fe5af5cb654` |
| `PHASE_STATUS.md` | `research_project/PHASE_STATUS.md` | *(this file)* | hash recorded in `PHASE0_VERIFICATION_LOG.md` §13 (a file cannot contain its own hash) |

Supporting (not required by the blueprint, produced for evidence):
`source_audit/SOURCE_IDENTITY_BLOCKER.md`, `source_audit/PRIOR_ART_REGISTER.md`,
`source_audit/FILE_MANIFEST.csv`, `source_audit/PHASE0_VERIFICATION_LOG.md`,
`tools/inventory.py`, `tools/extract_prior_art.sh`, `logs/phase0_evidence.out`.
