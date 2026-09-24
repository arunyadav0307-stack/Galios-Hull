# Phase 6 Final Consolidation and Publication-Safety Audit

**Date:** 2026-09-24
**Branch:** `arena/01a0c9d2-galios-hull`
**Purpose:** final code-first theorem consolidation, literature-transfer closure, N1 search, independent end-to-end regression, and publication-safety review.

## 1. Executive conclusion

Phases 1–5 now form one conditional theorem chain. The square-free affine decomposition, finite-field components, constacyclic factor selections, frozen second-slot `k`-Galois convention, inverse-Frobenius reciprocal, twist compatibility, root action, factor permutation, lcm hull support, orbit boundary statistic, transfer matrix, global labeled enumerator, distributions, LCD count, mean, and variance are stated in one dependency order.

The candidate-first and code-first duals are not identified. Under the hypotheses of the convention-transformation theorem,

\[
D_{\mathrm{candidate}}(C)=\sigma_k^2\bigl(D_{\mathrm{code-first}}(C)\bigr).
\]

The dual-code and factor-support objects can differ. A separate restricted Gram-matrix proof gives equality of the two same-code hull dimensions and LCD decisions; this does not give equality of hull subspaces or support sets. The code-first inverse-Frobenius support formula remains the principal theorem.

The independent Phase-6 validator passes all listed finite cases and all 73 rank-two planes in `\mathbb F_8^3`. This is regression evidence, not a replacement for the conditional proofs.

The final publication-safety decision is conservative:

> **Manuscript-readiness verdict: `NOT READY — MATERIAL GAPS REMAIN`.**

The remaining material gaps are the unresolved transfer of a central external theorem at final/corrected source level, the exact novelty boundary, and the absent N1 specification/output. N1 is not used to support the main theorem or its numerical examples.

## 2. Frozen convention and notation

For a component `K_s=\mathbb F_{q^{m_s}}=\mathbb F_{p^{d_s}}`, where `d_s=e m_s`, the fixed maps are

\[
\sigma_{s,k}(a)=a^{p^k},\qquad
\rho_{s,k}(a)=a^{p^{d_s-k}}=\sigma_{s,k}^{-1}(a).
\]

The code-first pairing and dual are

\[
\langle c,x\rangle_{s,k}=\sum_i c_i\sigma_{s,k}(x_i),
\qquad
D_{\rm code}(C)=\{x:\langle c,x\rangle_{s,k}=0\ \forall c\in C\}.
\]

The candidate-first comparison dual is defined independently by

\[
D_{\rm cand}(C)=\{y:\sum_i y_i\sigma_{s,k}(c_i)=0\ \forall c\in C\}.
\]

The notation is deliberately not collapsed: equality, Frobenius conjugacy, semilinear isomorphism, dimension equality, hull-dimension equality, LCD equality, and support equality are separate claims.

## 3. Consolidated hypotheses

The complete standing-assumption block is in `new-paper-blueprint.md` under **Standing Assumptions for the Main Enumeration Theorem**. It separates global assumptions from result-specific assumptions.

### 3.1 Global assumptions

1. `q=p^e`, `e\ge1`, and `K_s=\mathbb F_{q^{m_s}}` are finite-field components of a fixed labeled square-free affine decomposition.
2. The affine presentation has monic square-free positive-degree relations and the reduced algebra is a finite product of the labeled fields `K_s`.
3. `n\ge1` and `\gcd(n,p)=1`, so every `x^n-\lambda_s` is simple-root for `\lambda_s\ne0`.
4. `\lambda_s\in K_s^\times`, and `0\le k<e` is the declared base-field Galois iteration parameter, extended componentwise without relabeling idempotents.
5. Component codes are the labeled factor-selection ideals `J_s\subseteq\mathcal F_s`; no rotation, automorphism, isomorphism, or code-equivalence quotient is taken.
6. Component dimensions are over `K_s`; global dimensions are over `\mathbb F_q`; an orbit of factors of `K_s`-degree `d_O` has weight `w_O=m_s d_O`.

### 3.2 Result-specific assumptions and exclusions

- The same-factor-set factor permutation, support, transfer, distribution, LCD, mean, and variance results require
  `\lambda_s^{1+p^{d_s-k}}=1`.
- The candidate-first comparison uses the equivalent same-family condition `\lambda_s^{1+p^k}=1`.
- Square-free/simple-root binary factor support excludes repeated-root multiplicities.
- The global enumerator requires independent component selections under the fixed CRT/idempotent decomposition.
- Convention transformation and Gram invariance require only finite-field linearity and the displayed pairings; constacyclicity is not needed for those two general claims.
- Incompatible twists are retained as direct diagnostics, but are not entered into the same-factor-set transfer matrix.
- Burnside/Pólya equivalence counts, repeated-root enumerators, two-modulus incompatible transfer, and unconditional quantum-distance claims are outside the main theorem.

