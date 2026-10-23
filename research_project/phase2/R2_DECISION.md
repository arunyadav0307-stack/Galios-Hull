# R2 — Decision: NO-GO

**Candidate question (as recorded in `NOVELTY_ASSESSMENT.md` §5).** `λ = Σ_ℓ η_ℓ α_ℓ` admits
many decompositions; with `α₁ ≠ α₂`, how many admissible codes have a given hull-dimension
vector, and how does the count depend on the decomposition of `λ`?

**Verdict: NO-GO — but not for the reason the question anticipated.** The decomposition is not
ambiguous: in both readings of "decomposition" a given `λ` has **exactly one**. R2 therefore has a
false premise. The only real content in it is a normalisation hazard (Phase 1 finding F-1), which
is quantified below as a *modelling* trap to avoid, not an open question.

Written from `25bbe62` on branch `arena/831a2e65-galios-hull`. Probe:
`phase2/r2_probe/r2_probe.py`, log `r2_probe_log.txt` (53 lines), runtime < 1 s.

---

## 1. Assumptions

`R_e = F_{q²}[u]/(u^e − 1)`, `e | q+1`, `p = char F_{q²}`; `μ_1, …, μ_e` the `e`-th roots of
unity in `F_{q²}` (distinct, since `p ∤ e`); `λ ∈ R_e^*`; codes are `λ`-constacyclic, i.e. ideals of
`R_e[x]/(x^n − λ)`; Hermitian duality with the **ring** `q`-power; counting object = distinct
codes. Tested instances: `q = 2, e = 3` (the only `e ≥ 3` instance small enough to enumerate —
`|R_e| = 64`) and `q = 3, e = 4` at element level (`|R_e| = 6561`).

Two readings of "the decomposition of `λ`" are in play, and they are **different**:

| | Expansion | Coefficients |
|---|---|---|
| **A — CRT coordinates** | `λ = Σ_ℓ e_ℓ α_ℓ` with `e_ℓ` the true idempotents | forced: `α_ℓ = λ(μ_ℓ)` |
| **B — the paper's `η`** | `λ = Σ_ℓ η_ℓ a_ℓ` with `η_ℓ = ∏_{j≠ℓ}(u − μ_j)` | forced once `{η_ℓ}` is a basis |

The relation between them is the whole story:
`λ(μ_ℓ) = a_ℓ · η_ℓ(μ_ℓ)`.

---

## 2. T1 — the idempotents are the ones the analysis needs

Built by Lagrange interpolation in `R_e` (`e_ℓ = η_ℓ / η_ℓ(μ_ℓ)`), not assumed:

| Case | Roots of `u^e − 1` | Idempotents | `e_ℓ²=e_ℓ` | `e_ℓe_j=0` | `Σ_ℓ e_ℓ = 1` |
|---|---|---|---|---|---|
| `q=2, e=3` | `1, 2, 3` (all of `F_4^*`) | `(1,1,1)`, `(1,3,2)`, `(1,2,3)` | ✓ | ✓ | ✓ |
| `q=3, e=4` | `1, 2, 3, 6` | `(1,1,1,1)`, `(1,2,1,2)`, `(1,6,2,3)`, `(1,3,2,6)` | ✓ | ✓ | ✓ |

## 3. T2 — the decomposition is unique, in both readings

`q = 2, e = 3`: `|R_e| = 64`, `|R_e^*| = 27`.

| Check | Result |
|---|---|
| Reading A: `Σ_ℓ e_ℓ · λ(μ_ℓ) = λ` for every unit `λ` | **27/27** |
| Reading A: number of decompositions of a given `λ` | **1** (the coordinates *are* evaluations of `λ`, so they are forced) |
| Reading B: `(a_1,…,a_e) ↦ Σ_ℓ η_ℓ a_ℓ` on all `64` tuples | **injective** (64 distinct images) |
| Reading B: units hit | **27/27**, all fibres of size **1** |

The `η_ℓ` are a basis of `R_e` because `η_ℓ(μ_j) = 0` for `ℓ ≠ j` and `η_ℓ(μ_ℓ) ≠ 0`, so the
matrix `(η_ℓ(μ_j))` is diagonal and invertible. Reading B is therefore a **change of basis**, not
an ambiguity: `#decompositions = 1` in it as well.

