# FINAL INDEPENDENT MATHEMATICAL CHECK

**Date:** 2026-10-20
**Source:** Debnath–Islam–Martínez-Moro–Prakash, *Galois hulls of constacyclic codes over
affine algebra rings*, arXiv:2412.08512**v1** (11 Dec 2024), 27 pp, SHA-256 `0db90bfb…c039`.
Version of record: *Discrete Math.* **349**(2) (2026) 114750, DOI `10.1016/j.disc.2025.114750`
— **not read; see §4.4, BLOCKED.**

**Scope.** This document records a self-contained verification of two independent claims:
(Task A) that the Galois hull dimension is not an invariant of isometry for constacyclic
codes, and (Task B) that the source paper's component-field bookkeeping is defective
(audit item F11). It closes with a recommendation (§5).

**No novelty is claimed.** Everything here is either a correction of a published
statement or an elementary observation about how a question must be formulated. §5.4
lists what would have to be true for any of it to be more than that.

---

# TASK A — The isometry counterexample

## A.0 Summary of results, including one correction to our own earlier record

| Item | Result | Status |
|---|---|---|
| `C = ⟨1+x⟩ ⊆ F₄[x]/(x³−1)`, `φ = diag(1,ω,ω²)` | reproduced exactly | **confirmed** |
| `dim_F4 hull₀` (Euclidean): `C` vs `φ(C)` | **0 → 1** | **confirmed** |
| `dim_F4 hull₁` (Hermitian): `C` vs `φ(C)` | **0 → 0** | **CORRECTED** |
| `φ(C)` cyclic, same dimension, same weight enumerator | yes | **confirmed** |
| General criterion | `a_i^{1+p^k}` constant | **proved + verified** |
| Hermitian counterexample | **exists over `F_9`**: hull₁ `2 → 0` | **new in this check** |

> **Correction.** An earlier note in this project (`C1_ISOMETRY_SCREENING.md`) reported the
> `F_4` witness as changing **both** the Euclidean and the Hermitian hull. That was wrong.
> The earlier script raised field elements to the power `q^k = 4^k`; the paper's inner
> product (p.7) uses `p^k = 2^k`. Since `x⁴ = x` for all `x ∈ F₄`, the "k = 1" computation
> was silently the Euclidean one. Recomputed with the correct exponent, **the Hermitian
> hull is unchanged at `q = 4`** — and §A.5 shows it *cannot* change there. §5 records the
> other documents that need this correction.

## A.1 Conventions, fixed explicitly

**Field.** `F₄ = F₂[ω]/(ω² + ω + 1)`, so `ω² = ω + 1` and `ω³ = 1`. Elements are stored
as `a₀ + 2a₁` meaning `a₀ + a₁ω`:

```
0 = 0   1 = 1   2 = ω   3 = ω²
addition (⊕):        multiplication (⊗):
0 1 2 3              0 0 0 0
1 0 3 2              0 1 2 3
2 3 0 1              0 2 3 1
3 2 1 0              0 3 1 2
orders of units: 1 → 1, ω → 3, ω² → 3
```

**Code generator.** `C = ⟨1 + x⟩ ⊆ F₄[x]/(x³ − 1)`, i.e. the set of all
`f(x)(1+x) mod (x³ − 1)` for `f` ranging over the 64 ring elements.

**Coordinate convention** (paper p.4). A vector is `(c₀, c₁, …, c_{n−1})` with the index
equal to the power of `x`. The `λ`-shift is

```
T_λ(c₀, …, c_{n−1}) = (λ c_{n−1}, c₀, …, c_{n−2}),
```

and `C` is `λ`-constacyclic iff `T_λ(C) ⊆ C`.

**Inner products** (paper p.7, `⟨ρ,ρ′⟩_k = Σ_i ρ_i (ρ′_i)^{p^k}`). The exponent is the
**`p`-power**, not the `q`-power:

```
k = 0 :  ⟨u,v⟩₀ = Σ u_i v_i        (Euclidean)
k = 1 :  ⟨u,v⟩₁ = Σ u_i v_i²       (Hermitian, since √4 = 2)
```

