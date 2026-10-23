# Phase 3 / P3-2 — Structure of the two-orbit family (first results)

Setting throughout: `F = F_9`, `n = 6`, `α = 1`, so `x^6 − 1 = (x−1)³(x+1)³`, and

```
R = F[x]/(x^6 − 1),      C(a,b) = ⟨ (x−1)^a (x+1)^b ⟩ ⊂ R,      dim C(a,b) = 6 − a − b,
(a,b) ∈ {0,1,2,3}²  →  16 distinct codes.
```

Distances are the exact values computed in `P3_1_TABLES.md` / `r4_field_joint.py`. Everything below
is proved from that definition; nothing relies on the table except where it says so.

## 1. Lemma 1 — the whole family has no word of weight 1

**Claim.** For every `(a,b) ≠ (0,0)`, `d(C(a,b)) ≥ 2`.

*Proof.* Evaluation at `1` is a ring homomorphism `ev₁ : R → F`, well defined because `x^6 − 1`
vanishes at `1`. Every `f ∈ C(a,b)` is divisible by `(x−1)` when `a ≥ 1`, hence `f(1) = 0`. A word
of weight 1 is the residue class of `c x^i` with `c ≠ 0`, and `ev₁(c x^i) = c ≠ 0`. So no word of
weight 1 exists when `a ≥ 1`. If `a = 0` then `b ≥ 1`, and the same argument runs at `−1`, using
`ev₋₁(c x^i) = c(−1)^i ≠ 0`. ∎

This is a statement about the **whole** family, not one instance: the lowest possible distance is
attained only by the trivial code `(0,0)`.

## 2. Lemma 2 — the single-orbit codes have distance exactly 2

**Claim.** For `1 ≤ a ≤ 3`, `d(C(a,0)) = 2`; for `1 ≤ b ≤ 3`, `d(C(0,b)) = 2`.

*Proof.* `≥ 2` is Lemma 1. For the upper bound: `(x−1)³ = x³ − 1` because `3 = 0` in `F`, and
`(x−1)^a ∣ (x−1)³` for `a ≤ 3`, so `x³ − 1 ∈ C(a,0)` and has weight 2. Symmetrically
`(x+1)^3 = x³ + 1 ∈ C(0,b)`, also of weight 2. ∎

(Both expansions were checked by machine: `(x−1)³ ↦ [2,0,0,1]`, `(x+1)³ ↦ [1,0,0,1]`, both of
weight 2 in the coefficient encoding used by the probes.)

## 3. Lemma 3 — the two MDS corners, proved

**Claim.** `d(C(2,3)) = d(C(3,2)) = 6`, so both are `[6,1,6]` MDS codes.

*Proof.* For `(2,3)` and `(3,2)` we have `a + b = 5`, so `dim = 1` and `C = {c·g : c ∈ F}`. Weight is
invariant under `c ≠ 0`, so `d = w(g)`. Now in characteristic 3, `(x−1)² = x² − 2x + 1 = x² + x + 1`
(the `−2` is `+1`), so

```
(x−1)²(x+1)³ = (x² + x + 1)(x³ + 1) = 1 + x + x² + x³ + x⁴ + x⁵,        w = 6,
(x+1)²(x−1)³ = (x² − x + 1)(x³ − 1) = 2 + x + 2x² + x³ + 2x⁴ + x⁵,     w = 6.
```

Both have all six coefficients nonzero, so `d = 6 = n − dim + 1`: Singleton is met. ∎

(Machine-checked: the two polynomials come out as `[1,1,1,1,1,1]` and `[2,1,2,1,2,1]`.)

## 4. Lemma 4 — one middle case

**Claim.** `d(C(1,1)) = 2`.

*Proof.* `≥ 2` by Lemma 1. `C(1,1) = ⟨x² − 1⟩`, and `(x² − 1)(x² + 1) = x⁴ − 1`, which has weight 2
and lies in the code. ∎

## 5. What is proved, and what is not

| `(a,b)` | `d` | status |
|---|---|---|
| `(0,0)` | 1 | trivial (whole ring) |
| `(a,0)`, `(0,b)`, `a,b ≥ 1` | 2 | **Lemma 2** |
| `(1,1)` | 2 | **Lemma 4** |
| `(2,3)`, `(3,2)` | 6 | **Lemma 3** (MDS) |
| `(1,2)`, `(2,1)` | 3 | computed only |
| `(1,3)`, `(3,1)` | 4 | computed only |
| `(2,2)` | 3 | computed only |

