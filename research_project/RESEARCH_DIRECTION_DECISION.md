# RESEARCH_DIRECTION_DECISION

**Date:** 2026-10-20 · **Basis:** `INDEPENDENT_VERIFICATION_REPORT.md`, `C1_ISOMETRY_SCREENING.md`,
`JOINT_ENUMERATOR_FEASIBILITY.md`, `literature/`
**Status of the original object:** the joint Hermitian hull-dimension enumerator is
**K (known or routine)** — a product of published local results. That verdict is
unchanged and is now better supported (see §0).

**Decision required:** which of C1, C3, or stopping to pursue.

---

## 0. What changed this turn

Three findings alter the picture, and all three make the project *harder*, not easier.

1. **F11 is confirmed and is stronger than previously stated.** The strongest form
   needs no computation: the paper's own decomposition gives `|A| = q^{∏ deg t_i}`,
   while the Gray map takes values in `F_q^{|Ŝ|}`; in every example these differ by a
   factor `q²`. Independently computed: the `A`-module dimensions are `20` and `44`,
   against claimed code lengths `14` and `26`.
2. **A major precedent was missing from the literature review.** Li–Shi–Ling,
   *A mass formula for linear codes with prescribed hull dimension and related
   classification*, IEEE Trans. Inf. Theory **71**(1) (2025) 273–286, plus two
   companion papers, establish closed mass formulas and classifications for codes
   with a prescribed hull dimension. The *question type* is a mature industry.
3. **The isometry-class literature is also populated.** Chen–Fan–Lin–Liu (FFA 2012)
   introduced `n`-isometry precisely to classify constacyclic codes; a 2024
   *Cryptogr. Commun.* paper computes the numbers of `n`-isometry and `n`-equivalence
   classes over finite chain rings.

Consequence: C1, previously described as "the only surviving direction", is now seen
to sit at the **intersection of two well-developed lines**, not in empty space.

---

## C1 — Enumeration up to isometry

### C1.1 The exact research question

> Fix `A = F_q[X_1,…,X_ℓ]/⟨t_1,…,t_ℓ⟩`, a length `n`, a unit `λ ∈ A`, an integer
> `0 ≤ k < e`, and an **equivalence relation `~` on `λ`-constacyclic `A`-codes**.
> Determine
> `N_~(n, q, λ, k, h) = #{ ~-classes of λ-constacyclic A-codes with dim_q hull_k(C) = h }`.

**The relation `~` is not specified, and everything depends on it.** This is not a
formality — it is the first obstacle, and it is now known to be a fatal one for the
obvious choice.

> **Screening result, 2026-10-20 (`C1_ISOMETRY_SCREENING.md`).** If `~` is ordinary
> isometry (monomial equivalence), `N_~` **does not exist**: `dim hull_k` is not a
> class function. Over `F_4` with `q=4, n=3`, the cyclic code `⟨1+x⟩` has hull `0`,
> and its isometric image under `f(x) ↦ f(ωx)` — also cyclic, same dimension, same
> weight enumerator — has hull `1`. So the class would have to be counted at both
> `h` and `h+1`. The count is well defined only for the **similarity group** `Sim_k`
> of the Galois form, which is a proper subgroup (`|M| = 162` vs `|Sim_k| = 18` at
> `q=4, n=3`). Two reformulations survive — F1 (`Sim_k`-classes) and F2 (orbit/statistic
> pairs) — and neither is yet known to be non-trivial.

### C1.2 Established results

| Result | Reference | What it gives |
|---|---|---|
| `λ`-constacyclic codes over `A` ≅ tuples over the components | `[S1]` Thm 2, p.7 | reduces the object to a product |
| `hull_k` additive over components | `[S1]` Thm 7, p.10 | reduces the statistic to a sum |
| `n`-isometry / `n`-equivalence introduced to classify constacyclic codes over `F_q`; the `n`-equivalence classes in `F_q^*` number `gcd(n,q−1)` | Chen–Fan–Lin–Liu, FFA **18** (2012) 1217–1231 | the equivalence machinery over a field |
| numbers of `n`-isometry / `n`-equivalence classes of constacyclic codes over finite chain rings | *Cryptogr. Commun.* (2024), DOI `10.1007/s12095-024-00758-3` | the equivalence machinery over a ring |
| closed mass formulas for prescribed hull dimension (Euclidean, binary; all `q`; Hermitian; symplectic) | Li–Shi, ITT **70** (2024); Li–Shi–Ling, ITT **71** (2025) 273–286; arXiv:2410.13578 | counting codes with a prescribed hull dimension |
| hull dimension can change under equivalence for `q = 2, 3` | H. Chen, ITT **69** (2023) 2911–2922 | a warning: not every `~` is compatible with the statistic |