**Hull.** `hull_k(C) = C ∩ C^{⊥_k}` with
`C^{⊥_k} = {v : ⟨v,c⟩_k = 0 for all c ∈ C}`, evaluated by enumerating all `4³ = 64`
vectors and intersecting sets.

**A remark that matters for Task B.** `x³ − 1 = (x+1)(x+ω)(x+ω²)` **splits** over `F₄`.
So this ring is exactly the case in which the source paper's component model is valid
(every `|S(ν)| = 1`). Task A is therefore a *fair* test of the isometry question: it is
not contaminated by the defect analysed in Task B.

## A.2 Reproduction

`C = ⟨1+x⟩` has `|C| = 16`, `dim_F4 = 2`. Its 16 codewords (full list is in
`verification/final_check_A.out`):

```
000            110  1ωω²  1ω²ω   ω0ω   ωω0   ωω²1   ω²0ω²  ω²ω1
011            101  11ω   1ω1    ω1ω²  ωω²0  ω²1ω   ω²ω²0
0ωω 0ω²ω² …
weight distribution: {0: 1, 2: 9, 3: 6}
```

`φ = diag(1, ω, ω²)` satisfies `φ(f) = f(ωx)` for **every** element of the ring (checked
exhaustively). Consequently:

* `φ` is a monomial (diagonal, invertible) map, so it preserves every Hamming weight;
* `φ` is an `F₄`-algebra automorphism, since `(ωx)³ = ω³x³ = x³`;
* therefore `φ` maps ideals to ideals, i.e. cyclic codes to cyclic codes.

`φ(C)` has `|φ(C)| = 16`, `dim_F4 = 2`, is closed under `T₁` (**cyclic**), is *not*
closed under `T_ω`, and has the **same weight distribution** `{0:1, 2:9, 3:6}`.
`C ≠ φ(C)` as sets.

## A.3 Hull dimensions (brute force over all 64 vectors)

| `k` | form | `dim hull_k(C)` | `dim hull_k(φC)` | changed? |
|---|---|---|---|---|
| 0 | Euclidean | 0 | **1** | **YES** |
| 1 | Hermitian | 0 | 0 | no |

```
hull₀(C)      = {(0,0,0)}
hull₀(φC)     = {(0,0,0), (1,ω²,ω), (ω,1,ω²), (ω²,ω,1)}
```

By hand: a general element of `φ(C)` is `(α, (α+β)ω, βω²)`. The Euclidean conditions
`⟨v,φ(1+x)⟩ = 0` and `⟨v,φ(x+x²)⟩ = 0` reduce to

```
α + (α+β)ω² = 0        (α+β)ω² + βω = 0,
```

whose solutions are `(α,β) = (sω², sω)`, `s ∈ F₄` — a one-dimensional space, as computed.

## A.4 Why the Hermitian case cannot work at `q = 4`, and a genuine `F_9` witness

`⟨φu, φv⟩₁ = Σ a_i^{1+p} u_i v_i^{p}` with `p = 2`. Over `F₄`, `a³ = 1` for **every**
nonzero `a`, so `a_i^{1+p} = a_i³ = 1` identically. **Every** monomial map is therefore a
similarity of the Hermitian form, and `hull₁` is an isometry invariant at `q = 4` — no
counterexample of any shape exists there. This is a structural fact, not a small-range
accident.

Over `F₉ = F₃(ω)`, `ω² + 2ω + 2 = 0`, the norm `a^{1+3} = a⁴` is a nontrivial character
`F₉* → F₃* = {1,2}`. Taking the multiplier `ψ₂ : f(x) ↦ f(x²)` (a permutation with
scalings `b^{⌊2i/5⌋} = (1,1,1,ω,ω)`, hence weight preserving) gives:

