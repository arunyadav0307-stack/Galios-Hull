# SOURCE_THEOREM_REGISTER

Complete register of every numbered result in the audited source.

**Source:** `[S1]` I. Debnath, H. Islam, E. Martínez-Moro, O. Prakash,
*Galois hulls of constacyclic codes over affine algebra rings*,
arXiv:2412.08512v1, 27 pp. SHA-256 `0db90bfb…ddc039`.
**Auditor:** this session, 2026-10-20. **Read:** all 27 pages.

**Classification tags**

| Tag | Meaning |
|---|---|
| `DIM` | possible/attainable hull dimensions (a set) |
| `FORM` | closed formula for the hull dimension of a given code |
| `GEN` | generator/parity structure of dual or hull |
| `LCD` | LCD / self-dual / dual-containing characterization |
| `COUNT` | exact count of codes (an enumerator) |
| `QCODE` | quantum construction / parameters |
| `TOOL` | imported from the literature, not proved here |

**Notation for entries:** `[S1 §n]` = source section; "proof" = method used in S1;
"status" = this audit's verdict.

---

## Part A — Imported results (not proved in S1)

### Lemma 1 `[S1 §2.2, p.6]` — `TOOL`, cites [27] (Liu–Fan–Liu 2018)
Let `λ ∈ F_q^*`, `ord(λ) = r`.
1. If `C` is `λ`-constacyclic then `C^{⊥_k}` is `λ^{−p^{e−k}}`-constacyclic.
2. If `r | (1 + p^{e−k})` then both `C^{⊥_k}` and `hull_k(C)` are `λ`-constacyclic.

*Status:* accepted as imported. Used by **every** later hull statement.
*Unresolved:* the exact page/theorem in [27] was not checked (paywalled).

### Theorem 1 `[S1 §2.2, p.6]` — `TOOL`+`GEN`, cites [27]
`C = ⟨g(x)⟩` `λ`-constacyclic of dimension `l` in `F_q^n`, parity-check `h`.
Then `C^{⊥_k} = ⟨h^#(x)⟩` where, for `f = Σ f_i x^i` of degree `n`,
```
f^#(x) = Σ_{i=0}^{n} f_i^{p^{e−k}} x^{n−i}           (normalisation by f_0 omitted here)
```
and `hull_k(C) = ⟨lcm(g, h^#)⟩`, `(hull_k(C))^{⊥_k} = ⟨gcd(g, h^#)⟩`.

*OCR caveat:* the printed formula on p.6 reads
`h#(x) = Σ_{i=0}^{l} h_0^{−p^{e−k}} h_i^{p^{e−k}} x^{l−i}`, i.e. a normalising
scalar `h_0^{−p^{e−k}}` is present. `[OCR-SUSPECT]` only in the sense that
subscript/superscript placement could not be confirmed against clean typesetting.
*Status:* **independently confirmed in effect** — the identity
`dim hull_k(C) = n − deg lcm(g, h^#)` was used in the recomputation of Examples 2
and 3 and reproduced the published answers (see `SOURCE_EXAMPLE_RECALCULATION.md`).

### Lemma 2 `[S1 §2.3, p.7]` — `TOOL`, cites [44] (Yılmazgüç–de la Cruz–Martínez-Moro)
`λ = Σ λ_{S(ν)} e_{S(ν)} ∈ A` is a unit **iff** every `λ_{S(ν)} ∈ F_q^*`.
*Status:* elementary; correct (a product of fields).

### Lemma 7 `[S1 §4, p.17]` — `QCODE`, cites [7] (Cao 2021)
For `[n,k,d]_q` code `C`, an EAQECC `[[n, k − dim hull_k(C), d ; n − k − dim hull_k(C)]]_q` exists.
*Status:* imported, used verbatim by Theorem 10.

### Lemma 8 `[S1 §4, p.17]` — `QCODE`, cites [22] (Lai–Ashikhmin 2018)
For `[[n,k,d;c]]_q` with `d ≤ (n+2)/2`: `2(d−1) ≤ n − k + c`.
*Status:* imported bound, used only for the "relatively large minimum distance" label.

---

## Part B — Results proved in S1

### Lemma 3 `[S1 §3, p.9]` — `LCD` (dual-containing criterion, field case)
`C = ⟨g⟩` `λ`-constacyclic over `F_q`. Then `C^{⊥_k} ⊆ C` **iff**
`x^n − λ ≡ 0 (mod g(x)·g^{(l−1)#}(x))`, where `l` is the even integer of §2.4.

