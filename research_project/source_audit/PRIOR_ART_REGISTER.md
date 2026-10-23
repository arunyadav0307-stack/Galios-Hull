# PRIOR ART REGISTER — Phase 0

**Prepared:** 2026-10-23 (UTC)

The workspace contains substantial earlier work. It is registered here so that it
can be **used** and **challenged**, never silently inherited. Every claim attributed
below is a claim *made by the prior artefact*; it is **not** adopted as established
in this project. Paths are relative to
`research_project/prior_art/Galios-Hull-Complete-Work-2026-10-20/` unless stated.

---

## 1. Stream P1 — the "k-Galois affine-algebra" manuscript package

**Where:** `01_Paper_Package/` (102 files; byte-identical copy at
`prior_art/Galios-Hull-kGalois-Phase10F/`).

**What it claims to be.** A finished submission package for the paper *Exact Joint
Enumeration of $k$-Galois Hull Dimensions for Labeled Constacyclic Codes over
Square-Free Affine Algebras*: 19-page compiled PDF, LaTeX source, 8 validation
programs, 79 validation documents going up to "Phase 10F", a manifest, build
scripts and traceability files.

**Key artefacts**

| Path | Bytes | SHA-256 (prefix) | Nature |
|---|---:|---|---|
| `01_Paper_Package/manuscript/main.tex` | 50 635 | `b5c038f5540960a1` | LaTeX source, 19 pp. when compiled |
| `01_Paper_Package/manuscript/main.pdf` | 478 856 | `a4cbae942887235f` | compiled 2026-09-24, pdfTeX 1.40.26 |
| `01_Paper_Package/manuscript/references.bib` | 4 080 | `acc788ee15a476e1` | bibliography |
| `01_Paper_Package/blueprint/new-paper-blueprint.md` | 152 972 | `0240ca00df223daa` | **a different blueprint**, for the $k$-Galois project |
| `01_Paper_Package/validation/VALIDATION_REPORT.md` | 57 963 | `7a651acd246d8d03` | consolidated validation record |
| `01_Paper_Package/MANIFEST.txt` | 12 780 | `d1e71ae975acf6e6` | 101 hash/size entries |

**Subject matter.** $k$-Galois hulls (second-slot inner product
$\langle x,y\rangle_{s,k}=\sum_i x_i y_i^{p^k}$) of labelled constacyclic codes over
the **square-free affine algebra** $\mathbb F_q[X_1,\dots,X_\ell]/\langle t_1,\dots,t_\ell\rangle$,
with a transfer-matrix generating polynomial in a code-dimension variable $u$ and a
hull-dimension variable $z$.

**Relation to the present blueprint.** It is a *different research question on the
same source paper* (Object A). The present blueprint is about **Hermitian** hulls
over the **non-chain ring** $\mathcal R_e=\mathbb F_{q^2}+u\mathbb F_{q^2}+\cdots+u^{e-1}\mathbb F_{q^2}$
(Object C). The two share techniques (CRT decomposition, factor orbits,
conjugate-reciprocal action) but not objects, hypotheses or conclusions.

**Integrity status (verified this session).** All 101 manifest entries re-hash
correctly (101 OK / 0 missing / 0 mismatched). The package is internally consistent.

**Provenance status (unverified).** The manifest attributes the package to branch
`arena/01a0c9d2-galios-hull`, commit `360c1ef9b870ca4da89ab4ff2c92ff60d1d3dbe5`.
That branch and commit do not exist in this repository (single commit `33aeb79`,
no such ref). Content is checkable; history is not.

**Treatment in this project.** Reference only. It is **not** evidence that the
present blueprint's gates are passed, and its manuscript is **not** this project's
deliverable. If the present project later reaches Phase 9, it must produce its own
`paper/main.tex`; copying P1's manuscript would substitute a different theorem.

---

## 2. Stream P2 — the F11 / feasibility audit

**Where:** `02_F11_Audit/` (51 files: 15 top-level reports, 11 programs,
31-ish literature/verification files).

