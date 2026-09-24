# Phase-9 Theorem Dependency Graph and Numbering Plan

**Audit date:** 2026-09-24
**Base commit:** `2be1c505c4d79741bc5378bc20de0cd2d17b05e8`

The numbering below is a proposed manuscript map. It is not asserted as final journal numbering until the draft is typeset. The graph is acyclic and preserves the canonical 19-result architecture.

## 1. Main directed acyclic graph

```text
A. Square-free affine decomposition
   Proposition 3.1 / Result 1
        |
        v
B. Component constacyclic decomposition and factor selection
   Lemma 3.2 / Result 2
        |
        v
C. Code-first second-slot pairing and dual translation
   Proposition 4.2 / Result 3
        |
        v
D. Inverse-Frobenius normalized reciprocal
   Lemma 4.3 / Result 4
        |
        v
E. Root action
   Lemma 4.4 / Result 5
        |
        v
F. Compatible factor permutation
   Proposition 4.5 / Result 6
        |
        v
G. Code-first dual generator
   Theorem 4.6 / Result 7
        |
        v
H. Compatibility and same-twist criterion
   Proposition 4.7 / Result 8
        |
        v
I. Component hull support
   Theorem 5.1 / Result 9
        |
        v
J. Cyclic 1-to-0 boundary statistic
   Proposition 5.2 / Result 10
        |
        v
K. One-orbit polynomial
   Proposition 6.1 / Result 11
        |
        +--------------------------+
        |                          |
        v                          v
L. Transfer matrix             M. Local trace identity
   Proposition 7.2 / Result 12  Theorem 7.3 / Result 13
        |                          |
        +-------------+------------+
                      v
N. Global joint enumerator
   Theorem 8.1 / Result 14
                      |
                      v
O. Total labeled-code count
   Corollary 9.1 / Result 15
                      |
                      v
P. Exact hull-dimension distribution
   Corollary 9.2 / Result 16
                      |
                      v
Q. LCD count
   Corollary 9.3 / Result 17
                      |
                      v
R. Mean hull dimension
   Corollary 9.4 / Result 18
                      |
                      v
S. Variance, including the a=2 exception
   Corollary 9.5 / Result 19
```

The arrows from `K` to `L` and `M` mean that both the local polynomial identity and the transfer representation use the already-proved orbit statistic. `N` depends on both local descriptions but does not depend on any later corollary.

## 2. Separate convention-transformation branch

```text
C. Code-first second-slot pairing
        |
        v
CF. Candidate-first/code-first transformation
    Proposition 4.CF
        |
        v
CF'. Dual-code semilinear relation and source-convention comparison
```

`Proposition 4.CF` proves, for any finite-field-linear code under the two displayed pairings,

```text
D_code-first(C)=rho(C^perp_E),
D_candidate(C)=sigma(C^perp_E),
D_candidate(C)=sigma^2(D_code-first(C)).
```

This branch is used to explain literature transfer. It does not replace Result 3, Result 4, or Result 7, and it does not feed the code-first support formula as an equality of dual codes.

## 3. Separate Gram/invariance branch

```text
C. Two dual definitions
   |\
   | \
   |  +--> CF. Convention transformation
   |
   +----> G. Restricted Gram matrix
             Proposition 4.G
                 |
                 v
       same-code hull-dimension and LCD invariance
```

`Proposition 4.G` uses the restricted Gram matrix and rank-nullity. It establishes equality of same-code hull dimensions and LCD decisions. It does not establish equality of dual subspaces, hull subspaces, factor supports, or support orientations. It is not a prerequisite for the code-first global enumerator; it is a separate comparison result.

## 4. Proposed numbering map

The following map records the statement purpose, hypotheses, conclusion, proof source, dependencies, and classification for every result in the 19-result chain. IDs are proposed until the draft is typeset.

