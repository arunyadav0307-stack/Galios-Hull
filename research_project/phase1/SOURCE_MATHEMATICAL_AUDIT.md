# SOURCE MATHEMATICAL AUDIT

**Source:** Yadav, Singh, Islam, Prakash, Solé (2024), DOI `10.1007/s40314-024-02789-1`.
**Version examined: `hal-04825601v1`** (HAL author deposit, 23 pp., SHA-256 `7f7e6803…c27d249`). All `p.N` are physical PDF pages; printed page = N − 1.
**Scope:** blueprint §1B checklist, items 1–9. Nothing here is a correction of the paper's results; items that need a qualification are stated as qualifications and the executed computations are named.

**Verdict vocabulary:** `CONFIRMED` · `CONFIRMED WITH CORRECTION` · `UNVERIFIED` · `CONTRADICTED` · `NOT APPLICABLE`.

**Reproduction commands**

```bash
python3 research_project/code/phase1_examples.py    # Examples 1-3 + Gray matrices -> 31/31 checks
python3 research_project/code/phase1_tables.py      # Tables 1-3              -> 33/33 rows
python3 research_project/code/phase1_audit.py       # items 1-4, 6, 7 below   -> 11 audit items
```
Logs: `research_project/phase1/raw/{examples_log,audit_log}.txt`, `…/tables_recalc.json`.

---

## Item 1 — Ring decomposition and its hypotheses

**What the paper claims (p.4, p.6).** For `R₂ = F_{q²} + uF_{q²}`, `u² = 1`, with `γ ∈ F_{q²}` chosen so `2γ ≡ 1 (mod p)`, one has `R₂ ≅ ε₁F_{q²} ⊕ ε₂F_{q²}`, `ε₁ = γ(1+u)`, `ε₂ = γ(1−u)`. For `R_e`, `u^e = 1`, `e | q+1`, `R_e ≅ ⊕_{i=1}^{e} η_i F_{q²}` with `η_i = (u^e−1)/(u−μ^{i−1})`, `μ` a primitive `e`-th root of unity.

**Verdict: `CONFIRMED`.**

* The hypothesis `e | q+1` is exactly what is needed: `p ∤ q+1` because `q+1 ≡ 1 (mod p)`, hence `p ∤ e`, hence `u^e − 1` is separable and splits over `F_{q²}` (all `e`-th roots of unity already lie in `F_{q²}*`, a cyclic group of order `q²−1` divisible by `e` when `e | q+1 | q²−1`). Verified numerically: `x^e − 1` splits into exactly `e` linear factors over `GF(q²)` for `(p,e) ∈ {(5,2),(7,2),(13,2),(5,3),(11,3)}`.
* The idempotents were rebuilt by Lagrange interpolation and satisfy `e_i² = e_i`, `e_i e_j = 0` (`i ≠ j`), `Σ e_i = 1` in every case tested. The paper's `ε₁, ε₂` satisfy the same three identities (checked directly for `p = 5, 7, 13`).
* The decomposition is what makes `C = ε₁C₁ ⊕ ε₂C₂` a legitimate encoding of a code over `R₂`, and it is used in every construction verified in this phase.

**Hypotheses the paper states that matter.** `q` odd (`p` odd prime, p.4); `e | q+1`; `λ = Σ η_l α_l ∈ R*_e` (i.e. every `α_l ≠ 0`). The parenthetical "(q can also be even depending upon e)" (p.4) is not used anywhere in the paper's computations and is not needed by anything verified here; it is recorded in the glossary as an unused latitude.

---

## Item 2 — The idempotents `η_l` and their properties

**Verdict: `CONFIRMED WITH CORRECTION` (a normalisation omission, no effect on results).**

The printed definition `η_i = (u^e−1)/(u−μ^{i−1})` (p.4) and the printed polynomials of Example 3,

```
η1 = (u + 4)(u + t20),  η2 = (u + t4)(u + t20),  η3 = (u + t4)(u + 4)      (p.17)
```

are the **quotients**, not the idempotents. Computed in `R₃ = GF(25)[u]/(u³−1)`:

* each `η_i` does satisfy `η_i² = λ_i η_i` for a **nonzero** scalar `λ_i` (`8`, `3`, `24` for `i = 1,2,3` respectively) and `η_i η_j ≡ 0`;
* but `η₁ + η₂ + η₃ ≡ 3u² ≢ 1`.

After the obvious rescaling `e_i = η_i/λ_i`, the three polynomials are orthogonal idempotents summing to `1` (verified), i.e. they are exactly the CRT idempotents of `⊕³ F_{q²}`, in a permuted order.