For `q = 3, e = 4` the same reconstruction is checked on the `4` monomials `u^0…u^3`; since both
sides are linear in `λ`, that proves it for **every** `λ ∈ R_e`.

**Consequence.** R2 asks how the count depends on a choice that does not exist. Its premise is
false, and no amount of literature searching could rescue it — the objection is elementary.

## 4. T3 — what F-1 actually is: a rescaling, quantified

Phase 1 finding **F-1** recorded that the printed `η_ℓ` are unnormalised (`η_ℓ² = λ_ℓ η_ℓ`,
`Σ η_ℓ ≠ 1`). The probe gives the exact form:

| Case | `η_ℓ(μ_ℓ)` | `Σ_ℓ η_ℓ` | equals `1`? |
|---|---|---|---|
| `q=2, e=3` | `1, 3, 2` | `(0,0,1)` | no |
| `q=3, e=4` | `1, 2, 6, 3` | `(0,0,0,1)` | no |

and the relation `λ(μ_ℓ) = a_ℓ · η_ℓ(μ_ℓ)` holds for **every** unit `λ` (verified `27/27`).

So reading B's `a_ℓ` is *not* the `ℓ`-th component multiplier unless `η_ℓ(μ_ℓ) = 1`, which happens
only for the factor with `μ_ℓ = 1`. Since the `ℓ`-th component code is `λ(μ_ℓ)`-constacyclic
(`R_e[x]/(x^n−λ) ≅ ∏_ℓ F_{q²}[x]/(x^n − λ(μ_ℓ))`), using `a_ℓ` in place of `λ(μ_ℓ)` assigns the
wrong multiplier — and hence the wrong field law — to every component but one.

**Quantified cost.** At `F_4`, `n = 6` (`p = 2 | 6`) the field laws genuinely differ:

* `α = 1` → `{0:8, 1:12, 2:6, 3:1}` (27 codes)
* `α = 2, 3` → `{0:2, 3:1}` (3 codes)

Predicting the `R_3` hull law from reading B gets it **wrong for 18 of the 27 multipliers**; only
the 9 with `a_ℓ = λ(μ_ℓ)` throughout survive. This is the concrete form the Phase 1 warning takes:
an unnormalised-`η` count is not merely inelegant, it is numerically wrong on two thirds of the
multipliers.

**Important scope note.** This is a hazard for a *counting* extension, **not an error in the source
paper**. The paper uses `η_ℓ` only as notation inside lcm-based hull formulas, never to count
codes; Phase 1 already recorded that no parameter of the paper changes. The correction is the
normalisation `e_ℓ = η_ℓ/η_ℓ(μ_ℓ)`, a one-line fix.

## 5. T4 — with correct coordinates, the law depends only on the multiset

`q = 2, e = 3`, component laws convolved (the product law itself was enumerated exhaustively in R3:
**27/27** and **16/16**; it is not re-enumerated here). `F_4`, `n = 6`:

| Multiset of component laws | induced distribution | total |
|---|---|---|
| `{L,L,L}` with `L = {0:2,3:1}` | `{0:8, 3:12, 6:6, 9:1}` | 27 |
| `{L,L,M}` with `M = {0:8,1:12,2:6,3:1}` | `{0:32, 1:48, 2:24, 3:36, 4:48, 5:24, 6:12, 7:12, 8:6, 9:1}` | 243 |
| `{L,M,M}` | `{0:128, …, 9:1}` (10 terms) | 2 187 |
| `{M,M,M}` | `{0:512, …, 9:1}` (10 terms) | 19 683 |

* **4** distinct multisets occur among the 27 multipliers.
* Each multiset induces **exactly one** distribution — 0 multisets with more than one.
* Each total is the product of the component code counts (`27 = 3³`, `243 = 3²·27`,
  `2187 = 3·27²`, `19683 = 27³`) — an internal consistency check on the convolution.

So the law is a **symmetric function of the multiset of component laws**. The dependence on `λ` is
real (the four rows differ) but it is fully accounted for by Theorem 10 / the product law; there is
no residual "decomposition" freedom.

## 6. Kill criterion, named

