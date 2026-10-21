# P1-14 — Mathematical Advancement Without L1 (Independent Audit, New Corollaries, Moment Re-derivation)

**Command:** P1-14 — Mathematical Advancement Without L1  
**Date:** 21 October 2026

**Repository state (verified before any change):** branch `arena/ab8e330d-galios-hull`, local HEAD = remote = `20423cfe22f279728cc380b925da47801b1384fa` (“P1-12: L1 follow-up”), working tree clean. Frozen blueprint `02_THEOREM_BLUEPRINT.md` SHA-256 `ec2fd8d58f8d2a986314f83997d750d689f7c88e98ec8f87753ab4c9cf438cff` — **not edited**, and no proof file or validation script was edited. This file, `code/validate_p1_14.py`, `code/validation_p1_14_output.txt`, and `P1_14_PROPOSED_MANUSCRIPT_STRUCTURE.md` are new artifacts.

**What “independent” means here.** `code/validate_p1_14.py` imports **none** of the earlier validation scripts: it re-implements finite fields `GF(p^d)`, polynomial factorization, `τ`-orbits, the transfer trace, closed-walk counts, and Gram-rank hull dimensions from scratch, and it checks the formulas by three disjoint computational paths (direct exponent-tuple enumeration; fresh polynomial matrix powers; integer-evaluation matrix traces), plus a symbolic (sympy) re-derivation layer. Earlier validators were also re-run unmodified as a baseline (all pass; `validate_p1_03.py` output byte-identical to its saved output). **Computational agreement is evidence, never proof**; every result below is labelled accordingly.

**Headline outcome.** No counterexample to any frozen statement (T1–T6, corrected C1–C6) was found — in the proofs (re-read line by line), in a fresh symbolic re-derivation of every moment closed form, or in exact enumeration over 52 orbit configurations and 2,769 field-level assignments. Three **new corollaries (N1–N3)** are proved completely in §4; they are **proposals** (the frozen blueprint is untouched; adoption needs a Commander decision, exactly like the earlier PC items). L1 and Gate G1 are untouched: **no novelty or priority claim is made anywhere in this file.**

---

## 1. Theorem-by-theorem audit (T1–T6, C1–C7, and the blueprint §2 identity)

Each statement was re-read in `02_THEOREM_BLUEPRINT.md` and checked against its proof in `P1_04_PROOFS_T1_T4.md`, `P1_05_PROOFS_T5_T6_COROLLARIES.md`, `P1_06_MOMENT_PROOFS_C5_C6.md`, then re-tested by the fresh code. Verdicts:

