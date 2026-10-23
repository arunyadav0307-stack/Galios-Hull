# NOVELTY ASSESSMENT — Phase 2

**Question put by the blueprint (Gate 2):** *"The proposed main contribution is distinguishable from the closest known results. Otherwise revise the research question."*

**Answer: the question as currently framed is NOT distinguishable. Gate 2 is NOT PASSED on the present framing. A revision is required, and three candidate revisions that do survive the comparison are set out in §5.**

This is a negative result about the *framing*, not about the source paper (whose mathematics was independently reproduced in Phase 1) and not about the soundness of the source. It is reported rather than worked around, because the blueprint's own rule is to deliver a feasibility finding instead of a misleading manuscript.

**Classification vocabulary (blueprint §2B):** `N1` apparently new with documented comparison · `N2` potentially new but needs further checking · `K` known or routine · `F` false under proposed assumptions · `U` unresolved.

**Evidence basis and its limit.** All comparisons rest on abstracts, citing sentences and reference lists; the bodies of the paywalled works were not readable from this sandbox (`REFERENCE_VERIFICATION_REPORT.md` §4 lists them). Therefore **nothing below is classified `N1`**, and every "known" is asserted only where the work's own abstract states it explicitly.

---

## 1. The proposed contribution, decomposed

Blueprint Phase 3 proposes, for the source's ring `R_e = F_{q²} + uF_{q²} + … + u^{e−1}F_{q²}` (`u^e = 1`, `e | q+1`) and multipliers `λ = Σ_ℓ η_ℓ α_ℓ`:

| ID | Proposed element |
|---|---|
| **E1** | Constituent enumerator `H_ℓ(z_ℓ) = Σ_{D_ℓ ∈ C_ℓ(n,α_ℓ)} z_ℓ^{h_ℓ(D_ℓ)}`, `h_ℓ = dim_{F_{q²}} Hull_H(D_ℓ)` |
| **E2** | Joint enumerator `H_joint(z₁,…,z_e) = Σ_{admissible C} Π_ℓ z_ℓ^{h_ℓ(D_ℓ)}` |
| **E3** | Total enumerator `H_total(z) = H_joint(z,…,z) = Σ_j N_j z^j`, `N_j` = number of admissible ring codes with total hull dimension `j` |
| **E4** | The relation between total and constituent hull dimensions (the blueprint insists it be proved before `H_total` is interpreted) |
| **E5** | Well-definedness: what counts as a distinct code; uniqueness of the constituent representation; independence of constituent choices |

---

## 2. E1 — the constituent enumerator: **K (known or routine)**

The object `H_ℓ` is an exact count of `α`-constacyclic codes over a field by hull dimension. That problem is solved in the literature, several times over:

* **Sangwisut, Jitman, Ling, Udomkavanich (2015)** — hull dimensions of cyclic and negacyclic codes **and the number of codes for a given dimension of the hull** (stated in the citations of it that I could read).
* **Debnath & Prakash (2022/23), *Galois hulls of constacyclic codes over finite fields*** — abstract: *"a formula for the dimension of Galois hulls of constacyclic codes … considering some restrictions on q, the number of constacyclic codes of length n over F_q is calculated for a given Galois hull dimension."* This is `H_ℓ` for the constacyclic case, with the `k`-Galois product that specialises to the Hermitian product at `m = 2, k = 1`.
* **Lu, Yang, Liu, Fu, Guo (arXiv:2607.12242, v3 Oct 2026)** — Appendix B, *"Counting and the fine structure of the τ-fixed cosets"*: a **product enumerator** giving the **exact counts** of cyclic codes by hull codimension, plus the scarcity probability and the mean and variance.
* The same 2026 paper states in its own positioning section that *"codes have been enumerated by hull dimension, for cyclic and negacyclic codes [34, Thms. 22 and 23]"* — an independent 2026 confirmation that the enumerator over a field is prior art, not a gap.
* **arXiv:2605.29204 (2026)** — `A^H_{n,k,ℓ,q²}` for all `[n,k]` codes over `F_{q²}`.

