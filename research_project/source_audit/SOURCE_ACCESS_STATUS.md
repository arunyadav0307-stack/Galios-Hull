# SOURCE ACCESS STATUS — Yadav et al. (2024)

**Recorded:** 2026-10-23 (UTC) · **Branch:** `arena/831a2e65-galios-hull`
**Designated source of record:** the paper named by the blueprint (user decision, 2026-10-23)
**Gate 0 status:** ~~BLOCKED — source file not yet in hand~~ → **PASS (2026-10-23)**

> **RESOLVED.** The HAL author deposit was supplied by the user, staged at
> `source_paper/Hermitian hull of constacyclic codes and quantum Codes.pdf`
> (612 826 B, 23 pp., SHA-256 `7f7e6803…c27d249`), accepted by the identity gate
> (`GATE 0: PASS`, 7 PDFs examined, 1 acceptance), and its version tag
> `hal-04825601v1` recorded in `SOURCE_PDF_MANIFEST.csv`. The access routes tried
> below are retained as history of the escalation only; **none of them was
> retried**, per the user's instruction. Phase 1 has been executed and Gate 1
> passes — see `../PHASE_STATUS.md`.

---

## 1. The document that is required

| Field | Value |
|---|---|
| Title | Hermitian hull of constacyclic codes over a class of non-chain rings and new quantum codes |
| Authors | Shikha Yadav, Ashutosh Singh, Habibul Islam, Om Prakash, Patrick Solé |
| Journal | *Computational and Applied Mathematics* (Springer), Vol. **43**, Paper **269** (2024), 19 pp. |
| DOI | `10.1007/s40314-024-02789-1` |
| History | received 2023-12-02 · revised 2024-04-08 · accepted 2024-05-21 · published 2024-06-04 (version of record) |
| MSC | 94B05, 94B15, 94B35, 94B60 |
| Keywords | Hull of linear codes; Hull dimension; LCD codes; Gray map; Quantum codes |

## 2. Every access route attempted, and what it returned

| # | Route | Result | Evidence |
|---|---|---|---|
| 1 | Search the repository root and both committed ZIPs by filename, title and DOI | **absent** — the only PDFs are four copies of the Debnath et al. preprint (`0db90bfb…`) and the two prior manuscripts | `FILE_MANIFEST.csv`; `SOURCE_INVENTORY.md` §4 |
| 2 | DOI resolution through the page tool (`https://doi.org/10.1007/s40314-024-02789-1`) | Springer landing page; **abstract only**, "This is a preview of subscription content", PDF USD 39.95 | Springer page, chunks 0–4 all retrieved: only abstract, reference list, and "About this article" — no body text |
| 3 | Direct HTTPS from the sandbox to `link.springer.com` | **TLS blocked** (`SSL_ERROR_SYSCALL`); egress is allowlisted | `logs/phase0_evidence.out` §7 |
| 4 | Unpaywall API `api.unpaywall.org/v2/10.1007/s40314-024-02789-1` | `is_oa: true`, `oa_status: green`, one location: **HAL** `hal-04825601v1`, version `submittedVersion` | API JSON, 2026-10-23 |
| 5 | OpenAlex `api.openalex.org/works/https://doi.org/…` | same: `oa_url` = the HAL PDF, `any_repository_has_fulltext: true` | API JSON |
| 6 | Semantic Scholar Graph API | same: `openAccessPdf.url` = the HAL PDF, `status: GREEN` | API JSON |
| 7 | HAL landing page `hal.science/hal-04825601` | **metadata readable**: title, five authors, abstract, keywords, DOI, the file listed ("Hermitian hull of constacyclic codes and quantum Codes.pdf", 516.23 kB), deposit date 2024-12-08, licence "HAL Authorization", "Files produced by the author(s)" | page fetched successfully |
| 8 | HAL file download — `…/v1/file/Hermitian%20hull…pdf`, `…/v1/document`, `…/hal-04825601/document`, legacy `hal.archives-ouvertes.fr/hal-04825601/document` | **blocked**: the server sits behind an Anubis proof-of-work bot check ("Making sure you're not a bot!"); the challenge URL returns **503**. A text-extraction proxy (`r.jina.ai`) returns the same Anubis page | fetch attempts, 2026-10-23 |
| 9 | Direct HTTPS from the sandbox to `hal.science` / `api.archives-ouvertes.fr` | **TLS blocked** by the egress allowlist | `urllib` error `SSL_ERROR_SYSCALL` |
| 10 | CORE (`core.ac.uk`) and Internet Archive Scholar | CORE: "This page is not available now"; IA Scholar: ALTCHA anti-bot gate. No usable copy | fetch attempts |
| 11 | GitHub code search `"Hermitian hull of constacyclic codes" in:file` | 8 hits; **all are Scopus metadata dumps** (`.json` records with title/abstract), none contains the article | `gh api search/code` |
| 12 | General web search for an open PDF outside HAL/Springer | **none found**; the only indexed full-text pointers are the Springer paywall and the HAL deposit | search results, 2026-10-23 |

**Conclusion:** the article is openly deposited by its authors at HAL, but the only
free copy is served behind an interactive anti-bot challenge that this agent cannot
and should not circumvent, and the agent's egress policy blocks direct connections
to `hal.science` in any case. **The full text is therefore not obtainable by the
agent.**

