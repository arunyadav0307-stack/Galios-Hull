# SOURCE_PAPER_METADATA

## 1. Exact identity of the audited PDF

| Field | Value | How established |
|---|---|---|
| File audited | `Galios hulls of constacclic codes over affine algebra rings'.pdf` | `sha256sum` |
| SHA-256 | `0db90bfbeda69ad1af231b81d92f24be3589ed15ac2e0ade6605ba7ad0ddc039` | computed |
| Bytes / pages | 291,546 / 27 | `stat`, `PdfReader` |
| PDF `/Title` | `Galois hulls of constacyclic codes over affine algebra rings` | PDF metadata |
| PDF `/Author` | `Indibar Debnath; Habibul Islam; E. Martínez-Moro; Om Prakash` | PDF metadata |
| PDF `/Creator`, `/Producer` | `LaTeX with hyperref`, `GPL Ghostscript 10.01.2` | PDF metadata |
| PDF dates | created / modified `2024-12-11 20:59:09 −05:00` | PDF metadata |
| First page stamp | `arXiv:2412.08512v1 [cs.IT] 11 Dec 2024` | extracted text |
| Venue line | `Preprint submitted to Discrete Mathematics` | extracted text |
| arXiv record | `arXiv:2412.08512`, **v1 only** (no later version posted as of 2026-10-20) | arxiv.org/abs/2412.08512 |
| MSC | 94B05, 94B15, 94B60 | extracted text |

### Authors and affiliations (as printed)

- Indibar Debnath — Dept. of Mathematics, IIT Patna, India
- Habibul Islam — Dept. of Mathematics, IIIT Bhopal, India
- E. Martínez-Moro — Institute of Mathematics, University of Valladolid, Spain
- Om Prakash (corresponding) — Dept. of Mathematics, IIT Patna, India

### Publication status

A publisher version exists: **Discrete Mathematics (2025)**,
ScienceDirect article `S0012365X25003589`. It was **not** accessible in full in
this environment; only the abstract and a partial introduction snippet were
retrievable (see `literature/REFERENCE_VERIFICATION_REPORT.md`).

**This audit is therefore an audit of arXiv:2412.08512v1, not of the version of
record.** Any statement below is a statement about v1. A difference between v1 and
the Discrete Mathematics version cannot be excluded and is flagged as a residual
risk (R-1) in `PHASE_STATUS.md`.

## 2. Critical bibliographic mismatch with the blueprint

The blueprint names, on pages 1 and 2, the source paper as:

> "Hermitian hull of constacyclic codes over a class of non-chain rings and new
> quantum codes", Shikha Yadav, Ashutosh Singh, Habibul Islam, Om Prakash, and
> Patrick Solé, *Computational and Applied Mathematics* (2024),
> DOI 10.1007/s40314-024-02789-1.

The uploaded PDF is a **different article**. Side-by-side:

| | Blueprint's named source | Uploaded PDF (S1) |
|---|---|---|
| Authors | Yadav, Singh, Islam, Prakash, Solé | Debnath, Islam, Martínez-Moro, Prakash |
| Venue | Comput. Appl. Math. **43** (2024) 269 | arXiv:2412.08512v1; Discrete Math. (2025) |
| Ambient field | `F_{q^2}` | `F_q`, `q = p^e` |
| Ring | `R_e = F_{q^2} + uF_{q^2} + … + u^{e−1}F_{q^2}`, `u^e = 1`, `e | (q+1)` | `A = F_q[X_1,…,X_ℓ]/⟨t_1,…,t_ℓ⟩`, each `t_i` square-free |
| Inner product | Hermitian only | `k`-Galois, `0 ≤ k < e` |
| Enumerates codes? | No — *possible* hull dimensions only | No — *set* of attainable dimensions only |
| Quantum codes | Hermitian construction | EAQECCs from Galois hull dimension |

Relationship: **Yadav et al. is reference [43] of S1** and is cited in S1's
introduction (p. 2–3) as the paper that *"studied the Hermitian hulls of
constacyclic codes over a more general class of non-chain ring `F_q[u]/⟨u^e−1⟩`
such that `gcd(e,q)=1`"*.

### Why this is not a technicality

The blueprint instructs (p. 2): *"Do not generalize those assumptions without
proof"* and names the ring with `e | (q+1)`. If an auditor silently audited S1
while writing "the source paper shows …" about Yadav et al.'s Theorems 8–9, the
resulting manuscript would attribute theorems to the wrong paper. This audit
therefore:

1. audits **S1 only**, and marks each finding with `[S1]`;
2. records Yadav et al. as a **separate literature item** `[Y2024]`, verified only
   at abstract/metadata level;
3. refuses to transfer any statement between the two conventions without proof.

## 3. Verified bibliographic facts about Yadav et al. [Y2024]

Retrieved 2026-10-20 from the Springer article page
(`link.springer.com/article/10.1007/s40314-024-02789-1`):

- Title, authors, volume 43, article 269 (2024), published 04 June 2024.
- Abstract states the ring `R_e = F_{q^2}+uF_{q^2}+⋯+u^{e−1}F_{q^2}`, `u^e=1`,
  `F_{q^2}` of order `q^2`, `e | (q+1)`, and
  `λ = η_1α_1 + ⋯ + η_eα_e` with `α_l ∈ F_{q^2}^*` of order `r_l`.
- Abstract claims: (i) *possible* Hermitian hull dimensions; (ii) Hermitian LCD
  conditions; (iii) a result converting every constacyclic code to a Hermitian LCD
  code (Corollaries 2 and 3); (iv) structure of generator polynomials for
  Hermitian dual-containing codes (Theorems 8 and 9); (v) quantum codes via the
  Hermitian construction.

**Decisive point for the present project:** the abstract speaks of *possible*
Hermitian hull dimensions — a **set**, not a count per dimension. It does **not**
claim an enumerator. That is consistent with the gap the blueprint wants to attack.

## 4. Scope of the audited paper (one paragraph, for orientation)

`[S1]` decomposes the semisimple affine algebra
`A = F_q[X_1,…,X_ℓ]/⟨t_1(X_1),…,t_ℓ(X_ℓ)⟩`, with each `t_i` square-free, into a
direct sum of finite fields indexed by Frobenius classes `S(ν)`, defines a
`k`-Galois inner product on `A^n`, and proves that the `k`-Galois dual and hull of
a `λ`-constacyclic code decompose componentwise. It then gives a formula for the
`q`-dimension of the `k`-Galois hull in terms of the exponent data of the
generator polynomial relative to a fixed ordering of the irreducible factors of
`x^n − λ_S`, deduces the **cardinality of the set** of attainable hull dimensions
in two regimes (Corollary 3.5), gives a *sufficient* LCD criterion (Theorem 9), and
constructs EAQECCs through a matrix Gray map.
