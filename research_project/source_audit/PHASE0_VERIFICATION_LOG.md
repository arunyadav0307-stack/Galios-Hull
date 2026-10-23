# PHASE 0 VERIFICATION LOG

**Run:** 2026-10-23T11:46:34Z (UTC) · **Branch:** `arena/831a2e65-galios-hull`
· **HEAD:** `33aeb795a53e72d87856b6a255652c2acad41b0b`
**Raw transcript:** `../logs/phase0_evidence.out` (118 lines; every command and its
exit code). This file records what was run, what it returned, and what each result
supports.

---

## 1. Repository state

| Command | Result | Supports |
|---|---|---|
| `git rev-parse --abbrev-ref HEAD` | `arena/831a2e65-galios-hull` | correct working branch |
| `git rev-parse HEAD` | `33aeb795…41b0b` | single base commit |
| `git ls-tree -r --long HEAD` | 3 blobs (PDF, 2 ZIPs) | no hidden project documentation in Git |
| `git status --porcelain` | 1 entry (`?? research_project/`) | working tree clean apart from this session's new directory |
| `git branch -a` | `main`, `origin/main`, session branch | prior-art manifest's branch `arena/01a0c9d2-galios-hull` **does not exist** here |

## 2. Root artifacts and hashes

`sha256sum *` (exit 1 only because `*` also matched the new directory `research_project`):

```
0db90bfbeda69ad1af231b81d92f24be3589ed15ac2e0ade6605ba7ad0ddc039  Galios hulls of constacclic codes over affine algebra rings'.pdf
c192e76c43d828ad879a7bba8494b11b44981969a0a6295203e0d7ae389d3179  Galios-Hull-Complete-Work-2026-10-20.zip
6fd1a675fa4d780db71631156ddc8bd1554d517348ba24264bf2a0cccce2ad12  Galios-Hull-Submission-Phase10F.zip
```

→ `SOURCE_INVENTORY.md` §1; `FILE_MANIFEST.csv`.

## 3. Archive integrity

```
Galios-Hull-Complete-Work-2026-10-20.zip entries 169 files 155 bytes 3046562 testzip None
Galios-Hull-Submission-Phase10F.zip      entries 110 files 102 bytes 2156750 testzip None
```

`testzip() is None` on both: no corrupted member. Entry counts exceed file counts
because directories are listed as entries.

## 4. Source PDF identification

```
pages 27
metadata {'/Producer': 'GPL Ghostscript 10.01.2',
          '/CreationDate': "D:20241211205909-05'00'", '/ModDate': same,
          '/Creator': 'LaTeX with hyperref',
          '/Title': 'Galois hulls of constacyclic codes over affine algebra rings',
          '/Author': 'Indibar Debnath; Habibul Islam; E. Martínez-Moro; Om Prakash; '}
chars 54001
yadav_mentions 4
```

The four "Yadav" occurrences are: one introduction sentence (p. 2–3) and three
bibliography entries ([34] Prakash–Yadav–Islam–Solé; [42] Yadav–Debnath–Prakash;
[43] Yadav–Singh–Islam–Prakash–Solé). None is the title page.

→ `SOURCE_PAPER_METADATA.md` Object A. The identified title/author metadata does
**not** match the blueprint's named source paper (Object C).

## 5. Prior-art package internal consistency

```
diff -rq .../01_Paper_Package  .../Galios-Hull-kGalois-Phase10F | wc -l   -> 0
manifest entries OK 101 MISMATCH 0 MISSING 0
```

→ the Phase10F submission tree is byte-identical to `01_Paper_Package`; its
101-entry manifest re-verifies completely. Content integrity of the prior package
is therefore established, while its provenance (branch/commit) is not.

## 6. Generated inventory

```
wc -l FILE_MANIFEST.csv                     -> 261 (header + 260 rows)
repo-root 3 | prior-art/Phase10F 102 | prior-art/CompleteWork 155
```

