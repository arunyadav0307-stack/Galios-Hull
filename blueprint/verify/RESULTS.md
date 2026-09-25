# Computational evidence log (`blueprint/verify/`)

All numbers quoted in the blueprint come from these scripts. Python 3, no external
mathematics dependency except for the tiny field/polynomial library `fflib*.py`
(written for this purpose; not imported from any solver). Reproduce with

```bash
cd blueprint/verify
/home/user/.venv-papers/bin/python -u verify_all.py        # structural claims A1/A2/A3/B/C
/home/user/.venv-papers/bin/python -u verify_mechanism.py  # window/syndrome sweep + flagship
/home/user/.venv-papers/bin/python -u verify_syndrome.py   # independent syndrome + CRT-lcm case
/home/user/.venv-papers/bin/python -u verify_params.py     # exact quantum parameters (brute force)
```

| # | Claim verified | Script | Scale | Outcome |
|---|---|---|---|---|
| A1 | For every unit λ ∈ F_q\* and every s = p^κ: the σ_s-dual of every nontrivial λ-constacyclic code is λ-constacyclic **iff** λ^{p^κ+1} = 1 | `verify_all.py` | 1010 tests, q ∈ {3,4,5,7,8,9}, n = 3..7, all λ, all κ | 0 failures |
| A2 | C^{⊥σ_s} = ⟨h^τ⟩ with h = (x^n − λ)/g and h^τ = x^l h(1/x)^{σ_s} | `verify_all.py`, `exp_dual2.py` | 1010 + 488 codes | 0 failures |
| A3 | C^{⊥σ_s} ⊆ C ⟺ h^τ ∈ ⟨g⟩_{R_λ} (membership computed by linear algebra, not by divisibility) | `verify_all.py` | 1010 tests | 0 failures |
| A3-neg | The *rejected* criterion gcd(g, rev(g^{p^{e−κ}})) = 1 is **not** equivalent to C^{⊥σ} ⊆ C | `verify_all.py` | 1010 tests | 268 disagreements — criterion rejected |
| B | ord_f(x) = r·h with h | n, r = ord(λ), gcd(r, n/h) = 1 | `verify_all.py` | 2000 tests | 0 failures |
| M1 | Window at misalignment a is a scalar multiple of the λ-constacyclic shift τ^{−a}(v) of the content word v ∈ C | `verify_mechanism.py` | 1262 configurations (all chains C ⊆ D with C, D dual-containing; q ∈ {2,3,4,5,7,8,9}, n = 3..7, all admissible λ and κ) | 0 failures |
| M2 | Receiver syndrome J = (window / g_D) mod f equals **exactly** x^{−a} ∈ R_λ/(f), independent of the content word | `verify_mechanism.py` (independent expected value) + `verify_syndrome.py` | 1262 + 12 individual instances incl. maximal windows | 0 failures; no scalar correction needed |
| M3 | Distinctness of syndromes ⟺ a_l + a_r < ord_f(x) | `verify_mechanism.py`, `verify_syndrome.py` | same sweeps | 0 failures |
| CRT | For a two-component algebra A = F_q × F_q the ring tolerance is lcm(ord_{f_1}, ord_{f_2}) | `verify_syndrome.py` | q = 4, n = 7, λ = (ω,1), orders (21,7): 21 shifts in [−10,10] | 21 distinct syndrome pairs, 0 collisions |
| CRT-jit | The lcm law is stable under unequal component offsets (a+δ_1, a+δ_2), δ_i ∈ {0,1} | `verify_params.py` companion check | orders (21,7) | injective on every window of length 21 |
| P1 | Flagship classical data (F_4, n = 7): x^7 − ω has factors of degree 1,3,3,4,4,6,7 with ord(x) = 3,21,21,21,21,21,21; the degree-3 factors give [7,4,3]_4 codes containing their Hermitian dual (dual code [7,4]_4, d = 4) | `verify_params.py` | exact | see blueprint Table 4 |
| P2 | Flagship ring code ψ(C) ⊆ F_4^{14}: dim 8, Hermitian dual-containing, quantum [[14, 2, 3]]_2 (distances by exhaustive search over all 4^8 codewords) | `verify_params.py` | exact | [14,2,3]_2 |
| P3 | Tolerance of the flagship ring example: lcm(21,7) = 21 ⇒ T ≤ 20 while the component block length is n = 7 (so T > n, and T/L = 0.588 at maximal length 34 qubits) | `verify_params.py`, `verify_mechanism.py` | exact | see blueprint Table 5 |

Refuted along the way (do **not** appear in the blueprint as true statements):

* "λ^{p^κ+1} = 1 ⇒ every λ-constacyclic code contains its σ_κ-dual" — false
  (`verify_core.py`: q = 8, n = 7, λ = 1, p^κ = 4, deg g ∈ {6,7}). The correct
  statement is A1 (the *dual* is λ-constacyclic) plus A3 (containment criterion).
