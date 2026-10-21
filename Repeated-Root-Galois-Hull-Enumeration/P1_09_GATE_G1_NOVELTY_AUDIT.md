# P1-09 — Gate G1 Novelty Closure Audit

**Command:** P1-09 — Gate G1 Novelty Closure Audit  
**Date:** 21 October 2026  
**Companion:** `P1_09_OVERLAP_MATRIX.md` (claim-by-claim matrix K1–K7 × L1/L2/L3/L4/L8/neighbours, with per-source records).

**Gate G1 recommendation: DEFER — Gate G1 cannot be closed on the present evidence.** Overall project decision: **CONDITIONAL GO**. Recommendation on novelty claims: **NO-GO for any priority/“first” claim** until repo L1 is read in full. This audit is not permission to draft the manuscript.

---

## 1. Freeze verification (Step 1)

- Branch `arena/ab8e330d-galios-hull`; the local checkout was found reset to base commit `33aeb79` with the project files untracked (sandbox state, again), while the remote held the full pushed history. The workspace was first backed up (`/tmp/proj_backup_p109`), the remote state restored by fast-forward to `origin/arena/ab8e330d-galios-hull`, and `diff -r` confirmed the restored tree is **identical** to the pre-reset workspace (no loss, no history rewrite, no force-push).
- Current commit (before this audit’s commits): `33a8c28` — “P1-08: integration audit”. Working tree clean at verification time.
- Frozen blueprint `02_THEOREM_BLUEPRINT.md` SHA-256: `ec2fd8d58f8d2a986314f83997d750d689f7c88e98ec8f87753ab4c9cf438cff` — identical to the after-hash recorded in `P1_08_INTEGRATION_AUDIT.md`. **The blueprint was not edited in this command**, and no proof or validation artifact was modified.

## 2. The L1 question (Step 2) — still unresolved, lawfully

**Exact paper.** Indibar Debnath, Om Prakash & Habibul Islam, “Galois hulls of constacyclic codes over finite fields”, *Cryptography and Communications* 15(1), 111–127 (2023). DOI `10.1007/s12095-022-00591-6` (published online 23 June 2022; issue Jan 2023). Correction: DOI `10.1007/s12095-022-00602-6`, 15, 129–130 (2023). zbMATH Zbl 1518.94136 (paper), Zbl 1518.94137 (correction). OpenAlex `W4283360609`; Semantic Scholar CorpusId `250008629`; DBLP `journals/ccds/DebnathPI23`. Authors at IIT Patna.

**Version history (verified):** journal version of record (Springer, 2022/2023) + a 10-item correction (2023, lawfully read in full during P1-03 — all items editorial as displayed; the displayed `B_i` factor-set definitions mirror orbit-style bookkeeping but do not settle scope). No preprint (arXiv or other repository) has been located in any search to date.

**Lawful-access attempts (fresh, 21 Oct 2026, plus the P1-02/P1-03 records):**
- OpenAlex API record for the DOI (fresh fetch): `open_access.is_oa = false`, `oa_status = closed`, `any_repository_has_fulltext = false`, no PDF URL.
- Semantic Scholar Graph API (fresh fetch): `isOpenAccess = false`, `openAccessPdf.url` empty.
- Springer article page (lawful): abstract + metadata only; full text paywalled. A fresh web search (query: the exact title + preprint/manuscript/pdf, excluding ResearchGate) returned only the Springer page, the correction, an academia.edu copy **of the correction only** (unverified licence — not used), and citing papers. No author manuscript, institutional copy, or repository version was found.
- Not attempted (correctly): paywall circumvention of any kind; inferring theorems from the abstract.

**What the abstract level does verify:** “This paper presents a formula for the dimension of Galois hulls of constacyclic codes” (Springer abstract), and — corroborated by the introduction of repo L4 (ScienceDirect snippet, 21 Oct 2026) — “they also counted the number of constacyclic codes of a given Galois hull dimension.”

