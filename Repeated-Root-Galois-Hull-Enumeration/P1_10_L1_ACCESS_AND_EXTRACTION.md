# P1-10 — Lawful L1 Full-Text Acquisition Plan and Theorem-Level Extraction

**Command:** P1-10 — Lawful L1 Full-Text Acquisition Plan and Theorem-Level Extraction  
**Date:** 21 October 2026  
**Outcome in one line:** No lawful full text of repo L1 was obtained in this command. **No author, librarian, or any other person was contacted** — no communication tool was used; §6 contains drafts for the Boss to send. All L1 theorem-level comparisons remain **UNRESOLVED** (§5), Gate G1 remains **DEFERRED**, and the recommendation for the novelty claim is **DEFER** (no novelty claim may be made at present).

---

## 1. Repository state (verified before work)

- Branch `arena/ab8e330d-galios-hull`; local HEAD = remote ref = `84ffa46223784b0df6ce54c25d22cf9add08123e` (“P1-09: Gate G1 novelty audit”); working tree clean; no reset, no history rewrite.
- Frozen blueprint `02_THEOREM_BLUEPRINT.md` SHA-256: `ec2fd8d58f8d2a986314f83997d750d689f7c88e98ec8f87753ab4c9cf438cff` (identical to the P1-08 after-hash and the P1-09 verification).
- Read for this command: `P1_09_GATE_G1_NOVELTY_AUDIT.md`, `P1_09_OVERLAP_MATRIX.md`, `04_BLUEPRINT_GAP_REGISTER.md` (GAP-01/06/16/17 and P1-08/P1-09 outcomes), `02_THEOREM_BLUEPRINT.md` (corrected freeze, unedited here).

## 2. Repo L1 — exact identification (verified identifiers only)

| Field | Value (source) |
|---|---|
| Title | “Galois hulls of constacyclic codes over finite fields” (Springer; OpenAlex `W4283360609`) |
| Authors | Indibar Debnath; Om Prakash (corresponding author per OpenAlex); Habibul Islam — all Dept. of Mathematics, IIT Patna, Patna 801106, India |
| Journal | *Cryptography and Communications*, Springer, ISSN 1936-2447 / 1936-2455 |
| Citation | Vol. 15, Issue 1, pp. 111–127 (2023); published online 23 June 2022; received 23 Oct 2021, accepted 16 May 2022 (Springer page) |
| DOI | `10.1007/s12095-022-00591-6` → `https://doi.org/10.1007/s12095-022-00591-6` |
| Publisher page | `https://link.springer.com/article/10.1007/s12095-022-00591-6` |
| Correction | “Correction to: Galois hulls of constacyclic codes over finite fields”, *Cryptogr. Commun.* 15, 129–130 (2023); DOI `10.1007/s12095-022-00602-6`; published 22 July 2022; 10 items, all editorial as displayed (lawfully read in full in P1-03) |
| Indexes | zbMATH Zbl 1518.94136 (paper) / Zbl 1518.94137 (correction); Semantic Scholar CorpusId `250008629`; DBLP `journals/ccds/DebnathPI23`; ACM DL record `dl.acm.org/doi/10.1007/s12095-022-00591-6` |
| Version history | Journal version of record + 2023 correction. **No preprint or repository version located** (arXiv, OpenAlex, Semantic Scholar, Unpaywall, and web searches across P1-01…P1-10) |
| Access status | Closed access everywhere checked: OpenAlex `oa_status = closed`, `any_repository_has_fulltext = false`; Semantic Scholar `isOpenAccess = false`, empty `openAccessPdf`; Unpaywall (fresh, §3): `is_oa = false`, `has_repository_copy = false`, `oa_locations = []` |

**What is verified about content (abstract level only):** the abstract (Springer; ACM DL rendering fetched 21 Oct 2026) states that the paper presents a formula for the dimension of Galois hulls of constacyclic codes, arranging the irreducible factors of `x^n − λ` over `F_q` “in a suitable way”, and, **“considering some restrictions on q”**, counts (the abstract continues) constacyclic codes — corroborated as “counted the number of constacyclic codes of a given Galois hull dimension” by the introduction of repo L4 (ScienceDirect snippet). **Nothing beyond this paragraph is verified. No theorem, hypothesis, or page of the body has been read.**

## 3. Lawful access attempts (actual, dated)

