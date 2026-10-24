# Phase 8 deliverable — Research-gap and contribution decision

**Decision: STOP before Phase 9. Do not write the manuscript.**

The blueprint's Phase 9 condition is: *"Do not start the full manuscript until source audit, literature
comparison, at least one substantive proved theorem, defensible novelty, and independent small-case
verification are complete."* Four of the five hold. **"At least one substantive proved theorem" does
not**, and **"defensible novelty"** does not. Under the blueprint's own instruction — *"If these
conditions fail, deliver a feasibility report rather than a misleading manuscript"* — this document is
that report.

Written from `5fa1ac0`. No manuscript has been drafted. Phase 9 is **not started**.

---

## 1. Phase map: blueprint vs. this project

The blueprint's phase numbering and this project's working labels diverged, so the mapping is stated
explicitly for audit.

| Blueprint phase | Required deliverable(s) | Where it is here | Status |
|---|---|---|---|
| 0 Workspace / source integrity | `PROJECT_PLAN.md`, `SOURCE_INVENTORY.md`, … | `research_project/` Phase 0 set; PDF sha256 `7f7e6803…`, 612 826 B | **done** |
| 1 Source audit | `SOURCE_THEOREM_REGISTER.md`, `SOURCE_MATHEMATICAL_AUDIT.md`, `SOURCE_NOTATION_GLOSSARY.md`, `SOURCE_EXAMPLE_RECALCULATION.md` | `research_project/phase1/` | **done**, Gate 1 PASS |
| 2 Literature / novelty | `LITERATURE_REVIEW.md`, `LITERATURE_COMPARISON_MATRIX.csv`, `NOVELTY_ASSESSMENT.md`, `REFERENCE_VERIFICATION_REPORT.md` | `research_project/phase2/` | **done**, Gate 2 PASS on R4 |
| 3 Precise formulation | `MATHEMATICAL_FRAMEWORK.md` | `phase3/MATHEMATICAL_FRAMEWORK.md` | **done** (this commit) |
| 4 Factor-orbit enumeration | `FACTOR_ORBIT_ANALYSIS.md`, `LOCAL_ENUMERATOR_DERIVATION.md`, `CONSTITUENT_ENUMERATOR_FORMULA.md`, `REPEATED_ROOT_EXTENSION.md` | consolidated in `phase3/CONSTITUENT_ENUMERATOR_FORMULA.md` (§§3–6 are the first two; the repeated-root case is included in the theorem, so no separate extension file) | **done** (`5fa1ac0`) |
| 5 Main theorems | `MAIN_THEOREMS_AND_PROOFS.md` | `phase3/P3_2_TWO_ORBIT.md` (Lemmas 1–4), `P3_3_RING_GRAY.md` (Thm 1–5) | **done but elementary** — see §3 |
| 6 Dual-containing + quantum | `DUAL_CONTAINING_ENUMERATION.md`, `QUANTUM_CONSTRUCTION_THEOREM.md`, `QUANTUM_CODE_PARAMETER_TABLE.csv`, `QUANTUM_PARAMETER_VERIFICATION.md` | `phase3/P3_4_QUANTUM_DISTRIBUTION.md` (tables + counts) | **partial** — tables done; the four named files not split out, and **no quantum-construction theorem is claimed** |
| 7 Computational verification | `code/`, `data/`, `COMPUTATIONAL_VERIFICATION.md`, `REPRODUCIBILITY.md` | probes + logs in `phase2/r1_probe`, `phase2/r3_probe`, `phase3/` | **substantially done**; not yet consolidated under those two filenames |
| 8 Gap / contribution decision | this file | `phase3/RESEARCH_GAP_AND_CONTRIBUTION_DECISION.md` | **done** |
| 9 Manuscript | `paper/main.tex`, `references.bib`, `README.md` | — | **NOT STARTED — deliberately** |

Two honest gaps in Phases 6–7: the four named quantum files and the two named verification files have
not been written as separate documents. Their *content* exists (tables, logs, commands); splitting them
out is clerical, and it is not worth doing before §4's decision, because if the decision is "stop", those
files would be packaging for a contribution that does not stand.

## 2. Evaluation of the blueprint's six candidate contributions

| # | Candidate | Closest known result | Difference | Proof status | Novelty |
|---|---|---|---|---|---|
| 1 | Explicit constituent generating polynomial `H_α(z)` | Debnath–Prakash–Islam, *Cryptogr. Commun.* 15:111–127 (2023) — count by Galois hull dimension "with restrictions on `q`"; Sangwisut–Jitman–Udomkavanich, *AMC* 11 (2017) | orbit-product form, no restriction on `q`, repeated roots included | **proved** (`5fa1ac0`) | **K** — prior art in the square-free case; routine refinement of source Theorem 8 with `p \| n` |
| 2 | Exact total distribution | source Theorem 8/10 + candidate 1 | product of `e` marginals | **proved** (Theorem 1 + CRT) | **K** — a product of known laws |
| 3 | Joint constituent distribution | as above | same | **proved** | **K** — `H_joint = ∏_μ H_{λ_μ}` |
| 4 | Dual-containing enumeration | R3 (`c9d4517`); Debnath & Prakash, ICTIS 2025 (chain ring count) | none | **proved** | **K** — product of published field-level counts; the criterion is the source's own Theorem 15/16 |
| 5 | Quantum existence/counting theorem | source Theorems 18/19 already give existence | a *distribution* of parameters, computed | **not achieved as a theorem** | **U** — no theorem; only exact computation (P3-4) |
| 6 | Repeated-root generalization | Dinh 2011/2013, Chen–Dinh–Liu 2015, FFA 2024; source Theorem 8 already covers `p^v` | none | **proved but trivial** — Lemma 2(a) is one line in characteristic `p` | **K** |

