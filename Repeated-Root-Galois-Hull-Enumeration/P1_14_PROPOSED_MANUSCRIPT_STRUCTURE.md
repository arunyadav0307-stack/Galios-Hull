# P1-14 (companion) — Proposed Manuscript Structure and Readiness Map

**Command:** P1-14 — Mathematical Advancement Without L1 (companion deliverable)  
**Date:** 21 October 2026

**Status: PROPOSAL ONLY.** This is a structure plan, not a manuscript. No text below asserts novelty or priority. Gate G1 (literature/novelty) remains **DEFERRED**; manuscript drafting stays gated until the Commander decides otherwise (repo L1 full text still unacquired — see `P1_12_L1_ACQUISITION_STATUS.md`). Mathematical readiness tags come from `P1_14_MATHEMATICAL_ADVANCEMENT.md` (proofs: P1-04…P1-06 and P1-14 §4; computational evidence: `code/validate_p1_14.py`).

**Readiness tags:** ✅ READY = proof complete and independently audited · 🟡 PROPOSED = proof complete in P1-14, needs Commander adoption decision before it may be listed as a paper result · 🔬 SUPPORTING = computational-evidence section material · ⛔ BLOCKED = cannot be written honestly yet · ⚠️ CONDITIONAL = only under extra external hypotheses.

---

## Proposed section structure (aligned with the frozen blueprint §4 architecture)

### 1. Introduction — ⛔ BLOCKED (Gate G1)
- **May be written now (internal draft only):** the problem statement (joint `(dim C, dim Hull)` distribution for labeled repeated-root constacyclic codes over `A ≅ ∏ K_s`), the model, and a neutral summary of contributions phrased **without** “first / new / novel” priority language.
- **May not be written yet:** any priority positioning against repo L1 (Debnath–Prakash–Islam 2023 — unread at theorem level), any “to our knowledge the first” sentence, and any related-work table that ranks our results against L1/L4/L8 beyond what P1-09 verified from actual texts. The honest-distance paragraphs vs L4 (arXiv:2412.08512) and L8 (Eldin & Solé, arXiv:2305.15237) can be drafted from `P1_09_OVERLAP_MATRIX.md`, with L1 explicitly marked “comparison pending full text”.

### 2. Preliminaries and conventions — ✅ READY
Notation freeze; code-first pairing (S7) stated verbatim (it is load-bearing for T3’s `α_{i−1}`); `#` with the `f(0) ≠ 0` domain (PC-3); compatibility `λ_s^{1+p^{d_s−k}} = 1`; labeled assignments over fixed labeled components (PC-5). Sources: blueprint §0 + P1-04 §0. Include the orientation warning (P1-14 §2.3): the predecessor convention must be visible wherever T3/T4 are stated.

### 3. Repeated-root factorization and parametrization — ✅ READY
`M_s = S_s^P`; T1 (bijection, `(P+1)^{|F_s|}`); T2 (`#` multiplicativity with multiplicities, root transport, compatibility equivalence). Proofs: P1-04 §§1–2 (RR-1, RR-2). No separability is used in RR-1/RR-3 — worth one remark each, as referees will ask.

### 4. The Galois dual — ✅ READY
Euclidean-dual lemma RR-3 (no separability anywhere; the identity `gh = x^n − λ` does all the work); transport `D(C) = ρ(C^⊥)`; T3 with `β_i = P − α_{i−1}`; the remark that the generator identity survives without compatibility in the two-modulus form `x^n − λ^{−p^{d_s−k}}`, while the same-modulus statement needs compatibility (necessity witness: P1-04 §7, GF(9) order-8 `λ`).

### 5. Hull generator and dimension — ✅ READY
RR-5 (intersection = lcm, in `K[x]` and in the quotient); T4 with the edge term `min(P − α_i, α_{i−1})`. Proof: P1-04 §6. This is the paper’s computational heart; the `P − max(u,v) = min(P−u, P−v)` step should be displayed, not hidden.

### 6. Transfer matrix and the global enumerator — ✅ READY
T5 (closed-walk trace; labeled positions — no division by `L`); CRT/product assembly (Prop. 3.1 — direct product of the square-free algebra, no coprimality between components needed); T6 (main theorem). Proofs: P1-05 §§2–4. Include the hypothesis-separation remark (P1-14 §2.2): the trace identity is pure `Z[u,z]` combinatorics valid for all `P ≥ 1`; the prime-power enters through T1/T4.