*Proof method:* `g | h^#` ⇒ `h^# = g g_1`; apply the `l`-fold `#` to get `h` back up
to a unit; conclude `g·g^{(l−1)#} | x^n − λ`. Converse by reversing.
*Status:* **sound**, modulo the existence of `l` with `f^{l#} = u f` (proved in [9]).
*Use:* the only dual-containing criterion in S1; Theorem 6 globalises it.

### Theorem 2 `[S1 §2.3, p.7]` — `GEN` (decomposition)
`λ = Σ λ_S e_S` a unit. `C ⊆ A^n` is `λ`-constacyclic **iff** each projection
`C_{S(ν)}` is `λ_{S(ν)}`-constacyclic of length `n` over `F_q`.
`[S1 Theorem 3]` adds: `g(x) | x^n − λ` over `A`, `g = Σ e_S g_S`, `g_S | x^n − λ_S`.

*Status:* correct; this is the CRT/principal-ideal statement for a product of fields.
*Use:* **this is the structural reason the joint enumerator factorises** (see
`JOINT_ENUMERATOR_FEASIBILITY.md` §3). It is a *standard tool*, not a new result.

### Theorem 3 `[S1 §2.3, p.7]` — `GEN`
Generator polynomial structure: `g(x) = Σ e_S g_S(x)`, `g_S | x^n − λ_S` over `F_q`.
*Status:* correct, standard. **Gives the bijection**
`{λ-constacyclic codes over A} ↔ ∏_S {divisors g_S of x^n − λ_S}`.
This bijection is used silently by S1 and is the crux of the enumeration question.

### Theorem 4 `[S1 §3, p.8]` — `GEN`
`C` `λ`-constacyclic over `A` ⇒ `C^{⊥_k}` is `(λ^{−p^{e−k}})`-constacyclic over `A`.
*Proof method:* "follows from Proposition 3 of [44] and Lemma 1" — a 1-line proof.
*Status:* correct but **dependent on [44] Prop. 3, which was not read**.

### Theorem 5 `[S1 §3, p.8]` — `GEN`
`C^{⊥_k} = ⟨ h̃(x) = Σ e_S h_S^#(x) ⟩`, where `h_S = (x^n − λ_S)/g_S`.
*Proof method:* componentwise from Theorems 1 and 3.
*Status:* correct.

### Theorem 6 `[S1 §3, p.9]` — `LCD`
`C^{⊥_k} ⊆ C` over `A` **iff** for every `S(ν)`,
`x^n − λ_{S(ν)} ≡ 0 (mod g_{S(ν)} g_{S(ν)}^{(l−1)#})`.
*Proof method:* `C^{⊥_k} = ⊕ C_S^{⊥_k}`, so containment is componentwise; apply Lemma 3.
*Status:* correct. Note it **factorises** — dual-containing is a per-component
condition. This is what makes the restricted enumerator of blueprint Theorem C
also a product.

### Corollary 3.1 `[S1 §3, p.10]` — `LCD`
`C` is `k`-Galois **self-dual** (resp. **LCD**) over `A` **iff** every `C_S` is
self-dual (resp. LCD) over `F_q`.
*Status:* correct; again a product condition.

### Lemma 4 `[S1 §3, p.10]` — `LCD`
Product of two `k`-Galois self-dual codes is self-dual of the summed length.
*Proof method:* direct sum is orthogonal; cardinality count `q^{(n_1+n_2)/2}`.
*Status:* correct. *Minor:* the proof writes "Therefore, `C_1 × C_2 = (C_1 × C_2)^{⊥_k}`" after
showing `⊆` and equality of cardinalities — fine.

### Corollary 3.2 `[S1 §3, p.10]` — `LCD`
A `k`-Galois self-dual code of length 2 implies one of every even length.
*Proof:* `m`-fold product + Lemma 4. **Typo in S1:** the proof says
"from **Theorem 4**", but the result used is **Lemma 4**. `[S1-TYPO-1]`

### Corollary 3.3 `[S1 §3, p.10]` — `LCD`
Same over `A`.
*Status:* correct, follows from Corollary 3.1 + Corollary 3.2.