**What it claims.** That the uploaded PDF (Object A) has a structural hypothesis
gap, labelled **F11**: §2.3 of the preprint treats every CRT component as
$\mathbb F_q$, which holds only when all $t_i$ split over $\mathbb F_q$; in the
paper's own Examples 2–3 some components are $\mathbb F_{q^2}$, making the Gray map
non-injective and certain dimensions wrong. It further claims that the **joint
hull-dimension enumerator is not novel** — it factorises into constituent
enumerators, and the constituent enumerator is already published — so **Gate 2
fails** and phases 3–11 are blocked.

**Key artefacts**

| Path | Bytes | SHA-256 (prefix) |
|---|---:|---|
| `02_F11_Audit/PHASE_STATUS.md` | — | — |
| `02_F11_Audit/JOINT_ENUMERATOR_FEASIBILITY.md` | 17 060 | `0d36776f9d6a320a` |
| `02_F11_Audit/RESEARCH_DIRECTION_DECISION.md` | 17 072 | `c1da026a85e7ad85` |
| `02_F11_Audit/INDEPENDENT_VERIFICATION_REPORT.md` | 32 297 | `a9d55912b465fcc4` |
| `02_F11_Audit/FINAL_GO_NO_GO_DECISION.md` | 24 810 | `398b36cb19c5ea83` |
| `02_F11_Audit/C1_ISOMETRY_SCREENING.md` | 9 086 | `e30a742a316b02c8` |
| `02_F11_Audit/code/` | 11 programs | includes `gf.py`, `f11_source_audit.py`, `table1_forensics.py` |

**Status claims as written:** Phase 0 PASS · Phase 1 PASS · Gate 2 **FAIL** ·
Phases 3–11 **BLOCKED** · a single narrow direction (`C1`, isometry classes)
retained provisionally and then itself called into question.

**Treatment in this project.** Treated as an **unverified prior hypothesis set**.
Each decisive claim must be re-checked against Object A's pages before it is used.
Nothing in P2 is cited as authority in this project's deliverables.

---

## 3. Conflict register (prior art vs prior art)

| ID | Conflict | Evidence | Resolution policy |
|---|---|---|---|
| C-P1 | P2 states "no `paper/main.tex`, no PDF" (Phases 3–11 blocked) while P1 contains `manuscript/main.tex` and a 19-page `main.pdf` in the same archive | `02_F11_Audit/PHASE_STATUS.md` vs `01_Paper_Package/manuscript/` | Both preserved. P2's sentence describes P2's branch, not the archive. Neither is treated as the project's paper. |
| C-P2 | P1's manuscript is dated 2026-09-24; P2's novelty gate failure is dated 2026-10-20 | PDF `/CreationDate D:20260924160132Z`; P2 README date | The manuscript **predates** the audit that undermines its central claim. This is a material risk for any reuse of P1. |
| C-P3 | P1's `MANIFEST.txt` cites branch `arena/01a0c9d2-galios-hull`, commit `360c1ef9…`; the present repository has one commit `33aeb79` and no such branch | `git ls-tree`, `git branch -a` | Provenance unverifiable; content hashes are the usable evidence. |
| C-P4 | `00_START_HERE.md` says 154 files; the archive holds 155 | file count | Cosmetic; recorded, not corrected. |
| C-P5 | P1 uses a 153 KB `new-paper-blueprint.md` as its governing document; this session is governed by the 7-page PDF blueprint | both documents in the workspace | The PDF blueprint governs this session. The markdown blueprint is prior art. |

## 4. Reusable material (with conditions)

| Asset | Reusable how | Condition |
|---|---|---|
| `02_F11_Audit/code/gf.py` | exact $\mathbb F_q$ arithmetic for checks | must be re-read and re-tested before use; no blind import |
| `02_F11_Audit/verification/VERBATIM_LOCI_v1.md` | page-referenced quotations of Object A | must be re-confirmed against the PDF |
| `01_Paper_Package/code/validate_*.py` | patterns for finite enumeration over affine algebras | applicable to Object A's setting only, not automatically to $\mathcal R_e$ |
| `01_Paper_Package/references.bib` | starting bibliography | each entry re-verified in Phase 2 |
| `01_Paper_Package/validation/` | prior literature notes | re-checked, never cited as a source |

## 5. Prohibited reuse

* Copying P1's `main.tex` (or any of its theorems) into this project's Phase 9
  manuscript.
* Citing P2's findings as established facts.
* Treating either stream as evidence that a gate of **this** project has passed.
