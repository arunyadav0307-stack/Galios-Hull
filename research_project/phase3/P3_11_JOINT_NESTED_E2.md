# P3-11 — The exact joint `(Hermitian hull dimension, distance)` law for the nested `e = 2` family

Date: 2026-10-25. Probe: `phase3/p3_joint_nested_e2.py`. Log: `phase3/p3_joint_nested_e2_log.txt`
(112 lines, exit 0, 428 s). Pure stdlib, ASCII.

Status: **an exact computed distribution, not a theorem.** Every number in this document is a count
produced by exhaustive enumeration; none is estimated, sampled or bounded. This is the object R4 asks
for, obtained on the one sub-family where both coordinates are *determined*.

---

## 1. Why this family is the one that can be computed exactly

R4 needs the joint distribution of `(dim Hull_H, d)` over `R_e = F_q[u]/(u^e−1)` together with its
Gray image. In general the second coordinate is **not determined** by the component invariants:
P3-3 Theorem 5 exhibits a witness with `d(ψ) ∈ {3,4,5}` for fixed `(k_ℓ, d_ℓ)`.

But for `e = 2` with **nested** components both coordinates are exact and proved:

| Coordinate | Statement | Status |
|---|---|---|
| distance | `d(ψ(C₁×C₂)) = min{2·d(C₁), d(C₂)}` for `C₂ ⊆ C₁` | **P3-10**, proved (classical `|u|u+v|`) |
| hull | `dim Hull_H(ψ(C)) = Σ_ℓ dim Hull_H(C_ℓ)` | **P3-3 Thm 1**, proved; re-verified 256/256 |

So on this family the joint law is a finite computation with no bound and no sampling. That is what
was done.

## 2. Setting and method

* `F_9 = F_3[t]/(t²+1)`, elements `a + bt ↦ a + 3b`. Hermitian conjugation is the Frobenius `x ↦ x³`;
  on `a + bt` it sends `(a,b) ↦ (a,−b)` because `t³ = −t`. The script **asserts** `conj(x) == x³` for all
  nine elements before doing anything else.
* `R_2 = F_9[u]/(u²−1) ≅ F_9 × F_9` via the roots `1, −1`. These exist in every odd characteristic, so
  no splitting hypothesis is needed for the ring decomposition.
* `λ = (1,1)`, so both components are ordinary **cyclic** codes of length `n`. Every pair
  `C₂ ⊆ C₁` of cyclic codes is therefore realisable, and the enumeration over pairs is complete.
* `gcd(n,3) = 1`, so `xⁿ − 1` is separable and the cyclic codes are exactly the ideals `⟨g⟩`, `g | xⁿ−1`.
* `dim Hull_H(C) = k − rank(G·conj(G)ᵀ)`, computed from the generator matrix.
* The Gray matrix is `M = ((1,1),(1,−1))`, i.e. `ψ(c₁,c₂) = (c₁+c₂, c₁−c₂)`.
* `n ∈ {2, 4, 5, 7, 8}`, i.e. `ψ`-lengths `4, 8, 10, 14, 16`.

**Independent cross-check.** For every one of the 3368 pairs the additive hull value
`h(C₁) + h(C₂)` was compared against the hull of `ψ(C₁×C₂)` computed **directly** from its own
generator matrix `[(u,u)] ∪ [(v,−v)]`. **3368 pairs, 0 failures.** Hull additivity is therefore
confirmed again, this time on a family where it feeds a published table rather than an internal check.

## 3. Results

### 3.1 Per-length joint distributions

`n = 2` (5 pairs):

| h | d | count |
|---|---|---|
| 0 | 1 | 1 |
| 0 | 2 | 4 |

`n = 4` (65 pairs):

| h | d | count |
|---|---|---|
| 0 | 1 | 1 |
| 0 | 2 | 24 |
| 0 | 3 | 12 |
| 0 | 4 | 28 |

`n = 5` (19 pairs):

| h | d | count |
|---|---|---|
| 0 | 1 | 1 |
| 0 | 2 | 3 |
| 0 | 5 | 1 |
| 2 | 2 | 4 |
| 2 | 4 | 2 |
| 2 | 5 | 2 |
| 4 | 3 | 2 |
| 4 | 4 | 4 |

`n = 7` (9 pairs):

| h | d | count |
|---|---|---|
| 0 | 4 | 2 |
| 0 | 5 | 4 |
| 0 | 7 | 3 |