| | source | image |
|---|---|---|
| ring | `F₉[x]/(x⁵ − ω²)` | `F₉[x]/(x⁵ − ω)` |
| generator | `g = 2 + 6x + x²` | `ψ₂(g)` |
| shift | `ω²` | `ω` |
| constacyclic | yes | **yes** |
| `dim_F9` | 3 | 3 |
| **`dim hull₁`** | **2** (`|hull| = 81 = 9²`) | **0** (`|hull| = 1`) |

Both codes are `λ`-constacyclic for their respective `λ`, so this is a counterexample
**inside the family the source paper counts**, with the **Hermitian** (`k = 1`) hull —
the very parameter its Examples 2–3 compute. Full search: `256` (shift, multiplier,
code) triples at `n = 5`, `32` of them change the Hermitian hull dimension.

The scalings have norms `(1,1,1,2,2)`, non-constant, exactly as the criterion predicts.

## A.5 The general criterion, with proof

**Proposition.** Let `φ` be the monomial map `φ(e_i) = a_i e_{π(i)}` with `a_i ∈ F_q*` and
`π` a permutation. Then for all `u, v ∈ F_q^n`,

```
⟨φu, φv⟩_k = Σ_i a_i^{1+p^k} · u_i · v_i^{p^k}.
```

*Proof.* `(φu)_{π(i)} = a_i u_i`. Then

```
⟨φu,φv⟩_k = Σ_j (φu)_j ((φv)_j)^{p^k}
          = Σ_i a_i u_i (a_i v_i)^{p^k}
          = Σ_i a_i^{1+p^k} u_i v_i^{p^k}.  ∎
```

**Corollary 1 (invariance).** If `a_i^{1+p^k}` is independent of `i`, say `= c`, then
`⟨φu,φv⟩_k = c⟨u,v⟩_k` with `c ≠ 0`; hence

```
u ∈ C^{⊥_k}  ⟺  φu ∈ (φC)^{⊥_k},
```

so `φ(C^{⊥_k}) = (φC)^{⊥_k}`, `φ(C ∩ C^{⊥_k}) = φC ∩ (φC)^{⊥_k}`, and
`dim hull_k(φC) = dim hull_k(C)`.

**Definition.** `Sim_k = {φ monomial : a_i^{1+p^k} constant}` — the **similarity group of
the `k`-Galois form**. Corollary 1 says `dim hull_k` is a class function on `Sim_k`-classes.

**Corollary 2 (sharpness).** `Sim_k ⊊ M(q,n)` whenever `q > 2` and `k < e`:
`a^{1+p^k}` is then a nontrivial multiplicative character, so diagonals with non-constant
character exist. At `q = 4`, `n = 3`: `|M| = 3!·3³ = 162`, `|Sim₀| = |Sim₁| = 18`, index
`9`. `diag(1,ω,ω²)` is outside `Sim₀` and inside `Sim₁` — which is precisely the pattern
observed in §A.3.

**Verification.** The identity of the Proposition was checked on 300 random
`(k, π, a, u, v)`: **0 mismatches**. The invariance of Corollary 1 was checked
exhaustively on `432` (code, similarity, `k`) triples at `q = 4`, `n = 3`: **0 failures**.

## A.6 What Task A establishes

1. The `F₄` reproduction is exact, including the Euclidean hull change `0 → 1`.
2. **The Hermitian `k = 1` hull does *not* change at `q = 4`**, and provably cannot;
   the earlier claim to the contrary is retracted.
3. A genuinely Hermitian counterexample exists over `F₉` (`hull₁ : 2 → 0`), so the
   phenomenon is not an artefact of the Euclidean form or of `q = 4`.
4. `dim hull_k` is a class function on `Sim_k`-classes and on no larger class.

**Consequence for the source paper.** Its conclusion (p.23) proposes, as future work,

> "the enumeration of non-isometric constacyclic codes for a given Galois hull dimension
> is an interesting problem. This problem is still open over `A`."

Taken literally, this asks for the number of isometry classes carrying a given hull
dimension. By §A.3 and §A.4 that number is not defined: the same isometry class carries
several. The sentence is a *symptom* of the same conceptual gap as F11 — a statistic
being attributed to an equivalence class that does not preserve it — and it requires
reformulation before it can be answered, not merely computation.

