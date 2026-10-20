# FINAL_F11_EVIDENCE_DOSSIER

**Date:** 2026-10-20 · **Branch:** `arena/1625045b-galios-hull` · **Status:** final source-level
check of finding F11. No correction note drafted, no manuscript, nothing pushed to Git.

**Verdict in one sentence.** For **arXiv:2412.08512v1** the defect is proved at exact
loci by four independent lengths of argument (cardinality, component degree, module
rank, and — new this round — the length-versus-dimension dichotomy, which applies to
**all 13 rows of Table 1**); for the **published version of record** nothing is claimed
— its abstract, introduction and section snippets were read on 2026-10-20 (§4.2), but
its **body is not open access and was not obtained**, so the source-level comparison
remains **BLOCKED**. The decision is **BLOCKED**, not GO and not NO-GO; the
one-sentence rule that resolves it is in §7 and in `FINAL_GO_NO_GO_DECISION.md`.

---

## 0. What this document is, and is not

This is an evidence dossier, not an argument for publication. It does five things:

1. re-derives the component-field / Gray-map / dimension arithmetic of Examples 1–3 from
   the paper's own definitions, using a **new, self-contained implementation** that
   imports nothing from the rest of the project;
2. independently verifies the reported `F_9` isometry witness, including the field
   representation, the multiplier, the inner-product convention and the full hull
   computation;
3. extends the dimension check from Examples 2–3 to **all 13 rows of Table 1**, having
   first validated the transcription of the table against the paper's own definition of
   a constacyclic generator, and shows that the printed length and the printed dimension
   are **jointly inconsistent in every row**, whatever the splitting behaviour of the
   defining polynomials;
4. separates what is **proved about v1**, what is **not established about the version of
   record**, and what **cannot yet be asserted at all**;
5. gives a go/no-go recommendation — **BLOCKED**, with the decision rule that
   resolves it (the companion document `FINAL_GO_NO_GO_DECISION.md` carries the full
   reasoning);
6. anchors every decisive claim to a printed page with a verbatim excerpt — the register
   is `verification/VERBATIM_LOCI_v1.md`, and the third-pass verification record is
   `FINAL_F11_VERIFICATION_LOG.md`.

It does **not** state corrected quantum-code parameters (§4.3).

---

## 1. Source identity and exact loci

**File:** `Galios hulls of constacclic codes over affine algebra rings'.pdf`
(27 pp, 291 546 B), SHA-256
`0db90bfbeda69ad1af231b81d92f24be3589ed15ac2e0ade6605ba7ad0ddc039` — **unchanged
throughout this project**, re-hashed at the start of this turn.

**Identity:** Debnath–Islam–Martínez-Moro–Prakash, arXiv:2412.08512**v1**, submitted
11 Dec 2024. Version of record: *Discrete Mathematics* **349**(2) (2026) 114750,
DOI `10.1016/j.disc.2025.114750` — **partially inspected** 2026-10-20: abstract,
complete introduction, section snippets and reference list read; **body not obtained**
(§4.2).

| Locus | Statement (quoted or close paraphrase) | Role |
|---|---|---|
| p.4 | `\|S(ν)\| = lcm(d₁,…,d_ℓ) = [F_q(ν₁,…,ν_ℓ) : F_q]` | defines the component degree |
| p.5 | `A ≅ ⊕_S F_q[X₁,…,X_ℓ]/I_{S(ν)} ≅ ⊕_S F_q(ν₁,…,ν_ℓ)` | the CRT decomposition |
| p.5 | Ex. 1: "there are **six** equivalence conjugacy classes" | the paper's own value of `N` |
| p.7 | "Since `A = Σ_S(e_S F_q)`, each `a` can be expressed as `a = Σ a_{S(ν)} e_{S(ν)}`, where **`a_{S(ν)} ∈ F_q`**" | **the claim under test** |
| p.7 | eq. (4): `C_{S(ν)} = {c_{S(ν)} ∈ F_q^n ∣ c ∈ C}` | projections declared to lie in `F_q^n` |
| p.7 | `⟨ρ,ρ′⟩_k = Σ_i ρ_i (ρ′_i)^{p^k}` | inner product (note: **`p^k`**, not `q^k`) |
| p.10 | Cor. 3.1: "…is a `k`-Galois self-dual code **over `F_q`**" | stated for the component |
| p.12 | Thm 8: "the **`q`-dimension** of the `k`-Galois hull"; eq. (8): `Σ_S{n − deg lcm(g_S,h_S^#)}` | the dimension formula |
| p.17 | eq. (10): `ψ(a) = (a_{S(ν₁)},…,a_{S(ν_N)})M`, `M ∈ GL_N(F_q)`, "where `\|Ŝ\| = N`" | the Gray map |
| p.17 | "the map `ψ` is **bijective linear isometry** from `A^n` to `F_q^{nN}`" | **the claim contradicted** |
| p.17 | Lemma 9: `ψ(hull_k(C)) = hull_k(ψ(C))` | rests on `ψ` being an isometry |
| p.18 | Thm 10: `[[nN, k − dim_q hull_k(C), d ; nN − k − dim_q hull_k(C)]]_q` | the quantum parameters |
| p.19 | "`N = 2`. Then, there are 2 idempotents…" | `N` is `\|Ŝ\|`, unambiguously |
| p.19 | factorisations of `x⁷−1`, `x⁷−ω²`; `g₁ = x³+ω³x²+ω⁵x+2`, `g₂ = x+ω²` | Example 2 data |
| p.20 | `dim₉(hull₁(C)) = 0`; "`ψ(C)` has the parameters `[14,10,4]₉`"; `[[14,10,4;4]]₉` | Example 2 output |
| p.20–21 | `x¹³−1`, `x¹³−ω⁸` factorisations; `g₁=(x+4)(x²+ωx+1)`, `g₂=x+ω²⁰` | Example 3 data |
| p.21 | `dim₂₅(hull₁(C)) = 2`; `[26,22,4]₂₅`; `[[26,20,4;2]]₂₅` | Example 3 output |
| p.21 | the `q = 4` ring `F₄[x₁,x₂]/⟨x₁²+x₁+ω, x₂²+ωx₂+ω⟩` | Table 1's first block |
| p.22 | Table 1, 13 rows | all displayed parameters |
| p.23 | "the enumeration of **non-isometric** constacyclic codes for a given Galois hull dimension … is still open over `A`" | the stated open problem |

