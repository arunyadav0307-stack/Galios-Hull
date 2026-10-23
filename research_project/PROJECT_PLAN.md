# PROJECT PLAN — Hull-Dimension Enumeration over Finite Rings

**Governing instruction:** *Arena Master Research Blueprint*, 7 pp., SHA-256
`abcecc47d8eb64226a8c82518c9e43f9b5961a1ef45e47c3685cd5f95842ae23`
(`arunyadav0307-stack/JOINT`, `main`, commit `3cc9e87`), retrieved 2026-10-23.
The blueprint governs phase order, gates, deliverables, proof standards and stop
conditions. Where the blueprint and any earlier local document disagree, the
blueprint wins.

**Project directory:** `research_project/`
**Branch:** `arena/831a2e65-galios-hull` (branched from `main` @ `33aeb79`)
**Status vocabulary:** `PASS` · `FAIL` · `BLOCKED` · `PROVISIONAL`, each with a
named piece of evidence. A document being written is never, by itself, evidence
of a passed gate.

---

## 1. Scope as written in the blueprint

| Item | Blueprint statement |
|---|---|
| Primary objective | New theorems with rigorous proofs |
| Secondary objective | Exact hull-dimension enumeration and quantum-code applications |
| Working title | *Joint Hermitian Hull-Dimension Enumeration and Quantum-Code Construction for Constacyclic Codes over Finite Non-Chain Rings* |
| Named source paper | Yadav, Singh, Islam, Prakash, Solé, *Comput. Appl. Math.* **43** (2024), Paper 269, DOI `10.1007/s40314-024-02789-1` |
| Named ring | $\mathcal R_e=\mathbb F_{q^2}+u\mathbb F_{q^2}+\cdots+u^{e-1}\mathbb F_{q^2}$, $u^e=1$, $e\mid(q+1)$, specified multipliers |
| Proposed objects | Constituent enumerator $H_\ell(z_\ell)$, joint enumerator $H_{\text{joint}}(z_1,\dots,z_e)$, total $H_{\text{total}}(z)$ |

The blueprint is explicit that the enumerator and its quantum consequences are
**proposed**, not established: *"This document is a research plan, not a claim that
the proposed enumerator or its quantum-code consequences are new."*

## 2. Phase sequence, gates and deliverables

| Phase | Content | Gate | Deliverables (blueprint names) |
|---|---|---|---|
| 0 | Workspace inspection, source integrity | **Gate 0:** exact source PDF + usable environment identified | `PROJECT_PLAN.md`, `SOURCE_INVENTORY.md`, `SOURCE_PAPER_METADATA.md`, `ENVIRONMENT_CAPABILITIES.md`, `PHASE_STATUS.md` |
| 1 | Complete source-paper audit (1A extraction, 1B checks) | **Gate 1:** central results and required assumptions understood | `SOURCE_THEOREM_REGISTER.md`, `SOURCE_MATHEMATICAL_AUDIT.md`, `SOURCE_NOTATION_GLOSSARY.md`, `SOURCE_EXAMPLE_RECALCULATION.md` |
| 2 | Literature and novelty audit (2A matrix, 2B tests) | **Gate 2:** contribution distinguishable from closest known results, else revise the question | `LITERATURE_REVIEW.md`, `LITERATURE_COMPARISON_MATRIX.csv`, `NOVELTY_ASSESSMENT.md`, `REFERENCE_VERIFICATION_REPORT.md` |
| 3 | Precise formulation, well-definedness | — | `MATHEMATICAL_FRAMEWORK.md` |
| 4 | Factor-orbit enumeration (square-free first) | — | `FACTOR_ORBIT_ANALYSIS.md`, `LOCAL_ENUMERATOR_DERIVATION.md`, `CONSTITUENT_ENUMERATOR_FORMULA.md`, `REPEATED_ROOT_EXTENSION.md` only if developed |
| 5 | Main theorems and complete proofs (A–D) | — | `MAIN_THEOREMS_AND_PROOFS.md` |
| 6 | Dual-containing enumeration and quantum application | — | `DUAL_CONTAINING_ENUMERATION.md`, `QUANTUM_CONSTRUCTION_THEOREM.md`, `QUANTUM_CODE_PARAMETER_TABLE.csv`, `QUANTUM_PARAMETER_VERIFICATION.md` |
| 7 | Independent computational verification | — | `code/`, `data/`, `COMPUTATIONAL_VERIFICATION.md`, `REPRODUCIBILITY.md` |
| 8 | Research-gap and contribution decision | — | `RESEARCH_GAP_AND_CONTRIBUTION_DECISION.md` |
| 9 | Final manuscript | — | `paper/main.tex`, `paper/references.bib`, `paper/main.pdf` only if compilation succeeds, `paper/README.md` |
| 10 | Final independent audit | — | `FINAL_MATHEMATICAL_AUDIT.md`, `FINAL_NOVELTY_AUDIT.md`, `FINAL_REFERENCE_AUDIT.md`, `FINAL_REPRODUCIBILITY_AUDIT.md`, `FINAL_CHANGELOG.md`, `PACKAGE_MANIFEST.md` |
| 11 | Git and project delivery | — | commit hashes actually created; package manifest |