**Why this has no effect on any result.** Every use of `η_i` in the paper is of the form `η_i C_i` with `C_i` an `F_{q²}`-linear code. If `η_i = λ_i e_i` with `λ_i ∈ F*_{q²}`, then `η_i C_i = e_i C_i` by field-linearity, so the direct-sum decompositions, the hull formulas and the tables are unchanged. The same does **not** apply to `R₂`, where the paper does normalise: `ε₁ = γ(1+u)` with `2γ ≡ 1` is a genuine idempotent (verified).

**Assessment:** notational, not mathematical. It does not justify any change to a reported number, and none was made.

---

## Item 3 — Generator-polynomial structure, factorisation of `x^n − α`, multiplicities, CR pairs

**What the paper claims (p.8–9).** With `π(j, q²) = 0` iff `j | (q^{2k}+q)` for some `k ≥ 0`, and `Ω, Ω'` the divisors `j | n'r` with `gcd(n'r/j, r) = 1`, split by `π`,

```
x^n − α = Π_{j∈Ω} Π_{i=1}^{γ(j)} g_ij^{p^v} · Π_{j∈Ω'} Π_{i=1}^{β(j)} (f_ij f_ij^†)^{p^v},
γ(j) = φ(j)/(φ(r)·ord_j(q²)),   β(j) = φ(j)/(2φ(r)·ord_j(q²)),
```

`g_ij` self-conjugate-reciprocal of degree `ord_j(q²)`, `f_ij, f_ij^†` CR pairs of that degree, and the degree identity `n = Σ_Ω ord_j γ(j) p^v + Σ_{Ω'} 2 ord_j β(j) p^v`.

> **Extraction caveat.** The corpus renders the two fractions as `γ(j) := ϕ(j)ϕ(r)ordj(q2)` and `β(j) := ϕ(j)2ϕ(r)ordj(q2)` (p.9) because the fraction bars are lost. The quotient reading above is the only one consistent with the paper's own totals and with the degree identity; it is used throughout and reproduces every stated count.

**Verdict: `CONFIRMED`.**

| Example | `Ω` computed | `Ω'` computed | `Σγ` | `Σβ` | degree identity | paper |
|---|---|---|---|---|---|---|
| Ex. 1 (`n=12, r=1, q²=25`) | {1,2,3,6} | {4,12} | 6 | 3 | 12 = 12 ✓ | Ω={1,2,3,6}, Ω'={4,12}, γ=(1,1,2,2), β=(1,2) |
| Ex. 2 (`n=14, r=2, q²=169`) | ∅ | {4,28} | 0 | 7 | 14 = 14 ✓ | Ω=∅, Ω'={4,28}, β=(1,6) |
| Ex. 3 (`n=6, r=2, q²=25`) | ∅ | {4,12} | 0 | 3 | 6 = 6 ✓ | Ω=∅, Ω'={4,12}, β=(1,2) |

Additionally, the paper's twelve printed factors of `x¹²−1` (p.15), fourteen of `x¹⁴−12` (p.16) and six of `x⁶−4` (p.16) were multiplied out in `GF(25)`, `GF(169)`, `GF(25)` respectively; each product equals the stated polynomial **exactly**, and each printed CR pairing was checked with the paper's own definition `p^†(x) = a₀^{−q} Σ a_i^q x^{s−i}` (p.4) — all 6 self-CR factors, all 3 pairs (Ex. 1), all 7 pairs (Ex. 2), all 3 pairs (Ex. 3) confirmed, and `(p^†)^† = p` verified on all 24 linear factors of `x¹²−1`.

The three explicit generators were also confirmed as products of the printed factors: `x³+x²+t⁸x+t⁸ = (x+1)(x+t¹⁰)(x+t²²)`, `x²+t²¹x+1 = (x+t¹⁸)(x+t¹⁵⁰)`, `x²+tx+t⁸ = (x+t²)(x+2)`.

*Reading note.* The paper writes factors as `(x + c)`; the root is `−c`. My first pass expanded them as `(x − c)` and produced spurious mismatches; the convention is fixed in the code (`const()` in `phase1_examples.py`) and every identity above is with the `(x + c)` reading.

---

## Item 4 — Hull-dimension formula, re-derived

**What the paper claims (Theorem 8, p.10–11; Corollary 9, p.12).** For `C = ε₁C₁ ⊕ ε₂C₂` with `λ = ε₁α + ε₂α`,

