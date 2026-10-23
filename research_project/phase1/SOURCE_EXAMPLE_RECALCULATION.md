# SOURCE EXAMPLE RECALCULATION

**Source:** Yadav, Singh, Islam, Prakash, Solé (2024), DOI `10.1007/s40314-024-02789-1`.
**Version examined: `hal-04825601v1`** — HAL author deposit, 23 pp., SHA-256 `7f7e6803…c27d249`. `p.N` = physical PDF page (printed page = N − 1).
**Standard applied:** every number below was recomputed with exact field arithmetic (`galois` over `GF(p²)`); nothing was taken from the paper, from Magma, or from a prior audit. Where a computation could not be pushed to a definite answer the entry says so. **No mismatch was "fixed"; there is none to report.**

**Reproduce:**

```bash
python3 research_project/code/phase1_examples.py     # Examples 1-3  -> 31/31 checks PASS
python3 research_project/code/phase1_tables.py       # Tables 1-3    -> 33/33 rows PASS
```

Raw output: `research_project/phase1/raw/examples_log.txt`, `research_project/phase1/raw/tables_recalc.json`.

**Conventions forced by the source itself** (established in `SOURCE_MATHEMATICAL_AUDIT.md`, item 3):

* a printed factor `(x + c)` has root `−c`; `c` is either a literal integer (`x+4`) or a power of a primitive element (`x+t20`);
* `(x+t4)` and `(x+t16)` are the two *primitive* cube roots in Example 3 because `−t⁴ = t¹⁶` and `−t²⁰ = t⁸` in `GF(25)`;
* the conjugate-reciprocal of `(x+c)` is `(x + c^{−q})`, from `p^†(x) = a₀^{−q} Σ a_i^q x^{s−i}` (p.4);
* the Hermitian dual uses the exponent `q`, not `q²`: `C^{⊥H} = {y : Σ_j c_j y_j^q = 0}` over `GF(q²)`;
* the Gray map expands **each coordinate** into `e` symbols (interleaved), `(s₁ⱼ,…,s_{ej}) ↦ (s₁ⱼ,…,s_{ej})M` (p.6).

---

## Example 1 — p.15–16 (`p=5`, `GF(25)`, `n=12`, `α=1`, `r=1`)

| What the paper asserts | Recomputation | Agreement |
|---|---|---|
| `Ω = {1,2,3,6}`, `Ω' = {4,12}`, `ord_j(q²)=1` throughout | `Ω={1,2,3,6}`, `Ω'={4,12}`, all orders 1 | **MATCH** |
| `γ(1)=1, γ(2)=1, γ(3)=2, γ(6)=2` (sum 6) | 1, 1, 2, 2 — sum 6, from `φ(j)/(φ(r)ord_j(q²))` | **MATCH** |
| `β(4)=1, β(12)=2` (sum 3) | 1, 2 — sum 3, from `φ(j)/(2φ(r)ord_j(q²))` | **MATCH** |
| `x¹²−1` = product of the 12 printed linear factors | product equals `x¹²−1` exactly | **MATCH** |
| those 12 split as 6 self-CR + 3 CR pairs `{t²,t¹⁴},{2,3},{t¹⁰,t²²}` | 6 self-CR `{1,t⁴,t⁸,4,t¹⁶,t²⁰}`, 3 pairs exactly as printed (checked with `p^†`) | **MATCH** |
| `g₁ = x³+x²+t⁸x+t⁸ = (x+1)(x+t¹⁰)(x+t²²)` | identity holds | **MATCH** |
| `hull C₁ = 0`, `hull C₂ = 1` for `C₂=⟨x+t²⟩` | 0 and 1 by linear algebra | **MATCH** |
| `ψ(C)` is `[24,20,4]_{5²}` with hull dimension 1 | length 24, `k=20`, **exact** `d=4`, ring hull `0+1=1` | **MATCH** |
| `g'₂ = x+t⁸` gives Hermitian LCD `[24,20,4]_{5²}` | `hull C'₁ = 0`, `hull C'₂ = 0`, `ψ(C')` dim 20, hull 0 | **MATCH** |

**Note.** This example is where an apparent discrepancy was first suspected and then retracted: an early implementation returned `γ`-sum 4 and `β`-sum 0 because the helper required `j | m` inside Euler's totient and used integer division at `j=4,12`. Correcting the totient reproduces the paper's 6 and 3 exactly. **The paper's γ/β formula is not in error**; the error was in my code. This is recorded because the retracted claim would otherwise resurface.

---

## Example 2 — p.16 (`p=13`, `GF(169)`, `n=14`, `α=12`, `r=2`)