| Result | Proposed item | Statement purpose | Hypotheses | Conclusion | Proof source | Dependencies | Classification |
|---:|---|---|---|---|---|---|---|
| 1 | Proposition 3.1 | Decompose the affine algebra. | Monic square-free positive-degree relations over `F_q`. | `A ~= product_s K_s` with fixed labels and idempotents. | Phase-2 Sections 4.1–4.2; Phase-6 Section 4.1. | Section 2 definitions. | Known tool, derived under stated presentation. |
| 2 | Lemma 3.2 | Classify component codes. | `gcd(n,p)=1`; `lambda_s != 0`; simple-root factorization. | Component ideals biject with subsets `J_s subseteq mathcal F_s`. | Phase-2 Sections 4.2–4.3; Phase-6 Section 4.1. | Proposition 3.1. | Adapted/derived. |
| 3 | Proposition 4.2 | Fix the code-first pairing and translate its equations. | Finite-field component; `sigma` an automorphism. | `D_code-first(C)=rho(C^perp_E)` and the pairing is semilinear in the second slot. | Phase-2 Section 5; Phase-6 Section 4.2. | Definitions 2.5–2.8; Lemma 3.2 for code context. | Derived under convention. |
| 4 | Lemma 4.3 | Define the principal reciprocal. | Monic polynomial with nonzero constant term; finite-field automorphism `rho`. | The normalized `rho` reciprocal is monic, multiplicative, irreducibility-preserving, and invertible. | Phase-2 Section 6.1; Phase-6 Section 4.2. | Proposition 4.2. | Derived under convention. |
| 5 | Lemma 4.4 | Derive the root action. | `f(alpha)=0`; reciprocal from Result 4. | `alpha -> alpha^(-p^(d_s-k))`. | Phase-2 Section 6.2; Phase-6 Section 4.5. | Lemma 4.3. | Derived. |
| 6 | Proposition 4.5 | Establish a same-factor-set permutation. | Result 5 and `lambda_s^(1+p^(d_s-k))=1`. | `tau_(s,k)` bijects `mathcal F_s` and preserves factor degree. | Phase-2 Section 6.3; Phase-6 Section 4.5. | Lemma 4.4; irreducibility. | Derived with conditions. |
| 7 | Theorem 4.6 | Give the code-first dual generator. | Simple-root constacyclic component and code-first reciprocal. | The dual is generated by the normalized reciprocal of the check polynomial with twist `lambda_s^(-p^(d_s-k))`. | Phase-2 Section 7; Phase-6 Section 4.2. | Lemma 3.2; Proposition 4.2; Lemma 4.3. | Derived with conditions. |
| 8 | Proposition 4.7 | Separate compatible and incompatible twists. | Result 5 and the component root/twist calculation. | Compatibility preserves the factor set; failure changes the modulus to `x^n-lambda_s^(-p^(d_s-k))`. | Phase-2 Section 6.3; Phase-6 Section 4.5 and 6.5. | Lemma 4.4; Proposition 4.5; Result 7. | Derived with conditions. |
| 9 | Theorem 5.1 | Characterize the hull support. | Compatible square-free factor selections and code-first dual generator. | Hull support is `(mathcal F_s\J_s) intersection tau_(s,k)(J_s)=tau_(s,k)(J_s)\J_s`. | Phase-2 Sections 8–9; Phase-6 Section 4.6. | Lemma 3.2; Theorem 4.6; Proposition 4.5. | Derived with conditions. |
| 10 | Proposition 5.2 | Convert support to a cyclic boundary. | Orbit positions have equal factor degree; `epsilon_i=1` means selected. | Hull contribution is `w_O sum_i epsilon_i(1-epsilon_(i+1))`. | Phase-2 Sections 8–9; Phase-6 Sections 4.6–4.7. | Theorem 5.1; orbit decomposition. | Combination/derived. |
| 11 | Proposition 6.1 | Count one orbit directly. | Indexed cyclic binary words of length `a`; weight `w`. | `P_(a,w)(z)=2+sum_r 2 binom(a,2r)z^(rw)`, equivalently the composition form. | Phase-2 Section 11 and counterexample search. | Proposition 5.2. | Standard tool applied. |
| 12 | Proposition 7.2 | Encode local choices by a matrix. | Same orbit convention and destination weighting. | `T_w(u,z)=[[u^w,1],[u^w z^w,1]]`. | Phase-2 Section 10; blueprint Section 7. | Proposition 5.2; Proposition 6.1. | Standard tool applied. |
| 13 | Theorem 7.3 | Close the local cycle. | Indexed orbit positions and the matrix in Result 12. | `trace(T_w^a)` equals the weighted sum over all indexed cyclic selections. | Phase-2 Section 10; Phase-6 Section 4.8. | Proposition 7.2; cyclic indexing. | Standard tool applied. |
| 14 | Theorem 8.1 | State the central global enumerator. | All main assumptions; independent labeled selections; compatible orbits. | `E(u,z)=product_s product_O trace(T_(w_O)^a_O)` and coefficient interpretation. | Phase-2 Section 10; Phase-6 Section 4.8; blueprint Theorem 7.1. | Results 1, 9, 10, 12, 13. | Derived conditional central theorem. |
| 15 | Corollary 9.1 | Count all labeled codes. | Theorem 8.1 and factor-selection bijection. | `E(1,1)=2^(sum_s |mathcal F_s|)`. | Phase-2 Section 10; blueprint Proposition 7.2. | Result 14. | Corollary. |
| 16 | Corollary 9.2 | Obtain the hull distribution. | Theorem 8.1; uniform labeled selection interpretation. | `[z^H]E(1,z)` counts hull dimension `H`. | Phase-2 Section 12; blueprint Theorem 8.1. | Result 14. | Corollary. |
| 17 | Corollary 9.3 | Count LCD selections. | Positive orbit weights and zero-boundary characterization. | Every orbit is constant; LCD count is `2^(sum_s |mathcal O_s|)`. | Phase-2 Section 12; blueprint Proposition 9.1. | Results 14 and 16. | Corollary. |
| 18 | Corollary 9.4 | Derive the mean. | Uniform independent orbit selections. | Each orbit of length `a>=2` contributes `a w/4`; length 1 contributes zero. | Phase-2 Section 12; blueprint Proposition 9.2. | Result 14; indicator calculation. | Corollary. |
| 19 | Corollary 9.5 | Derive the variance. | Same uniform model; distinguish lengths 1, 2, and `>=3`. | Length 2 contributes `w^2/4`; length `a>=3` contributes `a w^2/16`; sum over independent orbits. | Phase-2 Section 12; blueprint Proposition 9.2. | Result 14; covariance calculation. | Corollary. |
| CF | Proposition 4.CF | Reconcile source and frozen dual conventions. | Any finite-field-linear code; paired definitions; no constacyclic hypothesis. | `D_candidate(C)=sigma^2(D_code-first(C))`. | Phase-5 Sections 4 and 7; Phase-6 Section 4.3. | Pairing definitions only. | Separate derived proposition. |
| G | Proposition 4.G | Prove numerical invariance without support equality. | Any finite-field-linear code; restricted Gram matrix. | Same-code hull dimensions and LCD decisions agree under the two pairings. | Phase-5 Sections 10–11; Phase-6 Section 4.4. | The two dual definitions; rank-nullity. | Separate derived proposition. |

