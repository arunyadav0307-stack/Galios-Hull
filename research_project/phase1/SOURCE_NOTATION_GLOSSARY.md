# SOURCE NOTATION GLOSSARY

**Source:** Yadav, Singh, Islam, Prakash, Solé (2024), DOI `10.1007/s40314-024-02789-1`, **version `hal-04825601v1`** (HAL author deposit). `p.N` = physical PDF page; printed page = N − 1.
**Purpose:** fix every symbol the paper uses, with its domain and first page of use, and record **overloads** rather than silently resolving them. Where the extracted corpus mangles a symbol (fraction bars, superscripts, `ε` → `ϵ`, `⊥_H` → `⊥H`, `Σ` → `P`), the glossary states the symbol as it is meant to be read and the paper's usage that forces that reading.

---

## 1. Global parameters

| Symbol | Meaning | Domain | Quantifier scope | First use |
|---|---|---|---|---|
| `p` | an odd prime; the characteristic | prime | global | p.4 |
| `m` | exponent with `q = p^m` | ℕ | global | p.4 |
| `q` | `p^m`; **the quantum codes are over `F_q`** | prime power | global | p.4 |
| `q²` | order of the field the classical codes live over | prime power | global | p.4 |
| `F_{q²}` | the field of the ring coefficients; also written `F_q[t]` (see `t`) | field | global | p.4 |
| `F_q` | subfield; alphabet of the resulting **quantum** codes | field | §4 on | p.3 |
| `e` | the ring exponent: `R_e = ⊕_{k<e} u^k F_{q²}`; must satisfy `e | q+1` | ℕ, `e ≥ 2` | global for `R_e` parts | p.4 |
| `v` | exponent with `n = p^v n'`, `p ∤ n'` | ℕ₀ | global for `n` | p.8 |
| `p^v` | written `pv` in the extracted text; the multiplicity of every irreducible factor of `x^n − α` | ℕ | global | p.8–9 |
| `n` | length of the constituent codes over `F_{q²}`; `ψ(C)` has length `en` (`2n` if `e = 2`) | ℕ, `gcd(n,p)` not always 1 | per construction | p.4 |
| `n'` | `n/p^v` | ℕ, coprime to `p` | global for `n` | p.8 |
| `t` | a **primitive element** of `F_{q²}`, used in every example and table | `F_{q²}*` | per example/table | p.15 |

## 2. The rings and their idempotents

| Symbol | Meaning | Domain | Scope | First use |
|---|---|---|---|---|
| `R_2` | `F_{q²} + uF_{q²}`, `u² = 1` | ring | §2–§4, e = 2 parts | p.4 |
| `R_e` | `F_{q²} + uF_{q²} + … + u^{e−1}F_{q²}`, `u^e = 1` | ring | §2–§4 general | p.4 |
| `u` | the ring generator with `u^e = 1` (so `1 − u` is a **zero divisor**) | `R_e` | global | p.4 |
| `γ` | **overload**: (a) the scalar with `2γ ≡ 1 (mod p)`, i.e. `γ = 1/2`, used to build `ε_i`; (b) the counting function `γ(j)` of §3 | `F_{q²}` (a) / `ℕ → ℕ` (b) | (a) p.4, (b) p.9 | p.4 |
| `ε₁, ε₂` | `γ(1+u)`, `γ(1−u)` — the two orthogonal idempotents of `R_2`, `ε₁+ε₂ = 1` | `R_2` | e = 2 | p.4 |
| `η_i` | `(u^e−1)/(u−μ^{i−1})`, `1 ≤ i ≤ e` — the **unnormalised** CRT idempotents of `R_e` (see warning below) | `R_e` | e ≥ 2 | p.4 |
| `μ` | a primitive `e`-th root of unity in `F_{q²}` | `F_{q²}*` | e ≥ 2 | p.4 |
| `R*_e` | the units of `R_e` = elements whose `e` components are all nonzero | group | global | p.4 |
| `I_e` | identity matrix of order `e` | `M_e(F_{q²})` | §2 | p.7 |
| `ε_i`, `η_l` (index letter) | the paper uses `i` for `R_2` components and `l` for `R_e` components (`1 ≤ l ≤ e`); `i` is *also* the factor index inside `Ω` | — | — | p.10–12 |

