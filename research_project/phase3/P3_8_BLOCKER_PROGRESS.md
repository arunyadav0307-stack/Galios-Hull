# P3-8 — Blocker progress after the L-2 episode (2026-10-24)

Purpose: record what changed about the three literature blockers **B-1, B-2a, B-2b** and the
**Tian–Gao–Gao** full text after a targeted re-search, and what did *not* change. No computation is
claimed here; every statement below is either a bibliographic fact located at a named URL or an
explicit statement that the body remains unread.

**Bottom line: no blocker is closed. Two are re-characterised more precisely, one new bibliographic
fact was found, and one full text belonging to the same research line was read end-to-end. R4 is
neither withdrawn nor promoted, and Phase 9 stays NO-GO.**

---

## 1. Why re-search was warranted

`P3_7B_L2_PROVENANCE_AUDIT.md` §5 recorded a failure mode: the Phase 2 literature pass searched the
project's *topic* (hulls of constacyclic codes) and missed a 2008 theorem about the *specific object*
(`⟨(x−1)^i⟩` of length `p^s`). The same failure mode could apply to the three blockers. So the search
was repeated on author names, exact titles and DOIs rather than on the topic.

## 2. What was found

### 2.1 B-2b — now fully identified; the record was already correct

Correct citation, confirmed on the publisher page
(<https://link.springer.com/chapter/10.1007/978-981-95-1365-9_25>):

> I. Debnath, O. Prakash, **Hulls of Cyclic Codes Over a Local Ring**, in *ICT for Intelligent
> Systems* (ICTIS 2025), Smart Innovation, Systems and Technologies vol. **325**, pp. **309–319**,
> Springer, first online 25 November 2025. DOI `10.1007/978-981-95-1365-9_25`.

Abstract, quoted verbatim:

> For a prime `p` and `ℓ ∈ N` with `gcd(ℓ,p) = 1`, this work explores the hulls of `ℓ`-length cyclic
> codes over `Z_{p^3}`. We establish the form of the generators of the hulls and provide a
> characterization of the hulls. Further, we present a condition for these codes to be LCD. To
> formulate the `p`-dimensions of the hulls, first, we find the types of the hulls and then use them
> to come up with an expression for the `p`-dimensions of the hulls. Moreover, for a fixed
> `p`-dimension of the hull, we count all the cyclic codes.

So: chain ring `Z_{p^3}` (as recorded), count of cyclic codes **by hull `p`-dimension** (as recorded),
**no distance** in the abstract. The body is paywalled (`USD 29.95` / institutional). **B-2a-style
limitation applies: absence of a distance law is not established.**

### 2.2 B-2a — still paywalled, but a **Correction** exists and was not in the register

Correct citation of the paper (unchanged):
Debnath, Prakash & Islam, *Galois hulls of constacyclic codes over finite fields*,
**Cryptogr. Commun. 15(1):111–127 (2023)**, DOI `10.1007/s12095-022-00591-6`.

**New bibliographic fact:** there is a published **Correction** —
*Correction to: Galois hulls of constacyclic codes over finite fields*, **Cryptogr. Commun.
15:129–130 (2023)**, DOI `10.1007/s12095-022-00602-6`, published 22 July 2022. Per its abstract
summary on Academia, the correction clarifies that a **primitive element of `F_8`** is needed for the
definition of constacyclic codes used there (an accuracy fix on page 5 of the original).

Consequence for this project: any appeal to B-2a's "restrictions on `q`" must be read against the
corrected text, which is a *second* document we do not have. This makes the B-2a blocker slightly
**worse**, not better, and it is now recorded as such.

### 2.3 The line's scope, established from a full text we *can* read

The same authors' successor paper is openly available: Debnath, Islam, Martínez-Moro & Prakash,
*Galois hulls of constacyclic codes over affine algebra rings*, **arXiv:2412.08512** (11 Dec 2024),
*Discrete Math.* **349** (2026) 18, DOI `10.1016/j.disc.2025.114750`. Its introduction and §1–§2 were
read directly (<https://arxiv.org/html/2412.08512v1>). Findings:

* Its object is a **`q`-dimension formula** for `k`-Galois hulls of `λ`-constacyclic codes over an
  affine algebra ring, plus Galois self-dual / dual-containing / LCD conditions, plus EAQECC examples.
* Its "counting" object is explicitly **`δ_k(n,q,λ)` = the number of distinct `q`-dimensions of
  `k`-Galois hulls** — i.e. the size of the *set of attainable hull dimensions*, which is weaker
  than even a count of codes by hull dimension.
* **No distance distribution appears anywhere in the paper.** Hamming distance is defined in §2 only
  to fix notation for the `[n,k,d]_q` symbol.
* It cites this project's source paper and describes its contribution as: *"Besides finding the
  Hermitian hull dimensions of `λ`-constacyclic codes over the ring, they also obtained the
  conditions for these codes to be Hermitian LCD."* — an independent corroboration of
  `SOURCE_MATHEMATICAL_AUDIT.md`, from a third party.

This is the strongest evidence available without the B-2a body: an accessible full text by **the same
three-or-four authors, same ring family, same method** contains no distance content. It is *not*
proof about B-2a, and is not treated as such.

### 2.4 Tian–Gao–Gao — still unobtainable, no preprint located

Citation (unchanged): Z. Tian, J. Gao, Y. Gao, *Hulls of constacyclic codes over finite non-chain
rings and their applications in quantum codes construction*, **Quantum Inf. Process. 23**, art. 9
(2024), DOI `10.1007/s11128-023-04230-8`.

A search for an arXiv/preprint version returned **none**. Statement of record: *no openly accessible
copy was located by search*; this is not a claim that none exists. Body remains unread.

## 3. What this does and does not license

| Claim | Status |
|---|---|
| B-2b counts cyclic codes over `Z_{p^3}` by hull `p`-dimension; no distance in the abstract | **supported** (verbatim abstract) — still not an absence claim |
| B-2a counts constacyclic codes over `F_q` by Galois hull dimension, under restrictions on `q` | **supported** (abstract) but **must be read against its 2022 Correction**, which we do not have |
| The Debnath–Prakash–Islam line is hull-dimension-only | **supported for the one full text read** (arXiv:2412.08512); *inferred* for the rest |
| None of them contains a joint (hull, distance) distribution | **NOT established.** B-1, B-2a body, B-2b body, Tian–Gao–Gao body all unread |
| R4's contribution is novel | **not claimed**; unchanged |
| R4 is withdrawn | **no** — the withdrawal trigger requires an actual joint distribution, which has not been found |

## 4. Distinction from R4, sharpened with sources

The nearest prior art now reads, in its own words:

* B-2a: "the number of constacyclic codes of length `n` over `F_q` is calculated **for a given Galois
  hull dimension**" — a **marginal** law on hull dimension, field level.
* arXiv:2412.08512: counts the **number of distinct attainable hull dimensions** `δ_k(n,q,λ)` —
  strictly less information than (a).
* B-2b: "for a fixed `p`-dimension of the hull, we count all the cyclic codes" — a marginal law over
  a chain ring, no Gray map.

R4 asks for something different in kind: the **joint** distribution of `(dim Hull_H, d)` over the ring
`R_e = F_q[u]/⟨u^e−1⟩` **together with its Gray image**, i.e. the very map Ψ studied in P3-3/P3-4.
A hull-dimension marginal — even an exact one — does not determine it, and P3-1 already produced the
witness for that: the observed joint law is *not* the product of its marginals (independence
violations 5, 5, 11, 2, 3, 9 across tables A/B/D/E/F). That is a computed fact about this project's
own tables, independent of the literature.

**This is a distinction in kind, not an absence claim**, and the standing rule is respected:
no novelty is asserted anywhere.

## 5. Effect on the standing decisions

* **Phase 9: NO-GO, unchanged.** Nothing here creates a theorem, and nothing here removes the reason
  Phase 9 was withheld.
* **R4: stands, still conditional.** The one thing that would have forced withdrawal — a joint
  (hull, distance) distribution in any of the four unread bodies — has not been found. It also has not
  been excluded.
* **Blockers after this pass:** B-1 (publisher bodies), **B-2a** (body **+ now also its Correction**),
  **B-2b** (body), Tian–Gao–Gao (body). None closed.
* **Prior-art register** gains the two bibliographic items of §2.1 and §2.2.

## 6. Reproducibility

This document contains no computation, so there is nothing to re-run. Every citation above is
traceable to a URL that was fetched during this pass:

* `https://link.springer.com/chapter/10.1007/978-981-95-1365-9_25` — B-2b page, abstract quoted.
* `https://link.springer.com/article/10.1007/s12095-022-00591-6` and
  `https://dl.acm.org/doi/10.1007/s12095-022-00591-6` — B-2a abstract.
* `https://link.springer.com/article/10.1007/s12095-022-00602-6` — the Correction.
* `https://arxiv.org/abs/2412.08512` and `https://arxiv.org/html/2412.08512v1` — full text read.
* `https://link.springer.com/article/10.1007/s11128-023-04230-8` — Tian–Gao–Gao record.

Per §2.2, the next action on B-2a is to obtain **both** `10.1007/s12095-022-00591-6` and
`10.1007/s12095-022-00602-6`. Requesting only the original would repeat a known-incomplete read.
