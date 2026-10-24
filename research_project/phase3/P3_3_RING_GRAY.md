# Phase 3 / P3-3 — Ring-level (`R_e`) Gray coupling

**Question.** Does the Gray-map interaction produce a substantive mathematical result beyond the
constituent-level formulas already established?

**Answer, stated first.** It produces **four small theorems with complete proofs** (§4) and a
**decisive negative structural result** (§5): the Gray distance is *not* determined by the constituent
parameters, and for `e ≥ 3` not even when all constituents are equal. It does **not** produce a closed
formula, and the bounds in §4 are elementary — close to folklore. So the honest verdict (§8) is
**GO for the distributional contribution, NO-GO for a "Gray-coupling structural theorem" as the
headline claim.**

Probe: `phase3/p3_ring_gray.py`, log `p3_ring_gray_log.txt` (43 lines). Earlier probe
`phase3/p3_tables.py` was re-run with a stdlib distance routine and reproduces the committed P3-1
numbers exactly (§7). Branch `arena/831a2e65-galios-hull`, from `148c6dc`.

---

## 1. Setting and conventions, fixed explicitly

| Item | Convention |
|---|---|
| Ring | `R_e = F_{q²}[u]/(u^e − 1)`, `q = p^m`, `e ≥ 2`, `e \| (q+1)`. Then `q ≡ −1 (mod e)` and `x^e − 1` splits into distinct linear factors over `F_{q²}` (`p ∤ e`). |
| Idempotents | `e_μ = (1/e) Σ_j μ^{−j} u^j` for `μ ∈ U_e`, the `e`-th roots of unity. The `η_ℓ` printed in the source are `∏_{μ'≠μ}(u − μ')`, i.e. `e_μ` multiplied by a scalar (**Phase 1 finding F-1**). |
| Involution | `y ↦ y^q` with the **ring** power: `u ↦ u^q = u^{−1}`, coefficients raised to `q`. **Fixes every idempotent** (proved in R3, re-derived in `R1_FEASIBILITY.md` §1): `e_μ^q = e_μ`. |
| Duality | Hermitian: `⟨x,y⟩_H = Σ_i x_i y_i^q`; `C^{⊥_H} = {x : ⟨x,c⟩_H = 0 ∀c ∈ C}`. |
| Code family | `λ`-constacyclic over `R_e`, `λ = Σ_ℓ e_ℓ λ_ℓ ∈ R_e^*`, i.e. ideals of `R_e[x]/(x^n − λ)`; equivalently tuples `(C_1,…,C_e)` of `λ_ℓ`-constacyclic codes over `F_{q²}`. Dual-containing means `C^{⊥_H} ⊆ C`. |
| Length | `n` arbitrary; `n = p^v n'` with `gcd(n',p) = 1` allowed (repeated-root case). |
| Coordinates | For a word `r = (r_0,…,r_{n−1}) ∈ R_e^n` write `r_i = Σ_k η_k s_{ki}` (`η`-basis, as in the source) and `c_k(i) = (η_k(μ_k)) s_{ki}`, the CRT coordinate of `r_i` in the `k`-th component. Since `η_k(μ_k) ≠ 0`, **`s_k` and `c_k` have the same support** and differ by a nonzero per-component scalar. |
| Gray map | `ψ(r) = [ (s_{1i},…,s_{ei}) M ]_{i=0}^{n−1} ∈ F_{q²}^{en}`, `M` a square matrix of order `e` with `M M^* = ν I_e`, `ν ∈ F_{q²}^*,` `M^*` the Hermitian transpose. `M` is **not fixed by the paper**; every statement below names the `M` it uses. |
| Distance | `d(ψ(C)) = min{ w(ψ(c)) : c ∈ C, c ≠ 0 }`, `w` Hamming weight in `F_{q²}^{en}`. |

Two facts used throughout, each machine-verified in this session: `M M^* = νI` with `ν ≠ 0` makes `M`
invertible (`det M · conj(det M) = ν^e`); and `Admissibility` of `M` is checked numerically by
`matrix_ok`.

## 2. What CRT preserves, and what the Gray map changes

This is the distinction requirement §2 of the task asks for, and it is the crux of P3-3.

**Preserved algebraically (no Gray map involved).**