| Statement | Audit method | Verdict |
|---|---|---|
| **T1** (assignments ⟷ codes; `(P+1)^{|F_s|}`) | Proof re-read (RR-1 via PID/UFD Facts 0.1–0.2). Fresh field cases reproduce totals `(P+1)^{|F|}` exactly (27, 27, 256, 256, 16, 2187). | **VERIFIED** |
| **T2** (`#` multiplicative; root transport; compatibility two forms) | Proof re-read (RR-2 (i)–(vi)). Domain discipline of PC-3 respected (`f(0) ≠ 0`, automatic since `S(0) = −μ_s ≠ 0`). Fresh code asserts `τ` permutes the factor set in every field case. | **VERIFIED** (within its stated domain) |
| **T3** (dual exponents `β_i = P − α_{i−1}`) | Proof re-read (RR-3 → Prop. 4.2 → T3). The code-first slot order (S7) is exactly what produces `ρ = σ⁻¹` and `α_{i−1}`; the opposite reading would give the `σ`-version and `α_{i+1}`. Fresh Gram-rank brute force pins the orientation **per assignment** (see §2.3). | **VERIFIED** under the frozen code-first convention |
| **T4** (hull generator `lcm`; dimension sums) | Proof re-read (RR-5 + T3). Fresh check: for **every** assignment in six field cases (2,769 total), `(dim C, dim Hull)` from the Gram matrix equals the T4 formula. | **VERIFIED** (compatible case) |
| **T5** (transfer trace identity) | Proof re-read (closed-walk expansion). Fresh: polynomial trace == direct enumeration == integer-evaluation trace on the grid of §2.1. | **VERIFIED** |
| **T6** (global joint enumerator) | Proof re-read (Prop. 3.1 assembly + distributive law). Layer D rebuilds a two-component global distribution by exact convolution of fresh orbit distributions and reproduces P1-05’s published counts (729 / 16 / 144 / 144) with none of its code. | **VERIFIED** |
| **C1** (total `(P+1)^{Σ|F_s|}`) | `J`-power argument re-read; totals match everywhere. | **VERIFIED** |
| **C2** (code-dimension marginal) | Rank-one trace argument re-read; per-orbit `z=1` marginal checked on the whole Layer-B grid. | **VERIFIED** |
| **C3** (LCD count `2^{#orbits}`) | Proof re-read (repaired boundary argument in P1-05 §5). `[z^0] = 2` per orbit on the whole grid; field LCD counts `2^{#orbits}` in all six cases. Strengthened as **N3** (§4). | **VERIFIED** |
| **C4** (self-orthogonal / dual-containing, incl. PC-4 count) | Nonnegative-edge-difference argument re-read. Per-orbit and global closed-walk counts `tr(B_P^L)`, `tr((B′_P)^L)` match enumeration everywhere tested; the two counts are equal (involution `α ↦ P−α`), e.g. GF(9), `λ=−1`: `100 = 100`. | **VERIFIED** |
| **C5** (means, corrected split) | §5: symbolic re-derivation + enumeration + field cases with pure/mixed orbit lengths. The pre-PC-1 display is refuted concretely (§5.3). | **VERIFIED** (in its frozen, corrected form) |
| **C6** (variance, three regimes) | §5: every closed form re-derived symbolically from tail sums (not from P1-06’s hand algebra); enumeration grid + field variances match (e.g. GF(8): brute `10/9` = `V_1(2) + V_6(2) = 2/9 + 8/9`). | **VERIFIED** |
| **C7** (EAQECC) | Conditional on an externally known distance; the enumerator alone gives no distance. Not a proved enumerator consequence, by design. | **OUT OF SCOPE — conditional only; must never be stated as following from the enumerator** |
| **Blueprint §2 layer identity** `min(P−α_i, α_{i−1}) = Σ_t ε_{i−1}^{(t)}(1−ε_i^{(P−t+1)})` | Proved here (§2.4) and checked for `P = 1..9`, all exponent pairs. | **VERIFIED** |

**No frozen statement requires correction.** The genuine defects found are documentation/reproducibility issues; they are listed honestly in §7.

---

## 2. Independent audit of the transfer-matrix enumerator (T5/T6)

The audited formula (frozen T5/T6):
`E(u,z) = ∏_s ∏_O tr( (T^{(P)}_{w_O}(u,z))^{L_O} )`, with `T_{a,b} = u^{w(P−b)} z^{w·min(P−b, a)}`, row `a` = previous exponent, column `b` = current exponent.

### 2.1 Three disjoint computational paths, one grid
For `P ∈ {1,2,3,4,5,7,8,9}`, all `L ≥ 1` with `(P+1)^L ≤ 100000` (52 `(P,L)` pairs; `w = 1`, plus `w ∈ {2,3}` spot configurations — 58 orbit configurations with moments checked), the fresh script compared:
1. **Ground truth:** direct enumeration of all `α ∈ {0,…,P}^L`, accumulating `(wΣ(P−α_i), wΣ min(P−α_i, α_{i−1}))`;
2. **Polynomial trace:** `tr(T^L)` with bivariate-polynomial matrix entries (fresh implementation);
3. **Integer-evaluation trace:** entries replaced by integers at `(u₀,z₀) ∈ {(2,3),(3,5)}`, ordinary integer matrix power, trace compared against the enumeration polynomial evaluated at the same points.

All three agree on the full joint distribution in every configuration. This is strong evidence; the proof itself is the closed-walk expansion (P1-05 §2), re-read and found complete: the bijection between closed walks `a_0 → … → a_{L−1} → a_0` and assignments is exact **because orbit positions are labeled factors** — there is no division by `L` (a walk and its rotation are different assignments), and the totals confirm it: the trace sums to exactly `(P+1)^L`, never to `(P+1)^L / L`.

