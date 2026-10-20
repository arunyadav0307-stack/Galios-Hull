# SOURCE_EXAMPLE_RECALCULATION

Independent recomputation of **all three** worked examples of `[S1]`, from scratch,
with a hand-written exact finite-field library (`code/gf.py`). No computer-algebra
system was used or available.

**Method.** Codes are built as subspaces, not manipulated symbolically:

1. `GF(p, m, modulus)` with the **paper's own** defining polynomials
   (`ω² + 2ω + 2 = 0` over `F_3`; `ω² + 4ω + 2 = 0` over `F_5`).
2. Irreducible factorization by square-free decomposition + Cantor–Zassenhaus.
3. A `λ`-constacyclic code `⟨g⟩` is realised as the row space of
   `x^i g(x) mod (x^n − λ)`, `i = 0,…,n−deg g−1`.
4. `C^{⊥_k}` is computed as the nullspace of the matrix of `c^{(p^k)}`, `c ∈ C`
   (S1's slot convention, `⟨α,β⟩_k = Σ α_i β_i^{p^k}`).
5. `dim hull_k(C) = dim C + dim C^{⊥_k} − dim(C + C^{⊥_k})`, all by exact row
   reduction.
6. Minimum distances are computed **exactly** from the parity-check matrix, by
   testing all `w`-subsets of columns for linear dependence — no random search.

Raw output: `verification/verify_example1.out`, `verification/verify_examples.out`.

---

## Example 1 `[S1 p.5–6]` — idempotents of `A_1`

`A_1 = F_2[x_1,x_2]/⟨t_1,t_2⟩`, `t_1 = x_1^5+x_1^4+1 = (x_1^2+x_1+1)(x_1^3+x_1+1)`,
`t_2 = x_2^4+x_2^2+x_2 = x_2(x_2^2+x_2+1)`.

| Check | Result |
|---|---|
| six displayed elements parse in `A_1` | **yes** |
| `e_i² = e_i` for all six | **PASS** |
| `e_i e_j = 0` for `i ≠ j` | **PASS** |
| `Σ e_i = 1` | **PASS** |

Six primitive orthogonal idempotents, as claimed, consistent with six Frobenius
classes. *(The paper does not display the six-component decomposition explicitly;
the count 6 matches `|Ŝ|`.)*

---

## Example 2 `[S1 p.18–20]` — `q = 9`, `n = 7`, `k = 1` (**Hermitian**, since `e = 2`)

Ring `R = F_9[x_1,x_2]/⟨x_1²+x_1+ω, x_2²+ω^5x_2+2⟩`, `N = 2`;
`λ = e_1 + ω²e_2`, so `λ_1 = 1`, `λ_2 = ω²`, `r_1 = 1`, `r_2 = 4`.
`g_1 = x³+ω³x²+ω⁵x+2`, `g_2 = x + ω²`.

| Check | Paper | Recomputed |
|---|---|---|
| `ω` primitive, order 8 | implicit | **yes**, `ω⁴ = −1`, `ω⁸ = 1` |
| `x^7−1` factor degrees | `1,3,3` | **`1,3,3`** |
| `x^7−ω²` factor degrees | `1,3,3` | **`1,3,3`** |
| `g_1 | x^7−1` | yes | **yes** |
| `g_2 | x^7−ω²` | yes | **yes** |
| `dim C_1`, `dim C_2` | 4, 6 (from `deg g`) | **4, 6** |
| `dim hull_1(C_1)` | 0 | **0** |
| `dim hull_1(C_2)` | 0 | **0** |
| total `dim_9 hull_1(C)` | **0** | **0** |
| `M(M^{(3)})^T = γI_2` | required | **yes**, `γ = 1` |
| `ψ(C)` | `[14,10,4]_9` | **`[14,10,4]_9`** |
| EAQECC | `[[14,10,4;4]]_9` | **`[[14,10,4;4]]_9`** |

**Exact distance certificate:** the parity-check matrix is `4 × 14`; every 3-column
set is independent, and a dependent 4-column set exists (columns `0,1,2,3`). Hence
`d = 4` exactly. This is a proof for this instance, not a search heuristic.

**Discrepancy found — `[S1-TYPO-4]` (see audit F2).** The paper writes
`β_{11}(7) = 3` and `β_{21}(28) = 3`. Both are **2**: the displayed factorizations
have exactly two cubics in each case, and the paper's own expansions
`b_{117} = b_{1117}+b_{1127}` and `b_{2128}=b_{21128}+b_{21228}` have exactly two
terms. The error does not propagate: `b_{117} = b_{2128} = 0` either way, and the
final hull dimension is `0` in both readings.

**Cross-check that the Galois parameter matters.** The *Euclidean* (`k=0`) hull
dimension of the same `C_1` is **3**, not 0. So the `k = 1` hypothesis is doing real
work, and a recomputation with the wrong `k` would not reproduce the paper.

---

## Example 3 `[S1 p.20–21]` — `q = 25`, `n = 13`, `k = 1` (**Hermitian**, `e = 2`)

Ring `R = F_25[x_1,x_2]/⟨x_1²+x_1+ω^13, x_2²+ω³x_2+1⟩`, `N = 2`;
`λ = e_1 + ω⁸e_2`, `r_1 = 1`, `r_2 = 3`;
`g_1 = (x+4)(x²+ωx+1)`, `g_2 = x+ω^20`.

| Check | Paper | Recomputed |
|---|---|---|
| `ω` order | 24 (used) | **24** |
| `x^13−1` factor degrees | `1` + six quadratics | **`1` + six quadratics** |
| `x^13−ω⁸` factor degrees | `1` + six quadratics | **`1` + six quadratics** |
| `g_1 | x^13−1`, `g_2 | x^13−ω⁸` | yes | **yes** |
| `dim C_1`, `dim C_2` | 10, 12 | **10, 12** |
| `dim hull_1(C_1)` | 2 (via `b_{1213}=1`, `ord_13(25)=2`) | **2** |
| `dim hull_1(C_2)` | 0 | **0** |
| total `dim_25 hull_1(C)` | **2** | **2** |
| `M(M^{(5)})^T = γI_2` | required | **yes**, `γ = 1` |
| `ψ(C)` | `[26,22,4]_25` | **`[26,22,4]_25`** |
| EAQECC | `[[26,20,4;2]]_25` | **`[[26,20,4;2]]_25`** |

**Distance certificate:** `4 × 26` parity check; all 3-column sets independent,
a dependent 4-column set exists (`0,1,2,3`); hence `d = 4` exactly.

*Note on attribution:* the non-zero hull contribution sits in **component 1**
(`b_{1,2,13} = 1`, weight `ord_13(25) = 2`), not component 2. Misreading the
double-subscript notation as `b_{12,13}` instead of `b_{1,2,13}` would put it in the
wrong component. The recomputation confirms `C_1` (the `λ_1 = 1` component) is the
one with hull dimension 2.

---

## Corollary 3.4 / 3.5 — brute-force tests

`verification/verify_corollary_3_5.out`.

### Test 1 — Corollary 3.5(1), `p` odd, `n' = 1`
`q = 9`, `p = 3`, `e = 2`, `e' = 2`, `n = 9`, `k = 1`, `λ ∈ {1, −1}`.
Single-field attainable sets: `D_1 = {0,1,2,3,4}` for **both** multipliers, with
multiplicities `{0:2, 1:2, 2:2, 3:2, 4:2}` (10 codes each, i.e. 10 divisors of
`x^9 − λ = (x − ·)^9`).

Ring `A = F_9[x]/⟨x²−1⟩` (`N = 2`), `λ = e_1+e_2`: attainable set `= {0,…,8}`,
cardinality **9**; predicted `N(n−1)/2 + 1 = 2·4+1 = 9`. **PASS.**

### Test 2 — Corollary 3.5(2), `p = 2`, `e` even, `k = e/2`
`q = 4`, `e = 2`, `k = 1`, `n' = 1`, `e' = 2`, `n = 4`, `λ = ω` (`ord = 3 | 3`).
Single-field set `D_1 = {0,1,2}` with multiplicities `{0:2, 1:2, 2:1}` (5 divisors).
Ring `A = F_4[x]/⟨x²+x+ω⟩`, `N = 2`: attainable set `{0,1,2,3,4}`, cardinality
**5**; predicted `Nn/2 + 1 = 4+1 = 5`. **PASS.**

Both tests were run in regimes satisfying every printed hypothesis, including the
`e' ≥ 1` condition that F3 shows is missing from the statement of part 2.

### Test 3 — the product/factorisation property (Theorem 7)
Same ring, `λ = e_1 + ωe_2`, constituent multipliers `1` and `ω`.
Local distributions `{0:2, 1:2, 2:1}` for each.

| | distribution |
|---|---|
| convolution of locals | `{0:4, 1:8, 2:8, 3:4, 4:1}` |
| direct enumeration over `A` | `{0:4, 1:8, 2:8, 3:4, 4:1}` |
| total number of codes | `25 = 5 × 5` |

**PASS.** The joint hull-dimension distribution is exactly the convolution of the
constituent distributions. This is Theorem 7 plus Theorem 3, and it is the
mathematical content of the "joint enumerator" — see
`JOINT_ENUMERATOR_FEASIBILITY.md` §3.

---

## Model caveat — read before using the tables above (see audit F11)

The recomputation above reproduces S1's numbers **within S1's own model**, i.e.
treating each idempotent component as contributing `n − deg g_S` many `F_q`
dimensions. That model is exactly the one S1 uses in §2.3 and in the Gray map.

It is **not** the model that the ring `A` actually forces when some `t_i` is
irreducible of degree `> 1`. In Examples 2 and 3, `t_1` is irreducible of degree 2
over `F_q` (verified above), so each component field is `F_{q²}`, `dim_q A = 4`,
while S1 uses `N = 2`. Under the correct bookkeeping:

- an `A`-submodule with component dimensions `(4, 6)` has `dim_q = 20`, not `10`;
- `ψ : A → F_q^2` cannot be injective.

So the entries marked **PASS** above certify that *S1's arithmetic is internally
consistent and reproducible*, **not** that the displayed codes are the Gray images
of the stated ring's modules. The distinction is essential; see audit finding F11
and `JOINT_ENUMERATOR_FEASIBILITY.md` §2.3.

Because all displayed hull dimensions in Example 2 are `0`, the Example 2 hull
statement is unaffected numerically. Example 3 is affected in principle; its
displayed value `2` is the component-dimension count, and the `F_q`-dimension
would carry an extra factor `|S(ν)| = 2`.

### Scope of each verification, stated individually

Added 2026-10-20 after independent re-derivation. "Model-valid" means the script's
model of `A` matches the ring actually described in the paper.

| Script / test | Ring actually used | Model-valid? | What it therefore proves |
|---|---|---|---|
| `code/verify_example1.py` | `A_1 = F_2[x_1,x_2]/⟨t_1,t_2⟩`, all `t_i` split | **yes** | the six idempotents are correct |
| `code/verify_examples.py` — hull values | components treated as `F_q` | **no** (Ex. 2, 3) | the paper's `0` and `2` are the correct `Σ_S dim_{A_S}` values |
| `code/verify_examples.py` — `psi(C)` rows | components treated as `F_q` | **no** | that the `F_q`-component model yields `[14,10,4]_9` and `[26,22,…]_25`. It does **not** prove these are Gray images of the `A`-modules |
| `code/verify_corollary_3_5.py` Test 1 | `A = F_9[x]/⟨x²−1⟩`, and `x²−1` **splits** | **yes** | Corollary 3.5(1), genuinely |
| `code/verify_corollary_3_5.py` Test 2 | `A = F_4[x]/⟨x²+x+ω⟩`, which is **irreducible** ⇒ `A ≅ F_16`, a field | **no** | only that the paper's `F_q`-model satisfies its own formula |
| `code/verify_corollary_3_5.py` Test 3 | same ring as Test 2 | **no** | additivity of hull dimensions (true by Theorem 7), not the numerical `25 = 5×5` for `A` |
| `code/independent_verification.py` | `A` built explicitly; real `A`-module | **yes** | `dim_q C = 20`, `44`; `ψ` not injective; Cor 3.5(2) fails at `e'=0` |

In short: **two of the seven checks are model-valid tests of the ring; the rest are
tests of the paper's arithmetic under its own assumption.** Both kinds are useful;
they must not be confused.

---

## What the recomputation does and does not establish

**Does:** the numerical content of all three examples, both corollaries, Lemma 9 and
the additivity theorem are correct and reproducible.

**Does not:** establish novelty of anything. Every item recomputed is a *check* of
a published claim, not a new result. In particular the factorisation verified in
Test 3 is a restatement of Theorem 7 and Theorem 3 — it is exactly the reason the
"joint enumerator" cannot be new (next document).