| # | Route | Attempt (21 Oct 2026 unless noted) | Result |
|---|---|---|---|
| 1 | Publisher (Springer) | Article page `link.springer.com/article/10.1007/s12095-022-00591-6` | Abstract/metadata only; full text paywalled. The project has no Springer subscription credential in this workspace; none was used or sought illicitly. |
| 2 | Unpaywall | `api.unpaywall.org/v2/10.1007/s12095-022-00591-6` (fresh) | `best_oa_location = null`, `has_repository_copy = false`, record updated 2025-05-22. No lawful OA copy exists in Unpaywall’s index. |
| 3 | OpenAlex | Work record `W4283360609` (fresh fetch, P1-09) | `is_oa = false`; no repository full text; no alternate locations with PDFs. |
| 4 | Semantic Scholar | Graph API by DOI (P1-09) + CorpusId record | `isOpenAccess = false`; `openAccessPdf` empty. |
| 5 | ACM Digital Library | DOI record (search result, 21 Oct 2026) | Bibliographic + abstract only (standard ACM DL behaviour for a Springer article); no full text. |
| 6 | Author/institutional repository hunt | Web searches (P1-09, P1-10): exact title + preprint/manuscript/pdf; IIT Patna repository phrasing | No author manuscript or institutional copy found. (An academia.edu copy of the **correction only**, licence unverified, was noted in earlier rounds and deliberately not used; ResearchGate was excluded as unauthorised/uncertain and its known leads were dead ends — see worklog.) |
| 7 | Correction notice | Springer correction page (lawfully read in full, P1-03) | Obtained — but it is the 2-page correction, not the paper; its displayed `B_i` definitions do not settle the paper’s scope. |
| 8 | Author / library contact | — | **Not attempted.** No e-mail or message was sent by Arena; no communication tool was invoked. Drafts are provided in §6 for the Boss to send through his own channels. |

**Conclusion of the access phase:** as of 21 October 2026 there is no lawful route *available inside this workspace* to L1’s full text. The remaining lawful routes all require action outside the workspace: (a) an author-supplied copy (realistic: the third author is this project’s research advisor; the corresponding author is at IIT Patna); (b) a library/ILL request through the Boss’s institution; (c) a publisher subscription held by the Boss’s institution. §6 drafts (a) and (b).

## 4. Exactly which theorem statements remain unresolved

The following are the comparisons a future lawful full text must settle (from P1-01 §5.2 / P1-09 §2). **None is answered here.**

- **L1-Q1 (length scope):** Does L1 assume `gcd(n, p) = 1`, treat `p | n`, or split cases? Does “restrictions on q” in the abstract restrict `q`, `n`, `λ`, or the Galois index?
- **L1-Q2 (hull formula):** Exact statement/hypotheses of the hull-dimension formula; is it the same edge-sum as our T4 finite-field specialization (`Σ_f [P − max(a_f, β_f)]·deg f`, `P = p^ϱ`), and with what pairing convention (code-first vs candidate-first matters for `β`)?
- **L1-Q3 (count type):** Is the announced count marginal (by hull dimension only) or joint in `(dim C, dim Hull)`? Labeled codes or dimension values? (Cf. repo L4’s Cor. 3.5, which counts dimension *values* — L1’s abstract wording suggests codes, unverified.)
- **L1-Q4 (factor bookkeeping):** How do L1’s `B_i` sets (displayed in the correction) relate to our `τ`-orbits and predecessor indexing? This decides whether our C3/C4-type counts could already be implicit there.
- **L1-Q5 (moments):** Any mean/variance statements? (Our C5/C6 territory; repo L2 is the known mean paper, but L1 must be checked.)
- **L1-Q6 (affine/product scope):** Finite fields only (as the title says) or any product/ring assembly? Decides whether K2’s affine part is automatically clear of L1.

## 5. Comparison table (all UNRESOLVED against L1)

| Comparison demanded by the command | Status | What would resolve it |
|---|---|---|
| `p | n` vs `p ∤ n` scope in L1 | **UNRESOLVED** | L1’s introduction/hypotheses (L1-Q1) |
| Marginal hull-dimension distribution vs joint code/hull enumerator | **UNRESOLVED** | L1’s counting theorem statement (L1-Q3) |
| L1’s `B_i` components vs our `τ`-orbits | **UNRESOLVED** | L1’s definitions + the correction’s displayed `B_i` in context (L1-Q4) |
| Repeated-root assumptions; component decomposition | **UNRESOLVED** | L1’s setup section (L1-Q1/Q6) |
| Counting / transfer-matrix / moment overlaps | **UNRESOLVED** (no transfer/moment result is visible even at abstract level, but absence is not asserted) | Full text search once obtained (L1-Q3/Q5) |