**Residual uncertainty (why this is `K` and not `K`-certain).** I did not read Debnath & Prakash's body: I cannot confirm (i) that their "restrictions on q" admit the `m = 2, k = 1` Hermitian case, (ii) that their count is per-dimension rather than an aggregate, (iii) whether they treat `p | n`. If any of these fails, E1 degrades from `K` to `N2`. **The check is one library visit away and must be done before any claim is made.** What is *not* in doubt is that the *problem type* — enumerating constacyclic codes by hull dimension over a field — is established prior art, so E1 cannot carry a novelty claim on its own.

---

## 3. E2 / E3 — the joint and total enumerators: **N2 at best, and vulnerable**

**Why they are not automatically new.** Under the source's own Theorem 1/2 and its CRT decomposition, a λ-constacyclic code over `R_e` corresponds to an `e`-tuple `(C₁,…,C_e)` of `α_ℓ`-constacyclic codes over `F_{q²}`, and the correspondence is a bijection onto admissible tuples. If the tuple coordinates are free (subject only to `λ = Σ η_ℓ α_ℓ ∈ R*_e`), then

```
H_joint(z₁,…,z_e) = Π_{ℓ=1}^{e} H_ℓ(z_ℓ; n, α_ℓ)
```

is a product of the constituent laws. A product of known generating functions is a **routine** consequence, not a discovery — and the blueprint anticipates exactly this trap: *"Do not treat the phrase 'joint enumerator' as a novelty argument."*

**What could still make E2/E3 non-routine** — and each of these is a proof obligation, not a slogan:

| # | Condition that would lift E2/E3 from routine to `N2` | Status |
|---|---|---|
| a | The constituents are **not** free: admissibility genuinely couples the tuple (e.g. the `α_ℓ` are linked, or `λ` constrains which tuples occur) | **`U`** — the source fixes `λ = Σ η_ℓ α_ℓ` but does not study how many `λ` yield a given tuple |
| b | The **repeated-root** regime `p^v > 1` changes the orbit structure over `R_e` in a way the field-level papers do not cover | **`U`** — the source's Theorems 8/10 do allow `p^v > 1`; whether the field-level counting papers do is unverified |
| c | Counting *distinct codes* over `R_e` differs from counting generator descriptions (the `η_ℓ` are not normalised — see Phase 1 finding F-1) | **`U`** — a real technical hazard: with the printed `η_ℓ`, `⟨Σ η_ℓ g_ℓ⟩` is well defined only up to the scalar of the idempotents, and a naive count could over- or under-count |

Note (c) connects Phase 1 to Phase 2: finding **F-1** (the printed `η_i` are unnormalised quotients) is exactly the kind of defect that would corrupt a count of distinct codes if §3A of the blueprint were skipped.

---

## 4. E4 and E5 — already inside the source paper or elementary: **K**

* **E4 is not an open question.** The source's proof of Theorem 8 already states and uses `dim(Hull_H(C)) = dim(Hull_H(C₁)) + dim(Hull_H(C₂))` (p.10), and Theorem 10 extends it to `e` components (p.13). Phase 1 verified it independently on `ψ(C)` (audit item A7: `hull(ψ(C)) = hull(C₁) + hull(C₂)` in all three test constructions). So the "relationship between total and constituent dimensions" is established prior art *in the very paper being extended*.
* **E5 is routine.** Uniqueness of the constituent representation is the CRT decomposition (source Theorem 2, Phase 1 audit A1–A2); distinctness of codes is the standard `[n,k]`-subspace notion used by Sendrier and by every counting paper in the matrix. The only non-routine part is the `η_ℓ` normalisation trap, which is a hazard to avoid, not a result to claim.

---

## 5. What survives: three revised questions

Each of these is *distinguishable* from the works in `LITERATURE_COMPARISON_MATRIX.csv` **on the evidence available**, and each comes with the check that would kill it. None is claimed new.

### R1 — The hull-dimension distribution over `R_e` in the repeated-root regime `p | n`

