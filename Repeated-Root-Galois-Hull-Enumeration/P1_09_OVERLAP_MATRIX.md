# P1-09 — Claim-by-Claim Overlap Matrix

**Date:** 21 October 2026  
**Companion:** `P1_09_GATE_G1_NOVELTY_AUDIT.md` (§2–§4 give the reasoning; this file is the matrix + per-source record).  
**Rules:** repo labels L1–L10 as in `01_LITERATURE_AUDIT.md` / `P1_01_FULL_TEXT_THEOREM_EXTRACTION.md` §0. “Verified” = seen in lawfully accessed text (full text or abstract/metadata, marked). “In inspected text” for absences refers only to the texts actually read (arXiv full texts for L4/L8; abstracts/publisher pages for the rest). Inaccessibility is never treated as absence.

**Legend:** ● = present (verified), ◐ = partial/related or abstract-level only, ? = unresolved, — = not present in the inspected text, n/a = not applicable.

Our claims (corrected blueprint, frozen 21 Oct 2026, commit `1c67fda` blueprint content):
- **K1** Hull generator + dimension at exponent level, repeated-root (`n = Pn_0`, `p | n` allowed), compatible twists (T3/T4).
- **K2** Joint `(dim_{F_q} C, dim_{F_q} Hull_k)` enumerator over **labeled** assignments over `A = ∏ K_s` (T6).
- **K3** Per-orbit transfer-matrix trace formula (T5).
- **K4** LCD count `2^{#orbits}` (C3); self-orthogonal/dual-containing criteria + closed-walk counts (C4).
- **K5** Mean formulas: corrected hull-mean split (C5 as corrected by PC-1) and code-dimension mean.
- **K6** Variance closed forms in `P` for `L = 1, 2, ≥ 3` (C6 as integrated from P1-06).
- **K7** `P = 1` recovery of the simple-root formulas (Gate-G3 identity).

| Claim | L1 (finite-field, 2023) | L2 (average dims) | L3 (small hull dims) | L4 (affine, arXiv full text) | L8 (multi-twisted, arXiv full text) | L9/L10 & Check-D neighbours |
|---|---|---|---|---|---|---|
| K1 hull generator/dimension, repeated-root | ? (abstract: hull-dimension formula exists; scope/hypotheses unseen) | — (averages, not per-code formula) | ◐ (conditions for dim 1, 2 incl. `p | n` cases; not the general exponent formula) | ◐/● (hull generator + dimension formula over `A`; repeated-root Thm. under extra `ord λ` hypotheses, simple-root idempotent framework) | ◐ (GPM hull dimension formulas, twisted setting; not our affine exponent lattice) | ◐ (repeated-root hull/LCD literature at publisher-scope level) |
| K2 joint enumerator, labeled, affine product | ? (abstract: “count of codes for given hull dimension” — joint vs marginal unseen) | — | — | — (counts of attainable dimension *values*; code enumeration over `A` left open in its conclusion) | — (not in inspected text) | — (joint *weight* enumerators of LCD pairs etc. are different objects) |
| K3 transfer-matrix trace per orbit | ? | — | — | — | — | — |
| K4 LCD / self-orth. counts & criteria | ? | — | ◐ (small-dim existence, not counts) | ◐ (LCD **condition**; not our labeled count `2^{#orbits}`) | ◐ (LCD-type results in GPM setting) | ◐ (LCD enumerations in other models, e.g. serial rings) |
| K5 means | ? (no mean in abstract) | ● (average Galois hull dimensions over finite fields / `R_{m,q}` — abstract verified; different model, mean as headline there) | — | — | — | ◐ (classical hull-average literature) |
| K6 variance in `P` | ? | ? (variance not verified) | — | — | — | — |
| K7 `P = 1` recovery | n/a | n/a | n/a | n/a (their setting is simple-root; our `P=1` case is a specialization, not their theorem) | n/a | n/a |

## Per-source record

