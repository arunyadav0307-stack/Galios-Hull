# Phase-8 Contribution Boundary

**Audit date:** 2026-09-24
**Branch:** `arena/01a0c9d2-galios-hull`
**Mandatory base commit:** `703260d610b4980df25610694bbe6a04f937abbc`
**Decision:** `B. READY WITH NARROWED CONTRIBUTION CLAIMS`

This document separates the mathematical result that is proved in the repository from claims about external novelty or priority. It is not permission to call any component “first,” “new,” or “novel.”

## 1. Boundary rule

The repository can support a manuscript whose central claim is:

> Under explicit square-free, simple-root, compatible-twist, fixed-component, and labeled-factor hypotheses, we derive a self-contained exact joint generating polynomial for the `F_q`-dimension of a selected constacyclic code and the `F_q`-dimension of its code-first `k`-Galois hull. The polynomial factors over factor orbits and is represented by a weighted two-state transfer matrix and a cyclic trace. The result unifies the factor-support/lcm calculation with standard cyclic-word enumeration in this specified family.

The repository cannot support any of the following stronger statements:

- exact hull-dimension enumeration is new in coding theory;
- the present work is the first enumeration over a finite ring, affine algebra, non-chain ring, or constacyclic family;
- no prior weighted transfer or generating-function formulation exists;
- the primary affine article is the only prior work or definitively leaves a field-wide gap;
- the candidate-first and code-first duals or hull subspaces are identical;
- labeled counts are equivalence-class counts;
- an N1 histogram, factorization, twist, or quantum distance exists;
- a hull dimension by itself proves a quantum parameter or distance.

## 2. Claim-by-claim classification

Novelty classifications use only:

`KNOWN`, `STANDARD TOOL`, `ADAPTED`, `COMBINATION`, `EXTENSION`, `POTENTIALLY DISTINCT`, `NOT ESTABLISHED`, and `FUTURE WORK`.

| ID | Candidate claim | Mathematical status in this repository | External novelty classification | Safe manuscript wording | Prohibited wording |
|---|---|---|---|---|---|
| CB-01 | Square-free affine algebra decomposes into labeled finite-field components. | Proved with conditions. | `STANDARD TOOL` | “By CRT/reduced finite-algebra structure, under the stated hypotheses, ...” | “We introduce the CRT decomposition.” |
| CB-02 | Simple-root component ideals correspond to binary selections of irreducible factors. | Proved with conditions. | `STANDARD TOOL` | “We use the standard simple-root factor-selection model and prove the exact labeled bijection needed here.” | “We are the first to enumerate factor selections.” |
| CB-03 | Fixed-dimension hull enumeration exists in finite-field cyclic/negacyclic and restricted constacyclic families. | Verified or partially verified at the source scopes recorded in `CENTRAL_RESULT_COMPARISON.md`. | `KNOWN` | “Prior work gives fixed-dimension counts in narrower finite-field families.” | “No fixed-dimension hull enumeration was known.” |
| CB-04 | Fixed-dimension hull enumeration exists for cyclic serial chain rings and `Z4` families. | Verified from the accessible chain-ring theorem text and publisher records. | `KNOWN` | “Chain-ring and `Z4` results provide adjacent exact distributions, but their hypotheses differ.” | “The present ring enumeration is the first ring enumeration.” |
| CB-05 | Componentwise hull decomposition and lcm/reciprocal generators over restricted non-chain direct products. | Verified in adjacent records, with source-specific conventions. | `KNOWN` | “Restricted non-chain/direct-product literature supplies related component formulas.” | “The component hull decomposition is new.” |
| CB-06 | The frozen second-slot pairing, inverse-Frobenius reciprocal, extension exponent `d_s=e m_s`, and explicit relation `D_candidate=sigma^2(D_code-first)`. | Proved in the separate convention and invariance audits. | `EXTENSION` | “We fix and prove a code-first convention, then reconcile it explicitly with the candidate-first record.” | “The literature uses the same dual convention.” |
| CB-07 | The code-first hull support is `tau(J) minus J`, equivalently the forward cyclic `1-to-0` boundary statistic. | Proved with conditions; direct finite checks pass. | `COMBINATION` | “Combining the code-first reciprocal action with the lcm support gives the following boundary formula.” | “The `1-to-0` statistic itself is new.” |
| CB-08 | `b_O(epsilon)=sum epsilon_i(1-epsilon_(i+1))` is the standard cyclic number of `1-to-0` transitions, and for nonconstant words the number of one-runs/zero-runs. | Proved elementarily and checked against standard cyclic-word/run terminology. | `STANDARD TOOL` | “We use the standard cyclic transition/run statistic.” | “We introduce a new run statistic.” |
| CB-09 | The two-state matrix `T_w(u,z)` and `trace(T_w^a)` enumerate weighted cyclic binary words. | Proved with conditions; standard walk/trace identity independently checked. | `STANDARD TOOL` | “A two-state transfer matrix and the closed-walk trace yield the orbit polynomial.” | “The transfer matrix or trace mechanism is new.” |
| CB-10 | The factor-orbit boundary calculation and the weighted transfer product combine to give the exact joint polynomial for all distinct labeled selections in the frozen family. | Proved with conditions; finite direct/transfer checks pass. | `COMBINATION` and `POTENTIALLY DISTINCT` as an application-specific formulation | “We derive an exact weighted joint enumerator for the specified labeled square-free affine family.” | “We prove the first exact hull enumerator anywhere.” |
| CB-11 | The exact product is absent from every prior source. | Not established; final/corrected source records remain incomplete and no exhaustive priority audit is possible. | `NOT ESTABLISHED` | “The audit did not verify an exact prior theorem identical to the product.” | “No prior work contains this result.” |
| CB-12 | Total count, exact hull distribution, LCD count, mean, and variance follow from the product. | Proved with conditions; the two-cycle variance case is separately handled. | `COMBINATION` | “These are corollaries of the stated labeled product.” | “These corollaries establish priority.” |
| CB-13 | Burnside/Pólya enumeration of inequivalent codes. | Not part of the theorem chain. | `FUTURE WORK` | “Equivalence-class enumeration is outside scope.” | “The trace already counts inequivalent codes.” |
| CB-14 | Repeated-root or incompatible-two-modulus enumeration. | Not part of the theorem chain. | `FUTURE WORK` | “The theorem is simple-root and compatible-twist only.” | “The formula covers repeated roots or incompatible twists.” |
| CB-15 | Quantum codes, distances, optimality, or journal outcomes. | Not proved by the frozen package. | `FUTURE WORK` | “Quantum applications require separate construction and distance checks.” | “The hull enumerator gives a quantum distance/optimal code.” |
| CB-16 | N1 numerical validation. | Exact status remains `UNSPECIFIED — CANNOT VALIDATE`. | `NOT ESTABLISHED` | Exclude N1 from manuscript evidence. | Any N1 histogram, factorization, or PASS claim. |