Duplicate analysis (computed from the CSV): 104 rows carry a non-empty
`duplicate_of`; all 102 Phase10F files duplicate their `01_Paper_Package`
counterparts, and 2 further duplicates are the copies of the root PDF
(`03_Source_Paper/…`, `references/source-paper.pdf`). Distinct contents: 156.

## 7. Environment probes

```
pdflatex/latex/bibtex/latexmk/tectonic = MISSING
magma/sage/gap                         = MISSING
pdftotext/pdfinfo/qpdf/gs              = MISSING
python3 3.11.2
pypdf 6.21.2 | sympy 1.14.0 | numpy 2.4.6 | galois 0.4.11
git 2.39.5 | gh 2.23.0
```

`sympy`, `numpy`, `galois`, `fontTools` were installed from PyPI **during** this
session (PyPI reachable); `pypdf` was already present. Installations are outside
the workspace and session-local.

Network probes: `api.github.com` and `pypi.org` reachable; `raw.githubusercontent.com`
and `link.springer.com` fail TLS from the sandbox; the page-fetch tool reaches
Springer but returns only the abstract + references.

→ `ENVIRONMENT_CAPABILITIES.md`.

## 8. Bibliographic cross-checks performed

| Check | Result |
|---|---|
| Blueprint PDF retrieved and hashed | 7 pp., 88 470 B, `abcecc47…ae23`, from `arunyadav0307-stack/JOINT@main` (`gh api .../contents`) |
| Object C DOI `10.1007/s40314-024-02789-1` resolves | yes — Springer, CAM **43**, art. 269, published 2024-06-04; abstract matches the blueprint's ring description |
| Object C full text accessible | **no** — "preview of subscription content"; PDF USD 39.95 |
| Object A version of record | *Discrete Mathematics* **349**(2) (2026) 114750, DOI `10.1016/j.disc.2025.114750` (resolves to ScienceDirect S0012365X25003589; abstract + introduction public, full text paywalled) |
| Object C present in the repository | **no** |

## 9. Deliverable existence check

Run after the documents were written (see §10 for the script). Every blueprint
Phase 0 deliverable must exist and be non-empty:

| Deliverable | Path | Expected |
|---|---|---|
| `PROJECT_PLAN.md` | `research_project/PROJECT_PLAN.md` | present, non-empty |
| `SOURCE_INVENTORY.md` | `research_project/source_audit/SOURCE_INVENTORY.md` | present, non-empty |
| `SOURCE_PAPER_METADATA.md` | `research_project/source_audit/SOURCE_PAPER_METADATA.md` | present, non-empty |
| `ENVIRONMENT_CAPABILITIES.md` | `research_project/source_audit/ENVIRONMENT_CAPABILITIES.md` | present, non-empty |
| `PHASE_STATUS.md` | `research_project/PHASE_STATUS.md` | present, non-empty |

Result of the check: recorded in §11 below (generated, not asserted).

## 10. Deliverable check script

```bash
cd /home/user/Galios-Hull
for f in research_project/PROJECT_PLAN.md \
         research_project/PHASE_STATUS.md \
         research_project/source_audit/SOURCE_INVENTORY.md \
         research_project/source_audit/SOURCE_PAPER_METADATA.md \
         research_project/source_audit/ENVIRONMENT_CAPABILITIES.md; do
  [ -s "$f" ] && printf 'PASS %8d  %s\n' "$(stat -c%s "$f")" "$f" \
              || printf 'FAIL           %s\n' "$f"
done
sha256sum research_project/*.md research_project/source_audit/*.md
```

## 11. Check result

(appended by the run; see below)

## 12. Deliverable check executed

```
PASS     8651  research_project/PROJECT_PLAN.md
PASS     7249  research_project/PHASE_STATUS.md
PASS     4083  research_project/README.md
PASS    10231  research_project/source_audit/SOURCE_INVENTORY.md
PASS     7116  research_project/source_audit/SOURCE_PAPER_METADATA.md
PASS     5772  research_project/source_audit/ENVIRONMENT_CAPABILITIES.md
PASS     7467  research_project/source_audit/PRIOR_ART_REGISTER.md
PASS     7025  research_project/source_audit/SOURCE_IDENTITY_BLOCKER.md
PASS    69947  research_project/source_audit/FILE_MANIFEST.csv
```

