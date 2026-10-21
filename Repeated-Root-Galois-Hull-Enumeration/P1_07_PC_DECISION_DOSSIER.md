# P1-07 — Decision Dossier for PC-1 … PC-6 (No Automatic Approval)

**Command:** P1-07 — PC-1 to PC-6 Decision Dossier  
**Date:** 21 October 2026  
**Purpose:** analysis and documentation only. **Nothing in this dossier approves, rejects, or integrates any proposal.** Every status below remains **PENDING — Boss/Commander decision required**.

**Sources cross-checked:** `02_THEOREM_BLUEPRINT.md` (frozen text, transcribed), `04_BLUEPRINT_GAP_REGISTER.md` (GAP-01, GAP-06, GAP-17, outcomes of P1-03…P1-06), `P1_03_MATHEMATICAL_PROOF_PLAN.md` (§4, §6), `P1_04_PROOFS_T1_T4.md`, `P1_05_PROOFS_T5_T6_COROLLARIES.md`, `P1_06_MOMENT_PROOFS_C5_C6.md`, and the validation scripts/outputs `code/validate_p1_03.py`, `code/validate_p1_05.py`, `code/validate_p1_06.py` (all rerun unmodified for this dossier; §8).

## How to use this dossier

For each PC: (1) exact frozen text affected, (2) exact proposed old→new change, (3) mathematical reason, (4) proof location and evidence, (5) classification, (6) consequences of accepting/rejecting, (7) **recommended disposition (recommendation only)**. The Boss/Commander should record, for each PC, one of APPROVE / REJECT / DEFER plus date; integration (if any) must happen in a later command as dated correction notes, never silently (GAP-17 resolution rule).

## Summary table (recommendations only — all statuses PENDING)

| PC | Affects | Class | Recommendation |
|---|---|---|---|
| PC-1 | C5 hull mean | **Theorem correctness** (frozen formula false) | **APPROVE** |
| PC-2 | T3 / convention freeze | Convention consistency (correctness-critical ambiguity) | **APPROVE** |
| PC-3 | T2 / definition of `#` | Correctness of quantification (definition domain) | **APPROVE** |
| PC-4 | C4 (add dual-containing count) | Exposition/completeness (proved addition, no change to existing text) | **APPROVE** |
| PC-5 | T1 / global scope | Scope/exposition | **APPROVE** |
| PC-6 | C6 status marking | Exposition/status accuracy | **REJECT as superseded** (RR-8 has since been proved; replace instead by integrating the P1-06 formulas — a separate integration action, not PC-6) |

---

## PC-1 — C5 hull mean: split `L = 1` / `L ≥ 2`

**1. Exact frozen statement affected** (`02_THEOREM_BLUEPRINT.md`, C5): “`E[Hull] = [P(2P+1) / (6(P+1))] · Σ_O w_O L_O`”, with proof key: “ek kenare par `min(P−α_i, α_{i−1})` do swatantra uniform `{0,…,P}` ka `min` hai; `E[min] = Σ_{t=1}^P ((P−t+1)/(P+1))² = P(2P+1)/(6(P+1))`. `P=1` par `1/4` — purana mean wapas.” (The first part of C5, `E[dim C] = (n/2)·(Σ_s m_s)`, is correct and is **not** touched by PC-1; re-derived in P1-06 §2.1.)

**2. Exact proposed change.** Replace the displayed formula and key by:
`E[Hull] = μ_P · Σ_{s} Σ_{O∈O_s, L_O ≥ 2} w_O·L_O  +  ν_P · Σ_{s} Σ_{O∈O_s, L_O = 1} w_O`, where `μ_P = P(2P+1)/(6(P+1))` and `ν_P = ⌊P²/4⌋/(P+1)`. Replace the “`P=1` par `1/4`” sentence by: “`P=1` par `E[Hull] = (1/4)·Σ_{L_O ≥ 2} w_O L_O` (`L_O = 1` orbits ka yogdaan `0` hai).”

**3. Mathematical reason.** The proof key is valid only when an edge’s two arguments come from distinct independent exponents. For `L_O ≥ 2` that holds (each cyclic edge pairs `A_i` with the distinct `A_{i−1}`; also for `L_O = 2`, the two edges are the two ordered pairings of the same distinct pair), so every edge has mean `μ_P` (P1-06 Lemma 1.1, tail-sum derivation) and the orbit mean is `L_O·μ_P` (Prop. 2.3). For `L_O = 1` the single edge is a self-loop `min(P−A, A)` whose arguments are functions of one variable; its mean is `ν_P` (Prop. 2.2, parity evaluation of `Σ_a min(P−a,a) = ⌊P²/4⌋`). Since `ν_P ≠ μ_P` for all `P ≥ 1` (e.g. `ν_1 = 0 ≠ 1/4 = μ_1`), the frozen display overcounts exactly the `L_O = 1` part.

