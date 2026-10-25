# P3-10 — The `e = 2` Gray image is the `|u|u+v|` construction, and its distance is exact

Date: 2026-10-25. Probe: `phase3/p3_nested_gray.py`. Log: `phase3/p3_nested_gray_log.txt`
(exit 0, 501 s). Pure stdlib, ASCII.

Status: **one theorem proved (elementary), verified on 878 cases, and identified as classical.**
No novelty is claimed; the new content here is that the question P3-3 left as a two-sided bound is,
for `e = 2` with nested components, a textbook construction with a known exact answer.

---

## 1. What P3-3 left open

`P3_3_RING_GRAY.md` Theorem 2 bounds the Gray-image distance two-sidedly:

    min_l d(C_l)  <=  d(psi(C))  <=  e · min_l d(C_l)        for every admissible M,

and Theorem 5 shows that `d(psi(C))` is **not determined** by the tuple `(k_1,d_1,...,k_e,d_e)`:
the witness `(1,3,1,3)` realises `d(psi) ∈ {3,4,5}`.

The upper bound `e · min_l d_l` was never sharpened. This document does that for `e = 2`.

## 2. The theorem

Setting exactly as in P3-3: `R_e = F_q[u]/(u^e − 1)`, `gcd(e,q) = 1`, `R_e ≅ F_q^e` through the roots
`α_1,…,α_e` of `u^e − 1`, and `ψ = M·(c_1,…,c_e)^T` with `M = (α_l^j)_{j,l}`. For `e = 2` and `q` odd
the roots are `α_1 = 1`, `α_2 = −1`, so `M = ((1,1),(1,−1))` and

    ψ(c_1, c_2) = ( c_1 + c_2 , c_1 − c_2 ).

**Theorem P3-10.** Let `q` be odd and let `C_2 ⊆ C_1` be linear codes of length `n` over `F_q`. Then

    ψ(C_1 × C_2) = { (u, u+v) : u ∈ C_1, v ∈ C_2 },

which is the `|u|u+v|` (Plotkin sum) code, and consequently

    d( ψ(C_1 × C_2) ) = min { 2·d(C_1) , d(C_2) } .

*Proof.* Put `u = c_1 + c_2` and `v = −2c_2`. Since `C_2 ⊆ C_1` we have `u ∈ C_1`, and `v ∈ C_2`. Then

    u + v = c_1 + c_2 − 2c_2 = c_1 − c_2 ,

which is exactly the second coordinate of `ψ(c_1,c_2)`. Conversely, given `(u,v) ∈ C_1 × C_2`, take
`c_2 = −v/2` (defined because `q` is odd) and `c_1 = u + v/2`; then `c_1 ∈ C_1` because `C_2 ⊆ C_1`, and
`ψ(c_1,c_2) = (u, u+v)`. So the map is a bijection `C_1 × C_2 → C_1 × C_2` and the image is the
`|u|u+v|` code.

For a codeword `(u, u+v)` the weight is `w(u) + w(u+v)`.
* If `v = 0`: the weight is `2w(u) ≥ 2 d(C_1)` (or `0` when `u = 0`).
* If `v ≠ 0`: `u − (u+v) = −v`, so by the triangle inequality `w(u) + w(u+v) ≥ w(v) ≥ d(C_2)`;
  equality is attained at `u = 0` with `v` of minimum weight.

Hence `d = min{2 d(C_1), d(C_2)}`. ∎

**Consistency with P3-3 Thm 2.** Since `C_2 ⊆ C_1` gives `d(C_2) ≥ d(C_1)`, we have
`min{2d_1,d_2} ≤ 2 d_1 = e·min_l d_l`, so the new value sits inside the old band, as it must. It is
strictly better whenever `d_2 < 2 d_1`, and it is *exactly* `e·min d_l` only in the corner case
`d_2 ≥ 2d_1`.

## 3. Verification

`python3 research_project/phase3/p3_nested_gray.py > phase3/p3_nested_gray_log.txt` — one command,
exit 0, 501 s (31 lines compared by `tools/verify_logs.py`). Every cyclic code of length `n` over `F_p` is enumerated via its generator
polynomial (all monic divisors of `x^n − 1`), distances are computed exhaustively, and for every
**nested** pair `(g_1 | g_2)` the code `ψ(C_1 × C_2)` is enumerated and its distance compared with
`min{2d_1,d_2}`. Pairs whose product exceeds 300 000 words are skipped and counted as skipped.

| `p` | `n` = 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| 3 | 5 | – | 19 | 5 | – |
| 5 | 5 | 5 | 64 | – | 41 |
| 7 | 5 | 19 | 16 | 2 | 371 |
| 11 | 5 | 4 | 12 | 115 | 19 |
| 13 | 5 | 15 | 34 | 1 | 111 |