### Repo L1 — Debnath, Prakash & Islam, “Galois hulls of constacyclic codes over finite fields”, *Cryptogr. Commun.* 15(1), 111–127 (2023). DOI `10.1007/s12095-022-00591-6`; correction DOI `10.1007/s12095-022-00602-6`, 15, 129–130. zbMATH Zbl 1518.94136 / correction Zbl 1518.94137. OpenAlex `W4283360609`; Semantic Scholar CorpusId `250008629`.
- **Verified (abstract/metadata level only):** the paper “presents a formula for the dimension of Galois hulls of constacyclic codes” (Springer abstract snippet, lawful page, re-read 21 Oct 2026) and, per its abstract as recorded in P1-01 §5.1 and corroborated by the introduction of repo L4 (ScienceDirect snippet: “They also counted the number of constacyclic codes of a given Galois hull dimension”), a count of codes by hull dimension. Authors/affiliation (IIT Patna), pages, dates verified via OpenAlex/Semantic Scholar (fresh 21 Oct 2026 responses: `is_oa = false`, `any_repository_has_fulltext = false`, `openAccessPdf` empty).
- **Not verified:** every theorem statement and hypothesis — in particular: whether `p | n` (repeated roots) is included or excluded; whether the count is of labeled codes, of codes with a given hull dimension only (marginal), or joint in `(dim C, dim Hull)`; the orbit/factor bookkeeping (cf. `B_i` sets in the correction); restrictions on `q, k, λ`.
- **Shared vs different:** potentially shares K1’s finite-field specialization and some counting territory (K2/K4 territory cannot be excluded). Even in the worst case for us, L1 is finite-field only (title/abstract), so K2’s affine-product assembly, K3, K5’s corrected split in `P`, and K6 have no counterpart *in the verified record* — but that record is incomplete.
- **Status: UNRESOLVED.** Exact comparison impossible until a lawful full text is read. This single source blocks Gate G1 closure.

### Repo L2 — “Average dimensions of Galois hulls of constacyclic codes”, *Adv. Math. Commun.* DOI `10.3934/amc.2025010`; Zbl 1579.94062.
- **Verified (abstract):** formulas for average dimensions of Galois hulls of constacyclic codes over finite fields (and, per the paper’s scope as recorded in P1-01 §6.3, related ring cases). 
- **Shared/different:** shares the *topic* of hull means (K5) but in the finite-field (and `R_{m,q}`) model with the mean as headline; our C5 is a corollary of the joint enumerator in the repeated-root affine labeled model, with the `L = 1`/`L ≥ 2` split. No joint enumerator, transfer trace, or `P`-variance verified.
- **Status: PARTIAL (abstract-level).** Consequence already locked (GAP-12): the mean must never be our headline novelty.

### Repo L3 — “Study of small Galois hull dimensions of constacyclic codes”, *Adv. Math. Commun.* DOI `10.3934/amc.2025054`.
- **Verified (publisher page/table):** conditions for Galois hull dimensions `1` and `2`, including cases with `p | n` (Table 1 conditions, e.g. `ord(α) | (1 + p^{e−ℓ})`, `α^n = λ`; fetched snippet 21 Oct 2026 records “Thm. 3.9” **as displayed on that publisher page**).
- **Shared/different:** overlaps K1 only in the small-dimension corner (`dim Hull ∈ {1, 2}` existence/conditions). No enumerator, counts of all codes, transfer traces, or moments.
- **Status: PARTIAL (publisher-page level).** Consequence: we may not claim to be first to treat repeated-root hulls or small hull dimensions.

