# R4 — Feasibility and structural test: the quantum-parameter distribution

**Status: structurally GO.** R4 is the first candidate in this project whose counting target is
**not** a product over the CRT components. That is a necessary condition for surviving Gate 2, not a
sufficient one — §6 lists the two checks that must still be run, and neither is a formality.

Written from `78b89ac` on branch `arena/831a2e65-galios-hull`. Probe: `phase2/r4_probe/r4_probe.py`,
log `r4_probe_log.txt` (29 lines), runtime < 1 s.

---

## 1. The question

> For `R_e = F_{q²}[u]/(u^e − 1)`, `e | q+1`, count `λ`-constacyclic codes `C` over `R_e` with
> `C^{⊥_H} ⊆ C` by their **quantum parameters** `[[en, 2k − en, ≥d]]_q` — equivalently by the pair
> (hull dimension, Gray distance `d = d(ψ(C))`) — and determine how the resulting distribution
> depends on `λ`, `n` and the repeated-root parameter `p^v`.

R1, R2 and R3 all died because their target quantity was additive over the `e` CRT components, which
made every count a product of published field-level laws. R4 was proposed in `R3_DECISION.md` §9 on
the guess that the **minimum distance** does not behave that way. This document tests the guess.

## 2. The Gray map, verified from the source

From pages 6–7 and 15 (full text, not abstract):

* `ψ(r_0, …, r_{n−1}) = [ (s_{10},…,s_{e0})M , …, (s_{1,n−1},…,s_{e,n−1})M ] ∈ F_{q²}^{en}`,
  where `r_i = Σ_k η_k s_{ki}` is the **η-basis** expansion of the `i`-th coefficient and `M` is a
  square matrix of order `e` with
  `M M* = ν I_e`, `ν ∈ F^*_{q²}`, `M* = (M^T)^{(q)}` (Hermitian transpose).
* `ψ` is a bijective linear map and `ψ(C^{⊥_H}) = ψ(C)^{⊥_H}` (Lemma 3), so dual-containing
  transfers exactly.
* Theorem 19: if `ψ(C)` has parameters `[en, k, d]_q` then there is a quantum code
  `[[en, 2k − en, ≥d]]_q`.

**The decisive structural point.** `ψ` multiplies the vector of the `e` component symbols **at each
position** by `M`. So the Gray weight is

```
w_G(c) = Σ_{i=0}^{n-1}  g( s_{1i}, …, s_{ei} ),      g = number of nonzero entries of (s_{1i},…,s_{ei})M,
```

a sum over **positions** of a **joint** function of all `e` component symbols. It is *not*
`Σ_k w(s_k)`, and it is not `Σ_k (Hamming weight of the k-th component codeword)`. The CRT
components are therefore **coupled by the distance**, even though they are free in the hull
dimension.

## 3. The e = 2 case, explicitly

