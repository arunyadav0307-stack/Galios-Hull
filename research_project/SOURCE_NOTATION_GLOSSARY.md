# SOURCE_NOTATION_GLOSSARY

Every symbol used by `[S1]`, with its **exact** meaning and the convention in force.
Where the blueprint and S1 use the same letter for different things, both are given.

> **Reading rule.** `q = p^e` always refers to the **ambient field `F_q` of S1**.
> The blueprint writes `F_{q^2}` and reuses `q`; in that convention the ambient
> field has order `q²`. These are *not* the same `q`. Every formula in this project
> is tagged with which one it uses.

---

## 1. Fields and primes

| Symbol | Meaning in S1 | Note |
|---|---|---|
| `p` | prime, characteristic | `q = p^e` |
| `e` | positive integer, `q = p^e` | blueprint reuses `e` as the number of ring components — **different** |
| `q` | `p^e`, size of the ambient field `F_q` | blueprint's `q` is S1's `q` only when S1's field is `F_{q²}`; do not mix |
| `k` | Galois parameter, `0 ≤ k < e` | the inner product exponent |
| `e'` | exponent in `n = n' p^{e'}`, `gcd(n',p)=1` | repeated-root multiplicity |
| `n'` | prime-to-`p` part of `n` | |
| `r` | `ord(λ)`, multiplicative order of `λ` | |
| `r_{S(ν)}` | `ord(λ_{S(ν)})` | divides `r` (Lemma 6) |
| `l` | least multiple of `lcm(e, e−k)` such that `l′` gives an even `l`; used so that `f^{l#} = u f` | `[S1 §2.4]`; `l = l' p^{e−k}` in the intended reading `[OCR-SUSPECT]` |
| `s` | number of distinct positive divisors of `l`; `a_1,…,a_s` are those divisors, `a_1 = 1` | |
| `φ` | Euler totient | |

## 2. The ring `A`

| Symbol | Meaning |
|---|---|
| `ℓ` | number of variables `X_1,…,X_ℓ` |
| `t_i(X_i)` | square-free polynomial in `F_q[X_i]` |
| `I` | ideal `⟨t_1(X_1),…,t_ℓ(X_ℓ)⟩` |
| `A` (or `R`) | `F_q[X_1,…,X_ℓ]/I`; a finite commutative semisimple ring |
| `H_i` | set of roots of `t_i` in a splitting field |
| `H` | `∏_i H_i` |
| `ν = (ν_1,…,ν_ℓ)` | an element of `H` |
| `S(ν)` | Frobenius class `{(ν_1^{q^j},…,ν_ℓ^{q^j}) : j ∈ N}` |
| `Ŝ` | set of all classes |
| `N` | `|Ŝ|` = number of idempotent components |
| `e_{S(ν)}` | primitive orthogonal idempotent attached to `S(ν)`; `Σ_S e_S = 1` |
| `p_{S(ν),i}`, `b_{S(ν),i}`, `w_{S(ν),i}`, `h_{S(ν)}` | auxiliary polynomials defining the CRT decomposition |
| `A_S` | `F_q(ν_1,…,ν_ℓ)` — the field component |

**Blueprint equivalent.** `R_e = F_{q²} + uF_{q²} + … + u^{e−1}F_{q²}`, `u^e = 1`,
`e | (q+1)`, is the special case `ℓ = 1`, `t_1(u) = u^e − 1` over `F_{q²}`, with
`N = e`. **The blueprint's `e` is this `N`, not S1's `e = log_p q`.**

## 3. Codes

| Symbol | Meaning |
|---|---|
| `C` | linear code over `A` or `F_q`; `A`-submodule of `A^n` |
| `C_{S(ν)}` | projection of `C` onto the `S(ν)`-component (`F_q`-code of length `n`) |
| `λ` | unit of `A`; `λ = Σ_S λ_{S(ν)} e_{S(ν)}` |
| `λ_{S(ν)}` | the component of `λ`, an element of `F_q^*` (Lemma 2) |
| `g(x)` | generator polynomial; `g = Σ_S e_S g_S` |
| `h(x)` | parity-check polynomial `(x^n − λ)/g` |
| `g_S`, `h_S` | component generator / parity-check |
| `n` | code length |
| `D_k(n,q,λ)` | **set** of attainable `q`-dimensions of `k`-Galois hulls over `A` |
| `δ_k(n,q,λ)` | S1's prose notation for the same object (Introduction) |

## 4. Inner products — the critical block

| Symbol | Meaning in S1 |
|---|---|
| `⟨α,β⟩_k` | `Σ_{i=0}^{n−1} α_i β_i^{p^k}` — **second slot raised**, first slot linear |
| `C^{⊥_k}` | `{α : ⟨α,c⟩_k = 0 for all c ∈ C}` — so `C^{⊥_k} = (C^{(p^k)})^⊥` |
| `hull_k(C)` | `C ∩ C^{⊥_k}` |
| `k`-Galois LCD | `hull_k(C) = {0}` |
| `k`-Galois dual-containing | `C^{⊥_k} ⊆ C`, i.e. `hull_k(C) = C^{⊥_k}` |
| `k`-Galois self-orthogonal | `C ⊆ C^{⊥_k}`, i.e. `hull_k(C) = C` |

