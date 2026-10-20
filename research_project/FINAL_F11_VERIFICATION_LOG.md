# FINAL F11 VERIFICATION LOG — third pass, 2026-10-20

**Branch:** `arena/1625045b-galios-hull` · **Status:** no manuscript, no correction note,
nothing committed or pushed.

**Question this round.** Does the published version of record contain the F11 defect, or
was it corrected between arXiv v1 and the published article?

**Answer. BLOCKED.** The published full text is not open access and could not be
obtained by any legitimate route available here. The decisive sentence in the published
`§2` was **not** read, so the question is **not answered, and no answer is inferred**
from the abstract, the introduction, the section snippets, the reference list, the arXiv
preprint, or any third-party summary.

What *was* done: the access question was settled by seven independent routes (§1), the
v1-versus-published comparison was carried out on the observable surface only (§2), both
audit scripts were re-run in a clean room and cross-checked against each other (§3), and
every decisive claim was pinned to a printed page with a verbatim excerpt
(`verification/VERBATIM_LOCI_v1.md`, §4).

---

## 1. Access to the published article: seven attempts, all closed

Target: I. Debnath, H. Islam, E. Martínez-Moro, O. Prakash, *Galois hulls of
constacyclic codes over affine algebra rings*, **Discrete Mathematics 349(2) (2026)
114750**, DOI `10.1016/j.disc.2025.114750`, PII `S0012365X25003589`.

| # | Route | Result |
|---|---|---|
| 1 | `https://www.sciencedirect.com/science/article/pii/S0012365X25003589` (full-text URL) | **redirects** to `/science/article/abs/pii/S0012365X25003589`, the "Article preview" |
| 2 | `https://www.sciencedirect.com/science/article/abs/pii/S0012365X25003589` | preview only: Abstract · Introduction · Section snippets · References (45). Access controls are `Access through your organization` and `Purchase PDF`. Page footer: "© 2025 Elsevier B.V. All rights reserved, including those for text and data mining, AI training, and similar technologies." |
| 3 | Crossref `api.crossref.org/works/10.1016/j.disc.2025.114750` | metadata and 45 references; `license` entries are Elsevier **TDM** licences only. **No Creative Commons licence** ⇒ not open access. |
| 4 | OpenAlex `api.openalex.org/works/doi:10.1016/j.disc.2025.114750` | `primary_location.is_oa = false`, `license = null`, `version = publishedVersion`; `open_access.oa_status = green`, `oa_url = https://arxiv.org/pdf/2412.08512` ⇒ the only free full text is the **preprint** |
| 5 | arXiv `arxiv.org/abs/2412.08512` | submission history `[v1] Wed, 11 Dec 2024` and **no v2**. The green copy is v1, not the published version. |
| 6 | Institutional repository of the third author, `uvadoc.uva.es` | searched; **no deposit** of this article |
| 7 | ResearchGate | the only hosted version is labelled **Preprint, Dec 2024** — i.e. the arXiv v1, not the published text |

**Shadow libraries and secondary summaries were not used.** Sci-Hub-type services were
not attempted, and the third-party AI-review page that summarises the article
(`themoonlight.io`) was not read for content and contributes nothing to this audit.

**Conclusion of §1.** There is no accessible, legitimate copy of the published article
in this environment. The obstruction is a paywall, not a broken link.

### 1.1 Exactly what is missing

The audit needs **one sentence** — the published counterpart of v1's p.7 sentence
(quoted in §4 below, L5):

> "Since A = ∑_{S(ν)∈Ŝ}(e_{S(ν)}F_q), each element a ∈ A can be expressed as
> a = ∑_{S(ν)∈Ŝ} a_{S(ν)}e_{S(ν)}, where a_{S(ν)} ∈ F_q for all S(ν) ∈ Ŝ."

Three further items would confirm the scope if the first is unfavourable:

1. published equation corresponding to v1 eq. (10) — does it still give `ψ : A → F_q^N`
   with `N = |Ŝ|`, and is `ψ` still called a bijection?
