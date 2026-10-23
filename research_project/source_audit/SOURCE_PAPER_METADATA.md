# SOURCE PAPER METADATA — Phase 0

**Prepared:** 2026-10-23 (UTC) · **Branch:** `arena/831a2e65-galios-hull`
**Updated:** 2026-10-23 — user decision recorded: **Object C (Yadav et al.) is the
source of record**. Objects A and B are retained as related work only.

There are **three** distinct bibliographic objects in play. They are recorded
separately because they must not be conflated.

> **Decision of record (2026-10-23).** The blueprint's named paper is authoritative
> for this project. The Debnath et al. preprint that happens to be in the workspace
> is **not** a substitute and will not be treated as one. Access to Object C is
> **still outstanding**; see `SOURCE_ACCESS_STATUS.md` for the twelve routes tried
> and the exact file needed. Phase 1 has not started.

---

## Object A — the uploaded PDF (the only full text in the workspace)

| Field | Value | How verified |
|---|---|---|
| File | `Galios hulls of constacclic codes over affine algebra rings'.pdf` (repository root) | `ls`, `git ls-tree` |
| Bytes | 291 546 | `sha256sum`, `git ls-tree --long` |
| SHA-256 | `0db90bfbeda69ad1af231b81d92f24be3589ed15ac2e0ade6605ba7ad0ddc039` | `sha256sum` |
| PDF pages | 27 | `pypdf.PdfReader(...).pages` |
| PDF `/Title` | *Galois hulls of constacyclic codes over affine algebra rings* | PDF document information dictionary |
| PDF `/Author` | *Indibar Debnath; Habibul Islam; E. Martínez-Moro; Om Prakash;* | same |
| PDF `/Creator` | *LaTeX with hyperref* | same |
| PDF `/Producer` | *GPL Ghostscript 10.01.2* | same |
| PDF `/CreationDate` | `D:20241211205909-05'00'` (2024-12-11 20:59:09 −05:00) | same |
| First page stamp | `arXiv:2412.08512v1 [cs.IT] 11 Dec 2024` | text extraction, p. 1 |
| Authors (p. 1) | Indibar Debnath (IIT Patna); Habibul Islam (IIIT Bhopal); E. Martínez-Moro (Univ. Valladolid); Om Prakash (IIT Patna, corresponding) | text extraction, p. 1 |
| Keywords | Constacyclic code; Galois inner product; Galois hull; Galois LCD code | p. 1 |
| 2020 MSC | 94B05, 94B15, 94B60 | p. 1 |
| Submission line | "Preprint submitted to Submitted to Discrete Mathematics" | p. 1 |
| Text layer | searchable: 54 001 characters extracted over 27 pages (concatenated page text, `pypdf` 6.21.2) | `pypdf` extraction |

**Topic (from the paper itself):** the $k$-Galois hulls of $\lambda$-constacyclic
codes over the affine algebra
$\mathcal A=\mathbb F_q[X_1,\dots,X_\ell]/I$, $I=\langle t_1(X_1),\dots,t_\ell(X_\ell)\rangle$
with each $t_i$ **square-free**, studied through **idempotent generators**; it
defines a $k$-Galois inner product, derives generators of the $k$-Galois dual and
hull, a hull-dimension formula, a $k$-Galois LCD criterion, and gives examples of
entanglement-assisted quantum codes (EAQECCs).

Identical copies of Object A are stored at
`prior_art/Galios-Hull-Complete-Work-2026-10-20/03_Source_Paper/source-paper-arXiv-2412.08512v1.pdf`
and in both `references/source-paper.pdf` files — all four hash to
`0db90bfb…c039` (`FILE_MANIFEST.csv`, `duplicate_of` column).

## Object B — the published version of Object A

| Field | Value |
|---|---|
| Title | Galois hulls of constacyclic codes over affine algebra rings |
| Authors | Indibar Debnath, Habibul Islam, Edgar Martínez-Moro, Om Prakash |
| Journal | *Discrete Mathematics*, Volume **349**, Issue 2, February 2026 |
| Article | 114750 |
| DOI | `10.1016/j.disc.2025.114750` |
| Publisher page | `https://doi.org/10.1016/j.disc.2025.114750` → ScienceDirect `S0012365X25003589` |
| Access | abstract, introduction and section snippets public; **full text paywalled** ("Purchase PDF") |
| Copy in workspace | **none** |

