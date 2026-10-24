# R1 — Feasibility and novelty kill test

**Candidate question.** For `n = p^v n'` with `v ≥ 1`, enumerate `λ`-constacyclic codes over
`R_e` by Hermitian hull dimension and compare with the `v = 0` law.

**Scope of this document.** Kill test only. No Phase 3 work, no manuscript text, no Phase 1
deliverable modified. Written on branch `arena/831a2e65-galios-hull` from `c9d4517`.

**Verdict, stated up front: R1 is NO-GO.** Section 5 names the theorem that makes it routine.

---

## 1. Assumptions, stated precisely

| Item | Assumption |
|---|---|
| Base field | `F = F_{q²}`, `q` a prime power; `x ↦ x^q` is the field involution; `F^{q+1} = {a : a^{q+1} = 1}`. |
| Ring | `R_e = F_{q²}[u]/(u^e − 1)`, `e ≥ 2`, `e \| (q+1)`, so `u^q = u^{−1}` in `R_e`. `R_e ≅ ∏_{μ^e=1} F_{q²}` by CRT; `ε_ℓ` (source notation) / `e_ℓ` (normalised, Phase 1 finding F-1) are the idempotents. |
| Length | `n = p^v n'`, `p = char F`, `gcd(n', p) = 1`, `v ≥ 1` (the **repeated-root regime**). |
| Multiplier | `λ = Σ_ℓ η_ℓ α_ℓ ∈ R_e^*` with `α_ℓ ∈ F^*`; the code is `λ`-constacyclic, i.e. an ideal of `R_e[x]/(x^n − λ)`. |
| Duality | Hermitian: `⟨x, y⟩_H = Σ_i x_i y_i^q`, where `y ↦ y^q` is the **ring** power, i.e. the conjugate-reciprocal map `u ↦ u^{−1}` composed with field Frobenius. For `e ≥ 3` this is *not* coefficientwise. Same convention as R3 (`c9d4517`). |
| Hull | `Hull_H(C) = C ∩ C^{⊥_H}`; `dim` over `F_{q²}`; `C` dual-containing iff `C^{⊥_H} ⊆ C`. |
| Counting object | **Distinct codes**, i.e. distinct `F_{q²}`-subspaces of `R_e^n` closed under the constacyclic shift. Not generator descriptions, not exponent tuples. |
| Field case | `e = 1`; then `R_1 = F_{q²}` and everything below is field-level. |

Two structural facts carry the whole analysis and are used repeatedly:

* **(P1) PIR.** `R_e[x] ≅ ∏_ℓ F_{q²}[x]` is a product of PIDs, hence a principal ideal ring.
  Every ideal of `R_e[x]/(x^n − λ)` is principal, and `R_e[x]/(x^n − λ) ≅ ∏_ℓ F_{q²}[x]/(x^n − λ_ℓ)`.
  So codes over `R_e` ↔ tuples `(C_1, …, C_e)` of field-level `λ_ℓ`-constacyclic codes, bijectively.
* **(P2) Additivity, with no permutation.** The `q`-power **fixes every CRT idempotent**. With
  `e_μ = (1/e) Σ_j μ^{−j} u^j` and `q ≡ −1 (mod e)` (which follows from `e | q+1`), the coefficient
  Frobenius `μ^{−j} ↦ μ^{−jq} = μ^{j}` exactly cancels the basis permutation `u^j ↦ u^{qj} = u^{−j}`,
  so `e_μ^q = e_μ`. Each component is therefore stable, the `q`-power acts on the `ℓ`-th component
  as the field Frobenius of `F_{q²}`, and
  `Hull_H(C) = ⊕_ℓ Hull_H(C_ℓ)`, i.e. `dim Hull_H(C) = Σ_ℓ dim(C_ℓ ∩ C_ℓ^{⊥_H})`.

  Verified concretely over `F_4`, `e = 3` (`q = 2`, `μ ∈ {1, ω, ω²}`): `e_1 = (1,1,1)`,
  `e_ω = (1, ω², ω)`, `e_{ω²} = (1, ω, ω²)`, and in every case `e_μ^q = e_μ`. Note this is *not*
  trivial — `μ ↦ μ^q = μ^{−1}` does permute the labels — the point is that the coefficient twist
  cancels it.

  Consequence used throughout: `N_{R_e}(n, λ, ·)` is the product of the `e` field-level laws, with
  **no orbit bookkeeping** over component labels.

