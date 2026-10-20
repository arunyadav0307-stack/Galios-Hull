# INDEPENDENT_VERIFICATION_REPORT

**Date:** 2026-10-20 (UTC) · **Branch:** `arena/1625045b-galios-hull`
**Object under verification:** `Galios hulls of constacclic codes over affine algebra rings'.pdf`,
SHA-256 `0db90bfbeda69ad1af231b81d92f24be3589ed15ac2e0ade6605ba7ad0ddc039`, 27 pp.,
= arXiv:2412.08512v1, I. Debnath, H. Islam, E. Martínez-Moro, O. Prakash.
**Published as:** *Discrete Math.* **349**(2) (2026) 114750, DOI `10.1016/j.disc.2025.114750`.

**Purpose.** Re-derive, from the PDF itself, the exact statements behind finding F11,
the CRT decomposition, the Gray-map dimension count, and the reported quantum
parameters; separate proven contradictions from labelling problems; verify the
literature precedents independently; and audit this project's own scripts.
Nothing here is a manuscript and nothing has been pushed to Git.

---

## 0. Method and provenance

The PDF was re-extracted page by page (all 27 pages, `pypdf` 6.21.1) and each cited
statement was read in the extracted text at the page given below. Page numbers are
**PDF page numbers, which coincide with the printed page numbers** (verified: the
bottom-of-page numerals 5, 8, 13, 14, 16, 19, 20, 21, 22, 23 recovered from the text
layer match the PDF page index).

All arithmetic was recomputed twice, independently:

| Artefact | Status |
|---|---|
| `verification/independent_verification.out` | **new this turn**; produced by `code/independent_verification.py`, exit 0, ALL CHECKS PASS |
| `verification/verify_examples.out` | earlier turn, exit 0 — but see §6.2, its model is assumption-laden |
| `verification/verify_corollary_3_5.out` | earlier turn, exit 0 — see §6.3 |
| `verification/verify_example1.out` | earlier turn, exit 0 |

`code/independent_verification.py` was written from scratch for this report. It does
**not** reuse the model in `code/verify_examples.py`. It constructs `A` explicitly as a
4-dimensional `F_q`-algebra `F_q[x_1,x_2]/⟨t_1,t_2⟩`, finds its idempotents by brute
force from the structure constants, builds `C = A·⟨g⟩` as a genuine `A`-submodule of
`A[x]/⟨x^n − λ⟩`, and computes `dim_{F_q}` by rank. It requires no assumption about
which component is which.

---

## 1. The statements, at their exact locations

### 1.1 The decomposition (p.4–5, §2.1)

> p.4: "the size of each class is given by `|S(ν)| = lcm(d_1,d_2,…,d_ℓ) = [F_q(ν_1,ν_2,…,ν_ℓ) : F_q]`, where `d_i` is the degree of `Irr(ν_i,F_q)`."

> p.5: "`F_q[X_1,…,X_ℓ]/I_{S(ν)} ≅ F_q(ν_1,ν_2,…,ν_ℓ)`, and by using the Chinese Remainder Theorem, we get
> `R ≅ F_q[X_1,…,X_ℓ]/⋂_{S(ν)∈Ŝ} I_{S(ν)} ≅ ⊕_{S(ν)∈Ŝ} F_q[X_1,…,X_ℓ]/I_{S(ν)} ≅ ⊕_{S(ν)∈Ŝ} F_q(ν_1,ν_2,…,ν_ℓ)`."

> p.5: "this is equivalent to having a decomposition as a direct sum of finite fields, and thus, `A` is a finite commutative semi-simple ring."

**Verified correct.** (The symbol `R` on p.5 is used for `A`; a notational slip, not an error
in substance. The same `R` appears in Examples 2–3 as the name of the ring.)

### 1.2 The idempotent description of codes (p.7, Theorem 2; p.10, Corollary 3.1; p.12, Theorem 8 proof)

- p.12 (Theorem 8 proof): "we know that `C = ⨁_{S(ν)∈Ŝ} C_{S(ν)} e_{S(ν)}`, where `C_{S(ν)}` are `λ_{S(ν)}`-constacyclic codes **over `F_q`**."
- p.10 (Corollary 3.1): "`C` is a `k`-Galois self-dual code over `A` if and only if for each `S(ν)∈Ŝ`, `C_{S(ν)}` is a `k`-Galois self-dual code **over `F_q`**."

**This is the locus of finding F11.** §2.1 says the components are `F_q(ν_1,…,ν_ℓ) = F_{q^{|S(ν)|}}`;
§2.3/§3 write the components as `F_q`. The two are consistent only if every `|S(ν)| = 1`.

### 1.3 The Gray map (p.17, equation (10))

