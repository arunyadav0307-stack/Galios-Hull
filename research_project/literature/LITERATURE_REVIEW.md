# LITERATURE_REVIEW

**Purpose.** Establish, from primary records, what is already known about enumerating
codes by hull dimension, so that the novelty question in
`JOINT_ENUMERATOR_FEASIBILITY.md` is decided by evidence rather than by the absence
of a result from one paper.

**Method.** Searched on 2026-10-20 for: hull dimension enumeration; constacyclic
codes over non-chain / product / affine-algebra rings; Hermitian and Galois hulls;
conjugate-reciprocal factor orbits; generating-function and transfer-matrix
enumeration. Publisher pages, arXiv HTML, and review records were used.
**Full text was available for:** S1, arXiv:2607.12242, arXiv:2606.22069.
**Only abstract/metadata was available for:** [Y2024], [D23], [DP25], [S25],
[SJL15], [TG24], [JLS18], and most Springer/Elsevier items. This distinction is
carried into every novelty statement.

---

## 1. The five strata of prior work

### Stratum A — Hull-dimension enumeration over a **field**
This is the oldest and most settled stratum.

| Ref | Work | What it establishes |
|---|---|---|
| `[Sen97]` | Sendrier, *On the dimension of the hull*, SIAM J. Discrete Math. **10** (1997) 282–293 | asymptotic proportion of `q`-ary codes with hull dimension `l`; average hull dimension is asymptotically constant |
| `[Ske03]` | Skersys, *The average dimension of the hull of cyclic codes*, Discrete Appl. Math. **128** (2003) 275–292 | first average-hull formula for cyclic codes |
| `[SJL15]` | Sangwisut–Jitman–Ling–Udomkavanich, *Hulls of cyclic and negacyclic codes over finite fields*, Finite Fields Appl. **33** (2015) 232–257 | **dimensions** of Euclidean and Hermitian hulls, and **enumerations** of cyclic and negacyclic codes having a hull of a given dimension |
| `[JLS18]` | Jitman–Sangwisut, *Average dimension of the Hermitian hull of constacyclic codes over finite fields of square order*, Adv. Math. Commun. **12** (2018) 451–463 | average Hermitian hull dimension for constacyclic codes over `F_{q²}` |
| `[D23]` | Debnath–Prakash–Islam, *Galois hulls of constacyclic codes over finite fields*, Cryptogr. Commun. **15** (2023) 111–127 (+ correction, **15** (2023) 129–130) | Galois hull dimension formula; **"the number of constacyclic codes of length `n` over `F_q` is calculated for a given Galois hull dimension"**, *"considering some restrictions on `q`"*; exact counts of `ℓ`-Galois self-orthogonal and self-dual constacyclic codes |
| `[DP25]` | Debnath–Prakash, *Average dimensions of Galois hulls of constacyclic codes*, Adv. Math. Commun. **19** (2025) 1569–1604 | average Galois hull dimension over `F_q` **and over the non-chain ring `R_{m,q} = F_q[u]/⟨u^m−u⟩`**; Galois-LCD construction over `R_{m,q}` |
| `[LYL26]` | Lu–Yang–Liu–Fu–Guo, arXiv:2607.12242v3 (2026) | structure theory of the Hermitian hull of cyclic codes; **product enumerator** for the hull codimension with exact counts, mean and variance |

