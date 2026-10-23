# LITERATURE REVIEW — Phase 2

**Project:** extension of Yadav, Singh, Islam, Prakash, Solé, *Hermitian hull of constacyclic codes over a class of non-chain rings and new quantum codes*, Comput. Appl. Math. **43**:269 (2024), DOI `10.1007/s40314-024-02789-1`, version **`hal-04825601v1`** (Phase 1 source).
**Date of search:** 2026-10-23. **Deliverable of:** blueprint Phase 2 (2A literature comparison).
**Companion files:** `LITERATURE_COMPARISON_MATRIX.csv` (18 rows), `NOVELTY_ASSESSMENT.md`, `REFERENCE_VERIFICATION_REPORT.md`.

---

## 1. Method, and its limits

**Search channels used:** scholarly web search (publisher and index pages), arXiv abstract and HTML pages, DOI landing pages, citation lists of works that cite the source, and the reference lists of two manuscripts already in this workspace (the Debnath et al. preprint and the source paper's own 48 references).

**What this method can and cannot support.**

| Can support | Cannot support |
|---|---|
| *Presence*: a work explicitly states in its abstract or accessible full text that it counts codes by hull dimension | *Absence*: "no one has counted X" — no search establishes this |
| Identification of the closest prior art and what it does | Full theorem statements of paywalled papers (Springer/AIMS bodies are inaccessible from this sandbox) |
| Forward-citation discovery of new 2025–2026 work | Exhaustive coverage of conference proceedings, theses, and non-indexed venues |

Consequently **no claim of absence is made anywhere in this Phase 2 output.** Every "new" classification below is at most `N2` (potentially new, needs further checking); nothing is `N1`.

**Search queries run** (verbatim, in order):

1. `Jitman Sangwisut "average dimension of the Hermitian hull" constacyclic codes finite fields square order`
2. `"hull dimension distribution" cyclic OR constacyclic codes exact number of codes with given hull dimension`
3. `count constacyclic codes given Hermitian hull dimension non-chain ring Fq2+uFq2 Gray map enumeration`
4. `"repeated-root" constacyclic codes hull dimension number of codes counted p-adic p^v`
5. `"Hulls of Cyclic Codes Over a Local Ring" count codes fixed hull dimension 2026 chapter`

Plus full-text extraction of the Debnath et al. preprint already in the repository (`Galios hulls of constacclic codes over affine algebra rings'.pdf`, 27 pp., 54 027 characters) and the source paper's own reference list (pp.20–23, [1]–[48]).

---

## 2. The prior-art map

The literature the blueprint names splits into **three strands that have converged on the proposed question from different directions**.

### Strand A — counting *all* linear codes by hull dimension

* **Sendrier (1997)**, *On the Dimension of the Hull*: the number of distinct `q`-ary linear codes with a hull of given dimension, and the asymptotic fact that a positive constant proportion have hull dimension `l`. This is the origin of "enumerate by hull dimension".
* **arXiv:2605.29204 (2026)**, *Enumeration and Monotonicity of Linear Codes with Prescribed Hull Dimensions*: `A^H_{n,k,ℓ,q²}`, the number of `[n,k]` codes over `F_{q²}` with **Hermitian** hull dimension `ℓ`, plus monotonicity.

*Relevance:* establishes the problem type, but carries no cyclic/constacyclic structure, so it says nothing about factor-orbit enumeration.

### Strand B — field-level cyclic / constacyclic codes: average, then exact counts

This is the strand that bears directly on the proposed constituent enumerator.

| Year | Work | What it gives |
|---|---|---|
| 2003 | Skersys | **average** hull dimension of cyclic codes (first moment) |
| 2015 | Sangwisut, Jitman, Ling, Udomkavanich | hull-dimension formulas for cyclic **and negacyclic** codes **and the number of codes for a given hull dimension** |
| 2016 | Jitman & Sangwisut (AIP) | **average** Hermitian hull of cyclic codes over `F_{q²}` |
| 2018 | Jitman & Sangwisut (AMC) | **average** Hermitian hull of **constacyclic** codes over `F_{q²}`, plus bounds |
| 2022/23 | Debnath & Prakash (Cryptogr. Commun.) | Galois hull dimension of constacyclic codes, **and the number of constacyclic codes of length `n` with a given Galois hull dimension** |
| 2025 | Debnath & Prakash (AMC) | **average** Galois hull dimension |
| 2026 | Lu, Yang, Liu, Fu, Guo (arXiv:2607.12242, v3) | Hermitian hull structure of cyclic codes via defining sets, plus **exact counts by hull codimension** — a *product enumerator* in Appendix B ("Counting and the fine structure of the τ-fixed cosets") that also gives the scarcity probability, mean and variance |

**The bearing on this project is direct and adverse to a naive novelty claim.** The blueprint's Phase 3 proposes

```
H_ℓ(z_ℓ) = Σ_{D_ℓ ∈ C_ℓ(n,α_ℓ)} z_ℓ^{h_ℓ(D_ℓ)}
```

an enumerator of α-constacyclic codes over `F_{q²}` by Hermitian hull dimension. Debnath & Prakash (2022/23) already count constacyclic codes of length `n` over `F_q` by **Galois** hull dimension, and the Hermitian inner product over `F_{q²}` is the special case `m = 2`, `k = 1` of the `k`-Galois product. Sangwisut et al. (2015) already did the cyclic/negacyclic case, and Lu et al. (2026) already exhibit an exact generating function for the cyclic Hermitian case.

Two caveats keep this from being a complete collapse:
* the paywalled bodies were **not** read — only abstracts and citing sentences. The exact *form* of Debnath & Prakash's count (whether it is a closed formula per dimension, an algorithm, or a generating function; whether it covers `p | n`) is **unverified**;
* their setting is a field, not the ring `R_e`, and the source paper's own object is the ring.

### Strand C — ring-level hulls, and the ring the source paper uses

| Work | Ring | What it gives |
|---|---|---|
| Jitman & Sangwisut (2020), *Hulls of cyclic codes over `Z_4`* | `Z_4` | hull types; **average** `2`-dimension `E(n) = 5n/9 − 2B_n/9` |
| Jitman & Sangwisut (2020), `F_2 + vF_2` | non-chain | hull structure, no count |
| Debnath & Prakash (2025/2026), ICTIS | `Z_{p^3}` (chain) | hull types, LCD condition, `p`-dimensions, **and a count of all cyclic codes for a fixed `p`-dimension of the hull** |
| Debnath, Islam, Martínez-Moro, Prakash (2026), *Discrete Math.* | affine algebra ring (non-chain) | `k`-Galois hull dimension; the **cardinality of the set** of attainable `q`-dimensions `δ_k(n,q,λ)` — a set, not a distribution |
| Shi, Huang, Yue (2021), *AAECC* | **`R_e = F_{q²}+uF_{q²}+…+u^{r−1}F_{q²}`** | quantum codes from constacyclic codes over **the same ring family** as the source |
| Quantum Inf. Process. (2023) | `F_q + vF_q` | dimensions of hulls of Gray images over a non-chain ring |
| Entropy (2026) | non-chain ring | `l`-Galois hull dimensions over a ring, quantum construction X |

**Bearing:** ring-level exact counting by hull dimension already exists for a **chain** ring (`Z_{p^3}`, cyclic codes). For the **non-chain** `R_e`, the literature gives hull *dimensions* and *sets* of dimensions, but I found **no** work that counts `λ`-constacyclic codes over `R_e` by Hermitian hull dimension. That is the narrowest surviving gap — and it is a gap I can only call `U` (unresolved), not established, because absence cannot be proven by search.

### Strand D — what the proposed enumeration would sit on top of

The quantum side is mature and does not carry novelty: constacyclic-over-ring quantum codes via a matrix Gray map are in Shi–Huang–Yue (2021) for the same `R_e`, in Islam–Prakash–Verma (2022) for `R_{k,m}`, and in the source paper itself (Theorems 18, 19; Tables 1–3, all reproduced in Phase 1). The Hermitian construction used is the standard one (Ketkar et al. 2006, cited by the source as [22] and verified in Phase 1 as Lemma 17).

---

## 3. What this means for the project (summary; full argument in `NOVELTY_ASSESSMENT.md`)

1. **The constituent enumerator is not new as a problem.** Field-level exact counting of constacyclic codes by (Galois, hence Hermitian) hull dimension is published, most directly by Debnath & Prakash (2022/23) and, for the cyclic case with an explicit generating function, by Lu et al. (2026).
2. **The joint/total enumerator over `R_e` is where any novelty must live** — but under the CRT decomposition `C = ⊕_ℓ η_ℓ C_ℓ`, admissible codes correspond bijectively to `e`-tuples of constituent codes, so `H_joint = Π_ℓ H_ℓ(z_ℓ)` follows from the constituent laws whenever the constituents are independent. The blueprint itself warns: *"Do not treat the phrase 'joint enumerator' as a novelty argument."* That warning now has teeth.
3. **The genuinely unprotected questions** appear to be (a) the distribution in the **repeated-root** regime `p | n` over `R_e` (the source's Theorem 8 allows `p^v > 1`; the accessible abstracts of the counting papers either state restrictions on `q` or work over `F_q` with simple-root assumptions — **unverified**), (b) counting over `R_e` where the multipliers `α_ℓ` can **differ**, so that a `λ ∈ R*_e` admits many component decompositions, and (c) the distribution restricted to **dual-containing** codes, i.e. counting the codes that actually yield quantum codes — which is the step from the source's Theorems 15/16 to a count that nobody in the accessible literature performs for `R_e`.

None of (a)–(c) can be declared new on this evidence. All three are, however, *distinguishable* research questions in the sense Gate 2 requires, whereas the question as currently framed is not.

---

## 4. Honest gaps in this review

| Gap | Consequence |
|---|---|
| Bodies of the paywalled papers (Debnath & Prakash 2022/23, 2025, 2026; Skersys; Sangwisut et al. 2015; Jitman & Sangwisut 2018) were not read | I know *that* they count, not *how*; the comparison is at abstract granularity |
| No library access, no MathSciNet/zbMATH | forward citations are partial; a decisive paper could be missed |
| Conference/thesis literature only partly indexed | same |
| `arXiv:2605.29204` and `arXiv:2607.12242` are recent preprints | their content may change; neither is peer-reviewed as of this review |
| The source paper's own claim (p.20) that its dual-containing approach "is new" | **not assessed here** — it is the source's claim about its own contribution, outside the scope of our project's novelty question |