### C1.3 The unresolved gap

No paper combines the last three rows. Specifically, **no result found** gives:

- the number of constacyclic codes over a *product ring* `A`,
- counted **up to an equivalence**,
- **stratified by Galois hull dimension**.

But the screening result above narrows what such a result could even mean. There are
now exactly two well-posed questions (F1 and F2 of `C1_ISOMETRY_SCREENING.md` §4),
and the earlier statement of C1 is not one of them. What remains open is therefore
**not** "the enumeration up to isometry"; it is "which of F1/F2, if either, has content".
That is a weaker and less attractive position than this document recorded before the
screening.

### C1.4 The likely theorem, and why it may be trivial

There are three natural readings of `~`, and they behave very differently.

**(E1) `n`-isometry of the shift constant** (`λ ≅_n μ`, Chen et al.). This is a
bijection between the `λ`-family and the `μ`-family that preserves dimensions and
distance distributions. If it also preserves hull dimension — plausible, since it is
induced by an algebra isomorphism — then

```
N_{E1}(n,q,λ,k,h) = (#{ μ : μ ≅_n λ }) × #{ λ-constacyclic codes with hull_k = h } / |Aut| …
```

i.e. the isometry-class count would be the *unrestricted* count divided by a known
factor. **Under E1 the problem would not be open.** But E1 is not what the literature
means, and it does not survive the screening either: the dividing factor is only
legitimate if the statistic is a class function, which §C1.2 now shows it is not.

**(E2) Monomial/semilinear equivalence of codes** (the standard notion in code
classification). *This reading is now dead as a counting problem.* It is the relation
`~ = M(q,n)`, and `C1_ISOMETRY_SCREENING.md` shows `dim hull_k` is not a class
function under it: over `F_4` at `n = 3`, `⟨1+x⟩` and `φ(⟨1+x⟩)` with `φ = diag(1,ω,ω²)`
are isometric, both cyclic, same weight enumerator, and have hull dimensions `0` and
`1`. A Burnside sum over `M` would therefore sum `|Fix_h(g)|` over a group that does
not preserve the property being fixed. The formulation below in the original text of
this section is withdrawn; the correct versions are F1 and F2 of
`C1_ISOMETRY_SCREENING.md` §4.

**(E3) An isometry of `A^n` for the Gray metric.** Does not exist in the literature —
it would have to be defined first, and F11 shows that defining it is exactly where
`[S1]` goes wrong.

> **Therefore the first deliverable of C1 is not a theorem. It is a decision about
> which relation is meant, with a proof that the chosen one is neither trivial nor
> ill-defined.** That is a note, not a paper.

*(Superseded 2026-10-20 — see the note under (E2): the Burnside sum over the full
isometry group is invalid because the group does not preserve the hull dimension.
The construction survives only with `G = Sim_k`, where it is correct but small.)*

### C1.5 Proof strategy (if E2 is chosen)

1. Fix the smallest interesting ring: `A = F_4 × F_4` (`ℓ=2`, both `t_i` linear) or
   `A = F_4[x]/⟨x²+x+1⟩ ≅ F_16` (a field — degenerate but a useful control).
2. Enumerate **all** `λ`-constacyclic `A`-codes for small `n` (`n = 3, 5, 7`) with
   `gcd(n,q) = 1`. The count is `∏_S (number of divisors of x^n − λ_S)`, so this is
   feasible exactly.
3. Compute `hull_k` for each, verifying against `[S1]` Thm 8 (as corrected).
4. Compute `Aut(C)` for each code — this is the hard step; start with the subgroup
   generated by the constacyclic shift, the multiplier group, and Frobenius.
5. Assemble the Burnside sum. Test it against brute-force orbit enumeration for the
   smallest cases.
6. Only then attempt the general formula.

### C1.6 Risks (ordered by severity)