No result was inferred from the abstract. The overlap matrix (`P1_09_OVERLAP_MATRIX.md`) therefore keeps every L1 cell at “?” — unchanged by this command.

## 6. Drafts for the Boss to send (nothing has been sent)

### 6.1 Draft A — request to the corresponding author (short e-mail)

> Subject: Request for a copy of “Galois hulls of constacyclic codes over finite fields” (Cryptogr. Commun. 15, 111–127)
>
> Dear Prof. Om Prakash,
>
> I am [NAME], [research scholar/student, INSTITUTION], working under the supervision of Dr. Habibul Islam on Galois hulls of repeated-root constacyclic codes over affine algebras. For a literature comparison essential to our work, we need to study your paper with Prof. Debnath and Dr. Islam, “Galois hulls of constacyclic codes over finite fields”, *Cryptography and Communications* 15(1), 111–127 (2023), DOI 10.1007/s12095-022-00591-6. The paper is not openly accessible to us, and we have not found an author manuscript in any repository.
>
> Would you be willing to share an author copy (preprint/accepted manuscript or offprint) for private research use? We would use it only to cite and position our work correctly, and we would be grateful for any version you are able to share.
>
> With thanks and regards,  
> [NAME] · [DEPARTMENT, INSTITUTION] · [E-MAIL]

*(Channel note for the Boss — not part of the e-mail: since Dr. Habibul Islam, a co-author, is the project advisor, asking through him may be simpler and faster than a cold e-mail; Draft A then becomes a two-line request he can forward or answer directly. Arena has not contacted anyone; sending either version is the Boss’s explicit action.)*

### 6.2 Draft B — library / interlibrary-loan request (form fields)

> Document type: Journal article (copy request under the library’s ILL/copyright terms)  
> Authors: Indibar Debnath, Om Prakash, Habibul Islam  
> Title: Galois hulls of constacyclic codes over finite fields  
> Journal: Cryptography and Communications (Springer) · Volume 15 · Issue 1 · Pages 111–127 · Year 2023 (online 2022)  
> DOI: 10.1007/s12095-022-00591-6 · ISSN 1936-2447  
> Requester: [NAME / ID] · Purpose: research/literature review · Date needed by: [DATE]

## 7. If a lawful full text arrives — extraction checklist (for the follow-up command)

1. Record provenance (who supplied it, version: publisher PDF / accepted manuscript / preprint; date; licence basis). File it outside the public repo or as permitted; do not redistribute third-party publisher PDFs in the git history (project precedent: the arXiv copy of repo L4 is arXiv-licensed; a Springer PDF would not be).
2. Extract, with page and theorem numbers and direct quotes distinguished from paraphrase: the setup (fields, `n`, `λ`, Galois index, pairing convention), the hull-dimension theorem, the counting theorem, any moment results, and the definitions behind the correction’s `B_i` sets.
3. Answer L1-Q1…Q6 in a table; update `P1_09_OVERLAP_MATRIX.md` cells from “?” to verified verdicts; then and only then hold the Gate G1 re-vote.

## 8. Decision

- **Novelty claim: DEFER** — strictly on evidence: the claim is neither established (L1 unread, search non-exhaustive) nor disproved (no inspected source contains the joint enumerator/transfer/variance package). Operationally this means **no novelty or “first” claim may be made now** (the must-not-claim list in P1-09 §4.2 remains in force), and Gate G1 is **not closed** by this command.
- **Overall: CONDITIONAL GO** for the project (the proved, corrected, frozen core is unaffected), with manuscript drafting still gated on Gate G1.
- Files changed in this command: created `P1_10_L1_ACCESS_AND_EXTRACTION.md` (+ PDF); updated `04_BLUEPRINT_GAP_REGISTER.md` and `ARENA_WORKLOG.md` sequentially. `02_THEOREM_BLUEPRINT.md` and all proof/validation artifacts untouched (hash re-verified above; validations rerun unmodified as sanity — see worklog entry).
