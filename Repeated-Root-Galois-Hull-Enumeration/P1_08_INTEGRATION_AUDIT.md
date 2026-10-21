# P1-08 — Integration Audit (Blueprint Correction Freeze)

**Command:** P1-08 — Apply Commander Decisions and Freeze the Corrected Blueprint  
**Date:** 21 October 2026  
**Decisions applied (explicit Commander decisions, not re-decided here):** PC-1 APPROVE, PC-2 APPROVE, PC-3 APPROVE, PC-4 APPROVE, PC-5 APPROVE, PC-6 REJECT (obsolete “to be proved” label; proved C6 status/formulas recorded instead).

---

## 1. Pre-edit state (recorded before any edit)

- Branch: `arena/ab8e330d-galios-hull`; working tree clean.
- Local HEAD before editing: `a92bb21a29f43a782bc973eff34203aaab8e0aae` (P1-07). Remote branch ref (via `git ls-remote`): `a92bb21a29f43a782bc973eff34203aaab8e0aae` — **local = remote, no divergence**, so the controlled edit proceeded (no reset, no overwrite; none was needed or performed).

## 2. Blueprint hashes

- **Before:** SHA-256 `013ef5a20742b3de735d49edb6f2fdde074b0d134adea9c85d30d24cab739ce3`
- **After:** SHA-256 `ec2fd8d58f8d2a986314f83997d750d689f7c88e98ec8f87753ab4c9cf438cff`
- **New frozen state:** blueprint at the after-hash, contained in integration commit **`1c67fda`** (“P1-08: apply PC-1..PC-5, reject PC-6 label; re-freeze blueprint”), pushed to `origin/arena/ab8e330d-galios-hull` and verified against the remote ref after push (see §6; final remote verification is reported in the P1-08 final report, together with this audit’s own commit hash).

## 3. Exact accepted changes and locations (one controlled edit; nothing else)

All line numbers refer to the after-edit file. Each change carries a dated `[P1-08 …]` marker in the file, and a “Correction Notes” section (lines 6–8) summarizing all six decisions.

| # | Decision | Location | Change | Proof reference |
|---|---|---|---|---|
| 1 | Header/freeze record | Lines 2, 6–8 | Status line updated; dated Correction Notes section added listing PC-1…PC-5 applied and PC-6 rejected, with rationale | This audit; `P1_07_PC_DECISION_DOSSIER.md` |
| 2 | PC-2 (dual order) | §0, line 17 | Added `D(C) = {y : ⟨c, y⟩_{s,k} = 0 for all c ∈ C}` (code first, candidate second); stated `D(C) = ρ(C^⊥)`, Euclidean generator `h^♮` (ordinary reciprocal), code-first generator `h_a# = ρ̄(h_a^♮)` | `P1_04_PROOFS_T1_T4.md` (S7), Lemma RR-3, Prop. 4.2, T3 |
| 3 | PC-3 (`#` domain) | §0, line 24; T2(i), line 38 | `#` restricted to monic `f` with `f(0) ≠ 0`; noted automatic for `f | M̄_s` (`M̄_s(0) = −μ_s ≠ 0`) and `h_a` | `P1_04_PROOFS_T1_T4.md` (S6), Lemma RR-2, §7 audit |
| 4 | PC-5 (T1 scope) | T1, line 34 | Global code = `A`-submodule of `A^n` under the fixed labeled CRT decomposition; component codes `K_s`-linear; counts labeled, not equivalence classes; product parametrization not claimed for mixing `F_q`-subspaces | `P1_05_PROOFS_T5_T6_COROLLARIES.md` (G3), Prop. 3.1 |
| 5 | PC-4 (C4 count) | C4, line 84 | Added `#{a : D(C) ⊆ C} = ∏_O tr((B′_P)^{L_O})`, `(B′_P)_{a,b} = 1` iff `a + b ≤ P`, under the characterization + compatible/labeled hypotheses; noted equality of the two counts via `α_i ↦ P − α_i` | `P1_05_PROOFS_T5_T6_COROLLARIES.md` §5 (C4) |
| 6 | PC-1 (C5 mean) | C5, lines 85–87 | Hull mean replaced by `E[Hull] = μ_P·Σ_{O : L_O ≥ 2} w_O L_O + ν_P·Σ_{O : L_O = 1} w_O` (`μ_P = P(2P+1)/(6(P+1))`, `ν_P = ⌊P²/4⌋/(P+1)`), old display explicitly marked incorrect for `L_O = 1`; proof key corrected (distinct uniforms only for `L_O ≥ 2`; self-loop `min(P−A, A)` for `L_O = 1`); **`P = 1` case corrected**: `E[Hull] = (1/4)·Σ_{L_O ≥ 2} w_O L_O` since `ν_1 = 0`. Code-dimension mean `E[dim C] = (n/2)·Σ_s m_s` **preserved unchanged** | `P1_06_MOMENT_PROOFS_C5_C6.md` §2 (Lemmas 1.1, Props. 2.2–2.3, Theorem 2.4); `P1_03_MATHEMATICAL_PROOF_PLAN.md` §4 |
| 7 | PC-6 (rejected label; correct status) | C6, lines 88–92 | **No** “to be proved” label added. C6 now states the proved result: `Var(dim_{F_q} Hull_k) = Σ_s Σ_{O∈O_s} w_O²·V_{L_O}(P)` with `V_1` parity-split, `V_2`, `V_L (L≥3)` formulas, adjacent covariance `κ_P`, `L=2` cross-covariance; mean-vs-variance weights (`w_O` vs `w_O²`) distinguished; marked “RR-8 discharged” | `P1_06_MOMENT_PROOFS_C5_C6.md` §3 (Theorem 3.7) |