## 3. Version warning (this matters for Phase 1)

Two different versions of the same article are in circulation:

| Aspect | Springer version of record | HAL deposit (`hal-04825601v1`) |
|---|---|---|
| Status | published 2024-06-04 | author deposit, submitted 2024-12-08; Unpaywall labels it `submittedVersion`; HAL marks it "Files produced by the author(s)" |
| Abstract wording | "…converts every constacyclic code to a Hermitian LCD code (**Corollaries 2 and 3**)… generator polynomials for Hermitian dual-containing constacyclic codes (**Theorems 8 and 9**)" | "…(**Corollaries 3.2 and 3.3**)…" — a different numbering scheme |
| File size | not stated publicly | 516.23 kB |

The differing corollary numbers are direct evidence that the two files are **not
identical**. Consequences for this project:

* Every theorem number written into `SOURCE_THEOREM_REGISTER.md` (Phase 1) must be
  qualified by the version it came from.
* If only the HAL copy is available, all Phase 1 deliverables must carry the tag
  **"HAL author version (hal-04825601v1)"**, and any statement about "the published
  paper" is out of scope until the version of record is supplied.
* The blueprint's whole programme depends on the paper's hypotheses ($e\mid q+1$,
  multipliers $\alpha_l$ of order $r_l\mid q+1$, the matrix Gray map). A submitted
  version may differ from the version of record in exactly those places, so the
  version tag is not cosmetic.

## 4. What is needed from the user (either one unblocks Phase 1)

**Option A — preferred: the version of record.**
Download the Springer PDF (institutional access or purchase) and place it in the
repository root as:

```
Yadav-2024-Hermitian-hull-CAM-43-269-Springer.pdf
```

**Option B — acceptable, flagged as an author version.**
Open this link in any ordinary browser (the browser solves the anti-bot challenge
automatically), then save the PDF:

```
https://hal.science/hal-04825601v1/file/Hermitian%20hull%20of%20constacyclic%20codes%20and%20quantum%20Codes.pdf
```

and place it in the repository root as:

```
Yadav-2024-Hermitian-hull-CAM-43-269-HAL-v1.pdf
```

Either filename is fine as long as the version is stated; the verifier records the
actual name and hash.

## 5. What happens the moment the file arrives

```bash
cd /home/user/Galios-Hull
python3 research_project/tools/verify_source_pdf.py <the-supplied-file>.pdf --record
```

The verifier checks, and refuses the file unless it passes:

| Check | Rule |
|---|---|
| A | the file is **not** the Debnath et al. preprint (explicit impersonator rejection) |
| B | the expected title appears in the PDF metadata or on pp. 1–2 |
| C | all five author surnames are present |
| D | the DOI `10.1007/s40314-024-02789-1` or the journal name is present |
| info | the ring $\mathcal R_e$ and "$e\mid(q+1)$" signals are reported (informational only) |

Each verdict is appended to `source_audit/SOURCE_PDF_MANIFEST.csv`.

**Verifier status: validated in both directions.**

* `--selftest` → `SELFTEST: PASS` (3/3: accepts a conforming record; rejects the
  Debnath preprint; rejects a record lacking journal/DOI).
* Run against the file that *is* present → `VERDICT: REJECTED` with
  `A … this is Debnath et al. "galois hulls of constacyclic codes over affine
  algebra rings"`, recorded in `SOURCE_PDF_MANIFEST.csv` (exit code 1).

So the gate is armed and has been shown to reject the wrong document; it has not
yet had the opportunity to accept the right one.

## 6. Status statement

* **Phase 0:** complete, unchanged, and still valid. Its deliverables stand; this
  document is an addendum that closes the "source of record?" question while
  leaving the "source file available?" question open.
* **Gate 0:** **BLOCKED.** The paper has been identified and verified
  bibliographically (DOI, authors, journal, abstract, keywords, MSC — all read from
  two independent catalogue records plus the publisher page), but **no copy of its
  full text exists in the workspace**.
* **Phase 1:** **not started**, per the blueprint's stop rule ("If the PDF cannot be
  accessed, stop and request it") and per the user's explicit instruction.
* No Phase 1 deliverable, theorem register, notation glossary, example
  recalculation or novelty statement has been written.

## 7. Also confirmed in this round

* The Debnath et al. PDF remains in the workspace, unmodified
  (`0db90bfb…`, 27 pp., arXiv v1). It is **not** a substitute for the source
  paper and will not be used as one; it may return only in Phase 2 as a
  *related-work* item, clearly labelled.
* The blueprint's own description of the source paper was cross-checked against
  the Springer abstract and matches it: ring
  $\mathcal R_e=\mathbb F_{q^2}+u\mathbb F_{q^2}+\cdots+u^{e-1}\mathbb F_{q^2}$,
  $u^e=1$, $e\mid(q+1)$, $\lambda=\sum_l\eta_l\alpha_l$ with $\operatorname{ord}(\alpha_l)=r_l\mid q+1$,
  Hermitian LCD conditions, dual-containing generator polynomials, quantum codes via
  the Hermitian construction. The blueprint is therefore describing the right paper;
  only the file is missing.
