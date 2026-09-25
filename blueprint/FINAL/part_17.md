
---

## PART 17 — Final Mathematical / Novelty / Reproducibility Audit

Each checklist item is answered with verdict + evidence + the action still owed.

### 17.1 Mathematics

| Check | Verdict | Evidence / owed action |
|---|---|---|
| All definitions valid; every symbol defined before use | **pass** | PART 7 fixes one convention per symbol; the `κ` bridge (`κ_ours = e − κ_source`) is stated in D1/7.1 |
| All assumptions explicit | **pass** | assumption block in PART 2.3 + per-theorem hypotheses in PART 8 |
| No notation collision | **pass** | `Θ` (tolerance), `o_i` (component order), `r_i` (`ord λ_i`), `h_i`, `T`, `L`, `K`, `d`, `c`, `HA` reserved; the previous document's overloaded use of `T` for both tolerance and length is removed by the A-symbol/F_q-coordinate rule (E5) |
| Duality convention consistent | **pass** | one convention throughout (`σ_κ(a) = a^{p^κ}`, `κ = 0` Euclidean, `κ = e/2` Hermitian), with the source-paper bridge |
| Generator/reciprocal formulas correct | **pass (verified)** | `h^τ = x^{deg h} h(1/x)^{σ_κ}`, 1010/1010 + 488/488 |
| CRT decomposition correct | **pass** | Thm 1 + dimension checks over `q ∈ {4,9,16}` |
| Synchronization theorem justified | **pass (proof outline + exhaustive verification)** | Thm 5 proved from the one-line Lemma L5; verification 166 528/166 528; owed: write the proof in full |
| **lcm theorem justified** | **pass, reframed** | the derivation is CRT-injectivity of `a ↦ (x^{-a} mod f_i)_i` (Thm 6, L8), *not* an assertion about "products of periods"; exhaustive abstract sweep plus the CRT case with 21 distinct pairs and a collision exactly at `Θ = 21`. **Correction accepted:** the lcm is *not* the mechanism behind `T > n`; that is `r = ord(λ) > 1` (Thm 4/7). The previous blueprint's causal claim is withdrawn |
| Quantum construction valid | **pass for the verified instances**; target for general theorem | `[[54,2,3]]_2` and `[[164,1,3]]_4` recomputed independently (F₂ Gaussian elimination; `C^{⊥H} ⊆ C`; distances exhaustive). Thms 10–11 are `[THEOREM TO BE PROVED]` |
| Dimensions consistent | **pass after repair (E4)** | logical-qudit count in the *construction alphabet*, with F₂/F₄ dimensions printed side by side; the earlier `[[14,4,3]]_2` slip is documented |
| Distance claims justified | **pass** | only exhaustive values are quoted as equalities; all other distances are labelled bounds (PART 9.3) |
| Bounds correct | **partially pass / downgraded** | the tolerant Singleton is **downgraded to Conjecture 1** because a proof that the tolerance consumes no Singleton budget is not available; the ceiling theorem (Thm 7) is the replacement quantitative statement and *is* proved |

### 17.2 Computation

| Check | Verdict | Evidence |
|---|---|---|
| Every number reproducible | **pass** | `blueprint/verify/` scripts + `RESULTS.md` (commands and raw outputs); T1–T10, T15, T17 run in pure Python |
| Scripts independently checked | **pass for the headline claims** | syndrome identity: two independent implementations (polynomial reduction vs an explicit `x^{-a}` operator built from `T`), plus a third in the flagship script; distances: enumeration vs CSS-split enumeration |
| Flagship independently verified | **pass** | `verify_flagship2.py` re-derived, in raw-integer F₄ arithmetic with F₂ linear algebra: the factorisations, the three `[7,4,3]` structures, dual containment, `d`-values, `[[7,1,3]]_2 → [[54,2,3]]_2` family, the syndrome table, and the collision at `a = 21` |
| No code-result mismatch | **pass after repair** | one mismatch was found and fixed (E4 dimensions); the earlier `verify_params.py` containment bug and the `check_mechanism` filter bug are logged and are not used |
| No unsupported extrapolation | **pass** | `T/L → (p^κ+1)/(p^κ+2)` is stated as a bound with attained instances, not as an asymptotic claim about rates; `HA > 1` is an open search item, not a claim |