### Theorem 7 `[S1 §3, p.10]` — `GEN`+`FORM` — **central structural result**
`hull_k(C) = ⊕_S hull_k(C_{S(ν)})`, with generator polynomial
`G(x) = Σ_S e_S · lcm(g_S(x), h_S^#(x))`.
*Proof method:* "follows from Theorem 3 and Theorem 5" — i.e. componentwise.
*Status:* **correct and decisive**. Consequences:
1. `dim_q hull_k(C) = Σ_S dim_q hull_k(C_S)` — hull dimension is **additive**.
2. Hence the hull-dimension distribution over `A` is the **convolution** of the
   constituent distributions. Verified exactly in `verification/verify_corollary_3_5.out`
   (Test 3: local `{0:2,1:2,2:1}` ⊗ same = direct over `A`; 25 codes both ways).
*Use:* this is the theorem that makes the "joint enumerator" a product, and
therefore routine. It is the single most important entry in this register.

### Lemma 5 `[S1 §3, p.11]` — `FORM`
With `Δ_{S t} := Σ_{j∈D_{S t}} Σ_{i=1}^{β_{S t}(j)} deg f_{ij}`,
```
Δ_{S t} = Σ_{j ∈ D_{S t}} φ(j) / (a_t · φ(r_{S(ν)})).
```
*Proof as printed:* combines `Σ_t a_t Δ_{S t} = n'` (Eq. 7) with the identity
`Σ_t Σ_{j∈D_{S t}} φ(j)/φ(r_S) = n'` from [9], then **passes to a termwise equality
in `t`**.
*Audit finding `[S1-GAP-1]`:* that passage is not justified. From
`Σ_t (a_t Δ_t − X_t) = 0` one may not conclude `a_t Δ_t = X_t` for each `t`.
The result is nevertheless **true**, because the per-`t` identity follows directly
from the cyclotomic degree count: the number of irreducible factors of degree
`ord_j(q)` attached to `(t,j)` is `φ(j)/(a_t φ(r_S) ord_j(q))`, so
`Δ_{S t} = Σ_j β_{S t}(j) ord_j(q) = Σ_j φ(j)/(a_t φ(r_S))`.
**Verdict:** true statement, incomplete proof. Repairable in two lines. Not a
correctness failure of Theorem 8.

### Lemma 6 `[S1 §3, p.12]` — `TOOL`
`ord(λ_{S(ν)}) | ord(λ)` for every component.
*Proof:* `λ^r = 1 = Σ e_S` ⇒ `λ_S^r = 1` for each `S`, by uniqueness of the
idempotent expansion.
*Status:* correct.

### Theorem 8 `[S1 §3, p.12]` — `FORM` — **main dimension formula**
Hypotheses: `n = n' p^{e'}`, `gcd(n',p) = 1`; `λ = Σ λ_S e_S` a unit;
`gcd(ord(λ), n') = 1`; `ord(λ) | (1 + p^{e−k})`, `0 ≤ k < e`.
Conclusion:
```
dim_q hull_k(C) = Σ_{S(ν)} Σ_{t=1}^{s} Σ_{j∈D_{S(ν)t}} ord_j(q) · b_{S(ν)t j},
b_{S(ν)t j} = Σ_{i=1}^{β_{S(ν)t}(j)} b_{S(ν)t i j},
b_{S(ν)t i j} = a_t p^{e'} − Σ_{δ=0}^{a_t−1} max{ u_{S(ν)tij,δ} , p^{e'} − u_{S(ν)tij,δ−1} },
0 ≤ b_{S(ν)t j} ≤ β_{S(ν)t}(j) · ⌊ a_t p^{e'}/2 ⌋.
```
*Proof method:* `dim = n − deg(lcm(g_S, h_S^#))` (Theorem 1/7); substitute the
exponent vectors of `g_S`, `h_S`, `h_S^#`; each lcm exponent is
`max{u_δ, p^{e'}−u_{δ−1}}`; sum.
*Audit:* the derivation is **correct** in structure and reproduces both worked
examples exactly. The stated upper bound is **true**, and admits a clean proof that
S1 does not give: since `max{x,y} ≥ (x+y)/2`,
`Σ_δ max{u_δ, p^{e'}−u_{δ−1}} ≥ ½ Σ_δ (u_δ + p^{e'} − u_{δ−1}) = a_t p^{e'}/2`,
whence `0 ≤ b ≤ a_t p^{e'}/2`; integrality gives the floor. Compare
`[S1-GAP-2]` below — S1 asserts this bound without proof.
*Status:* **verified** (Examples 2, 3 and Corollary 3.5 tests), **subject to audit
F11**: the formula computes `Σ_S dim_{A_S} hull_k(C_S)`, which equals
`dim_q hull_k(C)` only when every Frobenius class `S(ν)` is a singleton (i.e. every
`t_i` splits over `F_q`); otherwise a factor `|S(ν)|` per component is missing.

