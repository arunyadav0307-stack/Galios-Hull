# R3 DECISION DOCUMENT — "distribution of dual-containing codes over `R_e`"

**Prepared:** 2026-10-23, on top of Phase 2 at commit `26de249`.
**Status of this document: decision preparation only. Phase 3 has NOT been started, no manuscript text has been drafted, and no new theorem is claimed.**

## Verdict, stated first

**R3 is precise enough to be authorised — and that is exactly why it should not be.**

Over the ring in question the Hermitian dual-containing condition is *componentwise*, so the sought distribution is an **exact product of `e` independent, elementary, field-level counts**. The two-ring exhaustive probe below confirms this on every ideal for all `64` and `27` admissible multipliers. This is the "routine product count" case the blueprint and the user's instruction anticipate, and the honest recommendation is to **stop R3 rather than inflate it**.

One thing the probe *did* settle in the project's favour: Phase 1 had left Theorem 10 as `QUOTED` and had verified Theorem 16 only on `e = 2` data. Both are now corroborated at `e = 3` (§7). That is a strengthening of the audit, not a research result.

---

## 1. The question, stated precisely

| Item | Specification |
|---|---|
| Prime and field | `p` prime, `q = p^m`, `F = F_{q²}`, conjugation `c ↦ c^q` |
| Ring | `R_e = F_{q²}[u]/(u^e − 1)`, `e ≥ 1`, with **`e \| (q + 1)`** (the source's hypothesis); `gcd(e,p) = 1` holds automatically because `p \| q` |
| Structure | `R_e ≅ ∏_{j=0}^{e−1} F_{q²}` via `u ↦ β_j`, the `e`-th roots of unity in `F_{q²}`; CRT idempotents `e_j = (1/e) Σ_t β_j^{−t} u^t` |
| Length | `n ≥ 1` arbitrary, **repeated roots allowed** (`gcd(n,p) > 1`); no constraint `gcd(n,q) = 1` is imposed |
| Code family | `λ`-constacyclic codes over `R_e` of length `n`: ideals of `R_e[x]/(x^n − λ)` |
| Multipliers | `λ ∈ R_e^*`; write `λ = Σ_j e_j α_j` with `α_j = λ(β_j) ∈ F_{q²}^*`. The `α_j` are **not** required to be equal, and `λ` is a unit iff every `α_j ≠ 0` |
| Duality convention | Hermitian with the **ring** involution `y ↦ y^q` (the source's `⟨x,y⟩_H = Σ_i x_i y_i^q`, p. 4–5). Because `q ≡ −1 (mod e)`, this involution is `u ↦ u^{−1}` together with coefficient conjugation `c ↦ c^q` — a **conjugate-reciprocal**, *not* a coefficientwise Frobenius. (For `e = 2` the two coincide; for `e ≥ 3` they are different forms and only the first is the paper's.) |
| Dual | `C^{⊥H} = {x ∈ R_e^n : ⟨x,c⟩_H = 0 for all c ∈ C}` |
| Admissibility | `C` is **dual-containing** (DC) if `C^{⊥H} ⊆ C` |

**The question R3 would ask.** For fixed `(p, q, e, n, λ)` compute

```
N(n, λ)      = #{ λ-constacyclic codes C over R_e : C^{⊥H} ⊆ C } ,
N(n, λ; j)   = #{ such C with dim_{F_{q²}} Hull_H(C) = j } ,   Hull_H(C) = C ∩ C^{⊥H},
```

and describe how `N(n, λ; j)` depends on `n`, `e` and the decomposition `λ = Σ e_j α_j`.

Two conventions must be fixed or the question is not well posed, and both are settled in §2: what is being counted (codes, not generator listings), and whether equivalence is quotiented out (it is not).

---

## 2. What exactly is being counted

**(a) Generator descriptions — the wrong object.** The source writes `C = η₁C₁ ⊕ … ⊕ η_eC_e` with the printed `η_i = (u^e − 1)/(u − μ^{i−1})`. Phase 1 finding **F-1** established that the printed `η_i` are **not idempotents** (`Σ η_i = 3u²` for `e = 3`): each is a nonzero scalar multiple `η_i = λ_i e_i`. Because `η_i C_i = e_i C_i` for `F_{q²}`-linear `C_i`, no *result* of the paper is affected — but a count taken over printed tuples `(η_i, C_i)` would be wrong by the number of admissible rescalings, and the tuples are not in bijection with codes. **R3 must count ideals, never `(g₁,…,g_e)` listings.** This is the single most likely way to obtain a spurious "new" enumeration.

**(b) Ideals / codes — the right object.** `R_e[x]/(x^n − λ)` is a principal ideal ring (a quotient of a product of PIDs), so every ideal is principal; the CRT gives a bijection

```
{ λ-constacyclic codes over R_e }  ⟷  ∏_{j} { α_j-constacyclic codes of length n over F_{q²} } .
```

Counting ideals is well defined, and it is what §3 reduces.

**(c) Equivalence classes — not part of R3.** Monomial equivalence over `R_e` (or over the Gray image) is a genuinely harder quotient; no enumeration method exists in the accessible literature, the source's tables do not use it, and the existing field-level counting papers (Sangwisut et al.; Debnath–Prakash) count codes, not classes. Adopting classes would change the question rather than sharpen it, and would remove the comparability with prior art that Gate 2 needs.

---

## 3. The counting function and the exact constituent relationship

**Proposition (componentwise duality).** Let `e_j` be the CRT idempotents of `R_e`, `e | q+1`, and let `C = ⊕_j e_j C_j`. Then

```
C^{⊥H} = ⊕_j e_j · (C_j^{⊥H})            and therefore
C^{⊥H} ⊆ C   ⟺   C_j^{⊥H} ⊆ C_j  for every j .
```

*Proof.* Under `q ≡ −1 (mod e)`, applying the involution to `e_j = (1/e) Σ_t β_j^{−t}u^t` gives `(1/e) Σ_t β_j^{t}u^{−t} = (1/e) Σ_s β_j^{−s}u^{s} = e_j`, so **the involution fixes every idempotent**. Hence for `x = Σ_j e_j x^{(j)}`, `y = Σ_m e_m y^{(m)}`,

```
⟨x,y⟩_H = Σ_i Σ_{j,m} e_j e_m x_i^{(j)} (y_i^{(m)})^q = Σ_j e_j ⟨x^{(j)}, y^{(j)}⟩_F ,
```

a sum in the product ring, so it vanishes iff every component vanishes; and `x` ranges over the dual freely in each component. ∎

**Consequence — the count is a product.**

```
N(n, λ) = ∏_{j=0}^{e−1} N_F(n, α_j),        N_F(n, α) = #{ α-constacyclic codes over F_{q²} with C^{⊥H} ⊆ C }.
```

`N_F(n, α)` is elementary: the `α`-constacyclic codes of length `n` over `F_{q²}` correspond to the monic divisors `g | x^n − α`, and `C^{⊥H} ⊆ C` is a condition on the index pairs in the factorisation of `x^n − α` (the `b_ij + c_ij ≤ p^v` condition of the source's Theorems 15/16, which is exactly what the field-level papers count).

**So R3 asks for a product of `e` copies of a function that is (i) elementary and (ii) already in the literature (§4).** There is no interaction between the components, hence nothing for a "joint distribution" to say beyond the product.

---

## 4. Closest prior results, separated by evidence strength

| Result | What it gives | Evidence class |
|---|---|---|
| **Source, Theorem 15** (p. 13) | `C^{⊥H} ⊆ C ⟺ C₁^{⊥H} ⊆ C₁ and C₂^{⊥H} ⊆ C₂` for `R₂` — stated **in the proof**, i.e. the componentwise criterion is already the paper's own tool | **Full text** (Phase 1, `S1-T15`, VERIFIED) |
| **Source, Theorem 16** (p. 14) | Same criterion for `R_e`, all `1 ≤ l ≤ e` | **Full text**; Phase 1 verified it only on `e = 2` data. The probe in §6 verifies it at `e = 3` as well |
| **Source, Theorem 10** (p. 12–13) | `dim Hull_H(C) = Σ_l (component hull contributions)` for `R_e` | **Full text**; Phase 1 had recorded this as `QUOTED`. Now corroborated at `e = 2` and `e = 3` (§7) |
| **Sangwisut, Jitman, Ling, Udomkavanich (2015)**, Thms 22–23 | codes of cyclic/negacyclic type enumerated by hull dimension | **Secondary, verified sentence**: Lu et al. (2026) state that *"codes have been enumerated by hull dimension, for cyclic and negacyclic codes [34, Thms. 22 and 23]"* |
| **Lu, Yang, Liu, Fu, Guo, arXiv:2607.12242 v3** | exact counts of cyclic codes by hull codimension (product enumerator, App. B) | **Full text positioning section read** |
| **Debnath & Prakash, *Cryptogr. Commun.* (2022/23)** | *"the number of constacyclic codes of length n over F_q is calculated for a given Galois hull dimension"* — i.e. the field-level `N_F` | **Abstract only — blocker B-2** |
| **arXiv:2605.29204 (2026)** | `A^H_{n,k,ℓ,q²}` for all `[n,k]` codes over `F_{q²}` | **Abstract only** |
| **Debnath & Prakash, ICTIS 2025 / SIST 325** | ring-level count for the **chain** ring `Z_{p³}` | **Abstract only** |

**No novelty is claimed here, and none can be while B-1 (publisher bodies unreadable) and B-2 (Debnath–Prakash body unread) stand.** What the accessible evidence does establish is weaker and sufficient for the verdict: *the componentwise structure is the source's own*, so a product count over `R_e` is a consequence of a theorem already in the paper being extended.

---

## 5. The kill criterion — stated in advance, and fired

R3 would be non-novel, or reduced to a routine consequence, if any of the following held:

| # | Criterion | Status |
|---|---|---|
| **K1** | An existing theorem gives `C^{⊥H} ⊆ C ⟺` (componentwise conditions) for general `e` | **FIRED** — the source's Theorem 16, and its proof of Theorem 15 for `e = 2` |
| **K2** | The involution fixes the CRT idempotents, so the form splits as a sum over components | **FIRED** — proved in §3; `u ↦ u^{−1} = u^{q}` fixes `e_j` for every `e \| q+1` |
| **K3** | A published enumerator already gives `N_F(n, α)` | **FIRED to the standard required** — Debnath–Prakash (abstract), Sangwisut et al. (cited), Lu et al. (full text) |
| **K4** | The only surviving content would be the *joint law*, which is the product | **FIRED** — §3 |

A single genuine failure of K2 (a ring where the idempotents are permuted, making the dual genuinely crossed) would have saved R3. §6 shows the cross-check designed to detect exactly that, and shows it does not occur under the paper's involution.

---

## 6. Smallest tractable test case and the reproducible counting strategy

**Method (CRT-free on the ring side).** For a given `(p, q, e, n, λ)`:

1. Take the field `F_{q²}` = `GF(p^{2m})` from a prime polynomial; the involution there is `x ↦ x^q`.
2. Take `R_e` with the ring involution `y ↦ y^q`, i.e. `u ↦ u^{−1}` plus coefficient conjugation.
3. Enumerate **every principal ideal** of `R_e[x]/(x^n − λ)` by running over all `g ∈ (R_e)^n` and taking the `F_{q²}`-span of `{u^a x^j g mod (x^n − λ)}`. *Every* ideal is principal (§2b), so this is exhaustive. Restricting to monic divisors of `x^n − λ` is **not** exhaustive over a ring with zero divisors — ideals such as `⟨e₁(x−1)⟩` have a non-unit leading coefficient (this was my first error; it is recorded in §8).
4. Compute `C^{⊥H}` by linear algebra straight from the paper's definition, and test `C^{⊥H} ⊆ C`.
5. Compare with `∏_j N_F(n, α_j)` computed independently by the field-level routine.

**Smallest case: `p = 3, q = 3, e = 2, n = 2`.** `|R₂| = 81`, `64` units, `gcd(n,p) = 1` (non-repeated-root), at most `16` ideals per multiplier. Anything smaller fails `e | q+1` or makes the field trivial.

**The case that could have broken the product: `p = 2, q = 2, e = 3, n = 2`.** `|R₃| = 64`, `27` units, three components, and `gcd(n,p) = 2` (repeated-root) — the regime where a naive argument is most likely to fail.

**Results (exhaustive, every ideal, every admissible multiplier):**

| Test | `λ` tested | `#ideals(R_e) = ∏ #ideals(F)` | `#DC(R_e) = ∏ #DC(F)` | `dim C = Σ dim C_j` and `DC(C) ⇔ ∀j DC(C_j)` |
|---|---|---|---|---|
| `q=3, e=2, n=2` | 64 / 64 | **64/64** | **64/64** | **64/64** |
| `q=2, e=3, n=2` | 27 / 27 | **27/27** | **27/27** | **27/27** |

A second, independent check builds every code from its CRT tuple and verifies that the **number of dual-containing codes** equals the product, and that the dual is exactly the assembly of the component duals: **16/16** and **27/27** exact matches. For `e = 3` the naive product is `2·2·2 = 8` and the true count is `8`; had the components been permuted by the involution the two would differ, and the check is sensitive to that (it reported `12 ≠ 8` under the *wrong* involution — see §8).

**Reproduce:**

```
python3 research_project/phase2/r3_probe/r3_probe.py          # ~14 s
python3 research_project/phase2/r3_probe/r3_dual_formula.py   # ~0.2 s
python3 research_project/phase2/r3_probe/r3_hull_dim_check.py # ~0.5 s
```

Output is archived verbatim in `research_project/phase2/r3_probe/r3_probe_log.txt`. Deterministic, stdlib only, no network.

---

## 7. What the probe also settles, and what it does not

**Settled (as data, not as proof):**

* The source's **Theorem 16** holds at `e = 3` on the tested ring — Phase 1 had only checked it against `e = 2` table rows.
* The source's **Theorem 10** (hull-dimension additivity), recorded `QUOTED` in Phase 1, holds **16/16 and 27/27** including `e = 3`. That is the first independent recomputation of that theorem in this project.

**Not settled:**

* General `e` and general `n`. Two rings, exhaustively enumerated, are strong but not a proof; the proof is the four-line argument in §3, and the probe is its check.
* Anything about equivalence classes (out of scope of R3 by §2c).
* `N_F(n, α)` in closed form — not needed for the verdict, since K3 already fires.

---

## 8. Errors made while producing this document (recorded, because the verdict rests on the probe)

| # | Error | Effect | Fix |
|---|---|---|---|
| E-1 | Enumerated ideals only through **monic divisors** of `x^n − λ` | Missed ideals with non-unit leading coefficients (`⟨e₁(x−1)⟩`); `e = 2` totals came out `5 ≠ 16` | Enumerate all `g ∈ (R_e)^n`; every ideal is principal |
| E-2 | RREF used `+=` instead of `−=` in the elimination step | Harmless in characteristic 2, wrong in characteristic 3; `q = 3` counts were garbage | Subtract; RREF re-tested for canonicity on random bases |
| E-3 | Used **coefficientwise** conjugation (`u^q = u`) instead of the paper's ring power (`u^q = u^{−1}`) | Produced a spurious result: at `e = 3` the DC count was `12` where the product gives `8`, i.e. an apparent failure of the source's Theorem 16 | Restored the paper's involution; the anomaly vanished (`27/27`), and the closed-form proof in §3 explains why |
| E-4 | Subspace intersection computed by keeping only basis vectors of `A` lying in `B` | Understated `Hull(C)`; the hull-additivity check read `15/27` | Proper kernel-based intersection; now `27/27` |

E-3 is the one that matters: it shows how easily a "new phenomenon" can be manufactured by picking the wrong involution. It also shows why the verdict below is stated with the form pinned down in §1.

---

## 9. Recommendation

**Do not authorise R3.** It is well-posed, and its answer is a product of known counts. Authorising it would produce either a restatement of the source's own Theorem 16 with a `∏` in front, or an enumeration whose novelty depends entirely on blockers B-1/B-2 being resolved in a direction that the accessible evidence contradicts.

**Options that do not collapse, and why they are not recommended now:**

1. **Monomial-inequivalence counts.** Genuinely non-product (the quotient does not commute with the CRT), but there is no machinery, no prior art to compare against, and it is far from the source's programme. If pursued it needs its own Gate 2, not an R3 relabel.
2. **The distribution of quantum parameters `[[en, 2k − en, ≥d]]` after the Gray map.** This *is* non-product in an interesting way: the count of codes factors, but the minimum distance is a minimum over the whole code, so a condition like `d ≥ 3` couples the components. It is the only variant of R3 with genuine content — but it is a distance-distribution problem, not a hull-enumeration problem, and it is substantially harder than anything in the source.
3. **R1 (repeated-root regime over `R_e`).** The only remaining candidate from the Phase 2 assessment. Note that this probe already shows the *dual-containing* part of the repeated-root regime behaves multiplicatively (T1 has `gcd(n,p) = 2` and still products exactly), so R1 too must be re-scoped to the **per-component** count, where the open question actually lives.

**Whether R3 is "sufficiently precise to be considered for authorisation": yes — the specification in §1–§3 is complete enough to hand to a researcher, and the test in §6 is decisive. That is precisely why the answer is negative.**

**Nothing in this document is a novelty claim.** Phase 3 remains not started and requires fresh authorisation.
