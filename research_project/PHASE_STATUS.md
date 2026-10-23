# PHASE STATUS

**Updated:** 2026-10-23 (UTC) · **Branch:** `arena/831a2e65-galios-hull`
· **Base commit:** `33aeb795a53e72d87856b6a255652c2acad41b0b`
· **Source of record:** Yadav, Singh, Islam, Prakash, Solé, *Comput. Appl. Math.*
**43** (2024) 269, DOI `10.1007/s40314-024-02789-1` — **designated by the user on
2026-10-23**; full text **not yet in hand** (`source_audit/SOURCE_ACCESS_STATUS.md`).
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
| 0.10 | Obtain the blueprint's named source paper | **BLOCKED** | 12 external access routes tried and closed; see `source_audit/SOURCE_ACCESS_STATUS.md` §2 |
| 0.11 | Repository-wide search for the PDF (working tree, all 11 branches, all 349 blobs, both ZIPs by magic bytes, whole filesystem) | **PASS as a search, negative as a result** | `source_audit/REPOSITORY_SOURCE_SEARCH.md`; gate output: 6 PDFs examined, 0 accepted, 2 distinct documents, neither is the source paper |
| 0.12 | Armed gate that accepts the file wherever it is placed | **PASS** | `tools/find_and_verify_source.py` (walks the tree, tests every PDF, records SHA-256, exit 0 only on exactly one acceptance) + `tools/verify_source_pdf.py --selftest` 3/3 |
| 0.13 | Phase 1 work specification written in advance | **PASS** | `source_audit/PHASE1_EXECUTION_PLAN.md`: entry conditions (including the version tag), the four deliverable schemas, evidence standard, failure-mode responses |
| 0.14 | Phase 1 machinery built and dry-run | **PASS** | `tools/extract_source_text.py` refuses a non-source PDF, and under `--force` extracts 27 pages / 34 heading candidates / 30 high-confidence, 4 needing triage — mechanics proven, output discarded to `/tmp` |
| 0.15 | One-command handoff from "PDF supplied" to "Phase 1 may start" | **PASS** | `tools/accept_source_and_prepare.sh`; negative test on the wrong PDF: staged copy removed, original untouched, drop folder left clean |
| 0.16 | Read-only readiness check | **PASS** | `tools/preflight.py` → 18 PASS / 3 WARN / 0 FAIL, `RESULT: WAITING`; also refuses to report READY while a Phase 1 deliverable exists without an accepted source |

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

**Update 2026-10-23 — decision recorded.** The user designated **Yadav et al.
(2024)** as the authoritative source. That resolves U-1 but not the *file*: the
article is not obtainable by this agent (publisher paywall; the single green-OA copy
at HAL is behind an interactive anti-bot challenge and the host is outside the
sandbox's egress allowlist). Per the blueprint's stop rule and the user's explicit
instruction, **Phase 1 has not started**. The required file and the two acceptable
filenames are specified in `source_audit/SOURCE_ACCESS_STATUS.md` §4.

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
| U-1 | Which paper is the source of record? | **RESOLVED 2026-10-23** | Yadav et al. designated authoritative; Debnath et al. excluded as a substitute |
| U-2 | Yadav et al. full text not in the workspace | **blocking** | Phase 1 cannot start; a verified PDF must be supplied (`SOURCE_ACCESS_STATUS.md` §4) |
| U-7 | Two non-identical versions exist (Springer version of record vs HAL author deposit; different corollary numbering) | versioning | every Phase 1 result must be tagged with its version; the version of record is preferred |
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

## Prepared for Phase 1 (nothing executed)

| Artefact | Purpose |
|---|---|
| `source_audit/PHASE1_EXECUTION_PLAN.md` | the Phase 1 specification: entry conditions, deliverable schema, evidence rules, failure responses |
| `tools/extract_source_text.py` | page-anchored corpus + draft heading index; refuses any non-source PDF |
| `tools/accept_source_and_prepare.sh` | one command: stage → identify → record SHA-256 → build corpus → preflight |
| `tools/preflight.py` | read-only readiness report (18 PASS / 3 WARN / 0 FAIL today; `RESULT: WAITING`) |
| `requirements.txt` | pinned Python dependencies |
| `source_paper/` | the drop point |

No Phase 1 deliverable exists, and `preflight.py` fails the build if one appears
before the source is accepted.

## Next step

**One action unblocks everything: place the PDF in `research_project/source_paper/`
(any `*.pdf` name) and run `python3 research_project/tools/find_and_verify_source.py --record`.**

The repository has now been searched exhaustively — working tree, all 11 remote
branches (349 blobs), both ZIPs entry-by-entry by magic bytes, and the entire
filesystem: six PDFs exist, and none is the Yadav et al. article
(`source_audit/REPOSITORY_SOURCE_SEARCH.md`).

Preferred — the version of record, saved as
`Yadav-2024-Hermitian-hull-CAM-43-269-Springer.pdf` in the repository root.
Acceptable — the author deposit, saved as
`Yadav-2024-Hermitian-hull-CAM-43-269-HAL-v1.pdf`; download it in an ordinary
browser from
`https://hal.science/hal-04825601v1/file/Hermitian%20hull%20of%20constacyclic%20codes%20and%20quantum%20Codes.pdf`
(the browser solves the anti-bot challenge; this sandbox cannot).

On arrival I run `python3 research_project/tools/verify_source_pdf.py <file> --record`
and, only if it returns ACCEPTED, start Phase 1 (theorem register, mathematical
audit, notation glossary, example recalculation).

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
