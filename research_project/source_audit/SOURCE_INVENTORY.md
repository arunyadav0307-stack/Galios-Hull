# SOURCE INVENTORY — Phase 0

**Generated:** 2026-10-23 (UTC) · **Branch:** `arena/831a2e65-galios-hull`
**Method:** every figure below was produced by a command recorded in
`PHASE0_VERIFICATION_LOG.md`; every hash is SHA-256 and lives in
`FILE_MANIFEST.csv` (260 rows: 3 root artifacts + 155 + 102 extracted files).

---

## 1. What the repository actually contains

`git ls-tree -r HEAD` at `33aeb795a53e72d87856b6a255652c2acad41b0b` ("Add files via
upload", 2026-10-20 21:29:17 +0530) returns **exactly three blobs**:

| Path (repository root) | Bytes | SHA-256 | Type |
|---|---:|---|---|
| `Galios hulls of constacclic codes over affine algebra rings'.pdf` | 291 546 | `0db90bfbeda69ad1af231b81d92f24be3589ed15ac2e0ade6605ba7ad0ddc039` | PDF, 27 pp. |
| `Galios-Hull-Complete-Work-2026-10-20.zip` | 1 644 180 | `c192e76c43d828ad879a7bba8494b11b44981969a0a6295203e0d7ae389d3179` | ZIP, 169 entries / 155 files |
| `Galios-Hull-Submission-Phase10F.zip` | 1 152 081 | `6fd1a675fa4d780db71631156ddc8bd1554d517348ba24264bf2a0cccce2ad12` | ZIP, 110 entries / 102 files |

There is no README, licence, data directory, build configuration or `.gitignore` at
the root. The working tree was clean before this session's work; the only branch
beyond `main` is the session branch.

**Filename note (recorded, not corrected):** the uploaded PDF's filename contains
"Galios" (for *Galois*), "constacclic" (for *constacyclic*), and an unbalanced
apostrophe before `.pdf`. The file is preserved exactly as uploaded; its internal
metadata title is correct (see `SOURCE_PAPER_METADATA.md`).

## 2. The two ZIP archives

Both archives open without error (`zipfile.testzip()` returns `None`); neither
contains nested archives or duplicate member names.

| Archive | Root(s) | Files | Uncompressed bytes |
|---|---|---:|---:|
| `Galios-Hull-Complete-Work-2026-10-20.zip` | `Galios-Hull-Complete-Work-2026-10-20/` | 155 | 3 046 562 |
| `Galios-Hull-Submission-Phase10F.zip` | `Galios-Hull-kGalois-Phase10F/` | 102 | 2 156 750 |

**Relationship between them (verified by hash, not by reading names):**
`Galios-Hull-Complete-Work-2026-10-20/01_Paper_Package/` is **byte-identical** to
the entire `Galios-Hull-kGalois-Phase10F/` tree. All 102 files of the second
archive reappear with identical SHA-256 in the first. The remaining 53 files of
the first archive are `00_START_HERE.md`, `03_Source_Paper/…` (a copy of the root
PDF, same hash) and the 51 files of `02_F11_Audit/`.

```
CompleteWork = 01_Paper_Package (102, == Phase10F) + 02_F11_Audit (51) + 00_START_HERE.md + 03_Source_Paper (1)
             102 + 51 + 1 + 1 = 155
```

**Inventory arithmetic discrepancy:** `00_START_HERE.md` states "**Total:** 154
files across three folders". The actual count is 155. The likely cause is that the
note was written before it was added to the archive. Recorded as a cosmetic
discrepancy; no file is missing.

## 3. Prior-art trees (extracted, not tracked)

Extraction is reproducible with `tools/extract_prior_art.sh`, which first verifies
both ZIP hashes and refuses to extract on mismatch. The extracted trees live in
`research_project/prior_art/` and are excluded from Git (see `.gitignore`) because
they are byte-identical copies of committed archives.

| Folder | Files | Bytes on disk | Content |
|---|---:|---:|---|
| `prior_art/Galios-Hull-Complete-Work-2026-10-20/` | 155 | 3.3 MB | combined archive (paper package + F11 audit + source paper) |
| `prior_art/Galios-Hull-kGalois-Phase10F/` | 102 | 2.3 MB | submission package only |

### 3.1 `01_Paper_Package/` (102 files) — a *completed manuscript package*

| Sub-path | Files | What it is |
|---|---:|---|
| `manuscript/main.tex` | 1 | 50 635 B, SHA-256 `b5c038f5540960a1683cc3cb97d574dcaccb178fa86821e4a29f70ce82581fdd` |
| `manuscript/main.pdf` | 1 | 478 856 B, 19 pp., SHA-256 `a4cbae942887235f5d5f288535d74170c9ea3b562652283569433cf581b43397` |
| `manuscript/references.bib` | 1 | 4 080 B, SHA-256 `acc788ee15a476e163a4142d8ba081aaa0634543583df07a9afd035d186765cd` |
| `code/` | 8 | validation scripts (`validate_pilot.py`, `validate_global_product.py`, …) |
| `validation/` | 79 | Phase 2 → Phase 10F audit reports and `.out` transcripts |
| `references/` | 2 | `source-paper.pdf` (== the root PDF) + `README.md` |
| `blueprint/` | 2 | `new-paper-blueprint.md` (152 972 B) + `README.md` |
| `tools/` | 2 | `build_pdf.sh`, `run_all_validations.sh` |
| `traceability/` | 3 | `GIT_LOG.txt`, `FINAL_STATE_SHA256.txt`, `phase10f_source_changes.diff` |
| root docs | 3 | `MANIFEST.txt`, `README.md`, `SUBMISSION_CHECKLIST.md` |

Counts reconcile: 3 + 1 + 1 + 1 + 8 + 79 + 2 + 2 + 2 + 3 = **102**.

Manuscript title (from `main.tex` and `main.pdf` p. 1):
*"Exact Joint Enumeration of $k$-Galois Hull Dimensions for Labeled Constacyclic
Codes over Square-Free Affine Algebras"* — a `k`-Galois enumeration over square-free
**affine algebra** rings, i.e. a study of the paper that *is* present, not of the
paper the blueprint names.

**Integrity check that passed:** the 101 hash/size entries of
`01_Paper_Package/MANIFEST.txt` were re-verified file by file — **101 OK, 0 missing,
0 mismatched** (log §5). The package is internally consistent.

**Provenance that could not be verified:** the same `MANIFEST.txt` says it was
generated on branch `arena/01a0c9d2-galios-hull` at commit
`360c1ef9b870ca4da89ab4ff2c92ff60d1d3dbe5`. Neither the branch nor the commit exists
in this repository (which has a single commit, `33aeb79`, and no such ref). The
artifact's *content* is verifiable; its *history* is not.

### 3.2 `02_F11_Audit/` (51 files) — a *later, contrary audit*

Contains a second, independent Phase 0–2 record with the same deliverable names
this project uses (`SOURCE_INVENTORY.md`, `SOURCE_PAPER_METADATA.md`,
`ENVIRONMENT_CAPABILITIES.md`, `PROJECT_PLAN.md`, `PHASE_STATUS.md`,
`SOURCE_THEOREM_REGISTER.md`, …), 11 Python programs, 31 verification/literature
files, and three outgoing correspondence drafts
(`EVIDENCE_REQUEST_TO_AUTHOR.md`, `ILL_REQUEST_TO_LIBRARY.md`).

Its headline status (`02_F11_Audit/PHASE_STATUS.md`): Phase 0 PASS, Phase 1 PASS,
**Gate 2 FAIL for the joint enumerator**, "Phases 3–11 BLOCKED", "no
`MAIN_THEOREMS_AND_PROOFS.md`, no `paper/main.tex`, no PDF".

**Direct conflict with §3.1:** a complete `paper`-equivalent (`manuscript/main.tex`
+ 19-page `main.pdf`) *does* exist in the same archive, dated 2026-09-24, i.e.
*before* the audit of 2026-10-20. The audit's "no paper" sentence describes the
audit's own branch state, not the archive. Both artifacts are preserved; neither is
adopted as authority. The conflict is registered in `PRIOR_ART_REGISTER.md` §3.

### 3.3 `03_Source_Paper/`

`source-paper-arXiv-2412.08512v1.pdf` — 291 546 B, SHA-256 `0db90bfb…c039`,
identical to the root PDF. Confirms that the uploaded PDF is the arXiv v1 preprint
of Debnath–Islam–Martínez-Moro–Prakash.

## 4. Sources named by the blueprint but **absent** from the workspace

| Expected item | Status | Evidence |
|---|---|---|
| Yadav–Singh–Islam–Prakash–Solé, *Comput. Appl. Math.* **43** (2024) 269, DOI `10.1007/s40314-024-02789-1` — **full text** | **ABSENT** | no file in either ZIP or at the root matches the title or DOI; the only `source-paper.pdf` files hash to the Debnath et al. preprint |
| Any bibliography database (`.bib`) for the *new* project | ABSENT | the only `.bib` present (`references.bib`, 4 080 B) belongs to the earlier `k`-Galois manuscript |
| Published version of Debnath et al. (*Discrete Math.* **349**(2) (2026) 114750) | ABSENT | not in either archive; publisher version not open access |
| Any dataset, computational input, or verification log for the *Hermitian non-chain-ring* setting | ABSENT | the 11 Python programs present are for the `k`-Galois affine-algebra setting |
| LICENSE / authorship statement for this repository | ABSENT | `git ls-tree` shows three blobs only |

## 5. Missing / conflicting artifacts — summary

| ID | Item | Classification | Consequence |
|---|---|---|---|
| M-1 | Blueprint's named source paper is not the uploaded PDF | **Conflict — resolved by decision (2026-10-23)** | Yadav et al. is the source of record; Debnath et al. is excluded as a substitute (`SOURCE_IDENTITY_BLOCKER.md`) |
| M-2 | Yadav et al. full text unavailable in the workspace (publisher paywall; green-OA copy behind an anti-bot challenge) | **Missing — blocking** | Phase 1 cannot start until the PDF is supplied (`SOURCE_ACCESS_STATUS.md`) |
| M-3 | No LaTeX, Magma, Sage, GAP | **Missing — environment** | Phase 9 PDF build impossible here; Phase 7 cross-checks must be self-written |
| M-4 | Prior package claims a branch/commit that does not exist here | **Unverifiable provenance** | prior work is usable as evidence of content only |
| M-5 | Prior archive contains both a completed manuscript and an audit declaring the manuscript stage blocked | **Conflict — internal to prior art** | neither can be assumed correct; both must be re-derived |
| M-6 | `00_START_HERE.md` says 154 files; actual 155 | **Cosmetic** | none |
| M-7 | Uploaded PDF filename is misspelt and apostrophe-terminated | **Cosmetic** | none; file preserved byte-for-byte |

## 6. Files created by this Phase 0 run

All under `research_project/`; nothing pre-existing was modified or deleted.

| Path | Purpose |
|---|---|
| `README.md` | project index |
| `PROJECT_PLAN.md` | scope, phase/gate table, rules, assumptions, risks |
| `PHASE_STATUS.md` | Phase 0 status with per-requirement evidence |
| `source_audit/SOURCE_INVENTORY.md` | this document |
| `source_audit/SOURCE_PAPER_METADATA.md` | bibliographic identification of both papers |
| `source_audit/ENVIRONMENT_CAPABILITIES.md` | tools, versions, network, consequences |
| `source_audit/PRIOR_ART_REGISTER.md` | register of prior artifacts and how they are treated |
| `source_audit/SOURCE_IDENTITY_BLOCKER.md` | the Gate 0 escalation and its options |
| `source_audit/FILE_MANIFEST.csv` | machine-generated SHA-256 inventory (260 rows) |
| `source_audit/PHASE0_VERIFICATION_LOG.md` | commands, outputs, timestamps, deliverable check |
| `tools/inventory.py`, `tools/extract_prior_art.sh` | reproducibility utilities |
| `logs/phase0_*.out` | raw command transcripts |
| `.gitignore` (repository root) | excludes `research_project/prior_art/` |