* **Question.** For `n = p^v n'` with `v ≥ 1`, enumerate λ-constacyclic codes over `R_e` by Hermitian hull dimension and compare with the `v = 0` law.
* **Why distinguishable.** The source's Theorem 8 is stated for general `p^v` but never counts; the counting papers I could inspect state restrictions on `q` and work over fields, not over `R_e`.
* **Kill criterion.** If Debnath & Prakash (2022/23) already covers `p | n` **and** their count composes over the `e` components, R1 collapses to `K`.

### R2 — Counting `λ`-constacyclic codes over `R_e` when the multipliers `α_ℓ` differ

* **Question.** `λ = Σ η_ℓ α_ℓ` admits many decompositions; with `α₁ ≠ α₂` (as in every non-trivial row of the source's Tables 1–3), how many admissible codes have a given hull-dimension vector, and how does the count depend on the decomposition of `λ`?
* **Why distinguishable.** The field-level literature has a single multiplier; the ring-level literature I found counts hull *sets*, not codes, and for chain rings.
* **Kill criterion.** If `λ`'s decomposition is unique up to unit multiplication in `R_e*`, the question degenerates; **this must be settled first, and it is a short computation** (the source's own Tables 1–3 use `λ = ε₁ + 6ε₂`, `t^{36}ε₁ + ε₂`, etc., so decompositions plainly vary).

### R3 — Restricting the enumeration to dual-containing codes, i.e. counting the quantum-code-producing subfamily

* **Question.** Among λ-constacyclic codes over `R_e` with `C^{⊥H} ⊆ C` (source Theorems 15/16), give the hull-dimension distribution, and hence the distribution of the quantum parameters `[[en, 2k−en, ≥d]]` produced by Theorems 18/19.
* **Why distinguishable.** The source gives the *criterion*; no accessible work counts the codes satisfying it over `R_e`. This is the shortest bridge from the source paper to a genuinely new count, and it uses Phase 1's verified machinery (all 33 table rows were independently confirmed dual-containing).
* **Kill criterion.** If the dual-containing subset is a product of independent per-component conditions — which Theorem 15's `b_ij + c_ij ≤ p^v` shape suggests it may be — then the count factors again and R3 reduces to routine work on the constituent laws.

---

## 6. Verdict

| Proposed element | Classification | Basis |
|---|---|---|
| E1 constituent enumerator `H_ℓ` | **K** (known or routine) | Debnath & Prakash 2022/23; Sangwisut et al. 2015; Lu et al. 2026; arXiv:2605.29204 |
| E2 joint enumerator | **N2** (conditional) / **K** if constituents are free | multiplicativity of the CRT decomposition; unverified independence |
| E3 total enumerator | **N2** (conditional) / **K** | same; no independent content beyond E2 |
| E4 total-vs-constituent dimension relation | **K** | already proved in source Theorem 8/10; re-verified in Phase 1 (A7) |
| E5 well-definedness | **K** (routine), with a real `η_ℓ` hazard | source Theorem 2; Phase 1 finding F-1 |
| R1 repeated-root distribution over `R_e` | **N2** | no accessible work covers it; unverified |
| R2 differing multipliers `α_ℓ` over `R_e` | **N2** | no accessible work covers it; uniqueness question must be settled first |
| R3 dual-containing subfamily count | **N2** | no accessible work covers it; factorisation risk |

**Gate 2: NOT PASSED for the research question as framed.** The framing "enumerate constacyclic codes by hull dimension, and take the joint/total distribution over `R_e`" is `K` at the constituent level and conditional at the ring level, and the blueprint's own warning about the phrase "joint enumerator" applies to it verbatim.

**Recommendation:** adopt one of R1–R3 (or a combination) as the research question, and settle the corresponding kill criterion *before* Phase 3 begins. Per the blueprint, Gate 2 is to be re-run after the revision; a revised question that survives it can then be developed in Phases 3–4.

**No novelty is claimed anywhere in this document.** Every "distinguishable" above means "not found in the accessible literature under an explicitly stated search", which is the strongest statement the evidence supports.
