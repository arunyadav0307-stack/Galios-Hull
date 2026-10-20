# NOVELTY_ASSESSMENT

Classification vocabulary required by the blueprint (§2B):
**N1** apparently new with documented comparison · **N2** potentially new, needs
further checking · **K** known or routine · **F** false under the proposed
assumptions · **U** unresolved.

Every classification below states its *evidence*. No classification rests on the
absence of a statement from `[S1]`.

---

## 1. The object under assessment

The blueprint (Phase 3) proposes, for `A = F_q[X_1,…,X_ℓ]/⟨t_1,…,t_ℓ⟩` with the
`t_i` square-free, and for the components `S ∈ Ŝ`:

```
H_S(z)      = Σ_{C_S} z^{h_S(C_S)}                       (local / constituent)
H_joint(z⃗)  = Σ_{C}    ∏_S z_S^{h_S(C_S)}                (joint)
H_total(z)  = H_joint(z,…,z) = Σ_j N_j z^j               (total)
```
with `h_S(C_S) = dim Hull_H(C_S)`.

Establishing novelty requires that at least one of these be a theorem that is not
already available. Two facts decide the question: a **structural identity**
(§2), and a **literature comparison** (§3).

---

## 2. Structural identity: `H_joint` is a product, and the product is forced

### Proposition J
Let `A = ⊕_{S∈Ŝ} A_S` be the CRT decomposition, `A_S = F_q(ν_1,…,ν_ℓ)` a field of
degree `d_S = |S(ν)|` over `F_q`. Fix a unit `λ = Σ_S λ_S e_S` and `0 ≤ k < e`.
Then:

**(i) Bijection.** The map `C ↦ (C_S)_{S∈Ŝ}` is a bijection
```
{ λ-constacyclic codes over A of length n }  ⟶  ∏_{S∈Ŝ} { λ_S-constacyclic codes over A_S of length n }.
```
**(ii) Additivity.** `hull_k(C) = ⊕_S hull_k(C_S)`, hence
`dim_{A} hull_k(C) = Σ_S dim_{A_S} hull_k(C_S)`, and
`dim_q hull_k(C) = Σ_S d_S · dim_{A_S} hull_k(C_S)`.
**(iii) Factorisation.** With `h_S := dim_{A_S} hull_k(C_S)`,
```
H_joint(z⃗) = ∏_{S∈Ŝ} H_S(z_S) ,      H_total(z) = ∏_{S∈Ŝ} H_S(z) .
```
With the `F_q`-dimension convention `h_S^{q} := d_S · dim_{A_S}` one gets the same
statement with `z_S` replaced by `z_S^{d_S}`.

### Proof
(i) is `[S1, Thm 2 + Thm 3]`: `C` is `λ`-constacyclic iff every `C_S` is
`λ_S`-constacyclic, and `C = ⊕ C_S e_S`. Injectivity: if `C ≠ C'` then for some
`S`, `C_S ≠ C'_S`. Surjectivity: given any tuple `(C_S)`, the sum
`⊕_S C_S e_S` is a `λ`-constacyclic code whose components are the given `C_S`.
Distinct monic divisors of `x^n − λ_S` give distinct ideals, and every
`λ_S`-constacyclic code over a field has a unique monic generator polynomial, so
counting ideals = counting divisors.

(ii) is `[S1, Thm 7]`: `hull_k(C) = ⊕_S hull_k(C_S)` as a direct sum of
`A_S`-modules, and dimensions add. The factor `d_S` appears because `A_S` is a
`d_S`-dimensional `F_q`-space.

(iii) A product bijection with an additive statistic has a multiplicative
generating function:
```
Σ_{(C_S)} ∏_S z_S^{Σ_T h_T(C_T)}
   = Σ_{(C_S)} ∏_S ∏_T z_T^{h_T(C_T)}
   = ∏_S ( Σ_{C_S} z_S^{h_S(C_S)} ) .
```
∎