```
dim Hull_H(C) ∈ { Σ_{j∈Ω} ord_j(q²) a_j + Σ_{j∈Ω'} ord_j(q²) b_j }
0 ≤ a_j ≤ 2γ(j)⌊p^v/2⌋,  0 ≤ b_j ≤ 2β(j)p^v,
```

and when `gcd(n,p) = 1` the `Ω` term vanishes and `0 ≤ b_j ≤ 2β(j)`.

**Verdict: `CONFIRMED`.**

* The paper's route is the standard one: `Hull_H(C_i) = ⟨lcm(g_i, ((x^n−α)/g_i)^†)⟩` (p.5, citing [34, Thm 1]), so `dim = n − deg lcm`. I re-derived the same quantity **independently of the paper's bookkeeping**, from the definition: `C^{⊥H} = {y : Σ_j c_j y_j^q = 0}` computed as the Frobenius image of the Euclidean dual, then `dim(C ∩ C^{⊥H}) = dim C + dim C^{⊥H} − dim(C + C^{⊥H})` by rank.
* The two agree on **220 randomly sampled divisors** of `x¹²−1` over `GF(25)` (all values `0,1,2,3` represented).
* **Exhaustive** check over all **4096** monic divisors of `x¹²−1`: the attained hull dimensions are exactly `{0,1,2,3}`, and the Corollary-9 bound is `Σ_{j∈Ω'} ord_j(q²)β(j) = β(4) + β(12) = 1 + 2 = 3`. The range `0…3` is therefore both respected and attained.
* The `R₂` bound `2·3 = 6` is attained: with `g* = x³ + 11x² + 24x + 2` (hull 3, found by the exhaustive scan) taken as both constituents, `hull(ψ(C)) = 6` by direct linear algebra on `ψ(C)`.

**Hypothesis that is easy to miss.** Theorem 8 requires `λ = ε₁α + ε₂α` with the **same** `α` in both components; Theorem 15 (dual-containing) allows `λ = ε₁α₁ + ε₂α₂` with `α₁ ≠ α₂`. Both are respected in the codes verified (Table 1 row 2 has `λ = ε₁ + 6ε₂` and is a Theorem-15-type object only, not a Theorem-8 instance).

---

## Item 5 — The Hermitian LCD criterion: necessary, sufficient, or both?

**What the paper claims (Theorem 11, Corollary 12, p.13; `R_e` versions Theorem 13, Corollary 14).** With `gcd(n,p) = 1`, `α` of order `r`, and `S_{q²} = {j ≥ 1 : j | (q^{2k}+q) for some k ≥ 0}`: `D_{q²}(n) = {0} ⟺ n·r ∈ S_{q²}`.

**Verdict: `CONFIRMED` — it is an iff, but it is a statement about the *set* of hull dimensions, not about an individual code.**

* The proof of the forward direction ("`nr ∈ S_{q²}` ⟹ `Ω' = ∅` ⟹ `a_j = 0` ⟹ only hull dimension 0") is valid as written (p.13), given `π(j,q²)=0` for all `j | n·r` when `n·r | q^{2k}+q`.
* The converse is argued by exhibiting `n·r ∈ Ω'` with `0 < β(n·r)`, hence a nonzero `b_{nr}` — again valid.
* Independent test on four `(n, r)` pairs over `GF(25)`, computing the set of hull dimensions over sampled monic divisors:

| `n` | `r` | `n·r` | `n·r ∈ S_{25}` | hull dimensions attained | `D = {0}`? | iff holds |
|---|---|---|---|---|---|---|
| 6 | 1 | 6 | yes (`6 ∣ 25⁰+5`) | {0} | yes | ✓ |
| 12 | 1 | 12 | no | {0,1,2,3} | no | ✓ |
| 14 | 2 | 28 | no | {0,1,3,4,6,7} | no | ✓ |
| 6 | 2 | 12 | no | {0,1,2,3} | no | ✓ |

*Reading note on `nr`.* The string `nr` in Theorem 11/Corollary 12/13/14 is printed without a multiplication sign; the correct reading is the product `n·r`, as the proof's "for each divisor of `nr`" and the factorisation's divisor set `j | n'r` show. Under the quotient reading `n/r` the numerical tests above fail (`n/r = 12` for the first row would put `12 ∉ S`, contradicting `D = {0}`), so the product reading is not merely plausible but the only consistent one. Recorded in the glossary.

---

## Item 6 — Dual-containing conditions