## 4. Consolidated theorem chain

### 4.1 Square-free decomposition and factor selections — `PROVED WITH CONDITIONS`

The square-free affine algebra is reduced and decomposes by CRT into fixed labeled finite-field components. Each component constacyclic quotient is a simple-root principal-ideal product. Its distinct ideals are in bijection with subsets `J_s` of the monic irreducible factor set `\mathcal F_s`, with generator

\[
g_{J_s}=\prod_{f\in J_s}f,
\qquad
h_{J_s}=(x^n-\lambda_s)/g_{J_s}.
\]

The factor/ideal decomposition proves selection injectivity: if two selected subsets give the same monic generator ideal, unique factorization in the square-free quotient gives the same factor support. Therefore `2^{|\mathcal F_s|}` is a labeled factor-selection count, not an equivalence-class count.

### 4.2 Code-first dual and inverse-Frobenius reciprocal — `PROVED WITH CONDITIONS`

Applying `\rho_{s,k}` to the defining equation gives

\[
0=\rho_{s,k}\left(\sum_i c_i\sigma_{s,k}(x_i)\right)
 =\sum_i\rho_{s,k}(c_i)x_i.
\]

The ordinary Euclidean dual of the `\rho`-image, translated back, yields the normalized principal reciprocal

\[
f^{\#_{s,k}}(x)=
 f_0^{-p^{d_s-k}}\sum_{i=0}^{d}f_i^{p^{d_s-k}}x^{d-i}.
\]

The code-first dual generator is the reciprocal of the check polynomial using `\rho_{s,k}`, and its constacyclic twist is

\[
\lambda_s^{-p^{d_s-k}}.
\]

### 4.3 Formal convention-transformation theorem — `PROVED`

**Theorem.** Let `K=\mathbb F_{p^d}`, let `\sigma(a)=a^{p^k}` with `0\le k<d`, let `\rho=\sigma^{-1}`, and let `C\le K^n` be any finite-field-linear code. Define `D_code` and `D_cand` by the two displayed equations in Section 2. Then

\[
D_{\rm code}(C)=\rho(C^{\perp_E}),
\qquad
D_{\rm cand}(C)=\sigma(C^{\perp_E}),
\qquad
D_{\rm cand}(C)=\sigma^2(D_{\rm code}(C)).
\]

No constacyclic or square-free hypothesis is needed for this identity. For a constacyclic code, the two displayed dual generators use respectively the inverse-Frobenius and sigma Frobenius reciprocals, with twists `\lambda^{-p^{d-k}}` and `\lambda^{-p^k}`. The transformation is conjugacy, not literal equality unless the additional fixed-point condition makes `\sigma^2` act trivially on the relevant object.

### 4.4 Gram-matrix hull and LCD theorem — `PROVED`

Let `B` be a row basis of `C` and `G=B\sigma(B)^T`. For a codeword `vB`, the code-first hull equations have coefficient matrix `G` after the invertible change `v\mapsto\sigma(v)`. The candidate-first same-code equations give the left nullspace of the same `G`. Rank-nullity therefore gives

\[
\dim(C\cap D_{\rm code}(C))
=\dim(C\cap D_{\rm cand}(C))
=\dim(C)-\operatorname{rank}(G).
\]

Consequently the two conventions have the same same-code hull dimension and LCD decision. This proof does **not** claim `D_code=D_cand`, equality of hull subspaces, or equality of factor-labeled support sets.

### 4.5 Twist compatibility, root action, and factor permutation — `PROVED WITH CONDITIONS`

The code-first transformed twist is fixed precisely under the declared compatibility condition

\[
\lambda_s^{1+p^{d_s-k}}=1.
\]

Under it, `\sigma_{s,k}^2(\lambda_s)=\lambda_s`, and the normalized inverse-Frobenius reciprocal sends a root `\alpha` to the corresponding inverse-Frobenius reciprocal root. It preserves degree and irreducibility and defines a permutation

\[
\tau_{s,k}:\mathcal F_s\longrightarrow\mathcal F_s.
\]

The sigma and rho factor actions satisfy

\[
\tau_{\sigma}=\tau_{\rho}^{-1}
\]

on the compatible same factor set. The action need not be an involution; fixed points, 2-cycles, and longer cycles are all retained.

### 4.6 Hull support and boundary statistic — `PROVED WITH CONDITIONS`

For a selected factor set `J_s`, the code-first dual generator support is `\tau_{s,k}(\mathcal F_s\setminus J_s)`. The lcm/intersection proof gives the component hull support

\[
(\mathcal F_s\setminus J_s)\cap\tau_{s,k}(J_s)
=\tau_{s,k}(J_s)\setminus J_s.
\]

If an orbit is indexed by `\tau(f_i)=f_{i+1}` and `\varepsilon_i=1` means selected in the generator, the hull statistic is

\[
b_O(\varepsilon)=\sum_{i=0}^{a_O-1}
\varepsilon_i(1-\varepsilon_{i+1}),
\]

with cyclic indices. The hull dimension contribution is `w_O b_O`, where `w_O=m_s d_O`.

### 4.7 Boundary reversal and unequal weights — `PROVED WITH CONDITIONS`

The candidate-first orientation is the reversed boundary

\[
\sum_i\varepsilon_i(1-\varepsilon_{i-1}).
\]

For a Frobenius orbit, all factors have the same degree, so all positions have the same weight. Reversing the binary word bijects the two orientations and preserves both orbit length `a_O` and the weighted statistic. This includes `a_O=1` and `a_O=2`; no hidden assumption that `\tau` is an involution is used.

The claim is deliberately restricted. Unequal weights **within one reversed cycle** do not in general preserve weighted boundaries; the independent Phase-6 diagnostic gives forward weight `2` and reverse weight `4` for weights `(1,2,4)` and bits `(1,0,0)`. Unequal weights across distinct actual Frobenius orbits are allowed because each orbit is reversed independently and the global enumerator is a product.

### 4.8 Orbit polynomial, transfer matrix, and global enumerator — `PROVED WITH CONDITIONS`

For an orbit of length `a` and weight `w`, the matrix

\[
T_w(u,z)=
\begin{pmatrix}u^w&1\\u^wz^w&1\end{pmatrix}
\]

tracks code dimension and hull dimension on closed binary walks. The trace counts cyclic selections without choosing a distinguished starting point. Independence of labeled component selections gives

\[
\mathscr E(u,z)=
\prod_s\prod_{O\subseteq\mathcal F_s}
\operatorname{tr}\bigl(T_{w_O}(u,z)^{a_O}\bigr).
\]

Its specializations give total labeled-code count, the code-dimension distribution, the hull-distribution polynomial, the LCD count, and the first two moments. The exceptional `a=2` variance case is retained in the blueprint rather than silently applying an `a\ge3` formula.

## 5. Literature and source-PDF closure

### 5.1 Final local source-PDF check

The available local file is:

- `Galios hulls of constacclic codes over affine algebra rings'.pdf`
- SHA-256: `0db90bfbeda69ad1af231b81d92f24be3589ed15ac2e0ade6605ba7ad0ddc039`
- first-page record: `arXiv:2412.08512v1 [cs.IT] 11 Dec 2024`.

A final theorem-level spot check was performed on the locally available PDF content for Section 2.2, Lemma 1, Theorem 1, Theorems 2–5, Theorem 7, Theorem 8, and the later Gray-map/quantum results. The reproducible standard-library structural extraction is `validation/source_pdf_theorem_check.py`, with capture `validation/source_pdf_theorem_check.out`. The check confirms that the preprint prints:

1. the Galois product as `\sum_i\alpha_i\beta_i^{p^k}`;
2. the dual with the candidate in the first argument, `\langle\alpha,c\rangle_k=0`;
3. the displayed `h^\#` coefficients and constacyclic statement using the complementary inverse-Frobenius exponent in the source notation; and
4. the component lcm/hull construction and the later conditional Gray-map application.

This check is useful precisely because it exposes the convention issue; it does not authorize literal transfer of the source display to the frozen code-first theorem. The final/corrected publisher record and theorem-level applicability of the external finite-field result remain unresolved. For that remaining source record, the conservative status is:

> **SOURCE PDF AVAILABLE BUT THEOREM-LEVEL TEXT NOT INDEPENDENTLY VERIFIED** for the final/corrected publication applicability.

No theorem number, correction, DOI, or novelty claim has been fabricated. The local preprint check and the historical Phase-4 record are preserved separately.

### 5.2 Transfer matrix

`validation/LITERATURE_TRANSFER_MATRIX.md` is the authoritative Phase-6 transfer table. Its only transfer statuses are `DIRECT`, `DIRECT AFTER CONVENTION TRANSFORMATION`, `PARTIAL`, `NOT TRANSFERABLE`, and `UNVERIFIED`.

The central source convention is not imported as a proof of the present theorem. Broad decomposition and classical hull ingredients are partial background; the candidate-first source definition transfers only through the explicit `\sigma^2` transformation; the displayed source dual-generator formula is not transferred literally; quantum and external corrected-theorem claims remain unverified.

### 5.3 Historical preservation

`PHASE4_LITERATURE_CONVENTION_AUDIT.md` and `LITERATURE_CLAIM_LEDGER.md` are retained. Phase 6 adds the transfer matrix and does not rewrite historical Phase-4 conclusions.

## 6. Conservative scope audits

### 6.1 Novelty audit — `VERIFY`

The blueprint now claims only a conditional, self-contained theorem package and labels the external literature as background/convention-qualified. It does not claim priority, an exact novelty boundary, or a journal outcome. The novelty boundary requires a complete theorem-level comparison with the corrected/final source record and remains unresolved.

### 6.2 Quantum audit — `FUTURE WORK`

The source's Gray-map/EAQECC material is not treated as an unconditional consequence of the hull enumerator. No quantum distance, quantum parameter, entanglement count, or construction theorem is claimed for the present paper without separately verifying all hypotheses. The source-PDF check does not upgrade this scope.

### 6.3 Burnside/Pólya audit — `FUTURE WORK`

The enumerator counts distinct labeled factor selections. It does not quotient by automorphisms, rotations, or equivalence. Burnside/Pólya enumeration is not in the main theorem and no equivalence-class count is reported.

### 6.4 Repeated-root audit — `FUTURE WORK`

The condition `\gcd(n,p)=1` is explicit. Repeated-root multiplicities, nilpotent factors, and their hull statistics are excluded rather than silently covered by the square-free proof.

### 6.5 Incompatible-twist audit — `RESOLVED WITH CONDITIONS`

Direct dual and constacyclic-twist diagnostics are retained for incompatible examples. The dual may lie in a different constacyclic modulus; those cases are not placed in the same factor-set transfer matrix. A two-modulus enumerator is future work.

### 6.6 Abstract, conclusion, and example audit — `RESOLVED WITH CONDITIONS`

The abstract and conclusion in the blueprint now describe the result as conditional, labeled, and code-first; distinguish dual/support differences from hull-dimension invariance; and retain the N1 and source-verification limitations. Examples are finite illustrations only. N1 is not used as an example with fabricated parameters or a fabricated histogram.

## 7. N1 final repository/history/archive search

`validation/search_n1_specification.py` was upgraded for the final search. Its captured output is `validation/search_n1_specification.out`.

The search covers current source/document files, generated captures in aggregate, filenames, the current ZIP members and text contents, available PDF bytes/filenames (without treating binary matches as readable text), Git patch history, and Git-history filenames. The only N1 parameters explicitly recovered from repository evidence remain:

- `q=16`;
- `n=15`;
- proposed selection count `32768=2^15`.

The following remain absent and are not inferred:

- `lambda`;
- `k`;
- factorization;
- orbit decomposition;
- expected histogram/output.

Exact status:

> **N1: `UNSPECIFIED — CANNOT VALIDATE`.**

No substitute twist, Frobenius parameter, factorization, orbit list, histogram, or output has been created.

## 8. Independent end-to-end validation

The new standalone validator is `validation/phase6_end_to_end_check.py`, with the captured output in `validation/phase6_end_to_end_check.out`. It imports no earlier checker.

It tests:

- `\mathbb F_4`, `\mathbb F_8`, and `\mathbb F_{16}`;
- `k=0` and every admissible nonzero `k` in the listed fields;
- `\lambda=1`, compatible nontrivial twists where available, and incompatible nontrivial twists where available;
- direct defining-equation code-first and candidate-first annihilators;
- direct hull intersections versus the restricted Gram-matrix dimension;
- direct inverse-Frobenius reciprocal generators and factor permutations;
- code-first and candidate-first weighted support formulas;
- transfer-matrix enumerators versus direct enumeration of every selected factor set;
- injective generator selection; and
- all 73 rank-two planes in `\mathbb F_8^3` for the general convention/LCD check.

Every compatible case reports `direct=support=transfer`; every listed case has zero Gram, convention-relation, support, reciprocal-generator, and LCD failures. Incompatible cases are direct-only and explicitly excluded from transfer. The unequal-weight reversal diagnostic fails invariance as expected, documenting the theorem's weight condition.

The final captured line is:

> `PHASE6 END-TO-END CHECK: PASS`

This remains finite computational evidence only.

## 9. Phase-6 final status table

The table uses only the required Phase-6 final-status vocabulary.

| Area | Final status | Closure record |
|---|---|---|
| Standing global assumptions | `RESOLVED WITH CONDITIONS` | Consolidated in the blueprint and this audit. |
| Square-free decomposition and factor/ideal injectivity | `RESOLVED WITH CONDITIONS` | Conditional proof chain; labeled counts remain distinct from equivalence classes. |
| Code-first dual, reciprocal, root action, and compatible factor permutation | `RESOLVED WITH CONDITIONS` | Inverse-Frobenius derivation and hypotheses are explicit. |
| Convention transformation `D_cand=\sigma_k^2(D_code)` | `RESOLVED WITH CONDITIONS` | General finite-field-linear theorem, separate from constacyclic assumptions. |
| Gram hull-dimension and LCD invariance | `RESOLVED` | Restricted Gram proof; independent plane and factor tests pass. |
| Code-first hull support and boundary statistic | `RESOLVED WITH CONDITIONS` | Lcm support proof; equal orbit-weight restriction explicit. |
| Orbit polynomial, transfer matrix, global enumerator, distributions, LCD, mean, variance | `RESOLVED WITH CONDITIONS` | Square-free compatible labeled factor family only. |
| Independent end-to-end validator | `RESOLVED` | Direct, support, transfer, Gram, and 73-plane routes pass. |
| Incompatible-twist diagnostics | `RESOLVED WITH CONDITIONS` | Direct evidence only; two-modulus enumeration excluded. |
| Repeated-root extension | `FUTURE WORK` | Outside `\gcd(n,p)=1` theorem. |
| Burnside/Pólya equivalence enumeration | `FUTURE WORK` | No quotient or equivalence-class count claimed. |
| Quantum construction/distance | `FUTURE WORK` | Conditional literature application only. |
| Final source/correction theorem transfer | `VERIFY` | Local preprint convention spot check done; corrected/final applicability unresolved. |
| Novelty boundary | `VERIFY` | No priority claim; complete theorem-level comparison remains open. |
| N1 specification and output | `UNRESOLVED` | Final search found no `lambda`, `k`, factorization, orbit data, or histogram. |
| Manuscript source TeX/BibTeX | `NOT APPLICABLE` | No fake `.tex` or `.bib` files created at blueprint stage. |

## 10. Theorem-status ledger

The required theorem-status vocabulary is retained:

| Consolidated result | Theorem status |
|---|---|
| Square-free component decomposition | `PROVED WITH CONDITIONS` |
| Factor-selection/ideal injectivity | `PROVED WITH CONDITIONS` |
| Code-first inverse-Frobenius dual generator | `PROVED WITH CONDITIONS` |
| Formal candidate-first/code-first transformation | `PROVED` |
| General Gram hull-dimension/LCD identity | `PROVED` |
| Root action and compatible factor permutation | `PROVED WITH CONDITIONS` |
| Lcm hull support and boundary formula | `PROVED WITH CONDITIONS` |
| Transfer and global labeled enumerator | `PROVED WITH CONDITIONS` |
| Finite F4/F8/F16 and arbitrary-plane evidence | `COMPUTATIONALLY VERIFIED ONLY` |
| External theorem transfer and exact novelty boundary | `PARTIALLY PROVED` |
| Repeated-root, Burnside/Pólya, and quantum extensions | `FUTURE WORK` |

## 11. Package and reproducibility closure

The archive `Galios-Hull-main-files.zip` is rebuilt after the Phase-6 files and captures are finalized. It contains the source PDF under `references/source-paper.pdf`, the blueprint, all historical audits/captures, the literature transfer matrix, the independent Phase-6 validator and output, the final Phase-6 audit, the N1 search and output, and an updated `run_all_validations.sh`/README/manifest.

The clean-extraction test must confirm:

1. manifest paths exist exactly;
2. no `.git` directory is included;
3. the source PDF hash matches the local source evidence;
4. the extracted Phase-6 validator passes;
5. the extracted full validation suite passes, with N1 remaining `UNSPECIFIED — CANNOT VALIDATE`; and
6. no generated bytecode or hidden credentials are packaged.

Prior captures remain preserved; Phase 6 appends to `VALIDATION_REPORT.md` rather than rewriting historical evidence.

## 12. Final decision

**Phase-6 manuscript-readiness verdict:** `NOT READY — MATERIAL GAPS REMAIN`.

This is not a claim of mathematical disproof. It is the required conservative publication decision while the final/corrected literature theorem transfer, exact novelty boundary, and N1 artifact remain unresolved.