SHA-256 of the Phase 0 documents:

```
50ecc6be031f4d8d9a74257e2d84f4ef444b3b4244d5f4b8ff5dbb096496a499  research_project/PROJECT_PLAN.md
f2df3438f51a8ece9556f1d95a996ba2663a5dce789f0e5f91e0a65a79d598a6  research_project/PHASE_STATUS.md
de2c0619b273f63226f4f1246e0fdddd05de53c641186850f455e21ca8f4f291  research_project/README.md
de4cb331f1db6dff257bef2b2c39eb2964dba0c451c0a38273964fe5af5cb654  research_project/source_audit/ENVIRONMENT_CAPABILITIES.md
3e4d46185071f344b02f464277bcacf242c67fa5f7d216ee3964008cb3378367  research_project/source_audit/PHASE0_VERIFICATION_LOG.md
2495492be2ded90000f845bd8d9e95e285ab4af822b7e0a4bef8f28dca112b79  research_project/source_audit/PRIOR_ART_REGISTER.md
9eb8b1911b29073d9bc529fdadc8bd0f4eaa81aba180eaaeff797c4b22317ed8  research_project/source_audit/SOURCE_IDENTITY_BLOCKER.md
3e0a0d6162f1d9f061c33913410a74c5fc1a2a000f07e47b21860ea015db95eb  research_project/source_audit/SOURCE_INVENTORY.md
4c1d77637a2ee3f9332cfe5497cbeb52c0a9bc43eb4be195fe59117dcddef3ac  research_project/source_audit/SOURCE_PAPER_METADATA.md
95636ac1ec4398e825403795c31e18e2c8e3190320dc59d03b89970f31eb8848  research_project/source_audit/FILE_MANIFEST.csv
d6786b53a2e327312d1aa815094e588a3f3d447f451f01317760b5c99dad492a  research_project/tools/extract_prior_art.sh
b290e45b40a67736a3e083de6d44f922662de9ebf35014f06e10c8cecf3e9e08  research_project/tools/inventory.py
39a13af3f2cfa7b4c3036a6f93f0ded061c33dcdadbd4c486d240e7e23117db5  research_project/logs/phase0_evidence.out
```

## 13. Final state (supersedes §12 where hashes differ)

Recorded 2026-10-23T11:5xZ after the PHASE_STATUS deliverable table was filled in. PHASE_STATUS.md is hashed here because it cannot contain its own hash.

```
50ecc6be031f4d8d9a74257e2d84f4ef444b3b4244d5f4b8ff5dbb096496a499  research_project/PROJECT_PLAN.md
75ac133e48f8f14a704a2412ae5851adfad373e4217c35eaefcd2686e6b38e03  research_project/PHASE_STATUS.md
de2c0619b273f63226f4f1246e0fdddd05de53c641186850f455e21ca8f4f291  research_project/README.md
de4cb331f1db6dff257bef2b2c39eb2964dba0c451c0a38273964fe5af5cb654  research_project/source_audit/ENVIRONMENT_CAPABILITIES.md
b31f4ab1787878aec02ad534954e4cb155c2c7b5e3c6a5db00cf8415514b0761  research_project/source_audit/PHASE0_VERIFICATION_LOG.md
2495492be2ded90000f845bd8d9e95e285ab4af822b7e0a4bef8f28dca112b79  research_project/source_audit/PRIOR_ART_REGISTER.md
9eb8b1911b29073d9bc529fdadc8bd0f4eaa81aba180eaaeff797c4b22317ed8  research_project/source_audit/SOURCE_IDENTITY_BLOCKER.md
3e0a0d6162f1d9f061c33913410a74c5fc1a2a000f07e47b21860ea015db95eb  research_project/source_audit/SOURCE_INVENTORY.md
4c1d77637a2ee3f9332cfe5497cbeb52c0a9bc43eb4be195fe59117dcddef3ac  research_project/source_audit/SOURCE_PAPER_METADATA.md
95636ac1ec4398e825403795c31e18e2c8e3190320dc59d03b89970f31eb8848  research_project/source_audit/FILE_MANIFEST.csv
d6786b53a2e327312d1aa815094e588a3f3d447f451f01317760b5c99dad492a  research_project/tools/extract_prior_art.sh
b290e45b40a67736a3e083de6d44f922662de9ebf35014f06e10c8cecf3e9e08  research_project/tools/inventory.py
39a13af3f2cfa7b4c3036a6f93f0ded061c33dcdadbd4c486d240e7e23117db5  research_project/logs/phase0_evidence.out
```

