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
