# SOURCE_INVENTORY

**Audit date:** 2026-10-20 (UTC)
**Branch:** `arena/1625045b-galios-hull`
**Rule applied:** nothing is assumed to exist because a filename appears in a plan.
Every entry below was produced by `ls`, `sha256sum`, `unzip -l` or `find` in this
workspace on the audit date.

---

## 1. Uploaded input (the only file supplied for this task)

| # | Path | Bytes | SHA-256 |
|---|---|---|---|
| U1 | `/tmp/arena-coding-uploads/Arena_Master_Research_Blueprint.pdf` | 88,470 | `abcecc47d8eb64226a8c82518c9e43f9b5961a1ef45e47c3685cd5f95842ae23` |

MD5: `77eddbbfa986185f1b588c61aea8c8c5`.
Producer: `ReportLab PDF Library`; Author field `OpenAI`; 7 pages; 18,042 characters
of extractable text. Fully extracted to `/home/user/work/blueprint.txt`.
This is an instruction document, **not** a mathematical source. It contains no
theorems and is not citable.

## 2. The exact mathematical source PDF (matched, read in full)

| # | Path | Bytes | SHA-256 |
|---|---|---|---|
| S1 | `Galios hulls of constacclic codes over affine algebra rings'.pdf` | 291,546 | `0db90bfbeda69ad1af231b81d92f24be3589ed15ac2e0ade6605ba7ad0ddc039` |
| S1′ | `references/source-paper.pdf` **inside** `Galios-Hull-Submission-Phase10F.zip` | 291,546 | `0db90bfbeda69ad1af231b81d92f24be3589ed15ac2e0ade6605ba7ad0ddc039` |

**S1 and S1′ are byte-identical**, so the copy of the source inside the prior
submission package is the same document. (Checked by extracting the archive to a
temporary directory and hashing; the extraction was then discarded — it is
reproducible with `unzip` and is a duplicate of the ZIP.)

27 pages, 54,586 characters of extractable text,
fully extracted to `/home/user/work/source_paper.txt` and read end to end
(pages 1–27, including all proofs, the 13-row table and all 44 references).

> The uploaded filename is misspelled and is *not* a reliable identifier.
> Identity was established from the PDF metadata and the article body, not the
> filename. See `SOURCE_PAPER_METADATA.md`, which records a **bibliographic
> mismatch with the blueprint**.

## 3. Prior project package found in the repository

| # | Path | Bytes | Note |
|---|---|---|---|
| P1 | `Galios-Hull-Submission-Phase10F.zip` | 1,152,081 | `6fd1a675fa4d780db71631156ddc8bd1554d517348ba24264bf2a0cccce2ad12` |
| P1′ | (archive contents, inspected in a temporary extraction) | 2.3 MB, 102 files | contents listed by `unzip -l`; extraction discarded after inspection |

The archive `MANIFEST.txt` declares:
`branch arena/01a0c9d2-galios-hull`, `commit 360c1ef9b870ca4da89ab4ff2c92ff60d1d3dbe5`,
generated `2026-09-25T15:57:34Z`, 58 SHA-256 entries.

Contents by kind:

- `manuscript/main.tex` (50,635 B) + `main.pdf` (478,856 B) + `references.bib`
  — a *complete drafted manuscript* from the prior branch, titled
  **"Exact Joint Enumeration of k-Galois Hull Dimensions for Labeled Constacyclic
  Codes over Square-Free Affine Algebras."**
- `validation/` — 33 markdown audit documents plus 40+ `.out` logs and 6 `.py` checkers.
- `code/` — 7 validation scripts.
- `traceability/` — `GIT_LOG.txt`, `FINAL_STATE_SHA256.txt`, `phase10f_source_changes.diff`.
- `references/source-paper.pdf` — byte-identical to S1.
- `blueprint/new-paper-blueprint.md` (152,972 B) — a prior, much longer blueprint
  for the same project.

### 3.1 Why this matters for Phase 0 (conflict inventory)

The prior package already audited the *same* source paper (arXiv:2412.08512v1) and
already drafted a manuscript on the *same* object this session is being asked to
judge. Its own self-assessment is unusually candid and must be recorded, because
this audit either confirms or overturns it:

- `validation/NOVELTY_BOUNDARY.md` line 5:
  *"**Decision:** no priority, 'first,' 'new,' or state-of-the-art claim is
  authorized by this audit."*
- `validation/NOVELTY_BOUNDARY.md` NB-07: the trace/bivariate product is classed
  `POTENTIALLY DISTINCT`, explicitly *"not a priority claim."*
- NB-08: the global labeled `u,z` enumerator is classed `NOT ESTABLISHED`.
- `validation/CONTRIBUTION_BOUNDARY.md`: the repository *"cannot support"* the
  statement that *"exact hull-dimension enumeration is new in coding theory"*, nor
  that the work is *"the first enumeration over a finite ring, affine algebra,
  non-chain ring, or constacyclic family."*
- `validation/FINAL_REFERENCE_AUDIT.md` R2 and R9 already record the same
  bibliographic split found in §4 below: the readable theorem-bearing record is
  **arXiv:2412.08512v1**, while **Yadav et al. 2024** is a *narrower Hermitian
  non-chain-ring comparison*.

**Independent position of this audit:** the prior package's conclusions are
*consistent* with the findings below but are not treated as evidence. Every
literature and novelty statement in this audit was re-derived from primary
records on 2026-10-20, and two precedents are added that the prior package does
not appear to have used (Shukla–Pandey–Mishra–Pathak–Upadhyay, *Adv. Math.
Commun.* 2025; Debnath–Prakash, *Adv. Math. Commun.* 19 (2025) 1569–1604).

## 4. Conflicting source identities (critical)

| Claim source | Named source paper | Actual identity of S1 |
|---|---|---|
| Blueprint p.1 and p.2 | Yadav, Singh, Islam, Prakash, Solé, *"Hermitian hull of constacyclic codes over a class of non-chain rings and new quantum codes"*, Comput. Appl. Math. **43** (2024) 269, DOI `10.1007/s40314-024-02789-1` | Debnath, Islam, Martínez-Moro, Prakash, *"Galois hulls of constacyclic codes over affine algebra rings"*, arXiv:2412.08512v1 |

These are **different papers** with different rings, different inner products and
different main theorems. The blueprint's own mathematical description on page 2–3
(`R_e = F_{q^2} + uF_{q^2} + … + u^{e−1}F_{q^2}`, `u^e = 1`, `e | (q+1)`,
Hermitian hull) matches **Yadav et al.**, *not* the uploaded PDF.

Notably, Yadav et al. is reference **[43]** of the uploaded paper, and the uploaded
paper cites it in its own introduction. So the two documents are related, but one
cannot audit the other's theorems.

**Consequence:** every deliverable in this project audits **S1 (Debnath et al.)**,
and states explicitly where a claim would read differently under the Yadav et al.
convention. No theorem from Yadav et al. is asserted as verified here.

## 5. Artifacts deliberately *not* created

Following blueprint §0 ("never infer that a file exists from a planned filename")
and §11 ("do not place large generated artifacts in the repository"):

- No manuscript, LaTeX source or PDF was produced in this session.
- No data set larger than a few KB was written.
- The 2.3 MB extraction of P1 was temporary; it was discarded after inspection and
  is reproducible with `unzip`. The authoritative artifact remains the original ZIP.
- Total size of `research_project/` is ~216 KB.