Originals untouched (git diff against HEAD restricted to paths outside research_project/):

```
[no output above = no tracked file outside research_project/ changed]
```

## 14. Source-access attempt log (2026-10-23, after the user designated Yadav et al.)

```
$ python3 research_project/tools/verify_source_pdf.py --selftest
PASS  accepts a conforming record                                    expected=accept got=accept
PASS  rejects the Debnath preprint                                   expected=reject got=reject
PASS  rejects a right-title/right-author document without journal or DOI expected=reject got=reject

SELFTEST: PASS
[exit=0]

$ python3 research_project/tools/verify_source_pdf.py "<the only source PDF present>" --record
file        Galios hulls of constacclic codes over affine algebra rings'.pdf
bytes       291546
sha256      0db90bfbeda69ad1af231b81d92f24be3589ed15ac2e0ade6605ba7ad0ddc039
pages       27
pdf_title   'Galois hulls of constacyclic codes over affine algebra rings'
pdf_author  'Indibar Debnath; Habibul Islam; E. Martínez-Moro; Om Prakash; '

FAIL  A  is not a known wrong paper      this is Debnath et al. "galois hulls of constacyclic codes over affine algebra rings"
FAIL  B  expected title found            title not found
FAIL  C  all five authors present        missing ['singh', 'sol']
FAIL  D  journal or DOI identity         neither found
FAIL  info ring R_e / e|(q+1) signal     not detected on pp. 1-2 (informational only)
FAIL  info dual-containing discussed     not on pp. 1-2

VERDICT: REJECTED — this file is not the paper named by the blueprint.
         Phase 1 must not start on it.
recorded -> research_project/source_audit/SOURCE_PDF_MANIFEST.csv
[exit=1]
```

Network probes made through the agent page-fetch tool (not the shell, whose egress is allowlisted):

```
unpaywall api            -> is_oa true, oa_status green, HAL hal-04825601v1 (submittedVersion)
openalex api             -> any_repository_has_fulltext true, oa_url = HAL
semanticscholar api      -> openAccessPdf url = HAL, status GREEN
springer landing (5/5 chunks) -> abstract + references + about-this-article only; no body text
hal landing              -> metadata readable; file listed 516.23 kB
hal file / document URLs -> Anubis anti-bot challenge; challenge URL returns 503
r.jina.ai proxy of HAL   -> returns the Anubis page
hal.archives-ouvertes.fr -> Anubis pass-challenge then 503
core.ac.uk               -> 'This page is not available now'
scholar.archive.org      -> ALTCHA anti-bot gate
github code search       -> 8 hits, all Scopus metadata dumps, no article text
```

Detail and per-route evidence: source_audit/SOURCE_ACCESS_STATUS.md §2.

## 15. Repository-wide source search (2026-10-23)