---

## 2. Task 1 — cardinality, component fields, dimensions, Gray map

All numbers below are produced by `code/f11_source_audit.py`, a **new self-contained**
implementation (its own `GF(p^m)`, polynomial factoring, `A`-arithmetic, idempotent
search, rank, nullspace). It imports nothing from this project. Output:
`verification/f11_source_audit.out`.

### 2.1 The derivation, independent of any example

Let `A = F_q[X₁,X₂]/⟨t₁,t₂⟩` with `t₁,t₂` squarefree, and let the irreducible factors of
`t_i` have degrees `d_{i,1},…,d_{i,r_i}`.

**(D1) Component degrees.** Each maximal ideal `I_{S(ν)}` gives
`A/I_{S(ν)} ≅ F_q(ν₁,ν₂)`, of degree `lcm(d_{1,i}, d_{2,j})` over `F_q`. This is the
paper's own formula (p.4), used as given.

**(D2) The number of components.**
```
N = |Ŝ| = Σ_{i,j} gcd(d_{1,i}, d_{2,j}),
```
because the Frobenius orbits on the pairs `(ν₁,ν₂)` have size `lcm` and there are
`d_{1,i}d_{2,j}/lcm = gcd` of them per factor pair.

**(D3) The total dimension.** `dim_q A = Σ_S |S(ν)| = Σ_{i,j} d_{1,i}d_{2,j} = deg t₁ · deg t₂`,
the second form because `A` has the monomial basis `{X₁^a X₂^b}`.

**(D4) The contradiction.** The decomposition at p.7 writes `a = Σ_S a_S e_S` with
`a_S ∈ F_q`. That is a description of an `N`-dimensional `F_q`-space, since the `e_S` are
`N` commuting idempotents. So p.7 asserts `dim_q A = N`. By (D3), this holds **iff every
`|S(ν)| = 1`**, i.e. iff every `t_i` splits over `F_q`. When any `|S(ν)| > 1`:

```
|A| = q^{dim_q A}  >  q^{N} = |F_q^N|,
```

so `ψ : A → F_q^N` in eq. (10) **cannot be injective**, and p.17's "bijective linear
isometry" is impossible.

**(D5) The dimension transfer.** Since `C = ⊕_S C_S e_S` with `C_S ⊆ A_S^n`,

```
dim_q C = Σ_S |S(ν)| · dim_{A_S}(C_S)      and      dim_q hull_k(C) = Σ_S |S(ν)| · dim_{A_S} hull_k(C_S),
```

whereas Theorem 8 / eq. (8) computes `Σ_S dim_{A_S}(·)`, i.e. the same sum **with the
factor `|S(ν)|` omitted.** (For a field component, `dim_{A_S} hull = n − deg lcm(g_S,h_S^#)`,
so eq. (8) is exactly the unweighted sum.)

This is the whole finding. It is arithmetic, and it needs no interpretation of intent.

### 2.2 Example 1 (p.5)

`A₁ = F₂[x₁,x₂]/⟨t₁,t₂⟩`, `t₁ = x⁵+x⁴+1`, `t₂ = x⁴+x²+x`.

```
t₁ irreducible factor degrees : [2, 3]
t₂ irreducible factor degrees : [1, 3]
N  = Σ gcd(d,e)  = 1+1+1+3 = 6          (paper p.5: "six"  ✓)
dim_2 A = Σ d·e   = 2+6+3+9 = 20 = 5·4
class sizes |S(ν)| = [2,3,3,3,3,6],  sum = 20
|A| = 2^20 = 1048576     vs     |F_2^N| = 2^6 = 64
```

Two remarks.
* The paper's own count of **six** classes confirms `t₂` has factor degrees `{1,3}`, not
  the `{1,2}` implied by the printed parenthetical `t₂ = x₂(x₂²+x₂+1)` — that product is
  `x³+x²+x`, not `x⁴+x²+x`. The correct factorisation is `t₂ = x₂(x₂³+x₂+1)`. A slip,
  not a mathematical error, but it is the same locus.
* **Example 1 is not the split case either.** Class sizes are `2,3,3,3,3,6`. The
  hypothesis `a_S ∈ F_q` fails here too, in the very first example of the paper.

### 2.3 Example 2 (p.18–20)

`A = F₉[x₁,x₂]/⟨x₁²+x₁+ω, x₂²+ω⁵x₂+2⟩`, `F₉ = F₃(ω)`, `ω²+2ω+2 = 0`.

Both conjugate namings of `ω` (the two roots of `z²+2z+2` in `F₉`) were tested; both give
the same verdicts, so nothing below depends on which root is called `ω`.

```
t₁ irreducible over F_9 : True          t₂ irreducible over F_9 : True
dim_9 A = 2·2 = 4                       |A| = 9^4 = 6561
idempotents: 4;  primitive: 2  ⇒  N = 2   (brute force over all 6561 elements)
dim_9 of each component e_S A: [2, 2]   (direct rank) ⇒ A ≅ F_81 × F_81
|A| = 6561   vs   |F_9^N| = 9^2 = 81
```

The paper's own factorisations reproduce:

```
x^7 − 1   : degrees [1,3,3]
x^7 − ω^2 : degrees [1,3,3]
g₁ = x³+ω³x²+ω⁵x+2  divides x⁷−1  : True   (deg 3)
g₂ = x+ω²           divides x⁷−ω² : True   (deg 1)
```

Module computation. `C` is the `A`-submodule of `A⁷` generated by
`g = e₁g₁ + e₂g₂` with `λ = e₁ + ω²e₂`; equivalently the ideal `(g)` in
`A[x]/(x⁷−λ)`, spanned over `F₉` by `{b·x^i·g : b ∈ basis(A), 0 ≤ i < 7}` — 28 vectors in
`F₉^{28}`:

```
rank = 20  =  2·(7−3) + 2·(7−1) = 8 + 12
paper prints Σ_S (n − deg g_S) = 4 + 6 = 10
claimed Gray-image length nN = 7·2 = 14
20 > 14
```

**Two independent impossibilities for the printed `[14,10,4]₉`:**
(i) `dim_9 C = 20 ≠ 10`; (ii) even if the dimension were 10, `ψ` cannot be injective on
an `A`-space of `F₉`-dimension 20, and a code of length 14 cannot contain a 20-dimensional
subspace.

### 2.4 Example 3 (p.20–21)