**Consequence for this project.** A "generating function that counts codes by hull
dimension" is *not* a new device. It is the standard device, in use since 2015 at
least, and stated explicitly as such by `[SJL15]` ("using the concept of a
generating function in combinatorics") and `[D23]`.

### Stratum B — Hulls over **non-chain / product rings**
| Ref | Work | Ring | What it establishes |
|---|---|---|---|
| `[JS20]` | Jitman–Sangwisut, *Hulls of cyclic codes over the ring `F_2+vF_2`*, Thai J. Math. **18** (2020) 135–144 | `F_2+vF_2`, `v²=v` | hull dimension and average hull dimension |
| `[TBM22]` | Talbi–Batoul–Fotue Tabue–Martínez-Moro, *Hulls of cyclic serial codes over a finite chain ring*, Finite Fields Appl. **77** (2022) 101950 | finite chain ring | average Euclidean hull dimensions |
| `[TG24]` | Tian–Gao–Gao, *Hulls of constacyclic codes over finite non-chain rings and their applications in quantum codes construction*, Quantum Inf. Process. **23** (2024) Paper 9 | `F_q+vF_q` | Euclidean **and Hermitian** hulls of constacyclic codes and of their Gray images; QECCs |
| `[DS25]` | Dougherty–Saltürk, *The number of codes over rings of order 4 containing a hull of given type*, Adv. Math. Commun. **19** (2025) 11–35 | rings of order 4 | **enumerates** codes having a hull of a given *type* |
| `[Y2024]` | Yadav–Singh–Islam–Prakash–Solé, Comput. Appl. Math. **43** (2024) 269 | `R_e = F_{q²}+uF_{q²}+…+u^{e−1}F_{q²}`, `u^e=1`, `e | (q+1)` | **possible** Hermitian hull dimensions (a *set*), Hermitian-LCD conditions, dual-containing structure, quantum codes |
| `[S25]` | Shukla–Pandey–Mishra–Pathak–Upadhyay, *Hulls of `Z_pZ_p[v]`-cyclic codes and construction of EAQECCs*, Adv. Math. Commun. (2025), DOI 10.3934/amc.2025037 | `Z_pZ_p[v]`, `v²=v` — a ring of the **same product type** as `A` | hulls of separable cyclic codes; dimensions via a **generating function**; **"we also enumerate the SCCs over `Z_pZ_p[v]` with hulls of a fixed dimension"** (Thm 3.5 generating function, Thm 3.7 + Cor. 3.8 enumeration; non-separable case Thm 4.10) |
| `[DP25b]` | Debnath–Prakash, *Hulls of separable double cyclic codes over `Z_{p²}`*, Comput. Appl. Math. **44** (2025) 255 | `Z_{p²}` | types, `p`-dimensions, average; **for a fixed `p`-dimension, counts the codes** |
| `[GWF23]` | Gao–Wu–Fu, *Hulls of double cyclic codes*, Finite Fields Appl. (2023), DOI 10.1016/j.ffa.2023.102189 | `Z_2` | generating-function solution of hull dimensions; **enumeration** of double cyclic codes with fixed hull dimension |
| `[LGM25]` | Li–Gao–Ma–Mi, *Hulls of `Z_4`-double cyclic codes*, Comput. Appl. Math. (2025), DOI 10.1007/s40314-025-03385-7 | `Z_4` | enumeration for a fixed 2-dimension; average |

**Consequence.** `[S25]` is the closest structural precedent found: a ring that is a
product of finite fields, separable codes, dimensions by generating function,
**and an explicit enumeration of codes with hulls of a fixed dimension**. It differs
from `A` in that it takes `Z_p` (prime field), cyclic rather than constacyclic
codes, and the Euclidean inner product. Those are *specialisations*, not
qualitative differences.

### Stratum C — The specific ring family `A`
| Ref | Work | Scope |
|---|---|---|
| `[S1]` | Debnath–Islam–Martínez-Moro–Prakash, arXiv:2412.08512v1; **Discrete Math. 349(2) (2026) 114750** | `k`-Galois hulls over `A`; hull-dimension formula; attainable-dimension **set**; LCD condition; EAQECCs. **No enumeration**; declares it open |
| `[DP25]` | (above) | average Galois hull dimension over `R_{m,q} = F_q[u]/⟨u^m−u⟩`, the `ℓ = 1`, `t(u) = u^m−u` case of `A` |
| `[Y2024]` | (above) | the `t(u) = u^e − 1` case over `F_{q²}`, Hermitian |
| `[BGR]` | Bhardwaj–Raka (as reported in arXiv:2412.19126) | constacyclic codes over `F_q[u_1,…,u_k]/⟨f_1,…,f_k⟩`, each `f_i` splitting with simple roots |
| `[arXiv:2606.22069]` (2026) | *Hulls and sums of separable constacyclic codes over `F_q × (F_q+vF_q)`* | generator polynomials of Euclidean and Hermitian hulls **and sums** of separable constacyclic codes over a product ring, plus Gray images. No enumeration |
| `[Entropy 28(4) (2026) 407]` | *Quantum Codes from Galois Hulls of Constacyclic Codes over a Finite Non-Chain Ring* | `ℓ`-Galois hull dimensions over a non-chain ring, construction X. No enumeration |

**Consequence.** The affine algebra `A` itself is not virgin territory: its
decomposition, its constacyclic code structure, its Galois duals, its hull
dimension formula and even its *average* hull dimension (in the `ℓ=1`,
`t = u^m−u` case) are published. What is not published for `A` is an exact count
of codes per hull dimension.

### Stratum D — Galois / Hermitian duality machinery
`[FZ17]` Fan–Zhang, Galois self-dual constacyclic codes, Des. Codes Cryptogr. **84**
(2017) 473–492 (introduces the Galois inner product); `[LFL18]` Liu–Fan–Liu, Galois
LCD codes over finite fields, Finite Fields Appl. **49** (2018) 227–242 (Lemma 1 and
Theorem 1 of S1 come from here); `[LP20]` Liu–Pan, Galois hulls of linear codes,
Des. Codes Cryptogr. **88** (2020) 241–255; `[Cao21]` Cao, MDS codes with Galois
hulls of arbitrary dimensions and the related EAQEC, IEEE Trans. IT **67** (2021)
7964–7984 (Lemma 7 of S1).

### Stratum E — Quantum consequences
`[Cao21]`; `[LA18]` Lai–Ashikhmin (Lemma 8 of S1); `[Guenda18]` Guenda–Jitman–
Gulliver (hull dimension = number of pre-shared ebits); `[TG24]`, `[Y2024]`, `[S1]`,
`[Entropy 2026]` for the constacyclic-over-rings quantum pipeline.

---

## 2. What is now *established* (not merely absent from one paper)

E1. **Enumerating codes by hull dimension is a solved genre over fields.**
`[SJL15]` does cyclic and negacyclic, Euclidean and Hermitian. `[D23]` does
constacyclic with the *Galois* inner product, including exact counts, subject to
restrictions on `q`.

E2. **The generating-function technique for this enumeration is standard and
published.** `[SJL15] §§3–4`, `[S25] Thm 3.5`, `[GWF23]`, `[LYL26] App. B`.

E3. **Enumerating codes by hull dimension has already been done over a product of
finite fields.** `[S25]` over `Z_p × Z_p[v]`, `[DP25b]`/`[GWF23]`/`[LGM25]` over
`Z_{p²}` and `Z_4`-double cyclic codes.

E4. **The hull is additive over the CRT components, so the ring-level distribution
is the convolution of the constituent distributions.** This is Theorem 7 of `[S1]`;
it is independently verified here (`verification/verify_corollary_3_5.out`, Test 3).
*Caveat (audit F11):* Theorem 7 gives additivity of the **`A_S`-dimensions**; to get
the `F_q`-dimension one must weight each component by `d_S = |S(ν)|`. The convolution
statement holds verbatim only when every `t_i` splits over `F_q` (all `d_S = 1`).

E5. **`[S1]` does not enumerate, and says so.** Conclusion, p.23 of the arXiv text:
*"This problem is still open over `A`."* The published version's conclusion was
not readable behind the paywall; only its abstract and introduction were checked
(level B), and neither advertises an enumeration theorem.

E6. **The `k`-Galois hull dimension over `A` is already known in closed form**
(`[S1]` Theorem 8), and its **average** is known in the `R_{m,q}` case (`[DP25]`).

## 3. What remains genuinely open

O1. **Counting non-isometric (equivalence-class) constacyclic codes of `A` with a
given Galois hull dimension.** Declared open by `[S1]`. This is qualitatively
harder than counting subspaces, because the isometry group mixes components and
the constacyclic shift acts simultaneously on all of them.

O2. **The exact local count per hull dimension over `F_q` without `[D23]`'s
restrictions on `q`.** Whether `[D23]`'s restriction is essential or an artefact of
its proof could not be determined here (full text unavailable). Status: **U**.

O3. **Distance-aware enumeration.** No paper found counts codes by
`(hull dimension, minimum distance)`; `[S1]`'s own Remark 1 concedes that the Gray
map with `M = I_N` cannot improve distance.

O4. **Enumerating *dual-containing* constacyclic codes of `A` by hull dimension.**
Not found in the literature as an explicit theorem — **but it is not open**: by
Theorem 6 of `[S1]` dual-containment is a *componentwise* condition, and `[D23]`
already counts the self-orthogonal/self-dual component codes, so this enumerator
factorises as well. Absence from the literature, here, is a publication gap and not
a mathematical one. Classified **K** in `NOVELTY_ASSESSMENT.md` §3.

## 4. Convention map (avoid the two most likely false claims)

| Object | `[S1]` (ambient `F_q`, `q=p^e`) | `[Y2024]` / blueprint (ambient `F_{q²}`) |
|---|---|---|
| Hermitian | `k = e/2`, `e` even | `k = 1`, `e = 2`, conjugation `y ↦ y^q` |
| Ring components | `N = |Ŝ|` | `N = e` |
| "Hermitian hull enumerator" | `k = e/2` slice | the only case treated |

A paper that says "we enumerate Hermitian hull dimensions over `R_e`" and cites
`[D23]` for the local count must convert `k = 1` in `F_{q²}` into `k = e/2` in
`F_q` with `q` replaced by `q²`. Getting this wrong changes which theorem applies.

## 5. Bottom line of the literature review

The literature contains (i) the enumeration technique, (ii) the enumeration over
product rings, (iii) the exact field-level count for the Galois hull, and (iv) the
componentwise additivity that turns the ring-level count into a product.

**What the literature does not contain** is a paper that puts (i)–(iv) together for
the affine algebra `A` and prints the resulting product formula. That is a
*publication gap*, not a *mathematical gap*: the missing step is a three-line
consequence of theorems already in `[S1]`. The blueprint's own rule forbids
presenting a routine corollary as a new theorem, and `[S25]` already occupies the
same mathematical position one ring family to the left.

That distinction is the subject of `NOVELTY_ASSESSMENT.md` and
`JOINT_ENUMERATOR_FEASIBILITY.md`.

**Consistency check.** The `K`/`U`/`F` labels used in §3 above agree across
`NOVELTY_ASSESSMENT.md` §3 and §7, `JOINT_ENUMERATOR_FEASIBILITY.md` §5, and the
`Exact enumeration?` column of `LITERATURE_COMPARISON_MATRIX.csv`. Exactly three
objects carry an open label anywhere in the project: the *isometry-class* count
(O1), the *unrestricted-`q`* local count (O2), and *distance-aware* enumeration
(O3). Every enumeration that factorises through the CRT is labelled **K**, and the
claim that the joint enumerator is new is labelled **F**.