**4. Proof location and evidence.** Proof: `P1_06_MOMENT_PROOFS_C5_C6.md` §2.2–2.4 (Theorem 2.4), building on `P1_03_MATHEMATICAL_PROOF_PLAN.md` §4. Exact counterexamples to the frozen display (vector-level Gram-rank brute force, `P1_03` §7, GAP-01): `GF(2), n_0=7, P=2`: brute mean `11/3` vs frozen `35/9`; `GF(3)`/`GF(9)`, `λ=1, P=3` (four `L=1` orbits): brute `2` vs frozen `7/2`; `GF(8), k=1, P=2`: brute `11/3` vs frozen `35/9`; in `L≥2`-only cases (`λ=−1`) frozen = corrected = brute (`7/2`), isolating the error to `L=1`. Orbit-level: `validate_p1_06.py` confirms `ν_P, μ_P` against enumeration for `P ∈ {1,2,3,4,5,8,9}` (`ALL P1-06 MOMENT CHECKS PASSED`, rerun for this dossier).

**`P = 1` special-case verification (required).** At `P = 1`: `ν_1 = ⌊1/4⌋/2 = 0` (indeed `min(1−A, A) ≡ 0` on `A ∈ {0,1}`), `μ_1 = 1·3/(6·2) = 1/4`. Correct prediction: an `L = 1` orbit contributes `0`; each `L ≥ 2` orbit contributes `w_O·L_O/4`. Frozen prediction: `w_O·L_O/4` also for `L = 1` orbits — wrong by `w_O/4` per unit-weight `L = 1` orbit. Example: the `GF(3), λ=1, P=3` case has four `L=1`, `w=1` orbits: correct contribution `4·ν_3 = 4·(1/2) = 2` (brute `2`), frozen `4·1·μ_3 = 4·(7/8) = 7/2`. The cleanest `P=1` instance is any single `L=1, w=1` orbit: true mean `0`, frozen prediction `1/4`.

**5. Classification.** Theorem correctness. This is the only PC that repairs a false theorem statement.

**6. Consequences.** *Accept:* C5 becomes true; the `P=1` recovery note for moments becomes correct; P1-06 Theorem 2.4 can be cited as the proof. Nothing else in T1–T6/C1–C4 changes (the enumerator never used the mean). *Reject:* the blueprint permanently carries a false formula; any manuscript must either omit C5’s hull mean or flag it as an open error — a serious credibility risk, since the counterexamples are elementary (any `L=1` orbit). *Defer:* same as reject until decided.

**7. Recommended disposition: APPROVE** — the frozen formula is demonstrably false and the replacement is fully proved and multiply verified.

---

## PC-2 — Add the dual-order sentence to the convention freeze

**1. Exact frozen text affected** (`02_THEOREM_BLUEPRINT.md` §0, freeze): “Code-first pairing: `⟨x,y⟩_{s,k} = Σ_i x_i σ(y_i)`; dual `D(C)`, hull `Hull_k(C) = C ∩ D(C)`.” The symbol `D(C)` is used (here and in T3) **without a defining set-builder expression**; the word “code-first” in the header (“Convention freeze: … code-first pairing, inverse-Frobenius reciprocal”) is the only indication of the intended order.

**2. Exact proposed change.** Add one sentence to the freeze: “`D(C) = {y : ⟨c, y⟩_{s,k} = 0 for all c ∈ C}` (code vector first, candidate second).” No other wording changes.

**3. Mathematical reason — trace through RR-2, RR-3, RR-4 (with the roles of `σ, ρ, h^♮, h_a#`).**
- *RR-2 (`#`, `τ`):* `#` is defined by coefficientwise `ρ` plus reversal (`f#(x) = ρ(f_0)^{-1} Σ ρ(f_i) x^{r−i}`); it is multiplicative and permutes the factor set `F`. This is pure algebra — the dual-order convention plays no role here, but `#` is the object whose correctness as a *dual generator* depends on the order, next steps.
- *RR-3 (Euclidean dual):* the Euclidean pairing `Σ c_i z_i` is symmetric, so the Euclidean dual needs no order convention; its generator is `h^♮`, the **ordinary** reciprocal of `h_a` (no Frobenius), proved in P1-04 Lemma RR-3 without separability.
- *RR-4 (transport):* the code-first dual solves `⟨c, y⟩ = Σ_i c_i σ(y_i) = 0` for the **second-slot** candidate `y`: setting `w = σ(y)` shows `y ∈ D(C) ⟺ σ(y) ∈ C^⊥ ⟺ y ∈ ρ(C^⊥)` (coordinatewise `ρ = σ^{-1}`); applying the coefficientwise `ρ` to `h^♮` produces exactly `h_a#`, with exponents `β_i = P − α_{i−1}` (P1-04 Prop. 4.2, T3). Under the opposite slot order, the same computation gives `D(C) = σ(C^⊥)`, the generator built from coefficientwise `σ` instead of `ρ`, and predecessor indices reversed (`β_i = P − α_{i+1}` under the same orbit labeling) — i.e. the frozen `h_a#`/exponent formula would be **wrong**, not just differently worded. The freeze as written does not exclude that reading on paper.