* "gcd(g, rev(g^{p^{e−κ}})) = 1 ⟺ C^{⊥σ} ⊆ C" — false (268/1010).
* A first draft of the padding rule (no λ-twist in the periodic continuation,
  and a reversed x^{−1} operator in my own checker) produced spurious syndrome
  mismatches. Both errors were in the checker; the corrected rule and the
  corrected operator give M2 with multiplier exactly 1. The blueprint states the
  corrected rule only.

---

# Results added during the external audit (September 2026)

Scripts added in this round: `verify_padding_lcm.py`, `verify_flagship2.py`, `jitter.py`.
These supersede the corresponding claims of the earlier round; consult this section first.

| # | Claim verified | Script | Scale | Outcome |
|---|---|---|---|---|
| M1' | **Exact padding identity** `W_a(w) = x^{-a}·w` in `R_λ` for the **λ⁻¹-periodic** continuation | `verify_padding_lcm.py` | 9192/9192 | exact; the (wrong) λ-periodic convention satisfies only 5216/9192, i.e. it is off by a drift factor — hence the convention in Definition 7.7 of the final blueprint |
| M2' | **Exact syndrome identity** `J_a mod f = x^{-a}` (no scalar), content-free for `w ∈ C + g_D`; general formula `x^{-a}·((v/g_D) mod f)` for `v ∈ D` | `verify_padding_lcm.py` | 166 528/166 528 exact identities; 53 823 content-free chain/shift pairs; 124 260 general-formula checks | 0 failures |
| L1' | **lcm tolerance law** (abstract): injectivity on a window of `T+1` shifts ⟺ `T < lcm(o_i)` | `verify_padding_lcm.py` | orders (3),(7),(21,7),(21,21),(3,7),(4,6),(5,7,3),(2,4,8) | no mismatch with `T < lcm` |
| L2' | **CRT case** `A = F_4 × F_4`, `λ = (ω,1)`, orders `(21,7)`: 21 distinct syndrome pairs, 0 collisions, collision exactly at `a = Θ = 21` | `verify_flagship2.py` | all shifts in `[-10,10]` and the pair `{0,21}` | as stated |
| L3' | **Order invariant** used by the ceiling theorem: `ord_f = r·h`, `h | n`, `r = ord(λ)`, `gcd(r, n/h)=1` (earlier round 2000/2000) | `verify_all.py` | — | unchanged |
| F1' | **Flagship A (binary, Hermitian)** `q = 4, n = 7, λ = ω, κ = 1`: `x^7 − ω` has factors of degrees 1,3,3 (orders 3,21,21); the two degree-3 divisors give `[7,4,3]_4` with `C^{⊥H} ⊆ C`, `d(C^{⊥H}) = 4`, `d(C \ C^{⊥H}) = 3`; unpadded quantum `[[7,1,3]]_2`; padded at maximal tolerance `[[54,2,3]]_2`, `T = 20 > n = 7`, `T/L = 0.741` | `verify_flagship2.py` (independent F_4/F_2 implementation) | exact, distances by exhaustive enumeration | confirmed; **correction** of the earlier round's logical-qubit bookkeeping (`[[14,4,3]]_2` → `[[14,2,3]]_2`, and the padded length was previously conflated with 14) |
| F2' | **Flagship B (ququart, Hermitian)** `q = 16, n = 7, λ = ζ_5` (order 5 = `p^κ+1`, `κ = 2`): dual-containing degree-3 divisor with `ord_f = 35 = 5·7`; `[7,4,3]_{16}`, `C^{⊥H} ⊆ C`, unpadded `[[7,1,3]]_4`; padded at maximal tolerance `[[164,1,3]]_4`, `L = 41` symbols, `T = 34 > n`, `T/L = 0.829` | `verify_ceiling.py` (promoted to a standalone script; reproduces every number, incl. the cyclic control) | exact | confirmed |
| J1' | **Jitter/ambiguity criterion**: for orders `(21,7)` no genuine ambiguity for jitter ≤ 1 (gcd 7); for coprime orders (e.g. `(3,7)`) a non-constant jitter difference mimics a shift | `jitter.py` | 8 order patterns | as stated; degenerate pure-reparametrisation class `a + δ_i = θ_i` identified |
| N1' | **Negative results**: `F_4, n=3, λ=ω` admits no nontrivial tolerant chain; `q = 25, n = 3` admits no dual-containing component for `r ∈ {1,2}`; no `HA > 1` dual-containing example found for `q ∈ {4,9,16}`, `n ≤ 11` | several scripts | small sweeps | reported as negative evidence for the search plan (task T14) |

**Corrections of record (from this round).** (i) the padding convention (drift); (ii) the
`x^{-a}` operator's exponent reduction; (iii) the logical-qubit bookkeeping for Hermitian codes
over `F_4`; (iv) the causal explanation of the "cyclic ceiling" (λ = 1, not the number of
components); (v) `poly.mod`-based containment checks are to be replaced by the span form
(`h^τ` vs `⟨g⟩`), as in the earlier round.