## 3. Narrow contribution that remains defensible

The safe contribution is the **conditional exact joint enumerator as a self-contained application-specific synthesis**, not a priority claim about any individual ingredient. Its defensible features are the conjunction of:

1. a fixed reduced square-free affine product with possibly different labeled extension fields;
2. componentwise code-first second-slot `k`-Galois duality;
3. inverse-Frobenius reciprocal/root action with explicit `d_s=e m_s` exponent;
4. same-factor-set compatibility and explicit exclusion of incompatible twists;
5. the forward hull-support boundary with orbit weights `m_s deg(f)`;
6. an exact bivariate polynomial for code and hull dimensions over all distinct labeled factor selections;
7. exact labeled distribution and moment specializations, including the two-cycle variance exception;
8. separation of dual-subspace/support comparisons from the Gram-matrix dimension/LCD invariance result.

A manuscript may call this an **exact conditional labeled enumeration theorem**. It must call the transfer device standard and the overall external novelty boundary unresolved.

## 4. Required differentiation before a stronger claim

A stronger novelty or priority claim would require, at minimum:

- direct reading of the final publisher text of the 2026 affine article;
- direct reading of the corrected finite-field constacyclic article;
- a source-level search for exact joint generating polynomials, factor-orbit boundary statistics, and transfer products in square-free affine/non-chain settings;
- a precise comparison of labeled codes versus non-isometric/equivalence-class counts;
- a convention-by-convention comparison of code-first and candidate-first duals on extension components;
- an independently reviewed statement of what is mathematically new beyond the standard transition/trace device.

Until that work is done, the classifications `POTENTIALLY DISTINCT` and `NOT ESTABLISHED` must remain visible.

## 5. Manuscript guardrails

The abstract and conclusion may say “we derive,” “we prove,” or “under the stated hypotheses.” They may not say “first,” “new,” “novel,” “unique,” “complete prior gap,” or “state of the art.” The literature review must explicitly acknowledge the known finite-field, chain-ring, `Z4`, non-chain, average, and generalized-cyclic results listed in `CENTRAL_RESULT_COMPARISON.md`.

The code-first formulas remain frozen:

```text
sigma(a)=a^(p^k),
rho(a)=a^(p^(e*m_s-k)),
lambda_s^(1+p^(e*m_s-k))=1,
D_candidate(C)=sigma^2(D_code-first(C)).
```

The count remains labeled. N1 remains excluded. Repeated roots, incompatible twists, Burnside/Pólya quotients, and unconditional quantum claims remain outside the central theorem.

## 6. Phase-8 decision

The exact prior theorem match and a priority boundary are not established. Nevertheless, the repository supports a bounded manuscript contribution if all claims are narrowed as above. Therefore the Phase-8 decision is exactly:

> **B. READY WITH NARROWED CONTRIBUTION CLAIMS**

This decision does not upgrade any source transfer to `DIRECT`, does not convert `NOT ESTABLISHED` into a priority result, and does not make N1 manuscript evidence.