2. published Tables 1 and 2 and the new Example 4 — do they still print length `2n`
   against the unweighted `k`?
3. published Theorem 4 (v1 Theorem 2) — does it still say the components are
   constacyclic codes "over F_q"?

### 1.2 Legitimate ways to get them

In the order that would settle it fastest:

1. **Institutional subscription** to ScienceDirect (covers the authors' institutions —
   IIT Patna, IIIT Bhopal, Universidad de Valladolid — and most universities).
2. **Pay-per-view purchase** from the article page.
3. **Interlibrary loan / document delivery.**
4. **Request a reprint from the corresponding author** (O. Prakash, IIT Patna). If the
   authors send the accepted manuscript rather than the published PDF, it must be
   labelled as such, and the numbering shift in §2 applies.
5. **Institutional text-and-data-mining agreement** — Crossref lists Elsevier TDM
   licences for this DOI.
6. **Author deposit** — re-check the three institutions' repositories and the authors'
   ORCID records for a deposited accepted manuscript.

---

## 2. Published version vs arXiv v1 — comparison of the observable surface

This is the *whole* of what can honestly be compared. It is a bibliographic and
framing comparison, not a textual one.

| Property | arXiv v1 | Published (observable) | Same? |
|---|---|---|---|
| Article identity | arXiv:2412.08512v1, 27 pp, 11 Dec 2024 | Discrete Math. **349**(2) 114750, Feb 2026 | different object |
| References | 44 | **45** | **no** |
| Examples | Ex. 1, 2, 3 | Ex. 1, 2, **3, 4** (intro cites "Example 2, Example 4, and Table 2") | **no** |
| Tables | Table 1 | Table 1 **and Table 2** | **no** |
| Theorem numbering | Theorem 2 = hull/constacyclic equivalence | **Theorem 4** (same opening words) | **no** |
| Lemma numbering | Lemma 8 = EAQECC existence | **Lemma 7** | **no** |
| Counting result | none | **new**: cardinality of the set of `q`-dimensions, `𝒟_k(n,q,λ)` | **no** |
| "q-dimension" terminology | used | **used** (Introduction and §3 snippet) | **yes** |
| Abstract | — | substantively the same as v1 | apparently yes |

**The published version is materially longer and adds results.** Any inference of the
form "v1 had a defect, therefore the published version has it" is therefore invalid on
its face, and none is made.

**What cannot be compared.** The published `§2` body, the published Theorems 3–6 and
their proofs, the published Example 4, Tables 1–2, and the published conclusion. Those
are the loci that decide the question. **They were not read. The comparison is BLOCKED
at exactly that point.**

**One thing that is observable and worth recording.** The published `§3` snippet ends at
"**Theorem 4** — *Let λ be a unit in* 𝒜 *. If* 𝐶=∑𝑆(𝜈)∈ˆ𝑆𝐶𝑆(𝜈)𝑒𝑆(𝜈) *is a*" and then
stops. The decisive clause of Theorem 4 — which in v1 reads "…is a λ-constacyclic code
in A^n if and only if for each S(ν) ∈ Ŝ, C_{S(ν)} is a λ_{S(ν)}-constacyclic code of
length n **over F_q**" (L7) — falls inside the paywalled body. The preview therefore
cuts off one clause before the first place where the error would be visible *in a
theorem statement*.

**Consequence: the answer to "remains or corrected?" is unknown.** Recording it as
"remains" would be inference from the framing; recording it as "corrected" would be
inference from the fact that the paper was revised. Neither is evidence.

---

## 3. Clean-room re-run of the two audit scripts

Both scripts were re-run from a pristine extraction of the project archive, in a
directory containing nothing else, and cross-checked against each other and against the
logs shipped inside the archive.

**Environment.** `/tmp/cleanroom_2026-10-20`, Python 3.11.2, fresh `unzip` of
`FINAL_F11_EVIDENCE_DOSSIER.zip`, no network, no third-party packages.