**Status of Proposition J:** `[PROVED]` here from `[S1]` Theorems 2, 3, 7;
independently `[VERIFIED]` numerically (`verification/verify_corollary_3_5.out`,
Test 3: local `{0:2,1:2,2:1}` convolved gives exactly the direct histogram over
`A`, `25 = 5×5` codes).

### What Proposition J implies for novelty

`H_joint` carries **exactly the information of the tuple `(H_S)`**, and no more.
It is a bookkeeping device. Therefore:

> **The novelty of `H_joint` equals the novelty of the local `H_S`, and nothing else.**

Any claim that "the *joint* enumerator is new" is, after Proposition J, a claim
that the *local* enumerator is new. That reduces the question to a finite-field
question, which is settled in §3.

**And `H_S` is a known object.** For `A_S = F_q` it is precisely the enumeration
of `λ_S`-constacyclic codes over a finite field by `k`-Galois hull dimension —
the theorem `[D23]` states and proves (subject to restrictions on `q`). For
`A_S = F_{q^{d_S}}` the same method applies with `q` replaced by `q^{d_S}`, and
the special cases `k = 0` and Hermitian are `[SJL15]`.

---

## 3. Literature comparison, item by item

| Candidate contribution | Closest known result | Evidence class | Classification |
|---|---|---|---|
| **Local enumerator `H_S(z)` over `F_q`** | `[D23]` — "the number of constacyclic codes of length `n` over `F_q` is calculated for a given Galois hull dimension", plus exact counts of Galois self-orthogonal/self-dual codes; `[SJL15]` for cyclic/negacyclic Euclidean and Hermitian | publisher abstract of `[D23]`; `[SJL15]` abstract | **K** (restricted `q`); residual **U** only for unrestricted `q` |
| **Joint enumerator `H_joint`** | Proposition J + `[D23]`; and `[S25]` (same construction over `Z_pZ_p[v]`, with an explicit enumeration theorem) | `[S1]` Thm 2/3/7; `[S25]` abstract and Thm 3.5/3.7/Cor 3.8; our Test 3 | **K** |
| **Total enumerator `H_total`** | `[SJL15]`, `[D23]`, `[S25]`, `[GWF23]`, `[DP25b]`, `[LGM25]`, `[LYL26]` | abstracts + `[LYL26]` full text | **K** |
| **Bivariate `(dim C, hull)` enumerator** | `[LYL26]` uses a two-variable product enumerator for `(length, hull codimension)`; prior package's own trace product over `(u,z)` | `[LYL26]` App. B | **K** (product structure) — at best a re-parameterisation |
| **Dual-containing restricted enumerator** | `[S1]` Thm 6 makes dual-containment **componentwise**, so the restricted enumerator also factorises; `[D23]` gives the local Galois self-dual/self-orthogonal counts | `[S1]` Thm 6; `[D23]` abstract | **K** |
| **Gray-image enumerator** | `[S1]` Lemma 9: `ψ(hull_k C) = hull_k(ψ(C))`, so the distribution of hull dimensions of Gray images **equals** that of `C` | `[S1]` Lemma 9; verified numerically (P9) | **K**; and the underlying idea is **F** as a source of novelty — the Gray map cannot change the statistic |
| **Average hull dimension over `A`** | `[DP25]` — average Galois hull dimension over `R_{m,q} = F_q[u]/⟨u^m−u⟩`, an `ℓ=1` case of `A`; also `[JLS18]`, `[Ske03]` | `[DP25]` abstract | **K** |
| **Quantum parameters from the enumerator** | `[S1]` Thm 10 + Lemma 7; `[TG24]`, `[Y2024]`, `[Entropy 2026]` | `[S1]` full text | **K**; and an enumerator cannot produce distances |
| **Isometry-class enumeration of `A`-codes by hull dimension** | no direct hit; but see `[CFLL12]`, `[ISO24]` (class counts of constacyclic codes up to `n`-isometry) and `[LSL25]` (mass formulas for hull-constrained linear codes) | `[S1]` Conclusion p.23; `INDEPENDENT_VERIFICATION_REPORT.md` §4.4 | **U / OPEN at the intersection only** — the only candidate that survives, now with a substantially weaker novelty claim |

