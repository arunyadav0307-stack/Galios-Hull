# C1_ISOMETRY_SCREENING

**Question screened:** risk **R1** of `RESEARCH_DIRECTION_DECISION.md` §C1.6 —
*does an isometry of `F_q^n` preserve the Galois hull dimension?* If yes, direction
C1 collapses to a corollary of `[D23]`; if no, C1's counting problem may not even be
well posed.

**Answer: no, and the consequence is the second one.** The Galois hull dimension is
**not a class function on isometry classes of constacyclic codes**, so C1 as stated
is ill-posed. A corrected formulation is given in §4.

**Status:** the counterexample and the invariance proof are both settled. What this
does *not* do is establish that the corrected problem is novel or tractable — that
remains open (§6).

> **Revised 2026-10-20** after re-checking the exponent convention. Two statements in
> the first version of this note were wrong and are corrected below: (1) the criterion
> is `a_i^{1+p^k}`, not `a_i^{1+q^k}`; (2) the `F_4` witness changes the **Euclidean**
> hull only — the Hermitian hull is `0 → 0` there, and provably cannot change at `q = 4`.
> A genuine Hermitian counterexample, over `F_9`, is in §1b.
> Authoritative version: `FINAL_INDEPENDENT_MATHEMATICAL_CHECK.md`.

---

## 1. The witness

Over `F_4 = F_2[ω]/⟨ω²+ω+1⟩`, length `n = 3`, let

```
C = ⟨1 + x⟩ ⊆ F_4[x]/(x³ − 1),        dim_{F_4} C = 2,   |C| = 16,
φ = diag(1, ω, ω²),   i.e.   φ : f(x) ↦ f(ωx).
```

Then:

| | `C` | `φ(C)` |
|---|---|---|
| cyclic (`T₁`-invariant) | **yes** | **yes** |
| `dim_F4` | 2 | 2 |
| weight enumerator | `{0:1, 2:9, 3:6}` | identical |
| `dim hull_0` (Euclidean) | **0** | **1** |
| `dim hull_1` (Hermitian, `q = 4`) | 0 | 0 |

`φ` is a diagonal matrix with nonzero entries, so it preserves every Hamming weight
exactly: it is an isometry in the strongest sense. Both codes are cyclic, so both lie
inside the family C1 proposes to enumerate. They are indistinguishable by dimension
and by weight enumerator, and they differ in hull dimension.

**Verification:** `code/isometry_hull_screening.py` PART A, computed by brute-force
enumeration of all `q^n = 64` vectors — deliberately not using the library's hull
routine — with output in `verification/isometry_hull_screening.out`.

Why `φ` preserves cyclicity: `ω³ = 1`, so `(ωx)³ = x³`, and `f ↦ f(ωx)` is an
`F_4`-algebra automorphism of `F_4[x]/(x³−1)`. It therefore carries ideals to ideals,
i.e. cyclic codes to cyclic codes. It is *not* an isometry of the Euclidean form, and
that is the whole point.

---

## 2. The general criterion (why this was predictable)

Let `φ = D P` be a monomial map, `D = diag(a_0,…,a_{n−1})`, `a_i ∈ F_q^*`, `P` a
coordinate permutation. For the Galois form `⟨u,v⟩_k = Σ_i u_i v_i^{p^k}` (paper p.7 —
the exponent is `p^k`, not `q^k`),

```
⟨φu, φv⟩_k = Σ_i a_i^{1+p^k} u_i v_i^{p^k}.
```

So `φ` scales the form by a constant — and hence preserves orthogonality, and hence
the hull — **iff `a_i^{1+p^k}` is independent of `i`**. Define

```
Sim_k = { D P ∈ M(q,n) : a_i^{1+p^k} is constant in i }.
```

**Proposition.** For `φ ∈ Sim_k`, `φ(C^{⊥_k}) = (φC)^{⊥_k}`, so
`dim hull_k(φC) = dim hull_k(C)`.

*Proof.* `⟨φu, φv⟩_k = c⟨u,v⟩_k` with `c ≠ 0`. Hence `u ∈ C^{⊥_k}` ⟺ `φu ∈ (φC)^{⊥_k}`.
Apply `φ` to `C ∩ C^{⊥_k}`. ∎

**Corollary.** `dim hull_k` is a class function exactly on `Sim_k`-classes, not on
`M`-classes. `Sim_k ⊊ M` whenever `q > 2`.

Numbers for `q = 4, n = 3`: `|M| = 3!·3³ = 162`; `|Sim_0| = |Sim_1| = 18`
(for `k = 0` the condition forces all `a_i` equal since squaring is a bijection on
`F_4`; for `k = 1`, `a^{1+p} = a³ = 1` for every nonzero `a`, so `Sim_1 = M`).
`diag(1,ω,ω²)` lies outside `Sim_0` and inside `Sim_1` — which is exactly why only the
Euclidean hull moves.

**Over `F_4`, `Sim_1 = M`**, so `hull_1` is an isometry invariant there and no
counterexample of any shape exists. A Hermitian counterexample needs a field where
`a ↦ a^{1+p}` is nontrivial; the smallest is `F_9` (see §1b).