### Repo L4 (command “L1”) — Debnath, Islam, Martínez-Moro & Prakash, “Galois hulls of constacyclic codes over affine algebra rings”, *Discrete Math.* 349(2) (2026), Art. 114750. DOI `10.1016/j.disc.2025.114750`; arXiv `2412.08512` (full text inspected in P1-01); Zbl 1582.94185.
- **Verified (arXiv full text; P1-01 §3):** square-free affine algebra `A`; candidate-first pairing convention (differs from ours — convention is not contribution); hull via component idempotent generators `Σ e_s·lcm(g, h^#)`-type formula; hull-dimension formula; a repeated-root extension theorem (arXiv Thm. 8 in P1-01’s extraction) under additional hypotheses (`gcd(ord λ, n′) = 1`, `ord λ | 1 + p^{e−k}`-type conditions); hull generator `Σ e_{S(ν)} lcm(g, h^#)` over components (Thm. 7, arXiv numbering), Galois dual generator (Thm. 5); counts of **attainable hull-dimension values** (Cor. 3.5), not of codes; its conclusion (§5) leaves enumeration of codes over `A` open.
- **Shared vs different:** shares the affine setting and hull-generator/dimension territory (K1 partially — under different hypotheses and a semisimple/idempotent method that does not apply to our non-reduced quotient `K_s[x]/(x^n − λ_s)` when `P > 1`). Does **not** contain (in inspected text): our exponent-lattice parametrization of *all* codes for `P > 1` with the transfer trace (K2/K3), labeled joint enumerator, C3/C4 counts, K5/K6 moments.
- **Status: VERIFIED at arXiv full-text level; publisher-version equivalence unverified (metadata/snippet consistency only).** Consequence: K1 alone cannot be sold as the novelty; the enumerator/transfer/moments must carry the claim, with L4 cited and contrasted.

### Repo L8 (command “L4”) — Ramy Abu Eldin & Patrick Solé, “Generator polynomial matrices of the Galois hulls of multi-twisted codes”, *Finite Fields Appl.* 109 (2026), Art. 102712. DOI `10.1016/j.ffa.2025.102712`; arXiv `2305.15237` (full text inspected in P1-01 §4); Zbl 1576.94064.
- **Verified (arXiv full text, arXiv numbering):** Galois hull machinery for multi-twisted (GPM) codes — hull-dimension via generator-matrix rank (Thm. 8), Galois dual twist type (Thm. 9), Euclidean-dual GPM relation (Thm. 10), hull type under `Λ^{−p^{−κ}} = Λ` (Cor. 11), determinantal-divisor hull dimension (Thm. 25), GPM for the hull (Thm. 28), LCD/self-orthogonal criteria (Cors. 26/29); candidate-first pairing; constacyclic codes are the index-1 case and no general `gcd(m_j, p) = 1` restriction was found in the inspected text. Publisher numbering demonstrably differs from arXiv (P1-02 §2.2), so only arXiv numbering is ever quoted here.
- **Shared vs different:** shares hull-dimension technology in a different code family; no joint `(dim, hull)` enumerator over an affine exponent lattice, no per-orbit transfer trace, no `P`-moments in the inspected text.
- **Status: VERIFIED at arXiv full-text level (publisher equivalence unverified).**

### Repo L9/L10 and Check-D neighbours (publisher-scope / abstract level; P1-01 §6.4, P1-02 §3)
- Repeated-root constacyclic hull/LCD literature exists (publisher-scope records), so “repeated-root hulls are untouched” would be false. Classical hull enumeration/averages (Sendrier–Skersys tradition), joint *weight* enumerator of an LCD code and its dual (arXiv:1511.08889), DC/FC hull-dimension enumeration (arXiv:2307.05449), and hull enumeration over serial rings are **different objects** from K2/K3; none, in the inspected records, gives the labeled affine repeated-root joint `(dim C, dim Hull)` transfer-trace enumerator.
- **Status: PARTIAL (scope-level).** Databases searched (P1-02 Check D, re-confirmed with a fresh targeted search 21 Oct 2026 that returned no counterpart): arXiv, zbMATH Open, OpenAlex, Semantic Scholar, publisher pages. **Not searched: MathSciNet, Scopus, Web of Science** (no lawful workspace access). Coverage is non-exhaustive; non-discovery is not novelty.

## Matrix conclusion

No inspected source contains K2+K3 (joint labeled affine repeated-root enumerator by transfer traces) or K6 (variance in `P`), and K5 is headline-owned by L2 in its own model. K1 is substantially pre-occupied (L4 verified; L1 unresolved). The defensible contribution centre is therefore **K2 + K3 + K6 (with K4/K5 as corollaries)** — subject to the L1 caveat, which is exactly why Gate G1 cannot yet close (see the companion audit).