---

# TASK B — Independent check of F11

## B.1 The exact statements, at their loci

| Page | Statement (verbatim where quoted) |
|---|---|
| p.4 | `\|S(ν)\| = lcm(d₁,…,d_ℓ) = [F_q(ν₁,…,ν_ℓ) : F_q]` |
| p.5 | `A ≅ ⊕_{S(ν)∈Ŝ} F_q[X₁,…,X_ℓ]/I_{S(ν)} ≅ ⊕_{S(ν)} F_q(ν₁,…,ν_ℓ)` (the line above writes "`R ≅ …`", a slip for `A`) |
| p.7 | "Since `A = Σ_S(e_S F_q)`, each element `a ∈ A` can be expressed as `a = Σ a_{S(ν)} e_{S(ν)}`, where **`a_{S(ν)} ∈ F_q` for all `S(ν)`**" |
| p.7 | `C_{S(ν)} = {c_{S(ν)} ∈ F_q^n ∣ c ∈ C}` — the projection is declared to land in `F_q^n` |
| p.10 | Corollary 3.1: "`C_{S(ν)}` is a `k`-Galois self-dual code **over `F_q`**" |
| p.12 | Theorem 8: "the **`q`-dimension** of the `k`-Galois hull"; eq. (8): `dim(hull_k(C)) = Σ_S {n − deg(lcm(g_S, h_S^#))}` |
| p.12 | Theorem 8 proof: "`C_{S(ν)}` are `λ_{S(ν)}`-constacyclic codes **over `F_q`**" |
| p.17 | eq. (10): `ψ : A → F_q^N`, `a ↦ (a_{S(ν₁)},…,a_{S(ν_N)})M`, "where `\|Ŝ\| = N`" |
| p.17 | "It is easy to verify that the map `ψ` is **bijective linear isometry** from `A^n` to `F_q^{nN}`" |
| p.18 | Theorem 10: `[[nN, k − dim_q(hull_k(C)), d ; nN − k − dim_q(hull_k(C))]]_q`, for `ψ(C)` an `[nN,k,d]` code |

> **Page correction.** `Corollary 3.1` begins on **p.10**, not p.9 as an earlier version of
> our report stated. The substance ("over `F_q`") is unchanged.

## B.2 Derivation from first principles

Let `A = F_q[X₁,…,X_ℓ]/⟨t₁(X₁),…,t_ℓ(X_ℓ)⟩` with the `t_i` squarefree.

**(i) The components are fields of degree `|S(ν)|`.** For a maximal ideal `I_{S(ν)}`,
`A/I_{S(ν)} ≅ F_q(ν₁,…,ν_ℓ)`, a finite extension of `F_q` of degree `[F_q(ν₁,…):F_q]`,
which is `lcm(d₁,…,d_ℓ)` because each `ν_i` has degree `d_i` over `F_q` and the `ν_i` lie
in independent extensions. This is the paper's own p.4 formula.

**(ii) `dim_q A = Σ_S |S(ν)| = ∏_i deg t_i`.** Both sides are the `F_q`-dimension of `A`:
the first from the CRT, the second because `A` has the monomial basis
`{X₁^{e₁}…X_ℓ^{e_ℓ} : e_i < deg t_i}`. (For `ℓ=2`: `q^{deg t₁ · deg t₂}` elements.)

**(iii) Hence `a_{S(ν)}` lies in `F_{q^{|S(ν)|}}`, not in `F_q`,** unless every
`|S(ν)| = 1`. This is exactly where p.7 departs from p.4: p.4 computes the degree
`lcm(d_i)`, p.7 silently sets it to 1.

**(iv) Consequence for `ψ`.** `|A| = q^{dim_q A}` but `|F_q^N| = q^N` with `N = |Ŝ|`.
Since `Σ_S |S(ν)| = dim_q A` with `|Ŝ|` summands, `dim_q A > N` as soon as some `|S(ν)|>1`.
Then `|A| > |F_q^N|` and `ψ` **cannot be injective**, let alone bijective.