---

## 4. Why the "it is absent from the source paper" argument fails

The tempting argument is:

> `[S1]` contains no enumeration theorem, and its Conclusion says the enumeration
> is open. Therefore an enumeration over `A` is new.

Both premises are true (`[S1]` Conclusion, p.23 of the arXiv text; the published
version's abstract and introduction were checked and announce no enumeration).
The conclusion is false, for three independent reasons:

1. **`[S1]`'s own introduction says the field case is done.** p.2: *"In 2023,
   Debnath et al. [9] presented a formula to calculate the Galois hull dimensions
   of constacyclic codes over finite fields. **They also counted the number of
   constacyclic codes of a given Galois hull dimension.**"* The local building
   block is explicitly acknowledged as known.
2. **The gap between local and global is Proposition J**, a three-line
   multiplicativity argument from `[S1]`'s own Theorems 2, 3 and 7.
3. **The same construction is already published one ring family away** (`[S25]`),
   and in at least four other ring settings (`[GWF23]`, `[DP25b]`, `[LGM25]`,
   `[D23]`).

This is exactly the inference the blueprint forbids on p.2: *"Never claim a gap just
because a result is absent from the source paper; compare the wider literature."*

---

## 5. What *would* be needed for an N1 classification

To upgrade any candidate to N1 one would need, at minimum:

1. a theorem whose statement is **not** a product of known local theorems;
2. a proof that does **not** route through Proposition J;
3. a documented comparison showing the specific statement is absent from
   `[SJL15]`, `[D23]`, `[S25]`, `[GWF23]`, `[DP25b]`, `[LGM25]`, `[DP25]`,
   `[Y2024]`, `[LYL26]` at *theorem* level, not abstract level;
4. at least one exact verification that the prior results cannot reproduce.

No candidate in the blueprint's Phase 5 list meets (1)–(2) except the
isometry-class question, which is `U` and not addressed by the blueprint at all.

---

## 6. Residual uncertainties that could change a classification

| ID | Uncertainty | Effect if resolved the other way |
|---|---|---|
| U-1 | Full text of `[D23]` unavailable; its "restrictions on `q`" may be narrow | Would move part of the local enumerator from **K** to **N2** — but *not* the joint object, which stays **K** by Proposition J |
| U-2 | Full text of `[S25]` only partially read | Possibly strengthens **K**; cannot weaken it, since Proposition J is independent |
| U-3 | Published version of `[S1]` (Discrete Math. 2026) read only via abstract/intro/conclusion snippets | If it added an enumeration theorem, the whole question is moot (and the answer remains: not new) |
| U-4 | `[Y2024]` read at abstract level only | Its "possible hull dimensions" could conceivably include multiplicities; the abstract says "possible … dimensions", so **K** stands |

None of U-1…U-4 can make `H_joint` new, because Proposition J is a proof, not a
literature claim.

---

## 7. Classification summary

| Object | Class | One-line reason |
|---|---|---|
| `H_S` local, restricted `q` | **K** | `[D23]`, `[SJL15]` |
| `H_S` local, unrestricted `q` | **U** | scope of `[D23]`'s restriction unknown |
| `H_joint` | **K** | Proposition J (product of known local enumerators) |
| `H_total` | **K** | idem |
| dual-containing restricted | **K** | componentwise condition (`[S1]` Thm 6) |
| Gray-image enumerator | **K** (idea **F**) | `[S1]` Lemma 9 |
| average hull over `A` | **K** | `[DP25]` for `R_{m,q}` |
| isometry-class enumeration | **U** (open) | no result found; declared open by `[S1]` |
| "joint enumerator is new" | **F** | contradicts Proposition J + `[D23]`/`[S25]` |
