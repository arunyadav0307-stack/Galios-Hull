# VERBATIM LOCUS REGISTER — arXiv:2412.08512v1

**Purpose.** Every decisive claim in the F11 audit gets one row here: the printed page,
the section / theorem / equation, and the **verbatim** text. This file exists so that no
claim in the dossier has to be taken on trust.

**Source.** `Galios hulls of constacclic codes over affine algebra rings'.pdf`,
27 pp, SHA-256 `0db90bfbeda69ad1af231b81d92f24be3589ed15ac2e0ade6605ba7ad0ddc039`.
Text extracted with `pypdf` 6.21.1 and cross-checked page by page against the
`p01.txt … p27.txt` split. The printed page number in the page footer equals the page
index, and each quote below was read off the page named.

**Quotation policy.** Quoted characters are as they appear in the PDF text layer.
Ligatures (`ﬁ`, `ﬀ`), inline superscripts, and the extractor's spacing (e.g.
`|S(ν) |`, `d1,d 2`) are reproduced unchanged; nothing is silently corrected, so a
reader can search for the exact string in the extracted text. Words in **bold** inside
a quotation are my emphasis and are marked as such where it matters.

**Status of the version of record.** None of these quotes is from the published
article. The published `§2` is behind a paywall and was **not** read; see
`VOR_INSPECTION_2026-10-20.md` and `FINAL_F11_VERIFICATION_LOG.md` §1.

---

## A. The construction, stated correctly (v1 pp. 4–5)

### L1 — the component degree is `lcm(d_i)` — **p.4**, §2.1

> "The elements of ˆS form a partition of H, and the size of each class is given by
> |S(ν) | = lcm(d1,d 2,...,d ℓ) = [ Fq(ν1,ν 2,...,ν ℓ) : Fq], where di is the degree of
> Irr( νi, Fq), the irreducible polynomial of νi over Fq."

Establishes: `|S(ν)|`, the **degree of the component field**, is `lcm(d₁,…,d_ℓ)`.

### L2 — the CRT decomposition into **fields** — **p.5**, §2.1 (displayed)

> "Fq[X1,X 2,...,X ℓ]/IS(ν) ∼= Fq(ν1,ν 2,...,ν ℓ), and by using the Chinese Remainder
> Theorem, we get
> R ∼= Fq[X1,X 2,...,X ℓ]/ ⋂_{S(ν)∈ ˆS} IS(ν) ∼= ⨁_{S(ν)∈ ˆS}
> Fq[X1,X 2,...,X ℓ]/IS(ν) ∼= ⨁_{S(ν)∈ ˆS} Fq(ν1,ν 2,...,ν ℓ)."

Establishes: each summand is the field `F_q(ν₁,…,ν_ℓ)`, of degree `|S(ν)|` over `F_q`
by L1.

### L3 — each summand is a copy of that field, **not** of `F_q` — **p.5**, §2.1

> "…a set of primitive orthogonal idempotent elements in A denoted by eS(ν) such that
> ∑S(ν)∈ ˆSeS(ν) = 1 and **eS(ν)R ∼= Fq(ν1,ν 2,...,ν ℓ)**."

Establishes: `e_S A ≅ F_q(ν₁,…,ν_ℓ)`, a field of degree `|S(ν)|`. This is the statement
that p.7 later contradicts.

### L4 — `dim_q A = Σ_S |S(ν)|` follows, and `= ∏ d_i` when the `t_i` are coprime

Immediate from L1 + L2: `dim_q A = Σ_S |S(ν)| = Σ_S lcm(d_i)`, and in the examples the
classes are free, giving `∏ deg t_i`. Computed independently in
`code/table1_forensics.py` PART 1 (all three table rings: `Σ|S| = 4 = ∏ deg t_i`).

---

## B. The defective statement (v1 p.7)

### L5 — **the decisive sentence** — **p.7**, §2.3, immediately after the heading
"2.3. Constacyclic codes over A"

> "A linear code C of length n over A is an A-submodule of An. Since **A =
> ∑S(ν)∈ ˆS (eS(ν)Fq)**, each element a ∈ A can be expressed as
> a = ∑_{S(ν)∈ ˆS} aS(ν)eS(ν), **where aS(ν) ∈ Fq for all S(ν) ∈ ˆS**."

