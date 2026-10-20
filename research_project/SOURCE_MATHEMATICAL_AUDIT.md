# SOURCE_MATHEMATICAL_AUDIT

Proof-level audit of `[S1]` Debnath–Islam–Martínez-Moro–Prakash,
*Galois hulls of constacyclic codes over affine algebra rings*,
arXiv:2412.08512v1 (27 pp.), SHA-256 `0db90bfb…ddc039`.

Every numbered result is registered in `SOURCE_THEOREM_REGISTER.md`. This document
records only **judgements**: what is sound, what is repairable, what is wrong, and
what cannot be checked here.

**Verdict in one line:** the mathematics of S1 is sound in its main line
(Theorems 2, 3, 5, 6, 7, 8, 10 and Lemma 9 survive scrutiny and reproduce
numerically), with **one boundary-case defect** (F3), **one structural hypothesis
gap that the paper's own examples violate** (F11), **two incomplete proofs
repairable in a few lines** (F4, F5), and **several typographical slips**. Nothing
found here undermines the paper's central formula *as a formula for the sum of
component dimensions*. F11 does undermine its labelling as the `F_q`-dimension and
its quantum parameters in the non-split case. Nothing found here creates a new
theorem either.

---

## Part 1 — Findings

Severity: **C** critical (invalidates a claim), **M** major (needs repair before
the result can be cited), **m** minor (typographical / expository), **V**
verification-coverage limitation.

### F1 — `C` — Provenance mismatch between the brief and the audited PDF
The blueprint names Yadav et al. (2024, DOI `10.1007/s40314-024-02789-1`) as the
source; the uploaded PDF is Debnath–Islam–Martínez-Moro–Prakash,
arXiv:2412.08512v1. Details in `SOURCE_PAPER_METADATA.md` §2.
**Effect:** none on the mathematics of S1; total effect on provenance. Any
manuscript must cite S1 for S1's theorems.
**Action taken:** audit pinned to S1; Yadav et al. held as separate item `[Y2024]`.

### F2 — `m` — Example 2: stated factor multiplicities contradict the paper's own data
Example 2 (p.19) states `β_{11}(1)=1, β_{11}(7)=3, β_{21}(4)=1, β_{21}(28)=3`.
But:
- the paper's own displayed factorization of `x^7−1` over `F_9` is
  `(x+2)(x³+ωx²+ω⁷x+2)(x³+ω³x²+ω⁵x+2)` — **two** cubics, so `β_{11}(7)=2`;
- the paper's own expansion is `b_{117} = b_{1117} + b_{1127}` — **two** summands;
- the same for `b_{2128} = b_{21128}+b_{21228}` — two summands, so `β_{21}(28)=2`;
- our independent factorization confirms degrees `1,3,3` for both `x^7−1` and
  `x^7−ω²` (`verification/verify_examples.out`).

So the printed "3" in both places is inconsistent with the surrounding text and
with the mathematics. **[OCR-SUSPECT]** — the extracted glyph could be a misread
"2", but the surrounding arithmetic is unambiguous.
**Effect on the result:** none. The final hull dimension (0) is unaffected and is
reproduced exactly. Purely typographical.

### F3 — `M` — Corollary 3.5(2) is false as printed when `n` is odd
Part 2 claims: if `p = 2`, `e` even, `k = e/2`, and `ord(λ)n' | (2^e−1)`, then
`|D_{e/2}(n,2^e,λ)| = N n/2 + 1`.

Take `n = n' = 1` (i.e. `e' = 0`), which satisfies `gcd(n',p)=1` and is not
excluded. Then `D = {0}` and `|D| = 1`, while `N·1/2 + 1` is not an integer.

The proof (p.16) evaluates `β_{S t}(j)⌊a_t p^{e'}/2⌋` with `p^{e'} = 1`, i.e. a
factor `½`; the computation `= Nn/2` is only integral when `n` is even. Since
`n = n'2^{e'}` with `n'` odd, `n` is even **iff `e' ≥ 1`**.
**Repair:** add `e' ≥ 1` (equivalently `p | n`) to the hypotheses of part 2.
**Status of part 1:** unaffected; `n' = 1` with `p` odd gives `n = p^{e'}` odd and
the formula `N(n−1)/2 + 1` is integral for every `e' ≥ 0`.