**Exactly which comparisons therefore cannot yet be made (the L1-Q list):** (Q1) Does L1 allow `p | n` (repeated-root lengths) or assume `gcd(n, p) = 1`? (Q2) Is its hull-dimension formula equivalent to our finite-field specialization of T4 (`min(P − α_i, α_{i−1})` edge form), and under which hypotheses on `q, k, λ`? (Q3) Is its count a count of **labeled codes by hull dimension only**, or joint in `(dim C, dim Hull)`? (Q4) Does it count codes at all in the affine/product setting (title says finite fields — presumably not, unverified)? (Q5) Does it contain means/variances? (Q6) How do its `B_i` sets relate to `τ`-orbits (relevant to our C3/C4 counts)? Until a lawful full text is read, **no overlap verdict stronger than “unresolved” is honest for K1, K2, K4 against L1**.

## 3. Overlap assessment (Step 3) — summary

Full details: `P1_09_OVERLAP_MATRIX.md`. Headlines, with evidence levels:

- **L4 (affine; arXiv full text verified):** substantial partial overlap with **K1** — hull generator (Thm. 7), dual generator (Thm. 5), and a repeated-root hull-dimension theorem (Thm. 8, arXiv numbering) whose `b`-terms are cyclic sums of `max{u_δ, p^{e′} − u_{δ−1}}` expressions, **under extra hypotheses** (`gcd(ord λ, n′) = 1`, `ord λ | 1 + p^{e−k}`) and in an idempotent (semisimple) component presentation. It counts attainable dimension *values* (Cor. 3.5), not codes, and its conclusion leaves code enumeration over `A` open. No joint enumerator, transfer trace, or moments in the inspected text.
- **L8 (multi-twisted/GPM; arXiv full text verified):** strong hull-machinery overlap in a different family (Thms. 8–11, 21–22, 25–29, arXiv numbering); constacyclic codes are the index-1 case with no general simple-root restriction found — so T3/T4-style hull formulas are **not** first-in-field. No joint enumerator/transfer/moments in the inspected text.
- **L2 (average dimensions; abstract verified):** owns the *mean-as-headline* territory over finite fields/`R_{m,q}`. Our C5 must stay a corollary (GAP-12), never a headline.
- **L3 (small hull dimensions; publisher page verified):** covers hull dimensions 1–2 including `p | n` cases — “first repeated-root hulls” would be false.
- **Neighbours (scope level):** repeated-root hull/LCD literature and classical hull enumeration/averages exist; the inspected Check-D records (P1-02 §3, plus a fresh targeted search on 21 Oct 2026 returning no counterpart) contain **no** labeled affine repeated-root joint `(dim C, dim Hull)` transfer-trace enumerator. Databases: arXiv, zbMATH Open, OpenAlex, Semantic Scholar, publisher pages. **Not searched: MathSciNet, Scopus, Web of Science** (no lawful access). Non-exhaustive; non-discovery ≠ novelty.

**Net assessment.** The mathematical centre that no *inspected* source contains is the package **K2 + K3 + K6** (joint labeled enumerator over the affine product for `P > 1`, per-orbit transfer traces, variance in `P`), with K4/K5 as corollaries and K1 as (partially pre-occupied) foundation. But the finite-field core of K1 — and possibly counting territory adjacent to K2/K4 — cannot be cleared while L1 is unread. A novelty claim built today would rest on an incomplete search against the single most relevant finite-field predecessor, written by (among others) this project’s own advisor’s group — the worst possible source to leave unread.

## 4. Novelty statements (Step 4)

### 4.1 Safest defensible statement (internal/planning use; adaptable for a manuscript only after §4.3)

> “In the sources we have been able to inspect in full or at abstract level (listed in `P1_09_OVERLAP_MATRIX.md`), we have not found a joint enumeration of labeled repeated-root constacyclic codes over product affine algebras by code dimension and Galois hull dimension, nor the per-orbit transfer-matrix trace formula and the associated mean and variance formulas in `P` proved here. Hull-dimension formulas for individual codes (including repeated-root cases under additional hypotheses) and counts of attainable dimension values are known (repo L4; repo L8 for multi-twisted codes), as are average hull dimensions over finite fields (repo L2) and small-hull-dimension criteria (repo L3). A finite-field hull-dimension formula and a count of codes by hull dimension are announced in the abstract of Debnath–Prakash–Islam (2023) (repo L1), whose full text we have not been able to access lawfully; we make no priority claim relative to that paper.”