**What the paper claims (Theorem 15, p.13–14; Theorem 16, p.14).** `C^{⊥H} ⊆ C` iff, for every `j ∈ Ω_i` and every `i`, `0 ≤ a_ij ≤ ⌊p^v/2⌋`, and for every `j ∈ Ω'_i` and every `i`, `0 ≤ b_ij + c_ij ≤ p^v` (and likewise `u_ij`, `v_ij + w_ij` for the second component).

**Verdict: `CONFIRMED`.**

* The proof (p.14) reduces `C^{⊥H} ⊆ C` to `Hull_H(C_i) = C_i^{⊥H}`, i.e. `lcm(g_i, ((x^n−α_i)/g_i)^†) = ((x^n−α_i)/g_i)^†`, i.e. `g_i | ((x^n−α_i)/g_i)^†`. Exponent-wise this is `a_ij ≤ p^v − a_ij` (self-CR factor) and `b_ij ≤ p^v − c_ij` (pair factor), which is exactly the stated condition. Valid.
* Tested both ways at Example 2's parameters (`n=14, α=12, GF(169)`):
  * `g = f·f^†` (both members of one CR pair, so `b+c = 2 > p^v = 1`): **not** dual-containing ✓ (as predicted);
  * `g₁ = (x+t¹⁸)(x+t¹⁵⁰)` (one member from each of two different pairs): dual-containing ✓.
* All **14 Table-3 rows** and all three examples' constituents were independently confirmed dual-containing by direct computation (`is_dual_containing_matrix`), i.e. the condition is not merely quoted but reproduced on every object the paper applies it to.

---

## Item 7 — The Gray map: well-definedness, injectivity, and what it does *and does not* preserve

**What the paper claims (p.6–8, Lemma 3, Lemma 4, Lemma 5, Theorem 6).** `ψ(r_0,…,r_{n−1}) = [(s₁₀,…,s_{e0})M, (s₁₁,…,s_{e1})M, …]` where `r_j = Σ_k η_k s_{kj}`; `M` square of order `e` with `M M* = νI_e`, `ν ∈ F*_{q²}`; `ψ` is a bijective linear map; `ψ(C^{⊥H}) = ψ(C)^{⊥H}`.

**Verdict: `CONFIRMED`, with one scope clarification.**