**(v) Consequence for dimensions.** `C = ⊕_S C_S e_S` with `C_S ⊆ A_S^n`. Therefore

```
dim_q C = Σ_S |S(ν)| · dim_{A_S}(C_S),        dim_q hull_k(C) = Σ_S |S(ν)| · dim_{A_S} hull_k(C_S),
```

whereas Theorem 8 / eq. (8) computes `Σ_S dim_{A_S}(…)` with no factor `|S(ν)|`.

## B.3 Contradiction or convention? — **Contradiction**

The candidate defences and their answers:

| Defence | Answer |
|---|---|
| "The paper means `A_S = F_q`." | Then p.4's `\|S(ν)\| = lcm(d_i)` is false, and with it the CRT. The paper states both; they cannot both hold. |
| "`N` might mean `dim_q A`." | p.17: "where `\|Ŝ\| = N`", and p.19: "`N = 2`. Then there are 2 idempotents". `N` is the number of components, unambiguously. |
| "`a_{S(ν)} ∈ F_q` might be a harmless abuse." | It is not harmless: it fixes `\|A\|`, hence the codomain of `ψ`, hence the length of every code in Table 1. |
| "The examples might satisfy `\|S(ν)\| = 1`." | They do not (§B.4). |
| "It is a typo in one place." | The `F_q` assumption recurs at p.7 (twice), p.10, p.12 (twice), p.17, and is used in every computation. |

**Verdict: a genuine contradiction, not a notational variant.** The paper's *arithmetic*
is nevertheless internally consistent — it reproduces exactly when every dimension is
read as an `A_S`-dimension (§B.4). The defect is the missing factor `|S(ν)|`, i.e. the
implicit claim `dim_q A = N`.

**Severity:** `M`. It affects the Gray map, every code length, every code dimension, one
hull value, and every quantum parameter. It does not affect Theorems 2–7, which are
statements about the decomposition and are correct for `A_S` of any degree.

## B.4 Computed values

### Example 2 (p.18–20)

```
F_9 = F_3(ω), ω² + 2ω + 2 = 0
t₁ = x² + x + ω        irreducible over F_9: True
t₂ = x² + ω⁵x + 2      irreducible over F_9: True
dim_F9 A = 2·2 = 4       |A| = 9⁴ = 6561
idempotents of A: 4;  primitive: 2  ⇒  |Ŝ| = N = 2
A ≅ F_81 × F_81          |F_9^N| = 9² = 81
```

`x⁷ − 1` and `x⁷ − ω²` both factor over `F_9` with degrees `{1, 3, 3}`; the paper's `g₁`
(degree 3) and `g₂` (degree 1) both divide their moduli, as printed.

| quantity | printed | correct |
|---|---|---|
| `Σ_S (n − deg g_S)` / `Σ_S \|S\|(n − deg g_S)` | 10 | **20** |
| direct rank of the ideal `⟨g⟩` over `F_9` | — | **20** |
| claimed code length `nN` | 14 | **28** (= `n·dim_q A`) |
| `dim hull₁` | 0 | **0** (unaffected) |

### Example 3 (p.20–21)

```
F_25 = F_5(ω), ω² + 4ω + 2 = 0
t₁ = x² + x + ω¹³      irreducible over F_25: True
t₂ = x² + ω³x + 1      irreducible over F_25: False — it splits, roots in F_25
dim_F25 A = 4            |A| = 25⁴ = 390625 ;  |F_25^N| = 25² = 625
A ≅ F_625 × F_625,  N = 2   (t₂'s roots have degree 1, t₁'s degree 2, so |S| = 2)
```

`x¹³ − 1` and `x¹³ − ω⁸` both factor with degrees `{1,2,2,2,2,2,2}`; `g₁` (degree 3) and
`g₂` (degree 1) divide their moduli.