| Property | Behaviour | Status |
|---|---|---|
| ideal structure / generator polynomials | `R_e[x]/(x^n−λ) ≅ ∏_ℓ F_{q²}[x]/(x^n−λ_ℓ)`; codes ↔ tuples, bijectively | PIR lemma, R1 |
| Hermitian hull | `Hull_H(C) = ⊕_ℓ Hull_H(C_ℓ)`, so `dim Hull_H(C) = Σ_ℓ dim Hull_H(C_ℓ)` | proved in R3; re-verified below on 4 instances |
| dual-containing | `C^{⊥_H} ⊆ C ⟺ C_ℓ^{⊥_H} ⊆ C_ℓ` for every `ℓ` | proved in R3 |

**Changed by the Gray map.** The Gray map mixes the `e` component symbols **at each position** through
`M`. It is therefore **not** coordinatewise on components, and the resulting Hamming weight is not
the sum of component Hamming weights. Precisely,

```
W(c) = Σ_i g_i,        g_i = #{ j : ((s_{1i},…,s_{ei}) M)_j ≠ 0 },
```

and writing `u(c) = #{ i : (s_{1i},…,s_{ei}) ≠ 0 } = |∪_k supp(c_k)|`:

* `g_i = 0 ⟺ the position vector is 0`, because `M` is invertible;
* `1 ≤ g_i ≤ e` otherwise.

Hence the **key inequality**, valid for **every** admissible `M` and every `e`:

> **u(c) ≤ W(c) ≤ e·u(c).**

It depends only on `M` being invertible, i.e. on `MM^* = νI` with `ν ≠ 0`. The exact value of
`W(c)` depends on `M` and on the per-component scalars `η_k(μ_k)` (the F-1 normalisation), because
rescaling a coordinate changes which entries of `(sM)` vanish. **The bounds are convention-free; the
values are not.** That sentence is the whole reason the bounds are provable and the formula is not.

## 3. Hull dimensions (proved; independent of the Gray map)

**Theorem 1.** Let `C = ⊕_ℓ e_ℓ C_ℓ` be a `λ`-constacyclic code over `R_e`, `e \| (q+1)`. Then
`Hull_H(C) = ⊕_ℓ Hull_H(C_ℓ)` and `dim Hull_H(C) = Σ_ℓ dim Hull_H(C_ℓ)`; moreover
`C^{⊥_H} ⊆ C` iff `C_ℓ^{⊥_H} ⊆ C_ℓ` for all `ℓ`.

*Proof.* `y ↦ y^q` fixes every `e_μ` (§1), so for `x = Σ_μ e_μ x_μ` and `c = Σ_μ e_μ c_μ` we get
`x c^q = Σ_μ e_μ x_μ c_μ^q` because `e_μ e_ν = 0` for `μ ≠ ν`. Summing over positions,
`⟨x,c⟩_H = Σ_μ e_μ ⟨x_μ, c_μ⟩_H`. A sum of orthogonal idempotent components vanishes iff each
vanishes, so `C^{⊥_H} = ⊕_μ e_μ C_μ^{⊥_H}`. Intersecting with `C = ⊕_μ e_μ C_μ` componentwise gives
the hull statement, and containment is componentwise. ∎

This reproduces the source's Theorems 8/10 in the special case `λ_1 = … = λ_e` and shows that the
hull dimension is **blind** to the Gray map: it is `ψ`-independent.

## 4. Distances — four theorems

Throughout this section `C ↔ (C_1,…,C_e)` and `d_k := d(C_k)`.

**Theorem 2 (two-sided bound).** For every admissible `M`,
```
min_k d_k  ≤  d(ψ(C))  ≤  e · min_k d_k.
```

*Proof.* Let `c ≠ 0` and `k` with `c_k ≠ 0`. Then `supp(c_k) ⊆ ∪_j supp(c_j)`, so
`u(c) ≥ |supp(c_k)| ≥ d_k ≥ min_j d_j`. With `u ≤ W` (§2) this gives `W(c) ≥ min_j d_j`, and the
lower bound follows by minimising over `c`. For the upper bound let `k₀` minimise `d_k` and take
`a ∈ C_{k₀}` of weight `d_{k₀}`; the codeword with `c_{k₀} = a` and `c_j = 0` for `j ≠ k₀` has
`u = d_{k₀}`, hence `W ≤ e·d_{k₀}`. ∎

