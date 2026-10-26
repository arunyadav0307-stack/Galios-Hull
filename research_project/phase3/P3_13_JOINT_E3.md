# P3-13 — The exact joint `(hull, distance)` law for `e = 3`, and where it fails

Date: 2026-10-25. Probe: `phase3/p3_joint_e3.py`. Log: `phase3/p3_joint_e3_log.txt` (75 lines, exit 0,
4.9 s). Pure stdlib, ASCII.

Status: **one computed distribution (non-degenerate, `e = 3`) plus two documented failures.** P3-11 and
P3-12 were confined to `e = 2`; this is the first `e ≥ 3` joint law in the project. No theorem and no
novelty claim.

---

## 1. Choosing the field — and why two obvious choices fail

`R_e = F_q[u]/(u^e−1)` needs `gcd(e,q) = 1`, so `e = 3` forces `char ≠ 3`; the Hermitian form needs `q`
a square. That leaves `F_4, F_16, F_25, F_49, …`.

**Failure 1 — `F_4`.** In characteristic 2, `1·conj(1) + 1·conj(1) = 0`, so *every* cyclic code of
length 3 over `F_4` has hull 0. The joint law collapses to a single `h`-value and the independence test
is vacuous. Recorded, not hidden.

**Failure 2 — `F_25`, cyclic components.** `F_25 = F_5[t]/(t²−2)`, conjugation `x ↦ x⁵`. All 4 cyclic
codes of length 2 and all 8 of length 3 are **Hermitian LCD** (hull 0). Cause: their generator matrices
have entries in `F_5`, conjugation fixes `F_5`, so the Hermitian hull coincides with the Euclidean hull.
Again degenerate, again recorded.

**What works — `F_25`, negacyclic components, `n = 4`.** The 16 negacyclic codes (ideals of
`F_25[x]/(x⁴+1)`) have hull dimensions `0, 1, 2`. `x⁴+1` splits into 4 distinct linear factors over
`F_25` because `8 | 24`, so the divisors form the Boolean lattice `B₄`. This is the first `e = 3`
family here that is non-degenerate.

## 2. Method

* `ψ(c₁,c₂,c₃)[j] = Σ_l α_l^j c_l`, `j = 0,1,2`, with `α = (1, α, α²)` the three cube roots of unity
  in `F_25` (found and asserted by the script: `1, 12, 17`). Generator matrix = union over `l` and over
  generator rows `r` of `C_l` of the length-12 word `(α_l⁰r | α_l¹r | α_l²r)`.
* **Distance exactly, without enumeration.** `25¹²` words is impossible, so `d` is computed by the
  circuit characterisation (P3-7 Lemma C): `d` = smallest dependent set of columns of a parity-check
  matrix `H`, obtained from the RREF of `G`. Exact, not a bound. Search capped at weight 6; chains whose
  distance exceeds the cap are **counted and listed**, not silently dropped.
* **Hull** directly as `k − rank(G conj(G)ᵀ)`, cross-checked against `Σ_l dim Hull_H(C_l)`
  (P3-3 Thm 1): **0 failures**.

## 3. Result

`λ = (−1,−1,−1)`, `n = 4`, ψ-length 12. The 256 nested chains `C₃ ⊆ C₂ ⊆ C₁` (multichains in `B₄`,
`4⁴ = 256`); **235** gave an exact distance, 21 exceeded the cap of 6.

| h \ d | 1 | 2 | 3 | 4 | 6 |
|---|---|---|---|---|---|
| 0 | 1 | 3 | 7 | 0 | 2 |
| 1 | 0 | 8 | 20 | 4 | 8 |
| 2 | 0 | 8 | 24 | 16 | 14 |
| 3 | 0 | 8 | 12 | 32 | 8 |
| 4 | 0 | 6 | 6 | 26 | 2 |
| 5 | 0 | 4 | 4 | 8 | 0 |
| 6 | 0 | 2 | 2 | 0 | 0 |

* 7 distinct hull dimensions, 5 distinct distances — **the test is not vacuous**.
* **TV = 0.1989, max deviation 11.3617 → the joint law is NOT the product of its marginals.**
  (Corrected values. The earlier 234-triple version read TV 0.1991 / max deviation 11.2991; see the
  correction note below and `P3_14_KILLTEST_NONPRODUCT.md` §4.)