| quantity | printed | correct |
|---|---|---|
| `Σ_S (n − deg g_S)` / weighted | 22 | **44** |
| direct rank of `⟨g⟩` over `F_25` | — | **44** |
| claimed length `nN` | 26 | **52** |
| `dim hull₁` | 2 | **4** |

### The decisive diagnostic: every printed number is an `A_S`-dimension

Computing each component inside its own field `A_S` (degree 2 over `F_q`) reproduces the
paper's numbers **exactly**, and shows the missing factor:

| component | `dim_{A_S}` | `hull_{A_S}` | `\|S\|` | `dim_q` | `hull_q` |
|---|---|---|---|---|---|
| Ex 2, component 1 (`F_81`, `n=7`, `λ=1`) | 4 | 0 | 2 | 8 | 0 |
| Ex 2, component 2 (`F_81`, `n=7`, `λ=ω²`) | 6 | 0 | 2 | 12 | 0 |
| Ex 3, component 1 (`F_625`, `n=13`, `λ=1`) | 10 | 2 | 2 | 20 | 4 |
| Ex 3, component 2 (`F_625`, `n=13`, `λ=1`, `λ=ω⁸`) | 12 | 0 | 2 | 24 | 0 |

`4+6 = 10` and `10+12 = 22` — the printed dimensions. `0+0 = 0` and `2+0 = 2` — the
printed hull dimensions. **The paper's computation is flawless under the substitution
`dim_q ↦ dim_{A_S}`.** The single missing step is multiplication by `|S(ν)| = 2`.

### Example 1 (p.5) — the defect is not confined to §4