### F4 — `m` — Lemma 5: the inference is invalid, the statement is true
Lemma 5 asserts `Δ_{S t} = Σ_{j∈D_{S t}} φ(j)/(a_t φ(r_{S(ν)}))`. The printed proof
starts from the *summed* identity `Σ_t a_t Δ_{S t} = n'` and the *summed* identity
`Σ_t Σ_j φ(j)/φ(r_S) = n'`, and then concludes the termwise identity in `t`.
That inference is not valid: two sums being equal does not identify summands.

The statement is nevertheless true, by direct degree counting: the number of
irreducible factors of degree `ord_j(q)` attached to the pair `(t,j)` is
`φ(j)/(a_t φ(r_S) ord_j(q))`, hence
`Δ_{S t} = Σ_j β_{S t}(j)·ord_j(q) = Σ_j φ(j)/(a_t φ(r_S))`.
**Repair:** two lines, replacing the invalid inference with the count above.
**Effect:** none on Theorem 8, which uses only the truth of the identity.

### F5 — `m` — Theorem 8: the range bound is asserted without proof
Theorem 8 ends with `0 ≤ b_{S(ν)t j} ≤ β_{S(ν)t}(j)·⌊a_t p^{e'}/2⌋`, offered with
no argument. It is true, and the proof is short:
since `max{x,y} ≥ (x+y)/2`,
```
Σ_{δ=0}^{a_t−1} max{u_δ, p^{e'} − u_{δ−1}}
   ≥ ½ Σ_δ (u_δ + p^{e'} − u_{δ−1})
   = ½ · a_t p^{e'},
```
so `b_{S t i j} ≤ a_t p^{e'}/2`, and integrality gives the floor. The lower bound
`b ≥ 0` follows from `max{u_δ, p^{e'}−u_{δ−1}} ≤ p^{e'}`.
**Repair:** insert the two-line argument. **Status:** statement correct.

### F6 — `m` — Inner-product slot convention is asymmetric; a recomputation must pin it
`[S1 Eq. (2)]` defines `⟨α,β⟩_k = Σ α_i β_i^{p^k}` — the **second** slot is
conjugated and the **first** is not. Consequently
`C^{⊥_k} = (C^{(p^k)})^⊥`, not `(C^{(p^{e−k})})^⊥`, and the hull depends on which
slot the dual is taken in. Swapping the convention replaces `C^{⊥_k}` by
`(C^{(p^{−k})})^⊥`, which in general is a **different subspace**.

Our recomputations use S1's convention exactly, and reproduce both worked examples.
**Additional evidence gathered:** across 11 parameter sets and **385 distinct
constacyclic codes** (`F_9` with `n = 7,8`; `F_25` with `n = 6`; `F_4` with
`n = 4,5`; `k = 1`), the two conventions gave the *same hull dimension* in every
case (0 differences). We do **not** have a proof of dimension-invariance, so the
observation is recorded as `[VERIFIED-EMPIRICAL]`, not as a theorem.
**Practical rule for any follow-up work:** use S1's convention; do not assume the
hull *subspace* is convention-independent even if the dimension appears to be.

### F7 — `m` — Typographical slips
| ID | Location | Printed | Should be |
|---|---|---|---|
| `[S1-TYPO-1]` | Cor. 3.2 proof, p.10 | "from **Theorem 4**, `D` is self-dual" | **Lemma 4** |
| `[S1-TYPO-2]` | Thm 9, p.16 | "**A** divides `1+p^{e−k}`" | **`r`** divides |
| `[S1-TYPO-3]` | Cor. 3.5 proof, p.16 | `= Nn/2` written as `= Nn^2` in extraction | `Nn/2` |

