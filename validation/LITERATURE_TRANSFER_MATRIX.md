# Literature Transfer Matrix — Phase 6

This matrix is the current closure record for literature-dependent statements relevant to the main theorem. The source-level facts are separated from transfer to the present code-first, square-free, simple-root, labeled factor-selection framework.

Transfer statuses use only: `DIRECT`, `DIRECT AFTER CONVENTION TRANSFORMATION`, `PARTIAL`, `NOT TRANSFERABLE`, and `UNVERIFIED`.

| Result | Source Convention | Present Convention | Transformation | Hypotheses Match? | Transfer Status |
|---|---|---|---|---|---|
| Primary source's square-free affine decomposition and component-code setting, arXiv:2412.08512v1, Sections 1–3 | Source affine algebra with its displayed `k`-Galois pairing and component notation | Fixed labeled `A\cong\prod_s K_s`, componentwise Frobenius, simple-root factor selections | Identify source components with `K_s`; retain fixed idempotent labels; use `d_s=e m_s` for extension components | Partial: broad decomposition overlaps, but present simple-root/labeled scope is narrower | PARTIAL |
| Source Section 2.2 candidate-first dual definition | `D_cand(C)={y:sum y_i sigma(c_i)=0}` | `D_code(C)={x:sum c_i sigma(x_i)=0}` | `D_cand(C)=sigma^2(D_code(C))` | Yes for finite-field-linear codes after explicit slot conversion | DIRECT AFTER CONVENTION TRANSFORMATION |
| Source Lemma 1 and Theorem 1 dual twist/reciprocal as displayed | Candidate-first definition displayed with rho-based dual twist and reciprocal | Code-first inverse-Frobenius reciprocal and twist | The rho formulas are the frozen code-first formulas; literal candidate-first equations select the sigma formulas | No as printed for non-involutory `sigma`; final publisher text remains unavailable | NOT TRANSFERABLE |
| Source affine Theorems 4–5: component dual twist and generator | Candidate-first source notation with displayed rho-based `h_S#` | Componentwise code-first dual, `d_s=e m_s`, inverse-Frobenius reciprocal | Apply the dual transformation and replace the base-field exponent with the component exponent | Partial: structural assumptions overlap; exact final theorem comparison remains incomplete | PARTIAL |
| Source affine Theorem 7: component hull decomposition and lcm generator | Source component dual/hull notation | Code-first lcm/intersection proof for labeled simple-root ideals | Convert the dual generator before applying the lcm argument | Partial: lcm structure overlaps, but source convention and scope require conversion | PARTIAL |
| Source affine Theorem 8 and Corollary 3.4: specialized hull dimensions and LCD-related consequences | Source repeated-root/order/multiplicity notation and displayed rho formulas | Simple-root binary factor-orbit formula and code-first LCD count | Match only after restricting hypotheses and converting the convention | No complete hypothesis/theorem-text match established | UNVERIFIED |
| Source quantum Lemma 7, Gray-map Lemma 9, and Theorem 10 | Source conditional Gray-map/EAQECC setting | No unconditional quantum theorem in the present paper | Requires separate construction, distance, and parameter verification | No complete match established | UNVERIFIED |
| Debnath–Prakash–Islam finite-field paper, DOI `10.1007/s12095-022-00591-6`, with correction DOI `10.1007/s12095-022-00602-6` | Finite-field constacyclic Galois-hull formulas/counts; exact corrected theorem text not read | Code-first affine component framework | Use only publisher/abstract background; do not import its count as the present product theorem | Not established at theorem level | UNVERIFIED |
| Sangwisut–Jitman–Ling–Udomkavanich cyclic/negacyclic paper, DOI `10.1016/j.ffa.2014.12.008` | Euclidean/Hermitian finite-field cyclic/negacyclic setting | Square-free affine product and `k`-Galois code-first setting | Classical hull/counting ingredients only; no exact product-theorem transfer | Partial, narrower source family | PARTIAL |
| Jitman–Sangwisut Hermitian-average paper, DOI `10.3934/amc.2018027` | Hermitian constacyclic average-dimension setting | General code-first `k`-Galois labeled enumerator | Use only average-dimension background | No exact joint-enumerator match | PARTIAL |
| Liu–Pan Galois-hull methods, DOI `10.1007/s10623-019-00681-2` | General finite-field Galois-hull methods | Component constacyclic factor selections | General method context only | Partial and abstract-level in this audit | PARTIAL |
| Any external theorem claiming the present labeled bivariate `u,z` product | No exact matching theorem verified | `E(u,z)=prod_s prod_O tr(T_{w_O}^{a_O})` under the stated hypotheses | No external theorem is substituted; present proof is self-contained | Not established | UNVERIFIED |