### Corollary 3.4 `[S1 §3, p.14]` — `FORM`
If `gcd(n,q) = 1` (so `e' = 0`, `n = n'`), the `t = 1` term vanishes and
```
dim_q hull_k(C) = Σ_S Σ_{t=2}^{s} Σ_{j∈D_{S t}} ord_j(q) b_{S t j},
0 ≤ b_{S t j} ≤ β_{S t}(j) ⌊a_t/2⌋.
```
*Justification in S1:* `a_1 = 1 ⇒ b_{S1j} ≤ β⌊1/2⌋ = 0`.
*Status:* correct. **This is the simple-root case**, and it is the only case the
prior Phase-10F package treated (`gcd(n,p)=1`).

### Corollary 3.5 `[S1 §3, p.14]` — `COUNT`-adjacent — **the closest thing to an enumerator in S1**
Let `D_k(n,q,λ) := { dim_q hull_k(C) : C λ-constacyclic over A }`. Under
Theorem 8's hypotheses:
1. If `p` odd and `n' = 1`: `|D_k(n,q,λ)| = N(n−1)/2 + 1`.
2. If `p = 2`, `e` even, `k = e/2`, `ord(λ)n' | (2^e − 1)`: `|D_{e/2}(n,2^e,λ)| = N n/2 + 1`.

where `N = |Ŝ|` is the number of idempotent components.

*Audit — this is the crucial entry for the project.* Three observations:

(a) **It counts dimensions, not codes.** `|D_k|` is the cardinality of a *set of
attainable integers*. It says nothing about how many codes realise each value.
It is therefore **not** an enumerator and not a hull-dimension distribution.

(b) **`N`-multiplicativity is exactly Theorem 7.** Part 1's value
`N(n−1)/2 + 1` is what one gets by taking the single-field set `{0,…,(n−1)/2}`
(verified: `{0,1,2,3,4}` for `q=9,n=9,λ=±1,k=1`) and summing `N` independent
copies (verified: `{0,…,8}`, 9 values, for `N=2`). So the corollary *is* the
statement "the attainable set of a sum of independent copies is the sumset" — plus
the (non-trivial) single-field input that the set is a full interval.

(c) **Boundary gap `[S1-GAP-3]`:** Part 2 implicitly requires `n` even. With
`n = n'p^{e'}`, `p = 2`, `gcd(n',2)=1`, `n` is even iff `e' ≥ 1`. If `e' = 0` then
`n = n'` is odd and `N n/2 + 1` is not an integer. The printed hypotheses do not
exclude `e' = 0`. The proof uses `p^{e'}/2`, which is non-integral in that case.
**Recommended repair:** add `e' ≥ 1` to the hypotheses of part 2.

*Status:* parts (1) and (2) **verified computationally** in admissible regimes
(`verification/verify_corollary_3_5.out`: PASS, 9 and 5 respectively); part 2
**not valid** for `e' = 0` as printed.

### Theorem 9 `[S1 §3, p.16]` — `LCD` (sufficient only)
`gcd(n,q)=1`, `r = ord(λ)`, `gcd(r,n)=1`, `r | 1 + p^{e−k}`.
If `n·r ∈ B_1` then every `λ`-constacyclic code of length `n` over `A` is
`k`-Galois LCD.
*Proof method:* `n r ∈ B_1` ⇒ every divisor of `n r` lies in `B_1` ⇒
`A_{S(ν)} ⊆ B_1` ⇒ `D_{S t} = ∅` for `t ≥ 2` ⇒ Corollary 3.4 gives dimension 0.
*Status:* correct as a **sufficient** condition. It is **not** claimed necessary,
and is not necessary in general.
*`[S1-TYPO-2]`:* the statement prints "**A** divides `1+p^{e−k}`" where `r` is meant.

### Lemma 9 `[S1 §4.1, p.17]` — `QCODE` — Gray-map compatibility
For the linear map `ψ : A → F_q^N`, `a ↦ (a_{S(ν_1)},…,a_{S(ν_N)})·M` with
`M M^{(p^k)T} = γ I_N`:
1. `ψ(C^{⊥_k}) = ψ(C)^{⊥_k}`;
2. `ψ(hull_k(C)) = hull_k(ψ(C))`.