| What the paper asserts | Recomputation | Agreement |
|---|---|---|
| `Ω = ∅`, `Ω' = {4,28}`, `β(4)=1`, `β(28)=6` (sum 7) | `Ω=∅`, `Ω'={4,28}`, `β=1,6`, sum 7 | **MATCH** |
| `x¹⁴−12` = the 14 printed linear factors | product equals `x¹⁴−12` exactly | **MATCH** |
| all 7 printed groupings are CR pairs | all 7 confirmed via `p^†` | **MATCH** |
| `g₁ = x²+t²¹x+1 = (x+t¹⁸)(x+t¹⁵⁰)` | identity holds | **MATCH** |
| `g₁, g₂` satisfy the dual-containing condition | both constituents dual-containing | **MATCH** |
| `ψ(C)` is `[28,25,4]_{13²}` | length 28, `k=25`, **exact** `d=4` | **MATCH** |
| quantum code `[[28,22,≥4]]₁₃`, MDS | `2k−en = 22`; Singleton residual `28+2−(22+8) = 0` | **MATCH** |

**Note (a real trap).** With `M = [[1,1],[1,−1]]` the entry `−1` is `4` in `GF(25)` but `12` in `GF(169)`. A first pass hard-coded `4` and produced `[28,25,3]` — a spurious mismatch that would have been reported as a failure of the paper's MDS claim. The distance is reproduced exactly (4) once `−1` is taken from the field.

---

## Example 3 — p.16–17 (`p=5`, `GF(25)`, `n=6`, `α=4`, `r=2`, `e=3`)

| What the paper asserts | Recomputation | Agreement |
|---|---|---|
| `Ω = ∅`, `Ω' = {4,12}`, `β(4)=1`, `β(12)=2` | same | **MATCH** |
| `x⁶−4` = the 6 printed factors | product equals `x⁶−4` exactly | **MATCH** |
| all 3 groupings are CR pairs | all 3 confirmed | **MATCH** |
| `g₁ = x²+tx+t⁸ = (x+t²)(x+2)` | identity holds | **MATCH** |
| `g₁, g₂, g₃` satisfy the dual-containing condition | all three constituents dual-containing | **MATCH** |
| `ψ(C)` is `[18,14,4]_{5²}` (via `M(5)`) | length 18, `k=14`, **exact** `d=4` | **MATCH** |
| quantum code `[[18,10,≥4]]₅`, near-MDS | `2k−en = 10`; residual `18+2−(10+8) = 2 ≠ 0` → near-MDS | **MATCH** |
| `η₁=(u+4)(u+t²⁰)`, `η₂=(u+t⁴)(u+t²⁰)`, `η₃=(u+t⁴)(u+4)` are the CRT idempotents | each is a nonzero scalar multiple (`8η₁`, `3η₂`, `24η₃`) of an idempotent; `Ση_i = 3u² ≠ 1`; after rescaling: orthogonal idempotents summing to 1 | **MATCH up to normalisation** (see audit item 2 — no effect on the code) |
| `M(5)M(5)* = νI` | `= 4I` | **MATCH** |
| `C₃ = ⟨g₂(x)⟩` (p.16) | `g₂` and `g₃` are distinct; the dimension `4+5+5=14` requires `g₃` | **typographical slip**, recomputed with `g₃` |

---

## Tables 1–3 — all 33 rows

Method per row, with no shortcuts:

1. parse the printed `λ = aε₁ + bε₂` and `g₁, g₂` into `GF(q²)[x]`;
2. check `g_i | x^n − α_i` (necessary for `g_i` to be a generator polynomial) — **33/33 true**;
3. build `C_i = ⟨g_i⟩` and check `dim C₁ + dim C₂` against the printed `k`;
4. build `ψ(C)` with the row's own field and matrix (`M` for `e=2`, `M(5)`/`M(11)` for `e=3`);
5. compute the **exact** minimum distance by exhaustive dependent-column search on a parity-check matrix;
6. compute `hull(ψ(C))` by the Hermitian inner product over `GF(q²)`;
7. test `C_i^{⊥H} ⊆ C_i` for each constituent;
8. for Table 3, compute `[[en, 2k−en, ≥d]]` and the residual `en + 2 − (k+2d)`, and compare with the printed residual column.

`hull` is the recomputed hull dimension of `ψ(C)`; "paper hull" is the printed fifth column (Table 1 is titled *Hermitian LCD codes*, i.e. hull 0).

