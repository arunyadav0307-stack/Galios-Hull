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

## Phase 3 — started 2026-10-23 (task K4-2 complete)

Deliverable: `phase3/K4_2_FEASIBILITY.md`; probe `phase3/r4_field_joint.py`, log
`r4_field_joint_log.txt` (≈ 4 s).

**K4-2 question:** is R4's object — the joint (Hermitian hull dimension, minimum distance) law —
determined by the two marginals, or is the coupling essential?

**Answer: the coupling is essential.**

| Item | Result |
|---|---|
| Instance | `F_9`, `n=6`, `α=1`; `x^6−1 = (x−1)³(x+1)³`; 16 cyclic codes `⟨(x−1)^a(x+1)^b⟩` |
| Method | distances **exact** by increasing-weight membership testing (proven minima, no bounds); hull dimensions by the kernel method, independently of any formula |
| Consistency | `hull = min(a,3−a)+min(b,3−b)` reproduced for **16/16** — R1's orbit formula re-confirmed on a two-orbit instance |
| Joint law | hull 0 → `d ∈ {1,2,∞}`; hull 1 → `d ∈ {2,4,6}`; hull 2 → `d ∈ {2,3}` |
| Independence | **fails**: e.g. `(hull 1, d=6)` observed 2 vs predicted 1.00; `(hull 2, d=2)` observed 1 vs predicted 1.75 |
| Dimension | `d` is **not** a function of `dim = 6−a−b` either: on `a+b=3`, `d=2` for `(0,3),(3,0)` and `d=3` for `(1,2),(2,1)` |
| Verdict | joint law is irreducible; no closed form found; exact computation is affordable at table scale |

Consequence recorded: the Phase 3 deliverable cannot be "combine two known enumerators". Programme
(P3-1 exact tables over `q ∈ {3,4,5}`, `n ≤ 12`, several `α`; P3-2 structural theorems, starting with
the two-orbit distance matrix proven above; P3-3 the ring-level Gray coupling) is recorded in the
deliverable, and **P3-2 is now in progress**.

**No theorem, no closed form and no novelty claim** is made in this Phase 3 section. Blockers B-1
and B-2 remain open.

## Phase 3 — P3-1 exact tables (2026-10-23)

Deliverable `phase3/P3_1_TABLES.md`; probe `phase3/p3_tables.py`, log `p3_tables_log.txt` (85 lines).
Five instances, **169 codes, 144 with exactly computed distances** (`q ∈ {3,2}`, `n ∈ {3,6,2,4,6}`).

| Finding | Outcome |
|---|---|
| C1: "every LCD code has `d ≤ 2`" | **REFUTED** — `hull = 0` codes reach `d = 3` in 3 of 5 instances; instance A contains **LCD MDS** codes `[3,1,3]`, `[3,2,2]` over `F_9` |
| C2: "MDS ⟺ self-orthogonal" | **REFUTED both ways** — A: 16 MDS, only 4 self-orthogonal; B: 24 self-orthogonal, only 8 MDS |
| C3: joint law ≠ product of marginals | **CONFIRMED 5/5** — now across two fields and five lengths, not one instance |
| Closed form for `d(a,b)` | not found; reframed as a two-point multiplicity-code problem |
| Ring level (Gray coupling) — the actual R4 question | **not started** (P3-3) |

Both refutations were pre-registered as conjectures in `K4_2_FEASIBILITY.md` §2.1 and are recorded as
refuted rather than quietly dropped. No theorem and no novelty claim is made.

## Phase 3 — P3-2 structural results (2026-10-23)

Deliverable `phase3/P3_2_TWO_ORBIT.md`.

| Result | Status |
|---|---|
| Lemma 1: no word of weight 1 for any `(a,b) ≠ (0,0)` in the two-orbit family | **proved** |
| Lemma 2: single-orbit codes over `n=6` have `d = 2` | **proved** |
| Lemma 3: `[6,1,6]` MDS corners with `d = 6` | **proved** |
| Lemma 4: `d(C(1,1)) = 2` | **proved** |
| Four middle values (`d = 3,3,4,3`) | computed only, no formula claimed |
| `n=9` complete table (10 codes): `hull = min(a,9−a)` | computed, 10/10 |
| `d(C_a) = min{w((x−1)^j) : j ≥ a}` at `n=9` | **conjecture**, 10/10 — historical record; **it is the known Dinh (2008) formula, see P3-7b** |

Recorded error avoided: `(x−1)^9 = x^9 − 1 ≡ 0` in `R`, so it is *not* a weight-2 word — a natural
mistake that would have broken the `n=9` reading.

The field-level picture is now documented; next is **P3-3**, the ring-level `R_e` Gray coupling,
which is the actual R4 question.

## Phase 3 — P3-3 ring-level Gray coupling (2026-10-23)