### 4.2 Claims that must NOT be made yet

1. “First” hull-dimension formula/generator for repeated-root (or general) constacyclic codes — contradicted by L4 Thm. 7/8 and L8, and unverifiable vs L1.
2. “First” count of constacyclic codes by (Galois) hull dimension — L1’s abstract announces such a count; scope unread.
3. Any priority claim over repo L1 on the finite-field specialization of T3/T4/C3/C4.
4. “First” average/mean hull dimension (L2), “first” small-hull-dimension results incl. `p | n` (L3), “first” repeated-root hull treatment (L3/L4/L9–L10 scope records).
5. “No prior work exists” / “novel” unqualified — the search is non-exhaustive (MathSciNet/Scopus/WoS unsearched; L1 unread).
6. Publisher-version claims for L4/L8 theorem numbers (only arXiv numbering verified; L8 publisher numbering demonstrably differs).

### 4.3 Specific missing source/comparison needed to strengthen the claim

One item: **a lawful full text of repo L1** (author-supplied copy — note the third author is this project’s advisor, so an author/institutional channel is realistic — or library/ILL), followed by a theorem-by-theorem extraction answering L1-Q1…Q6 (§2) against T3/T4/C3/C4/C5 and the K2 joint-vs-marginal question. Secondary strengthening: publisher-version spot-verification of L4/L8 main theorems; a MathSciNet/Scopus pass if access becomes available.

### 4.4 Journal-level novelty-risk assessment

- **If submitted today** (e.g. to *Cryptography and Communications*, *Advances in Mathematics of Communications*, or *Finite Fields and Their Applications*) with the §4.1 statement and honest positioning: risk is **medium** — the enumerator/transfer/moment package is a real contribution over the inspected record, but a referee who knows L1 (plausible at exactly these journals; L1 sits in *Cryptogr. Commun.*) could force major reframing if L1’s count turns out to be joint or to cover `p | n`.
- **If submitted today with any “first” wording:** risk **high** — L4/L8/L3 already falsify broad versions, and L1 is a standing unknown.
- **After L1 is read:** risk drops to **low–medium** in the best case (L1 simple-root and/or marginal-only → our repeated-root affine joint package is cleanly positioned) and is **manageable** in the worst case (positioning shifts to the affine-product assembly, transfer traces, and `P`-moments, with L1 cited for the finite-field core). No acceptance probability is guaranteed or implied; this is a risk assessment, not a prediction.

## 5. Decision

- **Gate G1: DEFER (cannot close).** The blocking item is singular and identified (L1 full text). Closure criteria for a future vote: L1-Q1…Q6 answered from a lawful full text; overlap matrix updated; §4.1 re-checked word by word.
- **Overall: CONDITIONAL GO** — the proved, corrected, frozen mathematical core (T1–T6, C1–C6; blueprint SHA-256 `ec2fd8d5…`, commit `1c67fda`) is unaffected by this audit; what is conditioned is any novelty claim and the manuscript phase that depends on Gate G1.
- **NO-GO for novelty/priority claims** until Gate G1 closes.

## 6. What was run / changed in this command

- Fresh lawful fetches: OpenAlex DOI record; Semantic Scholar Graph API record; web searches (L1 manuscript hunt — negative; targeted joint-enumerator/transfer hunt — no counterpart). No paywall bypass; no theorem inferred from an abstract.
- Files created: `P1_09_GATE_G1_NOVELTY_AUDIT.md`, `P1_09_OVERLAP_MATRIX.md` (+ PDFs for side viewing). Files updated (sequentially): `04_BLUEPRINT_GAP_REGISTER.md`, `ARENA_WORKLOG.md`. **Not modified:** `02_THEOREM_BLUEPRINT.md`, all proof files, all validation scripts/outputs.
- Existing validation scripts were also rerun unmodified as a sanity check (outputs redirected outside the repo artifacts): `validate_p1_03.py` exit 0 and byte-identical to its saved output; `validate_p1_05.py` and `validate_p1_06.py` both printed their ALL-PASSED final lines. No saved output file was touched.