`t₁ = x⁵+x⁴+1` factors as degrees `{2,3}`; `t₂ = x⁴+x²+x` as degrees `{1,3}`.
Then `|Ŝ| = Σ gcd(d₁,d₂) = 6` (matching the paper's "six classes") but
`Σ|S(ν)| = Σ d₁d₂ = 20 = ∏ deg t_i`. Class sizes are `2,6,3,3,3,3`, not all 1.
**Even Example 1 is not the split case.**

*(Minor separate slip: p.5 writes `t₂ = x₂(x₂²+x₂+1)`, whose product is `x³+x²+x`, not
`x⁴+x²+x`. The correct factorisation is `t₂ = x₂(x₂³+x₂+1)`.)*

## B.5 The quantum parameters

Theorem 10 as stated is `[[nN, k − dim_q(hull_k(C)), d ; nN − k − dim_q(hull_k(C))]]_q`
for `ψ(C) = D` an `[nN,k,d]` code. Its **arithmetic is applied correctly**:

```
Ex 2:  nN = 14, k = 10, hull = 0  →  [[14, 10, 4 ; 4]]      = paper ✓
Ex 3:  nN = 26, k = 22, hull = 2  →  [[26, 20, 4 ; 2]]      = paper ✓
```

So the error is upstream of Theorem 10, in the parameters of `D`. Under the correction
the *dimensions* become `[[28, 20, d ; 8]]` and `[[52, 40, d ; 8]]`, but:

> **The corrected quantum parameters are NOT established, and this document does not
> assert them.** Two obstacles: (a) the minimum distance `d` of the true Gray image has
> not been computed; (b) Lemma 9 (`ψ(hull_k(C)) = hull_k(ψ(C))`), on which Theorem 10
> rests, is proved via `ψ` being an isometry — and the repaired `ψ` (repair R2) is only
> `F_q`-linear, so the orthogonality transfer no longer follows. Repairing F11 therefore
> requires re-proving Lemma 9, not just relabelling dimensions.

## B.6 The three repairs, costed

| | Repair | Consequence |
|---|---|---|
| **R1** | Add the hypothesis "every `t_i` splits over `F_q`" | Internally consistent, everything in §2–§4 goes through. But **all three of the paper's rings fail it** (§B.4), so Examples 1–3 and Table 1 would be void. |
| **R2** | Keep general `t_i`; `ψ : A → F_q^{n·dim_q A}` via `F_q`-bases of the `A_S` | Lengths become 28 and 52; `ψ` is only `F_q`-linear, so Lemma 9 needs a new proof. Not cosmetic. |
| **R3** | Restrict to codes with all `a_S ∈ F_q` | Not closed under multiplication by `A`; not a code over `A`. Not viable. |

---

# TASK C — Decision

## C.1 The evidence in one table

| Question | Answer | Certainty |
|---|---|---|
| Is F11 a real defect in arXiv v1? | **yes** | proved: `\|A\| = q⁴ > q² = \|F_q^N\|`; `dim_q C = 20, 44 > 14, 26 = nN` |
| Is it a convention issue? | **no** | §B.3 |
| Does the version of record still contain it? | **unknown** | **BLOCKED** (§C.4) |
| Is `dim hull_k` an isometry invariant? | **no** | two explicit counterexamples (§A.3, §A.4) |
| Is `dim hull_k` a `Sim_k`-invariant? | **yes** | proved and checked (§A.5) |
| Does the paper's own "open problem" make sense as stated? | **no** | it presumes the invariant relation just refuted |
| Is any of this publication-level novel? | **no** | §C.5 |

## C.2 The three options

### (i) Correction note

**Content.** ~4 pages: the corrected statement of Theorem 8
(`Σ_S |S(ν)|·dim_{A_S}`), the corrected Gray map of length `n·dim_q A`, the corrected
parameters of Examples 2–3 and Table 1, the Lemma 9 gap, and the observation that the
p.23 "non-isometric" formulation is ill-posed.

**Strengths.** The mathematics is already in hand and is not in doubt. It is the only
option with zero remaining mathematical risk. It uses everything produced so far.

**Risks.** (a) **Fatal if the version of record already fixed it.** (b) A correction is
not a research contribution — it will not support a thesis, a grant, or a promotion
case, and this document makes no claim that it will. (c) Journals rarely publish errata
from non-authors without the authors' involvement; the realistic route is a private
communication plus an arXiv note.

**Blocking dependency:** §C.4.

### (ii) Restricted-isometry-class enumeration

**What survives of the original C1.** Only two formulations, both now precisely stated:

* **F1 (`Sim_k`-classes).** Count `Sim_k`-classes stratified by `hull_k`. Well defined
  by Corollary 1 (§A.5). But `|Sim_k|` is small — index `9` at `q=4,n=3` — so the count
  is close to a raw enumeration and the arithmetic content may be nil.
* **F2 (orbit/statistic pairs).** Count monomial orbits of *pairs* `(C, hull_k(C))`.
  Well defined for any group. Task A shows the statistic is genuinely non-constant on
  orbits (`{0,1}` at `q=4,n=3`; `{2,0}` at `q=9,n=5`), so this is a real invariant.

**Strengths.** F1/F2 are the only well-posed versions of the paper's stated open problem.

**Risks.** F1 is plausibly vacuous; F2 is plausibly a reformulation rather than a
theorem. Neither has been shown to yield a statement that is not a restatement of an
enumeration count. Effort to first real signal: 1–2 weeks at `q = 4, 9`, feasible with
the tools present.

**Assessment: not recommended as a primary direction** on current evidence. It is a
reasonable *remark* inside (i), where the counterexamples earn their place by showing
why the naive formulation fails.

### (iii) Abandon both

**What has been produced either way.** A complete theorem register of the source; a
verified diagnosis of a published defect with exact loci and a costed repair; a
reproducible computational model of every worked example; a proof that the originally
proposed contribution (the joint enumerator) is a product of published local results;
and now a proof that the fallback direction was ill-posed.

**When to choose it.** If the version of record already repairs F11, then (i) has no
content and (ii) has no theorem. In that case the honest answer is (iii).

## C.3 Recommendation

> **Take option (i) — a correction note — but only after reading the version of record.
> Do not start (ii). If the version of record already fixes the defect, take (iii).**

The ordering is forced by the asymmetry of the evidence. F11 is proved for arXiv v1 and
is not in doubt; the only thing that can destroy it is the published text. Option (ii),
by contrast, has no theorem at all — it has a well-posed question and a warning that the
question may be trivial. Committing to it would be committing to an unknown.

Concretely, in order:

1. **Obtain *Discrete Math.* 349(2) (2026) 114750.** Read §2.3, §4.1 and §4.2. Record
   in `INDEPENDENT_VERIFICATION_REPORT.md` §5 whether p.7 still asserts `a_S ∈ F_q`,
   whether eq. (10) still says `N = |Ŝ|`, and what Examples 2–4 and Tables 1–2 print.
2. **If the defect is present** → write the correction note. Contents as in §C.2(i).
3. **If the defect is absent** → write nothing further. Record the negative result and
   stop.

Under no circumstances should the Phase-5 manuscript of the original blueprint be
written: that object remains `K`, a product of published local enumerators.

## C.4 Unresolved limitations (explicitly not resolved here)

| # | Limitation | Effect |
|---|---|---|
| L-1 | **Version of record never inspected.** Elsevier full text is paywalled; Semantic Scholar reports green OA = the arXiv preprint itself; arXiv shows only v1. The published introduction cites an "Example 4" and "Table 2" absent from v1, so the published text *is* longer. | F11, and therefore (i), remains **BLOCKED**. No claim is made either way about the published version. |
| L-2 | No Magma/Sage/GAP. All algebra is hand-written (`code/gf.py`, `code/final_check_A.py`, `code/final_check_B.py`). | Cross-checks are against the paper's own printed numbers, which all reproduce. A CAS re-run would be desirable. |
| L-3 | `d` (minimum distance) of the corrected Gray images not computed. | Corrected *quantum* parameters are not stated (§B.5). |
| L-4 | Lemma 9 not re-proved under repair R2. | The repair is not complete; only the defect is established. |
| L-5 | Only `q = 4, 9, 25` and `n ≤ 13` examined. | Counterexamples are existence proofs; no claim of exhaustiveness. |
| L-6 | The isometry observation is very likely known to specialists (it is why mass-formula work acts by the isometry group of the form). | Presented as a correction of our own earlier assumption, not as a discovery. |

## C.5 On novelty — stated plainly

**Nothing in this document is a publication-level novel result.**

- F11 is a **correction** of someone else's paper, not new mathematics.
- The criterion in §A.5 is a two-line computation. Its consequence — that hull dimension
  is a `Sim_k`-invariant and not an `M`-invariant — is the kind of fact a specialist
  would consider evident, and is implicit in the practice of the mass-formula literature
  (Li–Shi–Ling, *IEEE TIT* **71** (2025), act by unitary/symplectic groups).
- The enumeration question in (ii) remains **open and unanswered**; a well-posed
  question is not a result.

What can be claimed is narrower and defensible: *a published theorem's hypotheses are
incomplete, the omission is demonstrated with exact loci and explicit counterexamples,
and it propagates to every parameter in the paper's tables.*

---

## D. Reproducibility

| Script | Output | What it does |
|---|---|---|
| `code/final_check_A.py` | `verification/final_check_A.out` | Task A: `F₄` field tables, code enumeration, both hulls, criterion identity (300 trials), `F₉` Hermitian witness |
| `code/final_check_B.py` | `verification/final_check_B.out` | Task B: irreducibility, idempotent counts, factorisations, ideal ranks, component-field hulls, Example 1 |
| `code/gf.py` | — | exact `GF(p^m)`, polynomial factoring, rank, nullspace (dependency-free) |
| `code/isometry_hull_screening.py` | `verification/isometry_hull_screening.out` | superseded by `code/final_check_A.py`; **its original `k=1` line was wrong and has been fixed (see §A.0)** |

Both `code/final_check_A.py` and `code/final_check_B.py` are self-contained apart from
`code/gf.py`; `code/final_check_A.py` does not import it at all. All outputs are byte-for-byte reproducible from the scripts;
exit status 0.

**Environment:** Python 3.11.2, no CAS, no LaTeX. Source PDF hash
`0db90bfbeda69ad1af231b81d92f24be3589ed15ac2e0ade6605ba7ad0ddc039` (unchanged).
