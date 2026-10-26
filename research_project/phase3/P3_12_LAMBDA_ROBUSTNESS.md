# P3-12 — The non-product finding survives removing both restrictions of P3-11

Date: 2026-10-25. Probe: `phase3/p3_lambda_robust.py`. Log: `phase3/p3_lambda_robust_log.txt`
(log: in the verify_logs set, exit 0, 1.0 s). Pure stdlib, ASCII.

Status: **computed distribution tables plus one clean qualitative conclusion.** No theorem is claimed.
Every number is an exhaustive count.

---

## 1. The two restrictions left in P3-11, and why both can go

P3-11 computed the exact joint law of `(dim Hull_H(ψ(C)), d(ψ(C)))` for the nested `e = 2` family with
`λ = (1,1)` and found it is **not** the product of its marginals (TV = 0.2078 at `n = 5`, 0.1753 at
`n = 8`). Two hypotheses were still assumed:

| Restriction | Why it was there | How it is removed here |
|---|---|---|
| `λ = (1,1)` — both components **cyclic** | keeps both component rings equal | all four `λ ∈ {±1}²` of `R₂ = F₉ × F₉`: each component is `λ_ℓ`-constacyclic, i.e. **cyclic** (ideal of `F₉[x]/(xⁿ−1)`) or **negacyclic** (ideal of `F₉[x]/(xⁿ+1)`) |
| `C₂ ⊆ C₁` (**nested**) | makes P3-10's formula `min{2d₁,d₂}` applicable | drop the formula: for `e = 2`, `ψ(c₁,c₂) = (c₁+c₂, c₁−c₂)`, so `d(ψ)` is enumerated **directly** as `min over (c₁,c₂) ≠ (0,0)` of `w(c₁+c₂) + w(c₁−c₂)` |

The second point matters for correctness of framing: P3-10 needed nesting only to *recognise* the code
as `|u|u+v|`. The Gray image itself is defined for every pair, and its distance can simply be measured.

## 2. Feasibility, stated rather than hidden

Cost for "every pair" is `(Σ_ℓ Σ_g |C_g|)²` word-pairs, where the inner sum runs over the codes of one
component ring.

| `n` | Σ over codes of \|C\| | all-pairs cost | what is reported |
|---|---|---|---|
| 2 | 100 | 10⁴ | **all pairs**, all 4 `λ` |
| 3 | 820 | 6.7·10⁵ | **all pairs**, all 4 `λ` |
| 4 | 10 000 | 10⁸ — out of reach in pure Python | **nested only** (P3-10 formula), `λ = (1,1)` and `(−1,−1)` |

For **mixed** `λ` (one component cyclic, one negacyclic) at `n = 4` there is no nontrivial nesting at
all: `gcd(xⁿ−1, xⁿ+1)` divides 2, so `C₂ ⊆ C₁` forces `g₁ = 1` or `C₂ = 0`. That case is therefore
**skipped by reasoning, not by omission**, and is recorded as carrying no information.

## 3. The independence test, with a vacuity flag

Testing `P(h,d) = P(h)·P(d)` is **vacuous whenever one marginal is a point mass**: the product formula
then holds identically and says nothing. An earlier version of this run printed "independent" for such
rows, which overstates the evidence. The script now reports `h`-value and `d`-value counts and flags
degeneracy. This distinction turned out to be the whole story.

## 4. Results

| `n` | `λ` | pairs | mode | TV | `h` values | verdict |
|---|---|---|---|---|---|---|
| 2 | (+,+) | 15 | all | 0.0000 | 1 | independent — **VACUOUS** |
| 2 | (+,−) | 7 | all | 0.0000 | 1 | independent — **VACUOUS** |
| 2 | (−,+) | 7 | all | 0.0000 | 1 | independent — **VACUOUS** |
| 2 | (−,−) | 3 | all | 0.0000 | 1 | independent — **VACUOUS** |
| 3 | (+,+) | 15 | all | **0.2200** | 3 | **NOT independent** |
| 3 | (+,−) | 15 | all | **0.1689** | 2 | **NOT independent** |
| 3 | (−,+) | 15 | all | **0.1689** | 2 | **NOT independent** |
| 3 | (−,−) | 15 | all | 0.0000 | 1 | independent — **VACUOUS** |
| 4 | (+,+) | 65 | nested | 0.0000 | 1 | independent — **VACUOUS** |
| 4 | (−,−) | 1 | nested | 0.0000 | 1 | independent — **VACUOUS** |