**4. Proof location and evidence.** `P1_04_PROOFS_T1_T4.md` (S7) states the sentence verbatim and uses it in Prop. 4.2; `P1_05_PROOFS_T5_T6_COROLLARIES.md` §1/G5 rechecks it. Computational evidence that the intended reading is code-first: the `GF(8), k=1` case (`σ = a² ≠ a⁴ = ρ`) in `validate_p1_03.py` matches the `ρ`-formula (2,187 assignments; the old `GF(4)` prototype cannot distinguish the readings since there `σ = ρ`). Register: GAP-17.

**5. Classification.** Convention consistency with direct correctness consequences (an ambiguous freeze makes T3’s statement reader-dependent).

**6. Consequences.** *Accept:* T3/T4 become unambiguous; the sentence already used in P1-04/P1-05 becomes the frozen one; no theorem content changes. *Reject:* every future proof/manuscript must restate the convention locally (as P1-04/P1-05 did) and a referee can legitimately read T3 the other way. *Defer:* workable short-term (proof files carry the sentence), but leaves the root ambiguity in the frozen source.

**7. Recommended disposition: APPROVE** — one sentence, zero mathematical change to the intended (and computationally confirmed) reading, removes a genuine ambiguity.

---

## PC-3 — Add the hypothesis `f(0) ≠ 0` to the range of `#`

**1. Exact frozen text affected** (`02_THEOREM_BLUEPRINT.md` §0 and T2): the reciprocal is introduced as “`f#(x) = ρ(f₀)⁻¹ Σ_i ρ(f_i) x^{r−i}` (monic, degree-rakh rakhta hai)”, and T2 states “(i) `#` monic polynomials par multiplicative hai; … (ii) Root action: `f(α)=0 ⟹ f#(α^{−p^{d_s−k}})=0`”, without restricting which monic polynomials `#` applies to.

**2. Exact proposed change.** Wherever `#` is defined/quantified, read: “for monic `f` **with `f(0) ≠ 0`**”. Proposed sentence for the freeze: “`#` is defined for monic polynomials with nonzero constant term.”

**3. Mathematical reason.** The definition divides by `ρ(f_0)`; if `f(0) = f_0 = 0` this is division by zero — `#` is undefined, not merely inconvenient. Minimal witness: `f(x) = x` (monic) has no reciprocal of the displayed form. The hypothesis is automatic in every application in the paper (factors `f ∈ F_s` divide `S_s` and `S_s(0) = −μ_s ≠ 0`; likewise `h_a(0) ≠ 0` since `g_a(0)h_a(0) = −λ_s`), so adding it narrows nothing that is ever used; it only makes T2’s quantifier honest.

**4. Proof location and evidence.** `P1_04_PROOFS_T1_T4.md` (S6), Lemma RR-2(ii)/(iv) (the root-transport proof uses `α ≠ 0`, i.e. `f(0) ≠ 0`), and the §7 hypothesis audit (“`#` undefined when the constant term vanishes; such factors never divide `S`”). Register: P1-03 §6 review of T2.

**5. Classification.** Theorem correctness (well-posedness of a definition/quantifier); effectively a domain clarification.

**6. Consequences.** *Accept:* T2 is literally true as written; no proof step changes (P1-04 already assumed it). *Reject:* the frozen T2 remains formally ill-posed for e.g. `f(x) = x` — a trivial but real referee objection. *Defer:* same exposure until decided.

**7. Recommended disposition: APPROVE** — necessary for literal correctness, costless in scope.

---

## PC-4 — Add the dual-containing count to C4