With `M = [[1,1],[1,−1]]` (the paper's matrix for `e = 2`) and the η-coordinates `s_k = α_k/2`:

```
ψ(c) = ( a + b , a − b ),   w_G = w(a+b) + w(a−b),   a ∈ C_1, b ∈ C_2
```

so a codeword of Gray weight 1 exists **iff** `C_1` and `C_2` share a word of Hamming weight 1
(put `a = b = c·e_i`, then `a − b = 0`). Hence

```
d(ψ(C_1 × C_2))  depends on  C_1 ∩ C_2,
```

which is a joint invariant of the pair. No function of `(d(C_1), d(C_2))` — nor of the whole
per-component data `(k_ℓ, d_ℓ)` — can determine it. This is a proof, not an observation: it does not
depend on any particular parameter choice.

## 4. Computational check

`q = 3, e = 2, n = 2`, `F_9`, `M = [[1,1],[1,−1]]`. Every `(C_1, C_2)` pair of field-level
`α_ℓ`-constacyclic codes was enumerated, `d(ψ(C))` computed **exactly** by enumerating all
codewords of `ψ(C)`, and the pairs grouped by the component invariants `(k_1, d_1, k_2, d_2)`:

| Component invariants `(k₁,d₁,k₂,d₂)` | Gray distances realised | constant? |
|---|---|---|
| 9 distinct groups in total | — | — |
| `(1, 2, 1, 2)` | **`{2, 3}`** | **no** |
| all others | singleton | yes |

So the Gray distance is **not** a function of the component data: the same `(k_1,d_1,k_2,d_2)`
yields two different quantum distances. A product of field-level laws cannot reproduce this.

Dual-containing pairs: **144**. Quantum parameters realised: `(k, d) ∈ {(2,2), (2,3), (3,2), (4,1)}`,
i.e. `[[4, 0, ≥2]]`, `[[4, 0, ≥3]]`, `[[4, 2, ≥2]]`, `[[4, 4, ≥1]]` over `F_3`. These are deliberately
toy parameters (the instance is small enough to be exhaustive); **no claim is made that any of them
is good or new**, and the two `K = 0` cases are degenerate.

## 5. Two scope limitations found while doing this

**(5.1) The matrix `M` is a free parameter.** The paper requires only `M M* = ν I`. For `e = 2` the
matrix `[[1,1],[t,−t]]` is admissible exactly when `t` has norm 1 (`t t^q = 1`), which for `q = 3`
gives `t ∈ {1, 2}`. Both were verified numerically (`M M* = 2I` in each case). In this instance the
Gray distances were **identical** for both choices (`0/16` pairs differed) — so no dependence on `M`
was observed, but that is a small-scale observation, not a theorem. Any claim about "the"
distribution must fix `M` explicitly.

**(5.2) The paper's `e = 2` matrix is not admissible in even characteristic.** `ν = 2`, which is `0`
in `F_{2^m}`; `M` is then singular and `ψ` is not injective. The probe confirms the failure
concretely: over `F_4` it produces Gray distance `0` for nonzero codewords (`q = 2` run, then
suppressed). This is not an error in the paper — every worked example uses odd `q` (`5, 11, 13, 25`)
— but it is a real restriction on the construction's stated generality, and it is recorded here
because a counting question spanning all `q` would inherit it.

## 6. What must still be settled before R4 can be authorised

| # | Check | Why it could kill R4 | Status |
|---|---|---|---|
| **K4-1** | **Prior art.** Does any accessible work already count `λ`-constacyclic codes over `R_e` (or over `F_q + uF_q + …`) with `C^{⊥_H} ⊆ C` by quantum parameters, or compute the joint (hull, distance) law for a constacyclic family? | If yes, R4 is `K` like R1–R3. The construction literature (Dinh, Bag, Ashraf–Mohammad, et al.) produces *tables of codes*, not *counts*; but this must be checked with full-text evidence, and blockers B-1/B-2 are still open. | **not done** |
| **K4-2** | **Computational feasibility.** Does the count have any closed form, or is it a hard enumeration? Exact minimum distances of constacyclic families are not known in general, and computing them is expensive. | If the answer is "enumerate and hope", R4 is not a research programme; if a structural decomposition exists (e.g. via repeated-root distance formulas of Dinh), it is. | **partly**: the probe shows exact enumeration is affordable for small `n`, nothing more |

Also unresolved: the source's own Section 5 already tabulates quantum codes from `R_e`, so R4 must be
*distinguishable from the paper it extends* — a distribution is not a table, but the blueprint's
warning against relabelling applies.

### 6.1 First prior-art pass on K4-1 (search level only — not a verdict)

| Source | What it does | Bearing on R4 |
|---|---|---|
| **arXiv:2605.29204**, *Enumeration and Monotonicity of Linear Codes with Prescribed Hull Dimensions* | closed-form mass formulas for the number of `[n,k]_q` codes with prescribed (Hermitian) hull dimension | counts **all** linear codes of a length/dimension, with **no distance constraint**; says nothing about constacyclic families |
| **arXiv:2512.12519**, *Linear Codes with Certain Dimension of Hermitian Hulls* | closed-form counts of Hermitian `ℓ`-complementary codes; asymptotics of Hermitian self-orthogonal codes with `d ≥ δ` | **the closest prior art found**: it does couple hull and distance, but over the whole Grassmannian, asymptotically — not over a constacyclic family, and not exactly |
| **arXiv:2607.12242** | hull codimension additive over `τ`-orbits; exact hull-codimension enumerator; dual distances of *specific* extended codes; quantum codes with "distance preserved" | enumerates hull dimension; distances are studied per constructed code, not distributed over a family |
| **Sangwisut–Jitman–Udomkavanich, AMC 2017** | Hermitian hull dimensions of `λ`-constacyclic codes over `F_{q²}`; characterisation/enumeration of self-dual and LCD cases | no distance |
| **Dinh, Bag, Ashraf–Mohammad, et al.** (repeated-root quantum-code literature) | *tables* of quantum codes from repeated-root constacyclic codes, and over `F_q + uF_q + …` with Gray maps | constructions and tables, not counts or distributions |

Reading: the "count codes with a prescribed hull **and** a distance constraint" idea is not new in
the abstract (arXiv:2512.12519), and that is the strongest threat to R4. What I did not find is any
work that does it **for a constacyclic family**, exactly, with a repeated-root parameter — which is
exactly where the source's machinery lives. Under Phase 2's rules a search result of this kind
establishes **at most** that R4 is not obviously pre-empted; it does **not** establish absence, and
B-1/B-2 remain open. Classification, if it survives: **N2 at best**.

## 7. Relation to R1/R2/R3

| | Target quantity | Behaviour over CRT components | Outcome |
|---|---|---|---|
| R3 | count of dual-containing codes | additive (hull) | **NO-GO** — product of published counts |
| R1 | hull-dimension distribution, `p \| n` | additive | **NO-GO** — lattice-point count in the source's own boxes |
| R2 | dependence on the decomposition of `λ` | n/a | **NO-GO** — the decomposition is unique |
| **R4** | **(hull, Gray distance) distribution** | **coupled by the distance** | **structurally GO** — §3 proves non-factorisation; §4 confirms it numerically |

R4 is the only candidate in this project that passes the structural test that killed the other
three. That is a genuinely positive finding, and it is the first one in Phase 2.

## 8. Verdict and next action

**GO on structure; not yet GO on the research question.** R4 survives the kill criterion that
destroyed R1–R3, so it is worth the prior-art check (**K4-1**) and the feasibility question
(**K4-2**). It does **not** yet pass Gate 2, because Gate 2 asks for distinguishability, and that
is a literature question that has not been answered.

Next action, in order:

1. Prior-art search with full-text where obtainable, on: joint (hull dimension, minimum distance)
   distributions; quantum-code counts from constacyclic codes over rings with a Gray map; the
   distance distribution of repeated-root constacyclic families.
2. If K4-1 does not kill it, decide feasibility (K4-2) and only then re-run Gate 2.

No novelty is claimed. Blockers **B-1** (publisher full texts) and **B-2** (Debnath–Prakash body)
remain open, and K4-1 depends on both.
