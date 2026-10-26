# P3-14 — Kill test: the "non-product joint law" finding is a consequence, not a phenomenon

Date: 2026-10-25. Probe: `phase3/p3_killtest_nonproduct.py`. Log: `phase3/p3_killtest_nonproduct_log.txt`
(68 lines, exit 0, 0.6 s). Pure stdlib, ASCII.

**Outcome: the finding that P3-11, P3-12 and P3-13 built up is DEMOTED.** The computations in those
three documents stand and reproduce. What does not survive is the *interpretation*: the failure of
independence is not a phenomenon of the Gray image. It is a deterministic consequence of the fact that
hull size and minimum distance are correlated inside a single component code — which nobody would
doubt. This probe was run specifically to try to kill the finding, and it succeeded.

---

## 1. The objection, stated before the computation

Two results already proved in this project, both used uncritically by P3-11/P3-12/P3-13:

* **P3-3 Theorem 1** — `h(ψ) = h(C₁) + h(C₂)` (hull is additive over components).
* **P3-10** — `d(ψ) = min{2d(C₁), d(C₂)}` for `C₂ ⊆ C₁`.

Read them together. `h(ψ)` depends on the components **only through their hulls**; `d(ψ)` depends on
them **only through their distances**. So if hulls and distances were independent inside a single
component, then `h(ψ)` and `d(ψ)` would be independent automatically, for free, with no structure
needed. The ψ-level tables could only be non-product for one reason: `h` and `d` were already dependent
inside each component.

That is a strong reason to suspect the finding is empty. It is also testable in a few seconds.

## 2. What was computed

`F₉ = F₃[t]/(t²+1)`, conjugation `x ↦ x³`, cyclic components of length `n = 5`, ψ-length 10.
`x⁵ − 1` gives 8 divisors here (5 ∤ 8, and `ord₅(9) = 2`, so it factors as `(x−1)` times two
quadratics — 27 nested pairs).

**Step 1 — inside one component.** The joint law of `(h, d)` over the 7 nonzero codes:

| h \ d | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 0 | 1 | 1 | 0 | 0 | 1 |
| 2 | 0 | 0 | 2 | 2 | 0 |

**TV = 0.2449.** Mean distance by hull dimension: `h = 0` → 2.667 (range 1..5); `h = 2` → 3.500
(range 3..4). Larger hull, larger distance.

**Step 2 — at ψ level.** 26 usable nested pairs: **TV = 0.2382**, hull additivity 0 failures, and
P3-10's distance formula **0 failures** (the first run reported 1 failure — see §4, it was a bug in my
girth routine, not in P3-10).

**Step 3 — the comparison.** Component `TV = 0.2449`; ψ-level `TV = 0.2382`. The ψ-level number is not
larger than the component-level one. Nothing is being amplified. The dependence is the same dependence.

**Step 4 — the decisive test.** Replace the component law by the product of its own marginals (keeping
the real hulls and the real pair multiplicities), then push through the same map
`(h₁,h₂,d₁,d₂) ↦ (h₁+h₂, min{2d₁,d₂})`:

> **TV of the pushed-forward law = 0.0000000000 — exactly zero.**

The moment the component-level `(hull, distance)` correlation is removed, the ψ-level non-product-ness
vanishes completely. There is no residual effect from the Gray image.

## 3. The proposition this yields — and why it is not a contribution

Let `C₁, C₂` be linear over `F_{q²}` with `C₂ ⊆ C₁`, `ψ` the `|u|u+v|` map. Then `h(ψ)` is a function
of `(h(C₁), h(C₂))` alone and `d(ψ)` a function of `(d(C₁), d(C₂))` alone, so for independently drawn
components

```
h(ψ) ⊥ d(ψ)   ⟺   h(C) ⊥ d(C) in the component ensemble.
```

This is true, it is easy to prove from two results already in the project, and it is **not a
contribution** — it says that a function of one variable and a function of another are independent
when the underlying variables are. The empirical content of P3-11/P3-12/P3-13 reduces to
"codes with bigger hulls tend to have bigger distances", which is expected: a nonzero hull is a
constraint on a code.

**Honest status of R4:** the joint `(hull, distance)` distribution over `R_e` was the last surviving
candidate contribution. Its headline property is now explained rather than discovered. **R4 is
withdrawn on these grounds** — not on the grounds of the unread literature (B-1, B-2a, B-2b,
Tian–Gao–Gao), which remain open and which the withdrawal rule still applies to independently.

## 4. A real defect this probe found in P3-13

The first run of Step 2 reported **1 failure** of P3-10's formula. That was investigated rather than
recorded, and the cause was mine: `girth()` returned `None` when the parity-check matrix was empty,
i.e. when the code is the whole space. The correct distance there is `1`, not "undefined". Consequence
in P3-13: the chain with all three components equal to the full space printed *"distance above the
search cap 6, skipped"* and silently dropped out of the table, when it belongs at `(h=0, d=1)`.

**P3-13 has been corrected and re-run.** The table now has 235 triples (was 234), a `d = 1` column with
`(h=0, d=1) = 1`, and **TV = 0.1989** (was 0.1991), max deviation 11.3617 (was 11.2991). The conclusion
is unchanged — still not a product — but it is now not a product for the reason given in §3. The
P3-13 document carries a correction note and its log is 75 lines.

## 5. What is NOT being claimed

* Not that P3-11/P3-12/P3-13 are wrong. Their numbers reproduce exactly (P3-13's corrected log and
  this probe are both in the regression suite). The tables are right; the interpretation was too
  generous.
* Not that the Gray-image family is exhausted. §3 covers the *nested `e = 2`* case where both formulas
  hold. For the non-nested and `e = 3` cases there is no such product formula, so the inheritance
  argument does **not** automatically apply there — but nothing in those tables has been shown to
  survive as a phenomenon either, and the burden is now on a positive demonstration.
* Not a theorem of independent interest. §3 is a triviality and is labelled as one.

**Phase 9 remains NO-GO, and this strengthens it: the last candidate contribution has been withdrawn.**

## 6. Reproducibility

```
python3 research_project/phase3/p3_killtest_nonproduct.py > research_project/phase3/p3_killtest_nonproduct_log.txt
```

exit 0, 0.6 s. Registered in `tools/verify_logs.py`; `--only p3_killtest_nonproduct` reproduces 68
lines identically. Asserts before counting: `conj(x) = x³` on `F₉`; `x·conj(x) ≠ 0` for `x ≠ 0`;
`x⁵−1` has exactly 8 divisors. ψ-level distances use the column-matroid girth (P3-7 Lemma C), so a
length-10 code with `k = 10` costs 10³ subsets rather than 9¹⁰ words.