**1. Exact frozen statement affected** (`02_THEOREM_BLUEPRINT.md`, C4): “`C ⊆ D(C)` ⟺ har orbit-edge par `α_{i−1}+α_i ≥ P`; ginati `∏_O tr(B_P^{L_O})`, `(B_P)_{a,b} = 1` agar `a+b ≥ P` varna `0`. Ulta: `D(C) ⊆ C` ⟺ `α_{i−1}+α_i ≤ P` har edge par.” The characterization of `D(C) ⊆ C` is stated; **no count** is stated for that side.

**2. Exact proposed change.** Append to C4: “`#{a : D(C) ⊆ C} = ∏_O tr((B′_P)^{L_O})`, `(B′_P)_{a,b} = 1` agar `a + b ≤ P` varna `0`.” Nothing else changes.

**3. Mathematical reason.** The frozen characterization says dual-containing assignments are exactly the closed walks whose steps satisfy `a + b ≤ P`; by the same trace expansion as T5 (P1-05 §2, Step 1, with the `0/1`-matrix `B′_P`), their number per orbit is `tr((B′_P)^{L_O})`, and independence over orbits gives the product. Moreover the two counts in C4 coincide: `α_i ↦ P − α_i` maps `{a+b ≥ P}` walks bijectively to `{a+b ≤ P}` walks.

**4. Proof location and evidence.** Proved as the labeled PC-4 proposal in `P1_05_PROOFS_T5_T6_COROLLARIES.md` §5 (PC-4 box, including the involution). Computational: `validate_p1_03.py` checks the dual-containing brute counts against `∏ tr((B′)^L)` in all six vector cases (e.g. `GF(9), λ=−1`: `100 = 100`; `GF(8)`: `258 = 258`); `validate_p1_05.py` confirms the global count `144 = 144` in the two-component case. Both rerun for this dossier (§8).

**5. Classification.** Exposition/completeness: a proved addition; no existing frozen claim is altered.

**6. Consequences.** *Accept:* C4 becomes symmetric and complete; the manuscript can cite the count as a corollary. *Reject:* the count remains available only as the P1-05 proposal; the characterization (the mathematically essential part) is unaffected. *Defer:* harmless; can be decided together with manuscript drafting.

**7. Recommended disposition: APPROVE** — fully proved and verified; pure completion. (If the Boss prefers a minimal-diff philosophy for C4, REJECT is defensible and costs only a citation label.)

---

## PC-5 — State in T1 that global codes are `A`-submodules with fixed labels

**1. Exact frozen statement affected** (`02_THEOREM_BLUEPRINT.md`, T1): “Har component code `C_s ⊆ K_s[x]/(M_s)` ka ekmatra monic generator `M_s` ka divisor hai, isliye `a ↦ C_s(a)` ek bijection hai … CRT se global codes `A`-par `⟷` assignments ka product. Kul ginati `(P+1)^{Σ_s |F_s|}`.” The component-level statement is complete; the global step invokes “global codes” without saying what a code over `A` is.

**2. Exact proposed change.** Add to T1 (or to §0’s global model): “Global code se arth hai `A^n` ka `A`-submodule (fixed labeled CRT decomposition `A ≅ ∏_s K_s` ke tahat); component codes `K_s`-linear hain, aur ginati labeled assignments ki hai, equivalence classes ki nahi.” (English gloss: a code over `A` is an `A`-submodule of `A^n` under the fixed labeled decomposition; counts are over labeled assignments.)

**3. Mathematical reason.** The product parametrization is a statement about `A`-submodules: an `A`-submodule of `A^n ≅ ∏_s K_s^n` decomposes as a product of `K_s`-subspaces (P1-05 Prop. 3.1(ii), via the component idempotents of `A`). For arbitrary `F_q`-linear subspaces of the underlying `F_q`-space, this is false in general — a subspace mixing different components need not be a product — so without the `A`-submodule clause, T1’s global bijection has a genuine scope hole. The project’s own scope lock already intends this (`04_PAPER_BLUEPRINT.md` §3, locks 1–2: “A-submodule … component labels and the CRT isomorphism are fixed … never over equivalence/isometry classes”), but the frozen theorem text does not carry it.

**4. Proof location and evidence.** `P1_05_PROOFS_T5_T6_COROLLARIES.md` (G3), Prop. 3.1 (assembly proved under exactly this hypothesis), §0 of `P1_06_MOMENT_PROOFS_C5_C6.md` (uniform labeled model). No counterexample is involved; this is a scope-precision issue. Register: P1-03 §6 review of T1 (“PC-5, wording only”), `04_PAPER_BLUEPRINT.md` §3.

**5. Classification.** Scope/exposition (the proofs already work under the intended definition).