**K-R2. The decomposition is the CRT coordinate map, which is a bijection — so R2 has no free
variable to depend on.**

1. **Source Theorem 2 / elementary CRT**: `R_e ≅ ∏_{ℓ=1}^e F_{q²}` via `λ ↦ (λ(μ_1),…,λ(μ_e))`.
   A homomorphism out of a product of fields is determined by its coordinates, so `α_ℓ = λ(μ_ℓ)`
   is forced. Unique. (Verified 27/27 and by linearity for `e = 4`.)
2. **Every other `e`-term expansion with a basis** (`η_ℓ`) is related to it by an invertible
   diagonal change of basis — unique as well (verified: injective, all fibres size 1).
3. **The product law** (R3, enumerated 27/27 / 16/16) then gives the distribution as a symmetric
   function of the component laws.

Hence R2 is a **modelling question whose premise is false**; it does not reduce to a known result,
it reduces to *no question at all*. Classification: `K` (vacuous), not `N2`.

## 7. Status of Gate 2

| Revision | Outcome | Mechanism |
|---|---|---|
| **R3** — dual-containing subfamily over `R_e` | **NO-GO** (`c9d4517`) | product of published field-level dual-containing counts |
| **R1** — repeated-root distribution `p \| n` over `R_e` | **NO-GO** (`25bbe62`) | lattice-point count in the boxes of the source's own Theorem 10 |
| **R2** — dependence on the decomposition of `λ` | **NO-GO** (this document) | the decomposition is unique; the only content is an `η`-normalisation trap |

**All three surviving revisions are now dead.** Gate 2 — *"the proposed main contribution is
distinguishable from the closest known results"* — **cannot be passed** by the "count
`λ`-constacyclic codes over `R_e` by Hermitian hull dimension, then pass to a joint/total
enumerator" line of attack. The reason is structural and now demonstrated three times over: the
CRT decomposition makes every such quantity a product of field-level laws, and the field-level laws
for arbitrary `n` (including `p | n`) are given by the source's Theorem 10 and by
Sangwisut–Jitman–Udomkavanich (AMC 2017).

This is a negative result about the *proposed research question*, not about the paper. Phase 1
found no mathematical error that changes a parameter, and Phases 0–2 stand as delivered.

**Recommendation.** Do **not** begin Phase 3 on this question. Either

* (a) authorise a genuinely different question — the only one identified so far that is *not* a
  product of field laws is the **distance-constrained** quantum-parameter distribution over `R_e`
  (the minimum distance couples the CRT components, whereas the hull dimension does not). It is
  much harder and is not a relabelled R1/R2/R3; it would need its own feasibility check before any
  Phase 3 work; or
* (b) close the project at Gate 2 and record that the proposed contribution is not distinguishable
  from prior art under the available evidence.

No novelty is claimed anywhere in this document. Blockers **B-1** (publisher full texts) and **B-2**
(Debnath–Prakash body) remain open; the R2 verdict does not depend on either.

---

## 8. Probe correctness

| Item | Detail |
|---|---|
| Dependencies | none beyond the stdlib; imports `make_field` from the R1 probe and `GF`/`find_irreducible` from the R3 probe |
| Arithmetic | ring elements are coefficient tuples with cyclic convolution, so no `\|R\|²` tables and `e = 4` is affordable; all scalar arithmetic in the table field `F_{q²}` |
| Bug found and fixed | `units()` initially pre-filtered on *coefficients* being nonzero, which is wrong: `u` is a unit with a zero constant term. Correct criterion is `λ(μ_ℓ) ≠ 0` for every `ℓ`. With the bug, `\|R_e^*\|` was reported as 18 instead of 27 and T3's count was `12/18`; both are now `27`. |
| API trap | `find_irreducible(p, deg)` in the R3 probe returns a **field** already (`GF(p, deg, mod)`), not a modulus; reuse `r1_probe.make_field` instead of wrapping it again. |
| Self-correction during the test | The first version of T3 asserted that the `η`-map is "neither injective nor surjective". That is **false** — `{η_ℓ}` is a basis and the map is a bijection. The text and the test were rewritten around the actual defect (rescaling of the component multiplier). The misleading claim is recorded here rather than quietly dropped, because it was the natural guess and the probe is what refuted it. |
