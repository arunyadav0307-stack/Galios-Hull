# P1-18 — Manuscript Readiness Audit and Next Research Priorities

**Object:** corrected manuscript `P1_15_MANUSCRIPT_DRAFT.tex` / `.md` after P1-17, assessed against the frozen blueprint (`02_THEOREM_BLUEPRINT.md`, SHA-256 `ec2fd8d58f8d2a986314f83997d750d689f7c88e98ec8f87753ab4c9cf438cff`, unchanged), proof packages P1-04/P1-05/P1-06, the P1-16 audit, the P1-17 correction log, the gap register, and the validation scripts.
**Discipline used throughout:** correctness, novelty, significance, and presentation are four different questions. Evidence for one is not evidence for another. No priority or definitive novelty claim is made here.

---

## 1. Repository verification and P1-16 → P1-17 diff

At the start of this phase the repository was synchronized: branch `arena/ab8e330d-galios-hull`, local HEAD = remote = `1d3242e`, working tree clean. The complete commit range `3c72621` (P1-16) → `1d3242e` (P1-17) changes exactly six files: the two manuscript files, `P1_17_CORRECTION_LOG.md/.pdf`, `04_BLUEPRINT_GAP_REGISTER.md`, and `ARENA_WORKLOG.md`. It does **not** touch the frozen blueprint, any proof package, the optional-corollaries file, or any validator.

Every correction claimed in the P1-17 log was verified present in the current text:

- remarks are unnumbered, and a counter simulation gives the `P=1` recovery as **Proposition 6.4** in the LaTeX, identical to the Markdown companion; all other numbers are unchanged;
- the Euclidean-dual lemma now contains the `r=0` / `s=0` boundary verification;
- §2 now defines a `λ`-constacyclic code over `A` (shift-closed `A`-submodule = ideal of `A[x]/(xⁿ−λ)`, no separability/compatibility needed) and Theorem 3.1's closing sentence was corrected accordingly;
- the conditional quantum remark now contains the rank identity `c = rank(Π ρ(Π)ᵀ) = (n−K) − H` (kernel argument), cites the Galois form [DIMP2026] within the framework of [BDS2006], and renames the distance `d_EA` as independently determined;
- [FZ2017] is inserted and cited in §1/§2; the five incomplete bibliography entries are completed; the Talbi citation scope is narrowed to the chain ring; ZKZ2026 initials are added.

**No unintended mathematical change was found.** No theorem or corollary statement (§§3–9) was altered in substance: the only statement-level touches are the definitional correction in Theorem 3.1's consequence sentence, a shorthand clarification in Theorem 5.2, boundary cases inside one proof, and the §10 conditional remark. The frozen blueprint's SHA-256 is identical before and after.

**Structural checks (this phase, on the corrected `.tex`):** braces balanced; environments matched; 33 unique labels with no missing reference; 16 bibliography entries, all cited, none undefined. **Validators re-run:** `validate_p1_05.py`, `validate_p1_06.py`, and `validate_p1_14.py` all exit 0 (`ALL … CHECKS PASSED`); the P1-14 output is again byte-identical to its saved record. These finite/symbolic checks support — they do not replace — the proofs.

## 2. What the paper actually proves

### 2.1 Standing hypotheses (every hypothesis is load-bearing)

`A ≅ ∏_{s=1}^N K_s`, `K_s = F_{q^{m_s}}` (square-free affine algebra, fixed labeled components); common `n = P·n₀` with `P = p^ϱ` and `gcd(n₀,p)=1`; the code-first `k`-Galois pairing `⟨x,y⟩_k = Σ xᵢ σ(yᵢ)` with `σ = p^k`, `ρ = σ⁻¹`; **compatible twists** `λ_s^{1+p^{d_s−k}} = 1` wherever the dual/hull are placed in the same modulus; counting over **labeled** exponent assignments `a_f ∈ {0,…,P}`.

### 2.2 The proved chain

