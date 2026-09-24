# Phase-7 Final Reference Audit

**Audit date:** 2026-09-24
**Branch:** `arena/01a0c9d2-galios-hull`
**Purpose:** final source, DOI, metadata, convention, and manuscript-use audit for the literature that may appear in the manuscript specification.

## 1. Decision rule

This audit records what was actually checked on publisher pages, the accessible preprint, and the supplied local source PDF. A title, abstract, search result, citation record, or DOI does not establish theorem-level transfer. The final manuscript may use a source for the precise purpose listed in the last column only.

The literature-status vocabulary in this final audit is restricted to:

`VERIFIED`, `VERIFIED WITH CONVENTION TRANSFORMATION`, `PARTIALLY VERIFIED`, `METADATA ONLY`, `CONVENTION MISMATCH`, `SOURCE UNAVAILABLE`, `DOI UNVERIFIED`, and `VERIFY BEFORE MANUSCRIPT FINALIZATION`.

The final-reference audit does not claim that the accessible record is the final publisher proof. In particular, the final publisher full text of the primary 2026 article and the corrected full text of the 2023 finite-field article were not accessible in this checkout. The readable arXiv preprint is therefore recorded separately from the final publisher record.

## 2. Source-access record

### 2.1 Primary affine-algebra article

The publisher page was opened directly at [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0012365X25003589?via%3Dihub). It exposes the title, authors Indibar Debnath, Habibul Islam, Edgar Martínez-Moro, and Om Prakash; *Discrete Mathematics*, volume 349, issue 2, February 2026, article 114750; DOI `10.1016/j.disc.2025.114750`; the abstract; introduction; and section snippets. The publisher page requires institutional access or purchase for the complete article.