Note the asymmetry: the lower bound is attained by *no* particular construction, while the upper
bound is exhibited by a **single-component** codeword. That asymmetry is exactly why the value in the
middle is not determined.

**Theorem 3 (single-component codes).** If `C_k = 0` for all `k ≠ k₀`, then
```
d(ψ(C)) = ρ_{k₀} · d(C_{k₀}),      ρ_{k₀} := #{ j : M[k₀][j] ≠ 0 }.
```
*Proof.* At a position `i` with `c_{k₀}(i) ≠ 0`, the symbol vector is `s_{k₀}(i) e_{k₀}`, whose image
under `M` is `s_{k₀}(i)·(M[k₀][·])`, nonzero exactly in the positions `j` with `M[k₀][j] ≠ 0`; there
are `ρ_{k₀}` of them. So `W = ρ_{k₀}·w(c_{k₀})` for every codeword, and minimising gives the claim. ∎

For `e = 2`, `M = [[1,1],[1,−1]]`, `ρ_1 = ρ_2 = 2`, so `d(ψ) = 2 d(C_1)` — verified 16/16 and 24/24
in §6.

**Theorem 4 (equal components).** If `C_1 = … = C_e = D` and `σ := #{ j : Σ_k M[k][j] ≠ 0 }`, then
```
d(ψ(C)) ≤ σ · d(D),        with equality whenever σ = 1.
```
*Proof.* Take the diagonal codeword `c` with `s_{1i} = … = s_{ei} = d_i` for a minimum-weight
`d ∈ D`. At each `i ∈ supp(d)` the image is `d_i·(col sums)`, whose weight is `σ`; so
`W(c) = σ·w(d) = σ·d(D)`, giving the bound. If `σ = 1` then Theorem 2's lower bound `d(ψ) ≥ d(D)`
closes the gap. ∎

For `e = 2`, `M = [[1,1],[1,−1]]`: column sums are `2` and `0`, so `σ = 1` (`char ≠ 2`) and
**`d(ψ(D×D)) = d(D)`** — verified 16/16 and 24/24. For `e = 3` over `F_4` with
`M = ((1,2,2),(2,1,2),(2,2,1))` (all entries nonzero, `M M^* = I_3`, found by exhaustive search),
the column sums are all `1`, so `σ = 3` and the theorem gives only `d(ψ) ≤ 3 d(D)`.

**Theorem 5 (non-determination).** Fix `(k_k, d_k)` for all `k` and fix `M`; `d(ψ(C))` is not
determined. Explicitly, over `F_9`, `n = 3`, `M = [[1,1],[1,−1]]`, the component data
`(k_1,d_1,k_2,d_2) = (1,3,1,3)` occurs for several pairs `(C_1,C_2)` with `d(ψ)` taking the values
**3, 4 and 5** — three distinct distances under identical constituent data, inside the bounds
`[3, 6]` of Theorem 2.

*Proof.* by exhaustive computation over all pairs (§6); the table of witnesses is reproducible from
`p3_ring_gray.py`. ∎ (A theorem of non-determination is necessarily established by explicit
witnesses; no general construction is claimed.)

## 5. The `e ≥ 3` sharper negative, and a corrected prediction

I initially expected Theorem 4 with `σ = 3` to be tight for the dense `F_4` matrix, i.e.
`d(ψ(D,D,D)) = 3 d(D)`. **The computation refutes this.** For all six field codes `D` over `F_4`,
`n = 2`, the true value is `d(ψ(D,D,D)) = d(D)`, i.e. the **lower** bound of Theorem 2 is attained,
while `σ·d(D) = 3 d(D)`.

Interpretation, and this is the substantive point: for `e ≥ 3` the diagonal codeword is **not**
optimal; a genuinely different tuple achieves the minimum. Thus

* no product formula `d(ψ) = f(d_1)·g(…)` can exist for `e ≥ 3`;
* the gap between the bounds of Theorem 2 can be as large as the factor `e`, and both extremes are
  realised (`C_2 = 0` attains `e·d`; equal components over `F_4` attain `d`).

This prediction was wrong and is recorded as wrong rather than deleted, in the same spirit as the
R3/R1/R2 audit trails.

## 6. Validation

All numbers below are exact (codeword enumeration, no bounds, no sampling).
Log: `p3_ring_gray_log.txt`.

