# Phase-9 Manuscript Table Plan

**Audit date:** 2026-09-24
**Status:** design only; no unverifiable numerical data are introduced.

## Table 1 — Notation and assumptions

- **Purpose:** provide the reader with `q,p,e,m_s,d_s,K_s,A,n,lambda_s,k,sigma,rho,mathcal F_s,J_s,tau,a_O,d_O,w_O,epsilon,b_O,T_w,E`.
- **Location:** Section 2.
- **Columns:** symbol, meaning, hypothesis/condition, first use.
- **Source:** `MANUSCRIPT_ASSUMPTIONS.md` and `MANUSCRIPT_NOTATION_AUDIT.md`.
- **Guardrail:** use `mathcal F_s`, not ambiguous bare `F_s`; reserve `R` as a legacy citation symbol only.

## Table 2 — Literature comparison

- **Purpose:** distinguish known mathematics, standard tools, adapted/combined results, and unresolved transfer.
- **Location:** Section 1 or Section 11.
- **Columns:** source ID, setting, result actually checked, relation to the present theorem, transfer status, safe citation use.
- **Source:** `CENTRAL_RESULT_COMPARISON.md`, `FINAL_REFERENCE_AUDIT.md`, `LITERATURE_TRANSFER_MATRIX.md`.
- **Guardrail:** preserve `DIRECT`, `DIRECT AFTER CONVENTION TRANSFORMATION`, `PARTIAL`, `NOT TRANSFERABLE`, and `UNVERIFIED`; do not turn an abstract into theorem evidence.

## Table 3 — Theorem dependency map

- **Purpose:** present the 19-result chain and the two separate convention/invariance propositions.
- **Location:** Section 1 or after Section 2.
- **Columns:** proposed ID, result, dependencies, status, result type.
- **Source:** `THEOREM_DEPENDENCY_GRAPH.md`.
- **Guardrail:** no edge may point from a result to a later corollary; no cycle.

## Table 4 — Computational validation cases

- **Purpose:** document only fully specified finite validation cases.
- **Location:** Section 10.
- **Columns:** case, field/components, `n`, `k`, twist, orbit data, selection count, checks, script/capture.
- **Cases:** F4 pilot, F8 long orbit, F16 extension component, compatible nontrivial twist, N2-A comparison, N2-B incompatible diagnostic, and the Phase-10C global product bridge.
- **Source:** `MANUSCRIPT_DRAFT_SPECIFICATION.md` and the corresponding validator outputs.
- **Guardrail:** label all rows “finite computational validation”; do not include N1.

## Table 5 — Scope and exclusions

- **Purpose:** prevent the reader from extending the theorem beyond its hypotheses.
- **Location:** Section 11.
- **Columns:** topic, central status, reason, permitted future wording.
- **Rows:** repeated roots, incompatible twists, equivalence classes, Burnside/Pólya, unrestricted rings, quantum distance, N1, final/corrected literature transfer.
- **Source:** `MANUSCRIPT_ASSUMPTIONS.md`, `CONTRIBUTION_BOUNDARY.md`, `NOVELTY_BOUNDARY.md`.
- **Guardrail:** use “outside scope” or “future work,” not a claim that the excluded case is impossible.

## Optional display tables

1. A compact orbit-polynomial table for `a=1,...,5` may be included in Section 6 because all entries are symbolic and verified by the binary-word derivation.
2. A theorem-status table may be included in an appendix, but it must distinguish `PROVED WITH CONDITIONS` from computational evidence and literature transfer.
3. No table may contain N1 values, guessed factorizations, unsupported histograms, quantum distances, equivalence counts, or journal outcomes.

---

# Phase-10C table-plan resolution

**Date:** 2026-09-24

The Phase-10A task explicitly required four manuscript tables: notation/assumptions, literature comparison, computational validation, and scope/exclusions. The Phase-10A draft follows that four-table requirement. The earlier Phase-9 dependency-map table design is retained as an architecture record rather than duplicated as a fifth data table: the dependency graph remains explicit in `THEOREM_DEPENDENCY_GRAPH.md`, and the repaired global bridge is stated as Lemmas 3.3–3.6 and Proposition 3.7 in `manuscript/main.tex`. No verified data or theorem dependency is removed by this resolution.