Beware a notation clash: the symbol `σ` is used below for a *different* permutation — the action of
the conjugate-reciprocal `†` on the irreducible factors of `x^n − α` inside `F_{q²}[x]`, which
genuinely can have 2-cycles. The two permutations must not be confused; the CRT one is trivial.

**Separating the two effects requested.** The factorisation of `x^n − λ` over `F_{q²}` is
`(x^{n'} − c)^{p^v}` where `c^{p^v} = α`; the repeated-root effect is entirely the multiplicity
`p^v` on a *squarefree* base `x^{n'} − c`. Nothing about it changes the ring's ideal structure (P1);
it changes only the exponent ranges on each irreducible factor. Any genuinely new counting result
would therefore have to come from the *counting* step, not from the factorisation.

---

## 2. Literature evidence

Evidence grades follow Phase 2's convention: **FULL TEXT** = statement read in the paper's own
text; **ABSTRACT** = abstract/snippet only, statement read verbatim but no theorem body; **U** =
unresolved. No novelty claim is made anywhere in this document.

### 2.1 The source paper (authoritative; full text verified in Phase 1)

| Theorem | Content | Relevance to R1 |
|---|---|---|
| **Theorem 8** (p. 9–10) | `C = ε_1C_1 ⊕ ε_2C_2` over `R_2`; `dim Hull_H(C) = Σ_{j∈Ω} ord_j(q²)a_j + Σ_{j∈Ω'} ord_j(q²)b_j` with `0 ≤ a_j ≤ 2γ(j)⌊p^v/2⌋`, `0 ≤ b_j ≤ 2β(j)p^v`. Proof gives `Hull_H(C) = ⟨ε_1 lcm(g_1, ((x^n−α)/g_1)^†), ε_2 lcm(g_2, ((x^n−α)/g_2)^†)⟩`. | **Already the repeated-root case.** The bounds contain `p^v`; no coprimality hypothesis anywhere. | FULL TEXT |
| **Theorem 10** (p. 12–13) | Same for general `e`: `dim Hull_H(C) = Σ_{l=1}^e (Σ_{j∈Ω_l} ord_j(q²)a_{(l)j} + Σ_{j∈Ω'_l} ord_j(q²)b_{(l)j})`, `0 ≤ a_{(l)j} ≤ γ_l(j)⌊p^v/2⌋`, `0 ≤ b_{(l)j} ≤ β_l(j)p^v`. | **R1's answer at the level of one code, over `R_e`, for arbitrary `p^v`.** | FULL TEXT |
| Theorem 11 / Corollary 12 | `gcd(n,p) = 1`; `D_{q²}(n) = {0} ⟺ n/r ∈ S_{q²}`; LCD criterion over `R_2`. | Assumes `v = 0`. | FULL TEXT |
| Theorem 13 / Corollary 14 | Same over `R_e`. | Assumes `v = 0`. **This is the only textual gap R1 could point at.** | FULL TEXT |
| Theorem 15/16/18 | dual-containing criterion; `[[en, 2k−en, ≥d]]_q`. | Used in §4.3; already shown to factor per component in R3. | FULL TEXT |

Note the shape of Theorems 8/10: the hull dimension is a **linear form in integer invariants
`a_j, b_j` that live one per conjugate-reciprocal orbit**, with box bounds. That is the fact that
decides R1 in §5.

### 2.2 Field-level and repeated-root literature

