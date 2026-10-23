# PHASE STATUS

**Updated:** 2026-10-23 · **Branch:** `arena/831a2e65-galios-hull`
· **Base commit:** `33aeb795a53e72d87856b6a255652c2acad41b0b`
· **Source of record:** Yadav, Singh, Islam, Prakash, Solé, *Hermitian hull of constacyclic codes over a class of non-chain rings and new quantum codes*, *Comput. Appl. Math.* **43**, art. 269 (2024), DOI `10.1007/s40314-024-02789-1`.
· **Version examined (binding): `hal-04825601v1`** — HAL author deposit, 23 pp., SHA-256 `7f7e6803dffe8d42912c506cc0b6d8910187be169e14c869f3275d896c27d249`, staged at `source_paper/Hermitian hull of constacyclic codes and quantum Codes.pdf`.

**Vocabulary:** `PASS` · `FAIL` · `BLOCKED` · `PROVISIONAL` — each status names its evidence. A document existing is never, by itself, evidence of a passed gate.

---

## Gate summary

| Gate | Blueprint condition | Status | Evidence |
|---|---|---|---|
| **Gate 0** | "The exact source PDF and the usable research environment are identified. If the PDF cannot be accessed, stop and request it." | **PASS** (2026-10-23) | `GATE 0: PASS` from `tools/find_and_verify_source.py` over 7 PDFs with exactly 1 acceptance; SHA-256 + version recorded in `source_audit/SOURCE_PDF_MANIFEST.csv`; identity cross-checked against the HAL record, the DOI record and the publisher landing page (`SOURCE_PAPER_METADATA.md`) |
| **Gate 1** | "Central source-paper results and the assumptions needed for the new work are understood and documented." | **PASS** (2026-10-23) | four required deliverables written (`phase1/SOURCE_*.md`); 25/25 register entries; 33/33 table rows and 31/31 example checks recomputed exactly; 11/11 audit items recorded |
| Gate 2 | "The proposed main contribution is distinguishable from the closest known results." | **PASSED on R4 — distinguishable, not novel** (2026-10-23) | three novelty tests run in `phase2/NOVELTY_ASSESSMENT.md`; constituent enumerator classified **K** (exact field-level counts already exist: Debnath–Prakash 2022/23, Sangwisut et al. 2015, Lu et al. 2026, arXiv:2605.29204); joint/total enumerators **N2 at best** because CRT multiplicativity makes them a product of the constituent laws; three surviving revisions R1/R2/R3 identified, each at most **N2** and each with a stated kill criterion |

---

## Phase 0 — Workspace inspection and source integrity (COMPLETE)

Executed earlier in this session; full log in `source_audit/PHASE0_VERIFICATION_LOG.md` (including the §18 recovery record and its correction). Condensed, with two statuses revised by later events:

| # | Blueprint requirement | Status | Evidence |
|---|---|---|---|
| 0.1 | Locate the exact uploaded PDF | **PASS** | `source_audit/SOURCE_INVENTORY.md` §1 |
| 0.2 | Record source filename and SHA-256 | **PASS** | `source_audit/FILE_MANIFEST.csv`; per-document hashes in `SOURCE_PDF_MANIFEST.csv` |
| 0.3 | Identify the source unambiguously | **PASS after correction** | Originally the only PDF present was Debnath et al. (arXiv:2412.08512v1) — **not** the source paper. The verifier rejects it decisively (`REJECTED — impersonator`). The Yadav et al. deposit supplied later is `ACCEPTED`. |
| 0.4 | Inventory prior manuscripts, blueprints, audits, code, conflicting versions | **PASS** | `SOURCE_INVENTORY.md` §2–§3; `PRIOR_ART_REGISTER.md` (155 + 102 files, 5 conflicts) |
| 0.5 | Verify archive integrity rather than assume it | **PASS** | `zipfile.testzip() is None` for both ZIPs; 101/101 manifest entries re-hashed |
| 0.6 | Check availability of Python, Magma, finite-field libraries, LaTeX, bibliography tools, PDF utilities | **PASS** | `ENVIRONMENT_CAPABILITIES.md`; current preflight in a **clean tree**: **20 PASS / 2 WARN / 0 FAIL** (WARN: `pdflatex`, `magma`); the working-tree check adds a third WARN while files are uncommitted, giving 19/3/0 — 22 checks in total either way |
| 0.7 | Create a clean project directory; never infer a file from a planned name | **PASS** | `research_project/` |
| 0.8 | Preserve original files | **PASS** | no root artifact modified or deleted; the source PDF was staged *into* the project tree, never replacing anything |
| 0.9 | Separate verified facts, unresolved issues, assumptions | **PASS** | `PROJECT_PLAN.md` §5–§6; §Unresolved below |
| 0.10 | Obtain the blueprint's named source paper | **PASS** (was `BLOCKED`) | unblocked on 2026-10-23 by the user supplying the HAL deposit; access history in `SOURCE_ACCESS_STATUS.md` |
| 0.11 | Repository-wide search for the PDF | **PASS as a search, negative as a result** | `REPOSITORY_SOURCE_SEARCH.md`: 6 PDFs, 0 accepted, 11 branches, 349 blobs, both ZIPs by magic bytes, whole filesystem |
| 0.12 | Armed gate that accepts the file wherever placed | **PASS** | `tools/find_and_verify_source.py`; selftest 3/3 |
| 0.13 | Phase 1 specification written in advance | **PASS** | `source_audit/PHASE1_EXECUTION_PLAN.md` |
| 0.14 | Phase 1 machinery built and dry-run | **PASS** | `tools/extract_source_text.py` |
| 0.15 | One-command handoff "PDF supplied → Phase 1 may start" | **PASS** | `tools/accept_source_and_prepare.sh` — used for the real acceptance |
| 0.16 | Read-only readiness check | **PASS** | `tools/preflight.py` → 20 PASS / 2 WARN / 0 FAIL → `READY — source PDF accepted and all four Phase 1 deliverables present.` |
| 0.17 | Non-destructive validation of the pipeline | **PASS after repair** | `tools/selftest_gate.py` **7/7** |