1. **Parametrization (T1–T2).** Component codes are exactly `⟨∏ f^{a_f}⟩` for the distinct irreducible factors `f` of the separable `x^{n₀}−μ_s`; the Frobenius-twisted reciprocal `#` is multiplicative and induces the involution `τ_s` on factors under compatibility.
2. **Dual and hull in exponent form (T3–T4).** `D(C(a)) = ⟨h_a^#⟩` with dual exponents `β_i = P − α_{i−1}` (predecessor orientation fixed by the code-first pairing), and `Hull = ⟨lcm(g_a, h_a^#)⟩`, giving the local formulas `dim C = Σ w_O Σᵢ (P−αᵢ)`, `dim Hull_k = Σ w_O Σᵢ min(P−αᵢ, α_{i−1})` over `F_q`.
3. **Transfer-matrix enumerator (T5–T6, assembly).** Each `τ_s`-orbit contributes `tr(T^{(P)}_{w_O}(u,z)^{L_O})` with `T_{a,b} = u^{w(P−b)} z^{w·min(P−b,a)}`, and the global joint enumerator is the product over components and orbits: `E(u,z) = Σ_{labeled a} u^{dim C(a)} z^{dim Hull_k(a)}`. At `P=1` this is the binary simple-root specialization (Proposition 6.4).
4. **Counting corollaries (C1–C4).** Total `(P+1)^{Σ|F_s|}`; code-dimension marginal `∏_f (1+u^{w_f}+…+u^{Pw_f})`; **LCD count `2^{#orbits}`, independent of `P`** (each orbit contributes exactly its two constant tuples); self-orthogonal ⟺ `α_{i−1}+αᵢ ≥ P` on every edge and dual-containing ⟺ `≤ P`, counted by closed walks of the associated 0–1 matrices, the two counts equal.
5. **Moments (C5–C6).** Under the uniform labeled model: `E[dim C] = (n/2)Σ_s m_s`; `E[dim Hull] = ν_P·(Σ_{L=1} w_O) + μ_P·(Σ_{L≥2} w_O L_O)` with `μ_P = P(2P+1)/(6(P+1))` and the genuinely different length-one constant `ν_P = ⌊P²/4⌋/(P+1)`; `Var(dim Hull) = Σ w_O² V_{L_O}(P)` with three distinct regimes (`L=1` parity-split, `L=2`, `L≥3` via the negative adjacent covariance `κ_P`).

### 2.3 What remains conditional or outside the theorem