| Reference | Content | Grade |
|---|---|---|
| Sangwisut, Jitman, Udomkavanich, *Adv. Math. Commun.* **11**(3):595–613 (2017), DOI `10.3934/amc.2017045`, arXiv:1601.00144 | Factorisation algorithm for `x^n − λ` over `F_{q²}`; **determines the dimensions of Hermitian hulls of `λ`-constacyclic codes of length `n` over `F_{q²}`**; characterises and enumerates Hermitian self-dual and complementary-dual cases. No `gcd(n,q) = 1` hypothesis in the abstract framing. | ABSTRACT |
| Jitman, Sangwisut, *Adv. Math. Commun.* **12**(3):451–463 (2018) | *Average* Hermitian hull dimension of constacyclic codes over `F_{q²}`, with bounds and a table over `r ∈ M_q`, `n ∈ M_q`. | ABSTRACT |
| Dinh, *FFA* (2011), length `2p^s` | Structure of repeated-root constacyclic codes and their duals; all self-dual negacyclic codes. | SNIPPET |
| Dinh, *Discrete Math.* **313**:983–991 (2013), length `3p^s` | Full classification tables by `p^m mod 3` and `λ`; sizes `p^{m(3p^s−i−2j)}`; §7 duals `C^⊥ = ⟨(x−1)^{p^s−i}(x²+x+1)^{p^s−j}⟩`. | SNIPPET |
| Chen, Dinh, Liu, *FFA* **33**:137–159 (2015), length `2ℓ^m p^n` | Structure + duals; **characterisation and enumeration of all LCD and self-dual** repeated-root constacyclic codes. | SNIPPET |
| Sharma, *Cryptogr. Commun.* (Springer), length `ℓ^t p^s` | Structure and duals, `ℓ ≡ 1 mod 2`, `ℓ ≠ p` primes. | ABSTRACT |
| Dinh, Dinh, Vo, *FFA* **43** (2017), length `p^s` over finite **chain** rings | `R[x]/⟨x^{p^s} − λ⟩` is a chain ring; structure, sizes, duals. | ABSTRACT |
| *FFA* (2024), length `k^s l^m p^n` | `x^{k^s l^m p^n} − λ` explicitly factorised; **all** repeated-root constacyclic codes and their duals characterised. | ABSTRACT |
| Debnath, Prakash, Islam, *Cryptogr. Commun.* **15**:111–127 (2023), DOI `10.1007/s12095-022-00591-6` | Galois hulls of `λ`-constacyclic codes over `F_q`: dimension formula, **and the number of constacyclic codes of length `n` with a given Galois hull dimension, "considering some restrictions on q"**. Body not read (**blocker B-2**). | ABSTRACT |
| Debnath & Prakash, *SIST* **325**:309–319, DOI `10.1007/978-981-95-1365-9_25` (ICTIS 2025) | *Hulls of Cyclic Codes Over a Local Ring*: hull generators, LCD condition, and a count of all cyclic codes for a fixed `p`-dimension of the hull, over the chain ring `Z_{p^3}`. Body not read. | ABSTRACT |

**Blockers.** **B-1**: publisher full texts (ScienceDirect, Springer, AIMS) remain inaccessible, so
every row above except the source paper is ABSTRACT or SNIPPET — per Phase 2 rules this bounds no
absence claim. **B-2**: Debnath–Prakash body text still unobtainable.

> **Correction (2026-10-24).** This table previously carried a single row whose citation conflated two
> different papers: it gave the *Cryptogr. Commun.* DOI together with the *SIST* volume/pages and the
> description "hulls over affine algebra rings". The DOI `10.1007/s12095-022-00591-6` belongs to
> Debnath, Prakash & **Islam**, *Galois hulls of constacyclic codes over finite fields*, *Cryptogr.
> Commun.* **15**:111–127 (2023) — a **finite-field** paper with **three** authors; the *SIST*
> 325:309–319 entry is a separate paper (ICTIS 2025, *Hulls of Cyclic Codes Over a Local Ring*,
> DOI `10.1007/978-981-95-1365-9_25`) about a **chain** ring `Z_{p^3}`. The rows are now separated.
> No verdict changes: `LITERATURE_COMPARISON_MATRIX.csv` rows 10 and 12 had both entries correctly and
> were already consistent with this correction; the error was confined to this summary table. R1's own stated kill criterion
in `NOVELTY_ASSESSMENT.md` §5 was *"if Debnath & Prakash (2022/23) already covers `p \| n` and their
count composes over the `e` components"* — that specific condition **cannot be evaluated** on the
available evidence. Section 5 therefore does **not** rely on it.

---

## 3. The proposed counting statement, and what it follows from

### 3.1 What R1 would have to prove