> "Every `a ∈ A` can be expressed as `a = Σ_{S(ν)∈Ŝ} a_{S(ν)} e_{S(ν)}`, **where `a_{S(ν)} ∈ F_q` for all `S(ν) ∈ Ŝ`**. Then, we define the map `ψ : A → F_q^N`, `a ↦ ψ(a) = (a_{S(ν1)}, a_{S(ν2)}, …, a_{S(νN)}) M`, (10) where `|Ŝ| = N`, and `M ∈ GL_N(F_q)` is such that `M (M^{(p^k)})^T = γ I_N` … It is easy to verify that the map `ψ` is **bijective linear isometry** from `A^n` (Gray distance) to `F_q^{nN}` (Hamming distance)."

### 1.4 The dimension transfer (p.18)

> "`dim(hull_k(D)) = dim(hull_k(ψ(C))) = dim(ψ(hull_k(C))) = dim_q(hull_k(C))`."

> Theorem 10 (p.18): for `ψ(C) = D` an `[nN, k, d]` code over `F_q`, there is an EAQECC `[[nN, k − dim_q(hull_k(C)), d ; nN − k − dim_q(hull_k(C))]]_q`.

### 1.5 The examples (p.18–21) and the table (p.21–22)

- Example 2: `R = F_9[x_1,x_2]/⟨t_1,t_2⟩`, `t_1 = x_1^2+x_1+ω`, `t_2 = x_2^2+ω^5x_2+2`, `F_9 = F_3(ω)`, `ω^2+2ω+2 = 0`, `p=3, e=2, ℓ=2, N=2`, `λ = e_1+ω^2e_2`, `n=7`, `k=1`. Claims `dim_9(hull_1(C)) = 0`, `ψ(C)` is `[14,10,4]_9`, EAQECC `[[14,10,4;4]]_9`.
- Example 3: `t_1 = x_1^2+x_1+ω^{13}`, `t_2 = x_2^2+ω^3x_2+1`, `F_25 = F_5(ω)`, `ω^2+4ω+2 = 0`, `N=2`, `λ = e_1+ω^8e_2`, `n=13`, `k=1`. Claims `dim_25(hull_1(C)) = 2`, `ψ(C)` is `[26,22,4]_25`, EAQECC `[[26,20,4;2]]_25`.
- p.21: for `q = 4`, `A = F_4[x_1,x_2]/⟨x_1^2+x_1+ω, x_2^2+ωx_2+ω⟩`.
- Table 1, p.22: 13 rows; every `ψ(C)` has length `2n`, i.e. `N = 2` throughout.

---

## 2. Claim-by-claim verdicts

| # | Claim | Location | Verdict |
|---|---|---|---|
| V1 | `A ≅ ⊕_{S} F_{q^{|S(ν)|}}`, `|S(ν)| = lcm(d_i)` | p.4–5 | **CORRECT** (re-derived; see §3.1) |
| V2 | `dim_{F_q} A = ∏_i deg t_i` | implicit, p.4–5 | **CORRECT** (free module on monomials `X_i^{a_i}`, `a_i < deg t_i`) |
| V3 | `ψ : A → F_q^N` with `N=|Ŝ|` is a bijection | p.17, eq (10) | **PROVEN CONTRADICTION** in Examples 2, 3 and Table 1 (V8) |
| V4 | Theorem 8 computes "the **`q`-dimension** of the `k`-Galois hull" | p.12 | **LABELLING DEFECT, not a false equation.** The displayed formula is correct for `Σ_S dim_{A_S}(hull_k(C_S))`; it equals `dim_{F_q}` only when all `|S(ν)| = 1` |
| V5 | Theorem 7 additivity `hull_k(C) = ⊕_S hull_k(C_S)` | p.10 | **CORRECT** |
| V6 | Lemma 9 `ψ(hull_k C) = hull_k(ψ C)` | p.17–18 | **CORRECT as a conditional statement**; it presupposes a `ψ` that exists. With `ψ` undefined as specified (V3), it is vacuous for the paper's own examples |
| V7 | Corollary 3.5(2) `|D_{e/2}(n,2^e,λ)| = Nn/2 + 1` | p.14, proof p.15–16 | **PROVEN FALSE at `e' = 0`** (V10) |
| V8 | Examples 2–3 code dimensions `10`, `22` | p.20–21 | **NOT ESTABLISHED** as stated (V9); reproducible only as a different object |
| V9 | Quantum parameters `[[14,10,4;4]]_9`, `[[26,20,4;2]]_25`, Table 1 | p.20–23 | **NOT ESTABLISHED**; inherit V3/V8. The *arithmetic* of Theorem 10 is applied correctly to the stated inputs |
| V10 | Corollary 3.5(1) `|D_k(n,q,λ)| = N(n−1)/2 + 1` | p.14 | **Correct as printed** in the regime tested; no defect found |
| V11 | Theorem 9 (LCD sufficient condition) | p.16 | **Correct as a sufficient condition**; the phrase "`A` divides `1+p^{e−k}`" on p.16 is a typo for "`r` divides" |
| V12 | Remark 1 (no gain when `M = I_N`) | p.18 | **CORRECT and self-aware**: the authors know the direct-sum structure when `M = I_N` |