### 3.1 Archive integrity before running

16 of 16 members re-hashed and size-checked against `MANIFEST.txt` — **all match**.

### 3.2 `code/table1_audit.py` — exit code 0

```
C0  g_S | x^n - lambda_S (transcription) : 13/13, naming-free
C1  deg g_S < n in every component       : True
C2  k_printed = sum_S (n - deg g_S)       : 13/13
C3  length = 2n                           : 13/13
C4  true dim_q = 2 * k_printed            : by construction (|S|=2)
C5  2k <= 2n                              : violated in 8 rows [1, 3, 6, 7, 10, 11, 12, 13];
                                            degenerate in 3 rows [2, 4, 8]
C6  Theorem 10 arithmetic                  : 13/13 consistent
C7  'Diff' column identity                 : 13/13 consistent
```

### 3.3 `code/table1_forensics.py` — exit code 0 (self-contained, imports nothing)

```
PART 1  q=4 : N=2, |S|=[2,2], dim_q A=4, CONSISTENT with prod deg t_i
        q=9 : N=2, |S|=[2,2], dim_q A=4, CONSISTENT
        q=25: N=2, |S|=[2,2], dim_q A=4, CONSISTENT
PART 2  every printed tuple occurs verbatim in the copied raw text : 13/13
PART 2b g_S | x^n - lambda_S, all 8 admissible namings of omega    : 13/13 each
C2  13/13    C3  13/13    C6  13/13    C7  13/13
C8  13/13    C9  13/13    C10 13/13
C5  2k>2n : [1,3,6,7,10,11,12,13]   2k=2n : [2,4,8]   2k<2n : [5,9]
```

### 3.4 Reproduction and independent agreement

| Test | Result |
|---|---|
| `table1_audit` console output vs archived `verification/table1_audit.out` | **IDENTICAL** (timestamp and output-path lines excluded) |
| `table1_forensics` console output vs archived `verification/table1_forensics.out` | **IDENTICAL** (same exclusions) |
| The two scripts against each other: C2, C3, C6, C7 | **13/13 versus 13/13 — agree** |
| The two scripts against each other: the row sets | `[1,3,6,7,10,11,12,13]`, `[2,4,8]` from both — **agree** |

The two scripts share no code: `code/table1_audit.py` imports `Fld`/`pdivides` from
`code/f11_source_audit.py`, while `code/table1_forensics.py` rebuilds `F₄, F₉, F₂₅`,
their quadratic extensions `F₁₆, F₈₁, F₆₂₅`, the root sets and the Galois orbits from
scratch. Their agreement on every row set is therefore a genuine cross-check.

Full console transcript: `verification/cleanroom_run_2026-10-20.log`.

---

## 4. Decisive claims, with page and verbatim excerpt

Every claim is registered in `verification/VERBATIM_LOCI_v1.md` (L1–L18 for v1,
P-1…P-8 for the observable published surface). The load-bearing ones:

### 4.1 The sharpest form of the finding is now purely textual

Three quotations, all from v1, contradict each other with **no computation required**:

* **p.4 (L1):** "the size of each class is given by |S(ν)| = lcm(d1,d2,...,dℓ) =
  [Fq(ν1,ν2,...,νℓ) : Fq]"
* **p.5 (L3):** "eS(ν)R ∼= Fq(ν1,ν2,...,νℓ)" — each summand is a **field of degree
  `|S(ν)|`**
* **p.7 (L5):** "Since A = ∑S(ν)∈ˆS(eS(ν)Fq) … where aS(ν) ∈ **Fq** for all S(ν) ∈ ˆS" —
  each summand is a copy of **`F_q`**

The first two give `dim_q A = Σ_S |S(ν)|`; the third gives `dim_q A = N = |Ŝ|`. These
agree only when every `|S(ν)| = 1`.

