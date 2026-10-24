# Phase 6 deliverable — Quantum parameter verification

Independent checks on `QUANTUM_CODE_PARAMETER_TABLE.csv` (504 rows). The point is **not** to restate
the table but to attack it: every quantity is recomputed by a route that does not share code with the
route that produced it, where such a route exists.

From `4997773`. Log `p3_quantum_table_log.txt`.

---

## 1. What each column means

| Column | Meaning |
|---|---|
| `instance` | ring / field / length |
| `q`, `e`, `n` | parameters |
| `M` | the Gray matrix used (must be named: L-3) |
| `lambda_components` | `λ(μ_ℓ)` for `ℓ = 1..e` — the **CRT coordinates**, not the paper's unnormalised `η`-coefficients (F-1) |
| `component_dims` | `dim C_ℓ` over `F_{q²}` |
| `en` | Gray-image length |
| `K` | `dim ψ(C)`, computed as the **rank of the explicit image** |
| `quantum_k` | `2K − en` |
| `d` | exact minimum weight of `ψ(C)` |
| `quantum_params` | `[[en, 2K−en, ≥d]]_q` |
| `quantum_singleton_slack` | `(2K−en) + 2d − (en+2)`; `0` means quantum-MDS, negative means below the bound's reach |
| `rank_eq_sum_of_dims` | does `rank ψ(C)` equal `Σ_ℓ dim C_ℓ`? |
| `degenerate_zero_k`, `trivial_full_k` | flags for `K = en` (no logical qudits) and `K = en` (whole space) |
| `distance_exact` | always `yes`: no distance in the table is a bound |

## 2. Check 1 — dimension computed two independent ways

`K` is obtained as `rank(ψ(C))` from the explicitly constructed Gray image. The formula route is
`K = Σ_ℓ dim C_ℓ` (Theorem 1 + bijectivity). **Agreement: 504/504.**

This is a genuine independent check, not a tautology: the formula route never builds `ψ`, and the rank
route never uses the CRT decomposition — it only needs `M` and the component bases.

## 3. Check 2 — the table reproduces the earlier distribution

`P3_4_QUANTUM_DISTRIBUTION.md` computed the distributions using `K = Σ dim` and a different distance
routine. The regenerated table gives **identical parameter sets and identical multiplicities**:

| Instance | P3-4 | this table | match |
|---|---|---|---|
| `R_2/F_9/n=2` | 8, 8, 64, 64 | 8, 8, 64, 64 | ✓ |
| `R_2/F_9/n=3` | 16, 64, 64 | 16, 64, 64 | ✓ |
| `R_3/F_4/n=2` | 27, 81, 81, 27 | 27, 81, 81, 27 | ✓ |

Two independent scripts, same numbers.

## 4. Check 3 — quantum Singleton, and why the MDS count is not a finding

`k + 2d ≤ n + 2`. Rows with slack `0` are quantum-MDS. Raw counts look impressive and are misleading:

| Instance | codes | quantum-MDS | **non-trivial** (`0 < k < en`) | **non-trivial MDS** |
|---|---|---|---|---|
| `R_2/F_9/n=2` | 144 | 136 | 64 | 64 |
| `R_2/F_9/n=3` | 144 | 128 | 80 | 64 |
| `R_3/F_4/n=2` | 216 | 27 | 162 | **0** |

**Explicit warning.** The headline "136 of 144 are quantum-MDS" is an artefact: `K = en` (the whole
space, `d = 1`, two logical-... zero-distance codes) and `K = 0` rows are counted. At `n ≤ 3` the
quantum Singleton bound is weak in any case. The honest reading:

* `R_2/F_9/n=2`: **all 64** non-trivial codes are `[[4,2,2]]_3`, which is quantum-MDS — a real but
  tiny and surely classical fact at these parameters.
* `R_3/F_4/n=2`: **none** of the 162 non-trivial codes is quantum-MDS.
* No comparison with published tables is made, and **no claim that any parameter is good, new, or
  competitive**. The source's Section 5 tables are stronger.

## 5. Check 4 — bounds of `P3_3_RING_GRAY.md` Theorem 2 hold row by row

For every row, `min_ℓ d_ℓ ≤ d ≤ e·min_ℓ d_ℓ` was checked against the component distances. No violation
(the same check on all 256 + 576 pairs and 216 triples is recorded in `p3_ring_gray_log.txt`; the CSV is
a strict subset of those tuples).

## 6. Check 5 — dual-containing, verified independently

The ring code's dual-containing property is established by the **componentwise** criterion
(`DUAL_CONTAINING_ENUMERATION.md`), while `field_is_dc` decides each component by a basis test that does
not use the lcm formula. The tuple count equals `(#DC)^e` in all three instances (`12²`, `12²`, `6³`),
which is what the theorem predicts; a counting error in either the criterion or the enumeration would
break that identity.

## 7. Residual verification gaps — stated, not hidden

| Item | Status |
|---|---|
| `K` and `d` for rows where `ψ(C)` is large | all rows here were fully enumerable; nothing was estimated |
| Magma cross-check | **not done** — Magma is not available in this environment (blueprint Phase 7 asks for it if genuinely available; it is not) |
| Independent implementation of the Gray map | the `psibasis` construction was checked against `p3_ring_gray.gray_e2`'s weight routine via the parameter agreement in §3, but both live in the same codebase. A third-party reimplementation has not been done |
| QECC parameter databases | **not consulted**. No claim of "better than known" is made anywhere, so no comparison was required |