Deliverable `phase3/P3_3_RING_GRAY.md`; probe `phase3/p3_ring_gray.py`, log 43 lines.

| Result | Status |
|---|---|
| **Thm 1** `Hull_H(C) = ⊕_ℓ Hull_H(C_ℓ)`; `C^{⊥_H} ⊆ C` iff componentwise | **proved**; hull is `ψ`-independent |
| **Thm 2** `min_ℓ d_ℓ ≤ d(ψ(C)) ≤ e·min_ℓ d_ℓ` for every admissible `M` | **proved**; elementary (support counting). **Superseded for `e = 2` nested components by P3-10**: `d(ψ) = min{2d_1,d_2}` exactly |
| **Thm 3** single-component codes: `d(ψ) = ρ_k·d(C_k)` | **proved**; verified 40/40 |
| **Thm 4** equal components: `d(ψ) ≤ σ·d(D)`, equality when `σ = 1` | **proved**; `σ=1` verified 40/40 |
| **Thm 5** non-determination: `(k_1,d_1,k_2,d_2) = (1,3,1,3)` realises `d(ψ) ∈ {3,4,5}` | **proved by witnesses** |
| Bounds (exact enumeration) | 256 + 576 pairs, 216 triples: **0 violations** |
| Corrected prediction | `σ = 3` was expected tight; data show `d(ψ(D,D,D)) = d(D)`, so the diagonal codeword is **not** optimal for `e ≥ 3` — recorded as refuted |

**Key distinction recorded:** the bounds are convention-free (they use only `M` invertible, i.e.
`ν ≠ 0`); the exact values depend on `M` and on the `η`-normalisation (F-1). Rescaling a component
coordinate does not change supports but does change `(sM)`'s zeros.

**Environment incidents (three, none changed a result):** (i) `numpy` disappeared between turns, so
`p3_tables.py` was rewritten in stdlib and re-run — every committed P3-1 figure reproduced exactly;
(ii) the local `.git` was a fresh clone at `33aeb79` with `research_project/` untracked, while the
remote held all commits, so the branch was restored by `git fetch` + `git reset --mixed FETCH_HEAD`
— **no commit lost or rewritten**, working tree untouched, source PDF re-verified as 612 826 B and
sha256 `7f7e6803…`; (iii) `pypdf` is gone, so `tools/preflight.py` can no longer run — an
environment regression, not a broken artifact, worked around by direct `sha256sum` verification only.

**Verdict:** GO for the narrowed distributional contribution; **NO-GO** for a "Gray-coupling
structural theorem" as the headline. Novelty not claimed (bounds likely folklore; B-1/B-2 open).

## Phase 3 — P3-4 ring-level quantum-parameter distribution (2026-10-23)

Deliverable `phase3/P3_4_QUANTUM_DISTRIBUTION.md`; probe `phase3/p3_quantum_dist.py`, log 33 lines.

First exact distribution of dual-containing `λ`-constacyclic codes over `R_e` by quantum parameters
`[[en, 2K−en, ≥d]]`, with `d` computed exactly through the Gray map for a **named** matrix `M`.

| Instance | dual-containing tuples | distribution |
|---|---|---|
| `R_2`, `F_9`, `n=2`, `M=[[1,1],[1,−1]]` | 144 = 12² | `[[4,0,≥2]]`:8, `[[4,0,≥3]]`:8, `[[4,2,≥2]]`:64, `[[4,4,≥1]]`:64 |
| `R_2`, `F_9`, `n=3`, same `M` | 144 = 12² | `[[6,2,≥2]]`:16, `[[6,4,≥2]]`:64, `[[6,6,≥1]]`:64 |
| `R_3`, `F_4`, `n=2`, dense `M` (`ν=1`) | 216 = 6³ | `[[6,0,≥2]]`:27, `[[6,2,≥1]]`:81, `[[6,4,≥1]]`:81, `[[6,6,≥1]]`:27 |

**Key result:** over `F_9`, `n=2`, constituent data `((1,2),(1,2))` yields **both** `[[4,0,≥2]]` and
`[[4,0,≥3]]` — Theorem 5 of P3-3 lifted to the quantum parameters. The distribution is therefore not
a product of field-level laws.

**Honest counterweight recorded:** the effect is invisible in the `F_4`, `e=3` instance (0 of 4 groups)
because all dual-containing field codes there share the same `(k,d)`; non-determination needs ties
realised by inequivalent codes.

**No claim** that these parameters are good, new or competitive — they are toy, and degenerate rows
(`K=0`, `K=en`) are explicitly flagged. New limitation **L-8 (scaling)**: cost is `∏_ℓ |C_ℓ|` per
tuple; feasibility for `n` beyond single digits is not established.

**Phase 3 programme complete.** GO on the narrowed distributional contribution; NO-GO on a
structural-theorem headline. Novelty not claimed (B-1/B-2 open).