`n = 8` (3270 pairs) — the substantive table:

| h \ d | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
| 0 | 10 | 20 | 176 | 0 | 68 | 0 | 52 |
| 1 | 4 | 8 | 340 | 24 | 208 | 48 | 180 |
| 2 | 4 | 16 | 316 | 48 | 264 | 208 | 232 |
| 3 | 0 | 0 | 96 | 144 | 264 | 176 | 104 |
| 4 | 0 | 10 | 36 | 104 | 116 | 0 | 0 |

All cells of the `n = 8` table are taken from the log, in which every `(h,d)` with a nonzero count is
printed.

## 4. The R4-relevant finding: the joint law is **not** a product

P3-1 recorded, on the *field-level* tables A/B/D/E/F, that the joint law of hull and distance is not
the product of its marginals (independence violations 5, 5, 11, 2, 3, 9). It was open whether that was
an artefact of the non-determined regime. **It is not.** In the fully-determined nested `e = 2` regime:

| `n` | pairs | total variation | max deviation | verdict |
|---|---|---|---|---|
| 2 | 5 | 0.0000 | 0.0000 | independent (vacuously — single `h` value) |
| 4 | 65 | 0.0000 | 0.0000 | independent (single `h` value: all `h = 0`) |
| 5 | 19 | **0.2078** | 2.1053 | **NOT independent** |
| 7 | 9 | 0.0000 | 0.0000 | independent (single `h` value: all `h = 0`) |
| 8 | 3270 | **0.1753** | 134.1651 | **NOT independent** |

Computed with exact rational arithmetic (`fractions.Fraction`), so "independent" is a genuine zero
test, not a rounding artefact. The lengths at which independence *does* hold are exactly those where
one marginal is degenerate (`h ≡ 0` at `n = 2, 4, 7`), so they carry no information about independence.

**Interpretation.** Hull dimension and distance remain dependent on the family even after the distance
is made a deterministic function of the components. A hull-dimension-only count — which is precisely
what B-2a and B-2b do — cannot reproduce this table. This is a difference in **kind**, and here it is
demonstrated by exact enumeration rather than argued.

## 5. What this is and is not

**Is:** the first exact joint `(hull, d)` distribution in this project computed without any bound
relying on the non-determined case; 3368 pairs; both coordinates from proved formulas; an independent
direct computation of the hull on every pair; and a clean negative answer to "is the joint law a
product?" on the one family where the question was testable.

**Is not:**

* **Not a theorem.** It is a finite enumeration. The general `e ≥ 2`, `C₂ ⊄ C₁` case is untouched and
  P3-3 Theorem 5 still governs it.
* **Not new mathematics.** The ingredients are P3-3 Thm 1 (hull additivity, essentially the componentwise
  structure of the source paper) and P3-10, which is the classical `|u|u+v|` distance formula. The
  *distribution* is new to this project but is a computation over classical facts, and whether it is
  new to the literature cannot be asserted while B-1, B-2a (+ its Correction), B-2b and Tian–Gao–Gao
  remain unread.
* **Not a Phase 9 argument.** A distribution table is not the "substantive proved theorem" the
  blueprint requires. **Phase 9 remains NO-GO.**
* **Not a claim that these parameters are good.** No comparison with code tables is made anywhere.

## 6. Reproducibility

```
python3 research_project/phase3/p3_joint_nested_e2.py > research_project/phase3/p3_joint_nested_e2_log.txt
```

112 lines, exit 0, 428 s, stdlib only, no network. The run ends with `Overall: PASS`, which asserts two
things only: the 3368 direct-hull cross-checks all matched the additive value, and the printed joint
counts sum to the number of pairs. It does not assert anything about the mathematics beyond §1.

Sanity assertions executed before any count: `conj(x) == x³` for all `x ∈ F_9`, and `x·conj(x) ≠ 0` for
`x ≠ 0` (so `conj` is a field automorphism, hence the Hermitian form is non-degenerate).

## 7. Bookkeeping

* Probe: `research_project/phase3/p3_joint_nested_e2.py`; log `p3_joint_nested_e2_log.txt`.
* Added to `tools/verify_logs.py` as a slow case (~430 s) so the table cannot drift.
* `PHASE_STATUS.md`: P3-11 section.
* `LINKS.md`: probe, log, document.