### F8 — `V` — Imported results were not checked against their sources
Lemma 1 and Theorem 1 cite Liu–Fan–Liu [27]; Theorem 4 cites Yılmazgüç et al. [44]
Proposition 3; Lemma 7 cites Cao [7]; Lemma 8 cites Lai–Ashikhmin [22];
Lemma 2 cites [44]; Eq. (5) and the identity `Σ_t Σ_j φ(j)/φ(r) = n'` cite
Debnath–Prakash–Islam [9]. All are paywalled or were not retrievable in full.
**Consequence:** anything resting on them is `[SOURCE-DEPENDENT]`, not
`[ESTABLISHED]` from this audit. Theorem 1's *content* was nevertheless confirmed
operationally, because `dim = n − deg lcm(g,h^#)` reproduces both examples.

### F9 — `V` — Table 1 was not independently recomputed
Table 1 (p.22) lists 13 EAQECCs. Only the two rows that are Examples 2 and 3
(`n=7, λ=e_1+ω²e_2`, and `n=13, λ=e_1+ω⁸e_2`) were recomputed end to end; both
match exactly, including the minimum distances `4` and the `c` values `4` and `2`.
The other 11 rows depend on generator polynomials given only as coefficient
vectors and on distances attributed to Grassl's table; they were **not** checked.
No claim in this audit depends on them.

### F10 — `S` (scope, not a defect) — S1 contains **no** enumeration theorem
The register records **zero** results of type `COUNT`. The only cardinality result
(Corollary 3.5) counts *attainable dimension values*, not codes.
S1's Conclusion (p.23) states the enumeration problem is **open** over `A`.
This is the origin of the project; it is a gap *declared by the authors*, which is
the strongest legitimate form of gap statement — but it is still only a gap, not a
contribution.

### F11 — `M` — **Structural hypothesis gap: the component fields are not `F_q` in general**
This is the most substantive finding of the audit and it was not visible from
reading alone. It emerged from checking the examples against their own data.

**The issue.** §2.1 defines `S(ν)` and correctly states
`|S(ν)| = lcm(d_1,…,d_ℓ) = [F_q(ν_1,…,ν_ℓ) : F_q]`. Hence the CRT component
`A_S = F_q(ν_1,…,ν_ℓ)` is an extension field of degree `|S(ν)|` over `F_q`, and
`dim_q A = Σ_S |S(ν)| = |H| = ∏_i deg t_i`.

But §2.3 then writes every `a ∈ A` as `a = Σ_S a_{S(ν)} e_{S(ν)}` with
**`a_{S(ν)} ∈ F_q`**, defines `C_{S(ν)} ⊆ F_q^n`, and builds the Gray map
`ψ : A → F_q^N` with `N = |Ŝ|`. That is correct **iff every class `S(ν)` is a
singleton**, i.e. iff **every `t_i` splits over `F_q`**. In that case
`N = |H| = dim_q A` and everything is consistent.

**The examples are not in that case.** Verified by factorization
(`verification/verify_examples.out`):
- Example 2: `t_1 = x²+x+ω` is **irreducible** over `F_9` (discriminant `ω³`, a
  non-square); `t_2 = x²+ω⁵x+2` is **irreducible** over `F_9`.
- Example 3: `t_1 = x²+x+ω^13` is **irreducible** over `F_25`.

For Example 2: `|H| = 2·2 = 4`, and the paper's own `N = 2` then forces
`|S(ν)| = 2`. So each component is `F_81`, not `F_9`:
`dim_9 A = 4 ≠ N = 2`.

**Consequences.**
1. `ψ : A → F_q^N` has domain of `F_q`-dimension 4 and codomain of dimension 2, so
   it **cannot be the bijective isometry asserted on p.17**.
2. An `A`-submodule whose components have `A_S`-dimensions `4` and `6` has
   `dim_q = 2·4 + 2·6 = 20`, not `10`. So the codes in Examples 2–3 do not have
   the dimensions `10` and `22` attributed to them: the claimed `[14,10,4]_9`
   and `[26,22,4]_25` cannot be Gray images of the `A`-modules described.
