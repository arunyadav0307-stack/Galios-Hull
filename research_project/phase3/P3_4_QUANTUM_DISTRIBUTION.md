# Phase 3 / P3-4 — The ring-level quantum-parameter distribution

**What this is.** The first exact distribution of dual-containing `λ`-constacyclic codes over `R_e` by
their quantum parameters `[[en, 2K−en, ≥d]]`, with `d` computed exactly through the Gray map for a
**fixed, named** matrix `M`. It is the deliverable the GO verdict in `P3_3_RING_GRAY.md` §9 pointed to.

Probe: `phase3/p3_quantum_dist.py`, log `p3_quantum_dist_log.txt`. Stdlib only, ≈ 24 s.
Branch `arena/831a2e65-galios-hull`, from `cd89f69`.

**This is a computational result with tables. It is not a theorem, and no claim is made that the
parameters below are good, new, or competitive.** The source paper already tabulates better codes.

---

## 1. Setting (inherited, not re-derived)

`R_e = F_{q²}[u]/(u^e − 1)`, `e \| (q+1)`; `λ = Σ_ℓ e_ℓ λ_ℓ ∈ R_e^*` with `λ_ℓ ∈ F_{q²}^*`;
`C ↔ (C_1,…,C_e)` by CRT; Hermitian duality with the ring `q`-power; Gray map `ψ` with a fixed
admissible `M` (`M M^* = νI_e`, `ν ≠ 0`).

Three inputs, all proved earlier in this phase:

* **Thm 1 (P3-3)** — `C^{⊥_H} ⊆ C` **iff** `C_ℓ^{⊥_H} ⊆ C_ℓ` for every `ℓ`. So the dual-containing
  tuples are exactly tuples of dual-containing field codes; this is what makes the enumeration
  complete rather than heuristic.
* **`ψ` is bijective linear** — so `K := dim ψ(C) = dim C = Σ_ℓ k_ℓ`. The quantum dimension is
  determined by the constituents.
* **`d = d(ψ(C))`** — computed exactly, never bounded (Thm 2's bounds are used only as a sanity
  envelope, never as a substitute).

The quantum code attached to `ψ(C)` is `[[en, 2K − en, ≥d]]_q` (source Theorem 19 / Lemma 17).

## 2. The distributions

### 2.1 `R_2` over `F_9`, `n = 2`, `M = [[1,1],[1,−1]]` (`ν = 2`)

Dual-containing tuples: **144** = `12²` (12 dual-containing field codes per coordinate — a
consistency check on the enumeration, not an assumption).

| Quantum code | count |
|---|---|
| `[[4, 0, ≥2]]` | 8 |
| `[[4, 0, ≥3]]` | 8 |
| `[[4, 2, ≥2]]` | 64 |
| `[[4, 4, ≥1]]` | 64 |

### 2.2 `R_2` over `F_9`, `n = 3`, `M = [[1,1],[1,−1]]`

Dual-containing tuples: **144** = `12²`.

| Quantum code | count |
|---|---|
| `[[6, 2, ≥2]]` | 16 |
| `[[6, 4, ≥2]]` | 64 |
| `[[6, 6, ≥1]]` | 64 |

### 2.3 `R_3` over `F_4`, `n = 2`, `M = ((1,2,2),(2,1,2),(2,2,1))` (`ν = 1`, all entries nonzero)

Dual-containing tuples: **216** = `6³`.

| Quantum code | count |
|---|---|
| `[[6, 0, ≥2]]` | 27 |
| `[[6, 2, ≥1]]` | 81 |
| `[[6, 4, ≥1]]` | 81 |
| `[[6, 6, ≥1]]` | 27 |

## 3. The one thing the tables establish

**The quantum parameter is not determined by the constituent data — at the ring level, not just the
field level.**

Over `F_9`, `n = 2`, the constituent data `((k_1,d_1),(k_2,d_2)) = ((1,2),(1,2))` is realised by
several admissible tuples, and the resulting quantum code is **`[[4, 0, ≥2]]` for some tuples and
`[[4, 0, ≥3]]` for others**. Same `K = 2`, same component dimensions, same component distances —
**two different quantum distances**.

This is exactly Theorem 5 of `P3_3_RING_GRAY.md` lifted to the object the project cares about. It is
also the concrete reason the distribution is not a product of field-level laws: a product law would
have to assign a single distance to `((1,2),(1,2))`.

**Honest counterweight.** The effect is *invisible* in the `e = 3`, `F_4` instance: there every
dual-containing field code has the same `(k,d)`, so no group with two parameters occurs (0 of 4
groups). Non-determination needs *ties* in the constituent data realised by *inequivalent* codes;
small single-class fields cannot show it. The `F_9` instance is doing the real work here, and a
reader should not generalise the `F_4` row's flatness into a claim that the effect is rare.

