# Version-of-record inspection record — 2026-10-20

**Purpose.** Record exactly what of the published version was actually seen, where,
and what remains unseen. Nothing in this file is inferred.

**Target.** I. Debnath, H. Islam, E. Martínez-Moro, O. Prakash, *Galois hulls of
constacyclic codes over affine algebra rings*, **Discrete Mathematics 349(2) (2026)
114750**, DOI `10.1016/j.disc.2025.114750`.

---

## 1. What is publicly accessible (and was read)

| Source | URL | What it exposes |
|---|---|---|
| Publisher article page, "Article preview" | `https://www.sciencedirect.com/science/article/abs/pii/S0012365X25003589` | Abstract (complete), Introduction (complete), section snippets, references list |
| Crossref REST API | `https://api.crossref.org/works/10.1016/j.disc.2025.114750` | bibliographic metadata only, 45 references, no abstract, no text |

**Access status of the full text:** `Access through your organization` / `Purchase
PDF`. No institutional access was available. **The body of the paper was not read.**

---

## 2. Verbatim extracts bearing on this project

### 2.1 The abstract

Identical in substance to the arXiv v1 abstract, including the closing sentence:

> "Finally, we give some examples of the use of these codes in constructing
> entanglement-assisted quantum error-correcting codes."

### 2.2 The introduction — the `q`-dimension framing is retained

> "Our main objective is to derive a formula for the **q-dimensions** of the
> k-Galois hulls of λ-constacyclic codes over a serial ring 𝒜."

> "…we derive an expression for the Galois hull dimension of a constacyclic code
> over 𝒜. … This will provide some properties that allow us to compute the
> **cardinality of the set of q-dimensions** of k-Galois hulls of λ-constacyclic
> codes of length n over 𝒜, denoted as **𝒟_k(n,q,λ)**."

### 2.3 The §3 snippet — also retained

> "**Galois hulls of constacyclic codes over 𝒜** — In this section, we find the
> form of the generator of the k-Galois dual as well as the k-Galois hull of a
> λ-constacyclic code of length n over 𝒜. … Then we derive a formula for the
> **q-dimension of the k-Galois hull** of a λ-constacyclic code."

### 2.4 The published version is materially longer than v1

> "Additionally, we find some EAQECCs (see **Example 2, Example 4, and Table 2**)
> that are comparatively better than the existing ones [13], [30]."

Example 4 and Table 2 do **not** exist in arXiv v1. Crossref lists **45**
references; v1 has 44.

### 2.5 Theorem and lemma numbering has shifted

| Published | Snippet | v1 counterpart |
|---|---|---|
| **Theorem 4** | "Let λ be a unit in 𝒜. If C = Σ_{S(ν)∈Ŝ} C_{S(ν)} e_{S(ν)} is a …" | v1 **Theorem 2** (p.7) |
| **Lemma 7** | "[7] For a linear code C with parameters …" | v1 **Lemma 8** (p.17) |

So cross-references from v1 numbering do not transfer.

### 2.6 The published introduction states the v1-era precedent explicitly

> "In 2023, Debnath et al. [11] presented a formula to calculate the Galois hull
> dimensions of constacyclic codes over finite fields. **They also counted the
> number of constacyclic codes of a given Galois hull dimension.**"

This is the authors' own statement, in the published version, that the local
enumerator exists — consistent with `literature/REFERENCE_VERIFICATION_REPORT.md`
`[D23]`.

---

## 3. What was NOT seen