`A = F₂₅[x₁,x₂]/⟨x₁²+x₁+ω¹³, x₂²+ω³x₂+1⟩`, `F₂₅ = F₅(ω)`, `ω²+4ω+2 = 0`.

```
t₁ irreducible: True ;  t₂ irreducible: False — it splits into two linear factors
factor degrees: t₁ [2], t₂ [1,1]
N = gcd(2,1)+gcd(2,1) = 2               dim_25 A = 2·1 + 2·1 = 4
primitive idempotents (brute force over 390625 elements): 2
dim_25 of each component: [2,2]         ⇒ A ≅ F_625 × F_625
|A| = 390625   vs   |F_25^N| = 625
```

```
x^13 − 1   : degrees [1,2,2,2,2,2,2]
x^13 − ω^8 : degrees [1,2,2,2,2,2,2]
g₁ = (x+4)(x²+ωx+1), deg 3, divides x¹³−1   : True
g₂ = x+ω²⁰,          deg 1, divides x¹³−ω⁸  : True
rank of the A-module ⟨g⟩ = 44  =  2·10 + 2·12
paper prints 22 ;  claimed length nN = 26 ;  44 > 26
```

Note that neither component of Example 3 is a copy of `F₂₅`: one is `F₆₂₅` (containing a
root of `t₁`), and the "split" factor `t₂` contributes a component of degree
`lcm(2,1) = 2` because the *other* variable still lives in a degree-2 extension.

### 2.5 The Gray map (p.17)

```
ring      dim_q A   N     |A|         |F_q^N|     can ψ be injective?
Ex 1      20        6     1048576     64          NO
Ex 2      4         2     6561        81          NO
Ex 3      4         2     390625      625         NO
```

`N` is pinned by the paper itself: p.17 says "`|Ŝ| = N`", and p.19 says "`N = 2`. Then
there are 2 idempotents". It is not `dim_q A`; had it been, Example 2's code would have
length 28, not 14.

### 2.6 Table 1 (p.22) — all 13 rows

The three rings used are: the `q = 4` ring of p.21
`A = F₄[x₁,x₂]/⟨x₁²+x₁+ω, x₂²+ωx₂+ω⟩`, Example 2's ring over `F₉`, and Example 3's
ring over `F₂₅`. **In all three, both defining polynomials are quadratic**, so
`dim_q A = ∏ deg t_i = 4` in every case; and since each `ν_i` is a root of a
quadratic, `F_q(ν₁,ν₂) ⊆ F_{q²}` and every component degree `|S(ν)| ≤ 2`.

`code/table1_forensics.py` computes the structures explicitly rather than assuming
them. All six polynomials are square-free, as the paper requires:

| `q` | `t₁`, `t₂` | splitting behaviour | `N = \|Ŝ\|` | `\|S(ν)\|` | `dim_q A = Σ\|S\|` |
|---|---|---|---|---|---|
| 4 | `x²+x+ω`, `x²+ωx+ω` | both irreducible over `F₄` | 2 | `[2,2]` | 4 |
| 9 | `x²+x+ω`, `x²+ω⁵x+2` | both irreducible over `F₉` | 2 | `[2,2]` | 4 |
| 25 | `x²+x+ω¹³`, `x²+ω³x+1` | `t₁` irreducible, `t₂` splits over `F₂₅` | 2 | `[2,2]` | 4 |

`t₂` in Example 3 splitting is **not** an error — the paper's hypothesis is
square-free, not irreducible. (An earlier note in this project called it a paper slip;
that note was wrong and is corrected here.)

**The dichotomy.** The printed length is `nN = 2n`, and eq. (10) gives
`ψ : A → F_q^N` with `N = |Ŝ|`, so the printed length asserts `N = 2`. Since
`4 = dim_q A = Σ_S |S(ν)|` over those two components and each term is at most 2, both
component degrees equal 2. Hence

> `dim_q C = Σ_S |S(ν)|·dim_{A_S}C_S = 2[(n − deg g₁) + (n − deg g₂)] = 2k_printed`,

so the printed dimension is short by a factor of two **in every row**. Equivalently,
and without needing to know whether any `t_i` splits: if some `t_i` is non-split then
`N = 2` and the length `2n` is right while `k` should be `2k`; if both split then
`N = 4` and `k` is right while the length should be `4n`. **There is no algebra in
Table 1 for which `[2n, k, d]` is correct.**

**Transcription, before any arithmetic.** Two independent checks:

* **Divisibility (C0 / PART 2b).** `g_S ∣ xⁿ − λ_S` in `F_q[x]` for both components,
  in **13/13** rows, under **all 8** admissible namings of `ω` — i.e. for each choice
  of `ω` as one of the two roots of its defining quadratic (`{2,3}`, `{3,7}`,
  `{5,21}`). That is the complete set, not a sample. `code/table1_forensics.py` reruns
  this check self-contained, without importing the other script.
* **Double transcription (PART 2).** Every printed tuple of every row — `g₁`, `g₂`,
  `[len,k,d]` and `[[n′,k′,d;c]]` — occurs verbatim in an independently copied raw
  text block: **13/13**.

| # | `q` | `n` | `deg g₁` | `deg g₂` | arithmetic | `k` printed | `2k` | printed length | verdict |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 4 | 5 | 2 | 2 | (5−2)+(5−2) = 6 | 6 | **12** | 10 | **impossible** |
| 2 | 9 | 4 | 2 | 2 | (4−2)+(4−2) = 4 | 4 | **8** | 8 | whole space ⇒ `d = 1` |
| 3 | 9 | 5 | 2 | 1 | (5−2)+(5−1) = 7 | 7 | **14** | 10 | **impossible** |
| 4 | 9 | 5 | 3 | 2 | (5−3)+(5−2) = 5 | 5 | **10** | 10 | whole space ⇒ `d = 1` |
| 5 | 9 | 5 | 4 | 3 | (5−4)+(5−3) = 3 | 3 | **6** | 10 | dimension feasible, `k` wrong |
| 6 | 9 | 6 | 4 | 1 | (6−4)+(6−1) = 7 | 7 | **14** | 12 | **impossible** |
| 7 | 9 | 7 | 3 | 1 | (7−3)+(7−1) = 10 | 10 | **20** | 14 | **impossible** |
| 8 | 9 | 7 | 4 | 3 | (7−4)+(7−3) = 7 | 7 | **14** | 14 | whole space ⇒ `d = 1` |
| 9 | 9 | 7 | 4 | 6 | (7−4)+(7−6) = 4 | 4 | **8** | 14 | dimension feasible, `k` wrong |
| 10 | 25 | 13 | 3 | 1 | (13−3)+(13−1) = 22 | 22 | **44** | 26 | **impossible** |
| 11 | 25 | 16 | 2 | 1 | (16−2)+(16−1) = 29 | 29 | **58** | 32 | **impossible** |
| 12 | 25 | 20 | 2 | 1 | (20−2)+(20−1) = 37 | 37 | **74** | 40 | **impossible** |
| 13 | 9 | 26 | 4 | 1 | (26−4)+(26−1) = 47 | 47 | **94** | 52 | **impossible** |