### 2.1 Which of these are proven contradictions, and which are interpretive

**(a) Proven contradictions** (a stated equality fails on the paper's own data):

1. **Bijectivity of `ψ`.** p.17 asserts `ψ : A → F_q^N` is bijective with `N = |Ŝ|`.
   In Example 2, `dim_{F_q} A = 4` while `N = 2`, so `|A| = 9^4 = 6561` but
   `|F_9^2| = 81`. No bijection exists. Same for Example 3 (`25^4` vs `25^2`) and
   for the `q=4` ring of Table 1 (`4^4` vs `4^2`).
2. **Code dimension vs. ambient length.** In Example 2, the `A`-module `C` has
   `dim_{F_9} C = 20` (§3.2), but `ψ(C)` is claimed to have length `14` and dimension
   `10`. A linear image of a 20-dimensional space cannot have dimension 10, and no
   linear map `A^7 → F_9^{14}` is injective on a 20-dimensional subspace.
   Example 3: `dim_{F_{25}} C = 44` vs length `26`.
3. **Corollary 3.5(2) at `e' = 0`** (§3.4).

**(b) Labelling / interpretation issues** (the displayed formula is right; the words
attached to it are not):

4. Theorem 8 computes `Σ_S dim_{A_S}`, not `dim_{F_q}`. The formula is a correct
   restatement of Theorem 7 plus the per-component hull dimension. Only the words
   "`q`-dimension" and "over `F_q`" (p.12, p.9) are wrong.
5. Corollary 3.4 and 3.5 inherit the same labelling. Their **numerical** content is
   unaffected (both are statements about the unweighted sum), which is why the
   earlier brute-force test could "pass" (§6.3).
6. The numbers `10` and `22` are **not wrong as numbers**: they are the dimensions of
   the `M`-mixed direct sums of the two `F_q`-codes generated by `g_1` and `g_2`.
   That object is well defined and was independently rebuilt (§3.3). The error is
   identifying it with `ψ(C)` for the `A`-module `C`.

**(c) Not decidable from arXiv v1:** whether the version of record repairs any of this (§5).

### 2.2 Is there a reading that saves the paper?

Three repairs exist; each has a cost, which is why this is a defect and not a typo.

| Repair | Statement | Cost |
|---|---|---|
| **R1** | Add the hypothesis "every `t_i` splits over `F_q`" (equivalently `|S(ν)| = 1` for all `ν`) | Everything becomes consistent: `N = |Ŝ| = |H| = dim_q A`. But then **all three rings used in the paper fail the hypothesis**, and Examples 2–3, Table 1 and their parameters would have to be rebuilt |
| **R2** | Keep general `t_i`; define `ψ : A → F_q^{dim_q A}` by expanding each `a_{S(ν)}` in an `F_q`-basis of `F_{q^{|S(ν)|}}` | `N` must become `dim_q A` (4, not 2), so every length doubles; `ψ` is only `F_q`-linear, so Lemma 9 needs a new proof; the "bijective linear isometry" must be restated |
| **R3** | Restrict to codes with `a_{S(ν)} ∈ F_q` | This set is not closed under multiplication by `A`, so it is not a code over `A` |

R1 is the cheapest and is almost certainly what the authors intended. It is not
stated anywhere in the paper — and p.4 explicitly makes allowance for `|S(ν)| > 1`,
so the omission is not a harmless simplification.

> **Verdict on F11: confirmed, as a proven contradiction in §4.1 and a labelling
> defect in §3, for arXiv v1. Its severity is `M` (material): it affects every
> quantum parameter in the paper and every row of Table 1. Its repair is cheap but
> changes the examples.**

---

## 3. Reproducible derivations

Each step below is printed by `code/independent_verification.py` and recorded in
`verification/independent_verification.out`. The commands are given so any reader can
re-run them.

### 3.1 `|S(ν)| = 2` in both examples — a proof from the paper's own numbers

No computation is needed.

1. `dim_{F_q} A = ∏_i deg t_i` (free `F_q`-module). Examples 2, 3 and the `q=4` ring
   all have `ℓ = 2`, `deg t_1 = deg t_2 = 2`, hence `dim_q A = 4`.
2. p.4 gives `|S(ν)| = lcm(d_1,…,d_ℓ)` with `d_i | deg t_i`, so here `|S(ν)| ∈ {1,2}`.
3. p.5 gives `dim_q A = Σ_{S∈Ŝ} |S(ν)| = 4`.
4. The paper states `N = |Ŝ| = 2`.
5. Two terms each `≤ 2`, summing to 4 ⇒ **both equal 2**. So `A ≅ F_{q^2} ⊕ F_{q^2}`.

**Confirmed computationally** for all three rings:

| ring | `t_1` | `t_2` | `dim_q A` | primitive idempotents | `dim_q(e_i A)` |
|---|---|---|---|---|---|
| Ex. 2, `q=9` | `x^2+x+ω` **irreducible** | `x^2+ω^5x+2` **irreducible** | 4 | 2 | 2, 2 |
| Ex. 3, `q=25` | `x^2+x+ω^{13}` **irreducible** | `x^2+ω^3x+1` **splits** | 4 | 2 | 2, 2 |
| Table 1, `q=4` | `x^2+x+ω` **irreducible** | `x^2+ωx+ω` **irreducible** | 4 | — | — |

Note that the *number* of irreducible factors is not what decides `|S(ν)|`: in
Example 3, `t_2` splits and `t_1` does not, yet the Frobenius orbits on the *pairs*
`(ν_1,ν_2)` still have size `lcm(2,1) = 2`. This is exactly what p.4 says, and
exactly what §2.3 then ignores.

### 3.2 The true `F_q`-dimension of the `A`-module

`C = A·⟨g⟩` with `g = e_1g_1 + e_2g_2`. Since `A ≅ A_1 ⊕ A_2` with `A_i = F_{q^2}`,
`C ≅ A_1g_1 ⊕ A_2g_2` and

```
dim_{F_q} C = Σ_i [A_i : F_q] · dim_{A_i}(A_i g_i)
            = Σ_i 2 · (n − deg g_i).
```

- Example 2: `2(7−3) + 2(7−1) = 8 + 12 = **20**`.
- Example 3: `2(13−3) + 2(13−1) = 20 + 24 = **44**`.

**Computed independently**, by building `A` explicitly, finding `e_1,e_2`, forming
`g = e_1g_1+e_2g_2`, and taking the `F_q`-rank of the `n·dim_q A` generators
`{b_j · x^i g}`:

```
Example 2:  dim_F9(<g>)  by pairing: {'paper (g1 with lam=1)': 20, 'swapped': 28}
Example 3:  dim_F25(<g>) by pairing: {'paper (g1 with lam=1)': 44, 'swapped': 52}
```

The "swapped" figures are the same computation with `g_1` attached to the wrong
component (then `g_1 ∤ x^n − λ` there and the ideal is the whole component). The
paper's assignment of `λ = 1` to `g_1` and `λ = ω^2` (resp. `ω^8`) to `g_2` is
confirmed by divisibility in `F_q[x]`:

```
[PASS] g2 | x^7 - w^2      (Example 2)
[PASS] g1 | x^13 - 1  and  g2 | x^13 - w^8   (Example 3)
```

Hence:

```
Example 2: dim_F9(C) = 20  >  14 = nN
Example 3: dim_F25(C) = 44 >  26 = nN
```

Any `F_q`-linear `ψ : A^n → F_q^{nN}` has a kernel meeting a 20-dimensional subspace
of a 28-dimensional space in dimension `≥ 6`. So `ψ|_C` is not injective, and
`ψ` is not a bijection.

### 3.3 What the paper's `10` and `22` actually are

Rebuilding the reported codes as the `M`-mixed direct sums of the two `F_q`-codes:

```
Example 2:  M = [[w, w^3], [w^7, w^5]] on F_9   ->  dim = 10, d = 4   (paper: [14,10,4]_9)
Example 3:  M = [[w, w^2], [2, w^13]] on F_25   ->  dim = 22          (paper: [26,22,4]_25)
```

So `10 = (7−3)+(7−1)` and `22 = (13−3)+(13−1)`: the paper's `k` is
`Σ_S (n − deg g_S)`, i.e. the sum of the dimensions computed **as if every component
were `F_q`**. That is exactly `dim_{F_q} C / 2` here.

This is a coherent object — the `M`-mixed direct sum of two `F_q`-codes — and its
`[14,10,4]_9` parameters are correct. It is simply not `ψ(C)` for the `A`-module `C`,
because the `A`-module is twice as large.

> Note for the reader: with `M = I_N` this object is precisely the direct sum
> described in the authors' own Remark 1 (p.18). The paper is therefore internally
> aware of the direct-sum picture — but Remark 1 is invoked only for `M = I_N`,
> whereas the defect is independent of `M`.

### 3.4 Corollary 3.5(2) fails at `e' = 0`

p.14 defines `n = n'p^{e'}` with **`e'` a non-negative integer**, and asserts
`D_k(n,q,λ) ⊆ {0,1,…,⌊n/2⌋}`. Corollary 3.5(2) claims, for `p = 2`, `e` even and
`ord(λ)n' | (2^e−1)`, that `|D_{e/2}(n,2^e,λ)| = Nn/2 + 1`.

Take `q = 4` (`p=2`, `e=2`), `k = e/2 = 1`, `n = n' = 3` (`e' = 0`), `λ = 1`:
`ord(λ)·n' = 3 | 3`, so the hypothesis holds. The claim gives
`|D_1(3,4,1)| = 2·3/2 + 1 = 4`. But `D ⊆ {0,1}`, so `|D| ≤ 2`.

**Proven false**, independent of which ring `A` is used. (For odd `N` the printed
quantity `Nn/2` is not even an integer — a second, independent symptom.)

`code/independent_verification.py`, PART D, prints both facts:
`[PASS] claimed count is attainable: got False, expected False`.

---

## 4. Literature re-verification (independent of the source's reference list)

Every entry below was retrieved from the publisher / repository page this turn; none
is copied from `[S1]`'s bibliography. Verification level: **A** full text or full
publisher page · **B** abstract + metadata · **C** metadata only.

### 4.1 The precedent that decides the Phase 2 question

**[S25]** A. K. Shukla, O. P. Pandey, V. Mishra, S. Pathak, A. K. Upadhyay,
*Hulls of `Z_pZ_p[v]`-cyclic codes and construction of EAQECCs*,
**Adv. Math. Commun. 20 (2026) 209–238**, DOI `10.3934/amc.2025037`.
Received Feb 2025, revised Jul 2025, early access 11 Aug 2025. **Level A.**

> Abstract, verbatim: "we derive the generator polynomials of the hulls of separable
> cyclic codes (SCCs) over `Z_pZ_p[v]` and determine their dimensions **using the
> concept of a generating function in combinatorics**. We also **enumerate the SCCs
> over `Z_pZ_p[v]` with hulls of a fixed dimension**. Next, we present the generator
> polynomials of the hulls of non-separable cyclic codes (NSCCs) over `Z_2Z_2[v]` …
> Additionally, we enumerate the NSCCs over `Z_2Z_2[v]` with hulls of a fixed
> dimension."

`Z_pZ_p[v]` with `v² = v` is a product of finite fields — the same alphabet type as
`A`. This paper contains, in a special case, precisely the construction the blueprint
proposes as new. **Corrects the earlier record**: the volume is 20 (2026), pages
209–238, not "AMC 2025" without volume/pages.

### 4.2 The local (field-level) enumerator

**[D23]** I. Debnath, O. Prakash, H. Islam, *Galois hulls of constacyclic codes over
finite fields*, **Cryptogr. Commun. 15 (2023) 111–127**, DOI `10.1007/s12095-022-00591-6`.
Received 23 Oct 2021, accepted 16 May 2022, published 23 Jun 2022. **Level B.**

> Abstract, verbatim: "Also, **considering some restrictions on `q`, the number of
> constacyclic codes of length `n` over `F_q` is calculated for a given Galois hull
> dimension**."

**[D23c]** Correction, **Cryptogr. Commun. 15 (2023) 129–130**,
DOI `10.1007/s12095-022-00602-6`, published 22 Jul 2022. **Level A** (full page read).
Ten items; item 8 reads:

> "Page 8, line 250: '`1 ≤ i_1 ≤ i_2 ≤ a_i`' is replaced by '`1 ≤ i_1 < i_2 ≤ a_i`'."

The earlier record of this correction is confirmed, and the correction's full scope is
now known (it also adds two missing references and fixes example typos).

**[SJL15]** E. Sangwisut, S. Jitman, S. Ling, P. Udomkavanich, *Hulls of cyclic and
negacyclic codes over finite fields*, **Finite Fields Appl. 33 (2015) 232–257**,
DOI **`10.1016/j.ffa.2014.12.008`**. **Level B.**

> "The enumerations of cyclic codes and negacyclic codes of length `n` over `F_q`
> having hulls of a given dimension are established as well."

**Correction to the project record:** the DOI recorded earlier
(`10.1016/j.ffa.2014.12.002`) is **wrong**; it is `.008`.

### 4.3 Mass formulas for prescribed hull dimension — the precedent missed earlier

**[LSL25]** S. Li, M. Shi, S. Ling, *A mass formula for linear codes with prescribed
hull dimension and related classification*, **IEEE Trans. Inf. Theory 71(1) (2025)
273–286**, DOI `10.1109/TIT.2024.3425058`. **Level B.**

> "The main objective of this paper is to obtain a closed mass formula for linear
> codes with prescribed hull dimension. We simplify the mass formula obtained by
> Sendrier … Finally, we obtain a classification of (optimal) ternary linear codes
> with small parameters."

Companion: **[LS24]** S. Li, M. Shi, *Characterization and classification of binary
linear codes with various hull dimensions from an improved mass formula*,
**IEEE Trans. Inf. Theory 70(5) (2024) 3357–3372**.
And **[LSL24]** S. Li, M. Shi, Y. Li, S. Ling, *A further study on the mass formula
for linear codes with prescribed hull dimension*, **arXiv:2410.13578** (17 Oct 2024),
which does the Hermitian and symplectic cases. **Level A** (HTML full text, introduction).

**This is a direct precedent for the "count codes with a prescribed hull dimension"
programme, and it was absent from the earlier literature review.** It does not treat
constacyclic codes and does not work over a product ring, so it does not dispose of
`[S25]`'s status — but it does mean the *question type* ("how many codes have hull
dimension `h`?") is a well-developed industry, not a gap.

### 4.4 Isometry / equivalence classes of constacyclic codes

**[CFLL12]** B. Chen, Y. Fan, L. Lin, H. Liu, *Constacyclic codes over finite fields*,
**Finite Fields Appl. 18(6) (2012) 1217–1231**, DOI `10.1016/j.ffa.2012.10.001`.
**Level A** (publisher abstract + full-text excerpt).
Introduces `n`-isometry (`λ ≅_n μ`) and `n`-equivalence exactly to *classify
constacyclic codes*; the number of `n`-equivalence classes in `F_q^*` is `gcd(n,q−1)`.

**[?24]** *On isometry and equivalence of constacyclic codes over finite chain rings*,
**Cryptogr. Commun. (2024)**, DOI `10.1007/s12095-024-00758-3`. **Level B.**

> "we … compute the numbers of `n`-isometry and `n`-equivalence classes for each type
> of finite chain rings, as well as describe methods to find these classes."

**[Che23]** H. Chen, *On the hull-variation problem of equivalent linear codes*,
**IEEE Trans. Inf. Theory 69 (2023) 2911–2922**. Cited at level B via two independent
2025–26 papers that state and extend it: for classical codes under the Hamming metric
"the dimension of the hull can be reduced up to equivalence", and for `q = 2, 3` there
exist equivalent codes with different hull dimensions.

**Consequence for the project, and a correction to the earlier record:** the earlier
`JOINT_ENUMERATOR_FEASIBILITY.md` §5 C1 described isometry-class enumeration as
"`[OPEN]` … no result found in the literature". **That is too strong.** Two
well-developed lines exist — class counts of constacyclic codes up to `n`-isometry,
and mass formulas for hull-constrained codes. What is genuinely absent is their
*intersection*. See `RESEARCH_DIRECTION_DECISION.md` §C1.

### 4.5 What the source's own "open problem" most likely means

`[S1]` p.23: *"the enumeration of non-isometric constacyclic codes for a given Galois
hull dimension is an interesting problem. This problem is still open over `A`."*

Given `[CFLL12]` and the 2024 chain-ring paper use the word *isometric* in the
technical sense of `n`-isometry of the shift constant, the phrase most plausibly
refers to counting codes up to that equivalence — **not** to a new notion of isometry
of `A`-codes. This matters: it means the "open problem" the source names may be
considerably narrower (and possibly easier) than "count codes up to monomial
equivalence", and any project built on it must first pin down which relation is meant.

---

## 5. arXiv v1 versus the version of record — **BLOCKED**

| Check | Result |
|---|---|
| Can the version of record be read? | **No.** Elsevier paywall; only abstract, introduction, section snippets and the reference list are exposed. |
| Does it exist and is it the same paper? | Yes: *Discrete Math.* **349**(2) (2026) 114750, DOI `10.1016/j.disc.2025.114750`; authors identical; abstract substantively identical (one sentence reworded to "regarding their idempotent generators"). |
| Does the text differ from arXiv v1? | **Yes.** The published introduction adds Bajalan et al. and Debnath–Prakash (2025) and renumbers references (45 vs 44); the published "organisational" paragraph mentions **"Example 2, Example 4, and Table 2"**, whereas arXiv v1 has Examples 1–3 and Table 1 only. The version of record is therefore **longer**. |
| Was F11 repaired? | **UNVERIFIABLE — BLOCKED.** The published §3 snippet still says "we derive a formula for the **`q`-dimension** of the `k`-Galois hull", i.e. the same wording, but that is not evidence about the examples or Table 1. |
| Is there a published corrigendum? | None found in any index searched. |

**Statement for the record.** F11 is established **for arXiv:2412.08512v1**. Whether
it applies to the article of record is **unknown and must not be asserted either way**.
The same caveat applies to F3 (Corollary 3.5(2)) and to every numerical claim above.

---

## 6. Audit of this project's own deliverables and scripts

### 6.1 What is sound

| Artefact | Verdict |
|---|---|
| `SOURCE_THEOREM_REGISTER.md` | Counts check mechanically: 10 theorems, 9 lemmas, 5 corollaries |
| `SOURCE_EXAMPLE_RECALCULATION.md` | Examples 1–3 reproduced; the model caveat inserted last turn is correct and necessary |
| `code/verify_example1.py` + `.out` | Reproduces the six idempotents of Example 1; `e_i²=e_i`, `e_ie_j=0`, `Σe_i=1` all true. **Sound.** |
| `code/gf.py` | Re-read; `GF` arithmetic, `factor`, `span_rank`, `nullspace`, `hull_dim` behave correctly on the cases used. No error found |

### 6.2 `code/verify_examples.py` — a *model* caveat, stated explicitly

The function `gray_basis(F, n, N, comps, M)` builds `n − deg g_j` rows per component,
each row being a **length-`n` vector over `F_q`**, then mixes them through `M`. That is
the `F_q`-component model. It therefore *implements the assumption under test*.

Consequently the line

```
psi(C) = [14, 10, 4]_9   (paper: [14,10,4])
```

is **not** a verification that the paper's `ψ(C)` is correct. It is a verification
that, *if* one replaces the ring components by `F_q`, one gets the paper's numbers.
That is exactly the content of finding F11, not a refutation of it. The earlier
`SOURCE_EXAMPLE_RECALCULATION.md` says this in its caveat block, but the headline
table could still be misread, and it is misread by its own wording.

**Verdict: the test passes, but its scope is narrower than its label.** The label has
been corrected in `SOURCE_EXAMPLE_RECALCULATION.md` (see §7).

### 6.3 `code/verify_corollary_3_5.py` — two tests, different standing

- **Test 1** uses `A = F_9[x]/⟨x²−1⟩`. Since `x²−1` splits over `F_9`, every
  `|S(ν)| = 1`, so `N = dim_q A = 2`. This test is **model-correct** and genuinely
  corroborates Corollary 3.5(1).
- **Test 2** uses `A = F_4[x]/⟨x²+x+ω⟩`. This polynomial is **irreducible** over
  `F_4` (verified: no root among `0,1,ω,ω+1`), so `A ≅ F_16` is a *field*, `N = 1`,
  and the ring is **not** a product of two `F_4` copies. The test nevertheless
  convolves two "component" distributions. It is therefore a test of the paper's
  `F_q`-model, **not** of the ring.
  Its `PASS (5 = 5)` must be read as "the paper's arithmetic is self-consistent under
  its own component assumption", nothing more.
- **Test 3** (convolution = direct enumeration) uses the same ring and inherits the
  same caveat. Its conclusion — that hull dimensions add over components — is true and
  is Theorem 7; but the *numerical* `25 = 5 × 5` counts codes in the `F_4`-component
  model.

**Verdict: keep, with the standing of each test stated.** This is done in §7.

### 6.4 Errors found in this project's own earlier documents

| # | Error | Where | Correction |
|---|---|---|---|
| A1 | `[SJL15]` DOI given as `10.1016/j.ffa.2014.12.002` | `literature/REFERENCE_VERIFICATION_REPORT.md` | correct DOI is `10.1016/j.ffa.2014.12.008` |
| A2 | `[S25]` cited as "AMC 2025" without volume/pages | `literature/LITERATURE_MAP.md`, `literature/CITATION_LEDGER.md` | AMC **20** (2026) 209–238 |
| A3 | "isometry-class enumeration: no result found in the literature" | `JOINT_ENUMERATOR_FEASIBILITY.md` §5 C1, `literature/NOVELTY_ASSESSMENT.md` §3 | too strong; see §4.4. Two established lines exist; only their intersection is open |
| A4 | Literature review omits the Li–Shi–Ling mass-formula line | `literature/LITERATURE_REVIEW.md`, `literature/LITERATURE_MAP.md` | added in §4.3 above; to be propagated |
| A5 | `psi(C) = [14,10,4]` presented without an adjacent scope note | `SOURCE_EXAMPLE_RECALCULATION.md` headline table | scope note added (§7) |
| A6 | `SOURCE_THEOREM_REGISTER.md` Theorem 8 status originally "verified" | fixed last turn | now carries the F11 qualification |

None of A1–A6 changes the Phase 2 verdict. A3 and A4 change the *C1* assessment, in the
direction of **less** novelty for the project — which makes the verdict harder, not easier.

---

## 7. Actions taken on the project record

1. `SOURCE_MATHEMATICAL_AUDIT.md` F11 extended with the exact page/equation loci
   (p.9, p.12, p.17), the three repairs R1–R3, and their costs.
2. `SOURCE_EXAMPLE_RECALCULATION.md` — scope note attached to the `ψ(C)` rows.
3. `literature/REFERENCE_VERIFICATION_REPORT.md` — A1, A2, A4 corrected/added.
4. `JOINT_ENUMERATOR_FEASIBILITY.md` §5 C1 and `literature/NOVELTY_ASSESSMENT.md` §3
   annotated with A3.
5. New: `code/independent_verification.py` + `verification/independent_verification.out`.
6. New: `RESEARCH_DIRECTION_DECISION.md`; `PHASE_STATUS.md` rewritten for Phase 2.5.
7. `C1_ISOMETRY_SCREENING.md` + `code/isometry_hull_screening.py` +
   `verification/isometry_hull_screening.out` — R1 resolved negatively (see §9).
8. `README.md` evidence ledger extended; `literature/LITERATURE_MAP.md` gained stratum F
   (mass formulas and equivalence classes) and its "count up to isometry" row revised;
   `literature/CITATION_LEDGER.md` gained `[LSL25]`, `[CFLL12]`, `[ISO24]`, `[Che23]`.

**Status of items 1–8: all verified present on disk on 2026-10-20**, by direct
inspection after editing (not merely asserted). Item 4's annotations are at
`JOINT_ENUMERATOR_FEASIBILITY.md` §5 (C1) and `literature/NOVELTY_ASSESSMENT.md` §3.
A relative-link sweep over all 17 Markdown files resolves clean, with the two
deliberately absent blueprint-future filenames (`MATHEMATICAL_FRAMEWORK.md`,
`MAIN_THEOREMS_AND_PROOFS.md`) whitelisted in `PHASE_STATUS.md`.

---

## 8. What this report establishes, and what it does not

**Establishes.**

- F11 is real, and the strongest form of it is a **counting argument that needs no
  computation**: `|A| = q^{∏ deg t_i}` versus `|F_q^{|Ŝ|}|`; the two differ by `q²` in
  every example the paper gives.
- The reported code dimensions `10` and `22` are `Σ_S(n − deg g_S)`; the `A`-module
  dimensions are `20` and `44`; the latter exceed the claimed code lengths.
- Corollary 3.5(2) is false at `e' = 0`.
- Theorems 2, 3, 5, 6, 7, 10 and Lemma 9 remain correct as stated conditionally;
  Theorem 8's formula is correct as a sum of `A_S`-dimensions.
- The literature position is **stronger against novelty** than previously recorded,
  because of `[S25]` and the Li–Shi–Ling mass-formula line.

**Does not establish.**

- That the version of record contains any of these defects (§5, BLOCKED).
- That the paper's central theorem is wrong. It is not: it is a correct statement
  about component dimensions with an unstated hypothesis.
- Any priority claim. The observations here are corrections, not discoveries of new
  mathematics.

---

## 9. Post-report screening: the formulation of direction C1

Written after §1–§8, and separate from them: this section is about *our own* proposed
research direction, not about the source paper.

Risk **R1** of `RESEARCH_DIRECTION_DECISION.md` asked whether `dim_q hull_k` is
invariant under isometry. It is not, and the failure is elementary.

Take `q = 4`, `n = 3`, `C = ⟨1+x⟩ ⊆ F_4[x]/(x³−1)` and `φ = diag(1, ω, ω²)`, i.e.
`f(x) ↦ f(ωx)`. Then `φ` is diagonal with nonzero entries, hence a Hamming isometry;
`ω³ = 1`, hence `φ` is an `F_4`-algebra automorphism and carries cyclic codes to
cyclic codes; and

```
dim hull_0(C) = 0,   dim hull_0(φC) = 1        (Euclidean: CHANGED)
dim hull_1(C) = 0,   dim hull_1(φC) = 0        (Hermitian: NOT changed)
```

with identical weight enumerators.

**Correction (2026-10-20, second pass).** The first version of this section reported
`hull_1` as changing too. That was an artefact of raising field elements to `q^k`
instead of the paper's `p^k` (p.7); since `x⁴ = x` on `F₄`, the "`k = 1`" computation
was silently Euclidean. The Hermitian hull cannot change at `q = 4` at all, because
`a^{1+p} = a³ = 1` for every nonzero `a`, so every monomial map is a Hermitian
similarity. A genuine Hermitian counterexample exists over `F₉` (`hull_1 : 2 → 0`);
see `FINAL_INDEPENDENT_MATHEMATICAL_CHECK.md` §A.4. The general criterion is that a monomial map
`D diag(a_i)` preserves the `k`-Galois form iff `a_i^{1+q^k}` is constant, so the
invariance group is a proper subgroup `Sim_k` of the monomial group — index `9` at
`q = 4`, `n = 3`. The proposition is proved in `C1_ISOMETRY_SCREENING.md` §2 and
checked exhaustively there (432 triples, 0 failures).

**Consequence.** "Count constacyclic codes up to isometry, stratified by hull
dimension" does not define a number; the class of `⟨1+x⟩` would be counted at both
`h = 0` and `h = 1`. Only two reformulations survive (F1: `Sim_k`-classes; F2:
orbit/statistic pairs), and neither is yet known to have content.

**Standing.** This is an observation about how to formulate a question, not a theorem.
It is almost certainly known to specialists — it is why mass-formula work acts by the
isometry group of the form rather than by all monomial maps. It is recorded here
because the earlier project documents assumed the opposite.