### 2.2 Indexing, edge cases, coefficient interpretation
- **Indexing.** Row = predecessor exponent `a_{j−1}`, column = current `a_j`; the edge weight `min(P−a_j, a_{j−1})` is exactly T4’s hull term at position `j`. The closing edge `a_{L−1} → a_0` supplies the term at position `0` with predecessor `α_{L−1}` (indices mod `L`). For `L = 1` this degenerates correctly to the self-loop `tr(T) = Σ_a u^{w(P−a)} z^{w·min(P−a,a)}`, matching `α_{−1} = α_0`.
- **`P = 1` edge case.** `T^{(1)}_w(u,z) = [[u^w, 1],[u^w z^w, 1]]` (rows/cols `0,1`), the predecessor binary matrix of P1-05 §6; at `P=1` the hull edge term is the `1→0` transition indicator. The grid includes `P=1, L=1..8`.
- **Coefficient interpretation.** The coefficient of `u^K z^H` in `tr(T^L)` is the number of exponent tuples on that orbit with code-dimension contribution `K` and hull contribution `H` (both in `F_q`-units after the weight `w`). Verified coefficient-wise (full distribution equality, not just moments). Coefficients are nonnegative integers; `E(u,z) ∈ Z[u,z]` as claimed.
- **Weight scaling.** `T^{(P)}_w(u,z) = T^{(P)}_1(u^w, z^w)` entrywise, so `tr((T_w)^L)(u,z) = tr((T_1)^L)(u^w, z^w)`; the `w ∈ {2,3}` checks confirm the scaling behaves as the formula predicts.
- **Specializations.** `u=z=1`: `(P+1)^L` per orbit (C1 mechanism). `z=1`: per-orbit code marginal `(Σ_{j=0}^P u^{wj})^L` (C2 mechanism) — checked on the grid. `u=1`: hull marginal (no product closed form exists in general — this is precisely why the transfer matrix is needed). `[z^0] = 2` per orbit (C3 mechanism).
- **Hypothesis separation (a clarification the audit makes precise).** As an identity in `Z[u,z]`, T5 holds for **every integer `P ≥ 1`** — the proof is pure matrix multiplication; the prime-power condition `P = p^ϱ` is needed only upstream, where T1/T4 realize orbits and exponents from an actual field factorization. The audit’s `P ∈ {5,7}` grid points exercise the combinatorial identity outside the repeated-root field construction; no theorem statement is thereby extended.

### 2.3 The one thing computation alone cannot see: orientation
Replacing `T` by its transpose produces the distribution of `Σ_i min(P−α_i, α_{i+1})`, which equals the audited distribution under the reversal bijection `α_i ↦ α_{−i}`. **Hence no trace/distribution computation can distinguish predecessor from successor.** The frozen `α_{i−1}` (predecessor) is fixed by the proof chain T3 (`β_i = P − α_{i−1}`, from the code-first pairing) → T4, and it is pinned empirically where it matters: the fresh GF(8) case (`k=1, λ=1, P=2, n_0=7`, orbit lengths `[1,6]`) compares the T4 formula against Gram-rank hull dimensions **assignment by assignment** over all 2,187 assignments — on an `L=6` orbit, predecessor vs successor give genuinely different hull dimensions for generic `α`, so this check (unlike any distribution check) certifies the orientation. (Orbits of length `L ≤ 2` cannot distinguish the two readings; `L=6` can and does.)

### 2.4 The blueprint §2 layer identity (used nowhere in the proofs, now verified)
For `t ∈ {1,…,P}`, `ε^{(t)} = 1[α ≥ t]`. With `a = α_{i−1}`, `b = α_i`: `ε_{i−1}^{(t)} = 1 ⟺ t ≤ a` and `1 − ε_i^{(P−t+1)} = 1 ⟺ t ≤ P−b`. Hence `Σ_{t=1}^P ε_{i−1}^{(t)}(1−ε_i^{(P−t+1)}) = #{t : t ≤ min(a, P−b)} = min(P−α_i, α_{i−1})`. ∎ (Also checked for `P=1..9`, all pairs, in Layer B.) The optional Phase-4 layer-decomposition route therefore rests on a correct identity, should it ever be opened.

---

## 3. Corollaries re-derived from the verified theorem

C1–C4 were re-derived in full in P1-05 §5; this audit re-read those derivations and re-tested every conclusion computationally (§1 table). Two consequences are recorded here in the exact form the manuscript will need (frozen wording preserved; nothing new is claimed beyond what the cited proofs give):