For Example 2 the paper states its own `N`: "**N = 2.** Then, there are 2
idempotentseα, α = 1, 2" (p.19, L14), with both `t_i` quadratic (p.18). Hence
`|S(ν)| = lcm(2,2) = 2` by L1, so p.5 gives `dim_q A = 4` while p.7 gives `2`.
**The contradiction is internal to the paper and needs no computer.** The scripts
quantify its consequences; they do not create it.

### 4.2 The consequence is a genuine dilemma, not a typo

* **p.17 (L10):** "It is easy to verify that the map ψ is bijective linear isometry from
  An (Gray distance) to FnNq (Hamming distance)."
* **p.18 (L11):** the proof of Lemma 9(2) says "**Since ψ is an injective map**, we have
  c = c′".
* **p.18 (L12):** "dim(hullk(D)) = dim(hullk(ψ(C))) = dim(ψ(hullk(C))) = dimq(hullk(C))".

So either `ψ` is injective — in which case `dim_q ψ(C) = dim_q C = 2k ≠ k` and the
printed `[2n, k, d]` is false; or `ψ` is not injective — in which case Lemma 9(2)'s
proof fails at the quoted step and Theorem 10 loses its input. **There is no third
option.** This is why the finding is not a matter of a missing factor that a reader can
silently repair.

### 4.3 The numeric contradiction, per row

Table 1 (p.22, L17) has 13 rows over three rings, each defined by two quadratics, so
`dim_q A = 4` in all of them. With the printed length `2n` forcing `N = 2`, the true
dimension is `2k`:

* 8 rows (**1, 3, 6, 7, 10, 11, 12, 13**) have `2k > 2n` — the printed `(length,
  dimension)` pair is **not realisable by any `F_q`-subspace**;
* 3 rows (**2, 4, 8**) have `2k = 2n` — the image is the whole space, so `d = 1`,
  contradicting the printed `d ∈ {4,4,6}`; this is a **false distance claim** against a
  realisable dimension;
* 2 rows (**5, 9**) are dimensionally feasible, and only the printed `k` is wrong.

**In all 13 rows the printed length and the printed dimension cannot both be right.**

---

## 5. What this round changed

| Item | Before | Now |
|---|---|---|
| Table 1 status | 8 impossible, 3 degenerate, 2 "escape" | **all 13 rows jointly inconsistent**; the 2 compatible rows only escape the *impossibility*, not the error |
| Basis of the core finding | required rank computations | **also a purely textual contradiction between p.4/5 and p.7** |
| Page/theorem/equation anchoring | partial | **complete register, `verification/VERBATIM_LOCI_v1.md`** |
| Reproducibility evidence | archive re-run | **clean-room run + cross-script agreement + archived console transcript** |
| Access question | "paywalled" | **seven routes tried and closed, itemised; exact missing evidence named** |
| Decision | BLOCKED | **BLOCKED**, unchanged, now with the missing items enumerated one by one |

---

## 6. GO / NO-GO

**BLOCKED.** Unchanged from `FINAL_GO_NO_GO_DECISION.md`, and now more firmly so: seven
legitimate access routes have been tried rather than assumed, and the one sentence that
decides the matter is named exactly.

The decision rule remains:

| Finding at the published counterpart of v1 p.7 | Decision |
|---|---|
| still `a_{S(ν)} ∈ F_q` | **GO** — the defect is in the version of record |
| changed to `∈ A_{S(ν)}` or `∈ F_{q^{\|S(ν)\|}}` | **NO-GO, permanently** |

**Not GO:** a correction note would be about the published article, whose `§2` has not
been read; and drafting one is prohibited by the standing rules.

**Not NO-GO:** nothing supports the claim that the published version is clean. It is
materially longer, retains the "q-dimension" framing in its introduction and §3 snippet,
and adds a counting result over the same object.

**BLOCKED is a statement about access, not about the mathematics.** The v1 findings
(§4) are complete and will not change whatever the published sentence turns out to say.