Four results:

1. **`k` is the unweighted sum in all 13 rows** (C2, 13/13): the defect found in
   Examples 2–3 is uniform across the whole table.
2. In **8 of 13 rows** (1, 3, 6, 7, 10, 11, 12, 13) the true dimension `2k` exceeds the
   printed length `2n`. These are not codes with a wrong distance; they are not codes
   at all — **invalid input parameters**.
3. In **3 rows** (2, 4, 8) `2k = 2n` exactly, so the image would be all of `F_q^{2n}`
   and `d = 1`, contradicting the printed `d ∈ {4,4,6}`. Here the dimension is
   realisable and the **distance claim** is false — a different failure, reported
   separately.
4. Only rows **5 and 9** escape both failures, and even there the printed `k` is half
   the true dimension.

**The exhaustive dilemma.** Either `ψ` is injective, in which case `dim ψ(C) = 2k ≠ k`
and the printed parameters are false; or `ψ` is not injective, in which case the proof
of Lemma 9(2) fails — it reads, verbatim, "Since ψ is an injective map, we have
c = c′" — and Theorem 10's application collapses with it. The paper cannot have both.

**EAQECC arithmetic, checked separately.** Given only the printed `k` and `k′`, the
relation `h = k − k′` and `c = 2n − k − h` reproduce the printed `c` in **13/13** rows
(`h = 4,0,2,4,2,2,0,0,0,2,2,2,3`); the "Diff" column is reproduced in **13/13**; and
the `*`/`†` decoration matches `Diff ∈ {0,2}` in **13/13**. The arithmetic is sound and
the inputs are wrong: Theorem 10 is applied to `D = ψ(C)` with `dim D = k` when
`dim D = 2k`.

*Observation, reading-dependent:* Lemma 8 is quoted as requiring `d ≤ (n+2)/2`; the
extracted text reads "d ≤ n+22", only sensible as `(n+2)/2`. Rows **5 and 9** violate
that hypothesis, so their "Diff" entry compares quantities outside the lemma's domain.
This affects nothing above.

**Scope note.** Dimensional and arithmetic audit only. The printed minimum distances
were **not** verified, corrected distances were **not** computed, and no corrected
parameter set is asserted (§4.3).

---

## 3. Task 2 — independent verification of the `F_9` isometry witness

**What is verified.** Over `F₉ = F₃[z]/(z²+2z+2)` (element `a₀+a₁z` stored as `a₀+3a₁`),
let `R_a = F₉[x]/(x⁵−a)` and consider the monomial map `f(x) ↦ f(x²)` with scalings
`a_i = b^{⌊2i/5⌋}`, which sends `R_a → R_b` **iff `a = b²`** (the defining relation
`x⁵ − a` maps to `b² − a`, which must vanish).

With `ω = 3` (one of the two roots of `z²+2z+2`), take `b = ω`, `a = ω² = 4`:

| | source | image |
|---|---|---|
| ring | `F₉[x]/(x⁵ − 4)` | `F₉[x]/(x⁵ − 3)` |
| shift | `λ = ω²` | `λ = ω` |
| generator | `g = 2 + 6x + x²` | `ψ₂(g)` |
| divides `x⁵ − λ` | True | True |
| **constacyclic** | **True** | **True** |
| `dim_F9` | 3 | 3 |
| weight distribution | — | **identical** |
| **`dim hull₁` (Hermitian)** | **2** (`\|hull\| = 81 = 9²`) | **0** (`\|hull\| = 1`) |

The Hermitian form is `⟨u,v⟩₁ = Σ u_i v_i^{p}` with `p = 3` (paper p.7), the dual is
computed by solving the linear system `Σ v_i c_i³ = 0` over all basis vectors `c` of the
code, and the hull is obtained as an explicit **set** — all 81 elements of the dual are
enumerated and filtered by membership in `C`, so `|hull| = 81` and `= 1` are literal
counts, not ranks.

**Consistency with the criterion.** The scalings are `(1,1,1,ω,ω)`; their norms
`a_i^{1+3} = a_i⁴` are `(1,1,1,2,2)`, non-constant, so the map is a Hamming isometry but
not a similarity of the Hermitian form — which is exactly the precondition for the hull to
move.

**A naming caveat, recorded honestly.** Under the *other* naming of `ω` (the conjugate
root, code 7), the printed `g = 2+6x+x²` does **not** divide `x⁵−ω²`, and the two codes
are not constacyclic for those shift constants. The hull still changes `2 → 0` for that
conjugate instance, but it is not a witness inside the constacyclic family. **The valid
witness is the one with `ω = 3`.** This is a labelling dependence of the printed
coefficients, not a defect in the phenomenon.

**Independence.** `code/f11_source_audit.py` rebuilds the field, both rings, both codes,
the Hermitian dual and the hull from scratch, and does not read any earlier output. It
reproduces the numbers reported in the previous turn's `code/final_check_A.py` (a different
implementation with different internal conventions), which is the point of running it.

---

## 4. Task 3 — three-way separation

### 4.1 (a) Proved, about **arXiv:2412.08512v1**