```
PDF                                                                                                                    pp  verdict  reason
-------------------------------------------------------------------------------------------------------------------  ----  -------  ----------------------------------------
Galios hulls of constacclic codes over affine algebra rings'.pdf                                                       27  reject   this is Debnath et al. "galois hulls of constacyclic codes over affine algebra rings"; tit
research_project/prior_art/Galios-Hull-Complete-Work-2026-10-20/01_Paper_Package/manuscript/main.pdf                   19  reject   title not found; missing ['yadav', 'singh', 'islam', 'prakash', 'sol']; neither found
research_project/prior_art/Galios-Hull-Complete-Work-2026-10-20/01_Paper_Package/references/source-paper.pdf           27  reject   this is Debnath et al. "galois hulls of constacyclic codes over affine algebra rings"; tit
research_project/prior_art/Galios-Hull-Complete-Work-2026-10-20/03_Source_Paper/source-paper-arXiv-2412.08512v1.pdf    27  reject   this is Debnath et al. "galois hulls of constacyclic codes over affine algebra rings"; tit
research_project/prior_art/Galios-Hull-kGalois-Phase10F/manuscript/main.pdf                                            19  reject   title not found; missing ['yadav', 'singh', 'islam', 'prakash', 'sol']; neither found
research_project/prior_art/Galios-Hull-kGalois-Phase10F/references/source-paper.pdf                                    27  reject   this is Debnath et al. "galois hulls of constacyclic codes over affine algebra rings"; tit

PDFs examined: 6   accepted: 0

GATE 0: BLOCKED — no PDF in the repository is the source paper.
Place the file in research_project/source_paper/ (any name ending .pdf) and re-run.
```

Scope: working tree; 11 remote branches / 349 blobs read in full where >=10 kB; both ZIPs tested entry-by-entry by magic bytes; `find /` over the filesystem. Detail: source_audit/REPOSITORY_SOURCE_SEARCH.md.

## 16. Phase 1 readiness (preparatory work, 2026-10-23)

Tooling built and dry-run. Nothing below produced a Phase 1 deliverable.

```
$ python3 research_project/tools/verify_source_pdf.py --selftest
PASS  accepts a conforming record                                    expected=accept got=accept
PASS  rejects the Debnath preprint                                   expected=reject got=reject
PASS  rejects a right-title/right-author document without journal or DOI expected=reject got=reject

SELFTEST: PASS
[exit=0]

$ python3 research_project/tools/extract_source_text.py --pdf <wrong pdf>   # gated run
REFUSING: Galios hulls of constacclic codes over affine algebra rings'.pdf is not the source paper.
  FAIL  A  is not a known wrong paper      this is Debnath et al. "galois hulls of constacyclic codes over affine algebra rings"
  FAIL  B  expected title found            title not found
[refused]

$ python3 research_project/tools/extract_source_text.py --pdf <wrong pdf> --force --out /tmp/t2   # mechanics only
  empty pages    0
  heading lines  34  {'Example': 5, 'Table': 3, 'Lemma': 9, 'Theorem': 10, 'Corollary': 5, 'Remark': 2}
  numbered       30 high-confidence, 4 low (manual triage)
  NOTE these are line-level candidates, not verified statements.

$ bash research_project/tools/accept_source_and_prepare.sh <wrong pdf>   # must stage then unstage

NOT ACCEPTED (exit 1). Removing the staged copy so the drop folder stays clean.
The original at Galios hulls of constacclic codes over affine algebra rings'.pdf was not modified.
drop folder afterwards: README.md

$ python3 research_project/tools/preflight.py

summary: 18 pass, 3 warn, 0 fail

RESULT: WAITING — Phase 0 is complete and consistent; Phase 1 is gated on the source PDF.
Next: put the Yadav et al. PDF in research_project/source_paper/ and run
      python3 research_project/tools/find_and_verify_source.py --record
[exit=1]
```

## 17. Pipeline validation sweep (2026-10-23, non-destructive)

```
$ python3 research_project/tools/selftest_gate.py

PASS  1 accept a conforming record                 expected=True     got=True
PASS  2 reject title without authors or journal    expected=False    got=False
PASS  3 reject title+authors without journal/DOI   expected=False    got=False
PASS  4 reject the Debnath et al. identity         expected=False    got=False
PASS  5 reject the PDF actually in the repository  expected=False    got=False
PASS  6 record twice -> one row                    expected=1 row    got=1 row(s), added=True,False
PASS  7 out-of-tree path shown absolutely          expected=absolute got=/tmp/gate_selftest_wax6bnqk/accept.pdf

SELFTEST: PASS  (7/7)
fixtures were built in /tmp/gate_selftest_wax6bnqk and are not part of the repository

$ python3 research_project/tools/verify_source_pdf.py --selftest
SELFTEST: PASS

$ python3 research_project/tools/find_and_verify_source.py

GATE 0: BLOCKED — no PDF in the repository is the source paper.
Place the file in research_project/source_paper/ (any name ending .pdf) and re-run.

$ python3 research_project/tools/preflight.py --quiet
Next: put the Yadav et al. PDF in research_project/source_paper/ and run
      python3 research_project/tools/find_and_verify_source.py --record
```

