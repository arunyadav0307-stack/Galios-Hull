# REPOSITORY-WIDE SEARCH FOR THE YADAV ET AL. PDF

**Run:** 2026-10-23 · **Branch:** `arena/831a2e65-galios-hull` @ `f8a892c`
**Question:** is the designated source paper (DOI `10.1007/s40314-024-02789-1`)
already present somewhere in the repository or on the machine?

**Answer: no. Six PDFs exist; none is the Yadav et al. article.** Every check below
was executed in this session; the commands are reproducible.

---

## 1. Scope of the search

| # | Where | Method | Result |
|---|---|---|---|
| 1 | Working tree (repo root + `research_project/`, all depths) | `os.walk` for `*.pdf`, then identity test on each | 6 PDFs, **0 accepted** (§3) |
| 2 | **All 11 remote branches** (`main` + 10 `arena/*`) | `git ls-tree -r -l`, read every blob ≥ 10 kB, test magic bytes | 349 distinct blobs scanned; PDFs found only on 4 branches, all manuscripts or the Debnath preprint; **no Yadav PDF** |
| 3 | Git history / unreachable objects | `git log --all`, `git fsck --lost-found` | 3 commits on this branch, no dangling objects, nothing to recover |
| 4 | Both committed ZIPs, every entry | magic-byte test (`%PDF-`, `PK`, gzip, base64-`%PDF`) on all 155 + 102 entries, not just `.pdf` names | 5 PDF entries: 3 × Debnath preprint (291 546 B, `0db90bfb…`) and 2 × the prior 19-page manuscript; **no Yadav PDF** |
| 5 | Whole filesystem | `find / -xdev` for `*.pdf`, `*yadav*`, `*s40314*`, `*hermitian*`, excluding `/usr /opt /proc /sys` | only `/tmp/bp.pdf` (the blueprint) and the repo files |
| 6 | Agent scratch areas | `/tmp`, `/tmp/arena-workspace`, `/mnt`, `/media`, `/srv`, `/home` | only this session's own logs and diff artifacts |
| 7 | Content search for the DOI / title in every blob of every branch | substring scan over 349 blobs | 19 files mention `s40314-024-02789`; **all are bibliography/audit text** (prior `new-paper-blueprint.md`, `FINAL_REFERENCE_AUDIT.md`, our own metadata files) — no article body |

## 2. Why a "find by filename" is not enough

The 6 PDFs do not carry the article's name, so identification was done by
**content**, using `tools/find_and_verify_source.py`, which applies four checks to
each file: rejection of the known wrong paper, title presence, all five author
surnames, and DOI or journal name.

## 3. Result table (verbatim output of the gate)

```
PDF                                                                   pp  verdict  reason
Galios hulls of constacclic codes over affine algebra rings'.pdf      27  reject   this is Debnath et al.
research_project/prior_art/…/01_Paper_Package/manuscript/main.pdf     19  reject   title not found; missing ['yadav','singh',…]
research_project/prior_art/…/01_Paper_Package/references/source-paper.pdf  27  reject   this is Debnath et al.
research_project/prior_art/…/03_Source_Paper/source-paper-arXiv-2412.08512v1.pdf 27 reject  this is Debnath et al.
research_project/prior_art/…/kGalois-Phase10F/manuscript/main.pdf     19  reject   title not found; missing ['yadav','singh',…]
research_project/prior_art/…/kGalois-Phase10F/references/source-paper.pdf  27  reject   this is Debnath et al.

PDFs examined: 6   accepted: 0

GATE 0: BLOCKED — no PDF in the repository is the source paper.
```

Note the de-duplication: four of the six are byte-identical copies of one file
(`0db90bfb…`, the Debnath preprint), and two are byte-identical copies of the prior
`k`-Galois manuscript (`a4cbae94…`). The repository holds **two distinct documents**,
neither of which is the source paper.

## 4. What this rules out

* It is not "hidden under another name" — every file was opened and read, not
  merely listed.
* It is not on a previous session's branch — all 10 `arena/*` branches were fetched
  and their blobs inspected.
* It is not inside the archives under a misleading name — all entries were tested by
  magic bytes.
* It is not elsewhere on the machine — a filesystem-wide search found nothing.

## 5. The one action that unblocks Phase 1

Put the file in the prepared directory (any filename ending `.pdf`):

```
research_project/source_paper/
```

then, from the repository root:

```bash
python3 research_project/tools/find_and_verify_source.py --record
```

The script walks the tree, tests every PDF, prints a verdict per file, and records
the accepted one with its SHA-256 in `source_audit/SOURCE_PDF_MANIFEST.csv`. It
exits 0 only when exactly one file passes; it refuses the Debnath preprint and the
prior manuscripts by construction.

If the file has to come from the web, the author deposit is at
`https://hal.science/hal-04825601v1/file/Hermitian%20hull%20of%20constacyclic%20codes%20and%20quantum%20Codes.pdf`
(downloadable in an ordinary browser; this sandbox's egress is allowlisted and the
host additionally serves an interactive bot challenge — see
`SOURCE_ACCESS_STATUS.md` §2, routes 8–9).

## 6. Status

* Gate 0: **BLOCKED** — the source document is absent, not mislaid.
* Phase 1: **not started**; no theorem register, glossary, audit or example
  recalculation exists for Yadav et al.
* Nothing in this search modified or deleted any file.