3. Eq. (8), hence Theorem 8, computes `Σ_S dim_{A_S} hull_k(C_S)` — the sum of the
   **component-field** dimensions. That equals `dim_q hull_k(C)` only when every
   class is a singleton.

**What survives.**
- Theorems 2–7 are statements about the decomposition and are **unaffected**: they
  are correct for `A_S` whatever its degree.
- Theorem 8 is correct as a formula for `Σ_S dim_{A_S} hull_k(C_S)`; it is the
  label "`q`-dimension" that is unjustified in the non-singleton case.
- Every statement of S1 is correct under the **additional hypothesis that all
  `t_i` split over `F_q`**. That hypothesis is not stated and is violated by the
  paper's own examples.

**Why this matters for the present project (and why it is not merely pedantic).**
The natural repair is not cosmetic. It changes:
- which field the local enumerator lives over (`F_{q^{|S|}}`, not `F_q`);
- the relation between the local count and the global count (a factor `|S|` per
  component appears in the `F_q`-dimension);
- the Gray map and therefore every quantum parameter in Table 1.

**Contrast with the blueprint's own setting.** In Yadav et al.'s ring
`R_e = F_{q²}[u]/⟨u^e−1⟩` with `e | (q+1)`, one has `e | q²−1`, so `u^e−1`
**does** split over `F_{q²}`; every class is a singleton and `N = e = dim_{q²} R_e`.
So the blueprint's specific setting is **free of this defect**, and the clean
statement of a "joint Hermitian enumerator" is available there — but precisely
because it is the split case, where the product formula is most transparent and
least novel.

**Recommended status for S1:** `PROVISIONAL` pending either (a) an added
hypothesis "all `t_i` split over `F_q`", or (b) a corrected §2.3 using
`a_S ∈ A_S` and a Gray map `A → F_q^{|H|}`.

**Update, 2026-10-20 — exact loci, independent recomputation, and the three repairs.**
The finding was re-derived from the PDF page by page and recomputed from scratch
(`INDEPENDENT_VERIFICATION_REPORT.md` §3; `verification/independent_verification.out`).

*Exact locations of the `F_q` assumption:*
- p.9, Corollary 3.1 — "`C_{S(ν)}` is a `k`-Galois self-dual code **over `F_q`**";
- p.12, Theorem 8 proof — "where `C_{S(ν)}` are `λ_{S(ν)}`-constacyclic codes **over `F_q`**";
- p.12, Theorem 8, statement — "the **`q`-dimension** of the `k`-Galois hull";
- p.17, eq. (10) — "`a_{S(ν)} ∈ F_q` for all `S(ν) ∈ Ŝ`", `ψ : A → F_q^N`, `N = |Ŝ|`,
  followed by "the map `ψ` is bijective linear isometry".

*The strongest form of the contradiction needs no computation.* `dim_q A = ∏_i deg t_i`
and `dim_q F_q^N = N = |Ŝ|`. In Examples 2, 3 and the `q = 4` ring of Table 1,
`∏ deg t_i = 4` while `N = 2`. Therefore `|A| = q^4 ≠ q^2 = |F_q^N|`, and `ψ` is not a
bijection. This is a cardinality contradiction, not a modelling preference.

*Repairs, with costs.*

| Repair | Statement | Cost |
|---|---|---|
| **R1** | Add "every `t_i` splits over `F_q`" (⟺ `|S(ν)| = 1` for all `ν`) | consistent, but all three rings used in the paper fail it; Examples 2–3 and Table 1 must be rebuilt |
| **R2** | Keep general `t_i`; `ψ : A → F_q^{dim_q A}` via `F_q`-bases of the `A_S` | `N` becomes 4, not 2; every length doubles; `ψ` is only `F_q`-linear, so Lemma 9 needs a new proof |
| **R3** | Restrict to codes with `a_{S(ν)} ∈ F_q` | not closed under multiplication by `A`; not a code over `A` |

