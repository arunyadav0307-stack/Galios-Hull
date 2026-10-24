# Phase 3 deliverable — Mathematical framework

Blueprint Phase 3 asks for precise definitions, well-definedness, and the six specific
well-posedness questions in §3A. Each is answered below with a pointer to where the proof lives.
Nothing here is new mathematics; this is the consolidated framework, and it is deliberately short
because the content already exists in the cited documents.

---

## 1. Objects

| Symbol | Meaning |
|---|---|
| `q = p^m`, `F = F_{q²}` | ground field for every constituent; `p = char F` |
| `R_e = F[u]/(u^e − 1)`, `e \| (q+1)` | the source's non-chain ring; note `e \| q+1` forces `q ≡ −1 (mod e)`, and `p ∤ e` |
| `e_μ = (1/e)Σ_j μ^{−j}u^j`, `μ^e = 1` | CRT idempotents (the source's `η_ℓ` are these times a scalar — Phase 1 finding F-1) |
| `λ = Σ_μ e_μ λ_μ ∈ R_e^*`, `λ_μ ∈ F^*` | multiplier; `λ_μ = λ(μ)` is forced (R2) |
| `C = ⊕_μ e_μ C_μ` | `λ`-constacyclic code over `R_e`; `C_μ` is a `λ_μ`-constacyclic code over `F` |
| `n = p^v n'`, `gcd(n',p)=1` | length; `p \| n` allowed |
| `⟨x,y⟩_H = Σ x_i y_i^q` | Hermitian form; `y ↦ y^q` is the **ring** power (`u ↦ u^{−1}`) |
| `Hull_H(C) = C ∩ C^{⊥_H}` | hull; all dimensions are over **`F = F_{q²}`** unless stated |
| `M`, `M M^* = ν I_e`, `ν ≠ 0` | Gray matrix, **not fixed by the source**; must be named in every distance claim |
| `ψ(r) = [(s_{1i},…,s_{ei})M]_i` | Gray map, `r_i = Σ_k η_k s_{ki}` |

**Distance convention.** `d(ψ(C))` is the Hamming distance of the *field* code `ψ(C) ⊆ F^{en}`.
Hamming weight over `F`, never Lee weight over `R_e`.

## 2. The six well-posedness questions (blueprint §3A)

**(a) What counts as a distinct code?**
Distinct `F`-subspaces closed under the constacyclic shift — equivalently, distinct ideals of
`R_e[x]/(x^n − λ)`. At the field level, distinct ideals of `F[x]/(x^n − α)`, which are in bijection
with monic divisors of `x^n − α`: **proved**, `CONSTITUENT_ENUMERATOR_FORMULA.md` Lemma 1. At the ring
level the bijection is via CRT tuples (`R3_DECISION.md`; `PIR lemma` in `R1_FEASIBILITY.md` §1).
Equivalence classes of codes are **out of scope** and were never counted.

**(b) Uniqueness of the constituent representation.**
**Proved.** `R_e ≅ ∏_μ F` by CRT, and a homomorphism out of a product of fields is determined by its
coordinates, so `λ ↦ (λ_μ)` is a bijection and the tuple `(C_μ)` is unique. Verified `27/27` and, by
linearity, for every element at `e = 4` (`R2_DECISION.md` §3). The source's printed `η_ℓ` give a
*different* (also unique) coordinate system related by `λ(μ_ℓ) = a_ℓ·η_ℓ(μ_ℓ)`; using `a_ℓ` as the
multiplier is wrong for all but one component and was quantified there.

**(c) Are constituent choices independent?**
**Yes, and this is the crux.** Two independent statements:
* *Algebraic:* any tuple of `λ_μ`-constacyclic codes is admissible — there is no cross-component
  constraint, because `R_e[x]/(x^n−λ) ≅ ∏_μ F[x]/(x^n−λ_μ)` is a ring isomorphism.
* *Combinatorial (field level):* the exponent box `[0,p^v]^s` is a Cartesian product with only
  per-factor multiplicity bounds — no cross-factor coupling. Proved in
  `CONSTITUENT_ENUMERATOR_FORMULA.md` §6(c).

**But independence of the *hull* marginal does not extend to distance** — the Gray map couples the
components at each position (`P3_3_RING_GRAY.md` §2). This distinction is the framework's main content.

**(d) Behaviour of the Hermitian dual and hull under decomposition.**
**Proved.** The `q`-power **fixes every idempotent** (the coefficient Frobenius cancels the
`μ ↦ μ^{−1}` label permutation), hence `C^{⊥_H} = ⊕_μ C_μ^{⊥_H}`, `Hull_H(C) = ⊕_μ Hull_H(C_μ)`, and
`C^{⊥_H} ⊆ C` iff componentwise (`P3_3_RING_GRAY.md` Theorem 1). Verified `16/16`, `27/27` (R3) and
`256/256` for the Gray-image hull identity (P3-5).

**(e) Over which field are dimensions taken?**
Always `F = F_{q²}`, for both the ring-level and the constituent dimensions; `d(ψ(C))` is a Hamming
distance over the same `F`. The quantum code produced is over `F_q`, not `F_{q²}` — a confusion the
blueprint explicitly warns about and which is avoided by writing `[[en, 2K−en, ≥d]]_q`.

**(f) Counting codes vs. counting generator descriptions.**
Resolved at the field level by Lemma 1 (bijection), and independently confirmed by brute force over
**all 184 subspaces** of `F_9³` in the `q=3, n=3` case (8/8 values of `α` matched). At the ring level
the CRT tuple ↔ code correspondence is a bijection, so distinct tuples are distinct codes. The Phase 1
finding F-1 is the trap this question exists to catch.

## 3. The two enumerators, stated

**Constituent (proved, `CONSTITUENT_ENUMERATOR_FORMULA.md`):**

```
H_α(z) = ∏_{σ-orbits O} P_O(z),      P_i(z) = Σ_{a=0}^{p^v} z^{m_i min(a, p^v−a)}
                                     P_ij(z) = Σ_{a,b=0}^{p^v} z^{m_i min(a+b, 2p^v−a−b)}
```

**Joint / total.** Because the tuple coordinates are free and the hull dimension is additive,

```
H_joint(z_1,…,z_e) = ∏_{μ} H_{λ_μ}(z_μ),        H_total(z) = H_joint(z,…,z) = ∏_μ H_{λ_μ}(z),
```

and the total hull dimension is the sum of constituent ones **by Theorem 1, not by assumption**. This
is the relationship the blueprint requires to be proved before `H_total` is used — it is Theorem 1.
The consequence, recorded at Gate 2 and again in R1/R3: `H_total` carries **no information beyond the
`e` marginals**, which is why the enumerator programme was classified `K`.

**Status: `H_total` is routine.** The framework's value is that it says so precisely.

## 4. What the framework does *not* provide

* No distance law. `H_α` is the hull marginal; `d` is not determined by it (`P3_1_TABLES.md` §4, C3 5/5).
* No joint `(hull, d)` formula — and there cannot be one in product form, because `d(ψ)` is not a
  function of the constituent data (`P3_3_RING_GRAY.md` Theorem 5).
* No statement about equivalence classes, weight enumerators, or asymptotic behaviour.
