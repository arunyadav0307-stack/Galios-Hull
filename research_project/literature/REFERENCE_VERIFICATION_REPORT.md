# REFERENCE_VERIFICATION_REPORT

Verified 2026-10-20. Every entry states **how far** the metadata was checked, because
"present in a reference list" is not verification.

Levels: **A** = full text read · **B** = publisher page / abstract + metadata read ·
**C** = metadata only (cross-checked in ≥ 2 independent records) · **D** = could not
verify.

---

## 1. The two papers at the centre of the brief

| ID | Reference | Level | Findings |
|---|---|---|---|
| `[S1]` | I. Debnath, H. Islam, E. Martínez-Moro, O. Prakash, *Galois hulls of constacyclic codes over affine algebra rings*, arXiv:2412.08512v1 (11 Dec 2024) | **A** | 27 pp., read in full. `arXiv:2412.08512` has **v1 only**. Published version: *Discrete Math.* **349**(2) (2026) **114750**, DOI `10.1016/j.disc.2025.114750`; abstract and introduction retrieved (level B); **the published conclusion was not readable**. The "still open" statement is verified for the arXiv text only. |
| `[Y2024]` | S. Yadav, A. Singh, H. Islam, O. Prakash, P. Solé, *Hermitian hull of constacyclic codes over a class of non-chain rings and new quantum codes*, Comput. Appl. Math. **43**(5) (2024) Paper 269, DOI `10.1007/s40314-024-02789-1` | **B** | Published 04 June 2024. Ring `R_e = F_{q²}+uF_{q²}+…+u^{e−1}F_{q²}`, `u^e=1`, `e|(q+1)`. Abstract claims **possible** Hermitian hull dimensions (a set), LCD conditions, dual-containing structure, quantum codes. **No enumeration claim.** Metadata cross-checked against Springer and the reference list of `[S1]` (its [43]). |

> **Discrepancy of record:** the blueprint names `[Y2024]` as *the* source paper.
> The uploaded PDF is `[S1]`. Both are real, both are by overlapping author groups,
> and `[S1]` cites `[Y2024]`. See `SOURCE_PAPER_METADATA.md` §2.

## 2. Load-bearing precedents for the novelty question