**Special cases (S1, p.6):** `k = 0` is Euclidean;
`k = e/2` with `e` even is **Hermitian** (`y ↦ y^{p^{e/2}} = y^{√q}`).

**Blueprint/Yadav et al. convention:** ambient field `F_{q²}`, Hermitian
`y ↦ y^q`, which in S1's parametrisation is `k = 1` with `e = 2`.
Both descriptions coincide; the *letters* do not.

**Hazard (F6).** Because the form is asymmetric, swapping the slots changes
`C^{⊥_k}` as a subspace. All recomputations here use S1's convention.

## 5. Factor-orbit data

| Symbol | Meaning |
|---|---|
| `f_{ij}(x)` | the `i`-th irreducible factor of degree `ord_j(q)` in class `(t,j)` |
| `f^#(x)` | conjugate-reciprocal: `Σ f_i^{p^{e−k}} x^{n−i}` up to the normalising scalar |
| `f^{(a)#}` | `a`-fold iterate of `#` |
| `ord_j(q)` | multiplicative order of `q` modulo `j`; equals `deg f_{ij}` |
| `A` (set) | `{j : gcd(j,q)=1, j | n'r, gcd(n'r/j, r) = 1}` |
| `B_i` | `{j : i` least positive integer with `j | (p^{e l_1} + (−1)^{i−1} p^{i(e−k)})}` for some `l_1 ≥ 0`} |
| `D_{S t}` | `A_{S(ν)} ∩ B_{a_t}` |
| `β_{S t}(j)` | number of `i`-indices, `= φ(j)a_t/(φ(r_S) ord_j(q))` `[OCR-SUSPECT on the position of a_t]` |
| `Δ_{S t}` | `Σ_{j∈D_{S t}} Σ_i deg f_{ij}` |
| `u_{S t i j δ}` | exponent of `(f^{(δ)#}_{ij})` in `g_S`, `0 ≤ u ≤ p^{e'}` |
| `b_{S t i j}` | hull contribution of one irreducible block, `= a_t p^{e'} − Σ_δ max{u_δ, p^{e'}−u_{δ−1}}` |
| `b_{S t j}` | `Σ_i b_{S t i j}` |

**Dimension bookkeeping:** `dim_q C_S = n − deg g_S`; `dim_q hull_k(C_S) = n − deg lcm(g_S, h_S^#)`.

## 6. Gray map and quantum codes

| Symbol | Meaning |
|---|---|
| `ψ` | `A → F_q^N`, `a ↦ (a_{S(ν_1)},…,a_{S(ν_N)})·M` |
| `M` | `M ∈ GL_N(F_q)` with `M (M^{(p^k)})^T = γ I_N` |
| `M^{(p^k)}` | entrywise `p^k`-power of `M` |
| `w_G`, `d_G` | Gray weight / distance: `w_G(a) = w_H(ψ(a))` |
| `[[n,k,d;c]]_q` | EAQECC: length, dimension, distance, `c` pre-shared ebits |
| `D` | `ψ(C)` |

**Field bookkeeping for quantum parameters:** in Theorem 10, `nN` is the
**physical** length over `F_q`, and `dim_q hull_k(C)` is the **ring-level** hull
dimension. This is legitimate only because `ψ` is a `k`-Galois isometry (Lemma 9).

## 7. Symbols that collide

| Symbol | Meaning 1 | Meaning 2 | How to disambiguate |
|---|---|---|---|
| `e` | `q = p^e` (S1) | number of components of `R_e` (blueprint) | S1's `e` is `log_p q`; blueprint's is `N` |
| `q` | `|F_q|` (S1) | `|F_{q²}|` base (Yadav) | check whether the field is written `F_q` or `F_{q²}` |
| `k` | Galois exponent (S1) | `k = e/2` Hermitian case | always `0 ≤ k < e` |
| `A` | the ring (S1) | the set `{j : …}` in §2.4 (S1) | context: roman vs calligraphic |
| `D_t` | `A ∩ B_{a_t}` | `D_k(n,q,λ)`, the dimension set | subscript pattern |
| `l` | even integer of §2.4 | `l` = code dimension in Theorem 1 | Theorem 1 only |
| `d` | minimum distance | `d` as dummy index | context |

## 8. Conventions fixed for this project

1. `q = p^e` refers to S1's ambient field unless explicitly written `F_{q²}`.
2. Hermitian means `k = e/2` (S1) ⟺ `k = 1, e = 2` in the `F_{q²}` model.
3. Dimensions written `dim_q` are `F_q`-dimensions; `dim_A` is never used because
   `A`-modules here are free and the two agree only when stated.
4. A "code" is a subspace, never a generator polynomial; the bijection is Theorem 3.
5. All counts are of **labeled** codes (distinct subspaces), never of isometry
   classes. Isometry-class counts are a different and harder question (see
   `JOINT_ENUMERATOR_FEASIBILITY.md` §4).