Establishes: the paper asserts each summand is a copy of `F_q`, hence
`dim_q A = N = |Ŝ|`. **This is the assertion the whole finding turns on.** It
contradicts L3 by exactly the factor `|S(ν)|`.

### L6 — the projection code lands in `F_q^n` — **p.7**, eq. **(4)**

> "Also, for each ρ = (ρ0,ρ 1,...,ρ n−1) ∈ A n, the projection of ρ by eS(ν) is given by
> ρS(ν) = (ρ0,S(ν),ρ 1,S(ν),...,ρ n−1,S(ν)) ∈ Fnq , where ρi = ∑S(ν)∈ ˆSρi,S(ν)eS(ν),
> ρi,S(ν) ∈ Fq for i = 0, 1,...,n − 1. For each linear codes C ⊆ A n and S(ν) ∈ ˆS, we
> define the projection code over Fnq given by
> **CS(ν) = {cS(ν) ∈ Fnq |c ∈C}. (4)**
> Thus, we have C = ∑S(ν)∈ ˆSCS(ν)eS(ν)."

Establishes: the same `a_S ∈ F_q` assumption is baked into the definition of the
projection code, so the error is not local to one sentence.

### L7 — Theorem 2 says the components are codes **over F_q** — **p.7**

> "Theorem 2. Letλ = ∑S(ν)∈ ˆSλS(ν)eS(ν) be a unit in A. Then C is a λ-constacyclic
> code in An if and only if for each S(ν) ∈ ˆS, CS(ν) is a λS(ν)-constacyclic code of
> length n **over Fq**."

Establishes: the incorrect coefficient field is part of a numbered theorem, not a slip
of exposition. (In the published version this is **Theorem 4**; see §E.)

### L8 — Theorem 3 says the component generators divide over **F_q** — **p.7**

> "Theorem 3. … Then g(x) |xn −λ over A andg(x) is of the form
> g(x) = ∑S(ν)∈ ˆSeS(ν)gS(ν)(x), wheregS(ν)(x) is the generator polynomial of CS(ν)
> and **gS(ν)(x) |xn −λS(ν) over Fq**, for all S(ν) ∈ ˆS."

Establishes: the component generators are treated as polynomials over `F_q`. This is
consistent with the table's data (all 13 `g_S` have `F_q` coefficients and divide
`xⁿ − λ_S` over `F_q` — `code/table1_audit.py` C0, 13/13) and is *why* `dim_{A_S}C_S =
n − deg g_S` still holds over `A_S`.

---

## C. The Gray map and its consequences (v1 pp. 17–18)

### L9 — the Gray map's codomain — **p.17**, eq. **(10)**

> "LetGLN (Fq) be the set of all invertible matrices of order N … Every a ∈ A can be
> expressed as a = ∑S(ν)∈ ˆSaS(ν)eS(ν), where aS(ν) ∈ Fq for all S(ν) ∈ ˆS. Then, we
> define the map
> **ψ : A −→ FNq**, a ↦→ ψ(a) = (aS(ν1),a S(ν2),...,a S(νN ))M, **(10)**
> where | ˆS | = N , and M ∈GLN (Fq) is such that M (M (pk))T = γIN with γ ∈ F∗q"

Establishes: `ψ` maps the `q^{dim_q A}`-element algebra into `F_q^N` with `N = |Ŝ|`.

### L10 — the bijectivity claim — **p.17**, immediately after eq. (10)

> "The map in Equation (10) can be extended componentwise over ψ : An −→FnNq . We define
> the Gray weight for an element a ∈ A n bywG(a) = wH (ψ(a)) where wH refers the
> Hamming weight in Fq. **It is easy to verify that the map ψ is bijective linear
> isometry from An (Gray distance) to FnNq (Hamming distance).**"

Establishes: `ψ` is asserted to be a bijection onto `F_q^{nN}`; hence
`dim_q ψ(C) = dim_q C` is asserted, and the codomain of `ψ(C)` is `F_q^{nN}`.

### L11 — Lemma 9(2) — **p.17–18**

> "Lemma 9. For a linear code C over the ring A,
> 1. ψ(C⊥k ) = ψ(C)⊥k .
> 2. ψ(hullk(C)) = hull k(ψ(C))."

Proof of (2), **p.18**:

> "Again, take β ∈ ψ(C) ∩ψ(C⊥k ). Then there exist c ∈ C and c′ ∈ C⊥k such that
> ψ(c) = β = ψ(c′). **Since ψ is an injective map**, we have c = c′ ∈ C ∩C⊥k ."

Establishes: the proof **uses injectivity explicitly**. If `ψ` is not injective, this
step fails. This is the second horn of the dilemma in the dossier §2.6.

### L12 — the dimension chain, and Theorem 10 — **p.18**

> "For a linear code C of length n over A, let ψ(C) = D. Then D is a linear code of
> length nN . Again, from Lemma 9, we have
> **dim(hull k(D)) = dim(hull k(ψ(C))) = dim(ψ(hullk(C))) = dim q(hullk(C))**."

> "Theorem 10. For a linear code C of length n over A, let ψ(C) = D be an [nN, k,d ]
> linear code over Fq. Then there exists a EAQECC of parameters
> [[nN, k − dimq(hullk(C)),d ;nN − k − dimq(hullk(C))]]q."

Establishes: (i) the chain asserts `dim(ψ(·)) = dim_q(·)`, i.e. injectivity;
(ii) Theorem 10 takes `k = dim_q D` as an input, so if `dim_q D = 2k_printed` the
printed EAQECC parameters are the correct output of the theorem applied to the wrong
input.

---

## D. The arithmetic loci (v1 pp. 12, 19–22)

### L13 — Theorem 8 states the hull dimension **without the `|S(ν)|` weight** — **p.12**

> "Theorem 8. … Then **the q-dimension of the k-Galois hull** of a λ-constacyclic code
> C of length n over A is of the form
> ∑_{S(ν)∈ ˆS} ∑_{t=1}^{s} ∑_{j∈D_{S(ν)t}} ordj(q) ·bS(ν)tj,"

Establishes: the printed formula is a plain sum over `S` of terms that are
`A_S`-dimensions (`ord_j(q)` is the degree of a cyclotomic coset over `F_q`). It equals
the `q`-dimension only when every `|S(ν)| = 1`. Example 3 discriminates numerically:
the paper's own component arithmetic gives `2`, and the weighted value is `4`.

### L14 — the paper's own `N` and `|S|` for Example 2 — **p.19**

> "**N = 2.** Then, there are 2 idempotentseα, α = 1, 2, in the orthogonal idempotent
> decomposition of R."

Establishes: two components, and (Example 2, p.18) both `t_i = x² + …` are quadratic.
With `e_S A ≅ F_q(ν₁,ν₂)` (L3) of degree `lcm(2,2) = 2` (L1), `dim_q A = 4 ≠ N = 2`.

### L15 — Example 2's printed output — **p.20**

> "dim9(hull1(C)) = ( ord1(9) ×b111) + (ord7(9) ×b117) + (ord4(9) ×b214) + (ord28(9)
> ×b2128) = 0. So, by Lemma 9, we have dim9(hull1(ψ(C))) = 0 . Again, **ψ(C) has the
> parameters [14, 10, 4]9** which is an optimal code [15. …] Now, by Theorem 10, we have
> an EAQECC of parameters **[[14, 10, 4; 4]]9**."

Establishes the printed pair `(length 14, dimension 10)` for `n = 7`. Since
`dim₉ C = 20` (independent rank computation) and `20 > 14`, the two printed numbers
cannot both be right.

### L16 — Example 3's printed output — **p.21**

> "Finally, by Theorem 10, we have an EAQECC of parameters **[[26, 20, 4; 2]]25**."

with, immediately above (p.21), "`dim25(hull1(C)) = … = 2`" and "`ψ(C)` has the
parameters `[26, 22, 4]25`". Establishes the printed pair `(26, 22)` for `n = 13`;
`dim₂₅ C = 44 > 26`.

### L17 — Table 1's caption and its rings — **p.21–22**

> "In Table 1, we obtain a few EAQECCs over A. … **For q = 4, we consider A =
> F4[x1,x 2]/⟨x21 +x1 +ω,x 22 +ωx2 +ω⟩**, where ω is a primitive element of F4, …
> For q = 9, we consider the same ring A and the same invertible matrix M given in
> Example 2, and for q = 25, we consider A and M as given in Example 3."

> "**Table 1: EAQECCs obtained from λ-constacyclic codes over A**"