### 7. Corollaries: counts, LCD, self-orthogonality — ✅ READY (+ 🟡 one refinement)
- C1 (total), C2 (code-dimension marginal) — ✅.
- C3 (LCD `2^{#orbits}`, `P`-independent) — ✅. 🟡 **N3 refinement** (joint LCD × code-dimension generating function `∏_O (1 + u^{P w_O L_O})`): proved in P1-14 §4; include only after adoption decision.
- C4 (self-orthogonal ⟺ `α_{i−1}+α_i ≥ P` per edge; dual-containing ⟺ `≤ P`; both counts, equal by `α ↦ P−α`) — ✅ (PC-4 text already in the frozen blueprint).

### 8. Moments: mean, variance, and a covariance theorem — ✅ READY (+ 🟡 two additions)
- C5 corrected mean (`ν_P` on `L_O=1`, `μ_P` on `L_O≥2`) and the `L=1` self-loop phenomenon — ✅ (frozen corrected text; P1-06 Thm. 2.4). The pre-correction failure should be footnoted honestly if the predecessor manuscript used the unsplit form (P1-14 §5.3 gives two quantified witnesses).
- C6 variance (three regimes `V_1/V_2/V_{L≥3}`; weights `w_O` vs `w_O²`) — ✅ (frozen text; P1-06 Thm. 3.7; symbols re-derived in P1-14 Layer A).
- 🟡 **N1** `Cov(dim C, dim Hull) = 0` with the uncorrelated-≠-independent witness — proved in P1-14 §4; adoption decision pending. If adopted, it belongs here as a small theorem (its proof is short and the statement is quotable).
- 🟡 **N2** `Var(dim C) = [P(P+2)/12]·Σ w_f²` — proved in P1-14 §4; adoption decision pending; natural companion to N1 (together they give the full second-order summary of the joint distribution’s margins).

### 9. Examples and computational validation — 🔬 SUPPORTING (ready to assemble)
Material exists and is independently reproduced by `code/validate_p1_14.py`: E1 (`P=2,L=2` nine-tuple table — suitable as a hand-checkable first example), E2 (`P=1,L=3` simple-root recovery), E3 (GF(4), `n=10`, mixed orbits `[1,2]`), E4 (GF(8), `n=14`, orbit length 6 — also the orientation witness), E5 (two-component `GF(2)×GF(4)` assembly, 729 assignments). The section must carry the standing disclaimer: finite checks are supporting evidence, not proof. Suggested: print full joint distributions for E3/E4 (they are small) and the E1 table.

### 10. Limitations and scope boundaries — ✅ READY (content fixed; wording at drafting time)
Labeled (non-isometry) counting; compatible twists only; square-free affine `A`; uniform labeled model for moments; orientation convention borne by T3 (P1-14 §2.3); incompatible-twist two-modulus form of T3 as the only statement available there; `Cov = 0` is not independence (N1 remark).

### 11. Conditional quantum remark (C7) — ⚠️ CONDITIONAL / recommend appendix or omission
Only in the finite-field case with an externally known distance `d` (standard `[[n, K−H, d; n−K−H]]` form). The enumerator alone yields no distance or quantum parameter. Recommendation: omit from the main text, or one clearly-fenced remark; never a numbered consequence of T6.

### 12. Conclusion — ⛔ BLOCKED with §1
Depends on the introduction’s final positioning; draft only after Gate G1 is decided.

---

## Readiness summary

| Block | Content | Tag |
|---|---|---|
| §2–§6 | Conventions, T1–T6 | ✅ READY (proved; independently audited in P1-14) |
| §7 | C1–C4 | ✅ READY |
| §7/§8 | N3, N1, N2 | 🟡 PROPOSED — proved in P1-14 §4; Commander adoption decision required (frozen blueprint untouched until then) |
| §8 | C5 (corrected), C6 | ✅ READY (frozen corrected text; symbolically re-derived) |
| §9 | Examples/validation E1–E5 | 🔬 SUPPORTING — data reproduced by fresh import-free code |
| §10 | Limitations | ✅ READY (content fixed) |
| §11 | C7 EAQECC | ⚠️ CONDITIONAL — appendix or omit |
| §1, §12 | Introduction positioning, conclusion | ⛔ BLOCKED until Gate G1 (L1 theorem-level comparison) |

**What this structure deliberately does not do:** claim novelty or priority for any block; rank the results against repo L1; present computational checks as proofs; or fold N1–N3 into the theorem list before adoption. The mathematical core (§§2–10) is, as of P1-14, in a state where drafting could begin the day the Commander (i) decides on N1–N3 adoption and (ii) resolves Gate G1 — those are the only two gates left, and the second one still runs through the lawful acquisition of L1 (`P1_11_L1_ACQUISITION_HANDOFF.md`, drafts **NOT SENT**).