| # | Risk | Severity |
|---|---|---|
| R1 | ~~The relation turns out to be E1~~ — **RESOLVED, and worse than feared.** The Galois hull dimension is *not* a class function on isometry classes. Two witnesses: `q=4, n=3`, `C = ⟨1+x⟩`, `φ = diag(1,ω,ω²)`, Euclidean hull `0 → 1`; and `q=9, n=5`, `⟨2+6x+x²⟩ ⊂ F₉[x]/(x⁵−ω²)`, `ψ₂: f(x) ↦ f(x²)`, **Hermitian** hull `2 → 0`. **C1 as stated is ill-posed.** See `FINAL_INDEPENDENT_MATHEMATICAL_CHECK.md` §A. | **structural** |
| R2 | The relation is E2 but orbit counting is intractable beyond toy parameters, so the result is a table, not a theorem | high |
| R3 | The refined count is a formal consequence of the known counts plus a group-order division, i.e. no new mathematics | high |
| R4 | "Isometry" over `A` cannot be defined in a way that is simultaneously natural, checkable and compatible with `hull_k`. **Realised**: this is R1, now proved | high |
| R5 | The problem is solved while the project runs (the area is active: `[S25]`, Li–Shi–Ling, 2024–26 papers) | medium |

### C1.7 Computational requirements

Python is sufficient for steps 1–5 at `q = 4`, `n ≤ 7`; the counts are `≤ 10^5` codes.
Step 4 (automorphism groups) will need either a purpose-built backtrack search or a
CAS. **Magma/Sage are unavailable in this environment**, which caps the reachable
parameters. A GAP or Magma licence would be needed for anything beyond toy sizes.

### C1.8 Novelty evidence still needed before committing

1. Resolve R1: determine, with a proof, whether `λ ≅_n μ` preserves `hull_k`. If it
   does, C1 collapses to E1 and should be abandoned.
2. A literature check at full-text level (not abstract) of `[S25]`, the Li–Shi–Ling
   papers, and the 2024 chain-ring isometry paper, to confirm that none already
   contains a hull-stratified orbit count.
3. A proof that the answer is **not** obtainable as "(known total) / (group order)" —
   e.g. by exhibiting two codes with the same `(n, λ, k, h)` and different `Aut`.
4. A demonstration on one worked example that the orbit count differs from any
   published count.

If any of 1–3 fails, C1 is not viable.

---

## C3 — A corrigendum for F11 (with F3)

### C3.1 The exact research question

> Not a research question. It is: **what is the correct statement of `[S1]` §3–§4
> when the CRT components are not `F_q`, and what are the corrected parameters of
> Examples 2–3 and Table 1?**

### C3.2 Established results

The correction is already proved in `INDEPENDENT_VERIFICATION_REPORT.md` §3:

- `dim_q hull_k(C) = Σ_S |S(ν)| · (n − deg lcm(g_S, h_S^#))` — the corrected
  Theorem 8;
- `ψ : A → F_q^{dim_q A}` — the corrected Gray map (length `n·dim_q A`, not `n·N`);
- `|S(ν)| = 2` for every component in Examples 2, 3 and the `q = 4` ring;
- `dim_q C = 20` and `44`, against claimed lengths `14` and `26`;
- Corollary 3.5(2) fails at `e' = 0`, with an explicit counterexample.

### C3.3 The unresolved gap

**None mathematically.** The gap is procedural: the version of record is unreadable
(§5 of the verification report), so it is unknown whether the defect persists.

### C3.4 The "likely theorem"

There is no theorem. The deliverable is a **correction**: three restatements and a
table of corrected parameters. Its scientific value is that the paper's quantum
parameters depend on the error.

### C3.5 Proof strategy

Already complete. What would remain:
1. recompute the corrected parameters for all 13 rows of Table 1 under `R2`
   (length `n·dim_q A`);
2. state precisely which of the paper's conclusions survive (`Thm 2, 3, 5, 6, 7, 10`,
   `Lemma 9`) and which need restatement (`Thm 8`, `Cor 3.1`, `Cor 3.4`, `Cor 3.5`).

### C3.6 Computational requirements

None beyond what is already in `code/`. Roughly one day's work for items 1–2.

### C3.7 Risks

| # | Risk | Severity |
|---|---|---|
| R6 | **The version of record already fixed it.** Then C3 has zero value | **fatal if true** |
| R7 | Journals rarely publish errata by non-authors; the authors would have to be involved | high |
| R8 | A correction is not a research contribution and will not support a thesis, grant or promotion case | high (context-dependent) |
| R9 | The authors may dispute the reading; the `R1`/`R2` repair question is a judgement call | medium |

### C3.8 Novelty evidence still needed