> **Warning — `η_i` is not idempotent as printed.** For `e = 3` the printed `η_i` satisfy `Σ η_i = 3u² ≠ 1`; each is a nonzero scalar multiple of a genuine idempotent (verified: factors `8, 3, 24` in Example 3). All uses in the paper are of the form `η_i C_i`, so the scalar is absorbed. See `SOURCE_MATHEMATICAL_AUDIT.md` item 2. The `R_2` case is normalised correctly through `γ = 1/2`.

## 3. Constacyclic structure

| Symbol | Meaning | Domain | Scope | First use |
|---|---|---|---|---|
| `α` | multiplier of the `α`-constacyclic code; order `r` | `F_{q²}*` | per construction | p.4 |
| `α_l` | multiplier for the `l`-th component of an `R_e` code; order `r_l` | `F_{q²}*` | `1 ≤ l ≤ e` | p.8 |
| `r` | multiplicative order of `α`; **must satisfy `r | q+1`** so that `C^{⊥H}` is again `α`-constacyclic | ℕ | per construction | p.4 |
| `r_l` | order of `α_l`, `r_l | q+1` | ℕ | `1 ≤ l ≤ e` | p.8 |
| `λ` | multiplier of the `λ`-constacyclic code over `R_e`: `λ = Σ η_l α_l` | `R*_e` | per construction | p.5 |
| `τ_λ` | the constacyclic shift `(c₀,…,c_{n−1}) ↦ (λc_{n−1}, c₀, …, c_{n−2})` | map | §2.2 | p.5 |
| `g(x)`, `g_l(x)` | generator polynomial of the (constituent) constacyclic code, monic, dividing `x^n − α` | `F_{q²}[x]` / `R_e[x]` | per code | p.5 |
| `x` | the polynomial variable | — | global | p.4 |
| `p^†` (also `·^†`) | conjugate-reciprocal: `p^†(x) = a₀^{−q} Σ_{i} a_i^q x^{s−i}` for `p = Σ a_i x^i` of degree `s` | `F_{q²}[x] → F_{q²}[x]` | global | p.4 |
| `q` (in `·^†`) | **the exponent is `q`, not `q²`** — because the Hermitian form uses `y^q` over `F_{q²}` | — | global | p.4 |

## 4. Counting functions and index sets (`n'r` indexing)

| Symbol | Meaning | Domain | Scope | First use |
|---|---|---|---|---|
| `φ` | Euler's totient function | `ℕ → ℕ` | §3 | p.9 |
| `ord_j(q²)` | multiplicative order of `q²` in `(ℤ/jℤ)*`; **defined as `ord₁(q²) = 1`** | `ℕ → ℕ` | `j` coprime to `q²` | p.9 |
| `π(j, q²)` | `0` if `j | (q^{2k}+q)` for some `k ≥ 0`, else `1` | `ℕ → {0,1}` | §3 | p.8 |
| `Ω` | `{ j : j | n'r, π(j,q²) = 0, gcd(n'r/j, r) = 1 }` — indices of **self-CR** irreducible factors | set of ℕ | §3 | p.8 |
| `Ω'` | the same with `π = 1` — indices of **CR pairs** | set of ℕ | §3 | p.9 |
| `Ω_l, Ω'_l` | the `α_l`-versions, built on `n'r_l` and `r_l` | sets | `1 ≤ l ≤ e` | p.12 |
| `S_{q²}` | `{ j ≥ 1 : j | (q^{2k}+q) for some k ≥ 0 }` — the `π = 0` set; note `π(j,q²) = 0 ⟺ j ∈ S_{q²}` | set of ℕ | §3 | p.13 |
| `γ(j)` | `φ(j)/(φ(r)·ord_j(q²))` — number of self-CR factors of degree `ord_j(q²)` | `ℕ → ℕ` | `j ∈ Ω` | p.9 |
| `β(j)` | `φ(j)/(2φ(r)·ord_j(q²))` — number of CR **pairs** of that degree | `ℕ → ℕ` | `j ∈ Ω'` | p.9 |
| `γ_l(j), β_l(j)` | the same with `r_l` in place of `r` | `ℕ → ℕ` | `j ∈ Ω_l, Ω'_l` | p.12 |
| `N` | the set of positive integers | set | p.9 | p.9 |
| `s`, `t` | **overloads**: (a) `s` = number of self-CR polynomials and `t` = number of CR pairs (p.9); (b) `s` = degree of a polynomial `p(x) = a₀ + … + a_s x^s` (p.4); (c) `t` = a primitive field element in all examples/tables (p.15) | ℕ (a,b) / field element (c) | — | p.4, p.9, p.15 |