- **Total-count identity (C1).** `E(1,1) = (P+1)^{Σ_s |F_s|}`, equivalently the labeled-assignment count; field totals `3^3, 3^3, 4^4, 4^4, 4^2, 3^7` reproduced exactly.
- **Marginals.** Code-dimension marginal is C2 (`E(u,1) = ∏∏_f (1 + u^{w_f} + ⋯ + u^{Pw_f})`). Hull-dimension marginal is `E(1,z) = ∏_s∏_O tr((T^{(P)}_{w_O}(1,z))^{L_O})` with `T(1,z)_{a,b} = z^{w·min(P−b,a)}` — a trace product, **not** a factor product; its recorded special values are `[z^0] = 2^{#orbits}` (C3) and the first two moments (C5/C6).
- **LCD specialization (C3).** `#{a : dim Hull_{A,k} = 0} = 2^{#orbits}`, independent of `P`; per orbit exactly the two constant tuples `α ≡ 0`, `α ≡ P`. Reproduced in every layer (grid `[z^0]=2`; field counts `8,4,16,4,2,4` against orbit counts `3,2,4,2,1,2`).
- **Simple-root recovery (`P=1`, where the hypotheses permit).** `μ_s = λ_s`, squarefree divisors, binary assignments; hull edge = `1→0` transition indicator; the T6 product is the predecessor binary enumerator (P1-05 §6, re-read). Moments at `P=1`: `E[Hull] = (1/4)·Σ_{L_O≥2} w_O L_O` (since `ν_1 = 0`), `V_1(1) = 0`, `V_2(1) = 1/4`, `V_L(1) = L/16` — all inside the Layer-B grid.

---

## 4. New corollaries proved here (PROPOSED — not in the frozen blueprint)

Standing model (same as frozen): (G1)–(G6) of P1-05; uniform distribution on labeled assignments; per orbit `O`, `A_i` iid uniform on `{0,…,P}`, `X_i = min(P−A_i, A_{i−1})` (indices mod `L = L_O`), orbit code contribution `w_O Σ_i (P−A_i)`, hull contribution `w_O Σ_i X_i`. `F(c) := E[min(c,U)] = c(2P−c+1)/(2(P+1))` (P1-06 Lemma 1.3) and `μ_P = P(2P+1)/(6(P+1))` (P1-06 Lemma 1.1) are used.

### N1. `dim C` and `dim Hull` are uncorrelated (new)
**Statement.** `Cov(dim_{F_q} C(a), dim_{F_q} Hull_{A,k}(C(a))) = 0` under the uniform labeled model — for every component/orbit configuration, every `P ≥ 1`. (They are **not** independent; see the remark.)

**Lemma N1.1 (one shared variable, “self” pairing).** For independent `B, C` uniform on `{0,…,P}`, `Cov(B, min(B,C)) = P(P+2)/24 =: γ_P`.
*Proof.* Condition on `B = b`: `E[min(b,C)] = F(b)`, so `E[B·min(B,C)] = (1/(P+1)) Σ_b b·F(b) = (1/(2(P+1)^2)) Σ_b b²(2P+1−b)`. With `Σ_{b=0}^P b² = P(P+1)(2P+1)/6` and `Σ b³ = (P(P+1)/2)²`, the sum equals `(P/2)·(5P²+5P+2)/12`, hence `E[B·min(B,C)] = P(5P²+5P+2)/(24(P+1))`. Also `E[B]·E[min(B,C)] = (P/2)μ_P = P(4P²+2P)/(24(P+1))`. Subtracting: `γ_P = P(P²+3P+2)/(24(P+1)) = P(P+2)/24`. ∎

**Proof of N1.** Orbit blocks involve disjoint exponent variables, hence are independent (product model, P1-05 Prop. 3.1); cross-orbit covariance terms therefore vanish, and with `K_O = Σ_i (P−A_i)`, `S_O = Σ_j X_j` it suffices to show `Cov(K_O, S_O) = 0` for one orbit, since `Cov(dim C, dim Hull) = Σ_{s,O} w_O²·Cov(K_O, S_O)`. Expand: `Cov(K_O, S_O) = Σ_{i,j} Cov(P−A_i, X_j)`, where `X_j` depends only on `(A_j, A_{j−1})`.
- If `i ∉ {j, j−1}` (possible only for `L ≥ 3`): the two sides are functions of disjoint subfamilies of independent variables ⇒ covariance `0`.
- If `i = j`: `Cov(P−A_j, min(P−A_j, A_{j−1})) = γ_P` by Lemma N1.1 (with `B = P−A_j`, `C = A_{j−1}`).
- If `i = j−1` (requires `L ≥ 2`): `Cov(P−A_{j−1}, min(P−A_j, A_{j−1}))`. Put `C = A_{j−1}`, `B = P−A_j` (independent uniforms): this is `Cov(P−C, min(B,C)) = −Cov(C, min(B,C)) = −γ_P`, because `(B,C)` exchangeable gives `Cov(C, min(B,C)) = Cov(B, min(B,C))`.
- `L = 1`: the single term is `Cov(P−A, min(P−A, A))`. With `B = P−A` uniform, `min(B, P−B)` is invariant under `B ↦ P−B`, so `E[B·min(B,P−B)] = E[(P−B)·min(B,P−B)]`; averaging gives `E[B·min] = (P/2)·E[min] = E[B]·E[min]`, i.e. covariance `0`. (Both parity cases also confirmed symbolically, Layer A.)
For `L ≥ 2` each `j` contributes exactly one `γ_P` (from `i=j`) and one `−γ_P` (from `i=j−1`) — for `L=2` these two indices exhaust `{0,1}`, for `L≥3` all other `i` contribute `0` — so `Cov(K_O, S_O) = L·(γ_P − γ_P) = 0`; for `L=1` it is `0` directly. Summing with weights `w_O²` over all orbits and components gives `0`. ∎