Only one thing: **the version of record**. Until it is read, C3 must not be started.

---

## D — Stop, or choose a different direction

### D.1 What "stop" means here

The project has produced: a complete theorem register; a documented set of defects in
a published paper (F3, F4, F5, F11); a verified computational reproduction of every
worked example; a proof that the proposed contribution is routine (Proposition J); and
a literature map. That is a legitimate, completed feasibility study. Stopping is a
defensible outcome, and the blueprint explicitly permits it.

### D.2 If a different direction is wanted

Any new direction must pass the same gate, and the gate has already rejected one
candidate after two rounds of verification. The criteria are:

1. the object is not a product/linearisation of known objects;
2. the closest published statement is at least one genuine step away;
3. a theorem can be stated and proved within the available tools;
4. a small case can be computed and checked.

Two candidates that were considered and **rejected** in earlier rounds — distance-aware
enumeration (blocked by `[S1]` Remark 1) and dual-containing enumeration
(componentwise by `[S1]` Thm 6) — should not be revived.

---

## Comparison

| Criterion | C1 (isometry classes) | C3 (corrigendum) | D (stop) |
|---|---|---|---|
| Is there a real gap? | Narrower than recorded: the obvious formulation is **ill-posed** (R1), only F1/F2 remain | No gap — a defect | — |
| Is there a theorem? | Maybe; possibly none | No | — |
| Certainty of a deliverable | Low | **High**, conditional on §5 | **High** |
| Effort to first real signal | 2–4 weeks | 1–2 days | 0 |
| Blocking dependency | definition of `~` | version of record | none |
| Risk of wasted effort | High | Low (but fatal if already fixed) | — |
| Uses the work already done | Partly | **Fully** | Fully |
| Supports a publication | Possibly | Only as an erratum | No |

---

## Recommendation

**Do not begin a manuscript. Do not begin C1 yet.**

The evidence supports a three-step sequence, in this order:

**Step 1 (mandatory, cheap, blocks everything).** Obtain the version of record
(*Discrete Math.* **349**(2) (2026) 114750) through a library. Read §3, §4 and the
tables. Record, in `INDEPENDENT_VERIFICATION_REPORT.md` §5, whether F11, F3 and the
Example 2–3 parameters are as in arXiv v1. **Everything downstream depends on this and
it has not been possible here.**

**Step 2 (conditional).** If the defect survives in the version of record, write
**C3** — a short correction note, ~4 pages, with the corrected Theorem 8, the corrected
Gray map, the corrected parameters, and the Corollary 3.5(2) counterexample. This is
the only direction where a correct result is already in hand. It is not a research
contribution and should not be presented as one.

**Step 3 (optional, gated).** Only if Step 1 shows the defect is *already fixed* —
i.e. only if C3 has no value — should C1 be considered. **R1 has now been resolved
and the answer was negative** (`C1_ISOMETRY_SCREENING.md`), so the spike is shorter
and its target has changed:

- **Already done:** the naive formulation is dead. Do not spend any time on
  "count up to isometry stratified by hull dimension".
- **Week 1 (still required):** decide between F1 (`Sim_k`-classes) and F2
  (orbit/statistic pairs) by computing both at `q = 4, n = 3, 5` and asking whether
  either produces a number that is not a restatement of an enumeration count.
  - If neither does → **abandon C1**.
- **Week 2:** if one does, attempt a general statement for the product ring `A`.

The reason for this ordering is the asymmetry of the evidence. C3 has a certainty
that C1 does not, and C1 has a specific, identifiable way of being worthless (R1) that
can be settled in days. Spending the cheap check first protects against spending weeks
on a problem whose answer is a corollary of `[D23]`.

**What should not be done:** writing the blueprint's Phase 5 manuscript. That object
is **K** by Proposition J, and the two rounds of verification have strengthened, not
weakened, that conclusion.

---

## Open items carried to `PHASE_STATUS.md`

| ID | Item | Owner | Blocking? |
|---|---|---|---|
| B-1 | Version of record of `[S1]` not read | user (library access) | **yes, for C3 and for closing F11** |
| B-2 | Full text of `[D23]` not read; the "restrictions on `q`" remain unknown | user | no, but caps O2 |
| B-3 | Full texts of `[S25]`, Li–Shi–Ling (2025), chain-ring isometry (2024) | user | yes, for C1 step 3 |
| B-4 | No Magma/Sage/GAP in this environment | environment | caps C1 to small parameters |