## Closure conclusion

The central enumerator is not presented as an imported literature theorem. The accessible source is used for subject context and convention reconciliation. Its displayed candidate-first dual formulas are not transferred as printed. The source-PDF limitation remains exactly recorded in the Phase-6 audit and claim ledger.

---

# Literature Transfer Matrix — Phase 7 final manuscript classification

The Phase-6 matrix above is preserved. This table is the final Phase-7 transfer record for manuscript preparation and supersedes earlier rows when their status is repeated.

Transfer statuses use only: `DIRECT`, `DIRECT AFTER CONVENTION TRANSFORMATION`, `PARTIAL`, `NOT TRANSFERABLE`, and `UNVERIFIED`.

| ID | Source result or claim | Present statement | Required conditions/transformation | Final transfer status |
|---|---|---|---|---|
| T7-01 | Primary square-free affine decomposition and component/idempotent setting (R1/R2). | Fixed labeled product `A ~= prod_s K_s` and componentwise factor-selection model. | Identify the source's components with the fixed labeled components; retain the present simple-root and dimension hypotheses. | `PARTIAL` |
| T7-02 | Source candidate-first pairing and dual definition (R2). | Frozen code-first pairing `sum c_i sigma(x_i)` and code-first dual. | Apply `D_candidate(C)=sigma_k^2(D_code-first(C))`; do not identify subspaces. | `DIRECT AFTER CONVENTION TRANSFORMATION` |
| T7-03 | Source displayed rho-based reciprocal and twist attached to its candidate-first display. | Code-first rho reciprocal and twist `lambda^{-p^{d_s-k}}`. | Convert the slot convention and replace the source base-field exponent by `d_s=e m_s` on extension components. | `NOT TRANSFERABLE` |
| T7-04 | Source affine component dual/hull generator structure (R2). | Component code-first dual generator and lcm hull. | Reprove using the transformed dual and present normalized reciprocal; match simple-root hypotheses explicitly. | `PARTIAL` |
| T7-05 | Source affine specialized hull-dimension/LCD statements (R2). | Present weighted support and all-selection product. | Source assumptions, factor order, and displayed convention do not give a complete hypothesis match. | `UNVERIFIED` |
| T7-06 | Finite-field constacyclic formula and restricted counts (R3/R4). | Component-level background for hull formulas and fixed-dimension counts. | Read the corrected full text before importing a theorem or theorem number; no product transfer is assumed. | `PARTIAL` |
| T7-07 | Cyclic/negacyclic finite-field hull and fixed-dimension enumeration (R5). | Classical factor and lcm ingredients in the simple-root labeled setting. | Restrict the citation to its cyclic/negacyclic finite-field hypotheses; do not infer affine extension or Galois product scope. | `PARTIAL` |
| T7-08 | Hermitian constacyclic average dimension (R6). | Average-dimension context only. | Hermitian square-order setting does not match the general code-first weighted joint enumerator. | `PARTIAL` |
| T7-09 | General Galois-hull generator-matrix/invariance methods (R7). | Separate Gram-matrix proposition and LCD/hull-dimension comparison. | Use only the finite-field linear algebra actually checked; no constacyclic enumerator is imported. | `PARTIAL` |
| T7-10 | Average Galois hull dimensions over finite fields and `R_{m,q}` (R8). | Motivation and comparison for mean values. | Average formulas are not the present exact all-code bivariate product. | `PARTIAL` |
| T7-11 | Hermitian hulls and quantum applications over a specific non-chain ring (R9). | No central quantum theorem; optional conditional context only. | Verify a separate Gray-map/construction/distance theorem before any application. | `NOT TRANSFERABLE` |
| T7-12 | Any external theorem exactly equal to `prod_s prod_O tr(T_{w_O}^{a_O})`. | Present weighted bivariate labeled enumerator. | No exact source theorem was verified; the present proof and validators stand independently. | `UNVERIFIED` |
| T7-13 | Any external equivalence-class/Burnside/Pólya enumeration. | No quotient count in the main theorem. | Requires a separately defined group action and stabilizer analysis. | `NOT TRANSFERABLE` |
| T7-14 | Any repeated-root result. | No repeated-root claim. | Main theorem assumes `gcd(n,p)=1` and simple-root factors. | `NOT TRANSFERABLE` |

