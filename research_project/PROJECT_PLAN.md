# PROJECT_PLAN — Joint Hull-Dimension Enumeration over Affine Algebra Rings

**Status:** Phase 0 and Phase 1 complete; Phase 2 (literature/novelty) complete.
**Decision point reached:** see `JOINT_ENUMERATOR_FEASIBILITY.md`.
**Date of audit:** 2026-10-20 (UTC)
**Working branch:** `arena/1625045b-galios-hull`

---

## 1. What this project actually is

The supplied master blueprint (`Arena_Master_Research_Blueprint.pdf`) prescribes a
phase-gated, proof-first workflow whose objective is *new theorems with rigorous
proofs*, with a secondary objective of exact hull-dimension enumeration and
quantum-code applications.

The blueprint also prescribes a hard stop: **do not draft a manuscript until the
source audit, literature comparison, at least one substantive proved theorem,
defensible novelty, and independent small-case verification are complete.** If
those conditions fail, the instruction is to *deliver a feasibility report rather
than a misleading manuscript*.

This project therefore has one question to answer before any writing:

> Does the "joint Hermitian hull-dimension enumerator" over a non-chain ring
> support a genuinely new theorem?

Everything in this directory is organised to answer that question with evidence.

## 2. Phases executed so far

| Phase | Content | Status | Evidence |
|---|---|---|---|
| 0 | Workspace inspection, source integrity, environment | PASS (with one critical discrepancy) | `SOURCE_INVENTORY.md`, `SOURCE_PAPER_METADATA.md`, `ENVIRONMENT_CAPABILITIES.md` |
| 1 | Complete source-paper mathematical audit | PASS | `SOURCE_THEOREM_REGISTER.md`, `SOURCE_MATHEMATICAL_AUDIT.md`, `SOURCE_NOTATION_GLOSSARY.md`, `SOURCE_EXAMPLE_RECALCULATION.md` |
| 1B | Independent recomputation of examples and corollaries | PASS | `../verification/*.out`, `../code/` |
| 2 | Literature review and novelty audit | PASS | `../literature/*` |
| 3 | Feasibility determination on the joint enumerator | **GATE NOT PASSED as posed** | `JOINT_ENUMERATOR_FEASIBILITY.md` |

Phases 4–11 of the blueprint (framework, factor-orbit derivation, main theorems,
dual-containing enumeration, full verification suite, manuscript, final audit,
delivery) are **deliberately not started**, because the Phase 2 gate did not pass
for the object as defined.

## 3. Directory map

```
research_project/
  PROJECT_PLAN.md                  this file
  PHASE_STATUS.md                  phase-by-phase status with evidence
  SOURCE_INVENTORY.md              every artifact found, with hashes
  SOURCE_PAPER_METADATA.md         bibliographic identity of the uploaded PDF
  ENVIRONMENT_CAPABILITIES.md      what tooling actually exists
  SOURCE_THEOREM_REGISTER.md       complete register of every numbered result
  SOURCE_MATHEMATICAL_AUDIT.md     proof-level audit, findings F1..F9
  SOURCE_NOTATION_GLOSSARY.md      every symbol, with the exact convention
  SOURCE_EXAMPLE_RECALCULATION.md  Examples 1-3 recomputed from scratch
  JOINT_ENUMERATOR_FEASIBILITY.md  THE VERDICT + what would survive
  literature/
    LITERATURE_REVIEW.md
    LITERATURE_COMPARISON_MATRIX.csv
    NOVELTY_ASSESSMENT.md
    REFERENCE_VERIFICATION_REPORT.md
  code/                            independent finite-field / code library
  verification/                    raw reproducible outputs
```

## 4. Standing conventions adopted for this project

These are fixed now, because the blueprint and the source paper use *different*
field conventions and silently mixing them is the single most likely source of a
false novelty claim.

1. **Ambient field.** The source paper's ambient field is `F_q`, `q = p^e`.
   The blueprint's is `F_{q^2}`. All statements in this project are tagged with
   the convention in force.
2. **Galois parameter.** The source paper's `k`-Galois inner product is
   `⟨x,y⟩_k = Σ x_i y_i^{p^k}`, `0 ≤ k < e`.
   * Hermitian (`y ↦ y^{√q}`) is the special case **`k = e/2`, `e` even**.
   * In the blueprint's/Yadav et al.'s `F_{q^2}` convention, Hermitian is
     **`k = 1` with `e = 2`**.
   These are the same mathematical object written in two coordinate systems, and
   a paper must not mix them.
3. **"Hermitian hull enumerator"** therefore means: the `k = e/2` slice of the
   `k`-Galois theory, over the ambient field of the chosen source.
4. **Counting convention.** A "code" means a distinct linear subspace, not a
   generator polynomial; the bijection between admissible generator polynomials
   and codes is proved in the source (Theorem 3) and re-verified here.
5. **Evidence classes.** Every claim in these documents is tagged:
   `[ESTABLISHED]` (in the literature), `[SOURCE]` (stated in the audited paper),
   `[VERIFIED]` (recomputed by us), `[PROPOSED]`, `[CONJECTURE]`, `[OPEN]`.

## 5. Exit criteria for resuming the manuscript phase

The manuscript phase may resume only if a candidate satisfies **all** of:

- (a) it is not a product/restatement of an enumeration already published;
- (b) it is not a routine corollary of the CRT decomposition plus a known
      finite-field count;
- (c) it has a proof that does not depend on an unproved independence or
      equidistribution assumption;
- (d) it has at least one non-trivial exact verification.

`JOINT_ENUMERATOR_FEASIBILITY.md` §5 lists the candidates that pass (a)–(d) and
those that do not.