> **`nr` in Theorem 11 / Corollary 12 / 13 / 14.** Printed without a multiplication sign. It is the **product `n·r`**: the proof speaks of "each divisor of `nr`", the factorisation is indexed by `j | n'r`, and the numerical test in the audit only closes under the product reading.
> **Extraction artefact.** The fractions `φ(j)/(φ(r)ord_j(q²))` and `φ(j)/(2φ(r)ord_j(q²))` appear in the corpus as `ϕ(j)ϕ(r)ordj(q2)` and `ϕ(j)2ϕ(r)ordj(q2)` (p.9); the quotient reading is the only one consistent with the paper's own totals (6 and 3 in Example 1) and with `n = Σ_Ω ord_j γ(j)p^v + Σ_{Ω'} 2ord_j β(j)p^v`.

## 5. Factorisation symbols

| Symbol | Meaning | Domain | Scope | First use |
|---|---|---|---|---|
| `g_ij` (also `g^{(l)}_{ij}`) | the `i`-th **self-CR** irreducible factor at index `j ∈ Ω`, degree `ord_j(q²)` | `F_{q²}[x]` | `1 ≤ i ≤ γ(j)` | p.9 |
| `f_ij`, `f_ij^†` | a **CR pair** at `j ∈ Ω'`, each of degree `ord_j(q²)` | `F_{q²}[x]` | `1 ≤ i ≤ β(j)` | p.9 |
| `a_ij`, `u_ij` | exponent of `g_ij` in `g₁` (resp. `g₂`) | `0 ≤ · ≤ p^v` | §4 | p.10 |
| `b_ij, c_ij` | exponents of `f_ij`, `f_ij^†` in `g₁` | `0 ≤ · ≤ p^v` | §4 | p.10 |
| `v_ij, w_ij` | exponents of `f_ij`, `f_ij^†` in `g₂` — **`v` here is a coefficient index, not the `p^v` exponent** | `0 ≤ · ≤ p^v` | §4 | p.10 |
| `a^{(l)}_ij, b^{(l)}_ij, c^{(l)}_ij` | the `R_e` versions (per component `l`) | `0 ≤ · ≤ p^v` | `1 ≤ l ≤ e` | p.12 |
| `a_j`, `b_j` | the **aggregated** bound variables of Theorem 8 (summed over the two `R_2` components and over `i`) | ℕ | Thm 8 | p.10 |
| `a^{(l)}_j`, `b^{(l)}_j` | the per-component versions of Theorem 10 | ℕ | Thm 10 | p.13 |

## 6. Codes, duals, hulls

| Symbol | Meaning | Domain | Scope | First use |
|---|---|---|---|---|
| `C₁, C₂, C_l` | the constituent linear codes over `F_{q²}` | subspaces of `F_{q²}^n` | — | p.5 |
| `C = ε₁C₁ ⊕ ε₂C₂` | the code over `R_2`; `= Σ η_l C_l` for `R_e` | submodule of `R_e^n` | — | p.5 |
| `C^{⊥H}` | Hermitian dual: `{x : Σ x_i c_i^q = 0 ∀c ∈ C}` | code | global | p.4–5 |
| `Hull_H(C)` | `C ∩ C^{⊥H}` — the Hermitian hull | code | global | p.5 |
| `⟨x,y⟩_H` | `Σ x_i y_i^q = x y*` — the Hermitian inner product over `R_e` as well as over `F_{q²}` | form | global | p.5 |
| `y*` | `(y₀^q, …, y_{n−1}^q)^T` | vector | global | p.5 |
| `M*` | conjugate transpose `[m_{ji}^q]` (**not** the same as `†`) | matrix | §2 | p.4 |
| `M^T` | plain transpose | matrix | §2 | p.4 |
| `D_{q²}(n)` | the **set** of hull dimensions of `α`-constacyclic codes of length `n` | set of ℕ | §3 | p.13 |

## 7. The Gray map

