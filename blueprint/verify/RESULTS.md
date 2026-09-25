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