* **Well-defined and linear:** immediate from the CRT decomposition (Item 1); verified by construction in all computations.
* **Injective / dimension-preserving:** `dim ψ(C) = dim C₁ + dim C₂` verified on three constructions (Ex. 1 twice, Ex. 2). This is what makes `[en, k, d]` with `k = k₁ + k₂` legitimate.
* **`ν ≠ 0` is essential and holds:** `MM* = νI` verified for `M = [[1,1],[1,−1]]` (`ν = 2`), `M(5) = [[3,2,1],[3,4,3],[4,3,2]]` (`ν = 4`), `M(11) = [[7,4,2],[9,7,4],[4,2,4]]` (`ν = 3`). Without `ν ≠ 0` the proof of Lemma 3 collapses. Note `p ∈ {3,5,7,11,13}` in the paper, so `ν = 2, 3, 4` are all nonzero — but `ν` could vanish in characteristic 2 or 3 in other configurations; the paper's own tables stay clear of it.
* **`ψ(C^{⊥H}) = ψ(C)^{⊥H}`** verified numerically on three constructions.
* **Hull transport:** `hull(ψ(C)) = hull(C₁) + hull(C₂)` verified on the same three constructions — i.e. Theorem 6's conclusion in the form the tables use.
* **Scope clarification (important for the blueprint's rule).** What Lemma 3 shows is that `ψ` preserves the **Hermitian inner product up to the scalar `ν`**. It says nothing about Hamming/Gray distance: the Gray distance is *defined* as `d_G(C) = d_H(ψ(C))` (p.8), so the distance of `ψ(C)` is an object to be computed, not transported. Phase 1 therefore computed **every** distance in Tables 1–3 and in the examples **exactly** (minimum weight via exhaustive dependent-column search on the parity-check matrix, weights 1–3 exhaustive, weight 4 by exhaustive search where the co-dimension allows and by explicit witness otherwise), and did not infer any distance from the constituent codes.

---

## Item 8 — Unclear or unverified arguments (explicit list)

1. **No proof given for Theorem 2** (p.6) — asserted with "can be obtained by the next theorem". The claim is standard; verified operationally in all 33 table rows (`g_i | x^n − α_i`).
2. **Theorem 6's proof is a pointer** — "It can be proved by following the steps of Theorem 6.2 in [32]" (p.8). The conclusion was verified operationally instead (Item 7).
3. **Theorems 10, 13 and Corollary 14 have no proof** ("general case", "Similarly, we can obtain…"). Marked `QUOTED` in the register. Nothing in Phase 1 depends on them.
4. **Idempotent normalisation** (Item 2) — printed `η_i` are not idempotents. Qualified, not corrected.
5. **`nr` in Theorem 11/13/Cor 12/14** — no multiplication sign; product reading established by consistency (Item 5).
6. **The `T able` captions** (pp.17–19) — typographic artefact of the source itself, not of the extraction; the captions are otherwise complete.
7. **Comparison column of Table 3** ("New", "Optimal [11]", "[[52,43,≥3]]₃ [11]", …) — these are literature claims against references [3], [11], [14]. They are **`UNVERIFIED` and out of Phase-1 scope**: verifying them requires the cited works, which is Phase 2 material. They were not used and not adjusted.
8. **"Magma Computational software [5]"** (p.15) — the paper's numbers were produced by Magma, which is unavailable here (`preflight` WARN). Every number was therefore recomputed with independent Python code (`galois`), which is the stronger check.
9. **`ord_j(q²) = 1 ∀j ∈ Ω ∪ Ω'`** in all three examples (pp.15,16) — an assertion about those specific `j`; confirmed numerically in every case.

---

## Item 9 — Internal conflicts between statements

| # | Conflict | Resolution | Impact |
|---|---|---|---|
| 1 | §2 defines `η_i = (u^e−1)/(u−μ^{i−1})` and calls these the CRT idempotents; but `Σ η_i = 3u² ≠ 1` for `e = 3` | The `η_i` are the quotients; the idempotents are `η_i/λ_i`. Confirmed numerically (Item 2) | None on any reported parameter (scalar absorbed) |
| 2 | Theorem 8 bounds `a_j ≤ 2γ(j)⌊p^v/2⌋`, `b_j ≤ 2β(j)p^v`; Theorem 10 bounds `a(l)_j ≤ γ_l(j)⌊p^v/2⌋`, `b(l)_j ≤ β_l(j)p^v` | Not a conflict: Theorem 8's `a_j, b_j` are already summed over the two `R₂` components, Theorem 10's are per component | None |
| 3 | Example 3 writes "`C₃ = ⟨g₂(x)⟩`" although `g₃(x) = x+t¹⁰` was just defined and the sum `4+5+5 = 14` uses `g₃` | Evident typographical slip for `⟨g₃(x)⟩`; the recomputation with `g₃` reproduces the paper's `[18,14,4]` and `[[18,10,≥4]]` exactly | None (verified with `g₃`) |
| 4 | Lemma 3's proof writes `⟨ψ(c),ψ(x)⟩_H = Σ (r₁ᵢ,…)MM*(s₁ᵢ^q,…)^T` and then replaces `MM*` by `νI` | Valid only because `M*` is the conjugate transpose and `ν ∈ F*`; `ν ≠ 0` must be an explicit hypothesis (it is stated on p.7) | None for the parameters used (`ν = 2,4,3`) |
| 5 | Theorem 8 requires `λ = ε₁α + ε₂α` (equal `α`), Theorem 15 allows `λ = ε₁α₁ + ε₂α₂` | Deliberate difference, both used correctly in the tables (Table 1 rows 2–4, 7 have `α₁ ≠ α₂` and are not Theorem-8 instances) | None |

**No `SUSPECT` flag is raised against any numbered statement**: every statement whose content Phase 1 could compute was reproduced, and the two textual defects found (idempotent normalisation, `C₃` generator name) are typographical/notational with zero effect on any reported parameter.

---

## Summary table

| # | Item | Verdict |
|---|---|---|
| 1 | ring decomposition + hypotheses | `CONFIRMED` |
| 2 | idempotents `η_l` | `CONFIRMED WITH CORRECTION` (normalisation, no effect) |
| 3 | generator polynomial / factorisation / CR pairs | `CONFIRMED` |
| 4 | hull-dimension formula | `CONFIRMED` |
| 5 | Hermitian LCD criterion (iff) | `CONFIRMED` |
| 6 | dual-containing conditions (iff) | `CONFIRMED` |
| 7 | Gray map: well-defined, injective, inner-product preserving; distance *computed* not assumed | `CONFIRMED` |
| 8 | unclear / unverified arguments | 9 items listed, all `QUOTED`/`UNVERIFIED` and none load-bearing for Phase 1 |
| 9 | internal conflicts | 5 recorded, none affecting a reported parameter |
