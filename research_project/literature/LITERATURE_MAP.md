# LITERATURE_MAP

A one-page orientation to the field, organised so that the **nearest statements to
the proposed work** are easy to find. Every entry carries the ID used across the
project; full metadata and verification level are in
`REFERENCE_VERIFICATION_REPORT.md`; the comparison table is
`LITERATURE_COMPARISON_MATRIX.csv`.

```
                        what is enumerated
                 ┌──────────────────────────────┬──────────────────────────────┐
                 │  codes / polynomials         │  hull dimensions              │
     ┌───────────┼──────────────────────────────┼──────────────────────────────┤
     │  F_q      │  [SJL15] cyclic & negacyclic │  [SJL15] Euclidean+Hermitian  │
     │  (field)  │  [D23]  constacyclic,      │  [D23]  ℓ-Galois, restricted q│
     │           │         ℓ-Galois             │  [LYL26] Hermitian, cyclic    │
     │           │  [Ske03] average hull        │  [JLS18] average Hermitian    │
     ├───────────┼──────────────────────────────┼──────────────────────────────┤
     │  product  │  [S25]  Z_pZ_p[v] separable  │  [S25] fixed hull dim       ▲ │
     │  of       │  [GWF23] double cyclic Z_2   │  [GWF23] fixed hull dim     │
     │  fields   │  [DP25b] Z_{p²} double cyclic│  [DP25b] fixed p-dim        │
     │           │  [LGM25] Z_4 double cyclic   │  [LGM25] fixed 2-dim        │
     │           │  [DP25] average over R_{m,q} │  [DP25] average             │
     ├───────────┼──────────────────────────────┼──────────────────────────────┤
     │  general  │  [S1]  affine algebra A      │  [S1] possible dims only  ✗ │
     │  affine   │  [Y2024] R_e Hermitian      │  [Y2024] possible dims only  │
     │  algebra  │  [TG24] F_q+vF_q            │  [TG24] possible dims only   │
     │           │  [Ent26] non-chain ring     │  [Ent26] construction only   │
     └───────────┴──────────────────────────────┴──────────────────────────────┘
        ▲ = closest precedent to the proposed joint enumerator
        ✗ = the source paper's own acknowledged gap
```

**Reading the map.** The proposed "joint enumerator over `A`" sits in the bottom-right
cell. Everything to its left in that row already exists as an object; everything in
the row above exists as an *enumeration*. The only empty cells are in the bottom-right
corner, and that corner is empty for a reason: `[S1]` Theorem 2 reduces it to the
cells above.

---

## Strata

### A. Hulls over finite fields — solved
`[SJL15]` is the foundation: hull dimensions of cyclic and negacyclic codes, and
enumeration of codes with a given hull dimension, Euclidean and Hermitian.
`[D23]` extends to constacyclic codes with the `ℓ`-Galois product, and counts codes
of a given Galois hull dimension **under restrictions on `q`** (see `[D23c]` for the
published correction). `[LYL26]` gives a product-form Hermitian-hull-codimension
enumerator for cyclic codes with means and variances. `[Ske03]`, `[JLS18]` give
averages.
**Status: `K` — closed.**

### B. Rings that are products of fields — solved, and this is the key
`[S25]` (*Adv. Math. Commun.* **20** (2026) 209–238) is the single most important
precedent: over `Z_pZ_p[v]`, a product ring, it derives hull generating functions
*and enumerates the codes of fixed hull dimension*. `[GWF23]`, `[DP25b]`, `[LGM25]` do the same for double cyclic codes.
`[DP25]` computes average Galois hull dimensions over `R_{m,q} = F_q[u]/⟨u^m−u⟩`,
which is a product of `m` copies of `F_q` — i.e. the `ℓ = 1`, `t(u) = u^m − u` case
of `A`.
**Status: `K` — the technique is standard and the results exist.**

### C. General affine algebra rings — the source paper's home
`[S1]`, `[Y2024]`, `[TG24]`, `[Ent26]`, `[arXiv:2606.22069]` all work over
non-chain rings with CRT decompositions. **None enumerates.** Each determines
*possible* hull dimensions or constructs codes with *chosen* hull dimensions.
`[S1]` states plainly that the enumeration "is still open over `A`".
**Status: `U` for the enumeration — this is genuinely open, and it is
three lines deep (§`JOINT_ENUMERATOR_FEASIBILITY.md` 1.1).**

### D. Galois-self-orthogonal / dual-containing structure
`[FZ17]`, `[Liu18]`, `[LP20]`, `[Cao21]`, `[LA18]`. `[S1]` Theorem 6 makes
dual-containing a componentwise condition over `A`.
**Status: `K` — conditionwise known; the *enumeration* restricted to dual-containing
codes is `K` too, being a componentwise product of the `[D23]` counts.**

### E. Quantum codes
The EAQECC construction `[[n, k−dim(hull), d; n−k−dim(hull)]]_q` is standard
(`[Cao21]` via `[S1]` Lemma 7), as is the `d ≤ (n+2)/2` bound (Lemma 8). Every
paper in strata B and C ends with a table. `[S1]`'s Table 1 has 12 rows.
**Status: `K` — the construction is not a contribution; the tables are.**

### F. Mass formulas and equivalence classes — **added 2026-10-20**

This stratum was missing from the first version of this map and it matters.

`[LSL25]` (Li–Shi–Ling, *IEEE Trans. Inf. Theory* **71** (2025) 273–286) gives a
**closed mass formula for linear codes with a prescribed hull dimension**, plus a
classification of small ternary examples; `[LS24]` does the binary case and
`[LSL24]` (arXiv:2410.13578) the Hermitian and symplectic cases. Separately,
`[CFLL12]` introduced `n`-isometry and `n`-equivalence precisely to **classify
constacyclic codes**, and `[ISO24]` computes the numbers of such classes over finite
chain rings. `[Che23]` shows hull dimension is *not* invariant under equivalence for
`q = 2, 3`.

**Status: `K` for both components separately. The intersection — constacyclic over
`A`, up to an equivalence, stratified by hull dimension — is `U`.**

---

## Where the proposed work would land, and why

| If the paper proves… | Nearest existing statement | Verdict |
|---|---|---|
| `H_total(z) = ∏_S H_S(z)` | `[S1]` Thm 2 + Thm 7; `[S25]` does the same over a product ring | `K` |
| `H_joint(z⃗) = ∏_S H_S(z_S)` | same, plus independence of the CRT factors | `K` |
| exact `H_S(z)` for field components | `[D23]` (restricted `q`), `[SJL15]` | `K` (inside the restriction), `U` outside |
| dual-containing restricted count | `[S1]` Thm 6 + `[D23]` | `K` |
| average hull over `A` | `[DP25]` covers `R_{m,q}`; `[JLS18]`, `[Ske03]` for fields | `K`/`U` |
| **count up to isometry** | `[CFLL12]`, `[ISO24]` for class counts; `[LSL25]` for hull-constrained mass formulas | **`U` only at the intersection** — see `../RESEARCH_DIRECTION_DECISION.md` §C1 |
| count by `(hull, distance)` | nothing closed-form; `[S1]` Remark 1 blocks the easy route | `U`, likely intractable |

---

## One-line summary

Twenty years of work has closed the *linear* problems (hull dimensions, duals,
self-orthogonality, enumerators) over fields and over products of fields. The source
paper's ring `A` is a product of fields after CRT. What remains open is the
*non-linear* problem — counting objects up to equivalence — and that is the problem
`[S1]` itself names.