For fixed `q, e, n` and admissible `λ`, produce the function
`N_{R_e}(n, λ, d) = #{ C ⊆ R_e^n : C is λ-constacyclic, dim Hull_H(C) = d }`,
with `p \| n`, and show it differs from the `gcd(n,p) = 1` law in a way not already written down.

### 3.2 Reduction to the field, and to one orbit

By (P1) plus (P2),

```
N_{R_e}(n, λ, ·)  =  prod_{l=1..e} ( field-level law for the l-th component )
                     for the corresponding tuple coordinates,
```

because the components are independent (`λ_ℓ` free in `F^*`) and the hull dimension is additive,
with no permutation of components (P2). So the ring level contributes **no counting content at all**
beyond multiplying the published field-level laws. This is the same mechanism that closed R3.

It remains to ask whether the *field-level* law at `p | n` has new content. Write
`x^n − α = g_1^{p^v} ⋯ g_s^{p^v}` with the `g_i` distinct monic irreducibles of degree `m_i`, and
let `σ` act on `{g_i}` by `g ↦ g^†` (conjugate-reciprocal). A monic divisor is `∏ g_i^{a_i}`,
`0 ≤ a_i ≤ p^v`, the code is `C = ⟨∏ g_i^{a_i}⟩`, and

```
dim Hull_H(C) = Σ_{fixed i}  m_i · min(a_i, p^v − a_i)
              + Σ_{2-cycles {i,j}}  m_i · min(a_i + a_j, 2p^v − (a_i + a_j)).
```