| Table | Row | `n` | field | `λ` | `g₁(x)` | `g₂(x)` | recomputed | paper | hull `ψ(C)` | paper hull | dual-cont. | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 12 | GF(5²) | 1ε₁ + 1ε₂ | `x3 + x2 + t8x + t8` | `x+ t8` | [24,20,4] | [24,20,4] | 0 | 0 | no | PASS |
| 1 | 2 | 12 | GF(7²) | 1ε₁ + 6ε₂ | `x3 + t2x2 + t2x + t36` | `x+ t6` | [24,20,4] | [24,20,4] | 0 | 0 | no | PASS |
| 1 | 3 | 12 | GF(11²) | 1ε₁ + 1ε₂ | `x3 + x2 + t40x + t40` | `x+ t10` | [24,20,4] | [24,20,4] | 0 | 0 | no | PASS |
| 1 | 4 | 30 | GF(11²) | 1ε₁ + 10ε₂ | `x2 + 4x + 1` | `x+ t10` | [60,57,3] | [60,57,3] | 0 | 0 | no | PASS |
| 1 | 5 | 12 | GF(13²) | 1ε₁ + 1ε₂ | `x3 + 8x2 + 5x + 12` | `x+ 1` | [24,20,4] | [24,20,4] | 0 | 0 | no | PASS |
| 1 | 6 | 14 | GF(13²) | 1ε₁ + 1ε₂ | `x2 + t27x + t12` | `x+ 1` | [28,25,4] | [28,25,4] | 0 | 0 | no | PASS |
| 1 | 7 | 30 | GF(13²) | t36ε₁ + 1ε₂ | `x2 + t4x + t120` | `x+ 1` | [60,57,3] | [60,57,3] | 0 | 0 | no | PASS |
| 2 | 1 | 12 | GF(5²) | 1ε₁ + 1ε₂ | `x3 + x2 + t8x + t8` | `x+ t2` | [24,20,4] | [24,20,4] | 1 | 1 | no | PASS |
| 2 | 2 | 12 | GF(5²) | 1ε₁ + 1ε₂ | `x3 + x2 + t13x + t14` | `x+ 2` | [24,20,4] | [24,20,4] | 2 | 2 | no | PASS |
| 2 | 3 | 12 | GF(7²) | 1ε₁ + 1ε₂ | `x3 + tx2 + t22x + t44` | `x+ t4` | [24,20,4] | [24,20,4] | 2 | 2 | no | PASS |
| 2 | 4 | 12 | GF(7²) | 1ε₁ + t12ε₂ | `x3 + t2x2 + t2x + t36` | `x+ t5` | [24,20,4] | [24,20,4] | 1 | 1 | no | PASS |
| 2 | 5 | 12 | GF(11²) | 1ε₁ + 10ε₂ | `x3 + t3x2 + t103x + t70` | `x+ t25` | [24,20,4] | [24,20,4] | 1 | 1 | no | PASS |
| 2 | 6 | 12 | GF(11²) | 10ε₁ + 10ε₂ | `x3 + t45x2 + t50x + t95` | `x+ t5` | [24,20,4] | [24,20,4] | 2 | 2 | no | PASS |
| 2 | 7 | 30 | GF(11²) | 1ε₁ + 1ε₂ | `x2 + t5x + t4` | `x+ 1` | [60,57,3] | [60,57,3] | 1 | 1 | no | PASS |
| 2 | 8 | 30 | GF(11²) | 1ε₁ + 1ε₂ | `x2 + t5x + t4` | `x+ t4` | [60,57,3] | [60,57,3] | 2 | 2 | no | PASS |
| 2 | 9 | 12 | GF(13²) | 1ε₁ + 1ε₂ | `x3 + 11x + 4` | `x+ 1` | [24,20,4] | [24,20,4] | 1 | 1 | no | PASS |
| 2 | 10 | 12 | GF(13²) | 1ε₁ + 1ε₂ | `x3 + 4x2 + x + 4` | `x+ 2` | [24,20,4] | [24,20,4] | 2 | 2 | no | PASS |
| 2 | 11 | 30 | GF(13²) | 1ε₁ + t120ε₂ | `x2 + 8x + 4` | `x+ t4` | [60,57,3] | [60,57,3] | 2 | 2 | no | PASS |
| 2 | 12 | 30 | GF(13²) | 1ε₁ + t120ε₂ | `x2 + 8x + 4` | `x+ t60` | [60,57,3] | [60,57,3] | 1 | 1 | no | PASS |
| 3 | 1 | 16 | GF(3²) | 1ε₁ + 1ε₂ | `x3 + t7x2 + tx + 1` | `x+ t` | [32,28,3] | [32,28,3] | 4 | — | yes | PASS |
| 3 | 2 | 16 | GF(3²) | 1ε₁ + 1ε₂ | `x3 + t7x2 + tx + 1` | `x3 + tx2 + t7x + 1` | [32,26,4] | [32,26,4] | 6 | — | yes | PASS |
| 3 | 3 | 20 | GF(3²) | 2ε₁ + 2ε₂ | `x3 + x2 + x + t` | `x+ t` | [40,36,3] | [40,36,3] | 4 | — | yes | PASS |
| 3 | 4 | 26 | GF(3²) | 1ε₁ + t2ε₂ | `x3 + 2x2 + 1` | `x+ t` | [52,48,3] | [52,48,3] | 4 | — | yes | PASS |
| 3 | 5 | 28 | GF(3²) | 2ε₁ + t2ε₂ | `x3 + t6x2 + tx + t3` | `x2 + t3` | [56,51,3] | [56,51,3] | 5 | — | yes | PASS |
| 3 | 6 | 30 | GF(3²) | 1ε₁ + t2ε₂ | `x3 + t2x2 + t2x + 1` | `x2 + t3x + t6` | [60,55,4] | [60,55,4] | 5 | — | yes | PASS |
| 3 | 7 | 20 | GF(5²) | t4ε₁ + 1ε₂ | `x3 + t11x2 + t3` | `x+ 1` | [40,36,4] | [40,36,4] | 4 | — | yes | PASS |
| 3 | 8 | 26 | GF(5²) | 4ε₁ + 4ε₂ | `x3 + t7x2 + tx + 2` | `x+ 2` | [52,48,4] | [52,48,4] | 4 | — | yes | PASS |
| 3 | 9 | 28 | GF(5²) | 1ε₁ + 4ε₂ | `x3 + t23x2 + tx + 3` | `x2 + t15x + 1` | [56,51,4] | [56,51,4] | 5 | — | yes | PASS |
| 3 | 10 | 30 | GF(5²) | 1ε₁ + 4ε₂ | `x2 + 2x + 1` | `x+ t2` | [60,57,3] | [60,57,3] | 3 | — | yes | PASS |
| 3 | 11 | 30 | GF(7²) | 1ε₁ + t12ε₂ | `x2 + t3x + 1` | `x+ t2` | [60,57,3] | [60,57,3] | 3 | — | yes | PASS |
| 3 | 12 | 30 | GF(7²) | 1ε₁ + t12ε₂ | `x3 + t7x2 + t41x + 4` | `x+ t2` | [60,56,4] | [60,56,4] | 4 | — | yes | PASS |
| 3 | 13 | 36 | GF(7²) | 1ε₁ + t12ε₂ | `x3 + t4` | `x+ t3` | [72,68,3] | [72,68,3] | 4 | — | yes | PASS |
| 3 | 14 | 14 | GF(13²) | 12ε₁ + 12ε₂ | `x2 + t21x + 1` | `x+ t6` | [28,25,4] | [28,25,4] | 3 | — | yes | PASS |

