# Phase-9 Manuscript Figure Plan

**Audit date:** 2026-09-24
**Status:** design only; no figures are generated in Phase 9.

Figures must be mathematical diagrams prepared in the target journal’s permitted production format. Do not use AI-generated figures if the target venue prohibits them. Every figure must be checked against the notation audit before inclusion.

## Figure 1 — Overall mathematical workflow

- **Purpose:** show the proof pipeline from the square-free affine algebra to the labeled joint enumerator and its corollaries.
- **Mathematical content:** `A -> product K_s -> factor subsets J_s -> code-first dual/reciprocal -> tau-orbits -> b_O -> P_(a,w) -> T_w/trace -> E(u,z) -> distribution/LCD/moments`.
- **Caption draft:** “Logical workflow for the conditional labeled code/hull enumerator. Algebraic factor support is separated from the standard cyclic transfer calculation.”
- **Section location:** end of Section 1 or beginning of Section 3.
- **Dependencies:** Sections 2–9; Theorem dependency graph.
- **Must not show:** a quantum conclusion, an equivalence quotient, or an unsupported priority arrow.

## Figure 2 — Square-free affine decomposition

- **Purpose:** make the fixed labeled CRT decomposition and dimension weights visually explicit.
- **Mathematical content:** `A ~= product_s K_s`, idempotents, component moduli `M_s=x^n-lambda_s`, and global `F_q` weight `w=m_s deg(f)`.
- **Caption draft:** “Fixed labeled component decomposition used by the main theorem; labels are retained and are not quotiented by isometries.”
- **Section location:** Section 3.
- **Dependencies:** Proposition 3.1, Lemma 3.2, assumptions file.
- **Must not show:** repeated-root factors or an unqualified arbitrary finite ring.

## Figure 3 — Factor-orbit action and hull support

- **Purpose:** illustrate one compatible orbit and the forward boundary selected by the code-first hull.
- **Mathematical content:** `f_i -> f_(i+1)`, a binary selection word `epsilon`, the support `tau(J)\J`, and marked `1->0` edges.
- **Caption draft:** “A compatible reciprocal orbit converts the code-first lcm support into the cyclic `1-to-0` boundary statistic.”
- **Section location:** Section 5.
- **Dependencies:** Theorems 4.6–5.2; equal-degree orbit assumption.
- **Must not show:** a claim that candidate-first and code-first support labels are equal.

## Figure 4 — Two-state transfer matrix

- **Purpose:** explain the four entries of `T_w(u,z)`.
- **Mathematical content:** states `0` and `1`, destination selection weight `u^(w(1-t))`, and boundary factor `z^(w r(1-t))`; highlight the `1->0` entry `u^w z^w`.
- **Caption draft:** “Weighted two-state transitions for one factor orbit; the trace closes the indexed cycle.”
- **Section location:** Section 7.
- **Dependencies:** Proposition 5.2, Proposition 7.2, Theorem 7.3.
- **Must not call:** the matrix itself new or novel.

## Figure 5 — Local-to-global generating function

- **Purpose:** show multiplication of independent orbit polynomials into `E(u,z)`.
- **Mathematical content:** orbit traces `trace(T_(w_O)^a_O)` multiplied over `O` and `s`, followed by coefficient extraction `[u^K z^H]`.
- **Caption draft:** “Independent labeled orbit selections multiply to the exact joint code-dimension/hull-dimension generating polynomial.”
- **Section location:** Section 8.
- **Dependencies:** Theorem 7.3, Theorem 8.1, Sections 3 and 5.
- **Must not show:** an equivalence-class quotient or an unsupported complexity guarantee.

## Production checklist

- Use one notation for `mathcal F_s`, `tau`, `a_O`, `w_O`, `b_O`, `T_w`, and `E`.
- Label every arrow as a definition, derivation, or specialization where ambiguity is possible.
- State in captions that counts are labeled and conditional.
- Supply source data or a reproducible construction for every plotted object.
- Do not use N1 or any incomplete numerical artifact in a figure.