| ID | Reference | Level | Verified content |
|---|---|---|---|
| `[D23]` | I. Debnath, O. Prakash, H. Islam, *Galois hulls of constacyclic codes over finite fields*, Cryptogr. Commun. **15**(1) (2023) **111–127**, DOI `10.1007/s12095-022-00591-6` | **B** | Received 23 Oct 2021, accepted 16 May 2022, published 23 Jun 2022. Abstract: hull dimension formula; **"considering some restrictions on `q`, the number of constacyclic codes of length `n` over `F_q` is calculated for a given Galois hull dimension"**; exact enumeration of `ℓ`-Galois self-orthogonal and self-dual constacyclic codes. |
| `[D23c]` | Correction to `[D23]`, Cryptogr. Commun. **15**(1) (2023) **129–130**, DOI `10.1007/s12095-022-00602-6` | **B** | Corrects `1 ≤ i₁ ≤ i₂ ≤ a_i` to `1 ≤ i₁ < i₂ ≤ a_i` and proves `f_{i₁}^# ≠ f_{i₂}^#`. **Relevant:** this is exactly the distinctness of conjugate-reciprocal factors on which the orbit counting rests. Any enumeration built on `[D23]` must use the corrected statement. |
| `[S25]` | A. K. Shukla, O. P. Pandey, V. Mishra, S. Pathak, A. K. Upadhyay, *Hulls of `Z_pZ_p[v]`-cyclic codes and construction of EAQECCs*, **Adv. Math. Commun. 20 (2026) 209–238**, DOI `10.3934/amc.2025037` (early access 11 Aug 2025) | **A** | Abstract + substantial full-text excerpts. Confirms: hull generators of separable cyclic codes; **dimensions via a generating function**; **enumeration of SCCs with hulls of a fixed dimension** (Thm 3.5; Thm 3.7; Cor. 3.8); non-separable case with enumeration (Thm 4.10). **This is the closest precedent to the "joint enumerator".** |
| `[SJL15]` | E. Sangwisut, S. Jitman, S. Ling, P. Udomkavanich, *Hulls of cyclic and negacyclic codes over finite fields*, Finite Fields Appl. **33** (2015) **232–257**, DOI `10.1016/j.ffa.2014.12.008` | **B** | "The enumerations of cyclic codes and negacyclic codes of length `n` over `F_q` having hulls of a given dimension are established as well", for both Euclidean and Hermitian hulls. |
| `[DP25]` | I. Debnath, O. Prakash, *Average dimensions of Galois hulls of constacyclic codes*, Adv. Math. Commun. **19**(6) (2025) **1569–1604**, DOI `10.3934/amc.2025010` | **B** | Average Galois hull dimension over `F_q`; Galois duals and hulls over `R_{m,q} = F_q[u]/⟨u^m−u⟩`; formulae for hull dimensions **and average** hull dimensions over `R_{m,q}`; Galois-LCD construction. `R_{m,q}` is the `ℓ=1`, `t(u)=u^m−u` case of `A`. |
| `[LYL26]` | L. Lu, R. Yang, Y. Liu, Q. Fu, G. Guo, *Hermitian hulls of cyclic codes and exact dual distances of extended linear codes*, arXiv:2607.12242v3 (14 Oct 2026) | **A** (introduction) | Contains a **product enumerator** for the hull codimension of cyclic codes over `F_{q²}`, with exact counts, scarcity probability, mean and variance (its App. B). Field-only, defining-set method. |
| `[GWF23]` | J. Gao, T. Wu, F.-W. Fu, *Hulls of double cyclic codes*, Finite Fields Appl. (2023), DOI `10.1016/j.ffa.2023.102189` | **B** | Generating-function solution of hull dimensions; **enumeration** of double cyclic codes over `Z_2` with hulls of a fixed dimension. |
| `[DP25b]` | I. Debnath, O. Prakash, *Hulls of separable double cyclic codes over `Z_{p²}`*, Comput. Appl. Math. **44** (2025) **255**, DOI `10.1007/s40314-025-03206-x` | **B** | Types, `p`-dimensions, averages; **for a fixed `p`-dimension, counts the number of codes**. |
| `[LGM25]` | H. Li, J. Gao, F. Ma, J. Mi, *Hulls of `Z_4`-double cyclic codes*, Comput. Appl. Math. (2025), DOI `10.1007/s40314-025-03385-7` | **B** | Enumeration of NSDCCs with hulls of a fixed 2-dimension; average 2-dimension. |

| `[LSL25]` | S. Li, M. Shi, S. Ling, *A mass formula for linear codes with prescribed hull dimension and related classification*, IEEE Trans. Inf. Theory **71**(1) (2025) **273–286**, DOI `10.1109/TIT.2024.3425058` | **B** | closed mass formula for linear codes with a prescribed hull dimension; classification of (optimal) ternary linear codes with small parameters. |
| `[LS24]` | S. Li, M. Shi, *Characterization and classification of binary linear codes with various hull dimensions from an improved mass formula*, IEEE Trans. Inf. Theory **70**(5) (2024) **3357–3372** | **C** | binary case of the same programme. |
| `[LSL24]` | S. Li, M. Shi, Y. Li, S. Ling, *A further study on the mass formula for linear codes with prescribed hull dimension*, arXiv:2410.13578 (17 Oct 2024) | **A** (intro) | Hermitian and symplectic mass formulas via unitary/symplectic group actions. |
| `[CFLL12]` | B. Chen, Y. Fan, L. Lin, H. Liu, *Constacyclic codes over finite fields*, Finite Fields Appl. **18**(6) (2012) **1217–1231**, DOI `10.1016/j.ffa.2012.10.001` | **A** | introduces `n`-isometry and `n`-equivalence to classify constacyclic codes; the `n`-equivalence classes of shift constants in `F_q^*` number `gcd(n, q−1)`. |
| `[ISO24]` | *On isometry and equivalence of constacyclic codes over finite chain rings*, Cryptogr. Commun. (2024), DOI `10.1007/s12095-024-00758-3` | **B** | computes the numbers of `n`-isometry and `n`-equivalence classes for finite chain rings. |
| `[Che23]` | H. Chen, *On the hull-variation problem of equivalent linear codes*, IEEE Trans. Inf. Theory **69** (2023) **2911–2922** | **C** (via two 2025–26 papers) | for `q = 2, 3`, equivalent codes can have different hull dimensions. |