**Remark (uncorrelated ≠ independent).** At `P=1, L=2, w=1`: `Pr(dim C = 2) = 1/4`, `Pr(dim Hull = 1) = 1/2`, but `Pr(dim C = 2, dim Hull = 1) = 0 ≠ 1/8` (fresh enumeration, Layer B). Any manuscript wording must say “uncorrelated”, never “independent”.

**Status.** Proved completely above (the only inputs are P1-06 Lemmas 1.1/1.3 and the product model). Verified exactly: `Cov = 0` in all 58 Layer-B orbit configurations and in all six Layer-C field distributions and the Layer-D global distribution. **Adoption into the blueprint/manuscript result list requires a Commander decision; the frozen file is unchanged.**

### N2. Variance of the code dimension (new)
**Statement.** `Var(dim_{F_q} C(a)) = [P(P+2)/12] · Σ_s Σ_{f∈F_s} w_f²`, where `w_f = m_s·deg_{K_s} f`.
*Proof.* By T4, `dim_{F_q} C = Σ_{s,f} w_f (P − A_f)` with the `A_f` independent uniform on `{0,…,P}` (product model). `Var(P − A_f) = Var(U)` for `U` uniform on `{0,…,P}`: `E[U] = P/2`, `E[U²] = P(2P+1)/6`, so `Var(U) = P(2P+1)/6 − P²/4 = P(P+2)/12`. Independence ⇒ variances add with coefficients `w_f²`. ∎ Consistent with C5’s mean `E[dim C] = (n/2)·Σ_s m_s`. Verified on the whole Layer-B grid (per orbit: `w²L·P(P+2)/12`), all field cases (e.g. GF(8): `Var(C) = 14/3 = 7·(2·4/12)`), and Layer D (`190/3`). **PROPOSED** (same adoption status as N1).

### N3. LCD refinement: joint (LCD, code-dimension) count (new)
**Statement.** `Σ_{a : Hull(a) = 0} u^{dim_{F_q} C(a)} = ∏_{s} ∏_{O∈O_s} (1 + u^{P·w_O·L_O})`. At `u=1` this is C3.
*Proof.* By the C3 argument (P1-05 §5), `Hull(a) = 0` iff on every orbit `α ≡ 0` or `α ≡ P`. The orbit’s code-dimension contribution (T4) is `w_O Σ_i (P−α_i)`, equal to `P·w_O·L_O` for `α ≡ 0` and to `0` for `α ≡ P`. Hence the per-orbit generating polynomial over LCD-admissible tuples is `1 + u^{P w_O L_O}`, and independence over orbits/components (T1, Prop. 3.1) gives the product. ∎ Verified wherever C3 was verified (`[z^0]` counts plus the Layer-D convolution). **PROPOSED** (same adoption status).

---

## 5. Moment formulas C5/C6: symbolic re-derivation, boundary cases, covariance map

### 5.1 Independent symbolic re-derivation (Layer A)
Every closed form of P1-06 was re-derived from its **defining tail/finite sums** with sympy (`summation` over a symbolic `P`; the `L=1` formulas via the parity substitutions `P = 2m, 2m+1` as polynomial sums) — i.e. independently of P1-06’s hand simplifications:

| Quantity | Defining sum | Closed form (P1-06) | Symbolic match |
|---|---|---|---|
| `μ_P` | `Σ_{t=1}^P ((P−t+1)/(P+1))²` | `P(2P+1)/(6(P+1))` | ✓ |
| `E[min(U,V)²]` | `Σ_t (2t−1)((P−t+1)/(P+1))²` | `P(P²+P+1)/(6(P+1))` | ✓ |
| `Var(edge)` | difference | `P(P+2)(2P²+4P+3)/(36(P+1)²)` | ✓ |
| `F(c)` | `Σ_{t=1}^c (P−t+1)/(P+1)` | `c(2P−c+1)/(2(P+1))` | ✓ |
| `E[X_iX_{i+1}]` | `(1/(P+1))Σ_b F(P−b)F(b)` | `P(P−1)(11P²+15P+6)/(120(P+1)²)` | ✓ |
| `κ_P` | difference | `−P(P+2)(7P²+14P+9)/(360(P+1)²)` | ✓ |
| `E[X_0X_1]` (`L=2`) | `Σ_{s,t≥1, s+t≤P} ((P−s−t+1)/(P+1))²` | `P²(P−1)/(12(P+1))` | ✓ |
| `Cov_{L=2}` | difference | `−P²(P+2)²/(36(P+1)²)` | ✓ |
| `ν_P`, `E[X²]`, `V_1` (`L=1`, both parities) | `Σ_a min(P−a,a)^{1,2}` split at `P=2m / 2m+1` | P1-06 Prop. 2.2 / 3.1 | ✓ ✓ ✓ |
| `V_2`, `V_{L≥3}` assemblies | `2Var + 2Cov`; `Var + 2κ_P` per position | P1-06 Prop. 3.6 / 3.4 | ✓ ✓ |
| `γ_P` (new, for N1) | `(1/(P+1))Σ_b bF(b) − (P/2)μ_P` | `P(P+2)/24` | ✓ |
| `Var(U{0..P})` (for N2) | `Σ b²/(P+1) − (P/2)²` | `P(P+2)/12` | ✓ |

The same formulas were then compared against exact rational enumeration (`fractions.Fraction`, no floats) on the Layer-B grid and against the field distributions: **no discrepancy anywhere. No formula fails; no correction to the frozen C5/C6 is needed or proposed.**

### 5.2 Boundary cases (all inside the verified grid)
- **`P = 1`:** `ν_1 = 0` (the self-loop `min(1−A,A) ≡ 0`), `V_1(1) = 0`; `L≥2` edges are Bernoulli`(1/4)`: `Var = 3/16`, and `V_L(1) = L/16`, `V_2(1) = 1/4`.
- **`L = 2` is not the `L≥3` formula:** at `P=2`, true `V_2 = 44/81`, whereas substituting `L=2` into `V_{L≥3}` gives `8/27 = 24/81`. The two edges share **both** variables; P1-06’s separate treatment is necessary (recomputed independently here).
- **Parity at `L=1`:** the even/odd branches of `V_1` are different formulas but asymptotically agree (`~ P²/48`); no discontinuity in `P` is introduced — e.g. `V_1(2) = 2/9`, `V_1(3) = 1/4`, `V_1(4) = 14/25` (grid values all matched enumeration; the closed forms themselves are the symbolic identities of §5.1).
- **`ν_P < μ_P`:** self-loop mean (`~ P/4`) is strictly below the two-independent-uniforms mean (`~ P/3`); this gap is exactly the PC-1 correction.

### 5.3 The refuted pre-correction mean, quantified (why PC-1 mattered)
In the GF(4), `n_0=3, P=2` field case all three orbits have `L=1`: true `E[dim Hull] = 1 = 3·ν_2`. The pre-PC-1 display `μ_P·Σ_O w_O L_O` would give `3·μ_2 = 5/3 ≠ 1`. In GF(9), `λ=1, P=3` (four `L=1` orbits): true mean `2 = 4ν_3`; pre-correction `4μ_3 = 7/2 ≠ 2`. The frozen (corrected) C5 gives the true values in both cases — confirmed against Gram-rank brute force, not just the exponent model.

### 5.4 Covariance-dependence map (what depends on what)
- **Within an orbit, `L ≥ 3`:** adjacent edges are negatively correlated: `κ_P < 0` for all `P ≥ 1`; correlation `κ_P/Var(edge)`: `P=1: −1/3`, `P=2: −13/38`, `P=3: −19/55`. Non-adjacent edge pairs (`L ≥ 4`) are independent (disjoint variable pairs) ⇒ covariance `0`; at `L=3` every pair is adjacent.
- **`L = 2`:** the single pair shares both variables; correlation `Cov_{L=2}/Var(edge)`: `P=1: −1/3`, `P=2: −8/19`, `P=3: −5/11` — different from the adjacent-`L≥3` values at the same `P≥2`, as it must be.
- **Across orbits/components:** independent by the product model ⇒ all cross-covariances `0` (this is what makes C6 a sum with weights `w_O²`).
- **Code vs hull dimension:** covariance exactly `0` (N1) despite dependence (witness in §4). Correlation coefficient is therefore `0` whenever both variances are positive — a clean, quotable fact, provided “uncorrelated” is not upgraded to “independent”.