| # | Statement | Grounds |
|---|---|---|
| a1 | Every component `A_S` is a field of degree `|S(ν)| = lcm(d_i)` over `F_q`; `A ≅ F₈₁×F₈₁` (Ex. 2), `F₆₂₅×F₆₂₅` (Ex. 3) | p.4 + direct rank computation of `e_S A` |
| a2 | `dim_q A = Σ_S|S(ν)| = ∏ deg t_i`; equals 20 (Ex. 1), 4 (Ex. 2), 4 (Ex. 3) | CRT + monomial basis; brute-force idempotents for Ex. 2, 3 |
| a3 | p.7's `a_S ∈ F_q` is equivalent to asserting `dim_q A = N`, which is false in all three examples | a1, a2 |
| a4 | `ψ : A → F_q^N` (eq. 10) is not injective; the "bijective linear isometry" of p.17 does not exist for these rings | `|A| = q^{dim A} > q^N` |
| a5 | Ex. 2: `dim₉ C = 20`, not 10; `20 > 14 = nN`, so `[14,10,4]₉` cannot be the Gray image of `C` | module rank over `F₉` |
| a6 | Ex. 3: `dim₂₅ C = 44`, not 22; `44 > 26 = nN`, so `[26,22,4]₂₅` cannot be | module rank over `F₂₅` |
| a7 | Theorem 8's formula is correct as `Σ_S dim_{A_S} hull_k(C_S)` and equals the `q`-dimension only when all `|S(ν)| = 1` | D5 |
| a8 | All 13 rows of Table 1 have length `2n` while `dim_q A = 4` for every ring used | p.21–22 |
| a8b | Every printed `k` in Table 1 is the **unweighted** `Σ_S(n − deg g_S)`, with no factor `|S(ν)| = 2` | transcription validated (C0), then summed (C2): 13/13 |
| a8c | In 8 of 13 rows the true dimension `2k` exceeds the printed length `2n`; in 3 more `2k = 2n`, forcing `d = 1` | a8b + C5; rows 1,3,6,7,10,11,12,13 and 2,4,8 |
| a8d | **The printed length and the printed dimension are mutually inconsistent in all 13 rows.** `dim_q A = 4` (both `t_i` quadratic) and `|S(ν)| ≤ 2`, so a printed length `2n` forces `N = 2`, hence both `|S(ν)| = 2`, hence `dim_q C = 2k ≠ k` | a2 + p.4 + eq. (10); `code/table1_forensics.py` PART 4 |
| a8e | The three Table 1 rings have `N = 2`, `|S(ν)| = [2,2]`, `dim_q A = 4`, and all six defining polynomials are square-free | computed from the roots in `F_{q²}` and the Galois orbits; PART 1 |
| a8f | Either `ψ` is injective and the printed parameters are false, or `ψ` is not injective and the proof of Lemma 9(2) fails. Both cannot hold | injectivity is used verbatim in that proof (p.18) |
| a9 | The arithmetic of Theorem 10 applied to the paper's own inputs is self-consistent (`14−10−0 = 4`, `26−22−2 = 2`; all 13 table rows consistent) | p.18, p.20, p.21; C6, C7 |
| a10 | `dim hull₁` is **not** an isometry invariant of constacyclic codes; a `F₉` witness gives `2 → 0` | §3 |

Items a1–a9 are about the source paper. a10 is about the paper's *stated open problem*
(p.23), not about F11 itself, and is listed separately for that reason.

### 4.2 (b) **Not** established — about the published version of record

**Status: the source-level check is BLOCKED; the framing was inspected.**

On 2026-10-20 the publisher's public "Article preview" was read
(`sciencedirect.com/science/article/abs/pii/S0012365X25003589`): the **complete
abstract**, the **complete introduction**, the **section snippets**, and the
**references list**. The **body of the paper was not accessible** (no institutional
access; `Access through your organization` / `Purchase PDF`). A verbatim record is in
`verification/VOR_INSPECTION_2026-10-20.md`.

#### 4.2.1 What the partial inspection establishes

| # | Finding | Bearing on F11 |
|---|---|---|
| V1 | The published version is **materially different from v1**: Crossref lists **45** references (v1: 44); the introduction cites **"Example 2, Example 4, and Table 2"**, and Example 4 / Table 2 **do not exist in v1**. | Extrapolating any v1 defect to the published text is **unsafe**. No such extrapolation is made. |
| V2 | Theorem numbering has shifted: published **Theorem 4** is v1 **Theorem 2**; published **Lemma 7** is v1 **Lemma 8**. | Cross-references from v1 do not transfer; a note must cite the published numbering. |
| V3 | The phrase **"`q`-dimensions"** is retained in the published introduction ("a formula for the **q**-dimensions of the `k`-Galois hulls") **and** in the §3 snippet ("a formula for the **q-dimension** of the `k`-Galois hull"). This is the exact term implicated in F11. | **Raises the prior** that the affected passages were not rewritten. **Does not establish it.** |
| V4 | The published version adds a counting result absent from v1: the **cardinality of the set of `q`-dimensions** `𝒟_k(n,q,λ)`. | This is *not* code enumeration and *not* enumeration up to isometry, but it is closer to that territory than anything in v1. Any future novelty claim about counting constacyclic hull dimensions must reckon with it. |
| V5 | The published introduction states, of the 2023 local result `[11]`: "**They also counted the number of constacyclic codes of a given Galois hull dimension.**" | The authors' own confirmation that the field-level enumerator exists — consistent with `[D23]` in this project's literature review. |
| V6 | The published article is **not open access**: Crossref lists only Elsevier TDM licences; OpenAlex gives `primary_location.is_oa = false`, `license = null`, `version = publishedVersion` | There is no legal free copy of the published text to read. |
| V7 | The only green OA copy is **arXiv v1** (`oa_status: green`, `oa_url = arxiv.org/pdf/2412.08512`); the arXiv submission history shows `[v1] 11 Dec 2024` and **no v2** | The free copy is *not* the version of record and cannot be used as a proxy for it. |
| V8 | A direct request to `/science/article/pii/S0012365X25003589` **redirects to the `/abs/pii/` preview**; the page offers only `Access through your organization` and `Purchase PDF` | Access is genuinely gated, not merely awkward to navigate. |
| V9 | The published `§2` "Preliminaries" snippet is the **first paragraph only** (on constacyclic codes over a field) and stops **before** the primitive-idempotent decomposition | The snippet does not reach the decisive passage, so it decides nothing. |

#### 4.2.2 What remains unknown — and is marked BLOCKED

Six legitimate routes to the full text are listed in
`verification/VOR_INSPECTION_2026-10-20.md` §5.6. None was available here; none is
asserted to be available.