## 3. Supporting references cited by `[S1]` and used in this audit

| ID | Reference | Level | Note |
|---|---|---|---|
| `[Liu18]` | X. Liu, Y. Fan, H. Liu, *Galois LCD codes over finite fields*, Finite Fields Appl. **49** (2018) 227–242 | **C** | source of `[S1]` Lemma 1 and Theorem 1 — **not read** |
| `[FZ17]` | Y. Fan, L. Zhang, *Galois self-dual constacyclic codes*, Des. Codes Cryptogr. **84** (2017) 473–492 | **C** | introduces the Galois inner product |
| `[LP20]` | H. Liu, X. Pan, *Galois hulls of linear codes over finite fields*, Des. Codes Cryptogr. **88** (2020) 241–255 | **C** | — |
| `[Cao21]` | M. Cao, *MDS codes with Galois hulls of arbitrary dimensions and the related entanglement-assisted quantum error correction*, IEEE Trans. IT **67**(12) (2021) 7964–7984 | **C** | source of `[S1]` Lemma 7 — **not read** |
| `[LA18]` | C.-Y. Lai, A. Ashikhmin, *Linear programming bounds for entanglement-assisted quantum error-correcting codes by split weight enumerators*, IEEE Trans. IT **64**(1) (2018) 622–639 | **C** | source of `[S1]` Lemma 8 — **not read** |
| `[Y24b]` | G. G. Yılmazgüç, J. de la Cruz, E. Martínez-Moro, *Abelian and consta-Abelian polyadic codes over affine algebras with a finite commutative chain coefficient ring*, Cryptogr. Commun. **16**(4) (2024) 889–907 | **C** | source of `[S1]` Lemma 2 and Theorem 4 — **not read** |
| `[TG24]` | Z. Tian, J. Gao, Y. Gao, *Hulls of constacyclic codes over finite non-chain rings and their applications in quantum codes construction*, Quantum Inf. Process. **23** (2024) Paper 9, DOI `10.1007/s11128-023-04230-8` | **B** | ring `F_q+vF_q`, `v²=v`; Euclidean **and Hermitian** hulls of constacyclic codes and Gray images; QECCs. No enumeration claim. |
| `[Sen97]` | N. Sendrier, *On the dimension of the hull*, SIAM J. Discrete Math. **10**(2) (1997) 282–293, DOI `10.1137/S0895480195294027` | **B** | asymptotic proportion of codes with hull dimension `l` |
| `[Ske03]` | G. Skersys, *The average dimension of the hull of cyclic codes*, Discrete Appl. Math. **128**(1) (2003) 275–292 | **C** | average hull, cyclic codes |
| `[JLS18]` | S. Jitman, E. Sangwisut, *The average dimension of the Hermitian hull of constacyclic codes over finite fields of square order*, Adv. Math. Commun. **12**(3) (2018) 451–463, DOI `10.3934/amc.2018027` | **B** | average Hermitian hull over `F_{q²}`; bounds |
| `[JS20]` | S. Jitman, E. Sangwisut, *Hulls of cyclic codes over the ring `F_2+vF_2`*, Thai J. Math. **18** (2020) 135–144 | **C** | — |
| `[TBM22]` | S. Talbi, A. Batoul, A. Fotue Tabue, E. Martínez-Moro, *Hulls of cyclic serial codes over a finite chain ring*, Finite Fields Appl. **77** (2022) 101950 | **C** | — |
| `[DS25]` | S. T. Dougherty, E. Saltürk, *The number of codes over rings of order 4 containing a hull of given type*, Adv. Math. Commun. **19**(1) (2025) 11–35 | **C** | enumeration by hull **type** over rings of order 4 |
| `[Ent26]` | *Quantum codes from Galois hulls of constacyclic codes over a finite non-chain ring*, Entropy **28**(4) (2026) 407, DOI `10.3390/e28040407` | **B** | `ℓ`-Galois hull dimensions over a non-chain ring; construction X. No enumeration. |
| `[arXiv:2606.22069]` | *Hulls and sums of separable constacyclic codes over `F_q × (F_q+vF_q)` and new quantum codes* (2026) | **A** (intro) | generator polynomials of hulls **and sums** of separable constacyclic codes over a product ring + Gray images. No enumeration. |