| Symbol | Meaning | Domain | Scope | First use |
|---|---|---|---|---|
| `ψ` | the Gray map `R_e^n → F_{q²}^{en}`: each coordinate `(s₁ⱼ,…,s_{ej})` is replaced by `(s₁ⱼ,…,s_{ej})M` | map | global | p.6 |
| `s_kij` (printed `s_{k i}`) | the `k`-th CRT component of the `i`-th symbol of a codeword | `F_{q²}` | §2 | p.6 |
| `M` | square matrix of order `e` with `M M* = νI_e`; for `e = 2` the paper uses `[[1,1],[1,−1]]` | `M_e(F_{q²})` | global | p.7 |
| `M(q)`, `M(5)`, `M(11)` | the `e = 3` matrices, tabulated on p.15: `M(5) = [[3,2,1],[3,4,3],[4,3,2]]`, `M(11) = [[7,4,2],[9,7,4],[4,2,4]]` | `M₃(F_q)` | e = 3 | p.15 |
| `ν` | the nonzero scalar in `M M* = νI_e` (verified: `ν = 2` for `M` over `GF(q²)`, `ν = 4` for `M(5)`, `ν = 3` for `M(11)`) | `F_{q²}*` | global | p.7 |
| `w_H`, `d(·,·)` | Hamming weight / distance | ℕ | §2.1 | p.5 |
| `w_G`, `d_G`, `d_G(C)` | Gray weight / distance, **defined as** the Hamming weight/distance of `ψ(·)` | ℕ | §2.2 | p.8 |

## 8. Parameters and bounds

| Symbol | Meaning | Notes | First use |
|---|---|---|---|
| `[n, k, d]_q` | a linear code over `F_q` — **the paper's subscript is `q` even for codes over `F_{q²}`** | overload: the tables write `[24,20,4]_{q²}` for classical codes and `[[·]]_q` for quantum ones; the register quotes each occurrence as printed | p.3, p.5 |
| `[[n, k, d]]_q` | a quantum code over `F_q` | the introduction calls `k` "dimension `q^k`" (p.4), a slip for `q^k` codewords; the tables use `k` as the exponent, consistently with `[[en, 2k−en, ≥d]]` | p.3 |
| `k` | dimension; in Table 3's fifth column, the **quantum** dimension `2k − en` | overload: classical `k` vs quantum `k` | p.5 |
| Singleton bound | `d ≤ n − k + 1`; MDS if equality, near-MDS if `d = n − k` | p.15 | p.15 |
| quantum Singleton bound | `k + 2d ≤ n + 2`; MDS if equality | p.15 | p.15 |
| residual | Table 3's sixth column `en + 2 − (k + 2d)` — the paper's own bookkeeping of the quantum Singleton bound | equals 0 exactly for the one MDS row | p.19 |

---

## 9. Overload register (recorded, not resolved silently)

| Symbol | Use A | Use B | Use C |
|---|---|---|---|
| `γ` | scalar `2γ ≡ 1 (mod p)` (p.4) | function `γ(j)` (p.9) | `γ_l(j)` (p.12) |
| `t` | primitive field element (p.15 onward) | number of CR pairs, `t = p^v Σ β(j)` (p.9) | — |
| `s` | degree of a general polynomial (p.4) | number of self-CR polynomials, `s = p^v Σ γ(j)` (p.9) | — |
| `v` | exponent in `p^v` (p.8) | coefficient `v_ij` in `g₂` (p.10) | — |
| `u` | ring generator, `u^e = 1` (p.4) | coefficient `u_ij` in `g₂` (p.10) | — |
| `k` | classical dimension `[n,k,d]` | quantum dimension in `[[en, k, ≥d]]` | — |
| `x` | polynomial variable | a codeword of `C^{⊥H}` in Lemma 3's proof (p.7) | a vector in the Hamming distance definition (p.5) |
| `q` | `p^m`, the base field size | the exponent in `·^†` and `⟨·,·⟩_H` | the subscript of `[·]_q` also used for `F_{q²}` codes |
| `d` | minimum distance | `d_G` Gray distance | the differential-free `d`, `e`, `f` of Lemma 7 are separate letters (`d` unused there) |
| `e` | ring exponent | — | (in `M M* = νI_e`, the subscript `e` is the matrix order) |
| `M` | Gray matrix of order `e` | `M(q)`/`M(5)`/`M(11)` for ordered 3×3 matrices | — |
| `i` | `R_2` component index `i = 1,2` | factor index `1 ≤ i ≤ γ(j)` | index of a codeword coordinate |
| `l` | `R_e` component index `1 ≤ l ≤ e` | — | — |