- **Incompatible twists:** only the two-modulus dual statement survives; no hull enumerator is asserted.
- **EAQECC remark:** conditional and finite-field only; the rank count is proved inline, but the quantum code exists only via the cited Galois-form construction and an independently determined distance `d_EA`. The enumerator alone yields no distance and no quantum parameter.
- **Moments:** statements about the uniform distribution on labeled assignments, not about codes up to equivalence/isometry.
- **N1–N3 (candidate corollaries, kept separate by instruction):** `Cov(dim C, dim Hull)=0` (uncorrelated, not independent), `Var(dim C)= [P(P+2)/12]·Σ w_f²`, and the LCD generating refinement `Σ_{a:Hull=0} u^{dim C(a)} = ∏_{s,O}(1+u^{P w_O L_O})` (of which the manuscript's C3 is the `u=1` count). These are proved and checked in `P1_15_OPTIONAL_COROLLARIES.md` / P1-14, but they are **not** results of the paper until the authors adopt them; the main text's "LCD refinement" is currently only the count, not the generating function.

## 3. Readiness evaluation (four separate axes)

| Axis | Verdict | Basis |
|---|---|---|
| **Mathematical correctness** | Strong | Complete proof packages for every statement; two independent audits (P1-14, P1-16) with hand re-derivation of the delicate points (predecessor orientation, `L=1/L=2` regimes, covariance cancellation, `w_O²` weights); exact validators re-run green this phase; formulas fenced by the correct hypotheses. Residual risk is presentational (compiled-output check), not mathematical, as far as internal review can tell. |
| **Literature novelty** | **Unresolved** | The closest item, L1 (Debnath–Prakash–Islam 2023), is verified only at abstract level ("Galois hull dimension … and the number of such codes with a given Galois hull dimension … considering some restrictions on q"); its theorem scope — hypotheses, `p|n` treatment, counting scope, any moment or joint statement — is unknown because the full text has never been lawfully available in this project. Within the *inspected* sources (affine-algebra hulls DIMP2026, multi-twisted GPM ES2026, average dimensions DP2025, small dimensions DIYP2026, chain-ring hulls Talbi2021, and the Check-D neighbours), no counterpart of the joint affine repeated-root enumerator with moments was found. "No counterpart found in inspected text" is **not** a novelty proof and must not be upgraded into one. |
| **Significance** | Moderate, specialized — defensible if positioned honestly | The contribution is a complete exact joint distribution (not just a hull formula for one code) in the repeated-root affine setting, with an orbit-local transfer mechanism, a clean LCD count independent of `P`, and exact first/second moments including the subtle `ν_P` correction. Against that: the method (transfer matrices/closed walks) is a standard enumerative technique once the local formula is known; there are no distance results, no new code constructions, and the examples are small. This is a coherent specialist-journal paper, not a breakthrough claim; its strength is completeness and exactness in a regime (repeated root × product alphabet × Galois hull) that the verified neighbours treat only partially. |
| **Presentation** | Good draft, not yet a submission | Logical arc (conventions → dual → hull → enumerator → corollaries → moments → examples → limitations) is clear; scope is honestly fenced; examples E1–E5 include field-level certificates. Blockers: author placeholder; never compiled (see §5); the Introduction's closest-neighbour discussion is necessarily abstract-level for L1; N1–N3 undecided; no target-journal formatting. |

**Overall:** the manuscript is ready for author-side compilation and reading, and its mathematical core is in good shape. It is **not submission-ready**: the unresolved L1 overlap is the single largest scientific risk (it bears on novelty and on how the Introduction may position the work), followed by compilation.

## 4. Bibliography: what each entry is asked to support, and on what evidence

"Inspected" below means: P1-17 primary-record inspection (publisher/Crossref/arXiv/MDPI/Science pages, mostly metadata+abstract) and/or the repository's earlier full-text work (P1-01/P1-09). Nothing is claimed beyond the level stated.

| Entry | Claim it supports in the manuscript | Evidence actually inspected | Status |
|---|---|---|---|
| BDS2006 | EA framework reference in the conditional remark | Science journal page + arXiv record (P1-17) | Supports the EA framework; does **not** by itself support the Galois parameter form (that rests on the inline rank proof + DIMP2026). |
| CDL2015 | Member of the "substantial literature" on repeated-root codes/duals | Crossref record + ScienceDirect page (P1-17) | Bibliography verified; only a literature-existence claim is made. |
| DP2025 | "Average Galois hull dimensions … computed" (Introduction) | Publisher/abstract level (repository record) | Supports the sentence at abstract level; also why the hull *mean* cannot be the paper's headline. |
| DIMP2026 | Affine-algebra Galois hull formulas; simple-root emphasis with repeated-root case under extra hypotheses; Galois-form EA usage in §10 | arXiv full text (P1-01/P1-09); publisher metadata (repo) | Supports these claims as arXiv statements; publisher theorem numbering never checked and never cited. |
| DIYP2026 | "Constacyclic codes with small Galois hull dimension were studied" | Publisher page/abstract level (repo) | Supports at scope level only. |
| DPI2023 (L1) | "Determined the Galois hull dimension … and the number of such codes with a given Galois hull dimension" | Abstract/metadata only (Springer/ACM/OpenAlex; repeatedly re-checked in-repo) | **Theorem-level overlap unresolved.** The sentence stays within the abstract; no non-overlap is claimed or claimable. |
| DPI2023corr | "(see also the correction)" | Correction read in repo work | Supports existence/scope of the correction only. |
| ES2026 | Generator polynomial matrices for Galois hulls of multi-twisted codes; constacyclic = index one | arXiv full text (P1-01); ScienceDirect metadata + author form (P1-17) | Supports the claim; numbering cited only in arXiv form where used internally. |
| FZ2017 | Origin of the `k`-Galois inner product (Introduction, §2) | Springer article page + citing-paper abstracts (P1-17) | Supports the attribution of the pairing `Σ xᵢ yᵢ^{p^k}`; the manuscript's code-first dual convention remains its own, not attributed to FZ. |
| HP2003, MS1977 | "Standard terminology … follows" | Standard textbooks; not re-opened this project | Low-risk background citation; no theorem is rested on them. |
| Sharma2015 | Repeated-root literature (lengths `ℓ^t p^s`, duals) | Springer article page (P1-17) | Bibliography verified; literature-existence claim only. |
| Talbi2021 | Galois hulls of cyclic serial codes over a finite chain ring | arXiv record (P1-17) | Supports the narrowed Introduction sentence. |
| WZLL2023 | Repeated-root literature (length `6ℓ^m p^n`, duals/LCD/self-dual in scope) | AIMS publisher page incl. abstract (P1-17) | Bibliography verified; literature-existence claim only. |
| ZKZ2026 | "Galois hulls have likewise been used for quantum-code constructions" | MDPI article page incl. abstract (P1-17) | Supports the existence claim; not used for the manuscript's EA parameters. |
| ZWLL2025 | Repeated-root literature (length `k^sℓ^m p^n`) | ScienceDirect page (P1-17) + Crossref | Bibliography verified; literature-existence claim only. |

Unresolved comparisons: L1 (theorem level) is the only one that can change the paper's positioning; publisher-vs-arXiv numbering for DIMP2026/ES2026 is immaterial because the manuscript cites no theorem numbers from them.

## 5. Compilation

No LaTeX compiler exists in this environment (`pdflatex`, `xelatex`, `latexmk`, `tectonic` all absent, re-checked this phase); the manuscript has therefore **not** been compiled, and this report does not claim otherwise. On the author's TeX system:

```
pdflatex -interaction=nonstopmode P1_15_MANUSCRIPT_DRAFT.tex
pdflatex -interaction=nonstopmode P1_15_MANUSCRIPT_DRAFT.tex   % second pass for \ref
```
(only `geometry`, `amsmath`, `amssymb`, `amsthm` are required.)

Likely source-level issues the structural checks cannot detect: overfull lines in the long Introduction sentences and in Example 9.3's `aligned` display; the optional-title rendering of unnumbered remarks ("Remark (conditional quantum remark)."); `2^{\#\mathrm{orbits}}` spacing; math inside hand-written bibliography titles (journal styles may restyle `\(2\ell^m p^n\)` etc.); the draft date and author placeholder; and confirmation in the compiled output that the `P=1` proposition indeed prints as Proposition 6.4 with no stray numbered remarks. Two compilation passes are needed before judging cross-references.

## 6. Smallest set of remaining actions, in priority order

1. **(Scientific blocker) Close the L1 question.** Lawfully obtain Debnath–Prakash–Islam 2023 in full and answer the standing L1-Q1–Q6 (hypotheses; `p|n`/repeated-root treatment; counting scope — labeled assignments?; any joint (dim, hull) statement; any means/variances). Then update the overlap matrix and, only if warranted, the Introduction's positioning. This is the most consequential remaining research task; everything about novelty framing waits on it.
2. **(Author) Compile and proofread** with §5's instructions; fill authors/affiliations; verify Proposition 6.4 and references in the compiled PDF.
3. **(Author decision) N1–N3 adoption.** Adopting N3 (LCD generating refinement) and N1+N2 (complete second-order picture) would measurably strengthen §7–§8 at low cost; rejection is also safe since nothing depends on them.
4. **(After 1) Position and pick the venue.** Rewrite the closest-work paragraph using verified theorem-level comparisons only, choose the target journal, and apply its bibliography style.
5. **(Optional, later — not required now)** Research extensions the draft already names (incompatible-twist hull intersection; equivalence-class counting; distance-aware refinements) are new projects, not readiness fixes, and should not delay 1–4.

## 7. Files and blockers

- Created: `P1_18_READINESS_AND_RESEARCH_PRIORITIES.md` (this report; PDF rendered from it for reading).
- Updated: `04_BLUEPRINT_GAP_REGISTER.md`, `ARENA_WORKLOG.md` (P1-18 outcome).
- Unchanged: manuscript, frozen blueprint (hash in §1), proof packages, optional corollaries, validators.
- Remaining blockers: L1 full text unavailable (novelty unresolved); no LaTeX compiler in this environment; author placeholder and N1–N3 decision outstanding.