---

## 6. Worked examples (exact; reproduced by `code/validate_p1_14.py`)

**E1 — one orbit, `P=2, L=2, w=1` (all 9 tuples).** From Layer B (tuple `α=(α_0,α_1)` ↦ `(K,H) = (Σ(2−α_i), Σ min(2−α_i, α_{i−1}))`):
`(0,0)↦(4,0)`, `(0,1)↦(3,1)`, `(0,2)↦(2,2)`, `(1,0)↦(3,1)`, `(1,1)↦(2,2)`, `(1,2)↦(1,1)`, `(2,0)↦(2,2)`, `(2,1)↦(1,1)`, `(2,2)↦(0,0)`. Hence `E[H] = 10/9 = 2μ_2`, `Var(H) = 44/81 = V_2(2)`, `Cov(K,H) = 0`, `[z^0]=2` — the frozen `L=2` variance (not the `L≥3` formula, cf. §5.2) and N1 visible by hand.

**E2 — simple-root orbit, `P=1, L=3, w=1`.** Joint distribution `{(0,0):1, (1,1):3, (2,1):3, (3,0):1}`: hull `=1` exactly on the six non-constant binary necklaces’ tuples with a single `1→0` transition class, `E[H] = 3/4 = 3μ_1`, `Var(H) = 3/16 = V_3(1)`.

**E3 — field case GF(4), `k=1, λ=1, P=2, n_0=5, n=10`** (fresh implementation; factor degrees `[1,2,2]`, orbit lengths `[1,2]`, 27 assignments). Joint `(dim_K C, dim_K Hull)` distribution: `{(0,0):1, (1,1):1, (2,0):1, (2,2):2, (3,3):2, (4,2):2, (4,4):3, (5,5):3, (6,2):2, (6,4):3, (7,3):2, (8,0):1, (8,2):2, (9,1):1, (10,0):1}`. Checks: brute = T4 formula = T6 transfer; `E[H] = 23/9` (orbit split: `1·ν_2 + 2·2·μ_2 = 1/3 + 20/9`), `Var(H) = 194/81`, `Var(C) = 6` (N2), `Cov = 0` (N1), LCD `= 4 = 2²`, self-orthogonal = dual-containing `= 12`. The RR-3 reproduction (below) also ran on this case.

**E4 — field case GF(8), `k=1, λ=1, P=2, n_0=7, n=14`** (orbit lengths `[1,6]`, 2,187 assignments): brute = formula = transfer; `E[H] = 11/3`, `Var(H) = 10/9 = V_1(2) + V_6(2) = 2/9 + 8/9`, `Var(C) = 14/3` (N2), `Cov = 0` (N1), LCD `= 4`, self-orthogonal = dual-containing `= 258`. This is the case that pins the predecessor orientation (§2.3).

**E5 — two-component assembly without P1-05 code (Layer D).** Convolving the fresh per-orbit distributions for `P=2`, orbits `(L,w) = (1,1), (2,3), (1,2), (2,6)` (the `A = GF(2)×GF(4)` example): total `729`, LCD `16 = 2⁴`, self-orthogonal `144`, dual-containing `144` (all as published by P1-05, reproduced independently), plus `E[H] = 11` (C5 split), `Var(H) = 230/9` (C6), `Var(C) = 190/3` (N2), `Cov = 0` (N1).

**RR-3 reproduction (closing a lost-evidence gap).** P1-04 §9’s direct RR-3 check ran a script kept only in `/tmp`. Layer C re-creates it freshly: for **every** assignment in the GF(4) `n_0=3` and `n_0=5` cases, the shifts of the ordinary reciprocal `h^♮` are verified Euclidean-orthogonal to every generator row of `C` and number `deg g` (the inclusion + dimension argument of RR-3). Passed on all 54 assignments. The evidence is now a repo artifact (`code/validate_p1_14.py`), not a `/tmp` file.

---

## 7. Unresolved proof gaps and audit flags (honest list)