## Phase 3 — P3-5 literature checkpoint (2026-10-24)

Deliverable `phase3/P3_5_LITERATURE_CHECKPOINT.md`; probe `phase3/p3_gray_hull_identity.py`, log 5 lines.

| Item | Outcome |
|---|---|
| **Citation error found in my own record** | `R1_FEASIBILITY.md` merged two different papers into one row. DOI `10.1007/s12095-022-00591-6` = Debnath, Prakash & **Islam**, *Cryptogr. Commun.* **15**:111–127 (2023), **finite fields**, three authors — *not* the `SIST` 325:309–319 paper (ICTIS 2025, *Hulls of Cyclic Codes Over a Local Ring*, chain ring `Z_{p³}`). **Corrected by new commit with the note left in place.** CSV rows 10 and 12 were already correct; no verdict depended on it |
| **B-2 refined** | split into **B-2a** (Cryptogr. Commun. 2023: field-level count by Galois hull dimension, "restrictions on `q`" unverified) and **B-2b** (SIST 2025: count over chain ring `Z_{p³}`). Neither can reproduce a joint (hull, distance) law. **Both open** |
| **B-1 advanced** | arXiv:2606.22069 (Qian–Wang–Wang) read **in full text**: generator polynomials of Euclidean/Hermitian hulls and sums over `F_q × (F_q+vF_q)` **and their Gray images**, plus QECC tables — **no counting**. This is the closest work in shape |
| **New verified proposition** | `dim Hull_H(ψ(C)) = dim Hull_H(C) = Σ_ℓ dim Hull_H(C_ℓ)`, from the source's Lemma 3 + bijectivity + Thm 1. Checked `F_9, e=2, n=2`: **256/256** by two independent routes. So Tian–Gao–Gao's "hull dimensions of Gray images" is **the same invariant**, not extra prior art |
| **Bug recorded** | first version of that check used `basis × basis` (does not span the product code) and reported **112 spurious mismatches**; correct spanning set `{(a,0)} ∪ {(0,b)}` gives 256/256 |
| Novelty | **still not claimed**; B-2a/B-2b bodies and the Tian–Gao–Gao full text remain unobtainable |

## Phase 3 — blueprint Phases 3, 4 and 8 delivered (2026-10-24)

| Blueprint phase | Deliverable | Status |
|---|---|---|
| 3 Precise formulation | `phase3/MATHEMATICAL_FRAMEWORK.md` | **done** — all six §3A well-posedness questions answered with pointers to proofs |
| 4 Factor-orbit enumeration | `phase3/CONSTITUENT_ENUMERATOR_FORMULA.md` | **done (`5fa1ac0`)** — orbit-product form **proved**, not merely verified |
| 8 Gap / contribution decision | `phase3/RESEARCH_GAP_AND_CONTRIBUTION_DECISION.md` | **done — decision: STOP before Phase 9** |

**Phase 4 theorem (new proof, no novelty).** `H_α(z) = ∏_{σ-orbits} P_O(z)` with
`P_i(z) = Σ_a z^{m_i min(a,p^v−a)}` (fixed orbit) and `P_ij(z) = Σ_{a,b} z^{m_i min(a+b, 2p^v−a−b)}`
(2-cycle), and `H_α(1) = (p^v+1)^s`. Complete proof: Lemma 1 (divisors ↔ codes bijection, settling the
blueprint's "codes vs generator descriptions" requirement at field level), Lemma 2 (every factor of
`x^n − α` has multiplicity exactly `p^v`; `f^† ∝ f` under `α^{q+1} = 1`), Lemma 3 (`†` is an involutive
factor permutation), Lemma 4 (lcm exponents, plus the max-sum identity). The step the blueprint insists
on — independence of local choices — is proved from the fact that the only constraint on exponents is a
per-factor multiplicity bound, so the admissible set is a Cartesian product of orbit boxes. Re-verified
against enumeration 24/24 this turn. **Classification: `K`** — prior art in the square-free case,
routine refinement of source Theorem 8 in the repeated-root case.

**Phase 8 decision: Phase 9 (manuscript) is NO-GO.** The blueprint's gate requires "at least one
substantive proved theorem"; the proved inventory is thin and the strongest content is computational.
All six of the blueprint's candidate contributions are `K` or unresolved (§2 of the decision document).
R4 remains the only defensible direction and it carries no substantive theorem. Three library-access
checks (B-2a, B-2b, Tian–Gao–Gao full text) decide whether R4 can be written up at all; if any contains
a joint (hull, distance) distribution, the contribution must be **withdrawn**.

## Phase 3 — blueprint Phases 6 and 7 deliverables closed (2026-10-24)

All named deliverables from the Phase 8 document §1 gap table are now written.