Establishes: all 13 rows use one of three rings, each defined by **two quadratics** —
hence `dim_q A = 4` and `|S(ν)| ≤ 2` in every row, with no case left open.

### L18 — Remark 2 and the closing claim — **p.22–23**

> "Remark 2. In Table 1, we see that there is an EAQECC with parameters [[10, 1, 8; 5]]9."

> "As a future line of research, the enumeration of non-isometric constacyclic co des
> for a given Galois hull dimension is an interesting problem. **This problem is still
> open over A.** Therefore, it may be interesting to count the number of constacyclic
> codes for a given Galois hull dimension over A."

Establishes: the open problem that the `F₉` witness in dossier §3 bears on. Not part
of F11 itself.

---

## E. What is observable about the published version (NOT the body)

Everything in this section is from the legitimate public preview or bibliographic
services. **None of it is the published `§2`, and none of it is used to infer the
published body.**

| # | Published text | Source | What it shows |
|---|---|---|---|
| P-1 | "Our main objective is to derive a formula for the **q-dimensions** of the k-Galois hulls of λ-constacyclic codes over a serial ring 𝒜." | ScienceDirect preview, Introduction | the term implicated in F11 is retained in the introduction |
| P-2 | "…we derive an expression for the Galois hull dimension of a constacyclic code over 𝒜. … This will provide some properties that allow us to compute the **cardinality of the set of q-dimensions** of k-Galois hulls of λ-constacyclic codes of length n over 𝒜, denoted as **𝒟_k(n,q,λ)**." | ScienceDirect preview, Introduction | a **new** counting result absent from v1 |
| P-3 | "Then we derive a formula for the **q-dimension of the k-Galois hull** of a λ-constacyclic code." | ScienceDirect preview, §3 snippet | retained in §3 |
| P-4 | "**Theorem 4** — *Let λ be a unit in* 𝒜 *. If* 𝐶=∑𝑆(𝜈)∈ˆ𝑆𝐶𝑆(𝜈)𝑒𝑆(𝜈) *is a* …" | ScienceDirect preview, §3 snippet | published Theorem 4 begins like v1 **Theorem 2** (L7), i.e. numbering shifted; the snippet is truncated at the decisive clause |
| P-5 | "**Lemma 7** — *[7] For a linear code C with parameters* …" | ScienceDirect preview, §4 snippet | published Lemma 7 = v1 Lemma 8 (the EAQECC existence lemma); numbering shifted |
| P-6 | "### Preliminaries — Let 𝔽𝑞 be the finite field. A linear code of length n is an 𝔽𝑞-subspace of 𝔽𝑞ⁿ. Let λ be a unit in 𝔽𝑞. …" | ScienceDirect preview, §2 snippet | the §2 snippet is the **first paragraph only** and **stops before** the idempotent decomposition |
| P-7 | References (45); Crossref `reference-count: 45` | preview; Crossref | v1 has 44 |
| P-8 | "© 2025 Elsevier B.V. All rights reserved, including those for text and data mining, AI training, and similar technologies." | ScienceDirect article page | no OA licence; no free full text |

**Consequence for the audit.** P-6 is the reason the decisive question cannot be
resolved from the preview: the §2 snippet ends before L5. P-4 shows the numbering moved,
so a note must cite Theorem 4, not Theorem 2. P-8 is part of why access is closed.

---

## F. Register summary

| Locality | Page(s) | Function in the argument |
|---|---|---|
| L1–L3 | 4–5 | the correct statement: components are fields of degree `lcm(d_i)` |
| **L5** | **7** | **the defective sentence: `a_{S(ν)} ∈ F_q`** |
| L6–L8 | 7 | the same assumption in eq. (4), Theorem 2 and Theorem 3 |
| L9–L10 | 17 | the Gray map and the bijectivity claim |
| L11–L12 | 17–18 | Lemma 9's proof uses injectivity; Theorem 10 consumes `k = dim_q D` |
| L13 | 12 | Theorem 8 prints the unweighted sum |
| L14–L16 | 19–21 | the paper's own `N = 2`, and the printed parameters for Examples 2 and 3 |
| L17–L18 | 21–23 | the three rings of Table 1; the closing open problem |
| P-1…P-8 | published | observable surface only — **not** the published body |