* Component distances cover 2, 3, 4 (and 1 for the whole space); hull dimensions 0, 1, 2.

This is the first `e = 3` evidence for the non-product phenomenon established for `e = 2` in P3-11 and
P3-12, and it agrees with it.

## 3a. Correction (2026-10-25, P3-14) — one chain was silently mislabelled

The P3-14 kill test found that `girth()` returned `None` whenever the parity-check matrix was empty,
i.e. when the code is the whole space. That code has `d = 1`, not "undefined". So the chain whose three
components are all the full space printed *"distance above the search cap 6, skipped"* and dropped out
of the table, when it belongs at `(h = 0, d = 1)`.

Corrected and re-run: **235** triples (was 234), a new `d = 1` column with `(h=0, d=1) = 1`, **TV =
0.1989** (was 0.1991), max deviation **11.3617** (was 11.2991), log 75 lines. The conclusion is
unchanged — still not a product. The table and the figures above are the corrected ones; the old values
are recorded here rather than erased.

## 3b. Interpretation withdrawn (2026-10-25, P3-14) — read this before citing the table

The non-product property above is **not** a phenomenon of the Gray image. It is a deterministic
consequence of hull and distance already being correlated inside a single component code, because
`h(ψ)` depends on the components only through their hulls (P3-3 Thm 1) and `d(ψ)` only through their
distances (P3-10). `P3_14_KILLTEST_NONPRODUCT.md` shows that product-ising the component law makes the
ψ-level TV **exactly zero**. The table stands; the finding it was offered as is withdrawn.

## 4. Two bugs this run exposed (kept as an audit trail)

1. **`fneg(-1)` returned `6`, not `1`.** `fneg` took an *encoding* `a + 5b`, but was called with the raw
   integer `−1`; it returned `1 + t`. Consequence: the "negacyclic" modulus was actually `x⁴ + t + 1`,
   which has only 4 divisors — so the first run reported `n = 4` as degenerate when it is not. Caught by
   the divisor count being 4 where 16 was expected. `fneg` now asserts its precondition and `modulus`
   passes `lam % MOD`.
2. **A wrong chain count.** I wrote `C(4+3,3) = 35` chains for `B₄`. That is not the multichain count;
   `4⁴ = 256` is. The script printed 256 while the comment said 35, and the discrepancy was traced by
   testing divisibility independently: **81 ordered divisor pairs = 3⁴, 0 disagreements** between
   `pmod` and explicit multiplication. So the enumeration was right and my arithmetic was wrong.

Both are now stated in the script, not silently fixed.

## 5. Scope

**Not a theorem.** A finite table over one field at one length, with 21 of 256 chains excluded by a
search cap.

**Not a claim that `e ≥ 3` is settled.** Only `n = 4` over `F_25` with `λ = (−1,−1,−1)` is covered.
Whether the non-product phenomenon holds for all `e ≥ 3` is untouched, and P3-3 Theorem 5's
non-determination of `d(ψ)` still governs the general case.

**Not a novelty claim.** Ingredients are P3-3 Thm 1 (hull additivity, from the source paper's
componentwise structure) and the circuit characterisation of distance. Blockers B-1, B-2a (+ its
Correction), B-2b and Tian–Gao–Gao remain unread.

**Phase 9 remains NO-GO.**

## 6. Reproducibility

```
python3 research_project/phase3/p3_joint_e3.py > research_project/phase3/p3_joint_e3_log.txt
```

exit 0, 4.7 s, stdlib only. Asserts before counting: `conj(x) == x⁵` on all of `F_25`; `x·conj(x) ≠ 0`
for `x ≠ 0`; the cube roots `1, 12, 17` are distinct and satisfy `α³ = 1`. Ends with `Overall: PASS`,
which asserts only that the hull cross-check never failed.

## 7. Bookkeeping

* Probe `phase3/p3_joint_e3.py`, log `p3_joint_e3_log.txt`, added to `tools/verify_logs.py`.
* `PHASE_STATUS.md`: P3-13 section; the P3-11/P3-12 "e ≥ 3 untouched" line updated to record partial
  `e = 3` coverage with its limits.
* `LINKS.md`: script, log, document.