| Blueprint phase | Deliverable | Status |
|---|---|---|
| 6 Dual-containing | `phase3/DUAL_CONTAINING_ENUMERATION.md` | **done** |
| 6 Quantum construction | `phase3/QUANTUM_CONSTRUCTION_THEOREM.md` | **done** — labelled `K`, it is the source's Thm 19 composed; no novelty |
| 6 Parameter table | `phase3/QUANTUM_CODE_PARAMETER_TABLE.csv` | **done — 504 rows, machine-generated by `p3_quantum_table.py`, not typed** |
| 6 Parameter verification | `phase3/QUANTUM_PARAMETER_VERIFICATION.md` | **done** |
| 7 Computational verification | `phase3/COMPUTATIONAL_VERIFICATION.md` | **done** |
| 7 Reproducibility | `phase3/REPRODUCIBILITY.md` | **done** |

**New independent check.** `K` computed as the **rank of the explicit Gray image** agrees with
`Σ_ℓ dim C_ℓ` in **504/504** rows. The two routes share no code: one builds `ψ(C)`, the other never
does. The CSV also reproduces the P3-4 distributions exactly (8/8/64/64, 16/64/64, 27/81/81/27).

**Caveat recorded prominently.** The raw quantum-MDS count (136/144 etc.) is misleading because it
includes `K = 0` and `K = en` rows. Separated out: `R_2/F_9/n=2` has **64/64** non-trivial codes
quantum-MDS (`[[4,2,2]]_3`), `R_2/F_9/n=3` **64/80**, and `R_3/F_4/n=2` **0/162**. At these lengths the
quantum Singleton bound is weak; **no claim that any parameter is good, new or competitive**.