| Check | Instance | Result |
|---|---|---|
| Theorem 2, lower and upper bound | `F_9, n=2`, all 256 ordered pairs | **0 violations** |
| Theorem 2 | `F_9, n=3`, all 576 ordered pairs | **0 violations** |
| Theorem 2, `e=3` | `F_4, n=2`, all 216 ordered triples, dense `M` | **0 violations** |
| Theorem 3, `C_2 = 0` | `F_9, n=2` (16 codes), `n=3` (24 codes) | **40/40 hold** |
| Theorem 4, `σ = 1` | `F_9, n=2` (16), `n=3` (24) | **40/40 hold** |
| Theorem 4, `σ = 3` (inequality only) | `F_4, n=2`, 6 codes | 6/6 satisfy `≤`; **0 tight** — see §5 |
| Theorem 5 (non-determination) | `F_9, n=2` / `n=3` | 1 and 4 groups respectively with >1 value |
| Degenerate `M` guard | `F_4, n=2`, `n=4` | `ν = 2 = 0`, `M` singular → **skipped, not silently passed** |

The `F_4` rows confirm the `e = 2` matrix limitation recorded in `R4_FEASIBILITY.md` §5.2: the
paper's `[[1,1],[1,−1]]` needs `ν = 2 ≠ 0`, so it excludes even characteristic. Nothing in Theorems
2–5 needs that matrix, only `ν ≠ 0`; the `e = 3` test used a different admissible `M` for exactly
that reason.

## 7. Reproducibility incident (recorded)

Three environment incidents occurred during P3-3. None changed a result; all are recorded because
the verdict rests on reproducibility.

**(7.1) `numpy` disappeared.** `p3_tables.py` originally imported `numpy` inside its distance
routine. On resuming, `numpy` was no longer present (it had worked earlier in the same session), so
the committed P3-1 numbers were, for a moment, not reproducible. The routine was rewritten in pure
stdlib and the whole table re-run: **every committed P3-1 figure is reproduced exactly** — C1 maxima
`3, 3, 1, 1, 3`; MDS counts `16, 16, 3, 6, 6`; self-orthogonal counts `4, 24, 3, 6, 9`; independence
verdicts 5/5, 11/11, 2/2, 3/4, 9/9. `p3_tables_log.txt` was regenerated from the stdlib version. The
dependency is gone and no result changed.

**(7.2) The local git repository was reset to the branch base.** On resuming, the local `.git` was a
fresh clone at `33aeb79` (the branch base) and `research_project/` appeared as untracked, while the
working files were intact. The remote still held every commit
(`refs/heads/arena/831a2e65-galios-hull = 148c6dc`), so the branch pointer was restored with
`git fetch` + `git reset --mixed FETCH_HEAD`. **No commit was lost, rewritten or reordered**, and the
working tree was not modified by the recovery. Verified afterwards: the source PDF is
612 826 B with sha256 `7f7e6803…` — identical to the Phase 0 record — and all Phase 0–3 deliverables
are present.

**(7.3) `pypdf` is gone, so `tools/preflight.py` can no longer run.** It now stops with
`ModuleNotFoundError: No module named 'pypdf'`, which is an environment regression, **not** a
missing or broken artifact. The check it performs on the source was substituted directly:
`sha256sum` of the source PDF equals `7f7e6803dffe8d42912c506cc0b6d8910187be169e14c869f3275d896c27d249`
and the size equals 612 826 B, both matching the Phase 0 verification log. Nothing was installed or
modified to work around this; the blocker is recorded instead.

## 8. Novelty test — decisive

| Statement | Prior art | Assessment |
|---|---|---|
| Theorem 1 (hull additivity) | source Theorems 8/10; R3 | **known**; re-proved for completeness |
| Theorem 2 (`min d ≤ d(ψ) ≤ e·min d`) | Gray maps are classically isometries between a Lee-type weight on the ring and the Hamming weight on the image (the `Z_4` and `F_2+uF_2` cases are textbook); the support-counting argument here is the direct generalisation | **elementary, probably folklore.** I found no source stating it for `R_e` in exactly this form, but I also cannot claim it is new — B-1/B-2 are open |
| Theorem 3, 4 (exact values in degenerate cases) | follows in two lines from Theorem 2 | **trivial corollaries** |
| Theorem 5 / §5 (non-determination, `e ≥ 3`) | the phenomenon is implicitly present in every explicit Gray-map example; I found no source that states it as a negative result | **the substantive finding of P3-3**, but it is a *negative* statement |
| The `(hull, d)` distribution itself | mass-formula literature counts hull without distance and cannot be specialised to constacyclic families (`R4_FEASIBILITY.md` §6.1); constacyclic distance literature gives tables, not distributions | **survives**, but as a computational/distributional contribution |