*Recomputed values.* `dim_q C = 20` (Example 2) and `44` (Example 3), against claimed
code lengths `14` and `26`; the paper's `10` and `22` are `Σ_S (n − deg g_S)`, i.e. the
dimensions computed as if each component were `F_q`.

*Scope of the claim.* Established for **arXiv:2412.08512v1 only**. The version of
record (*Discrete Math.* **349**(2) (2026) 114750) has additions (an "Example 4" and a
"Table 2" are referenced in its introduction) and could not be read; whether F11
persists there is **BLOCKED** and must not be asserted either way.

---

## Part 2 — Positive verification record

| # | Claim of S1 | How checked | Result |
|---|---|---|---|
| P1 | `hull_k(C) = ⊕_S hull_k(C_S)` and hull dimension is additive (Thm 7) | direct sum over component codes; compare joint histogram with convolution | **PASS** (25 = 25 codes, histograms identical) |
| P2 | Example 2 total hull dimension `0` | built both component codes, exact nullspace intersection | **PASS** |
| P3 | Example 2 `ψ(C) = [14,10,4]_9`, EAQECC `[[14,10,4;4]]_9` | Gray matrix built from `M`; exact `d` by parity-check column dependence | **PASS** |
| P4 | Example 3 total hull dimension `2` | as above | **PASS** |
| P5 | Example 3 `ψ(C) = [26,22,4]_25`, EAQECC `[[26,20,4;2]]_25` | as above | **PASS** |
| P6 | Factorizations of `x^7−1`, `x^7−ω²`, `x^13−1`, `x^13−ω⁸` | Cantor–Zassenhaus | **PASS** (degrees 1,3,3 / 1,3,3 / 1,2×6 / 1,2×6) |
| P7 | Corollary 3.5(1): `|D| = N(n−1)/2+1` | brute force, `q=9, n=9, k=1, λ=±1`, `N=2` | **PASS** (9 = 9) |
| P8 | Corollary 3.5(2): `|D| = Nn/2+1` | brute force, `q=4, n=4, k=1, λ=ω`, `N=2` | **PASS** (5 = 5) |
| P9 | Lemma 9: `dim hull_k(ψ(C)) = dim hull_k(C)` | computed hull of Gray image | **PASS** (0 and 2) |
| P10 | Gray matrix condition `M M^{(p^k)T} = γI_N` | direct matrix product | **PASS**, `γ = 1` in both examples |

Raw logs: `verification/verify_examples.out`, `verification/verify_corollary_3_5.out`.

---

## Part 3 — What the audit establishes about the *gap*

Three statements must be kept strictly apart, because the whole project turns on
the difference:

1. **`[SOURCE]` S1 does not enumerate codes by hull dimension.** (Register: zero
   `COUNT` results.)
2. **`[SOURCE]` S1 declares that enumeration open.** (Conclusion, p.23.)
3. **`[FALSE INFERENCE]` "therefore an enumeration over `A` is new."**

Statement 3 does **not** follow, and the blueprint forbids exactly this inference
(p.2: *"Never claim a gap just because a result is absent from the source paper;
compare the wider literature"*). Part 2 of `literature/NOVELTY_ASSESSMENT.md`
supplies the wider comparison, and it is decisive against statement 3.

---

## Part 4 — Audit status

| Aspect | Status |
|---|---|
| Completeness of reading | **PASS** — all 27 pages, all 44 references listed, all proofs read |
| Theorem register completeness | **PASS** — 10 theorems, 9 lemmas, 5 corollaries, 2 remarks, 3 examples, 1 table |
| Main-line correctness | **PASS** with F4, F5 repairs; **PROVISIONAL** on F11 (needs the split hypothesis or a corrected §2.3); F3 is a boundary repair |
| Independent numerical confirmation | **PASS** for Examples 2–3 and Corollaries 3.4/3.5 — **within S1's own component model**, see F11 |
| External-source confirmation | **BLOCKED** (paywalls) — F8 |
| Full table reproduction | **NOT DONE** — F9, disclosed |
| Overall | **PASS with repairs** for the register/audit purpose; **PROVISIONAL** as a statement about `dim_q` in the non-split case |
