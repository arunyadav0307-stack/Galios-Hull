# Hull-Dimension Enumeration over Affine Algebra Rings — Phases 0–2

**Branch:** `arena/1625045b-galios-hull` · **Audit date:** 2026-10-20 (UTC)
**Status:** Phase 0 PASS · Phase 1 PASS · Phase 2 **gate not passed for the
proposed object** · Phases 3–11 blocked by the blueprint's own stop condition.

---

## The answer

> **Can the joint Hermitian hull-dimension enumerator support a genuinely new
> theorem?**
>
> **No, not as defined.** The joint enumerator factorises, provably, into a product
> of constituent enumerators (Proposition J), and the constituent enumerator is
> already published for the finite-field case — `[D23]` counts constacyclic codes
> of a given Galois hull dimension under stated restrictions on `q`; `[SJL15]`
> covers cyclic and negacyclic codes in general. Under the blueprint's own taxonomy
> the object is **K — known or routine**: its novelty is exactly the novelty of the
> local enumerator, which is not this project's question.
>
> One direction survives, but narrowly: **enumeration up to isometry** — and a
> 2026-10-20 screening showed that even this must be reformulated, because the hull
> dimension is not invariant under isometry (`C1_ISOMETRY_SCREENING.md`). An
> independent literature check (2026-10-20) found that both halves of that problem
> are already developed — class counts of constacyclic codes up to `n`-isometry
> (Chen et al. 2012; 2024), and mass formulas for hull-constrained linear codes
> (Li–Shi–Ling 2025). Only their intersection is untouched — and the screening above
> shows that "up to isometry" is not even the right equivalence to ask about.

Full argument: **`JOINT_ENUMERATOR_FEASIBILITY.md`**.

---

## Two findings that change how the brief should be read

**1. The uploaded PDF is not the paper the blueprint names.**
The blueprint (pp. 1–2) names Yadav–Singh–Islam–Prakash–Solé, *Comput. Appl. Math.*
**43** (2024) 269 (DOI `10.1007/s40314-024-02789-1`). The uploaded PDF is
Debnath–Islam–Martínez-Moro–Prakash, *Galois hulls of constacyclic codes over affine
algebra rings*, arXiv:2412.08512v1, now *Discrete Math.* **349**(2) (2026) 114750 —
a different paper, different ring, different inner product, different theorems.
Yadav et al. is reference **[43]** of that paper.
→ `SOURCE_PAPER_METADATA.md` §2.

**2. The source paper has a structural hypothesis gap that its own examples
violate.** `[S1]` §2.3 treats every CRT component as `F_q`. That holds only if all
`t_i` split over `F_q`. In Examples 2 and 3, `t_1` is irreducible of degree 2, so
the components are `F_{q²}`, `dim_q A = 4` while the paper uses `N = 2`; the Gray
map `A → F_q^2` cannot be injective, and an `A`-submodule with component dimensions
`(4,6)` has `dim_q = 20`, not `10`.
→ audit finding **F11**.

---

## What was actually produced

### Phase 0 — provenance and environment
| File | Contents |
|---|---|
| `SOURCE_INVENTORY.md` | every artifact with SHA-256; prior Phase-10F package; conflict inventory |
| `SOURCE_PAPER_METADATA.md` | exact identity of the audited PDF; the bibliographic mismatch; verified facts about Yadav et al. |
| `ENVIRONMENT_CAPABILITIES.md` | what exists; **Magma/Sage/LaTeX absent**; what was built instead |
| `PROJECT_PLAN.md` | scope, conventions, exit criteria |

### Phase 1 — the source audit
| File | Contents |
|---|---|
| `SOURCE_THEOREM_REGISTER.md` | **complete register**: 10 theorems, 9 lemmas, 5 corollaries, 2 remarks, 3 examples, 1 table, 6 unnumbered load-bearing items; **zero** enumeration results |
| `SOURCE_MATHEMATICAL_AUDIT.md` | findings **F1–F11** and positive record **P1–P10** |
| `SOURCE_NOTATION_GLOSSARY.md` | every symbol; the two competing field conventions; a symbol-collision table |
| `SOURCE_EXAMPLE_RECALCULATION.md` | Examples 1–3 recomputed from scratch, with exact minimum distances |