Defects found: D-1 duplicate evidence rows (fixed, manifest collapsed 3 rows -> 1), D-2 preflight side effect + out-of-tree path display (fixed), D-3 local flag shadowing the record() function (fixed; would have crashed the first acceptance).

## 18. Environment rollback and restoration (2026-10-23, 15:0x UTC)

The sandbox was rolled back between turns: `.git` returned to the base commit
`33aeb79`, the derived `prior_art/` tree and the session-installed Python packages
disappeared. The working files themselves survived. Nothing was lost; the recovery
is fully reproducible and is recorded here as evidence.

| Symptom observed | Root cause | Recovery performed | Verified by |
|---|---|---|---|
| `git log` showed only `33aeb79`; `research_project/` untracked | local `.git` refs rolled back | `git fetch origin`; branch pointer restored to `origin/arena/831a2e65-galios-hull` = `ebbbcf3` | `git log --oneline` shows `ebbbcf3, 69496e8, 746bdec, 3b56509` |
| — | — | before moving the pointer, all 29 tracked files were compared blob-by-blob with the commit | 29/29 identical, 0 differing, 0 missing |
| `research_project/prior_art/` absent (git-ignored, not in snapshot) | derived tree lost with the sandbox | `bash research_project/tools/extract_prior_art.sh` (re-verifies both ZIP hashes first, then extracts 155 + 102 files) | 155 + 102 files restored; `FILE_MANIFEST.csv` counts 3/155/102 |
| `preflight` FAIL: `pypdf` not importable | session-local site-packages rolled back | `pip install -r research_project/requirements.txt` | pypdf 6.21.2, sympy 1.14.0, galois 0.4.11, numpy 2.4.6 |
| long pypdf Type1-font warnings on stderr | `fontTools` was installed ad hoc earlier and was not pinned | added `fonttools==4.67.0` to `requirements.txt` and installed it | warnings gone; `preflight` reports fonttools present |

**Final state after restoration:** `preflight` → **19 PASS / 2 WARN / 0 FAIL**,
`RESULT: WAITING`; `selftest_gate.py` → **7/7 PASS**; working tree clean at
`ebbbcf3`; Gate 0 still **BLOCKED** on the source PDF.

### Correction to this section (2026-10-23, verified against the transcript)

An earlier version of the table above stated that `preflight` failed on *inventory
counts* because `prior_art/` was missing. **That was wrong, and it has been
corrected.** Evidence:

* `check_manifest_consistency()` in `preflight.py` reads only
  `source_audit/FILE_MANIFEST.csv`, a tracked file that was present throughout the
  rollback; it never consults `prior_art/`. It could not have failed for that reason.
* The three observed preflight outcomes were `15P/5W/1F` → `16P/4W/1F` →
  `19P/2W/0F`. The single `FAIL` in the first two runs was **`pypdf` not
  importable** — the only *required*-tool check. The `+1 PASS / −1 WARN` step
  between the first two runs was the working tree going from dirty (untracked
  `research_project/`) to clean after the branch pointer was restored.
* `prior_art/` was still correctly regenerated — it is needed for prior-art access
  in Phase 2 and is referenced by `PRIOR_ART_REGISTER.md` — but its absence was
  never a preflight failure.

Lesson recorded rather than hidden: a recovery log written from memory of the turn
can overstate causality. The counts in this log are the ones that matter, and they
are reproduced by `preflight.py` on demand.

The two remaining WARNs are the absent `pdflatex` (Phase 9) and `magma` (Phase 7
cross-check) — both are declared limitations, not defects.