**Defects found and fixed in Phase 0** (kept as audit trail): D-1 manifest row inflation (fixed by dedupe on `(SHA-256, verdict)` + atomic rewrite); D-2 `preflight.py` directory side effect and path display; D-3 flag shadowing `record`/`record()` in `preflight`-era code; **D-3′ a second instance of the same shadowing in `find_and_verify_source.py:58`**, hit during the real acceptance and fixed (`record` → `do_record`).

---

## Phase 1 — Complete source-paper mathematical audit (COMPLETE)

### What was actually done, in order

1. **Source staged and accepted.** `tools/accept_source_and_prepare.sh` → `GATE 0: PASS`; manifest row written with version tag; corpus built.
2. **Corpus built.** `tools/extract_source_text.py` → 23 page files (`source_audit/source_text/pages/page_002.txt … page_023.txt`, git-ignored, regenerable), 0 empty pages, 24 heading lines (12 theorem / 5 lemma / 4 corollary / 3 example), 23 high-confidence + 1 low-confidence. The extraction tool was extended with a `version` column (`verify_source_pdf.py`, 3 insertions / 2 deletions) and re-passed selftest 7/7.
3. **The whole article was read** (pp.2–23), and every statement was re-read against its page before entering the register.
4. **Independent recomputation** with exact finite-field arithmetic (`galois` over `GF(p²)`, no Magma): `code/gfcore.py` (field, Hermitian dual, hull, exact minimum distance, conjugate-reciprocal map), `code/phase1_examples.py`, `code/phase1_tables.py`, `code/phase1_audit.py`.
5. **Four deliverables written** (below), then the low-confidence heading triaged, then this status.

### Deliverables (blueprint §1A/§1B)

| Deliverable | Path | Content |
|---|---|---|
| `SOURCE_THEOREM_REGISTER.md` | `research_project/phase1/` | 25 entries (19 numbered statements + 3 examples + 3 tables) with verbatim text, hypotheses, conclusion, proof method, classification, uses and status; 20 `VERIFIED`, 5 `QUOTED`, 0 `UNCLEAR`, 0 `SUSPECT` |
| `SOURCE_MATHEMATICAL_AUDIT.md` | `research_project/phase1/` | the nine §1B items with verdicts and evidence, plus 9 explicit unclear/unverified arguments and 5 recorded internal conflicts |
| `SOURCE_NOTATION_GLOSSARY.md` | `research_project/phase1/` | every symbol with domain, quantifier scope and first page, plus a **10-row overload register** |
| `SOURCE_EXAMPLE_RECALCULATION.md` | `research_project/phase1/` | Examples 1–3 and all 33 table rows, field by field, with method and verdict |

Supporting evidence (regenerable, committed):
`code/{gfcore,phase1_examples,phase1_tables,phase1_audit}.py`,
`phase1/raw/{examples_log.txt,audit_log.txt,tables_recalc.json,audit_results.json}`.

### Verification results

| Check | Result | Reproduce |
|---|---|---|
| Examples 1–3 + Gray matrices `MM* = νI` | **31/31 PASS** | `python3 research_project/code/phase1_examples.py` |
| Tables 1–3, every row (length, dimension, **exact** minimum distance, hull, dual-containing, quantum parameters, Singleton residual) | **33/33 PASS** | `python3 research_project/code/phase1_tables.py` |
| §1B structural audit, items 1–7 | **11/11 checks CONFIRMED** — the nine §1B items, with the ring decomposition run in 5 configurations (one item, A2, carries a normalisation correction) | `python3 research_project/code/phase1_audit.py` |

Highlights that carry real weight:

* `x¹²−1`, `x¹⁴−12`, `x⁶−4` each equal the product of the paper's printed factors **exactly**; every printed conjugate-reciprocal pairing confirmed with the paper's own `p^†`; the three printed generators confirmed as products of the printed factors.
* Example 2's `[28,25,4]₁₃²` and the MDS quantum code `[[28,22,≥4]]₁₃` — the strongest claim in the paper — reproduced with **exact** distance 4 and Singleton residual 0.
* The hull-dimension formula tested against linear algebra on 220 divisors, **exhaustively** over all 4096 divisors of `x¹²−1` (attained exactly `{0,1,2,3}`, matching Corollary 9's bound 3), and the `R₂` bound 6 attained by direct computation.
* The Hermitian-LCD iff (`n·r ∈ S_{q²}`) tested on four `(n,r)` cases, holding in all four.
* The dual-containing iff tested in both directions, including the violating configuration.

### Findings (recorded, not "fixed")

| ID | Finding | Effect |
|---|---|---|
| F-1 | The printed `η_i = (u^e−1)/(u−μ^{i−1})` are **not** idempotents for `e = 3`: `Ση_i = 3u² ≠ 1`; each is a nonzero scalar multiple (`8, 3, 24` in Example 3) of a genuine idempotent | **none** — every use is `η_i C_i` with `F_{q²}`-linear `C_i`, so the scalar is absorbed. `R₂` is normalised correctly. Marked `CONFIRMED WITH CORRECTION` |
| F-2 | Example 3 writes "`C₃ = ⟨g₂(x)⟩`" where `g₃ = x+t¹⁰` was just defined and the dimension `4+5+5 = 14` requires `g₃` | **none** — typographical; recomputed with `g₃` and reproduced exactly |
| F-3 | `nr` in Theorem 11 / Corollaries 12, 14 is printed without a multiplication sign | read as the product `n·r`; established by the proof's own wording and by four numerical tests (the quotient reading fails them) |
| F-4 | The γ/β "discrepancy" suspected earlier in this session is **retracted**: the paper's formula is correct and reproduces its own totals (6 and 3); the fault was an incorrect totient in my helper | none; the retraction is recorded so the claim cannot resurface |
| F-5 | Table 3's "Remark / Comparison" column (`New`, `Optimal [11]`, …) refers to references [3], [11], [14] | **`UNVERIFIED`, out of Phase-1 scope**; neither used nor adjusted |

**No numbered statement is flagged `SUSPECT`. No reported parameter of the paper failed to reproduce.**

**Low-confidence heading triaged:** `HEADING_INDEX.csv` line `page 6, kind Theorem, number empty, "theorem."` is a **false positive** — the tail of the sentence "…can be obtained by the next theorem." (p.6). Tables 1–3 are *missing* from the heading index because the extractor renders the caption `T able 1`; all three were added by hand from pp.17–19. Both facts are recorded in the register.

---

## Unresolved issues

| ID | Issue | Type | Consequence |
|---|---|---|---|
| U-1 | Which paper is the source of record? | **RESOLVED 2026-10-23** | Yadav et al. designated authoritative; Debnath et al. excluded as a substitute |
| U-2 | Yadav et al. full text not in the workspace | **RESOLVED 2026-10-23** | HAL deposit `hal-04825601v1` supplied, accepted, SHA-256 recorded |
| U-7 | Two non-identical versions exist (Springer version of record vs HAL deposit — different corollary/theorem numbering) | versioning | every Phase 1 result is tagged `hal-04825601v1`; the register states that publisher numbering is **not** interchangeable |
| U-8 | The version of record was never examined; only the HAL author deposit | versioning | Phase 1 conclusions hold **for `hal-04825601v1` only**. If the version of record differs in a statement or a table entry, that phase must be re-run on it. Not currently blocking, because every number verified here comes from the deposit. |
| U-3 | Prior package's branch/commit absent from this repo | provenance | prior work usable as content only, never as history |
| U-4 | Prior archive holds both a "completed" manuscript and an audit declaring that stage blocked | internal conflict | neither is authoritative; re-derivation required |
| U-5 | Published version of Object A (45 refs) differs from v1 (44 refs) | versioning | all Object A claims must be tagged "arXiv v1" |
| U-6 | No LaTeX, no Magma, no Sage/GAP | environment | Phase 9 PDF and the CAS cross-check of Phase 7 cannot be run here; declared, not simulated. Phase 1 is unaffected — `galois` provided an independent exact check, which is stronger than repeating Magma. |

## Assumptions currently relied upon

| ID | Assumption | Basis | Reversible? |
|---|---|---|---|
| A-1 | The PDF blueprint governs, not the markdown blueprint in prior art | user instruction | no |
| A-3 | Prior audits are inputs, not authority | `PROJECT_PLAN.md` §3 | no |
| A-4 | `prior_art/` may be excluded from Git (byte-identical extraction of committed ZIPs) | `FILE_MANIFEST.csv` | yes |
| A-5 | The corpus `page_NNN.txt` text is a faithful (if layout-flattened) rendering of the PDF | extractor output checked against page images for dense formula pages (pp.8–9, 13–14) | yes — a re-extraction would be needed if a formula's reading were disputed |
| A-6 | `hal-04825601v1` is the same *mathematical content* as the version of record | identical title/authors/DOI and identical abstract modulo numbering; **not verified page-by-page** | no until the version of record is examined (U-8) |

---

## Scope compliance for this run

The blueprint's closing instruction is: *"Execute Phase 0 and Phase 1 only. … Do not draft the new paper or claim novelty. Verify every deliverable exists, report exact paths and unresolved issues, and stop after reporting the Phase 1 status."*

* Phase 2 (related literature and novelty audit) had **not** been started at that point; it was authorised and executed afterwards — see §Phase 2 below. No novelty claim is made anywhere in the project.
* No manuscript text, no enumerator, no generating function, no new theorem.
* No original file was overwritten, and the corrected §18 recovery record in `PHASE0_VERIFICATION_LOG.md` is intact.
* The source paper's own numbers were never adjusted to fit a computation, and no computation was adjusted to fit the paper.

## Final Phase 1 consistency check (2026-10-23, read-only)

Run at the user's request after Phase 1 was committed as `c82de37`. Everything below was **re-read and
re-derived from the stored artifacts**, not from the prose; no mathematical computation was repeated.

| Check | Method | Result |
|---|---|---|
| Source identity | `sha256sum`, `stat`, `pypdf` on the staged PDF vs `SOURCE_PDF_MANIFEST.csv` | **match** — `7f7e6803…c27d249`, 612 826 B, 23 pp., verdict `ACCEPTED` |
| Version tag | every deliverable vs the manifest | **match** — `hal-04825601v1` in all five places, no stale tag |
| Theorem numbering | 25 register IDs vs `HEADING_INDEX.csv` and the corpus | **match** — HAL v1 sequence T1, T2, L3, L4, L5, T6, L7, T8, C9, T10, T11, C12, T13, C14, T15, T16, L17, T18, T19 |
| Page anchors | 23 fenced verbatim quotes searched in the pages they cite; 12 further claims (captions, `η_i` list, `M(5)`, the Example-3 `C3` slip, Theorem 15's condition, Lemma 17, Theorem 8's `λ = ε₁α + ε₂α`) | **35/35 located on the cited page** |
| Table values | the 33 rows regenerated from `phase1/raw/tables_recalc.json` and diffed against the report | **33/33 byte-identical** |
| Counts | 31 `[PASS]` / 0 `[FAIL]` in `examples_log.txt`; 33/33 `PASS` rows; 25 entries with 20 `VERIFIED` / 5 `QUOTED`, none without a status; 11 audit records (10 `CONFIRMED`, 1 `CONFIRMED WITH CORRECTION`) | **all as reported** |
| Preflight / selftest | `tools/preflight.py`, `tools/selftest_gate.py` | 20 PASS / 2 WARN / 0 FAIL; selftest **7/7** |
| Novelty | full-text scan of the four deliverables | **no novelty claim present** |

**Two inconsistencies were found and corrected** (they were in prose only — no mathematical result,
count, register entry or table value changed):

| ID | Inconsistency | Correction |
|---|---|---|
| C-1 | `PHASE_STATUS.md` stated the preflight total as "19 PASS / 2 WARN / 0 FAIL", a state that does not exist: the clean-tree run is **20 PASS / 2 WARN**, and it drops to 19 PASS / **3** WARN only while the tree is dirty. The same row also quoted the pre-correction `RESULT:` line. | counts restated for both tree states, `RESULT:` line re-quoted from the current tool output |
| C-2 | `source_audit/SOURCE_ACCESS_STATUS.md` §6 "Status statement" still asserted **"Gate 0: BLOCKED"** and **"Phase 1: not started … no Phase 1 deliverable has been written"** — a *current-status* section contradicting its own top banner and this file. | §6 marked **SUPERSEDED**, original text preserved verbatim beneath a banner giving the current status |
| C-3 | minor: `PHASE_STATUS.md` summarised the audit as "11/11 items", while the audit document has **nine** §1B items and the log has **11 records** (the ring decomposition was run in five configurations). | restated as "11/11 checks, nine items" so the two figures cannot be read as the same thing |

The corrected documents were re-validated (preflight 20/2/0, selftest 7/7) and committed separately so
that `c82de37` and all verified deliverables are preserved unchanged.

## Phase 2 — Related literature and novelty audit (DELIVERED; Gate 2 NOT PASSED)

Run on the user's authorisation after Phase 1 closed. Four deliverables, all under `phase2/`.

| Deliverable | Path | State |
|---|---|---|
| `LITERATURE_COMPARISON_MATRIX.csv` | `phase2/LITERATURE_COMPARISON_MATRIX.csv` | 18 rows, the blueprint's 8 columns, plus explicit exact-enumeration / quantum-construction flags and a "difference from proposed work" cell per row |
| `LITERATURE_REVIEW.md` | `phase2/LITERATURE_REVIEW.md` | method + explicit limits; prior-art map in strands A/B/C plus D; §4 states honestly where the gaps are *unresolved* rather than *empty* |
| `NOVELTY_ASSESSMENT.md` | `phase2/NOVELTY_ASSESSMENT.md` | the blueprint's three novelty tests; classification of each proposed element; Gate 2 verdict; three revised questions with kill criteria |
| `REFERENCE_VERIFICATION_REPORT.md` | `phase2/REFERENCE_VERIFICATION_REPORT.md` | reference apparatus audited (48/48 cited, no orphans, no duplicates); 12 key works bibliographically checked |

### Classification (no element reaches `N1`)

| Proposed element | Class | Reason |
|---|---|---|
| E1 constituent enumerator `H_ℓ(z_ℓ)` | **K** | exact field-level counts by hull dimension already exist — Debnath–Prakash (2022/23) for Galois hulls of constacyclic codes, Sangwisut et al. (2015), Lu et al. (2026, exact generating function), arXiv:2605.29204 |
| E2 joint enumerator | **N2** / `K` if constituents are free | the CRT decomposition makes it `Π_ℓ H_ℓ` — the blueprint explicitly forbids treating the phrase "joint enumerator" as a novelty argument |
| E3 total enumerator | **N2** / `K` | no content independent of E2 |
| E4 total-vs-constituent dimension relation | **K** | already proved in the source (Thms 8/10) and re-verified in Phase 1 (audit A7) |
| E5 well-definedness | **K** (routine) with a real hazard | Phase 1 finding F-1 (unnormalised `η_ℓ`) would corrupt a naive count of distinct codes |
| R1 repeated-root regime (`p` divides `n`) over `R_e` | **N2** | no accessible work covers it |
| R2 differing multipliers `α_ℓ` over `R_e` | **N2** | no accessible work covers it; uniqueness of the decomposition of `λ` must be settled first |
| R3 dual-containing subfamily count | **N2** | no accessible work covers it; factorisation risk |

### Gate 2 verdict

**NOT PASSED for the question as currently framed.** The framing "enumerate constacyclic codes by hull dimension over `R_e`, and take the joint/total distribution" is known at the constituent level and only conditionally new at the ring level. Per the blueprint, the research question must be revised; R1–R3 are the three candidates that survive the comparison, each with an explicit kill criterion that must be settled before Phase 3.

### Two retractions recorded during this phase

| ID | Earlier flag | Resolution |
|---|---|---|
| P2-R1 | `[22]` in the source's reference list "listed but never cited" | **Retracted.** `[22]` is cited as `[22, Hermitian construction]` in Lemma 17; the audit regex required the digit to be adjacent to `]` |
| P2-R2 | `[50, 51, 52, 55, 56, 57, 60, 68, 72]` "cited but absent from the list" | **Retracted.** All nine come from `[n,k,d]` / `[[n,k,≥d]]` code-parameter cells in Tables 2–3; they are not citations. The paper's apparatus is sound: 48/48 cited, 0 orphans, 0 duplicates |

Also corrected: the Phase 2 matrix had dropped Udomkavanich from the `[21]` author list; fixed in the CSV, trail in `REFERENCE_VERIFICATION_REPORT.md` §5.

| P2-R3 | First draft described arXiv:2607.12242 as giving "an exact generating function — the hull codimension enumerator, App. B.2" | **Overstated and corrected.** Re-reading the paper's positioning section: Appendix B is *"Counting and the fine structure of the τ-fixed cosets"* and supplies a **product enumerator** giving exact counts, scarcity probability, mean and variance. Wording corrected in the matrix, the review and the assessment. The same section independently confirms that cyclic and negacyclic codes *"have been enumerated by hull dimension"* (Sangwisut et al., Thms 22 and 23) — which strengthens, rather than weakens, the `K` classification of E1 |

### Blockers and limits carried forward

* **B-1 — publisher full texts unreadable.** Bodies of the paywalled works were not accessible (network to Springer/HAL frozen by instruction). Every "known" in the assessment therefore rests on the work's own abstract or on citing sentences, and **nothing is classified `N1`**. Closing B-1 is what would upgrade R1–R3 from `N2` to `N1` or kill them.
* **B-2 — Debnath–Prakash (2022/23) body not read.** E1 = `K` rests on their abstract; if their "restrictions on `q`" exclude `m = 2, k = 1`, or their count is aggregate rather than per-dimension, E1 falls to `N2`. One library visit settles it.
* **U-8 (carried from Phase 1)** — the version of record still has not been examined; all page references are to `hal-04825601v1`.

## R3 decision document (2026-10-23) — R3 NOT RECOMMENDED

Prepared at the user's request, after Phase 2, at their preferred candidate **R3: the distribution of dual-containing codes over `R_e`**. Deliverable: `phase2/R3_DECISION.md`. Phase 3 was **not** started.

| Item | Outcome |
|---|---|
| Question specified | yes — ring, code family, length and multiplier hypotheses, and the duality convention fixed in §1 (the involution is the **ring** `q`-th power, i.e. conjugate-reciprocal `u ↦ u^{−1}`, since `e \| q+1` forces `q ≡ −1 mod e`) |
| Counting target distinguished | codes/ideals, never generator listings — the Phase 1 **F-1** unnormalised-`η` trap would corrupt a tuple count; equivalence classes explicitly out of scope |
| Constituent relationship | **proved**: the involution fixes every CRT idempotent, so `C^{⊥H} = ⊕_j e_j (C_j^{⊥H})` and `C^{⊥H} ⊆ C ⟺ ∀j C_j^{⊥H} ⊆ C_j`; hence `N(n,λ) = ∏_j N_F(n, α_j)` |
| Kill criterion | **fired** — K1 (source Thm 16), K2 (idempotents fixed), K3 (published field-level counts), K4 (product) |
| Smallest test case | `q=3, e=2, n=2` (`\|R\|=81`, 64 multipliers) and `q=2, e=3, n=2` (`\|R\|=64`, 27 multipliers, three components, repeated-root) |
| Result | product identity exact on **64/64** and **27/27** multipliers, over every ideal; dual decomposition exact on **16/16** and **27/27** CRT tuples |

**Supporting probe (new, small, deterministic):** `phase2/r3_probe/` — `r3_probe.py`, `r3_dual_formula.py`, `r3_hull_dim_check.py`, log in `r3_probe_log.txt`. Runtime ≈ 15 s total, stdlib only, no network.

**Phase 1 items strengthened by the probe** (no Phase 1 result changed):
* **Theorem 10** (`QUOTED` in Phase 1) recomputed independently: hull-dimension additivity holds **16/16** and **27/27**, including `e = 3`.
* **Theorem 16** had been verified only against `e = 2` table rows; it is now corroborated at `e = 3` as well.

**Recommendation recorded:** stop R3. It is precise enough to authorise, and its answer is a product of known counts. The only non-collapsing variant is quantum-parameter distribution with a distance constraint (the distance couples components), which is a different and much harder problem, not a relabelled R3.

**Four errors made and fixed inside the probe** (E-1 monic-only ideal enumeration; E-2 `+=` instead of `−=` in RREF; E-3 coefficientwise conjugation instead of the paper's conjugate-reciprocal involution, which produced a spurious failure of Theorem 16; E-4 incorrect subspace intersection). All are recorded in `R3_DECISION.md` §8 because the verdict rests on the probe.

## R1 feasibility and novelty kill test (2026-10-23) — R1 NO-GO

Full argument: `phase2/R1_FEASIBILITY.md`. Probe: `phase2/r1_probe/` (`r1_probe.py`,
`r1_orbit_check.py`, log `r1_probe_log.txt`, 185 lines).

| Item | Outcome |
|---|---|
| Question | `n = p^v n'` with `v ≥ 1`; enumerate `λ`-constacyclic codes over `R_e` by Hermitian hull dimension and compare with the `v = 0` law |
| Assumptions fixed | `R_e = F_{q²}[u]/(u^e−1)`, `e \| q+1`; Hermitian `⟨x,y⟩ = Σ x_i y_i^q` with the **ring** `q`-power (conjugate-reciprocal); distinct codes, not generator descriptions |
| Ring-level reduction | `q`-power **fixes every CRT idempotent** (the coefficient Frobenius cancels the `μ ↦ μ^{−1}` label permutation), so `Hull_H(C) = ⊕_ℓ Hull_H(C_ℓ)` and `N_{R_e}(n,λ) = ∏_ℓ N_F(n, α_ℓ)` — a plain product |
| Repeated-root effect isolated | entirely the multiplicity `p^v` on the squarefree base `x^{n'} − c`; the ideal structure is unchanged, only the exponent ranges change |
| Kill criterion | **fired** — **K-R1: source Theorem 10** (general `e`, arbitrary `p^v`, hull dimension = linear form in per-orbit integers with explicit box bounds `0 ≤ a ≤ γ_l(j)⌊p^v/2⌋`, `0 ≤ b ≤ β_l(j)p^v`) + **CRT/PIR**: counting is a lattice-point count in the paper's own boxes |
| Smallest tests (`p \| n`) | `q=3,n=3=p` over `F_9`; `q=3,n=6=2·3`; plus `q=2,n=2`, `q=3,n=9`, `q=2,n=4`, `q=2,n=8`, `q=2,n=6` |
| Verification | 184 subspaces of `F_9³` brute-forced, matching the monic-divisor count and hull distribution for **8/8** `α`; lcm formula **32/32** and **80/80**; orbit product exact on **24/24** `α` |
| Result | repeated roots **do** change the distribution (hull dimensions spread to `⌊n/2⌋`; LCD no longer automatic), but the law is a product over conjugate-reciprocal orbits — the same routine-product failure mode as R3 |
| Verdict | **NO-GO**: `K`, not `N2` |

**The only textual gap R1 could claim** is that the source states its LCD criteria (Theorems 11/13,
Corollaries 12/14) under `gcd(n,p) = 1`. Filling it means substituting Theorem 10's bounds and
noting the achievable set is no longer `{0}` — a line of algebra inside the same paper. That is not
a research question.

The kill does **not** rely on the paywalled literature (blockers B-1, B-2 stay open); it rests
entirely on the source paper's own Theorem 10 plus CRT. R1's originally stated criterion
(Debnath–Prakash covering `p | n` and composing over components) was therefore never evaluated:
it is not needed.

Three probe defects fixed and recorded in `R1_FEASIBILITY.md` §4.4 (quotient/remainder confusion
plus an untrimmed remainder; over-generated subspace enumeration — true count is 184, not 488;
`O(Q^n)` divisor brute force replaced by structural enumeration with the brute force kept as an
assertion). One error of my own in drafting §1 (asserting that duality permutes CRT components) was
caught by explicit computation and corrected in §4.5; the earlier R3 record had it right.

## R2 decision (2026-10-23) — R2 NO-GO, Gate 2 cannot be passed on this question

Full argument: `phase2/R2_DECISION.md`. Probe: `phase2/r2_probe/` (`r2_probe.py`, log 53 lines,
runtime < 1 s).

| Item | Outcome |
|---|---|
| Question | does the hull-dimension distribution depend on the decomposition `λ = Σ_ℓ η_ℓ α_ℓ`? |
| Finding | **the premise is false — the decomposition is unique**, in both readings |
| Reading A (CRT coordinates `α_ℓ = λ(μ_ℓ)`) | `Σ_ℓ e_ℓ λ(μ_ℓ) = λ` verified **27/27** (`q=2,e=3`), and by linearity for **every** `λ` at `e=4`; coordinates are evaluations, hence forced |
| Reading B (paper's `η_ℓ`) | `{η_ℓ}` is a **basis** (`η_ℓ(μ_j)=0`, `ℓ≠j`), so `(a_ℓ) ↦ Σ η_ℓ a_ℓ` is **injective** on all 64 elements, units hit **27/27**, all fibres size 1 — a change of basis, not an ambiguity |
| F-1 quantified | `λ(μ_ℓ) = a_ℓ·η_ℓ(μ_ℓ)` with `η_ℓ(μ_ℓ) = 1,3,2` (`q=2,e=3`) and `1,2,6,3` (`q=3,e=4`); `Σ η_ℓ = (0,0,1)` and `(0,0,0,1)`, never `1`. Using `a_ℓ` as the component multiplier predicts the wrong hull law for **18 of 27** multipliers at `F_4, n=6` (where the field laws differ) |
| Multiset dependence | with correct coordinates, `F_4, n=6`: 4 distinct multisets of component laws, each inducing **exactly one** distribution; totals `27, 243, 2187, 19683` = products of field code counts |
| Kill criterion | **K-R2: CRT (source Theorem 2)** — the decomposition is the coordinate map, a bijection; there is no free variable to depend on. R2 is not a known-result corollary, it is **vacuous** |
| Verdict | **NO-GO** (`K`) |

**Scope note.** The `η`-normalisation issue is a hazard for a *counting* extension, not an error in
the paper: the paper uses `η_ℓ` only inside lcm-based hull formulas and never counts. Phase 1's
conclusion that no parameter changes stands.

**Gate 2 status.** R1, R2 and R3 have now all failed their own kill criteria. Gate 2 — *"the
proposed main contribution is distinguishable from the closest known results"* — **cannot be passed**
by the "count `λ`-constacyclic codes over `R_e` by Hermitian hull dimension, then form a
joint/total enumerator" line. The obstruction is structural: the CRT decomposition makes every such
count a product of field-level laws, and those laws are given for arbitrary `n` (including `p | n`)
by the source's Theorem 10 and by Sangwisut–Jitman–Udomkavanich (AMC 2017). This is a negative
result about the proposed question, **not** a defect in the source paper.

## R4 feasibility and structural test (2026-10-23) — structurally GO

Full argument: `phase2/R4_FEASIBILITY.md`. Probe: `phase2/r4_probe/` (`r4_probe.py`, log 29 lines,
runtime < 1 s).

R4 is the fourth revision considered and **the first that passes the structural test that killed
R1–R3**.

| Item | Outcome |
|---|---|
| Question | count `λ`-constacyclic codes over `R_e` with `C^{⊥_H} ⊆ C` by quantum parameters `[[en, 2k−en, ≥d]]`, i.e. by (hull dimension, Gray distance) |
| Gray map (source pp. 6–7, 15, full text) | `ψ` applies `M` (`M M* = νI_e`) to the vector of `e` component symbols **at each position** |
| Structural fact | the Gray weight is `Σ_i g(s_{1i},…,s_{ei})` — a joint function of the components **at each position**, not a sum of component weights; for `e=2`, `w_G = w(a+b)+w(a−b)` |
| Consequence | a weight-1 Gray word exists **iff** `C_1 ∩ C_2` contains a weight-1 word, so `d(ψ(C))` depends on `C_1 ∩ C_2` — a joint invariant. **No function of `(k_ℓ, d_ℓ)` determines it** |
| Numeric confirmation | `q=3, e=2, n=2`, `F_9`, `M=[[1,1],[1,−1]]`: 9 component-invariant groups; the group `(k₁,d₁,k₂,d₂)=(1,2,1,2)` realises Gray distances **`{2,3}`** — non-constant; 144 dual-containing pairs; parameters `(k,d) ∈ {(2,2),(2,3),(3,2),(4,1)}` |
| Scope limit found (5.1) | `M` is a free parameter (`MM*=νI`); two admissible choices gave *identical* distances in this instance (`0/16`), so no `M`-dependence is claimed |
| Scope limit found (5.2) | the paper's `e=2` matrix has `ν = 2`, which is `0` in even characteristic: `M` is singular, `ψ` not injective, and the probe reproduces Gray distance `0` over `F_4`. Not an error (all the paper's examples use odd `q`) but a real generality restriction |
| Prior-art pass (K4-1) | **resolved at abstract/page level.** The closest threat arXiv:2512.12519 is **withdrawn** (16 Dec 2025, "overlap with existing papers") and its distance content was asymptotic anyway. The mass-formula line (arXiv:2410.13578, IEEE TIT 2024, arXiv:2605.29204) counts all `[n,k]` codes by hull dimension via a **Grassmannian** group action: no distance constraint, and it **cannot be specialised to a constacyclic family** (the unitary group does not preserve constacyclicity). Constacyclic work gives hull dimensions, criteria or tables — not (hull, distance) distributions. Absence not established; B-1/B-2 open; **N2** |
| Feasibility (K4-2) | **partial**: exact enumeration is affordable at small `n`, nothing more. No closed form identified |
| Verdict | **GO** — survives the structural test and is not pre-empted by the closest known results. **Gate 2 PASSED on R4** (distinguishable; no novelty claimed). K4-2 (feasibility of an exact count) becomes the first task of Phase 3 |

## Next step

**Gate 2 has been passed on R4.** R1, R2, R3 are recorded NO-GO (`25bbe62`, `78b89ac`, `c9d4517`).
R4 — the exact joint (Hermitian hull dimension, Gray distance) distribution of `λ`-constacyclic codes
over `R_e` with `C^{⊥_H} ⊆ C` — is distinguishable from the closest known results and, unlike the
other three, is not a product of field-level laws.

**Phase 3 may now begin.** Its first task is **K4-2**, feasibility, in this order:

1. Fix the research statement precisely, including the choice of `M` (which the paper leaves free
   subject to `MM* = νI`).
2. Settle whether the field-level input — the joint (hull dimension, minimum distance) law for
   `λ`-constacyclic codes over `F_{q²}` of length `n`, for arbitrary `n` including `p | n` — is
   obtainable in closed form, e.g. from the repeated-root distance results of Dinh, or whether it is
   irreducibly a computation.
3. Only then decide the deliverable: a closed-form distribution, or an exact algorithm plus tables.

Phase 3 and later phases have **not** begun; the first Phase 3 deliverable will be the feasibility
decision in (2). Nothing in Phase 2 changed a Phase 1 result, count or register entry.

Phase 1 stands complete; nothing in Phase 2 changed a Phase 1 result, count or register entry.

---

## Deliverables index

| Blueprint deliverable | Path |
|---|---|
| `PROJECT_PLAN.md` | `research_project/PROJECT_PLAN.md` |
| `SOURCE_INVENTORY.md` | `research_project/source_audit/SOURCE_INVENTORY.md` |
| `SOURCE_PAPER_METADATA.md` | `research_project/source_audit/SOURCE_PAPER_METADATA.md` |
| `ENVIRONMENT_CAPABILITIES.md` | `research_project/source_audit/ENVIRONMENT_CAPABILITIES.md` |
| `PHASE_STATUS.md` | `research_project/PHASE_STATUS.md` (this file) |
| `SOURCE_THEOREM_REGISTER.md` | `research_project/phase1/SOURCE_THEOREM_REGISTER.md` |
| `SOURCE_MATHEMATICAL_AUDIT.md` | `research_project/phase1/SOURCE_MATHEMATICAL_AUDIT.md` |
| `SOURCE_NOTATION_GLOSSARY.md` | `research_project/phase1/SOURCE_NOTATION_GLOSSARY.md` |
| `SOURCE_EXAMPLE_RECALCULATION.md` | `research_project/phase1/SOURCE_EXAMPLE_RECALCULATION.md` |
| `LITERATURE_COMPARISON_MATRIX.csv` | `research_project/phase2/LITERATURE_COMPARISON_MATRIX.csv` |
| `LITERATURE_REVIEW.md` | `research_project/phase2/LITERATURE_REVIEW.md` |
| `NOVELTY_ASSESSMENT.md` | `research_project/phase2/NOVELTY_ASSESSMENT.md` |
| `REFERENCE_VERIFICATION_REPORT.md` | `research_project/phase2/REFERENCE_VERIFICATION_REPORT.md` |

Supporting evidence: `source_audit/PHASE0_VERIFICATION_LOG.md`, `source_audit/SOURCE_PDF_MANIFEST.csv`, `source_audit/PHASE1_EXECUTION_PLAN.md`, `source_audit/REPOSITORY_SOURCE_SEARCH.md`, `source_audit/PRIOR_ART_REGISTER.md`, `source_audit/SOURCE_IDENTITY_BLOCKER.md`, `source_audit/SOURCE_ACCESS_STATUS.md`, `phase1/raw/*`, `code/*`, `tools/*`, `logs/*`.