**6. Consequences.** *Accept:* T1/T6’s counts are unambiguously about the labeled `A`-submodule model that all proofs and validations use. *Reject:* the global statement stays open to a mixing-subspaces misreading; the defense would have to cite the paper blueprint instead of the theorem file. *Defer:* tolerable internally, risky at manuscript stage.

**7. Recommended disposition: APPROVE** — aligns the frozen theorem with the model that was actually proved and computed.

---

## PC-6 — Mark C6 “to be proved (RR-8)” — now superseded

**1. Exact frozen statement affected** (`02_THEOREM_BLUEPRINT.md`, C6): “Variance: Orbit-swatantra yog; `L=1` …, `L=2` …, `L≥3` … — teeno cases ke band sutra (closed forms) Phase 4 me `P` ke parimaani (polynomial) roop me nikale jayenge. **[RR-8]**” At the time PC-6 was registered (P1-03), no closed forms existed, and GAP-06 required C6 to be marked as unproved wherever summarized, lest a summary overclaim a variance theorem.

**2. Exact proposed change (as registered).** Add the marking “to be proved (RR-8)” to C6 and to any summary of it, until RR-8 is discharged.

**3. Mathematical reason — and why the situation changed.** The marking was a truth-in-labeling device during P1-03…P1-05. Since then, `P1_06_MOMENT_PROOFS_C5_C6.md` §3 (Theorem 3.7) proves the closed forms: parity-split `Var(S_1)`; `Var(S_2) = P(P+2)(P²+2P+3)/(18(P+1)²)`; `Var(S_L) = L·P(P+2)(P²+2P+2)/(60(P+1)²)` for `L ≥ 3`; globally `Σ_{s,O} w_O² Var(S_{L_O})`. RR-8 is therefore discharged mathematically, and a “to be proved” label would now be **false**.

**4. Proof location and evidence.** `P1_06_MOMENT_PROOFS_C5_C6.md` §§1, 3 (Lemmas 1.2, 3.2, 3.3, 3.5; Props. 3.1, 3.4, 3.6); `code/validate_p1_06.py` exact-rational verification (rerun, §8). Register: GAP-06 and the P1-06 outcome.

**5. Classification.** Exposition/status accuracy.

**6. Consequences.** *Accept (as worded):* the blueprint would assert the variance is unproved — now incorrect; would need immediate re-amendment after integration. *Reject:* C6’s frozen program sentence (“closed forms will be derived in Phase 4”) temporarily remains, which is now an understatement rather than an overclaim; the accurate fix is a different edit (below). *Defer:* leaves a stale status label question open with no benefit.

**7. Recommended disposition: REJECT as superseded.** The protective intent of PC-6 is fully honored by recording here (and in GAP-06) that RR-8 was open until P1-06 and is now proved. The correct follow-up edit — replacing C6’s program sentence by the P1-06 Theorem 3.7 formulas — is **not** PC-6 as registered and must be proposed/decided as part of the integration command, e.g.: “C6 Variance: `Var(dim_{F_q} Hull_k) = Σ_{s,O} w_O² V_{L_O}(P)` with `V_1, V_2, V_L (L≥3)` as in P1-06 Theorem 3.7.”

---

## 7. Interaction note

PC-1 and the C6 replacement suggested under PC-6 are siblings: both repair blueprint corollaries whose mathematics is now settled (P1-06). Approving PC-1 without planning the C6-formula integration would leave the blueprint half-updated; the recommended sequencing is a **single** future approval/integration command deciding PC-1…PC-6 (this dossier’s recommendations: approve PC-1…PC-5, reject PC-6-as-worded while adopting the C6 formula replacement), applying all accepted changes as dated correction notes in one edit, and recording the Git hash. Until that command, **all six statuses remain PENDING and the frozen file remains untouched.**

## 8. Checks run for this dossier (unmodified scripts)

```
python3 code/validate_p1_03.py   # exit 0; output byte-identical to code/validation_p1_03_output.txt; ALL P1-03 EXTENDED CHECKS PASSED
python3 code/validate_p1_05.py   # ALL P1-05 MULTI-COMPONENT ASSEMBLY CHECKS PASSED
python3 code/validate_p1_06.py   # ALL P1-06 MOMENT CHECKS PASSED
```
These reruns support the evidence columns above (PC-1 means, PC-2 `σ ≠ ρ` placement, PC-4 counts, C6 formulas). They are finite computational evidence; the proofs cited are the actual warrants. No earlier proof or validation artifact was modified; `02_THEOREM_BLUEPRINT.md` is untouched (git diff empty), and **Gate G1 (novelty) remains open and untouched by this dossier** — none of PC-1…PC-6 concerns literature priority.