**The conclusion, stated at the strength the data supports:** in the `e = 2` family over `F₉`, *every
case in which the independence test is not vacuous fails it.* There is no non-degenerate case in this
sweep where hull dimension and distance are independent.

Two consistency checks pass silently and are worth naming:

* `λ = (+,−)` and `λ = (−,+)` give **identical** TV (0.1689) and identical tables, as they must by the
  component-swap symmetry.
* Hull additivity `dim Hull_H(ψ(C)) = Σ_ℓ dim Hull_H(C_ℓ)` was re-verified by computing the hull
  **directly** on `ψ(C)` from its own generator matrix in **every** row: **0 failures** across all
  150 pairs enumerated.

### 4.1 The informative tables

`n = 3`, `λ = (+,+)`, all 15 pairs (both components cyclic):

| h \ d | 1 | 2 | 3 | 4 | 6 |
|---|---|---|---|---|---|
| 0 | 1 | 2 | 0 | 0 | 0 |
| 1 | 0 | 4 | 0 | 2 | 2 |
| 2 | 0 | 1 | 3 | 0 | 0 |

`n = 3`, `λ = (+,−)` (cyclic × negacyclic), all 15 pairs — identical to `λ = (−,+)`:

| h \ d | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| 0 | 1 | 4 | 0 | 1 | 0 | 1 |
| 1 | 0 | 2 | 3 | 1 | 1 | 1 |

The dependence is visible by inspection and is not marginal-driven: with `h = 0` the distances are
concentrated at `2`, while `h ≥ 1` puts substantial mass on `3, 4, 6`.

## 5. What this adds, and what it does not

**Adds.** P3-11's non-product finding is *not* an artefact of the specific `λ = (1,1)` choice, and it
survives dropping the nesting hypothesis at `n = 3` — including in the **mixed** `λ = (+,−)` case,
where the two components are genuinely different code classes (cyclic and negacyclic) and no nesting
formula was available at all. The distance there was measured, not deduced.

**Does not add.**

* Still **not a theorem.** Every row is a finite enumeration over very small lengths. The informative
  evidence is `n = 3` here, plus `n = 5, 8` in P3-11.
* **No proof** that the joint law can never be a product. The vacuity pattern (independence exactly
  when `h` is constant) is an observation about these cases, not a lemma.
* **No novelty claim.** The ingredients remain P3-3 Thm 1 (hull additivity) and the classical
  `|u|u+v|` structure; blockers B-1, B-2a (+ its Correction), B-2b and Tian–Gao–Gao are still unread,
  so whether this distribution appears in the literature cannot be asserted.
* **Phase 9 remains NO-GO.** A slightly wider table does not change that.

## 6. Reproducibility

```
python3 research_project/phase3/p3_lambda_robust.py > research_project/phase3/p3_lambda_robust_log.txt
```

exit 0, 1.0 s (49 lines compared by `tools/verify_logs.py`). The programme asserts `conj(x) == x³` for all `x ∈ F₉` before counting, and
ends with `Overall: PASS`, which asserts only that the direct-hull cross-check never failed. Added to
`tools/verify_logs.py`.

## 7. Bookkeeping

* Probe: `research_project/phase3/p3_lambda_robust.py`; log `p3_lambda_robust_log.txt`.
* `PHASE_STATUS.md`: P3-12 section; P3-11 annotated as strengthened (its two hypotheses are not needed
  for the conclusion).
* `LINKS.md`: script, log, document.
* `tools/verify_logs.py`: added as a fast case.