The readable theorem-bearing record is [arXiv:2412.08512](https://arxiv.org/html/2412.08512), version 1 dated 2024-12-11. Its displayed Section 2.2 convention, Lemma 1, Theorem 1, affine Theorems 4, 5, 7, and 8, and quantum section were inspected. The supplied local PDF was also checked by `validation/source_pdf_theorem_check.py`; its SHA-256 is recorded in the Phase-6 evidence. These are independent source records, but they do not remove the need to check the final/corrected publisher text before submission.

### 2.2 Final reference table

| ID | Bibliographic record and source | Evidence actually checked | Final status | Safe manuscript use |
|---|---|---|---|---|
| R1 | I. Debnath, H. Islam, E. Martínez-Moro, and O. Prakash, “Galois hulls of constacyclic codes over affine algebra rings,” *Discrete Mathematics* 349(2) (2026), Article 114750. [Publisher record](https://www.sciencedirect.com/science/article/abs/pii/S0012365X25003589?via%3Dihub), DOI `10.1016/j.disc.2025.114750`. | Direct publisher metadata, abstract, introduction, and section snippets; complete final text not accessible. | `VERIFIED` | Use for the broad square-free affine-algebra hull scope and bibliographic identity. Do not cite the final record as exact support for the frozen code-first theorem without the transformation note below. |
| R2 | I. Debnath, H. Islam, E. Martínez-Moro, and O. Prakash, “Galois hulls of constacyclic codes over affine algebra rings,” arXiv:2412.08512v1 (2024-12-11). [Readable HTML](https://arxiv.org/html/2412.08512). | Readable theorem-bearing preprint: pairing, dual definition, reciprocal/twist formulas, affine decomposition, hull statements, and quantum section. | `VERIFIED` | Use as the exact accessible record for source convention and displayed source formulas, always with the candidate-first/code-first warning. |
| R3 | I. Debnath, O. Prakash, and H. Islam, “Galois hulls of constacyclic codes over finite fields,” *Cryptography and Communications* 15 (2023), 111–127. [Springer record](https://link.springer.com/article/10.1007/s12095-022-00591-6), DOI `10.1007/s12095-022-00591-6`. | Publisher metadata, abstract, publication data, and correction link. The abstract supports a finite-field hull formula and restricted fixed-dimension counts; complete article not accessible. | `PARTIALLY VERIFIED` | Cite only for finite-field background at abstract scope. The corrected full theorem and hypotheses require a pre-submission check. |
| R4 | I. Debnath, O. Prakash, and H. Islam, “Correction to: Galois hulls of constacyclic codes over finite fields,” *Cryptography and Communications* 15 (2023), 129–130. [Correction record](https://link.springer.com/article/10.1007/s12095-022-00602-6), DOI `10.1007/s12095-022-00602-6`. | Direct correction record and bibliographic data. | `VERIFIED` | Record the correction in the bibliography and do not quote an uncorrected theorem from R3. Exact corrected content still requires access before theorem-level attribution. |
| R5 | E. Sangwisut, S. Jitman, S. Ling, and P. Udomkavanich, “Hulls of cyclic and negacyclic codes over finite fields,” *Finite Fields and Their Applications* 33 (2015), 232–257. [Publisher record](https://www.sciencedirect.com/science/article/pii/S107157971400166X), DOI `10.1016/j.ffa.2014.12.008`. | Open publisher page, authors, DOI, abstract, outline, Theorem 1, Theorem 2, Lemma 3, and introductory scope. | `VERIFIED` | Use for the verified cyclic/negacyclic Euclidean and Hermitian hull and fixed-dimension enumeration background. It is not evidence for the affine product or the present bivariate transfer theorem. |
| R6 | S. Jitman and E. Sangwisut, “The average dimension of the Hermitian hull of constacyclic codes over finite fields of square order,” *Advances in Mathematics of Communications* 12(3) (2018), 451–463. [AIMS record](https://www.aimsciences.org/article/doi/10.3934/amc.2018027), DOI `10.3934/amc.2018027`. | Publisher metadata, authors, abstract, and introduction; full text is access restricted. | `PARTIALLY VERIFIED` | Use for average Hermitian-hull context only. Do not import its average formula into the present labeled joint enumerator. |
| R7 | P. Liu and Y. Pan, “Galois hulls of linear codes over finite fields,” *Designs, Codes and Cryptography* 88 (2020), 241–255. [Springer record](https://link.springer.com/article/10.1007/s10623-019-00681-2), DOI `10.1007/s10623-019-00681-2`. | Publisher metadata, abstract, publication data, and accessible reference list. | `PARTIALLY VERIFIED` | Use for general Galois-hull, permutation-invariance, and Gram-matrix context; it is not a constacyclic factor-selection enumeration theorem. |
| R8 | I. Debnath and O. Prakash, “Average dimensions of Galois hulls of constacyclic codes,” *Advances in Mathematics of Communications* 19(6) (2025), 1569–1604. [AIMS record](https://www.aimsciences.org/article/doi/10.3934/amc.2025010), DOI `10.3934/amc.2025010`. | Publisher metadata, authors, abstract, and introduction. The complete HTML is access restricted. | `PARTIALLY VERIFIED` | Use for finite-field and `R_{m,q}` average-dimension background only. |
| R9 | S. Yadav, A. Singh, H. Islam, O. Prakash, and P. Solé, “Hermitian hull of constacyclic codes over a class of non-chain rings and new quantum codes,” *Computational and Applied Mathematics* 43 (2024), Article 269. [Springer record](https://link.springer.com/article/10.1007/s40314-024-02789-1), DOI `10.1007/s40314-024-02789-1`. | Publisher metadata, author record, abstract, and stated non-chain-ring/Hermitian scope. | `PARTIALLY VERIFIED` | Use only as a narrower Hermitian non-chain-ring comparison; keep quantum conclusions conditional. |
| R10 | Y. Fan and L. Zhang, “Galois self-dual constacyclic codes,” *Designs, Codes and Cryptography* 84(3) (2017), 473–492. [Springer DOI record](https://doi.org/10.1007/s10623-016-0282-8), DOI `10.1007/s10623-016-0282-8`. | DOI and bibliographic identity are present in the accessible publisher reference material; the article abstract/full text was not independently opened. | `METADATA ONLY` | Use only as a bibliographic lead for Galois constacyclic background, not as theorem evidence. |
| R11 | K. Guenda, S. Jitman, and T. A. Gulliver, “Constructions of good entanglement-assisted quantum error correcting codes,” *Designs, Codes and Cryptography* 86(1) (2018), 121–136. [Springer DOI record](https://doi.org/10.1007/s10623-017-0330-z), DOI `10.1007/s10623-017-0330-z`. | DOI record and cited relationship between classical hulls and EAQECC constructions. | `PARTIALLY VERIFIED` | Mention only for conditional quantum motivation; independently verify every quantum construction and parameter before inclusion. |
| R12 | S. Jitman and E. Sangwisut, “Hulls of cyclic codes over `F_2+vF_2`,” *Thai Journal of Mathematics* 18 (2020), 135–144. | Source bibliography identifies the record, but no confirmed DOI was found in the direct checks. | `DOI UNVERIFIED` | Omit from the manuscript bibliography unless the journal record and DOI are independently confirmed. |
| R13 | T. Tian, X. Gao, and X. Gao, “Hulls of constacyclic codes over finite non-chain rings and their applications in quantum codes construction,” *Quantum Information Processing* 23 (2024), Article 9, DOI `10.1007/s11128-023-04230-8`. [Springer DOI record](https://doi.org/10.1007/s11128-023-04230-8). | DOI/title record and related-paper metadata; full theorem comparison not independently read. | `METADATA ONLY` | Keep outside the core literature argument unless the publisher record is checked directly. |
| R14 | Local supplied source PDF, “Galios hulls of constacclic codes over affine algebra rings.” | File presence, SHA-256, and structural theorem/convention markers checked by `validation/source_pdf_theorem_check.py`; filename is malformed and publisher-final identity is not inferred from the filename. | `VERIFIED` | Retain as an audit input only. Cite R2/R1 for bibliographic identity; do not cite the malformed filename as a publication record. |

## 3. Convention and transfer conclusions

1. R1 and R2 support the broad subject: square-free affine algebras, component/idempotent decompositions, Galois duals and hulls, hull dimensions, LCD conditions, and conditional quantum examples.
2. R2 visibly defines its comparison dual with the candidate in the first slot, while the frozen manuscript convention places the code in the first slot and applies `sigma` to the candidate. The exact relation retained in the manuscript is
   `D_candidate(C) = sigma_k^2(D_code-first(C))`.
3. The displayed inverse-Frobenius reciprocal and twist in R2 agree with the frozen code-first formulas only after the explicit convention transformation and component exponent replacement `e -> d_s=e m_s`. They are not a literal transfer from the displayed candidate-first definition when `sigma_k^2` is nontrivial.
4. R5 verifies classical cyclic/negacyclic hull and fixed-dimension results, including an lcm intersection mechanism in its displayed setting. Its hypotheses do not establish the present square-free affine, extension-component, code-first, bivariate product.
5. R3, R6, R7, R8, and R9 are related background records. They do not independently establish the present labeled `u,z` transfer-matrix product.
6. No source checked in this audit establishes, or disproves, the exact present contribution package. The manuscript therefore uses `NOT ESTABLISHED` as a novelty conclusion in `NOVELTY_BOUNDARY.md`, not a priority claim.

## 4. Required final-manuscript reference policy

- Keep R1 and R2 separate: the publisher record is the final bibliographic record, while R2 is the accessible theorem-bearing preprint.
- Cite the source convention and the convention transformation explicitly; never identify candidate-first and code-first dual codes or hull subspaces.
- Include R4 whenever R3 is cited.
- Do not use R10, R12, or R13 as theorem evidence without a fresh direct check; R12 has no confirmed DOI.
- Do not cite a source for a theorem number unless the cited version has been directly read and the theorem number is confirmed.
- The final manuscript reference list must not contain guessed DOI, publisher outcome, priority, quantum distance, equivalence count, or unverified numerical data.

## 5. Final reference-audit decision

The bibliographic identity and broad abstract scope of the primary article are now verified, and several related publisher records were independently checked. The central theorem-level transfer remains conditional because the final/corrected source texts are not fully accessible and because the readable primary record requires the explicit slot-convention transformation. The manuscript-readiness verdict therefore remains:

> **NOT READY — MATERIAL GAPS REMAIN**

## 6. Phase-8 source additions

The Phase-7 source records above remain unchanged. Phase 8 additionally inspected the following theorem-bearing or publisher-level records:

| Source | Phase-8 evidence | Safe use |
|---|---|---|
| Talbi–Batoul–Fotue Tabue–Martínez-Moro, arXiv:2102.06995, [HTML](https://arxiv.org/html/2102.06995) | Readable theorem text through Proposition 8: cyclic serial finite-chain-ring hull parameters and fixed-`q`-dimension counts. | Strong adjacent enumeration; chain-ring hypotheses must remain explicit. |
| Zhang–Kong–Zheng, *Entropy* 28 (2026), DOI [10.3390/e28040407](https://doi.org/10.3390/e28040407), [full text](https://www.mdpi.com/1099-4300/28/4/407) | Open full text: restricted CRT/direct-product non-chain ring, code-first-looking Galois dual, component hull decomposition, lcm generator, Gram-rank dimensions. | Adjacent structural comparison; no central labeled enumerator or unconditional quantum transfer. |
| Aliabadi–Kalaycı–Zadehdabbagh, *Cryptography and Communications* 18 (2026), DOI [10.1007/s12095-025-00861-z](https://doi.org/10.1007/s12095-025-00861-z) | Open article with prescribed Euclidean-hull enumeration for double and four circulant codes. | Counterevidence to broad enumeration novelty; different code family. |
| Gao–Wu–Fu, *Finite Fields and Their Applications* 88 (2023), DOI [10.1016/j.ffa.2023.102189](https://doi.org/10.1016/j.ffa.2023.102189) | Publisher abstract and theorem preview: fixed-hull enumeration for double cyclic codes over `Z_2`. | Adjacent generalized-cyclic background only. |
| Debnath–Prakash, *Advances in Mathematics of Communications* 19 (2025), DOI [10.3934/amc.2025010](https://doi.org/10.3934/amc.2025010), and Debnath–Islam–Yadav–Prakash, DOI [10.3934/amc.2025054](https://doi.org/10.3934/amc.2025054) | Publisher records for average-dimension and small-dimension Galois-hull constacyclic results. | Scope/background only; full theorem text is restricted. |
| Transfer-matrix reference, [Combinatorics Notes](https://seragunn.github.io/combinatorics-notes/regular-languages/transfer-matrix.html) | Theorem 24.1/24.2: matrix powers count walks and generating functions; cyclic closure uses the closed-walk trace identity. | Standard combinatorial tool; not evidence of a hull theorem. |

The final publisher text of the primary affine article and the corrected finite-field constacyclic article remain `SOURCE UNAVAILABLE` for complete theorem-level transfer. This limitation is carried into the Phase-8 audit rather than hidden.
