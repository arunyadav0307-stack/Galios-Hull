# Phase 3 / K4-2 — Feasibility of the R4 object

**Question of Phase 3, task 1.** Is the field-level **joint** law of (Hermitian hull dimension,
minimum distance) for `λ`-constacyclic codes over `F_{q²}` obtainable from the two marginal laws —
i.e. is R4's object determined by what is already published — or is the coupling essential?

**Answer: the coupling is essential.** The joint law is **not** the product of its marginals, and
neither marginal determines the other. So R4's object is irreducible, and the Phase 3 deliverable
must compute it directly.

Probe: `phase3/r4_field_joint.py` (stdlib, ≈ 4 s). Written from `372d9a3`.

---

## 1. Instance and method

`F_9`, `n = 6`, `α = 1`. Then `x^6 − 1 = (x−1)³(x+1)³` over `F_9`, so there are
`(3+1)² = 16` distinct cyclic codes, indexed by `(a,b) ∈ {0..3}²`:

```
C(a,b) = ⟨ (x−1)^a (x+1)^b ⟩  ⊂ F_9[x]/(x^6 − 1),   dim = 6 − a − b.
```

Distances are **exact**: for each code, membership of every vector of weight `1, 2, 3, …` is tested
in increasing order, so the reported `d` is a proven minimum — not a bound, not a table lookup.
Hull dimensions are computed independently by the kernel method (R3/R1 machinery), not by formula.

## 2. Results

Distance matrix `d(a,b)` (rows `a = 0..3`, columns `b = 0..3`; `–` = zero code):

| `a \ b` | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **0** | 1 | 2 | 2 | 2 |
| **1** | 2 | 2 | 3 | 4 |
| **2** | 2 | 3 | 3 | 6 |
| **3** | 2 | 4 | 6 | – |

The matrix is symmetric in `(a,b)`, as it must be. Hull dimension for the same codes:
`hull(a,b) = min(a,3−a) + min(b,3−b)`, **reproduced for all 16 codes** — an independent confirmation
of R1's orbit formula on a two-orbit instance.

Joint law over the 16 codes:

| | `d=1` | `d=2` | `d=3` | `d=4` | `d=6` | zero code |
|---|---|---|---|---|---|---|
| **hull 0** | 1 | 2 | – | – | – | 1 |
| **hull 1** | – | 4 | – | 2 | 2 | – |
| **hull 2** | – | 1 | 3 | – | – | – |

Marginals: hull `{0:4, 1:8, 2:4}` (matching R1's `{0:4,1:8,2:4}` for this case) and
`d ∈ {1:1, 2:7, 3:3, 4:2, 6:2}` plus the zero code.

**Independence fails, and fails in the informative direction.** At hull dimension 1 the distance
takes three different values (`2, 4, 6`); at hull 0 it takes `1, 2` and `∞`; at hull 2 it takes
`2, 3`. Observed vs independent prediction, e.g. `(hull 1, d=6)`: observed **2**, predicted **1.0**;
`(hull 2, d=2)`: observed **1**, predicted **1.75**. So neither marginal determines the joint law.

**Distance is not a function of the dimension either.** `d` is constant on `a+b = 1` (all 2) and on
`a+b = 2` (all 2), but on `a+b = 3` it is `2` for `(0,3),(3,0)` and `3` for `(1,2),(2,1)`; on
`a+b = 4` it is `3` for `(2,2)` and `4` for `(1,3),(3,1)`. Same `[6,3]` or `[6,2]` parameters,
different distances.

### 2.1 Two verified observations for P3-2 (no proof claimed)

* **Singleton.** With `k = 6 − a − b`, the Singleton bound reads `d ≤ a + b + 1`. All **15** non-zero
  codes satisfy it, and equality holds for exactly **5** of them:
  `(0,0)`, `(0,1)`, `(1,0)` (trivial), and `(2,3)`, `(3,2)` — the latter two are `[6,1,6]` MDS codes,
  which are also the codes with `hull = 1 = dim`, i.e. Hermitian **self-orthogonal**.
  So the family contains MDS members, but they are a thin set, and no simple `(a,b)` formula for `d`
  is visible: `d` is not a function of `a + b`.
* **LCD distance.** Every `hull = 0` code in this instance has `d ≤ 2` (`d = 1` for the whole space,
  `d = 2` for `⟨(x−1)³⟩` and `⟨(x+1)³⟩`). Recorded as a **conjecture to test**, not a result. If it
  held generally it would be the sharpest statement in the project — it would say that LCD
  constacyclic codes in this family cannot have good distance — so it must be attacked, not hoped for.

`d` for the family is a minimum-weight problem for polynomials with prescribed multiplicities at
`1` and `−1`, i.e. a **multiplicity-code / two-point evaluation** minimum-distance question. That
reframing is the honest starting point for P3-2, and it is why no closed form was found in a day.

## 3. What this settles, and what it does not

**Settled.**

1. R4's object is **not** a function of the hull law (known: Sangwisut–Jitman–Udomkavanich 2017,
   source Theorem 10) plus a distance law. The coupling must be computed.
2. Therefore the Phase 3 deliverable cannot be "combine two known enumerators"; it must be an exact
   algorithm plus structure.
3. Exact computation is **cheap at this size**: 16 codes, all distances proven, ≈ 4 s including hull
   dimensions. The cost grows as `#codes × #small-weight vectors`, both explicit.

**Not settled.**

1. **No closed form for the joint law.** None was found; whether one exists (e.g. a
   `q`-analogue of the rank-metric/weight-enumerator identity, or an appeal to Dinh's repeated-root
   distance results) is open. Dinh's results give `d` for named families; they were not sufficient
   here — the 16 codes span `d = 1,2,3,4,6` with no single formula visible in `(a,b)`.
2. **Scaling.** Nothing here says the computation is feasible for larger `n` or `q`; it says it is
   feasible for a table.
3. **One instance, one field, one `α`.** No general claim is made. In particular the observation
   that every LCD (`hull = 0`) code here has `d ≤ 2` is a **conjecture to test in Phase 3**, not a
   result — and it is exactly the kind of statement that would give the project its coding-theory
   meaning (LCD codes with distance).

## 4. Consequence for Phase 3

K4-2 passes in the sense that the object is well defined, irreducible, and exactly computable at
table scale. It does not pass in the sense of "there is a formula waiting to be written down".

The Phase 3 programme that follows from this:

* **(P3-1)** Extend the exact computation to a table over `q ∈ {3,4,5}`, `n` up to ≈ 12, several `α`,
  including `p | n`, recording `(hull, d)` joint distributions.
* **(P3-2)** Prove the structural facts the table suggests — starting with the distance of the
  two-orbit codes `⟨(x−1)^a (x+1)^b⟩`, where the matrix above is already a complete answer for
  `n = 6, α = 1`, and the LCD-distance observation.
* **(P3-3)** Only then attempt the ring-level statement (the Gray coupling of §3 of
  `R4_FEASIBILITY.md`), which is the actual R4 question.

Honest status: Phase 3 has produced its first feasibility decision and a complete exact computation
on one instance. It has **not** produced a theorem, a closed form, or any novelty claim; blockers
**B-1** (publisher full texts) and **B-2** (Debnath–Prakash body) remain open.