(entries are the number of nested pairs checked; `–` means `p | n`, so `x^n − 1` is not separable
and the `e = 2` hypothesis `gcd(e,q) = 1` fails for the ring decomposition.)

**Result: 878 nested pairs checked, 0 disagreements across 22 `(p,n)` cases.**

**The hypothesis is necessary, not decorative.** The same sweep tests every **non-nested** pair and
finds **2915** of them where `d(ψ) ≠ min{2d_1,d_2}`. So `C_2 ⊆ C_1` is both sufficient (proved) and,
in the cases tested, necessary. Two concrete examples from the log (earlier `F_9` run):

* `C_1 = ⟨x+1⟩`, `C_2 = F_9[x]/(x^2−1)`: `d_1 = 2`, `d_2 = 1`, formula predicts `1`, `d(ψ) = 2`.
* `n = 3`: `C_1 = ⟨x−1⟩`, `C_2 = ⟨1⟩`: `d_1 = 3`, `d_2 = 1`, formula predicts `1`, `d(ψ) = 2`.

## 4. This is classical — and that matters for the project

The `|u|u+v|` construction and its distance `min{2d(C_1), d(C_2)}` is textbook:

* J. H. van Lint, *Repeated-root cyclic codes*, **IEEE Trans. Inf. Theory 37(2):343–345 (1991)** —
  obtains a binary cyclic code of length `2n` (`n` odd) from two codes of length `n` by `|u|u+v|`.
* G. Castagnoli, J. L. Massey, P. A. Schoeller, N. von Seemann, *On repeated-root cyclic codes*,
  **IEEE Trans. Inf. Theory 37(2):337–342 (1991)**.
* Restated as the *generalised van Lint theorem*, e.g. **Theorem 2.1 of arXiv:2402.02853**, verbatim:
  *"the minimum distance of `C(C_1,C_2)` is `min{2d(C_1), d(C_2)}`"*.

So Theorem P3-10 is a **re-derivation of a classical fact**, and the finding of consequence is a
negative one about this project's own framing:

> For `e = 2`, the Gray map of the source paper is *exactly* the `|u|u+v|` construction. Therefore the
> `e = 2` distance question was never open, and P3-3's two-sided bound is superseded in the nested case
> by an exact classical formula.

This is the same pattern as P3-7b (L-2 turned out to be Dinh 2008): a question carried in this project
as "bounded, open" is in fact settled in the literature. Recorded as such. **No novelty claimed.**

## 5. Consequence for R4 (the one line of forward value)

For `e = 2` with nested components, `d(ψ)` is a **function of the pair** `(d(C_1), d(C_2))`. Two codes
with the same distance pair therefore have the same `d(ψ)`, and the joint law of
`(dim Hull_H(ψ(C)), d(ψ(C)))` — the object R4 asks for — collapses to the joint law of
`(dim Hull_H(C_1), dim Hull_H(C_2), d(C_1), d(C_2))` composed with a deterministic map on the second
coordinate. Hull dimensions add by P3-3 Theorem 1 (`dim Hull_H(ψ(C)) = Σ_l dim Hull_H(C_l)`, verified
256/256 in `p3_gray_hull_identity.py`). So for the nested `e = 2` family the R4 distribution is a
*computation over the field-level joint law*, not a new structural problem.

**Consistency check on P3-3 Theorem 5.** Its non-determination witness has `d_1 = d_2 = 3` and realises
`d(ψ) ∈ {3,4,5}`. By Theorem P3-10 a *nested* pair with `d_1 = d_2 = 3` would force
`d(ψ) = min{6,3} = 3`, so the witness pair must be **non-nested** — which is exactly where the sweep
above finds the formula failing. The two results are consistent; neither overturns the other.

## 6. What this does not do

* It does not settle `e ≥ 3`. The reduction to `|u|u+v|` is specific to `e = 2`; for `e ≥ 3` the Gray
  image is a length-`e` product and P3-3 Theorem 5's non-determination still stands.
* It does not touch the hull side at all, and says nothing about the source paper's own theorems.
* It does not close any blocker (B-1, B-2a + Correction, B-2b, Tian–Gao–Gao all still unread), so no
  novelty is claimed for anything here.
* **It does not revive Phase 9.** A re-derived classical formula is not a new theorem. Phase 9 remains
  **NO-GO**.

## 7. Bookkeeping

* Probe: `research_project/phase3/p3_nested_gray.py`; log `p3_nested_gray_log.txt` (in the P3-9 regression set; reproduces exactly).
* Alias note: this document is numbered P3-10 to avoid collision with `P3_9_REGRESSION_AUDIT.md`.
* `PHASE_STATUS.md`: P3-10 section; P3-3's Theorem 2 row annotated as superseded for `e = 2` nested.
* `LINKS.md`: probe, log and document added.
* `tools/verify_logs.py`: the new probe added to the regression set.