**Diff audit:** the complete `git diff` of the blueprint was inspected line by line; it contains exactly the seven items above (status/correction-notes, §0 ×2, T1, T2, C4, C5, C6). No other mathematical change was introduced; in particular T1–T6 statements, C1–C3, C7, the layer-decomposition section, the dependency map, and the section architecture are byte-unchanged.

## 4. Consistency audit (against the proof files)

- **C5 at `P = 1` / `L = 1`:** blueprint now gives `ν_1 = ⌊1/4⌋/2 = 0` and `E[Hull] = (1/4) Σ_{L_O≥2} w_O L_O`, matching P1-06 Prop. 2.2/Theorem 2.4 and the brute counterexamples to the old display (`GF(2)/GF(8)`: `11/3` vs old `35/9`; `GF(3)/GF(9) λ=1`: `2` vs `7/2`).
- **Dual convention:** the added sentence is verbatim the convention (S7) of P1-04 under which `h_a#` was proved to be the dual generator; `h^♮` (ordinary reciprocal, RR-3) vs `h_a# = ρ̄(h_a^♮)` (RR-4 transport) stated as in Prop. 4.2; the opposite-order alternative (which would give the `σ`-reciprocal) is excluded by the sentence, as PC-2 intended.
- **Reciprocal domain:** `f(0) ≠ 0` in §0 and T2 matches P1-04 (S6)/RR-2; necessity witness `f(x) = x` recorded in the dossier.
- **Dual-containing count:** formula, matrix `B′_P`, and hypotheses (characterization + compatible twists + labeled model) match P1-05 §5 exactly; count equality via `α ↦ P − α` noted.
- **C6 variance:** formulas compared character-for-character with P1-06 Theorem 3.7 (`V_1` even `P(P+2)(P²+2P+4)/(48(P+1)²)`, odd `(P−1)(P+3)/48`; `V_2 = P(P+2)(P²+2P+3)/(18(P+1)²)`; `V_L = L·P(P+2)(P²+2P+2)/(60(P+1)²)`; `κ_P = −P(P+2)(7P²+14P+9)/(360(P+1)²)`; `L=2` covariance `−P²(P+2)²/(36(P+1)²)`) — identical. Weights: mean uses `w_O` (P1-06 Thm 2.4), variance `w_O²` (Thm 3.7) — distinguished in both C5/C6 text now.
- **Compatibility assumptions:** unchanged everywhere (per-component `λ_s^{1+p^{d_s−k}} = 1`); PC-4’s count explicitly inherits them.

## 5. Validation (existing scripts, unmodified — supporting evidence, not proof)

Run on 21 Oct 2026 after the edit:

```
python3 code/validate_p1_03.py        # exit 0; output byte-identical to code/validation_p1_03_output.txt; ALL P1-03 EXTENDED CHECKS PASSED
python3 code/validate_p1_05.py        # ALL P1-05 MULTI-COMPONENT ASSEMBLY CHECKS PASSED
python3 code/validate_p1_06.py        # ALL P1-06 MOMENT CHECKS PASSED
python3 code/validate_repeated_root.py # ALL PROTOTYPE CHECKS PASSED
```
No validation script or saved output was modified (git status shows only the intended files). Passing finite tests support — but do not substitute for — the cited proofs.

## 6. Freeze, remaining gaps

- **Frozen state identifier:** blueprint SHA-256 (after) `ec2fd8d58f8d2a986314f83997d750d689f7c88e98ec8f87753ab4c9cf438cff`, committed as `1c67fda` and pushed; the remote ref was re-read after push to confirm it points at the pushed history (no force-push, no history rewrite at any point).
- **Closed by this integration:** GAP-01 (C5 mean), GAP-06/RR-8 (variance), GAP-17 (convention/corrections register). PC-1…PC-5 are now **APPROVED–APPLIED (21 Oct 2026)**; PC-6 is **REJECTED (superseded)** with the proved C6 status recorded.
- **Still open (unchanged):** **Gate G1 — novelty/literature** (repo L1 theorem text unresolved; no novelty or priority claim is made anywhere in the corrected blueprint); C7/RR-9 remains a conditional scope statement (no EAQECC parameters from the enumerator alone); incompatible twists remain out of scope; counts are labeled assignments only. Manuscript drafting has **not** begun.