## 4. References inside `[S1]` that are listed but not verified
`[S1]` has 44 references. The audit has verified levels A/B/C for **31** of them (the rows above;
**19 rows were present on 2026-10-20 before the independent-verification pass, 12 were added by it**).
The remainder (e.g. `[2]` Assmus–Key, `[6]` Brun–Devetak–Hsieh, `[8]`
Carlet–Guilley, `[11]` Dougherty–Sahinkaya, `[14]` Goyal–Raka, `[15]` Grassl's
table, `[16]` Guenda et al., `[17]` Islam–Martínez-Moro–Prakash, `[18]` Islam–
Prakash–Verma, `[19]`, `[21]`, `[23]`–`[25]` Leon et al., `[26]` Li–Zhu–Li,
`[30]`–`[33]`, `[36]`, `[38]`, `[39]`, `[40]`, `[42]`, `[44]`) were **not**
individually verified. No claim in this audit depends on them.

## 5. Metadata defects found

| ID | Defect | Impact |
|---|---|---|
| M-1 | The blueprint attributes `[S1]`'s content to `[Y2024]` | provenance; corrected in `SOURCE_PAPER_METADATA.md` |
| M-2 | `[D23]` has a **published correction** (Cryptogr. Commun. 15 (2023) 129–130) affecting the distinctness of `f^#`-conjugates — i.e. the factor-orbit argument | any enumeration citing `[D23]` must cite the correction too |
| M-3 | `[S1]` arXiv v1 was not updated after publication | the arXiv and journal texts may differ; unverifiable here |
| M-4 | The uploaded file name is misspelled ("Galios", "constacclic") | not an identifier; always use the hash |

### Corrections made to this file on 2026-10-20 (independent verification)

| ID | Was | Now |
|---|---|---|
| A1 | `[SJL15]` DOI `10.1016/j.ffa.2014.12.002` | **`10.1016/j.ffa.2014.12.008`** (verified on ScienceDirect, Wikidata and three citing papers) |
| A2 | `[S25]` cited without volume or pages | **Adv. Math. Commun. 20 (2026) 209–238** |
| A4 | The Li–Shi–Ling mass-formula line was absent | added as `[LSL25]`, `[LS24]`, `[LSL24]` |

These corrections do not change any verdict about `[S1]`; they change the novelty
assessment of direction **C1** (see `../RESEARCH_DIRECTION_DECISION.md` §C1).

## 6. Honest limitation

Ten of the twenty-six verified items were checked only at **metadata** level (`C`),
two were read in full (`A`), and fourteen at **abstract/publisher** level (`B`). This is enough to establish *that a result exists* and *what it claims*, and
therefore enough to defeat a novelty claim ("this is absent from the literature").
It is **not** enough to establish priority in the other direction, and none is
claimed.