### Phase 2 — literature and novelty
| File | Contents |
|---|---|
| `literature/LITERATURE_REVIEW.md` | five strata of prior work; what is established; what is open |
| `literature/LITERATURE_COMPARISON_MATRIX.csv` | 19 entries, prescribed columns |
| `literature/NOVELTY_ASSESSMENT.md` | Proposition J with proof; N1/N2/K/F/U classification of every candidate |
| `literature/REFERENCE_VERIFICATION_REPORT.md` | 31 references, each with a verification level A–D (5 A / 14 B / 12 C) |

### Independent verification and decision (2026-10-20)
| File | Contents |
|---|---|
| `INDEPENDENT_VERIFICATION_REPORT.md` | F11, the CRT decomposition, the Gray-map count and the quantum parameters re-derived from the PDF at exact page/equation loci; proven contradictions separated from labelling issues; literature re-verified from publisher pages; **version of record BLOCKED at the time of writing** (partially inspected 2026-10-20 — see the dossier); audit of this project's own scripts |
| `FINAL_F11_EVIDENCE_DOSSIER.md` | **F11 evidence dossier**: independent re-derivation of the cardinality, component-field, dimension and Gray-map arithmetic for Examples 1–3 **and all 13 rows of Table 1**; independent verification of the `F_9` isometry witness; partial inspection of the version of record (abstract, full introduction, snippets — body BLOCKED); three-way separation of proved (v1) / BLOCKED (version of record) / not-yet-assertable; evidence table; go/no-go. Archive: `FINAL_F11_EVIDENCE_DOSSIER.zip` |
| `EVIDENCE_REQUEST_TO_AUTHOR.md` | **outgoing request** to the corresponding author: article title, DOI, the exact discrepancy in arXiv v1, and the precise sentence needed from the published §2 — a one-line (A)/(B)/(C) answer, a quotation, or a PDF reprint. Contains no claim that the published article is wrong |
| `ILL_REQUEST_TO_LIBRARY.md` | **outgoing request** for lawful access through interlibrary loan / document delivery: full citation with DOI, PII and ISSN, the section required if only a partial supply is possible, acceptable formats, copyright declaration, and fallbacks if the item cannot be supplied |
| `FINAL_F11_VERIFICATION_LOG.md` | **third-pass verification record**: seven access routes to the published article tried and itemised (all closed); the exact missing evidence; the version comparison restricted to the observable surface; the clean-room re-run with cross-script agreement; and the final BLOCKED decision |
| `verification/VERBATIM_LOCI_v1.md` | **verbatim locus register**: every decisive claim with printed page, section / theorem / equation, and the exact extracted text (L1–L18 for arXiv v1; P-1–P-8 for the observable published surface, explicitly not the body) |
| `verification/cleanroom_run_2026-10-20.log` | console transcript of both audit scripts re-run from a pristine unzip, including full manifest verification and the diff against the archived logs |
| `FINAL_GO_NO_GO_DECISION.md` | **final decision document**: verified facts about arXiv v1 (F1–F8) and about the published version (P1–P4), the BLOCKED items b1–b7, the 13-row Table 1 audit with its derivation and reproducibility, the precise scope of any correction, and the one-sentence decision rule that turns BLOCKED into GO or NO-GO |
| `verification/VOR_INSPECTION_2026-10-20.md` | verbatim record of what of the **published version** (*Discrete Math.* **349**(2) 2026, 114750) was and was not read: abstract, complete introduction, section snippets, 45-item reference list; what the surviving "`q`-dimension" framing does and does not license |
| `code/table1_audit.py` → `verification/table1_audit.out` | audit of all 13 rows of Table 1: naming-free transcription check (`g_S ∣ xⁿ−λ_S`, 13/13), printed `k` vs unweighted `Σ(n−deg g_S)` (13/13), length vs `2n`, feasibility of `2k ≤ 2n`, Theorem 10 arithmetic |
| `code/table1_forensics.py` → `verification/table1_forensics.out` | **self-contained** re-audit (no project imports): rebuilds `F₄, F₉, F₂₅` and `F₁₆, F₈₁, F₆₂₅`, finds the roots of the six defining polynomials, counts Galois orbits, derives `N` and `|S(ν)|` for all three rings, and runs checks C0–C10 on all 13 rows including a second-transcription match |
| `FINAL_INDEPENDENT_MATHEMATICAL_CHECK.md` | **final deliverable**: Task A (isometry counterexample, `F₄` Euclidean and `F₉` Hermitian, with the general criterion and proof), Task B (F11 re-derived from first principles at component level), Task C (recommendation among correction note / restricted enumeration / abandon) |
| `C1_ISOMETRY_SCREENING.md` | **negative result**: the Galois hull dimension is not a class function on isometry classes (`q=4, n=3`: `⟨1+x⟩` and `f(ωx)` are cyclic, isometric, same weight enumerator, hulls 0 and 1). Refutes the naive form of C1 and states the two formulations that survive |
| `RESEARCH_DIRECTION_DECISION.md` | C1 vs C3 vs stop, each with question, established results, gap, likely theorem, proof strategy, compute needs, risks and the novelty evidence still required |
| `PHASE_STATUS.md` | every phase, with evidence and status |

