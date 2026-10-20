# CITATION_LEDGER

Every citation that appears in a project document, with what it is cited **for** and
whether that use is supported by what was actually read. This ledger exists so that
no claim in this project rests on a reference that was never opened.

**Legend.** Verification level: **A** full text · **B** abstract/metadata ·
**C** metadata only · **D** unverified. Use type: `fact` (a statement about the
world), `method` (a technique attributed to the work), `precedent` (a claim that the
work already contains a result), `context` (background).

**Rule applied throughout.** A reference may be used as a `precedent` only at the
level at which it was read. A `B`-level abstract that says "we count the number of
codes" is sufficient to support "this paper counts codes"; it is **not** sufficient
to support "this paper's theorem has such-and-such hypothesis".

---

## 1. Load-bearing citations — the novelty argument depends on these

| Ref | Cited in | Cite as | Use | Level | Is the cited use supported? |
|---|---|---|---|---|---|
| `[D23]` | `NOVELTY_ASSESSMENT.md` §1.2, §4; `JOINT_ENUMERATOR_FEASIBILITY.md` §1.2; `LITERATURE_MAP.md` stratum A | the number of constacyclic codes over `F_q` of a given Galois hull dimension is calculated, under restrictions on `q` | precedent | **B** | **Yes.** The sentence is in the abstract, verbatim. The *nature* of the restrictions is **not** supported and is not claimed. |
| `[D23c]` | `REFERENCE_VERIFICATION_REPORT.md` §2 | correction to `[D23]`; changes `i₁ ≤ i₂` to `i₁ < i₂`; proves `f_{i₁}^# ≠ f_{i₂}^#` | fact | **B** | **Yes**, at abstract level. Its *consequences* for `[D23]`'s counts are not asserted. |
| `[S25]` | `NOVELTY_ASSESSMENT.md` §1.2; `JOINT_ENUMERATOR_FEASIBILITY.md` §1.3; `LITERATURE_MAP.md` stratum B | over `Z_pZ_p[v]`: hull generating functions (Thm 3.5), enumeration of separable cyclic codes with fixed hull dimension (Thm 3.7, Cor 3.8), non-separable case (Thm 4.10) | precedent | **B+** | **Yes.** Theorem and corollary numbers appear in the retrieved full-text excerpts. |
| `[SJL15]` | `NOVELTY_ASSESSMENT.md`; `LITERATURE_MAP.md` stratum A | enumerations of cyclic and negacyclic codes with a given Euclidean/Hermitian hull dimension over `F_q` | precedent | **B** | **Yes**, abstract. Note the scope limit: cyclic and negacyclic, not general constacyclic. |
| `[S1]` | throughout | Theorems 2, 3, 6, 7, 8, 10; Lemma 9; Conclusion; Examples 1–3; Table 1 | fact + precedent | **A** | **Yes** — full text read, and the load-bearing computations independently reproduced. |
| `[Y2024]` | `SOURCE_PAPER_METADATA.md`; `REFERENCE_VERIFICATION_REPORT.md` §1 | `R_e = F_{q²}+uF_{q²}+…+u^{e−1}F_{q²}`, `u^e=1`, `e|(q+1)`; possible Hermitian hull dimensions; LCD conditions; quantum codes; **no** enumeration claim | fact | **B** | **Yes**, abstract. The absence of an enumeration claim is supported by the abstract *and* by `[S1]`'s own description of it. |
| `[LSL25]` | `LITERATURE_MAP.md` stratum F; `RESEARCH_DIRECTION_DECISION.md` §C1 | closed mass formula for linear codes with a prescribed hull dimension (IEEE TIT 71(1) 2025, 273–286) | precedent | **B** | **Yes**, abstract. It counts *linear* codes, not constacyclic ones, and does not work over a product ring. |
| `[CFLL12]` | `LITERATURE_MAP.md` stratum F; `RESEARCH_DIRECTION_DECISION.md` §C1 | `n`-isometry / `n`-equivalence introduced to classify constacyclic codes; `gcd(n,q−1)` `n`-equivalence classes of shift constants | precedent | **A** | **Yes**, publisher abstract and full-text excerpt. |
| `[ISO24]` | `RESEARCH_DIRECTION_DECISION.md` §C1 | numbers of `n`-isometry / `n`-equivalence classes over finite chain rings | precedent | **B** | **Yes**, abstract. |
| `[Che23]` | `RESEARCH_DIRECTION_DECISION.md` §C1.2 | hull dimension can change under equivalence for `q = 2, 3` | fact | **C** | **Partially** — cited at second hand from two 2025–26 papers. Flagged, not relied on. |
| `[DP25]` | `NOVELTY_ASSESSMENT.md` §3; `LITERATURE_MAP.md` stratum B | `R_{m,q} = F_q[u]/⟨u^m−u⟩`; average Galois hull dimensions over `F_q` and over `R_{m,q}`; Galois-LCD construction | precedent | **B** | **Yes**, abstract. |