## 5. Acyclicity audit

- No definition depends on a theorem or corollary.
- Proposition 3.1 precedes the factor-selection lemma.
- The reciprocal and root-action lemmas precede the factor permutation.
- The dual generator and compatibility proposition precede hull support.
- The boundary statistic precedes both the orbit polynomial and transfer matrix.
- The trace identity precedes the global product.
- The global product precedes every count, distribution, LCD, moment, and variance corollary.
- The convention-transformation and Gram branches are separate and do not feed a later result that would identify the two duals.
- Computational validation is a post-theorem evidence section and is never a prerequisite of a proof.
- Literature comparison, figures, tables, and future work are non-proof material and are not graph prerequisites.

A topological ordering is therefore `A,B,C,D,E,F,G,H,I,J,K,(L,M),N,O,P,Q,R,S`, together with the independent `CF` and `G` branches. No backward edge or circular dependency is authorized.

---

# Phase-10C global-product repair amendment

**Date:** 2026-09-24
**Base:** `92a7eb2ba6472b95fe9306fb76e762477c836c01`

The Phase-10B audit identified that the component theorem chain did not explicitly connect the affine product code, global pairing, global dual, global hull, and global `F_q` dimensions to Theorem 8.1. The following acyclic bridge is now inserted before the component hull-support theorem is used globally:

```text
square-free affine decomposition (Proposition 3.1)
        |
        v
component factor-selection classification (Lemma 3.2)
        |
        v
Global CRT ambient module and code (Lemma 3.3)
        |
        v
Global Frobenius and A-valued code-first pairing (Lemma 3.4)
        |
        v
Global code-first dual decomposition (Lemma 3.5)
        |
        v
Global hull decomposition (Lemma 3.6)
        |
        v
Global F_q-dimension additivity (Proposition 3.7)
        |
        v
component hull support (Theorem 5.1)
        |
        v
weighted orbit boundary (Proposition 5.2)
        |
        v
orbit polynomial and transfer trace
        |
        v
Theorem 8.1 global labeled enumerator
        |
        v
Section-9 corollaries
```

The convention-transformation and Gram-invariance branches remain separate. The new global lemmas do not alter the reciprocal, factor-orbit, orbit-polynomial, transfer-matrix, or variance formulas; they supply the missing product-code and dimension bridge only.