## Phase-7 transfer conclusion

The only direct literature-to-manuscript transfer is the explicitly transformed comparison of the two dual-slot conventions. Structural and background results transfer only partially. The weighted bivariate enumerator, exact moments, and labeled-code product are not replaced by an external theorem; their status is `UNVERIFIED` as an external literature match and conditional/proved independently in the internal theorem audits.

---

# Phase-8 transfer additions and final gap characterization

**Audit date:** 2026-09-24
**Purpose:** add the theorem-level comparisons inspected in Phase 8 without deleting the historical Phase-6/Phase-7 matrix.

Transfer statuses remain restricted to: `DIRECT`, `DIRECT AFTER CONVENTION TRANSFORMATION`, `PARTIAL`, `NOT TRANSFERABLE`, and `UNVERIFIED`.

| ID | Source result | Present statement | Conditions and reason | Phase-8 transfer status |
|---|---|---|---|---|
| P8-T1 | Primary affine source's square-free component/hull setting and its explicit open enumeration statement. | Frozen labeled square-free affine component model and exact labeled enumerator. | Structural setting overlaps; the source's conclusion leaves enumeration open, but the final publisher theorem text is inaccessible and the source convention differs. | `PARTIAL` |
| P8-T2 | Primary source candidate-first dual definition. | Frozen code-first second-slot dual. | Apply `D_candidate(C)=sigma_k^2(D_code-first(C))`; retain distinct subspaces/supports. | `DIRECT AFTER CONVENTION TRANSFORMATION` |
| P8-T3 | Primary source displayed rho reciprocal/twist attached to the candidate-first display. | Frozen code-first rho reciprocal/twist. | The displayed operation is not the literal candidate-first consequence in non-involutory cases. | `NOT TRANSFERABLE` |
| P8-T4 | Talbi et al. cyclic serial chain-ring Proposition 8 fixed-hull-dimension count. | Exact labeled square-free affine bivariate product. | Chain ring has nilpotent layers and ordered partition data; no square-free field-product or target transfer product. | `PARTIAL` |
| P8-T5 | `Z4` cyclic fixed-2-dimension enumerations. | Exact labeled square-free affine bivariate product. | Ring, inner product, and dimension/type hypotheses differ. | `PARTIAL` |
| P8-T6 | 2026 finite non-chain direct-product component hull/lcm formulas. | Component code-first hull support and global product. | Restricted direct-product ring gives adjacent structural support only; no all-selection weighted trace product is stated. | `PARTIAL` |
| P8-T7 | Finite-field cyclic/negacyclic and restricted constacyclic fixed-dimension counts. | Full affine labeled distribution. | Source families are narrower; use only their stated background counts and factor/lcm ingredients. | `PARTIAL` |
| P8-T8 | Double cyclic and double/four circulant prescribed-hull enumerations. | Constacyclic factor-selection product over affine components. | Different generalized/quasi-cyclic code families and constituent parameter spaces. | `PARTIAL` |
| P8-T9 | Standard finite-state transfer matrix and `tr(A^a)` closed-walk identity. | Orbit polynomial `tr(T_w(u,z)^a)`. | Direct combinatorial identity; it does not transfer the algebraic hull-support identification. | `DIRECT` |
| P8-T10 | Any external theorem exactly equal to the central weighted bivariate product. | `E(u,z)=product_s product_O trace(T_(w_O)^a_O)`. | No exact source theorem was verified; final/corrected source comparison remains incomplete. | `UNVERIFIED` |

## Phase-8 transfer conclusion

The standard transfer mechanism is directly usable as combinatorial background. The candidate-first/code-first relation is directly usable only after the explicit convention transformation. Every source-specific hull enumeration or non-chain component theorem transfers only partially to the frozen target. No external theorem replaces the internally proved central product.