The v1 preprint and the published article differ in detail (the published abstract
and introduction cite 45 references where v1 has 44, and v1's bibliography is
numbered up to [44]). Therefore **v1 is not a substitute for the version of
record** for any claim about the published article. All statements in this project
about Object A refer to **arXiv:2412.08512v1** unless explicitly marked otherwise.

## Object C — the paper the blueprint names as its source

| Field | Value |
|---|---|
| Title | Hermitian hull of constacyclic codes over a class of non-chain rings and new quantum codes |
| Authors | Shikha Yadav, Ashutosh Singh, Habibul Islam, Om Prakash, Patrick Solé |
| Journal | *Computational and Applied Mathematics* (Springer), Volume **43**, article 269 (2024) |
| DOI | `10.1007/s40314-024-02789-1` |
| Dates | received 2023-12-02 · revised 2024-04-08 · accepted 2024-05-21 · published 2024-06-04 |
| Access | **paywalled**: "This is a preview of subscription content"; article PDF purchasable at USD 39.95 |
| Open deposit | **yes, at HAL**: `hal-04825601v1`, a 516.23 kB author-deposited PDF ("Files produced by the author(s)", licence "HAL Authorization", deposited 2024-12-08). Unpaywall/OpenAlex/Semantic Scholar all point to it as the only green OA copy. Its corollary numbering (`Corollaries 3.2 and 3.3`) differs from the publisher abstract (`Corollaries 2 and 3`), so it is **not** byte-identical with the version of record. |
| Copy in workspace | **none** — download blocked by an interactive anti-bot challenge; see `SOURCE_ACCESS_STATUS.md` §2 |

Verified abstract content (Springer landing page, read 2026-10-23) — it matches the
blueprint's description on pp. 1–3:

> "…we find the possible Hermitian hull dimensions of $\lambda$-constacyclic codes
> over $R_e=\mathbb F_{q^2}+u\mathbb F_{q^2}+u^2\mathbb F_{q^2}+\cdots+u^{e-1}\mathbb F_{q^2}$,
> $u^e=1$ … $e\mid(q+1)$ and $\lambda=\eta_1\alpha_1+\cdots+\eta_e\alpha_e$ for
> $\alpha_l\in\mathbb F_{q^2}^{*}$ of order $r_l$ such that $r_l\mid q+1$ …
> conditions for these codes to be Hermitian LCD … generator polynomials for
> Hermitian dual-containing constacyclic codes (Theorems 8 and 9) … parameters of
> quantum codes using the Hermitian construction."

**Relation to Object A:** Object A cites Object C as its reference **[43]**,
verbatim (p. 26 of the PDF):

> "[43] S. Yadav, A. Singh, H. Islam, O. Prakash, P. Solé, Hermitian hull of
> constacyclic codes over a class of non-chain rings and new quantum codes,
> Comput. Appl. Math. 43(5) (2024) Paper No. 269, 19 pp."

and discusses it in the introduction (p. 3):

> "In 2024, Yadav et al. [43] studied the Hermitian hulls of constacyclic codes over
> a more general class of non-chain ring $\mathbb F_q[u]/\langle u^e-1\rangle$ such
> that $\gcd(e,q)=1$. Besides finding the Hermitian hull dimensions of
> $\lambda$-constacyclic codes over the ring, they also obtained the conditions for
> these codes to be Hermitian LCD."

## Identification verdict

| Question | Answer | Evidence |
|---|---|---|
| Which paper governs this project? | **Object C (Yadav et al.)** — user decision, 2026-10-23 | blueprint pp. 1–2; `SOURCE_ACCESS_STATUS.md` |
| Is the uploaded PDF (Object A) the paper named by the blueprint? | **No.** | Object A vs Object C: different title, authors, journal, ring, inner product, code family, and results. Object C appears in Object A only as reference [43]. |
| Is Object A a legitimate research paper? | **Yes**, and it stays in the workspace unmodified. | 27-page arXiv v1, complete text layer, published in *Discrete Mathematics* 349(2) (2026) 114750. |
| Is the blueprint's source paper available in the workspace? | **Not yet.** | twelve access routes tried (`SOURCE_ACCESS_STATUS.md` §2); the only free copy sits behind an anti-bot challenge and direct egress to that host is blocked |
| Can Object C be obtained by this agent? | **No.** | Springer serves a preview only; HAL download blocked; no other copy indexed |

**Consequence:** Gate 0 stays **BLOCKED** until the correct PDF is supplied. The
blueprint's own instruction for this situation is to stop and request the document,
which is what happened: no Phase 1 deliverable has been produced. Object A is
*never* substituted, and none of its results, notations or hypotheses are carried
into the Yadav-based project.