**What would eliminate the proposed contribution?** Any of:

1. a published statement of the bounds of Theorem 2 for `R_e` (kills the bound as a result, not the
   distribution);
2. any accessible work computing a joint (hull, distance) distribution for a constacyclic family,
   over a field or a ring (kills the distribution outright);
3. the Debnath–Prakash body text (B-2) containing such a count.

None of these was found, but **none was excluded either** — all three depend on full-text access that
remains blocked.

## 9. Verdict

| Question | Answer |
|---|---|
| Does the Gray map produce a substantive theorem? | **Partially.** Four short theorems with complete proofs, all elementary. No closed form; §5 shows why none exists in the naive product sense. |
| Is the hull dimension affected by the Gray map? | **No** — Theorem 1 is `ψ`-independent. |
| Is the Gray distance determined by constituent data? | **No** — Theorem 5, with three distinct values under identical constituent data. |
| Does that make the quantum-parameter distribution non-product? | **Yes**, and this is the surviving R4 claim. |
| Novelty | **Not claimed.** The bounds are probably folklore; the non-determination is a negative result; the distributional statement is the defensible claim and depends on B-1/B-2. |

**Recommendation.**

* **GO** on the narrowed contribution: *the exact joint (Hermitian hull dimension, Gray distance)
  distribution of dual-containing `λ`-constacyclic codes over `R_e`, its non-product structure, and
  the resulting quantum-parameter distribution* — as a computational and distributional result, with
  Theorems 1–5 as its supporting analysis.
* **NO-GO** on presenting a "Gray-coupling structural theorem" as the headline: the base ring is a
  product of fields, the bounds are support-counting, and §5 is a negative result.

## 10. Limitations carried forward, explicitly labelled

| # | Item | Status |
|---|---|---|
| L-1 | Four middle distances of the two-orbit family (`d = 3, 3, 4, 3` at `n = 6, q = 3`) | **computed only**, no proof, no formula (`P3_2_TWO_ORBIT.md` §5) |
| L-2 | `n = 9` power-attainment conjecture `d(C_a) = min{w((x−1)^j) : j ≥ a}` | **conjecture**, 10/10 support; missing step named |
| L-3 | Choice of `M` | **open convention.** `M` is free subject to `MM^* = νI`; exact Gray distances depend on it (Theorem 4's `σ`), bounds do not. Every future statement must name `M`. |
| L-4 | Even characteristic | the paper's `e=2` matrix has `ν = 2 = 0`, hence singular; the construction needs another `M`. Confirmed again in §6. |
| L-5 | **B-1** publisher full texts (ScienceDirect, Springer, AIMS) | **open blocker**; no absence claim possible |
| L-6 | **B-2** Debnath–Prakash body text | **open blocker** |
| L-7 | Theorem 5 is proved by witnesses, not by a general construction | limitation of the *statement*, stated as such |

Nothing above is promoted to a theorem. No novelty is claimed while L-5/L-6 remain open.

## 11. Next decision required

The remaining Phase 3 work with real content is the **distribution over `R_e`**, not more field-level
analysis: enumerate dual-containing tuples, compute `d(ψ)` exactly for a fixed `M`, and record the
quantum-parameter distribution `[[en, 2K−en, ≥d]]`. That is a computation whose size is controlled by
`|C_1|·…·|C_e|`, and the interesting instances begin at `e = 3`.

Before that is worth doing, one question should be settled, because it changes the deliverable:

> **Is the intended claim the distribution (a computational result with tables), or a theorem?**
> On the evidence of P3-3, no theorem beyond Theorems 1–5 is available at this level of generality,
> and Theorems 1–5 are elementary. If the project needs a theorem, the only remaining route is to
> find a restricted family where `d(ψ)` *is* determined (Theorem 4's `σ = 1` case is the one known
> such family) and characterise it; if a distribution is acceptable, Phase 3 can proceed to tables.