**Negative tests** are tabulated in `COMPUTATIONAL_VERIFICATION.md` §4: eight cases where computation
contradicted an expectation (mine or the code's), all retained rather than smoothed over.

Phase 8 standing decision unchanged: **Phase 9 (manuscript) is NO-GO.** These files make the package
auditable; they do not create a theorem.

## Phase 3 — P3-7 power attainment, limitation L-2 (2026-10-24)

Deliverable `phase3/P3_7_POWER_ATTAINMENT.md`; probe `phase3/p3_power_attainment.py`;
log `phase3/p3_power_attainment_log.txt` (212 lines, exit 0, 759 s, stdlib only).

Question: is `d(C_a) = m(a) := min_{a <= j <= n-1} w((x-1)^j)` for `C_a = <(x-1)^a> <= F_q[x]/(x^n - 1)`,
`n = p^s`? This was the `n = 9` conjecture in the P3-2 table.

| Result | Status |
|---|---|
| **Lemma W** `w((x-1)^j) = prod_i (d_i + 1)` for `j = sum d_i p^i` | **proved** (no cancellation across residue classes) |
| **Lemma H** `C_a = ker H_a`, `H_a[i][j] = C(j,i) mod p` (Lucas) | **proved**; falling factorials are **wrong** in char `p` for `a > p` |
| **Lemma C** `d(C_a)` = girth of the column matroid of `H_a` | **proved**; no codeword enumeration needed |
| **Theorem A** `s = 1` (`n = p`): `d(C_a) = a + 1 = m(a)` for `0 <= a <= p-1` | **proved** (explicit word + Vandermonde lower bound) |
| **Theorem B** `s >= 2`, `1 <= a <= p^{s-1}`: `d(C_a) = 2 = m(a)` | **proved** (word `1 - x^{p^{s-1}}`; proper ideal excludes weight 1); sharp at `a = p^{s-1}+1` |
| Singleton consistency `m(a) <= a+1` | checked all `a` in 16 cases up to `n = 125` (`--mbound` log) |
| L-2 on `p^{s-1} < a < p^s` | **CLOSED by citation — see P3-7b**: it is the `t >= 1` branch of Dinh (2008). **Superseded; not open, not a contribution** |
| Verification | 11 cases `(p,s)` = (2,1…4), (3,1…3), (5,1…2), (7,1), (11,1): **117/117 agree, 0 disagree, 0 undetermined** |
| Two-method cross-check (circuit matroid vs enumeration) | **70 values, 0 mismatches** |
| Not computed | `n = 49`, `n = 81`, `n = 125` — cap-7 subset search out of reach in pure Python (stated, not skipped silently) |

Recorded errors (audit trail, both caught by the project's own tables):
1. Using falling factorials `j(j-1)…(j-i+1)` instead of `C(j,i)` made `d = 2` for every `a >= 3` at
   `n = 9` (5 disagreements with the committed table). Over `F_3`, `(x-1)^3 = x^3 - 1` kills all
   ordinary derivatives at 1 although the root has multiplicity 3.
2. `code_distance_direct` divided by `k!` mod `p`, invalid for `k >= p`; it reported `d = 3` for
   `(x-1)^8` over `F_3` instead of `9`.

**Effect on the standing decisions:** Phase 9 remains **NO-GO**. Theorems A and B are correct but
small, are special cases of the conjecture, and are not claimed as new (B-1, B-2a, B-2b and
Tian–Gao–Gao remain unread).

**SUPERSEDED by P3-7b (below):** L-2 is **not** a conjecture at all. It is Dinh (2008)'s theorem, and
Theorems A and B are its `t = 0` branches. Nothing in this section is a contribution; the section is
kept as the audit trail of how the identification was reached and of the two bugs it exposed.

## Phase 3 — P3-7b L-2 provenance audit: L-2 is a KNOWN THEOREM (2026-10-24)

Deliverable `phase3/P3_7B_L2_PROVENANCE_AUDIT.md`; probes `phase3/p3_known_formula_check.py`
(log 32 lines, **5050 values, 0 mismatches**) and `phase3/p3_weight2_field.py` (log 39 lines).

**Correction of the P3-7 status, not of the P3-7 mathematics.** The exact minimum distance of
`C_i = <(x-1)^i> <= F_q[x]/<x^{p^s}-1>` is known for every `i`:

> **Dinh, *Finite Fields Appl.* 14(1):22-40 (2008):** `d_i = (tau+1) p^t` where `1 <= tau <= p-1`,
> `0 <= t <= s-1`, on the band `p^s - p^{s-t} + (tau-1)p^{s-t-1} < i <= p^s - p^{s-t} + tau p^{s-t-1}`.

Restated as Lemma 1 of arXiv:2304.00762 (citing Dinh 2008 and Massey-Costello-Justesen 1973) and as
Thm 2.4 of arXiv:1704.03311; used throughout the symbol-pair / `b`-symbol literature.

| Item | Verdict |
|---|---|
| **L-2** (`d(C_a) = min_{j>=a} w((x-1)^j)`) | **CLOSED by citation** — never an open problem; **removed from the limitation list** |
| Theorem A (`s = 1`, MDS) | **classical** re-derivation (`t = 0`, `tau = i`); not new |
| Theorem B (`1 <= a <= p^{s-1}` ⇒ `d = 2`) | **classical** (`t = 0`, `tau = 1`); not new |
| Theorem C (`p^{s-1} < a <= 2p^{s-1}` ⇒ `d = 3`) | **classical** (`t = 0`, `tau = 2`); verified 3/3 bands, not new |
| "Open range" `p^{s-1} < a < p^s` in P3-7 §6 | **not open** — it is the `t >= 1` branch; the block/`epsilon` obstruction was a route to an existing theorem |
| `n = 49, 81, 125, 343, 1331, 2197` "out of reach" | **moot** — settled by the formula; `m(a)` agrees at all of them |
| Weight Lemma, Lemma H, Lemma C, both recorded bugs | **correct work**, no novelty claimed |

**Verification of the identification:** `m(a)` vs the published formula at **5050 values**
(`p = 2, s <= 8`; `p = 3, s <= 4`; `p = 5, 7, 11, 13, `s <= 3`), **0 mismatches**. Independent anchor:
the published Example 1 of arXiv:2304.00762 gives, for `n = 25` over `F_5`, the bands
`2,3,4,5,10,15,20,25` with counts `5,5,5,5,1,1,1,1` — my `m(a)` produces exactly the same band
structure, and my `n = 25` distances in P3-7 §7.3 were computed by matroid girth, not by the formula,
so the two routes agree independently.

**Two small correct results that survive, neither claimed as new:** field independence of `d(C_a)`
(`H_a` has entries in `F_p`, rank is field-independent; checked `F_9` vs `F_3` at `n = 9`), and the
weight-2 classification (`a = 0` ⇒ `w = 1`; `1 <= a <= p^{s-1}` ⇒ `w = 2`; verified at 90 values over
10 `(p,s)` pairs) which is exactly the `tau = 1` branch.

**Methodological lesson recorded:** the Phase 2 rule "read complete theorem statements, not abstracts"
fails in a second way here — the theorem exists but sits in a 2008 paper about *negacyclic* codes whose
title names distance distributions generally, and is restated in a 2025 paper about *weight
distributions*. Searching the project's own topic (hulls) does not surface it; searching the specific
object (`<(x-1)^i>`, length `p^s`) does. Prior-art row added to `phase2/LITERATURE_COMPARISON_MATRIX.csv`.

**Effect on standing decisions:** Phase 9 remains **NO-GO and is now reinforced** — the last route to a
"substantive proved theorem" leads to a 2008 result. R4 is unaffected (the Dinh theorem has no hull
content), and the withdrawal rule for R4 is untouched.

## Phase 3 — P3-8 blocker progress (2026-10-24)

Deliverable `phase3/P3_8_BLOCKER_PROGRESS.md`. **No blocker closed; nothing computed.** After the
P3-7b lesson (search the exact object, not the topic), the four unread bodies were re-searched on
author, title and DOI.

| Blocker | Change |
|---|---|
| **B-2b** | **Fully identified**, record was correct: Debnath & Prakash, *Hulls of Cyclic Codes Over a Local Ring*, ICTIS 2025, SIST **325**:309–319, DOI `10.1007/978-981-95-1365-9_25`. Abstract quoted verbatim (`Z_{p^3}`, count of all cyclic codes **for a fixed hull `p`-dimension**, no distance). Body paywalled. **Still open** |
| **B-2a** | Body still paywalled — but a **Correction** exists: *Correction to: Galois hulls of constacyclic codes over finite fields*, Cryptogr. Commun. **15**:129–130 (2023), DOI `10.1007/s12095-022-00602-6` (clarifies a primitive element of `F_8`). So B-2a is **two** unread documents. Blocker **slightly worse**, not better. **Still open** |
| **B-1** | unchanged; publisher bodies inaccessible |
| **Tian–Gao–Gao** | no preprint located by search (stated as "not located", not "does not exist"); body unread |
| **Line scope, from a full text we can read** | arXiv:2412.08512 (Debnath–Islam–Martínez-Moro–Prakash, *Discrete Math.* 349 (2026) 18) read directly: `k`-Galois hull dimension formula, LCD/dual-containing conditions, EAQECC examples; its counting object is `delta_k(n,q,lambda)` = **number of distinct attainable hull dimensions**; **no distance distribution anywhere**; it also independently describes the source paper's contribution as "Hermitian hull dimensions + Hermitian LCD conditions" |

**What is still not established:** that none of B-1/B-2a/B-2b/Tian–Gao–Gao contains a joint
`(hull, distance)` distribution. **R4 is not withdrawn and not promoted; novelty still claimed
nowhere; Phase 9 remains NO-GO.**

**Distinction sharpened (with sources):** B-2a gives a *marginal* count of codes by Galois hull
dimension; arXiv:2412.08512 gives only the *number of distinct attainable hull dimensions*; B-2b gives
a marginal count over `Z_{p^3}` with no Gray map. R4 asks for the *joint* `(dim Hull_H, d)` law over
`R_e` **together with its Gray image** — and P3-1 already showed the joint law is not the product of
its marginals (independence violations 5, 5, 11, 2, 3, 9). A distinction in **kind**, not an absence
claim.

**Next action on B-2a recorded:** request **both** `10.1007/s12095-022-00591-6` **and** its
Correction `10.1007/s12095-022-00602-6`; requesting only the original would repeat a known-incomplete
read.

## Phase 3 — P3-9 regression audit: every log reproduces (2026-10-25)

Deliverable `phase3/P3_9_REGRESSION_AUDIT.md`; tool `tools/verify_logs.py`;
full-run log `logs/VERIFY_LOGS_full.txt`.

**Result: 14 of 14 probes reproduce, 0 failures, exit 0. 836 log lines compared.
`QUANTUM_CODE_PARAMETER_TABLE.csv` regenerates byte-identically (504 rows).**

| Item | Detail |
|---|---|
| Method | re-run each committed script from the repo root with `PYTHONHASHSEED=0`, capture stdout, compare line-by-line with the committed log; exit code must be 0 |
| Tolerated differences | only text the *logging command* wrote: elapsed-time lines, the `# ... generated <timestamp>` banner, the `Python 3.11.x` interpreter line, `## <script>.py --` part headers, one recorded historical `numpy: ModuleNotFoundError` line, and the trailing CSV dump (replaced by a byte-for-byte CSV check) |
| Not tolerated | any changed digit anywhere; the report prints the first differing line with both versions |
| Structure found | `r1_probe_log.txt` (2 parts), `r2_probe_log.txt` (1), `r3_probe_log.txt` (3) are **composite** logs and need two or three scripts to regenerate — recorded so a re-runner does not produce a truncated log and mistake it for missing evidence |
| History found | `p3_quantum_table_log.txt` deliberately preserves the pre-rewrite `numpy: ModuleNotFoundError`; it is skipped explicitly rather than quietly deleted |
| Strongest single check | the 504-row CSV is snapshotted before the run and must be byte-identical after; `git status` is clean after the full run |

**What it establishes:** the package is internally reproducible — run the committed code, get the
committed output, including the largest deliverable.
**What it does not establish:** correctness (a script that reproduces a wrong number reproduces it
faithfully — this is a drift check, not a proof), novelty (blockers unchanged), or that Phase 9 should
be written. **Phase 9 NO-GO is unchanged.**

Excluded, and why: `tools/preflight.py` (needs `pypdf`, absent), `tools/selftest_gate.py` (environment
gate, PASS 7/7, no committed log), the acquisition/inventory tools (bound to the network and to the
source PDF, which `PHASE0_VERIFICATION_LOG.md` pins by sha256), and `code/phase1_*.py` (outputs quoted
inside `phase1/*.md`).

## Phase 3 — P3-10 the e = 2 Gray image is |u|u+v|, distance exact (2026-10-25)

Deliverable `phase3/P3_10_GRAY_E2_UV.md`; probe `phase3/p3_nested_gray.py`
(log in the P3-9 regression set, exit 0, 501 s, stdlib only).

**Theorem P3-10 (proved, elementary).** For `q` odd and linear codes `C_2 <= C_1` of length `n` over
`F_q`, the `e = 2` Gray map `psi(c_1,c_2) = (c_1+c_2, c_1-c_2)` satisfies

    psi(C_1 x C_2) = { (u, u+v) : u in C_1, v in C_2 }        (the |u|u+v| / Plotkin-sum code)

and therefore `d(psi(C_1 x C_2)) = min { 2 d(C_1), d(C_2) }`.

| Item | Detail |
|---|---|
| Proof | substitute `u = c_1+c_2`, `v = -2c_2`; bijection needs only `C_2 <= C_1` and `2` invertible; triangle inequality for the lower bound, `u = 0` for the upper |
| Verification | **878 nested pairs, 0 disagreements**, 22 `(p,n)` cases with `p` in 3..13 and `n` in 2..6, `gcd(n,p)=1` |
| Hypothesis is necessary | the same sweep finds **2915 non-nested pairs** where the formula fails |
| Relation to P3-3 Thm 2 | `min{2d_1,d_2} <= 2d_1 = e min d_l`, so the new value sits inside the old band and is exact, not a bound; it equals `e min d_l` only when `d_2 >= 2 d_1` |
| **Provenance** | this is the **classical** `|u|u+v|` construction: van Lint, IEEE TIT 37(2):343-345 (1991); Castagnoli et al., IEEE TIT 37(2):337-342 (1991); restated as Thm 2.1 of arXiv:2402.02853. **Re-derived, not new** |
| Forward value | for nested `e = 2`, `d(psi)` is a *function* of `(d(C_1),d(C_2))`, so R4's joint law collapses to a deterministic map on the field-level joint law (hull dimensions add by P3-3 Thm 1). The distribution is then a computation, not a new structural problem |
| Consistency with P3-3 Thm 5 | the non-determination witness `(d_1,d_2) = (3,3)` giving `d(psi) in {3,4,5}` must be **non-nested** — exactly where the sweep finds the formula failing. The two results agree |
| Not done | `e >= 3` untouched (`|u|u+v|` is specific to `e = 2`); hull side untouched; blockers unchanged |

**Same pattern as P3-7b:** a question carried in this project as "bounded / open" is settled in the
literature. **Phase 9 remains NO-GO** — a re-derived classical formula is not a new theorem.

## Phase 3 — P3-11 exact joint (hull, distance) law, nested e = 2 (2026-10-25)

Deliverable `phase3/P3_11_JOINT_NESTED_E2.md`; probe `phase3/p3_joint_nested_e2.py`
(log 112 lines, exit 0, 428 s, stdlib only).

**This is the object R4 asks for, on the one sub-family where both coordinates are determined.**
`e = 2` with `C_2 <= C_1`: distance exact by P3-10 (`min{2d_1,d_2}`), hull exact by P3-3 Thm 1
(additive).

| Item | Detail |
|---|---|
| Enumeration | all nested pairs of cyclic codes over `F_9`, `lambda = (1,1)`, `n in {2,4,5,7,8}` (`psi`-lengths 4,8,10,14,16), `gcd(n,3)=1` |
| Pairs | **3368** with both components nonzero |
| Independent cross-check | hull computed **directly** on `psi(C)` from its own generator matrix for all 3368 pairs: **0 failures** vs the additive value |
| Sanity assertions | `conj(x) == x^3` for all `x in F_9`; `x*conj(x) != 0` for `x != 0` |
| Largest table | `n = 8`, 3270 pairs, `h in 0..4`, `d in 2..8`; counts printed cell by cell |
| **R4 finding** | (strengthened by P3-12: neither `lambda=(1,1)` nor nesting is needed for it) the joint law is **NOT the product of its marginals**: TV = **0.2078** at `n = 5` (19 pairs) and **0.1753** at `n = 8` (3270 pairs), exact rational arithmetic. Independence holds only where one marginal is degenerate (`h = 0` throughout at `n = 2,4,7`), so those cases are uninformative |
| Consequence | P3-1's "joint law is not a product" is **not** an artefact of the non-determined regime. A hull-dimension-only count (what B-2a and B-2b do) cannot reproduce this table — a difference in **kind**, now shown by exhaustive enumeration |
| Not claimed | not a theorem (finite enumeration); not new mathematics (P3-10 is classical `|u|u+v|`); general `C_2` not subset of `C_1` still governed by P3-3 Thm 5; **no** claim that these parameters are good; **no** novelty claim while B-1/B-2a/B-2b/Tian-Gao-Gao are unread |

**Phase 9 remains NO-GO** — a distribution table is not the "substantive proved theorem" the
blueprint requires.

## Phase 3 — P3-12 the non-product finding survives removing P3-11's hypotheses (2026-10-25)

Deliverable `phase3/P3_12_LAMBDA_ROBUSTNESS.md`; probe `phase3/p3_lambda_robust.py`
(log in the verify_logs set, exit 0, 1.0 s, stdlib only).

P3-11 assumed `lambda = (1,1)` (both components cyclic) and `C_2 <= C_1` (nested). **Both are removed
here.** Nesting is dropped by measuring `d(psi)` directly as `min w(c_1+c_2) + w(c_1-c_2)`; `lambda` is
dropped by running all four `lambda in {+1,-1}^2`, so components are cyclic **or negacyclic**.

| `n` | scope | pairs | result |
|---|---|---|---|
| 2 | all pairs, 4 lambda | 15 / 7 / 7 / 3 | independence holds but is **VACUOUS** (`h` has one value) |
| 3 | all pairs, 4 lambda | 15 each | **NOT independent** for `(+,+)` TV=0.2200, `(+,-)` TV=0.1689, `(-,+)` TV=0.1689; vacuous for `(-,-)` |
| 4 | nested only (cost 10^8 otherwise), `(1,1)` and `(-1,-1)` | 65 / 1 | vacuous |

**Conclusion at the strength the data supports: in every case where the independence test is not
vacuous, it fails.** 0 direct-hull cross-check failures over all 150 words-pairs enumerated.

| Item | Detail |
|---|---|
| Vacuity control added | an earlier version reported "independent" for degenerate rows; the probe now prints `h`-value and `d`-value counts and flags vacuity. **Every** "independent" row in this sweep turned out to be vacuous — the distinction is the whole finding |
| Symmetry check | `(+,-)` and `(-,+)` give identical TV and identical tables, as required by component swap |
| Most informative case | `n = 3`, `lambda = (+,-)`: components are genuinely different classes (cyclic x negacyclic), no nesting formula available, distance measured not deduced — and still not a product |
| Feasibility stated | `n = 4` all-pairs costs 10^8 word-pairs (out of reach); mixed `lambda` at `n = 4` has no nontrivial nesting because `gcd(x^n-1, x^n+1)` divides 2 — skipped **by reasoning**, not by omission |
| Not claimed | not a theorem (small finite tables); no proof that the joint law can never be a product; no novelty claim; blockers unchanged |

**Phase 9 remains NO-GO.**

## Next step

**The blueprint's deliverable set is now complete through Phase 8.** Every named file exists except the
manuscript (Phase 9), which is deliberately withheld.

Only two kinds of work remain, and neither is mine to do unilaterally:

1. **Library access** — **B-2a** (Debnath–Prakash–Islam 2023 body **and now also its Correction**,
   DOI `10.1007/s12095-022-00602-6`), **B-2b** (ICTIS 2025 chapter, DOI
   `10.1007/978-981-95-1365-9_25`), **Tian–Gao–Gao** QIP 2024 full text. If any contains a joint
   (hull, distance) distribution for a constacyclic family, the R4 contribution is **withdrawn**, not
   narrowed. See `P3_8_BLOCKER_PROGRESS.md`: three of the four bodies are now identified to DOI
   level, so an interlibrary request can be made precisely.
2. **A structural idea** for the one restricted family where `d(ψ)` is determined (`σ = 1` is the only
   known case). Without it there is no route to the primary objective.

The third option that existed at the end of P3-7 — *decide L-2 and turn it into a theorem* — is now
**gone**: P3-7b shows L-2 is Dinh's 2008 theorem. It was never a contribution. Nothing on the distance
side of the single-orbit family is left to settle.

Everything computable at this scale has been computed, cross-checked, and now **re-verified
end-to-end**: P3-9 re-runs all 14 probes and reproduces 836 log lines exactly, plus the 504-row CSV
byte-for-byte. There is no remaining computational step at this scale. Both remaining items require
material this workspace does not have — library access (B-1, B-2a + its Correction, B-2b,
Tian–Gao–Gao) or a new structural idea — so further "proceed" turns have nothing legitimate left to
execute, and manufacturing activity would violate the standing rule against it.

R1, R2, R3 remain NO-GO; Gate 2 stands on R4; novelty claimed nowhere; L-1, L-3 … L-8 open, **L-2 closed by citation (Dinh 2008)**; source PDF
re-verified 612 826 B / sha256 `7f7e6803…`.

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