**No mathematical gap in T1–T6 / C1–C6 was found, and no counterexample exists in the tested range; no change to the frozen core is needed, and none is made.** The following flags are documentation, scope, or literature items — recorded, not silently fixed:

1. **(Closed by this command)** RR-3’s original direct computational check existed only as `/tmp/check_rr3.py` (P1-04 §9) and was not reproducible from the repo. Reproduced freshly in Layer C (E3 note above).
2. **Evidence layering.** `validate_p1_05.py` imports `validate_p1_03.py`, so the P1-05 multi-component evidence was never code-independent of P1-03; `validate_p1_06.py` tests the orbit model at formula level. `validate_p1_14.py` is import-free and re-derives the same conclusions (including P1-05’s 729/16/144/144) — the dependence is now mitigated, but readers should know the earlier scripts share code.
3. **Frozen-file bookkeeping lags the proofs.** In `02_THEOREM_BLUEPRINT.md` §5, the RR-1…RR-9 checkboxes and the “Prototype-2” box remain unchecked although RR-1…RR-8 are discharged in P1-04…P1-06 and the `F_9` / two-component evidence exists (P1-03/P1-05). This is a stale checklist inside a frozen file; correcting it would require a Commander-approved dated note (GAP-17 rule) and is **not** done here.
4. **Orientation is proof-borne, not computation-borne** (§2.3): any future exposition must keep the code-first convention (S7) visibly attached to T3/T4, because the enumerator’s distribution alone cannot detect a predecessor/successor swap.
5. **Scope boundaries (not gaps):** labeled assignments only (not equivalence/isometry classes); compatible twists only (incompatible: T3 survives in two-modulus form, T4 onward is not claimed); square-free affine `A`; uniform labeled model for all moments; `C7` conditional on external distance data.
6. **Literature (untouched by this command):** L1 full text still unacquired; L1-Q1–Q6 unresolved; **Gate G1 remains DEFERRED**. The mathematical strengthening in this file does not bear on novelty or priority.

---

## 8. What is proved vs what is computational evidence

| Claim | Status |
|---|---|
| T1–T6, C1–C4 | **Proved** (P1-04, P1-05; proofs re-read in this audit). Computation: supporting evidence (Layers B–D). |
| C5 (corrected), C6 | **Proved** (P1-06). Independently re-derived symbolically (Layer A) + exact enumeration evidence. |
| N1 (`Cov = 0`), N2 (`Var(dim C)`), N3 (LCD refinement) | **Proved in §4 of this file** (complete proofs; inputs: P1-05 Prop. 3.1, P1-06 Lemmas 1.1/1.3, T4). Exact enumeration/field evidence agrees everywhere tested. Adoption status: **PROPOSED** — not in the frozen blueprint. |
| Blueprint §2 layer identity | **Proved in §2.4** (one-paragraph proof) + numeric check. |
| All numeric distributions/moments quoted in §6 | **Computational evidence** from `code/validate_p1_14.py` (exact integer/`Fraction` arithmetic; sympy only in Layer A as a derivation aid). Finite checks never constitute proof. |
| Novelty / priority vs L1, L4, L8 | **Not addressed; not claimed.** Gate G1 DEFERRED. |

## 9. Reproducible commands (as executed for this package)

```
python3 code/validate_p1_03.py        # baseline rerun: exit 0, output byte-identical to code/validation_p1_03_output.txt
python3 code/validate_repeated_root.py  # baseline rerun: ALL PROTOTYPE CHECKS PASSED
python3 code/validate_p1_05.py        # baseline rerun: ALL P1-05 MULTI-COMPONENT ASSEMBLY CHECKS PASSED
python3 code/validate_p1_06.py        # baseline rerun: ALL P1-06 MOMENT CHECKS PASSED
python3 code/validate_p1_14.py        # NEW: exit 0 in ~8s; full output saved as code/validation_p1_14_output.txt
                                      # final line: ALL P1-14 INDEPENDENT AUDIT CHECKS PASSED
                                      # (Layer A uses sympy if importable; Layers B–D are stdlib-only)
```

Key output lines: “Layer A done: every P1-06 closed form re-derived symbolically; gamma_self = P(P+2)/24 confirmed” · “orbit grid: 52 (P,L) pairs; … N1 (Cov=0 in 58 orbit configs incl. weights), N2 all checked” · six `FIELD …` blocks (§6) · “OK: P1-05 global counts reproduced independently; moments verified”.