### 17.3 Novelty

| Check | Verdict |
|---|---|
| Closest prior art identified | **pass** — P4 (Luo–Ma–Lin product/`(u+v\|u−v)`), P7 (ring QSC 2024, `F_q+vF_q`, `(1−2v)`), P8 (mixed-weight *QECC*, `F_q × (F_q+vF_q)`), P9 (Galois-hull EAQECC framework) |
| Claimed novelty specific | **pass** — N1 (exact syndrome + padding convention), N2 (invariant `Θ` with `ord_f = r·h` and the ceiling), N3 (`HA`; object only), N4 (EA-QSC; flagged) |
| No copied theorem | **pass** — every retained statement is either attributed (`[KNOWN]`, reference) or carries a status tag and a proof strategy |
| No routine extension presented as major | **pass** — the paper's headline is the *ceiling theorem* (an impossibility for the audited regime plus attainability here); the `κ`-twist machinery is explicitly listed as non-novel |
| Terminology checked for equivalents | **pass (with caveat)** — searches used conceptually equivalent phrasings ("misalignment", "insertion/deletion", "block resynchronization", "synchronizable", "ebits"); **caveat:** arXiv full text, MathSciNet and zbMATH were not queried through their APIs, hence no "first" claim is made anywhere |

### 17.4 Presentation

| Check | Verdict |
|---|---|
| Q1-quality structure | **pass** — 13 sections + 3 appendices (PART 14); every table/figure has a defined content contract (PART 13) |
| LaTeX-compatible | **pass** — PART 16 compiles structurally: required packages and environments present, environments balanced, no undefined `\ref` |
| Clear contribution statement | **pass** — five contributions with object, result and evidence |
| Reproducibility section | **pass** — Appendix B contract plus the verification suite |
| Limitations section | **pass** — Model A/B/C separation; repeated-root, skew, framing, HA and Gray-map limitations |
| Open problems separated | **pass** — Open Problems 1–4 in PART 8 and in the LaTeX; conjectures in their own environments |

### 17.5 What this audit did **not** finish (honest task list, ranked)

1. **Write out the proofs** of Theorems 2, 3, 4, 9 (currently verified + outlined) — the single
   most important remaining task; Theorems 2 and 4 have short standard proofs, Theorem 3 needs
   the σ-reciprocal calculus written carefully, Theorem 9 is a short structural argument.
2. **`HA > 1` example** (Open Problem 3 / task T14): a systematic search over `q ≤ 25`,
   `n ≤ 11` for a dual-containing pair with coprime component orders. If none is found, the
   paper must present `HA` as a definition with a negative search report.
3. **An explicit EA-QSC instance with `c > 0`** (task T13): verify `c = dim hull_{σ_κ}` by rank
   and exhibit the tolerant EA-QSC with unchanged `Θ`.
4. **Systematic prior-art search** (arXiv full-text API, MathSciNet, zbMATH) to license any
   "first" phrasing for the EA-QSC; otherwise use the fallback phrasing already prepared.
5. **MAGMA replication** of T2–T4, T11–T13 (independent implementation #2 at scale).
6. **Tolerant Singleton**: either prove Conjecture 1 or present it purely as a conjecture with
   the measured defects from Table 6.
7. **Bibliography verification**: every reference in blueprint PART 3 must be checked against the
   published version (DOI, volume, pages); the source paper's Theorem 6 needs re-reading against
   the published PDF (our extraction diverges from the verified criterion in 344/742 cases).