`code/isometry_hull_screening.py` PART C checks the proposition exhaustively:
432 (code, similarity, `k`) triples, **0 failures** — consistent with the proof, and a
control that the machinery is not simply reporting "everything differs".

---

## 1b. A Hermitian counterexample over `F_9`

`ψ₂ : f(x) ↦ f(x²)` on `F₉[x]/(x⁵ − ω²)`, with scalings `(1,1,1,ω,ω)` and target ring
`F₉[x]/(x⁵ − ω)`, sends `⟨2 + 6x + x²⟩` (dim 3) to a `ω`-constacyclic code of dim 3,
both with equal weight distributions, and

```
dim hull_1 :  2  →  0        (|hull| = 81 = 9²  →  1).
```

Norm scalings `(1,1,1,2,2)`, non-constant — as the criterion requires. Full search at
`n = 5`: 256 triples, 32 changes. Reproduce with `code/final_check_A.py`.

---

## 3. What this refutes

It refutes, by counterexample, the only formulation of C1 that had been written down
(both over `F_4` for the Euclidean hull and over `F_9` for the Hermitian hull):

> "Count `λ`-constacyclic codes with `dim hull_k = h`, up to isometry."

That count is not well defined: the class of `⟨1+x⟩` would have to be counted once
for `h = 0` and once for `h = 1`. Any implementation of C1 that divided a total count
by a group order (the tempting shortcut) would be **wrong**, not merely crude.

It does *not* refute the underlying research area. `[S25]`, `[D23]`, `[SJL15]` count
codes, not classes, so they are untouched.

---

## 4. The two formulations that survive

**(F1) Similarity classes.** Count `Sim_k`-classes:

```
N_{Sim_k}(n, q, λ, h) = #{ Sim_k-classes of λ-constacyclic A-codes with dim_q hull_k = h }.
```

This is well defined by the proposition. Its difficulty: `Sim_k` acts on codes but is
a *small* group (order `n!` up to scalars for `q = 4`), so the count is close to a
brute-force enumeration and the interesting arithmetic content may vanish. This is
the honest risk: **well defined but possibly trivial.**

**(F2) Orbit–statistic pairs.** Count orbits of the pair `(C, hull_k(C))`:

```
N(n, q, λ, h) = # M-orbits of pairs (C, V) with V = hull_k(C), dim V = h.
```

Equivalently, for each `M`-orbit `𝒪`, record the *distribution* of `dim hull_k` over
`𝒪` and count orbits weighted by that distribution. This is well defined for any group
and is the version that matches what C1 was trying to ask. Its difficulty: the
distribution is a genuinely new invariant, and computing it requires understanding how
`Sim_k`-cosets act — which is a *different* and possibly more interesting problem than
the one originally proposed.

**Which to pursue:** neither, yet. F1 risks being vacuous; F2 risks being a
reformulation rather than a result. The screening has converted "is C1 open?" into
"is either F1 or F2 worth a paper?" — and that question cannot be answered without the
literature step in §6.

---

## 5. Naming the phenomenon

The gap between `M` and `Sim_k` is not an artefact of the Galois setting. It appears
already for the Euclidean form over any `q > 2`: a diagonal isometry with
`a_i²` non-constant preserves Hamming weight but not orthogonality. Over `F_2` the two
groups coincide (`a_i = 1` is forced), which is why the classical intuition "the hull
is an invariant of the equivalence class" is reliable over the binary alphabet and
misleading in general.

This is very likely known to specialists — it is the reason mass-formula papers act by
the *isometry group of the form* (unitary, symplectic) rather than by all monomial
maps. **We do not claim it as new.** It is recorded because it was not in this
project's earlier documents, and because the whole of C1 rested on it.

---

## 6. What is still needed before C1 can be judged

| # | Question | Why it decides the direction |
|---|---|---|
| Q1 | Does `[S25]` / `[D23]` / `[CFLL12]` / the 2024 chain-ring paper already quotient by `Sim_k` rather than by `M`? | If a precedent exists, C1 has no content at all |
| Q2 | Is `N_{Sim_k}` expressible without enumerating codes (a Burnside sum with computable fixed points)? | Decides whether F1 is a theorem or a table |
| Q3 | Is the `M`-orbit hull distribution of F2 ever non-constant in a family with a closed form? | Decides whether F2 is a result |
| Q4 | Does the `A`-version (product ring, `ℓ ≥ 2`) add anything the field case does not have? | If not, C1 is a field-level problem, already well populated |

Q1 and Q4 are literature questions, blocked only by paywalls. Q2 and Q3 are
mathematical and can be attacked immediately at `q = 4, n = 3` and `n = 5`.

---

## 7. Reproducibility

| Item | Path |
|---|---|
| script | `code/isometry_hull_screening.py` |
| output | `verification/isometry_hull_screening.out` (exit 0) |
| dates | 2026-10-20 |
| dependencies | `code/gf.py` only; Python 3.11.2; no CAS |
| independent check | PART A recomputes hulls by enumerating all `q^n` vectors, never calling `gf.hull_dim` |

The script prints the counterexample, the group orders, the exhaustive invariance
check, and exits non-zero if the invariance check finds a failure (it does not).