*Fixed-point case, with proof.* If `g^† ∝ g` and `x^n − α = g^{p^v}`, then `C = ⟨g^a⟩` inside
`F[x]/(g^{p^v})`, `C^⊥ = ⟨g^{p^v−a}⟩`, so `Hull_H(C) = ⟨g^{max(a,p^v−a)}⟩` and
`dim = n − m·max(a, p^v − a) = m·min(a, p^v − a)`. This is exactly the source's lcm formula
(Theorem 8's proof) evaluated in the single-factor case.
*Two-cycle case.* The same lcm formula with `g_i^† ∝ g_j` gives, after the substitution
`s = a_i + a_j`, `dim = n − m·max(s, 2p^v − s)`. Verified below, not proved here in general.

Consequently the field-level distribution is a **product over orbits of small univariate
polynomials in a formal variable `z`**:

```
fixed orbit  :  P_i(z) = Σ_{a=0}^{p^v} z^{m_i·min(a, p^v−a)}
2-cycle      :  P_{ij}(z) = Σ_{a,b=0}^{p^v} z^{m_i·min(a+b, 2p^v−a−b)}
```

and the number of codes is the evaluation at `z = 1`, i.e.
`N(n, α) = ∏_{orbits} (p^v + 1) = (p^v + 1)^{#orbits}`.

The whole content of "the repeated-root hull-dimension distribution" is therefore a lattice-point
count in the boxes of Theorem 10, with a product form forced by independence of the per-factor
exponents. **Section 4 tests whether that product form is actually what happens**; §5 draws the
conclusion.

**Nothing above is claimed as a theorem for general `q, n`.** The fixed-orbit formula is proved;
the two-cycle formula and the product over orbits are verified on the exact cases in §4.

---

## 4. Smallest nontrivial exact test cases, `p | n`

Code: `research_project/phase2/r1_probe/r1_probe.py` and `r1_orbit_check.py`;
archived output `r1_probe_log.txt` (185 lines). Pure Python, stdlib only, ASCII only.
Duality convention: Hermitian as in §1; `y ↦ y^q` implemented as the ring power.

### 4.1 Case A — `q = 3`, `n = 3 = p`, `F = F_9` (smallest repeated root at all)

Per `α ∈ F_9^*`, exactly **4** `α`-constacyclic codes (divisors of `(x−c)³`; `p^v = 3`, one orbit,
`(3+1)^1 = 4`).

| `α` | hull-dim distribution | count of codes |
|---|---|---|
| 1, 2, 3, 6 | `{0: 2, 1: 2}` | 4 |
| 4, 5, 7, 8 | `{0: 4}` (all LCD) | 4 |

**Independent verification of exhaustiveness.** All subspaces of `F_9³` were enumerated from
scratch — **184** subspaces, which is the Gaussian binomial
`Σ_k [3 choose k]_9 = 1 + 91 + 91 + 1` — and each was tested for `α`-constacyclicity. This
reproduced the count **and** the hull-dimension distribution for **8/8** values of `α`. So the
monic-divisor enumeration is exhaustive here, and the hull dimensions are confirmed without using
any generator description. (Contrast R3: over a ring with zero divisors, monic divisors are *not*
exhaustive; over a field at `n = p` they are, and this is now checked, not assumed.)

**Lcm cross-check.** For all **32/32** codes, `dim Hull_H(C) = n − deg lcm(g, ((x^n−α)/g)^†)`
reproduces the subspace-computed answer — i.e. the source's own hull formula is confirmed on this
case, including the multiplicity.

### 4.2 Case B — `q = 3`, `n = 6 = 2·3`, `F = F_9` (mixed orbits, 2-cycles occur)

`x^6 − α = (x² − c)³`. `x² − c` is either two linear factors (2 fixed orbits) or one irreducible
quadratic (1 fixed orbit), and for some `α` the two linear factors are interchanged by `†`
(a 2-cycle).

| `α` | #codes | hull-dim distribution |
|---|---|---|
| 1, 2 | 16 | `{0: 4, 1: 8, 2: 4}` |
| 3, 6 | 16 | `{0: 2, 1: 4, 2: 6, 3: 4}` |
| 4, 5, 7, 8 | 4 | `{0: 4}` |

`16 = (3+1)^2`, `4 = (3+1)^1`: the count formula holds. `α = 3, 6` are the 2-cycle cases (the
richest distributions; hull dimension reaching 3 means self-dual codes occur). Lcm cross-check:
**80/80** codes agree.

**Dual-containing codes and parameters.** These are **field-level** codes (`e = 1`), so the
applicable construction is the elementary Hermitian one, `[[n, 2k − n, ≥d]]_q` over `F_q = F_3`
with `k` the `F_9`-dimension of `C` — *not* the source's ring-level `[[en, 2k − en, ≥d]]` of
Theorem 18, which would apply to codes over `R_e`. Recorded to make the duality convention and the
distance computation checkable, not as a parameter claim.

| `α` | `k` | hull | `d` | `[[6, 2k−6, ≥d]]_3` |
|---|---|---|---|---|
| 1, 2, 3, 6 | 6 | 0 | 1 | `[[6,6,≥1]]` (trivial) |
| 1, 2, 3, 6 | 5 | 1 | 2 | `[[6,4,≥2]]` |
| 1, 2, 3, 6 | 4 | 2 | 2 | `[[6,2,≥2]]` |
| 3, 6 | 3 | 3 | 2 or 3 | `[[6,0,≥2]]`, `[[6,0,≥3]]` (self-dual; degenerate) |

Minimum distances were computed exactly by exhaustive search over the codewords of each enumerated
code — no bound and no table lookup. The `[[6,0,·]]` entries are degenerate and are recorded only to
show that the repeated-root regime produces them. **No claim is made that any of these parameters is
new.**

### 4.3 The product-form check (`r1_orbit_check.py`)

`P_i(z)` and `P_{ij}(z)` of §3.2 were built from the actual irreducible-factorisation and the actual
`σ`, multiplied out, and compared with the enumeration:

| Case | `q` | `n` | `p^v` | `α` tested | matched |
|---|---|---|---|---|---|
| A | 3 | 3 | 3 | 4 | **4 / 4** |
| B | 3 | 6 | 3 | 4 | **4 / 4** |
| C | 2 | 2 | 2 | 3 | **3 / 3** |
| D | 3 | 9 | 9 | 4 | **4 / 4** |
| E | 2 | 4 | 4 | 3 | **3 / 3** |
| F2 | 2 | 8 | 8 | 3 | **3 / 3** |
| G | 2 | 6 | 2 | 3 | **3 / 3** |
| | | | | | **24 / 24** |

Distributions agree *exactly*, not merely in total. Two illustrative rows:

* `q=3, n=9` (multiplicity `9`, one orbit): `{0:2, 1:2, 2:2, 3:2, 4:2}` — ten codes, all ten
  dimensions `0…9` present, hull dimension peaking at `⌊9/2⌋ = 4`.
* `q=2, n=6` with `x³ − c` irreducible (one orbit of degree 3, multiplicity 2): `{0:2, 3:1}` —
  only three codes, and the two non-trivial ones have hull dimension exactly 3.

Interpretation: the repeated-root regime produces *different distributions* from `gcd(n,p)=1`
(hull dimensions spread up to `⌊n/2⌋`, LCD is no longer automatic) but the distribution is a
**mechanical product over conjugate-reciprocal orbits**, i.e. a lattice-point count in exactly the
boxes that Theorem 10 states. That is the diagnostic that fired for R3, and it fires here.

### 4.4 Tool bugs found and fixed (transparency)

| # | Bug | Effect | Fix |
|---|---|---|---|
| T-1 | Call site took `_, h = divmod_(f, g)`, i.e. the **remainder** as `h`; and `Pol.divmod_` does not trim/normalise the remainder, so `h` came back as `[0]`, making `Pol.dagger` raise `StopIteration` on `a[0] = 0`. Also `g` was recovered from RREF by enumeration (`key_to_poly`) and could be non-monic. | R1-c crashed; earlier R1-c output is void. | Carry `(α, g)` directly through the enumeration; take `h, _ = divmod_`; verify `g·h = x^n − α` on every divisor (32/32 and 80/80). |
| T-2 | `all_subspaces` iterated over `k·#free` slots but only used the slots with `fc > piv[row]`, so subspaces were generated many times. | Reported "488 subspaces"; the true count is **184**. | Iterate over the slots actually used. The code counts had been deduplicated by RREF so they were unaffected — but the stated total was wrong and is corrected here. |
| T-3 | `divisors()` brute-forces every monic polynomial of degree `≤ n` over `F`: `O(Q^n)`. | `n = 9` never finished (silent 900 s timeout). | Enumerate structurally as `∏ g_i^{a_i}, 0 ≤ a_i ≤ p^v` (exhaustive by unique factorisation), and keep the brute-force list as an **assertion** for `n ≤ 6`. The two agree on all small cases. |
| T-4 | First version of the orbit product used `v` (the exponent) instead of `p^v` (the multiplicity). | 0/11 matched, all MISMATCH. | `mult = p**v`. Recorded because it shows the check does catch a plausible-looking error. |

A silent timeout of `timeout 900` produced an *empty* log with exit code 0 (the pipe's status);
logs are now written directly with `>`, not through a pipe, and line counts are checked.

---

### 4.5 One error of my own, caught and corrected in this document

While drafting §1 I asserted that the `q`-power permutes the CRT components by `μ ↦ μ^{−1}` and that
duality therefore has to be handled per `σ`-orbit of component labels. **That was wrong.** The
coefficient Frobenius cancels the label permutation exactly, so every idempotent is fixed; the
concrete `F_4`, `e = 3` computation in §1 (`e_μ^q = e_μ` for all three `μ`) settled it. The
correction makes the ring-level reduction *stronger* (a plain product, not an orbit product) and
does not change the verdict. The reason it is recorded: it is the same class of error as R3's
wrong-involution bug (E-3 in `R3_DECISION.md`), and both were caught only by computing the
involution explicitly rather than reasoning about it.

Note that `R3_DECISION.md` and `PHASE_STATUS.md` had this right ("the involution fixes every CRT
idempotent"); the error was mine in this document, not a defect in the earlier record.

## 5. Decisive kill criterion — the theorem that makes R1 routine

**K-R1. R1 is routine because of Theorem 10 of the source paper, combined with the CRT/PIR
decomposition (P1).**

Restated as the criterion R1 would have had to survive:

> If the Hermitian hull dimension of a `λ`-constacyclic code over `R_e` is already given, for
> arbitrary `p^v`, as a linear form in integer invariants indexed by conjugate-reciprocal orbits,
> with explicit box bounds; and if the CRT decomposition makes codes over `R_e` tuples of field-level
> codes with additive hull dimension — then counting codes by hull dimension is a lattice-point
> count in those boxes, and R1 is a corollary, not a discovery.

Both halves hold, and both are **full-text verified in the authoritative source**:

1. **Theorem 10 (p. 12–13)** states, for general `e` and with no coprimality hypothesis,
   `dim Hull_H(C) = Σ_{l=1}^e (Σ_{j∈Ω_l} ord_j(q²)a_{(l)j} + Σ_{j∈Ω'_l} ord_j(q²)b_{(l)j})`
   with `0 ≤ a_{(l)j} ≤ γ_l(j)⌊p^v/2⌋`, `0 ≤ b_{(l)j} ≤ β_l(j)p^v`. This is the repeated-root
   answer for a single code. The invariants are indexed by orbits, and the boxes are explicit.
2. **Theorem 8's proof** supplies the operative formula
   `Hull_H(C) = ⟨ε_1 lcm(g_1, ((x^n−α)/g_1)^†), ε_2 lcm(g_2, ((x^n−α)/g_2)^†)⟩`, which is what
   §3.2 specialises; §4.1–4.2 confirm it numerically on repeated roots.
3. **(P1)** plus **(P2)** `R_e[x] ≅ ∏_ℓ F_{q²}[x]`, with the `q`-power fixing every idempotent, turns
   the ring level into a plain product of the `e` field-level laws; no ring-level counting content
   survives (§3.2, and R3 in `c9d4517` for the same mechanism).
4. **Sangwisut–Jitman–Udomkavanich (AMC 2017)** independently determines Hermitian hull dimensions
   of `λ`-constacyclic codes over `F_{q²}` without a `gcd(n,q) = 1` restriction — corroboration at
   ABSTRACT grade only, and **not needed** for the kill: (1)–(3) already suffice.

Consequences, stated without inflation:

* The **only** textual gap R1 could claim is that the source's LCD criteria (Theorems 11/13,
  Corollaries 12/14) are stated under `gcd(n,p) = 1`. Filling that gap means substituting
  `a_{(l)j}` from Theorem 10 and observing that for `p | n` the set of achievable dimensions is no
  longer `{0}` — a line of algebra, in the same paper, from a theorem that already covers `p^v > 1`.
  §4.1 gives the explicit instance (`q=3, n=3`: LCD for `α ∈ {4,5,7,8}`, not for `α ∈ {1,2,3,6}`).
* The distribution **does** change with `v` (§4.1 vs §4.3), so a "comparison with the `v=0` law" is
  *true*, but it is *routine*: it is the evaluation of a product of geometric-type polynomials.
  Per the blueprint, "the joint enumerator is a product of known laws" is precisely the trap.
* R1's own originally stated kill criterion (Debnath–Prakash covering `p | n` and composing over the
  `e` components) is **not evaluable** (blockers B-1, B-2). The kill above is stronger, because it
  does not depend on the literature at all: it depends only on the source paper's Theorem 10.

**R1 verdict: NO-GO.** It is `K` (known or routine), not `N2`.

---

## 6. R1 versus R2, and the strongest defensible question

| | R1 — repeated-root distribution | R2 — differing multipliers `α_ℓ` |
|---|---|---|
| Status after this turn | **NO-GO** (`K`) | **untested** |
| What kills / would kill it | Theorem 10 + CRT: it is a lattice-point count in the source's own boxes | the decomposition-uniqueness lemma: if `λ`'s decomposition into `Σ η_ℓ α_ℓ` is unique up to unit multiplication, the question degenerates; if it is *not* unique, the question may be ill-posed rather than new |
| Content beyond a product of field laws | none — verified 24/24 that the product form is exact | potentially: the literature has a single multiplier per code; the count could depend on the decomposition, which is ring-level structure not visible over a field |
| Honest confidence | high — needs no literature | low — the decisive computation has not been done |

**R1 versus R2 on surviving content.** After §5, R1's surviving content is essentially zero: the
one thing the source does not state (`D_{q²}(n)` for `p | n`) is obtained by substituting into
Theorem 10, and the resulting distribution is a product over orbits that the probe reproduces
exactly on seven independent parameter sets.

**The strongest defensible question that remains** is R2, in this precise form:

> Fix `λ ∈ R_e^*` with `e ≥ 3` and `λ = Σ_{ℓ=1}^e η_ℓ α_ℓ`. Determine the number of admissible
> decompositions of `λ` up to unit multiplication in `R_e^*`, and — for those `λ` with more than one
> inequivalent decomposition — whether the hull-dimension distribution over the `e` CRT components
> depends on the decomposition chosen, or only on the multiset `{α_ℓ}`.

This is the only one of R1/R2/R3 whose content is not a product of field-level laws, because the
coupling it asks about (which `λ` admit which component tuples) has no field-level counterpart.
It is **not** claimed novel — B-1 and B-2 remain open, and per Phase 2 rules no absence claim is
available.

**It must not be assumed to survive.** Two failure modes are live and cheap to test:
(a) if `λ ↦ (α_1, …, α_e)` is a bijection up to permutations and units, R2 collapses to bookkeeping
and should be rejected before Phase 3 (this is the "short computation" already flagged in
`NOVELTY_ASSESSMENT.md` §5); (b) the answer may be invariant in the decomposition, in which case
R2 has no content beyond R1 and dies with it.

**Recommendation.** Report R1 as NO-GO. Before any Phase 3, settle R2's uniqueness lemma — it is a
short, exact computation over the same `R_e` machinery already validated in R3 and here, and it is
the only remaining route to a Gate 2 pass. If it degenerates, the honest conclusion is that all
three revisions are `K` and Gate 2 cannot be passed by this line of attack; that conclusion should
then be reported to the author rather than worked around.

---

## 7. Deliverables and reproduction

| Path | Content |
|---|---|
| `phase2/r1_probe/r1_probe.py` | Field-level enumeration (monic divisors), brute force over **all** subspaces of `F^n` (case A), lcm cross-check, hull distributions, dual-containing table with exact minimum distances. |
| `phase2/r1_probe/r1_orbit_check.py` | Independent factorisation + `σ`-orbits; product-form prediction; seven parameter sets. |
| `phase2/r1_probe/r1_probe_log.txt` | Archived output, 185 lines, generated `2026-10-23`. |
| `phase2/R1_FEASIBILITY.md` | This document. |

Run from the repository root:

```
python3 research_project/phase2/r1_probe/r1_probe.py
python3 research_project/phase2/r1_probe/r1_orbit_check.py
```

Total runtime under one minute. All asserted equalities (structural vs brute-force divisor lists
for `n ≤ 6`; `g·h = x^n − α` for every divisor; prediction vs enumeration) are hard `assert`s /
explicit `MATCH`/`MISMATCH` lines, not silent checks.

---

## 8. Verdict

| Question | Answer |
|---|---|
| Is the counting statement derivable? | Yes, routinely — from Theorem 10 of the source plus CRT multiplicativity. |
| Does the repeated-root regime add new structure? | It changes the distribution (hull dimensions spread to `⌊n/2⌋`; LCD is not automatic), but only as a lattice-point count in the source's own boxes: 24/24 exact matches to the product form. |
| Is R1 novel on the available evidence? | No claim of novelty is possible, and none is needed: R1 follows from a theorem in the paper it would extend. |
| **R1 decision** | **NO-GO.** |

No Phase 3 work has been started; no Phase 1 deliverable has been modified; no novelty is claimed
anywhere in this document. Awaiting explicit authorisation before any further phase.

---

## Addendum — correction to the citation audit, already discharged

`PHASE_STATUS.md` row **P2-R2** previously flagged `[50, 51, 52, 55, 56, 57, 60, 68, 72]` as
"cited but absent from the list". Those nine are `[n,k,d]` / `[[n,k,≥d]]` code-parameter cells in
Tables 2–3, not citations. The retraction was already recorded in `c9d4517`; it is restated here
only so this document's numerical reading of the tables (§4.2) is not confused with it.

Confirmed this turn, as a by-product of reading the tables: the reference list contains exactly
`[1]`–`[48]` with no gaps and no duplicates. The full citation audit (cited/orphan counts) recorded
in `REFERENCE_VERIFICATION_REPORT.md` is **not** re-run here — per the standing instruction not to
repeat completed Phase 2 work — and the present document makes no new claim about it. Note also
that a naive `\[[0-9]+\]` regex over the body text matches only 22 of the 48 numbers, because
citations in the extracted text are frequently grouped or split across line breaks; that
regex-level count is an artefact of extraction and is *not* evidence of orphan references.