## 2. Supportive citations — used for `method`, `context`, or `fact` not under dispute

| Ref | Used for | Level |
|---|---|---|
| `[Liu18]` | source of `[S1]` Lemma 1 and Theorem 1 (Galois LCD codes) | C |
| `[FZ17]` | introduction of the Galois inner product | C |
| `[LP20]` | Galois hulls over finite fields | C |
| `[Cao21]` | source of `[S1]` Lemma 7 (EAQECC from a hull) | C |
| `[LA18]` | source of `[S1]` Lemma 8 (the `d ≤ (n+2)/2` bound) | C |
| `[Y24b]` | source of `[S1]` Lemma 2 and Theorem 4 (polyadic codes over affine algebras) | C |
| `[TG24]` | non-chain ring `F_q+vF_q`, Euclidean and Hermitian hulls, QECCs; no enumeration | B |
| `[GWF23]` | double cyclic codes over `Z_2`: hull generating functions + fixed-dimension counts | B |
| `[DP25b]` | `Z_{p²}` separable double cyclic codes: fixed-`p`-dimension counts | B |
| `[LGM25]` | `Z_4` double cyclic codes: fixed-2-dimension counts, average 2-dimension | B |
| `[LYL26]` | product-form Hermitian hull-codimension enumerator over `F_{q²}`, mean/variance | A (intro) |
| `[Ent26]` | `ℓ`-Galois hulls over a finite non-chain ring, Construction X, EAQECCs; no enumeration | B |
| `[arXiv:2606.22069]` | separable constacyclic codes over `F_q×(F_q+vF_q)`: hulls and sums; no enumeration | A (intro) |
| `[JLS18]` | average Hermitian hull dimension over `F_{q²}` | B |
| `[Ske03]` | average hull dimension of cyclic codes | C |
| `[Sen97]` | asymptotic distribution of hull dimension | B |
| `[DS25]` | number of codes over rings of order 4 with a hull of given **type** | C |
| `[TBM22]` | hulls of cyclic serial codes over a finite chain ring | C |
| `[JS20]` | hulls of cyclic codes over `F_2+vF_2` | C |

## 3. Citations that appear in no project document
`[S1]`'s remaining references (44 total) are listed in
`REFERENCE_VERIFICATION_REPORT.md` §4 and are **not** cited anywhere in this
project. Nothing here depends on them.

## 4. Known citation risks

| Risk | Mitigation taken |
|---|---|
| `[D23]` is paywalled; only its abstract was read | used only at abstract level; the `q`-restriction is described as unknown (`U`), never as a specific condition |
| `[D23]` has a published correction | both the paper and the correction are recorded; the correction's content is reported only at abstract level |
| `[S25]`'s theorem numbering is from a retrieved excerpt, not a re-typeset copy | cited as "Thm 3.7 / Cor 3.8" with the caveat that this is the publisher's HTML excerpt |
| arXiv IDs `2606.22069`, `2607.12242` are 2026-dated and were retrieved as web pages | cited as `[OPEN]`/`precedent` only for their stated scope; no theorem statement of theirs is relied on |
| Two references share the visual label `[DP25]`/`[DP25b]` | disambiguated by suffix throughout |
| The blueprint's own citations were not independently checked | out of scope; the blueprint's named source was checked and found to be a different paper (`SOURCE_PAPER_METADATA.md` §2) |

## 5. Statement of integrity

No citation in this project was invented. No DOI was written from memory: every DOI
in `REFERENCE_VERIFICATION_REPORT.md` was either returned by a search result or
appeared in the reference list of `[S1]`. Where a reference could not be opened, that
fact is stated at the point of use rather than hidden in a bibliography.