*Proof method:* (1) `C^{⊥_k} = (C^{(p^{e−k})})^⊥` and `ψ` intertwines Frobenius;
(2) `ψ` is injective, hence `ψ(C∩D) = ψ(C)∩ψ(D)`.
*Status:* **correct, and conceptually important**: because `ψ` is a `k`-Galois
isometry, the Gray map **cannot change** the hull-dimension distribution. Any
"enumerator of Gray images" is the same enumerator. This kills a natural-looking
research direction (see `JOINT_ENUMERATOR_FEASIBILITY.md` §4, candidate C4).

### Theorem 10 `[S1 §4.1, p.18]` — `QCODE`
`ψ(C) = D` an `[nN, k, d]_q` code ⇒ EAQECC
`[[nN, k − dim_q hull_k(C), d ; nN − k − dim_q hull_k(C)]]_q`.
*Proof method:* Lemma 7 + Lemma 9 + `dim ψ(hull_k C) = dim hull_k C`.
*Status:* correct **given** Lemma 7 and Lemma 9. Note the dimension `k` here is
`dim ψ(C)`, and `dim_q hull_k(C)` is the **ring-level** hull dimension — legitimate
precisely because of Lemma 9. Verified numerically in both examples.

---

## Part C — Unnumbered but load-bearing content

| ID | Content | Location | Status |
|---|---|---|---|
| **Eq. (1)** | Definition of `A = F_q[X_1,…,X_ℓ]/⟨t_1(X_1),…,t_ℓ(X_ℓ)⟩`, `t_i` square-free | p.3 | definition |
| **§2.1** | Class `S(ν)`, `N = |Ŝ|`, `A ≅ ⊕_S F_q(ν_1,…,ν_ℓ)`, primitive idempotents `e_S` | p.4–5 | standard CRT; correct |
| **Eq. (2)** | `⟨α,β⟩_k = Σ α_i β_i^{p^k}` | p.6 | **asymmetric in the two slots** — convention hazard, see audit F5 |
| **Eq. (4)** | Projection code `C_{S(ν)}` | p.7 | definition |
| **Eq. (5)/(6)** | Factor ordering of `x^n − λ`; `β_t(j) = φ(j)a_t/(φ(r) ord_j(q))` `[OCR-SUSPECT: numerator/denominator of a_t]` | p.8, p.11 | **not reproduced verbatim**; see audit F2 |
| **Eq. (7)** | `Σ_t a_t Δ_{S t} = n'` | p.11 | **verified** by degree count |
| **Eq. (10)** | Gray map `ψ(a) = (a_{S(ν_1)},…,a_{S(ν_N)})M`, `M M^{(p^k)T} = γ I_N` | p.17 | definition; matrix condition verified in Ex. 2, 3 |
| **Table 1** | 13 rows of EAQECCs over `F_4, F_9, F_25` | p.22 | **not** independently recomputed (only rows 7 and 13, which are Examples 2 and 3, were) |
| **Example 1** | Idempotents of `A_1 = F_2[x_1,x_2]/⟨t_1,t_2⟩` | p.5–6 | **not** recomputed; no output depends on it |
| **Remark 1** | `M = I_N` gives a direct sum, no distance gain | p.18 | heuristic remark, correct in spirit, no proof |
| **Remark 2** | `[[10,1,8;5]]_9` "relatively large minimum distance" | p.22 | label only |

---

## Part D — Summary statistics of the register

| Kind | Count | IDs |
|---|---|---|
| Theorems | 10 | 1–10 |
| Lemmas | 9 | 1–9 |
| Corollaries | 5 | 3.1–3.5 |
| Remarks | 2 | 1–2 |
| Worked examples | 3 | 1–3 |
| Numbered tables | 1 | Table 1 |
| **Proved in S1** | 15 | Thm 2,3,4,5,6,7,8,9,10; Lem 3,4,5,6,9; Cor 3.1–3.5 (excluding imported) |
| **Imported** | 4 | Thm 1, Lem 1, 7, 8 (+ Lem 2 from [44]) |
| **Results that are `COUNT`** | **0** | — |

**`|{results in S1 that count codes by hull dimension}| = 0.`**
S1 explicitly says so in its Conclusion (p.23):
*"the enumeration of non-isometric constacyclic codes for a given Galois hull
dimension is an interesting problem. This problem is still open over A. Therefore,
it may be interesting to count the number of constacyclic codes for a given Galois
hull dimension over A."*

That sentence is the origin of the entire project, and it must be quoted accurately:
S1 declares the enumeration **open**; it does not claim it.