**All six are `K` or unresolved.** Per the blueprint: *"If all candidates are known or routine, stop and
propose a better-supported direction."*

## 3. Why "substantive theorem" fails — stated plainly

The proved results of Phases 4–5 are, in ascending order of content:

* **Lemma 2(a)** (`p^v`-fold multiplicity) — one line.
* **Lemmas 1–4, max-sum identity** — bookkeeping over a squarefree factorisation.
* **Constituent enumerator theorem** — a genuine theorem with a complete proof, but a *re-derivation*
  of a known object; its novelty is nil by construction.
* **Theorems 2–4 of P3-3** (Gray bounds, single-component and equal-component values) —
  support-counting, two lines each, and probably folklore.
* **Theorem 5 of P3-3** (non-determination) — a *negative* result, established by explicit witnesses
  rather than a general construction.

None of these is a theorem a journal would accept as the contribution of a paper. That is the crux: the
honest inventory of *proved* statements is thin, and the strongest content of the project is
computational.

## 4. The better-supported direction, and exactly where it stands

The Phase 2 novelty audit killed the blueprint's enumerator programme and identified **R4**: the exact
joint **(Hermitian hull dimension, Gray distance)** distribution over `R_e`, and the resulting
quantum-parameter distribution. R4 is not one of the blueprint's six candidates.

| R4 component | Status | Evidence |
|---|---|---|
| The object is well defined and not a product of known laws | **established** | P3-1 C3 5/5; P3-3 Thm 5; P3-4 (`((1,2),(1,2))` gives both `[[4,0,≥2]]` and `[[4,0,≥3]]`) |
| Exact computation at small scale | **done** | P3-1 (169 codes), P3-4 (three instances, all distances exact) |
| Supporting theorems | **elementary only** | P3-3 Thms 1–5 |
| Distinguishable from closest known results | **Gate 2 PASS** | P3-5: arXiv:2606.22069 read in full text, no counting |
| Novelty | **not established** | B-2a, B-2b, Tian–Gao–Gao full text all unread |
| Scaling | **unknown** | L-8: cost `∏_ℓ |C_ℓ|` per tuple |

So R4 is a defensible *computational and distributional* contribution, gated on three library access
checks, and carrying no substantive theorem.

## 5. Decision

**Phase 9: NO-GO.** Reasons, in order of force:

1. **No substantive proved theorem.** The blueprint's Phase 9 gate is explicit; it fails.
2. **Novelty not defensible.** The guarded claim "not found under an explicit search" is a literature
   position, not a result, and three full-text checks remain open. Writing a manuscript whose
   contribution section would need that qualification is exactly what the blueprint forbids.
3. **The strongest content is computational**, and the blueprint requires proofs as the primary
   objective (Phase 5: *"Symbolic calculations or finite searches do not replace proof"*).

**What is delivered instead:** this feasibility report, plus the complete audit trail from Phases 0–8.

## 6. What would change the decision

| Trigger | Effect |
|---|---|
| **B-2a / B-2b / Tian–Gao–Gao full texts contain no joint `(hull, d)` distribution** | R4's novelty becomes defensible as a *distributional* contribution; a paper becomes possible, but with an honest framing ("exact computational distribution", not "new theorem") |
| Any of them **does** contain such a distribution | **withdraw** the contribution; report that the direction is closed |
| A restricted family is found where `d(ψ)` **is** determined (Theorem 4's `σ = 1` case is the only known one) | a genuine theorem could be attempted; this is the only route to the primary objective seen so far |
| Scaling is solved (L-8) | the contribution becomes substantive rather than toy: distributions for families of lengths rather than single instances |

None of these is a computation task. The first three are library access; the fourth needs a structural
idea not presently available.

## 7. Status summary

| Item | Status |
|---|---|
| Phases 0–2 | PASS (Gate 1, Gate 2 on R4) |
| Phases 3–7 | delivered, with two clerical gaps named in §1 |
| Phase 8 | **this document — decision: stop** |
| Phase 9 | **NOT STARTED, and should not be** |
| Blockers | **B-1** publisher full texts, **B-2a** Cryptogr. Commun. 2023 body, **B-2b** SIST 2025 body, **Tian–Gao–Gao** full text — all open |
| Limitations | L-1 … L-8, all recorded and unresolved |
| Novelty claimed anywhere | **none** |
| Source PDF | re-verified 612 826 B, sha256 `7f7e6803…` |

No manuscript, no release, no push to `main`.