**Result: 33/33 rows reproduced.** Length, dimension, exact minimum distance, hull dimension (Tables 1–2), dual-containing property and quantum parameters + Singleton residual (Table 3) all agree with the printed values. There is no `MISMATCH` and no `NOT REPRODUCIBLE` row.

**Distance provenance (why "exact").** For each `ψ(C)` a parity-check matrix `H` of full rank `en − k` was built. A codeword of weight `w` exists iff some `w` columns of `H` are linearly dependent, so the minimum distance is the smallest `w` for which `C(en, w)` subsets are dependent. Weights 1–3 were searched **exhaustively** for every row (a vectorised `3×3` minor test for `w=3`); weight 4 was settled by an explicit witness (or, when the co-dimension is `≤ 3`, by the fact that any 4 columns are then automatically dependent). No distance was inherited from a constituent code or from the paper.

**Two encoding checks that had to be got right before any row could be believed** (both were my errors, not the paper's):

* the coefficient `x` with no exponent is `x¹`, not `x⁰` — an early parser dropped 11 rows' linear terms and made `div=False`;
* `ϵ1 + t120ϵ2` means `a = 1, b = t¹²⁰`; writing the two coefficients in the other order produced six rows whose generator did not divide `x^n − α`. After orientation, all 33 rows divide correctly and every parameter matches.

**Not verified here (out of Phase-1 scope):** the "Remark / Comparison" column of Table 3 (`New`, `Optimal [11]`, `[[52,43,≥3]]₃ [11]`, …). Those are literature claims requiring references [3], [11], [14]; they are `UNVERIFIED` and were neither used nor adjusted.