## 4. Degeneracies and what the tables do **not** show

| Item | Note |
|---|---|
| `K = en` rows (`[[4,4,≥1]]`, `[[6,6,≥1]]`) | the code is the whole space; `d = 1`, quantum code trivial. Included only for completeness. |
| `K = 0` rows (`[[4,0,·]]`, `[[6,0,·]]`) | quantum code has **zero** logical qudits — degenerate, not usable. |
| Smallest non-trivial | `[[4,2,≥2]]` and `[[6,2,≥2]]`: 2 logical qudits, distance `≥ 2`. Weak, and not claimed good. |
| `d ≥ 2` everywhere | consistent with Thm 2 (`min_ℓ d_ℓ ≥ 1`) and with no component code having `d = 1` except the trivial ones. |
| Not done | no comparison with published quantum-code tables; no claim of improvement, optimality, or novelty |

## 5. Reproducibility

| Check | Result |
|---|---|
| Dual-containing tuple counts match `(#DC)^e` | `12² = 144`, `12² = 144`, `6³ = 216` — **3/3** |
| `2K − en ≥ 0` holds for all enumerated tuples | yes (guarded; no tuple rejected) |
| Distances exact | all from codeword enumeration, none from bounds |
| `M` recorded | yes, for every table |
| Degenerate `M` refused | the `e = 2` matrix over `F_4` gives `ν = 2 = 0` and is skipped (P3-3 §6) |

Log: `p3_quantum_dist_log.txt`.

## 6. Novelty statement — explicitly bounded

| Claim | Status |
|---|---|
| Exact `(hull, Gray distance)` distribution for constacyclic codes over `R_e` | **not found** in the accessible literature; `R4_FEASIBILITY.md` §6.1 records that the mass-formula line cannot specialise to constacyclic families and that constacyclic work gives hull dimensions or tables, not distributions |
| The negative structure (parameter not determined by constituents) | Theorem 5 + §3 here; the phenomenon is implicit in Gray-map examples, but I found no source stating it |
| The parameters themselves | **no claim.** Trivially small, degenerate cases included, nothing competitive |

**Not claimed:** novelty. Blockers **B-1** (publisher full texts) and **B-2** (Debnath–Prakash body)
remain open; either could contain a distribution of this kind, and until they are resolved any
novelty statement would be unsupported.

## 7. Verdict — end of the Phase 3 programme

| Deliverable | Status |
|---|---|
| K4-2 feasibility | done (`K4_2_FEASIBILITY.md`) |
| P3-1 exact field-level `(hull, d)` tables | done; two conjectures refuted (`P3_1_TABLES.md`) |
| P3-2 structural lemmas for the two-orbit family | four lemmas proved (`P3_2_TWO_ORBIT.md`) |
| P3-3 ring-level Gray coupling | five theorems; bounds elementary, one decisive negative (`P3_3_RING_GRAY.md`) |
| **P3-4 ring-level quantum-parameter distribution** | **done — this document** |

**GO** on the narrowed contribution: *the exact joint (Hermitian hull dimension, Gray distance)
distribution of dual-containing `λ`-constacyclic codes over `R_e`, its non-product structure, and the
resulting quantum-parameter distribution* — a computational, distributional result supported by
Theorems 1–5.

**NO-GO** on any structural-theorem headline: the bounds are elementary, the base ring is a product
of fields, and the sharpest statements are negative.

The Phase 3 programme identified in `R4_FEASIBILITY.md` §7 is now complete. What remains to make this
publishable is **not more computation** — it is the two literature blockers, plus a scaling question
(§8).

## 8. Limitations, carried forward unchanged

| # | Item | Status |
|---|---|---|
| L-1 | four middle distances of the two-orbit family | computed only, no proof |
| L-2 | `n = 9` power-attainment conjecture | conjecture, 10/10 support |
| L-3 | choice of `M` | **open convention**; exact distances depend on it, bounds do not |
| L-4 | even characteristic | the paper's `e = 2` matrix is singular there; another `M` is needed |
| L-5 | **B-1** publisher full texts | **open blocker** |
| L-6 | **B-2** Debnath–Prakash body text | **open blocker** |
| L-7 | Thm 5 is witness-based, not a general construction | limitation of the statement |
| **L-8 (new)** | **scaling** | the enumeration costs `∏_ℓ \|C_ℓ\|` per tuple; `e = 2, n = 3` already involves 144 tuples × ≤ 3⁴ codewords. Nothing here shows feasibility for `n` beyond single digits, and no asymptotic claim is made |

Nothing above is promoted to a theorem. No manuscript is drafted.