**Hard stop condition (blueprint, "Execution Protocol"):** the full manuscript may
not start until source audit, literature comparison, at least one substantive
proved theorem, defensible novelty, and independent small-case verification are
complete. If these fail, deliver a feasibility report, not a manuscript.

## 3. Working rules adopted for this project

1. **No fabrication.** No invented theorem, citation, DOI, parameter, program
   output or verification result. Missing files or tools are reported as blockers.
2. **Provenance first.** Every claim in a deliverable points to a path, a page, a
   hash or a command transcript.
3. **Preservation.** Original PDFs and ZIPs are never modified or deleted. Prior
   audits are treated as *inputs to be re-verified*, not as authority.
4. **Status discipline.** `PASS` requires evidence; `PROVISIONAL` marks results
   that depend on an unresolved source or on a convention choice.
5. **One phase per turn-request.** No phase starts before its predecessor's gate is
   satisfied or an explicit user decision overrides it.
6. **No push without authorization.** Work is committed locally on the session
   branch only; publishing is a separate, explicitly authorised step.

## 4. Directory layout (target)

```
research_project/
├── README.md                 index
├── PROJECT_PLAN.md           this file
├── PHASE_STATUS.md           per-phase status and evidence
├── source_audit/             Phase 0–1 documents, manifests, verification logs
│   └── source_text/          generated page-anchored corpus (git-ignored, regenerable)
├── source_paper/             drop point for the accepted source PDF
├── literature/               Phase 2 documents and comparison matrix
├── theory/                   Phases 3–5 (framework, factor orbits, proofs)
├── proofs/                   Phase 5 proof packages, dependency graph
├── code/                     Phase 7 programs (deterministic, no hidden state)
├── data/                     Phase 7 inputs and raw outputs
├── verification/             Phase 7 logs, reproducibility records
├── paper/                    Phase 9 LaTeX source and bibliography
├── logs/                     command transcripts with timestamps
├── tools/                    inventory, identity gate, corpus builder, preflight
├── requirements.txt          Python dependencies with pinned versions
└── prior_art/                extracted copies of the two submitted ZIPs (not tracked)
```

`prior_art/` is a byte-identical extraction of the two ZIPs committed at the
repository root; it is excluded from Git to avoid duplicating 5.6 MB, and is
reproducible with `tools/extract_prior_art.sh`, which verifies both ZIP hashes
before extracting.

## 5. Assumption register

| ID | Assumption | Status |
|---|---|---|
| A-1 | The blueprint PDF at the given URL is the governing document. | **VERIFIED** — 7 pp., hash recorded, content read in full. |
| A-2 | The uploaded PDF is the blueprint's named source paper. | **REFUTED** — see `SOURCE_IDENTITY_BLOCKER.md`. |
| A-3 | Prior audit documents describe earlier work on the same materials. | **VERIFIED in part** — they are internally consistent (101/101 manifest hashes) but their branch/commit provenance cannot be checked here. |
| A-4 | The mathematical programme of Phases 3–6 applies verbatim to the paper that *is* present. | **NOT ESTABLISHED** — different ring, different inner product, different code family. |
| A-5 | A LaTeX toolchain is available for Phase 9. | **FALSE in this environment** — no TeX binaries. |

## 6. Risk register

| ID | Risk | Mitigation |
|---|---|---|
| R-1 | Work proceeds against the wrong paper. | Gate 0 is held `BLOCKED`; explicit user decision requested before Phase 1. |
| R-2 | Novelty claim collapses (as in the prior audit). | Phase 2 is a hard gate with a literature matrix and complete-statement reading. |
| R-3 | No CAS for cross-checks. | Self-written exact Python verifiers plus an independent pathway; disclosure of the limitation. |
| R-4 | No TeX at Phase 9. | Deliver `main.tex` + `references.bib` and report the compilation limitation. |
| R-5 | Prior-art contamination: earlier conclusions get copied instead of re-derived. | Independent re-derivation is required; prior statements are cited only as hypotheses to test. |
| R-6 | Scope creep into the earlier `k`-Galois manuscript. | That manuscript is registered as prior art, not as this project's output. |

## 7. Deliverable verification protocol

At the end of every phase:

1. list the files actually created or changed, with sizes and SHA-256;
2. run a check that each named deliverable exists and is non-empty;
3. record unresolved issues and the exact next step;
4. assign the gate status with its evidence, and stop unless the gate passes.

The Phase 0 verification record is `source_audit/PHASE0_VERIFICATION_LOG.md`.