| # | Question | Status |
|---|---|---|
| b1 | Does the published body still assert `a_{S(ν)} ∈ F_q`? | **BLOCKED — not seen** |
| b2 | Does the published Gray map still set `N = \|Ŝ\|` with `M ∈ GL_N(F_q)`? | **BLOCKED — not seen** |
| b3 | Do the published Examples 2–4 and Tables 1–2 still print lengths `2n`? | **BLOCKED — not seen** |
| b4 | Are the published quantum parameters still `[[14,10,4;4]]₉`, `[[26,20,4;2]]₂₅`? | **BLOCKED — not seen** |
| b5 | Does the published Theorem 4 print the same hull-dimension formula? | **BLOCKED — not seen** |
| b6 | Does the conclusion retain "the enumeration of non-isometric … is still open over 𝒜"? | **BLOCKED** — the snippet stops at "Hulls of different families of linear codes have yet to be" |
| b7 | Does the new cardinality `\|𝒟_k(n,q,λ)\|` result inherit the component-bookkeeping issue? | **BLOCKED** — guessing would be speculation |

**Therefore:** it is not inferred, and must not be assumed, that the version of record
contains the same defect. The correct statement is: *proved for v1; the framing survives
into the published version; the body is unread.*

### 4.3 (c) Consequences that **cannot yet be asserted**

| # | Cannot be asserted | Why not |
|---|---|---|
| c1 | **Corrected quantum-code parameters.** The tempting values `[[28,20,d;8]]₉` and `[[52,40,d;4]]₂₅` follow mechanically from `n·dim_q A`, `dim_q C` and the corrected hull dimension — **but they are not established.** | (i) the minimum distance `d` of the true Gray image has not been computed; (ii) more seriously, Theorem 10 rests on Lemma 9, `ψ(hull_k C) = hull_k(ψ C)`, whose proof uses that `ψ` is an *isometry*; any repaired map (`ψ : A → F_q^{n·dim_q A}` via `F_q`-bases) is only `F_q`-linear, so the orthogonality transfer is not available without a new argument |
| c2 | The corrected hull dimension for Example 3 (`4` rather than `2`) | follows from the same factor `|S| = 2` applied to the component hulls `(2, 0)` computed in `code/final_check_B.py`, but the paper's own `dim₂₅ hull₁ = 2` is *internally* correct as an `A_S`-dimension; presenting `4` as "the" value presupposes the repair choice |
| c3 | That the authors "meant" `a_S ∈ A_S` | that would be a natural repair, but it is not what is written, and intent is not evidence |
| c4 | That the defect invalidates the paper's other theorems | Theorems 2–7 are statements about the decomposition and are correct for `A_S` of any degree; only the `q`-dimension labelling and everything downstream of the Gray map are affected |
| c5 | Any priority or novelty claim | this is a correction of a published statement; the component-field distinction is elementary and very likely familiar to specialists |
| c6 | The corrected parameters of the 13 Table 1 rows | §2.6 establishes only that the printed `k` omits the factor `2` and that 11 of 13 rows then contradict the printed length; the printed distances were **not** verified and corrected distances were **not** computed |
| c7 | Whether the published version's new result on `\|𝒟_k(n,q,λ)\|` is affected | the statement and its proof are inside the paywalled body; nothing was read of it (§4.2.2, b7) |

---

## 5. Evidence table

Every row names the script that produces the number.
`SA` = `code/f11_source_audit.py`; `TA` = `code/table1_audit.py`;
`FB` = `code/final_check_B.py`; `FA` = `code/final_check_A.py`.
Outputs: `verification/{f11_source_audit,table1_audit,final_check_B,final_check_A}.out`.