| Item | Status |
|---|---|
| §2 Preliminaries body (the CRT decomposition, the `a_{S(ν)} ∈ F_q` sentence, eq. (10)) | **NOT SEEN** |
| §3 body (Theorem 4's full statement and proof, the hull-dimension formula) | **NOT SEEN** |
| §4 body (Examples 2 and 4, Tables 1 and 2, the Gray map definition) | **NOT SEEN** |
| Conclusion (whether the "enumeration of non-isometric … is still open" sentence survives) | **NOT SEEN** — the snippet stops at "Hulls of different families of linear codes have yet to be" |

---

## 4. Consequences, stated carefully

**What the partial inspection DOES establish.**

1. The published version differs materially from arXiv v1: +1 reference, new
   Example 4, new Table 2, shifted theorem numbering. **Extrapolating any defect
   from v1 to the published text is therefore unsafe**, and none is made.
2. The phrase "`q`-dimension" — the exact term implicated in F11 — **is still used**
   in the published introduction and §3 snippet. This raises the prior that the
   affected passages were not rewritten; **it does not establish it**.
3. The published version adds a counting result, `|𝒟_k(n,q,λ)|`, the number of
   distinct `q`-dimensions attained. This is **not** code enumeration, and it is
   not the enumeration of codes up to isometry; but it is closer to that territory
   than anything in v1, and any future novelty claim about counting constacyclic
   hull dimensions must reckon with it.

**What it does NOT establish.**

- That the `a_{S(ν)} ∈ F_q` statement survives. **Unknown. BLOCKED.**
- That eq. (10) still sets `N = |Ŝ|`. **Unknown. BLOCKED.**
- That Examples 2–4 and Tables 1–2 still print lengths `2n`. **Unknown. BLOCKED.**

**Net effect on F11.** The finding remains **proved for arXiv v1** and **unverified
for the version of record**. The blocking item has changed in character: it is no
longer "no information at all", it is "the framing survives, the body is unread".

---

## 5. Second pass, same day: access re-verified before declaring BLOCKED

The decisive passage (`§2`, the CRT coefficient statement) was **not** reachable in
the first pass. Before recording it as BLOCKED, access was re-checked by four
independent routes; the result is that **no legitimate free copy of the published
version exists at the time of writing**.

### 5.1 Bibliographic identification (complete)

| Field | Value | Source |
|---|---|---|
| Authors | I. Debnath, H. Islam, E. Martínez-Moro, O. Prakash | Crossref |
| Journal | *Discrete Mathematics* (Elsevier), ISSN 0012-365X | Crossref |
| Volume / issue | **349** / **2** | Crossref; publisher page |
| Date | February 2026 (published-print 2026-02) | Crossref; publisher page |
| Article number | **114750** (first and last page = 114750) | Crossref `page`; publisher page |
| DOI | **10.1016/j.disc.2025.114750** | Crossref |
| PII | **S0012365X25003589** | publisher URL |
| Article type | Research article | publisher page |
| References | 45 | Crossref `reference-count`; publisher page "References (45)" |
| Cited by | 1 | Crossref `is-referenced-by-count` |

The record is `type: journal-article`, so this is the published version, not an
"article in press".

### 5.2 Is the published version open access? (re-checked)

| Check | Result |
|---|---|
| Crossref `license` | Only Elsevier **TDM** licences (`elsevier.com/tdm/userlicense/1.0/`, `tdmrep-license`, STM ASF policies). **No Creative Commons licence**, i.e. not OA. |
| OpenAlex `W4413796731`, `primary_location` | `is_oa: **false**`, `license: **null**`, `version: publishedVersion` |
| OpenAlex `open_access` | `is_oa: true`, `oa_status: **green**`, `oa_url: **https://arxiv.org/pdf/2412.08512**` — i.e. the only free full text is the **arXiv preprint**, not the published article |
| Direct request to `/science/article/pii/S0012365X25003589` | **redirects to `/science/article/abs/pii/S0012365X25003589`**, the "Article preview" page |
| Page access controls | Offer only `Access through your organization` and `Purchase PDF` |
| ScienceDirect "Article preview" tab list | Abstract · Introduction · Section snippets · References (45). No full-text tab. |

### 5.3 Is the green-OA copy the published version? (No)

`https://arxiv.org/abs/2412.08512`, submission history as served on 2026-10-20:

> **[v1]** Wed, 11 Dec 2024 16:24:26 UTC (22 KB)

There is **no v2**. The arXiv licence is CC BY-NC-ND 4.0. So the green copy is the
27-page v1 that this project has audited throughout — **v1 is not the version of
record**, and per the standing rules it may not be used as a proxy for it.

### 5.4 What the published §2 snippet does and does not show

The "Preliminaries" snippet is the **first paragraph only**, on constacyclic codes
over a finite field:

> "Let 𝔽𝑞 be the finite field. A linear code of length n is an 𝔽𝑞-subspace of 𝔽𝑞ⁿ.
> Let λ be a unit in 𝔽𝑞. A linear code C ⊆ 𝔽𝑞ⁿ is said to be a λ-constacyclic code if
> (c₀,c₁,…,cₙ₋₁) ∈ C implies that (λcₙ₋₁,c₀,c₁,…,cₙ₋₂) ∈ C. …"

It **stops before** the primitive-idempotent decomposition and therefore says
nothing about whether the coefficient `a_{S(ν)}` is taken in `F_q` or in `A_S`.

### 5.5 Verdict

**BLOCKED.** The published `§2` body, the published `§4` examples and tables, and the
published conclusion were not read. No statement in this project asserts anything
about the published body.

**Secondary summaries were not used.** A third-party AI-review page summarising the
article exists (`themoonlight.io`). It is not the published text, is not admissible
as evidence, and none of its content appears anywhere in this dossier.

### 5.6 Legitimate routes to the full text (for whoever can act on them)

Listed in the order that would settle the question fastest. None was available in
this environment; none is asserted to be available.

1. **Institutional subscription.** Any library with a ScienceDirect licence: open the
   DOI and use `Access through your organization`. Covers IIT Patna, IIIT Bhopal and
   Universidad de Valladolid (the authors' institutions) and most university libraries.
2. **Pay-per-view purchase** from the publisher (`Purchase PDF` on the article page).
3. **Interlibrary loan / document delivery** — most university libraries will supply
   an Elsevier article through their ILL service.
4. **Request a copy from the corresponding author.** The corresponding author is
   O. Prakash (IIT Patna), per OpenAlex. A reprint supplied by an author is a
   legitimate copy; if the authors send the accepted manuscript rather than the
   published PDF, it must be labelled as such and the numbering check in §2.5 of the
   main dossier still applies.
5. **Institutional text-and-data-mining agreement.** Crossref lists Elsevier TDM
   licences for this article; an institution with a TDM agreement can obtain the full
   text through the Elsevier API.
6. **Author deposit.** Re-check the authors' institutional repositories (IIT Patna,
   IIIT Bhopal, Universidad de Valladolid) and their ORCID records for a deposited
   accepted manuscript. A deposit would be an *accepted manuscript*, not the version
   of record.

**Not used and not to be used:** Sci-Hub or any other shadow-library service; the
third-party summary page; the arXiv v1 as a stand-in for the published text.

### 5.7 The single decisive sentence

Everything reduces to one sentence in the published `§2`. In v1 it reads (p.7):

> "Every a ∈ A can be expressed as a = Σ_{S(ν)∈Ŝ} a_{S(ν)} e_{S(ν)}, where
> **a_{S(ν)} ∈ F_q for all S(ν) ∈ Ŝ**."

The published version must be checked at the corresponding place for whether the
coefficient is still `∈ F_q`, or has become `∈ A_{S(ν)}` / `∈ F_{q^{|S(ν)|}}`.