**Not proved, and no formula claimed:** the four middle values. An attempt to read a formula off the
table fails — `d` is not a function of `a + b` (on `a + b = 3`, `d = 2` for `(0,3),(3,0)` but `3` for
`(1,2),(2,1)`), nor of `min(a,b)`, nor of `max(a,b)`. The honest description is that `C(a,b)` is a
**two-point multiplicity code** — polynomials of degree `< 6` with prescribed multiplicities at `1`
and `−1` — and its minimum distance is a multiplicity-code minimum-distance question for which no
short closed form is visible at this size.

**The Singleton bound** `d ≤ a + b + 1` holds for all 15 non-zero codes (table), with equality
exactly for the five codes `(0,0)`, `(0,1)`, `(1,0)`, `(2,3)`, `(3,2)`. Lemmas 2–3 prove equality in
four of those five cases; that no other code attains it is a table computation, not a proof.

## 6. Consequence for Phase 3

The family is not uniform: it contains MDS members and members with `d = 2` at the same dimension
(e.g. `dim 4` at `(0,2)` with `d = 2` and at `(1,1)` with `d = 2`; `dim 3` at `(0,3)` with `d = 2`
and at `(1,2)` with `d = 3`). So any Phase 3 theorem must be about the **distribution**, which is
what the tables compute, and cannot be a formula for individual codes. That is consistent with the
one structural fact the tables did establish: the joint law is not a function of its marginals.

Next in P3-2 is the same analysis at `n = 9` (`x^9 − 1 = (x−1)^9`, a single orbit of multiplicity 9),
where the family is one-dimensional in `a` and a complete formula may exist. P3-3 (the ring-level
Gray coupling) remains the actual R4 question and is not started.

## 7. The single-orbit case `n = 9` is complete

`x^9 − 1 = (x−1)^9` over `F_9` (characteristic 3), so the family is one-dimensional:
`C_a = ⟨(x−1)^a⟩`, `a = 0..9`, `dim = 9 − a`. Computed exactly (`p3_tables.dist_of_span`,
weights 1–3 by membership then full enumeration where affordable):

| `a` | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| `dim` | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| `hull` | 0 | 1 | 2 | 3 | 4 | 4 | 3 | 2 | 1 | 0 |
| `d` | 1 | 2 | 2 | 2 | 3 | 3 | 3 | 6 | 9 | – |

Two facts stand out.

**(7.1) The hull dimensions are `min(a, 9−a)`** for all ten codes — a complete confirmation of the
single-factor case of the source's Theorem 8 formula on a multiplicity-9 instance, computed
independently by the kernel method.

**(7.2) The distance is attained by a power of `(x−1)`.** In characteristic 3,

```
(x−1)^3 = x^3 − 1              (weight 2)
(x−1)^6 = (x−1)^6 = x^6 + x^3 + 1   (weight 3)
(x−1)^7 = weight 6,  (x−1)^8 = weight 9,
```

and `(x−1)^j ∈ C_a` exactly when `j ≥ a`. The table is exactly reproduced by

```
d(C_a) = min { w((x−1)^j) : a ≤ j ≤ 9 },        with (x−1)^9 = 0 in R,
```

for all **10** values of `a`. Note that `(x−1)^9 = x^9 − 1 ≡ 0` in `R`, which is why large `a` does
*not* collapse to distance 2 — the naive reading of `(x−1)^9 = x^9 − 1` as a weight-2 word is exactly
the mistake the quotient ring prevents, and it is worth recording because it is a natural error.

**Status: conjecture, supported 10/10, not proved.** The missing step is that the minimum of
`w(g·h)` over `deg h < k` is attained at a monomial `h = (x−1)^j`; that is plausible for a
single-orbit code but is not evident, and no proof is claimed here.

## 8. Summary of P3-2

| Result | Status |
|---|---|
| Lemma 1: no weight-1 word for any `(a,b) ≠ (0,0)` | **proved** |
| Lemma 2: single-orbit codes over `n = 6` have `d = 2` | **proved** |
| Lemma 3: `[6,1,6]` MDS corners, `d = 6` | **proved** |
| Lemma 4: `d(C(1,1)) = 2` | **proved** |
| Four middle values of the `n = 6` family (`d = 3,3,4,3`) | computed only |
| `n = 9` complete table, hull `= min(a,9−a)` | computed, all 10 values |
| `d(C_a) = min{w((x−1)^j) : j ≥ a}` at `n = 9` | **conjecture**, 10/10 |
| Closed form for the two-orbit `n = 6` family | not found, and §5 explains why none is expected |

No novelty claim. The next Phase 3 item is P3-3, the ring-level `R_e` Gray coupling, which is the
actual R4 question; the field-level picture is now documented well enough to support it.