| # | Claim | Page / eq. | Calculation | Result | Limitation |
|---|---|---|---|---|---|
| 1 | `|S(ν)| = lcm(d_i)` and equals the component degree | p.4 | SA §3, §4: rank of `e_S·A` for each primitive idempotent | `[2,2]` in Ex. 2; `[2,2]` in Ex. 3 | Ex. 1 not computed directly (dim 20 too large for brute force) |
| 2 | `A ≅ ⊕_S F_{q^{|S|}}` | p.5 | SA §3, §4 | `F₈₁×F₈₁`; `F₆₂₅×F₆₂₅` | — |
| 3 | `a_S ∈ F_q` forces `dim_q A = N` | p.7 | SA §2–4 | false in all three examples | — |
| 4 | `|A| = q^{dim_q A}` vs `|F_q^N|` | p.17 | SA §5 | 6561 vs 81; 390625 vs 625; 2²⁰ vs 2⁶ | — |
| 5 | `ψ` cannot be a bijection | p.17, eq. (10) | SA §5 (pigeonhole) | not injective in any example | — |
| 6 | Ex. 1 is not the split case | p.5 | SA §2 | `N=6`, `dim=20`, sizes `[2,3,3,3,3,6]` | corroborated by the paper's own "six" |
| 7 | Ex. 2 code dimension is 20, not 10 | p.20 | SA §3: rank of 28 generators over `F₉` | **20** | — |
| 8 | Ex. 2 `[14,10,4]₉` impossible | p.20 | SA §3 | `20 > 14 = nN` | distance itself not checked |
| 9 | Ex. 3 code dimension is 44, not 22 | p.21 | SA §4: rank of 52 generators over `F₂₅` | **44** | — |
| 10 | Ex. 3 `[26,22,4]₂₅` impossible | p.21 | SA §4 | `44 > 26 = nN` | distance itself not checked |
| 11 | Thm 10 arithmetic is self-consistent on the printed inputs | p.18, 20, 21 | SA §3, §4 (hand check) | `14−10−0=4`; `26−22−2=2` | does not validate the inputs |
| 12 | All Table 1 rows have length `2n` | p.22 | SA §7 | 13/13 rows | only lengths |
| 12b | Table 1 transcription is correct (divisibility) | p.22 | TA C0; **TF PART 2b (self-contained)** | `g_S ∣ xⁿ−λ_S` in **13/13** rows under **all 8** admissible namings of `ω` (the complete set) | — |
| 12b* | Table 1 transcription is correct (second copy of the page) | p.22 | TF PART 2 | all four printed tuples of every row occur verbatim in an independently copied raw block: **13/13** | catches a single-transcription slip only |
| 12c | Every printed `k` is the **unweighted** `Σ(n−deg g_S)` | p.22 | TA check C2 | **13/13 rows** | — |
| 12d | True dimension `2k` exceeds printed length `2n` | p.22 | TA check C5 | **8/13 rows impossible**; 3 degenerate (`d=1`); 2 escape | distances not checked |
| 12e | EAQECC arithmetic is internally consistent | p.22 | TA C6, C7; TF C6–C8 | **13/13 rows**, implied `h = 4,0,2,4,2,2,0,0,0,2,2,2,3`; "Diff" and the `*`/`†` decoration also 13/13 | input values not validated by this |
| 12f | `d` and `n′` agree between the two printed columns | p.22 | TF C9, C10 | **13/13** | — |
| 12g | **Length and dimension are jointly inconsistent in every row** | p.22 + p.4 + eq. (10) | TF PART 4 (derivation) | `2n ⇒ N=2 ⇒ \|S\|=2 ⇒ dim = 2k ≠ k`; **13/13 rows** | uses only `dim_q A = 4` and `\|S\| ≤ 2` |
| 12h | The three Table 1 rings have `N=2`, `\|S\|=[2,2]`, `dim 4`, all square-free | p.18–21 | TF PART 1 (roots in `F_{q²}`, Galois orbits) | matches the paper's own `N = 2` statements | — |
| 13 | `dim_q A = 4` for the `q=4` ring too | p.21 | SA §7 | both quadratics irreducible | — |
| 14 | Component hull dims in Ex. 3 are `(2,0)` | p.21 | FB (component-field embedding) | `2·2 + 2·0 = 4` weighted | depends on repair choice (§4.3 c2) |
| 15 | `F₉` witness: Hermitian hull `2 → 0` | — (about p.23's open problem) | SA §6, FA | `\|hull\| = 81 → 1`, both constacyclic, equal weight distributions | naming-dependent; valid under `ω=3` |
| 16 | Published version ≠ v1 | VoR | Crossref (45 refs) + publisher intro (Example 4, Table 2) | **materially different** | body not read |
| 17 | "`q`-dimension" still used in published intro and §3 snippet | VoR | publisher preview, quoted in `verification/VOR_INSPECTION_2026-10-20.md` | **retained** | does not establish the body text |
| 18 | Published version adds a counting result `\|𝒟_k(n,q,λ)\|` | VoR | publisher intro | **present** | content and correctness unknown |
| 19 | Whether the published body retains the defect | VoR | — | **BLOCKED** | paywall |
| 20 | Published article is not open access | VoR | Crossref licences; OpenAlex `primary_location` | `is_oa: false`, `license: null`, `version: publishedVersion` | — |
| 21 | The green OA copy is v1, not the published version | arXiv | submission history | `[v1] 11 Dec 2024`; **no v2** | — |
| 22 | `/pii/` and `/abs/pii/` both give the preview page only | VoR | direct request | redirect to `/abs/pii/`; `Purchase PDF` offered | — |
| 23 | The published §2 snippet stops before the decisive passage | VoR | publisher preview | first paragraph only (constacyclic codes over a field) | does not reach the CRT step |

**Legend.** `SA` = `code/f11_source_audit.py`; `FB` = `code/final_check_B.py`;
`FA` = `code/final_check_A.py`; `TA` = `code/table1_audit.py`;
`TF` = `code/table1_forensics.py` (self-contained); `VoR` = version of record,
inspector record in `verification/VOR_INSPECTION_2026-10-20.md`.

---

## 6. Reproducibility and non-actions

**New this turn**

| File | Contents |
|---|---|
| `FINAL_F11_EVIDENCE_DOSSIER.md` | this document |
| `code/f11_source_audit.py` | self-contained re-implementation (no project imports) |
| `verification/f11_source_audit.out` | its full output, exit 0 |
| `code/table1_audit.py` | all 13 rows of Table 1: transcription check, dimensions, EAQECC arithmetic |
| `verification/table1_audit.out` | its full output, exit 0 |
| `code/table1_forensics.py` | **self-contained** re-audit: builds the three fields and their quadratic extensions, finds roots, counts Galois orbits, runs C0–C10 |
| `verification/table1_forensics.out` | its full output, exit 0 |
| `verification/VOR_INSPECTION_2026-10-20.md` | verbatim record of what of the published version was and was not seen, plus the access re-verification and the six legitimate routes to the full text |
| `FINAL_GO_NO_GO_DECISION.md` | the decision document: verified facts about v1 and the VoR, BLOCKED items, the 13-row audit, the scope of any correction, and the decision rule |
| `FINAL_F11_EVIDENCE_DOSSIER.zip` | report + scripts + outputs + `MANIFEST.txt` |

**Preserved, unmodified this turn:** `code/gf.py`, `code/final_check_A.py`,
`code/final_check_B.py`, `code/independent_verification.py`,
`code/isometry_hull_screening.py`, `code/verify_*.py`, and every `.out` log and every
report from previous turns.

**Non-actions:** no correction note; no manuscript; no git commit or push; the source PDF
was not modified (hash re-verified at the start and end of this turn).

**Four coding/transcription errors were made and caught, before any output was recorded.**

1. *Factorisation.* The first version of the routine confused remainder with quotient
   (`pmod` returns the remainder) and reported one irreducible factor per polynomial,
   which would have produced wrong class data for Examples 1 and 3. Caught by inspecting a
   failing intermediate result; fixed with an explicit `pquo`; the audit re-run from
   scratch.
2. *Table 1 coefficients.* Symbolic entries (`ω⁵`) were first written as bare integers
   (`5`). This is what the transcription check C0 exists to catch.
3. *Table 1 `λ`.* A single `λ` was first used for both components, whereas `g_S` divides
   `xⁿ − λ_S` with its **own** `λ_S`. With this error 8 of 13 rows appeared to fail; with
   the correct per-component `λ`, **13/13 pass** under every conjugate naming.
4. *Row 1's `λ`, in `code/table1_forensics.py`.* The λ-cell reads `ω e₁ + e₂`, but the PDF
   text layer renders it `w^e1 +e2` — because `^I` is part of the UTF-8 encoding of ω
   itself (bytes `CF 89`), not a caret. Read hastily it looks like `ω^{e₁+e₂}`, and it
   was first transcribed that way, making row 1 fail. The divisibility test settled it:
   of the nine assignments in `(F₄*)²`, **only** `(λ₁,λ₂) = (ω,1)` makes both `g_S`
   divide `xⁿ − λ_S`. This is precisely the class of error the check exists to catch.

The lesson is recorded because it is the reason check C0 exists: had the table simply
been transcribed and its dimensions summed, the two coefficient/labelling errors would
have been invisible and the row-level result would have rested on unverified input.

---

## 7. Go / no-go recommendation

### Recommendation: **BLOCKED** — with a one-sentence decision rule.

The full reasoning, the branch table and the scope of any correction are in
**`FINAL_GO_NO_GO_DECISION.md`**. The short form:

* **Not GO.** GO means "write the correction", and the correction would be against the
  *published* article, whose `§2` body has not been read. Two standing rules forbid
  exactly that: do not infer the version of record's content, and do not draft a
  correction note.
* **Not NO-GO.** NO-GO would assert the published version is clean. Nothing supports
  that: it differs materially from v1, it retains the "`q`-dimension" framing in the
  introduction and in the `§3` snippet, and it adds a counting result in the same
  territory.
* **BLOCKED** is therefore the honest state. It is a statement about **access, not
  about the mathematics**. §1 and §2 of this dossier are complete for v1 and need no
  revision whatever the answer turns out to be.

**The decision rule.** One sentence in the published `§2` decides it. In v1 it is on
p.7:

> "Every a ∈ A can be expressed as a = Σ_{S(ν)∈Ŝ} a_{S(ν)} e_{S(ν)}, where
> **a_{S(ν)} ∈ F_q for all S(ν) ∈ Ŝ**."

| Finding at the corresponding place in the published `§2` | Decision |
|---|---|
| still `a_{S(ν)} ∈ F_q` | **GO** — a correction note is warranted, scoped by the decision document §5 |
| changed to `∈ A_{S(ν)}` or `∈ F_{q^{\|S(ν)\|}}` | **NO-GO, permanently** — v1-only defect; record the negative result |

Two confirmation checks in the same sitting: published eq. (10) (still `N = |Ŝ|`, still
"bijective linear isometry"?), and published Tables 1–2 with the new Example 4 (still
length `2n` with the unweighted `k`?).

**If the answer is GO,** the note must claim only the missing factor `|S(ν)|` and its
listed consequences; cite the **published** numbering (Theorem 4, Lemma 7); acknowledge
the new `|𝒟_k(n,q,λ)|` result and say plainly that its status could not be determined;
and make **no** novelty claim.

**In no branch** should the abandoned Phase-5 manuscript be revived.

## 8. One-paragraph summary for a reader who reads nothing else

The source paper's affine algebra `A` has components that are extension fields
`F_{q^{|S(ν)|}}`, but its §2 writes every element with coefficients in `F_q`, which is
only valid when every defining polynomial splits. It never does in this paper: the component
degrees are 2–6 in Example 1 and 2 in Examples 2–3, so `dim_q A = 20, 4, 4` while the
paper's Gray map has codomain `F_q`-dimension `N = 6, 2, 2`. The map it calls a
"bijective linear isometry" therefore cannot be injective, and the code dimensions it
prints are the sums of *component* dimensions with the factor `|S(ν)|` omitted. This
holds for all 13 rows of its Table 1 — indeed in every row the printed length and the
printed dimension cannot both be right: 8 rows are impossible as printed and 3 more would
force minimum distance 1. The paper's *arithmetic* is internally consistent throughout —
the defect is a single missing factor, not a computational error. All of this is proved
for arXiv v1; the published version differs materially from v1, retains the "`q`-dimension"
framing, and its body has not been read, so the published status is **BLOCKED**.

---

## 9. Third pass (2026-10-20, later the same day)

A further, dedicated attempt was made to read the published `§2`, and both scripts were
re-run in a clean room. Full record: **`FINAL_F11_VERIFICATION_LOG.md`**.

**Access.** Seven legitimate routes were tried and all are closed: the publisher's
full-text URL redirects to the preview; the preview offers only "Access through your
organization" and "Purchase PDF" and carries the notice "© 2025 Elsevier B.V. All
rights reserved, including those for text and data mining, AI training, and similar
technologies"; Crossref lists Elsevier TDM licences only, with no Creative Commons
licence; OpenAlex reports `primary_location.is_oa = false`, `license = null`,
`version = publishedVersion` and green OA pointing at `arxiv.org/pdf/2412.08512`;
arXiv has `[v1]` only, with no v2; `uvadoc.uva.es` holds no deposit; ResearchGate hosts
the **Preprint, Dec 2024** (i.e. v1). Shadow libraries and third-party summaries were
not used.

**A sharper formulation of the finding.** The three loci L1 (p.4), L3 (p.5) and L5 (p.7)
in `verification/VERBATIM_LOCI_v1.md` contradict one another **with no computation
required**: p.4 says `|S(ν)| = lcm(d_i) = [F_q(ν_1,…,ν_ℓ):F_q]`; p.5 says
`e_{S(ν)}R ≅ F_q(ν_1,…,ν_ℓ)`, a field of that degree; p.7 says `A = Σ(e_{S(ν)}F_q)` with
`a_{S(ν)} ∈ F_q`, a copy of `F_q`. The first two give `dim_q A = Σ_S|S(ν)|`; the third
gives `dim_q A = N`. For Example 2 the paper itself states "N = 2" (p.19) with two
quadratic `t_i`, so `|S(ν)| = 2` and the two readings give 4 and 2. **The contradiction
is internal to the paper.** §1–§3 of this dossier quantify its consequences; they do
not create it.

**Clean room.** Both scripts re-run from a pristine unzip, nothing else in the
directory, 16/16 manifest members verified before running:

| Test | Result |
|---|---|
| `code/table1_audit.py` | exit 0; C0 13/13 naming-free, C2 13/13, C3 13/13, C6 13/13, C7 13/13; C5 violated in `[1,3,6,7,10,11,12,13]`, degenerate in `[2,4,8]` |
| `code/table1_forensics.py` | exit 0; PART 1 all three rings `N=2, \|S\|=[2,2], dim 4, CONSISTENT`; PART 2 13/13; PART 2b 13/13 in all 8 namings; C2–C10 all 13/13 |
| each output vs its archived `.out` | **IDENTICAL** (timestamp and output-path lines excluded) |
| the two scripts against each other | row sets `[1,3,6,7,10,11,12,13]` and `[2,4,8]` **agree**; C2, C3, C6, C7 all 13/13 in both |

Console transcript: `verification/cleanroom_run_2026-10-20.log`. The two scripts share
no code, so their agreement is an independent cross-check.

**Decision.** Unchanged: **BLOCKED**, in favour of neither GO nor NO-GO. The missing
evidence is named one item at a time in `FINAL_F11_VERIFICATION_LOG.md` §1.1, and six
legitimate routes to it are listed in §1.2.