### Verification
| File | Contents |
|---|---|
| `code/gf.py` | dependency-free exact `GF(p^m)`, polynomial, code and hull library |
| `code/independent_verification.py` | builds `A` explicitly, finds its idempotents, builds the real `A`-module, computes `dim_q` — no assumption about components |
| `code/verify_examples.py` · `code/verify_example1.py` · `code/verify_corollary_3_5.py` | the three verification drivers |
| `verification/*.out` | raw timestamped outputs |

---

## Evidence ledger

| Claim | Class | Where |
|---|---|---|
| `[S1]` Theorems 2, 3, 5, 6, 7, 10 and Lemma 9 are correct | `[VERIFIED]` | audit P1–P10 |
| `[S1]` Examples 1, 2, 3 reproduce exactly (hull dims, Gray parameters, distances) | `[VERIFIED]` | `verification/` |
| Corollary 3.5(1) and (2) hold in admissible regimes | `[VERIFIED]` | Test 1, Test 2 |
| Corollary 3.5(2) fails as printed when `n` is odd | **defect** | F3 |
| Lemma 5's proof is invalid; statement true | **defect** | F4 |
| Theorem 8's bound is unproved; a two-line proof is supplied | **defect** | F5 |
| §2.3's component-field assumption fails in the paper's own examples | **defect** | F11 |
| The joint enumerator factorises | `[PROVED]` | Proposition J |
| The local enumerator is published | `[ESTABLISHED]` | `[D23]`, `[SJL15]` |
| Enumeration over a product ring is published | `[ESTABLISHED]` | `[S25]`, `[GWF23]`, `[DP25b]`, `[LGM25]` |
| Isometry-class enumeration is open | `[OPEN]` | `[S1]` p.23; no result found |
| "The joint enumerator is new" | **`[FALSE]`** | contradicts Proposition J + `[D23]`/`[S25]` |
| The paper's `ψ : A → F_q^2` is a bijection in its own examples | **`[FALSE]`** | `|A| = q^4 > q^2`; independent verification §2.1 |
| `dim_q C = 20` and `44` in Examples 2, 3 | **`[VERIFIED]`** | `verification/independent_verification.out` |
| The Galois hull dimension is a class function on isometry classes | **`[FALSE]`** | `verification/final_check_A.out` — `q=4, n=3` (Euclidean, 0→1) and `q=9, n=5` (Hermitian, 2→0) |
| The Hermitian hull changes in the `F_4` witness | **`[FALSE — retracted]** | it is `0 → 0`; provably invariant at `q=4` |

---

## What was deliberately not done

No manuscript, no LaTeX, no PDF, no novelty claim, no priority claim, no Git push,
no overwriting of the original files. The blueprint's stop condition was applied:
*"If these conditions fail, deliver a feasibility report rather than a misleading
manuscript."*

## Where to start reading

1. `JOINT_ENUMERATOR_FEASIBILITY.md` — the decision and what survives.
2. `SOURCE_MATHEMATICAL_AUDIT.md` — findings F1–F11.
3. `SOURCE_THEOREM_REGISTER.md` — the complete register.
4. `literature/NOVELTY_ASSESSMENT.md` — Proposition J and the classifications.

---

**Known caveat — `code/final_check_A.py` and `code/final_check_B.py`.** These two
scripts contain **hardcoded absolute output paths**
(`/home/user/Galios-Hull/research_project/verification/final_check_{A,B}.out`), unlike
`code/table1_audit.py` and `code/table1_forensics.py`, which resolve their output path from
`__file__`. Consequence: running them from an extracted copy of the archive writes its
log back into this project tree rather than beside the extracted script. The only
difference is the timestamp line; the mathematical content is identical. The scripts were
left unmodified so that every archived hash stays valid. If the logs ever appear to have
"changed", compare them against the archive — a timestamp-only diff is expected.
