# Paper Blueprint — BP-01

**Command:** BP-01 — Paper Blueprint Preparation  
**Date:** 20 October 2026  
**Project:** *Exact Joint Enumeration of k-Galois Hull Dimensions of Repeated-Root Constacyclic Codes over Square-Free Affine Algebras*  
**Status:** Blueprint audit complete. This is **not** a manuscript draft and it does not close Literature Gate G1.

## 0. Rules used in this blueprint

- The theorem statements in `02_THEOREM_BLUEPRINT.md` remain frozen. BP-01 does not edit them.
- A suspected error is recorded in `04_BLUEPRINT_GAP_REGISTER.md`; it is not silently repaired in the frozen file.
- “PASS” below means internal mathematical consistency at blueprint level. It does not mean novelty, priority, or a completed formal proof.
- “Prototype passed” means only the finite cases actually run. It is never used as a substitute for proof.
- The paper’s headline object remains the **joint labeled enumerator**, not the existence of one hull generator or one hull-dimension formula.

---

## 1. Executive verdict

### 1.1 Mathematical verdict

The central repeated-root mechanism is coherent:

\[
x^n-\lambda_s=(x^{n_0}-\mu_s)^P,\qquad n=Pn_0,\quad P=p^\varrho,\quad \gcd(n_0,p)=1,
\]

codes are parametrized by exponents \(a_f\in\{0,\ldots,P\}\), the code-first dual has orbit exponents

\[
\beta_i=P-\alpha_{i-1},
\]

and, in the compatible case, the hull has local contribution

\[
w_O\sum_i \min(P-\alpha_i,\alpha_{i-1}).
\]

Consequently, the proposed transfer-trace enumerator

\[
E(u,z)=\prod_s\prod_O
\operatorname{tr}\!\left(T^{(P)}_{w_O}(u,z)^{L_O}\right),
\qquad
T^{(P)}_w(u,z)_{a,b}=u^{w(P-b)}z^{w\min(P-b,a)},
\]

passes the BP-01 internal audit, conditional on the formal RR-3 dual-generator proof being written correctly.

### 1.2 Important exception

The frozen C5 hull-mean formula is **wrong as written** when a \(\tau\)-orbit has length \(L_O=1\) and \(P>1\). The problem is already visible in the saved prototype distributions. The original C5 statement is preserved in `02_THEOREM_BLUEPRINT.md`; the counterexample and a proposed replacement are recorded as **GAP-01** in the gap register.

### 1.3 Literature verdict

BP-01 does **not** close Gate G1. Two findings make the next literature step more important, not less:

1. The accessible affine-algebra paper (L4) cannot safely be described as “simple-root only.” Its accessible text writes \(n=n'p^{e'}\), allows generator exponents between \(0\) and \(p^{e'}\), and derives a hull-dimension formula from \(\max\) terms. It therefore overlaps the individual hull-dimension part of the project under its own hypotheses and convention.
2. The multi-twisted paper (L8), in the arXiv text inspected, does not display a general \(\gcd(m_j,p)=1\) restriction in the definitions/theorems reviewed. Since constacyclic codes are the index-one case, its GPM machinery may cover repeated-root hull generators in principle.

Thus the defensible centre of the proposed paper is:

> the exact **bivariate labeled joint enumerator** for code dimension and code-first \(k\)-Galois hull dimension, its \((P+1)\)-state orbit transfer trace, the \(P=1\) recovery, and the resulting labeled counts/moments over fixed square-free affine components.

The individual hull formula must be positioned as the explicit multiplicity-orbit foundation for that enumerator, not promoted as an unsupported “first hull formula.”

---

## 2. Scope resolution: finite fields versus affine algebras

BP-01 wording mentioned finite fields, while the frozen project title and setting use square-free affine algebras. BP-01 resolves this only at the level of proof architecture; it does not change the frozen title or theorem scope.

### Layer A — one finite-field component

For one component field \(K_s\), prove the repeated-root parametrization, dual exponents, hull formula, and local orbit trace. This is the mathematical core.

### Layer B — dimension weight over \(\mathbb F_q\)

Convert a \(K_s\)-dimension to an \(\mathbb F_q\)-dimension using

\[
[K_s:\mathbb F_q]=m_s.
\]

This explains the weight \(w_O=m_s\deg_{K_s}(f)\).

### Layer C — labeled affine assembly

For a fixed labeled decomposition

\[
A\cong \prod_{s=1}^N K_s,
\]

take the Cartesian product of component choices. Global dimensions add, so the global enumerator is the product of component/orbit traces.

The finite-field case is the specialization \(N=1\), \(m_1=1\) (with the usual identification of the component field with the base field). The manuscript should prove the component theorem first and then assemble the affine theorem. It should not retitle the paper as finite-field-only without a boss/commander decision.

---

## 3. Frozen model and definition locks

The following points must be explicit in any eventual manuscript:

1. A “code over \(A\)” means an \(A\)-submodule of \(A^n\) under the fixed labeled CRT decomposition. Without that, the Cartesian-product parametrization is not a statement about arbitrary \(\mathbb F_q\)-linear subspaces mixing components.
2. Component labels and the CRT isomorphism are fixed. The count is over labeled exponent assignments, never over equivalence/isometry classes.
3. \(\lambda_s\in K_s^*\). The case \(\lambda_s=0\) is outside the constacyclic unit-twist setting.
4. \(P=p^\varrho\) with \(\varrho\ge 0\). The \(P\)-th root \(\mu_s\) of \(\lambda_s\) is unique because Frobenius is bijective on the finite field \(K_s\), including when \(\varrho\) exceeds the absolute degree \(d_s\).
5. Compatibility is componentwise:
   \[
   \lambda_s^{1+p^{d_s-k}}=1.
   \]
   Without it, the code-first dual lies in the transformed-twist quotient and the same-factor-set orbit product is not asserted.
6. The quotient \(K_s[x]/(x^n-\lambda_s)\) is generally nonreduced when \(P>1\). No proof may use square-freeness or CRT idempotents inside this component quotient. The PID divisor lattice is the correct tool.

---

## 4. Literature-claim classification after BP-01

### 4.1 Evidence grades

- **V — Verified at source level:** the claim was checked against an accessible publisher page, abstract, or full text for the stated limited scope.
- **P — Partially verified:** abstract/introduction/table or secondary quotation supports part of the claim, but theorem-by-theorem extraction is missing.
- **U — Unverified:** the project file asserts it, but BP-01 did not obtain sufficient source evidence.
- **X — Unsafe/contradicted wording:** the current wording should not be reused without correction after full-text comparison.

### 4.2 Claim-by-claim status

| Record | BP-01 classification | What is supported | What remains open / unsafe |
|---|---|---|---|
| Audit question: no inspected record combines repeated-root + Galois hull + affine components + all labeled codes + joint \((K,H)\) enumerator | **P** | No such combined statement was found in the sources inspected in BP-01. | This is not a proof of absence. MathSciNet/zbMATH/Scopus-style exhaustive searching remains Gate G1 work. No priority sentence is allowed yet. |
| L1 — Debnath–Prakash–Islam, finite fields, Cryptogr. Commun. 15 (2023) | **P / X for “simple-root” label** | Publisher abstract verifies a Galois hull-dimension formula and, under restrictions on \(q\), counts of constacyclic codes with a given Galois hull dimension. | The “simple-root only” label in Audit v1 is unsafe. The affine successor imports a factorization \(n=n'p^{e'}\); L1’s exact hypotheses, exponent range, counting restrictions, and whether its hull-only count includes repeated roots require full-text extraction. |
| L2 — Debnath–Prakash, average dimensions, AMC 19 (2025) | **V for abstract-level scope; P for hypotheses** | Publisher abstract verifies average Galois hull dimensions over finite fields and over \(R_{m,q}\), together with hull-dimension formulas and LCD constructions. | It does not, at abstract level, give the full joint labeled distribution. Exact length hypotheses remain for Phase 1. A mean alone cannot be the headline. |
| L3 — Debnath–Islam–Yadav–Prakash, small Galois hull dimensions, AMC 22 (2026) | **P** | AIMS abstract/introduction/summary table verify existence conditions for hull dimensions 1 and 2, including \(p\mid n\) and \(n=p^m\) cases, plus EAQECC examples. | Check A remains open: theorem-by-theorem extraction is still required before asserting that no general exponent formula or partial enumeration is present. |
| L4 — Debnath–Islam–Martínez-Moro–Prakash, affine algebra rings, Discrete Math. 349 (2026); arXiv:2412.08512 | **V for accessible arXiv scope; X for Audit v1’s “simple-root” description** | Accessible text gives affine-algebra Galois dual/hull generators, an \(\operatorname{lcm}\) hull generator, generator exponents \(0\le u\le p^{e'}\), a hull-dimension formula, and attainable-dimension set results under hypotheses including \(\gcd(\operatorname{ord}\lambda,n')=1\). | Publisher-version comparison, convention translation, exact component model, and the absence/presence of code-dimension joint counting remain Phase-1 checks. T4 cannot be advertised as the first individual repeated-root hull formula. |
| L5 — User’s predecessor manuscript | **V locally** | Local manuscript gives the simple-root labeled joint enumerator, transfer matrix, LCD count, mean/variance with short-orbit exceptions, and code-first convention. | It is the \(P=1\) target, not external novelty evidence. Its convention/proof wording must not be copied where the simple-root support argument was used. |
| L6 — Galois hulls of cyclic serial codes over a finite chain ring | **P** | Available descriptions support hull structure, an algorithm for Euclidean-hull parameters, and averages under a coprime-length chain-ring setting. | Different alphabet and length regime; keep as background only after bibliographic verification in Phase 1/5. |
| L7 — Quantum codes from Galois hulls over a finite non-chain ring, Entropy 28 (2026) | **P** | Publisher/full-text descriptions support component hull formulas and quantum constructions over that ring. | Not the square-free affine labeled joint enumerator. Do not use it to imply an EAQECC contribution for the present paper. |
| L8 — Eldin–Solé, generator polynomial matrices of Galois hulls of multi-twisted codes, FFA record / arXiv:2305.15237 | **V for arXiv definitions/theorems inspected; P for publisher identity** | The inspected text defines MT codes over \(\mathbb F_{p^e}\), gives GPM formulas for Galois duals/hulls, hull-dimension formulas via determinantal divisors, and self-orthogonal/LCD criteria. Constacyclic codes are index one. No general \(\gcd(m_j,p)=1\) condition was seen in the definitions/theorems inspected. | Check B is substantially answered at arXiv level but not closed: compare the published version and explicitly specialize its GPM result to a scalar repeated-root constacyclic code. Hull-generator novelty is therefore not available as a headline. |
| L9 — Repeated-root structure papers (Dinh school and others) | **V at publisher-abstract level for major records** | Publisher abstracts verify special-length structure/duals and, for length \(k^sl^mp^n\), LCD cyclic/negacyclic enumeration; for \(2\ell^mp^n\), structure/duals and LCD/self-dual enumeration; for \(\ell^tp^s\), classification/duals and self-dual/self-orthogonal results. | Exact theorem extraction remains Check C. The project may not claim that repeated-root generator/dual structure itself is new. |
| L10 — Pang–Zhu–Li, LCD repeated-root cyclic codes, J. Appl. Math. Comput. 56 (2018) | **V at publisher-abstract level** | Springer abstract verifies LCD criterion, minimum-distance results, and enumeration for repeated-root cyclic codes of length \(n'p^r\) over a finite field. | The project’s LCD result is a \(k\)-Galois affine/orbit corollary of the joint enumerator, not a standalone new LCD enumeration claim. |
| L11 — Hulls of cyclic codes over a local ring, Springer chapter (2026) | **P** | Bibliographic/abstract-level descriptions indicate hull generators/types and fixed \(p\)-dimension counts over a local ring. | Different ring world; no action unless Phase 1 finds an unexpected joint enumerator. |
| L12 — Derivative-twisted intersection dimensions of repeated-root cyclic codes, Mathematics 14 (2026) 2866 | **V at publisher-page level for its different object** | The paper studies Hasse-derivative images and derivative-twisted intersections via multiplicities/Lucas data, with exact dimension formulas. | It is not a \(k\)-Galois dual/hull enumerator. Keep only as terminology/watchlist protection. |

### 4.3 Status of mandatory Checks A–D

- **Check A (L3): OPEN.** Abstract/table evidence only; no theorem-by-theorem extraction yet.
- **Check B (L8): SUBSTANTIALLY ANSWERED, NOT CLOSED.** The arXiv text does not show the hoped-for simple-root exclusion. Published-version comparison and scalar specialization remain.
- **Check C (L9/L10): PARTIALLY ANSWERED.** Major special-length LCD/self-dual enumerations are verified at abstract level; a theorem-level distance table remains.
- **Check D (database searches): OPEN.** BP-01 used targeted web/publisher checks, not MathSciNet/zbMATH/Scopus exhaustive searches.
- **New Check E required (from BP-01): L1/L4 repeated-root comparison.** Extract the exact exponent parametrization, hull formula, counting restrictions, twist hypotheses, and convention from L1 and L4, then compare them line-by-line with T3/T4 and the marginal \(E(1,z)\).

### 4.4 Safe research-gap statement for internal planning

> In the sources inspected during BP-01, no statement was found that gives, for all labeled multiplicity assignments in the repeated-root case \(n=Pn_0\), a bivariate generating polynomial simultaneously recording the global \(\mathbb F_q\)-code dimension and the code-first \(k\)-Galois hull dimension over fixed labeled square-free affine components, factored as a product of traces of \((P+1)\times(P+1)\) transfer matrices and specializing at \(P=1\) to the predecessor’s labeled simple-root enumerator.

This is a **search finding**, not a priority claim. It may enter a manuscript only after Gate G1 is closed, and even then should be phrased as a scoped contribution statement rather than “first.”

### 4.5 Statements that remain unsafe

- “First repeated-root Galois hull formula.”
- “First enumeration of repeated-root LCD codes.”
- “The affine hull formula is new because earlier affine work was simple-root.”
- “The mean hull dimension is new” without comparison to average-dimension literature.
- Any EAQECC parameter claim derived from the enumerator without an independently proved distance.

---

## 5. Theorem-by-theorem audit

### 5.1 Summary table

| Item | BP-01 mathematical status | Novelty / proof note |
|---|---|---|
| T1 parametrization | **PASS, conditional on the \(A\)-submodule definition lock** | Routine PID/divisor-lattice proof. Structure itself overlaps classical repeated-root theory; the value is the uniform exponent model used for counting. |
| T2 reciprocal and compatibility | **PASS** | Multiplicativity extends to prime powers. The \(\lambda\leftrightarrow\mu\) compatibility equivalence proof is valid in characteristic \(p\). |
| T3 code-first dual exponents | **PASS as candidate; formal proof pending** | RR-3 route is sound without separability. Direct generator check passed in one GF(4) case. Literature may contain equivalent generator results, so position as explicit foundation. |
| T4 hull generator and dimension | **PASS as candidate, conditional on T3 + RR-5** | The \(\operatorname{lcm}\) argument works in the PID quotient. Individual formula overlaps L4/L8 territory; do not headline it as first. |
| T5 local transfer trace | **PASS** | Closed-walk expansion is exact, including \(L=1\). This is the combinatorial core. |
| T6 global joint enumerator | **PASS as candidate, conditional on T1–T5** | Main theorem. Independence is over components and \(\tau\)-orbits; coefficients count labeled assignments. |
| C1 total count | **PASS** | At \(u=z=1\), each orbit contributes \((P+1)^{L_O}\). |
| C2 code-dimension distribution | **PASS** | Exponents \(P-a_f\) run through \(0,\ldots,P\); the displayed geometric factor is correct. |
| C3 LCD count | **PASS mathematically** | Zero-hull words on an orbit are exactly all-\(0\) and all-\(P\). Novelty is only as a Galois/affine/joint-enumerator corollary. |
| C4 self-orthogonal / dual-containing | **PASS mathematically** | Edge criteria follow by termwise comparison of nonnegative sums. The dual-containing count needs the analogous matrix \(B_P^-\) written explicitly in a manuscript. |
| C5 mean | **MIXED: code mean PASS; hull mean FAILS as frozen** | See §7.4 and GAP-01. Do not use the frozen hull-mean display until the commander approves a corrected statement. |
| C6 variance | **OPEN, not false** | No closed form is frozen yet. \(L=1\), \(L=2\), and \(L\ge3\) must remain separate. |
| C7 EAQECC | **CONDITIONAL only** | No quantum parameter follows from enumeration alone. Use only with independently known distance and the standard EAQECC hypotheses. |

### 5.2 Proof-dependency map with BP-01 status

```text
T1 parametrization ───────┐
T2 reciprocal/τ ──────────┼──► T3 dual exponents ──► T4 hull formula ──► T5 trace ──► T6 enumerator
Euclidean-dual lemma ─────┘                                  ▲
lcm/intersection lemma ──────────────────────────────────────┘

T6 ──► C1, C2, C3, C4
T6 + probability on labeled assignments ──► C5 (after GAP-01 decision)
T6 + orbit moment calculation ──► C6 (open)
External distance theorem ──► C7 (conditional)
```

### 5.3 Proof obligations RR-1 to RR-9

| Obligation | BP-01 status | Remaining action |
|---|---|---|
| RR-1 divisor lattice in non-semisimple quotient | **Proof-ready** | Write via ideals of \(K_s[x]\) containing \((M_s)\); do not use idempotents inside \(K_s[x]/(M_s)\). |
| RR-2 \(\#\) multiplicativity on prime powers | **Proof-ready** | One explicit induction/multiplicativity line; predecessor lemma supplies the base mechanism. |
| RR-3 Euclidean dual without separability | **Route verified; formal write-up pending** | See §6. This is no longer the principal mathematical blocker, but the manuscript proof must be rewritten, not copied from a support/idempotent argument. |
| RR-4 twist calculation with \(M_s=\bar M_s^P\) | **Route verified; validation incomplete** | The algebra is standard, but the current prototype does not discriminate \(\rho\) from \(\sigma\) and uses \(\lambda=1\). Prototype-2 must test this. |
| RR-5 intersection equals \(\operatorname{lcm}\) ideal | **Proof-ready** | Prove by lifting ideals to the PID \(K_s[x]\). |
| RR-6 closed-walk expansion | **Proof-ready** | Routine; take care with row/column orientation and \(L=1\). |
| RR-7 global assembly | **Proof-ready after definition lock** | State fixed labels, \(A\)-linearity, global pairing, and \(\mathbb F_q\)-dimension conversion in one hypothesis block. |
| RR-8 variance closed forms | **Open** | Phase 4 only; derive and symbolically/numerically test \(L=1,2,\ge3\). |
| RR-9 EAQECC conditions | **Conditional / optional** | Include only if a concrete code has independently proved distance. Otherwise omit or state as a conditional remark. |

---

## 6. RR-3 investigation: dual generator in the non-separable case

### 6.1 Question

Let \(K\) be a finite field, \(M(x)=x^n-a\) with \(a\ne0\), \(G\mid M\) monic, and \(H=M/G\). Does the Euclidean dual of \(\langle G\rangle\subset K[x]/(M)\) equal \(\langle H^*\rangle\) in the \(a^{-1}\)-constacyclic quotient when \(M\) is not separable?

### 6.2 BP-01 conclusion

**Yes — the coefficient proof does not require separability.** The proof uses only:

- \(GH=x^n-a\);
- \(G(0)H(0)=-a\ne0\);
- non-wrapped shifts have distinct degrees;
- dimension counting.

No roots, idempotents, CRT decomposition of \(K[x]/(M)\), or multiplicity-free factorization is needed.

### 6.3 Proof skeleton to be formalized later

Write \(r=\deg G\), \(h=\deg H\), so \(r+h=n\). Let

\[
H^*(x)=H(0)^{-1}\sum_{i=0}^{h}H_i x^{h-i}.
\]

For \(0\le i<h\) and \(0\le j<r\), compare the coefficient pairing of \(x^iG\) and \(x^jH^*\). After the reversal in \(H^*\), the pairing is, up to the nonzero scalar \(H(0)^{-1}\), the coefficient of \(x^{h-i+j}\) in \(GH=x^n-a\). Since

\[
1\le h-i+j\le n-1,
\]

that coefficient is zero. Hence the span of the non-wrapped \(H^*\)-shifts is contained in the Euclidean dual.

Those shifts have degrees \(h,h+1,\ldots,n-1\), hence are linearly independent and span a space of dimension \(r\). The Euclidean dual also has dimension \(r\). Therefore the spaces are equal. Finally, \(H^*\) divides the normalized reciprocal of \(M\), namely \(x^n-a^{-1}\), so that span is the corresponding constacyclic ideal.

### 6.4 From Euclidean dual to code-first dual

The correct convention step is

\[
D_{\mathrm{CF}}(C)=\rho(C^{\perp E}),
\]

where \(\rho\) acts coordinatewise. Equivalently, use the coefficientwise field automorphism on polynomials. It descends to a quotient isomorphism from the \(a^{-1}\)-twist quotient to the \(a^{-p^{d-k}}\)-twist quotient and sends the generator \(H^*\) to the normalized polynomial \(H^\#\).

Under compatibility \(a^{-p^{d-k}}=a\), the dual is an ideal in the original quotient. If

\[
H=\prod_f f^{P-a_f},
\]

multiplicativity of \(\#\) on prime powers gives the orbit exponent formula

\[
\beta_i=P-\alpha_{i-1}.
\]

### 6.5 Pitfalls that must not enter the eventual proof

- Do **not** argue by saying that a repeated factor contributes a CRT component; in the nonreduced quotient it does not.
- Do **not** infer factor multiplicities from the root map alone; apply \(\#\) to the factorization of \(H\).
- Do **not** copy any predecessor wording that ambiguously applies \(\rho\) to dual equations or to the code in the wrong direction. The clean statement is \(D_{\mathrm{CF}}(C)=\rho(C^{\perp E})\).
- Do **not** claim that prototype agreement proves RR-3. BP-01’s finite direct-generator check is evidence only.

### 6.6 BP-01 finite check for RR-3

A temporary audit script compared, for GF(4), \(k=1\), \(\lambda=1\), \(n_0=5\), \(P=2\), all \(27\) exponent assignments:

- vector-space code-first dual obtained as the Frobenius image of the Euclidean nullspace;
- ideal generated by \(h^\#\) in \(\mathbb F_4[x]/(x^{10}-1)\).

The row spaces agreed for all \(27\) assignments. Because here \(d=2\) and \(k=1\), one has \(\rho=\sigma\); this check does **not** test the inverse-Frobenius distinction. See GAP-05/GAP-07.

---

## 7. Formula audits

### 7.1 Joint enumerator and transfer matrix

For a cyclic orbit word \(\alpha=(\alpha_0,\ldots,\alpha_{L-1})\), the diagonal entry of \(T^L\) expands over closed walks. With rows indexed by the previous exponent \(a\) and columns by the current exponent \(b\), every edge contributes

\[
u^{w(P-b)}z^{w\min(P-b,a)}.
\]

Thus

\[
\operatorname{tr}(T^L)=
\sum_{\alpha\in\{0,\ldots,P\}^L}
u^{w\sum_i(P-\alpha_i)}
z^{w\sum_i\min(P-\alpha_i,\alpha_{i-1})}.
\]

For \(L=1\), the diagonal term is \(T_{a,a}\), giving \(\min(P-a,a)\), as required. Different components and different \(\tau\)-orbits use disjoint exponent coordinates, and both dimensions add; hence the global product in T6 is the correct labeled joint enumerator.

**Audit result: PASS.**

### 7.2 LCD count

On one orbit, the hull contribution is zero exactly when every term \(\min(P-\alpha_i,\alpha_{i-1})\) is zero. The only cyclic words with this property are

\[
(0,\ldots,0)\quad\text{and}\quad(P,\ldots,P).
\]

Indeed, if some \(\alpha_i=P\), the next edge forces the next exponent to be \(P\), and cyclicity propagates this around the orbit. If no exponent equals \(P\) but some \(\alpha_i>0\), the next edge is positive unless the next exponent equals \(P\), a contradiction. The \(L=1\) case is included because \(\min(P-a,a)=0\) only for \(a=0,P\).

Therefore

\[
\#\{a:\operatorname{Hull}=0\}=2^{\#\tau\text{-orbits}}.
\]

**Audit result: PASS mathematically.** Its literature position is corollary-level because repeated-root LCD enumerations already exist in special settings.

BP-01 also checked the exponent-word criterion exhaustively for \(P=1,\ldots,4\) and \(L=1,\ldots,5\).

### 7.3 Self-orthogonal and dual-containing criteria

Self-orthogonality \(C\subseteq D(C)\) is equivalent to equality of hull and code dimensions. On each orbit edge,

\[
\min(P-\alpha_i,\alpha_{i-1})\le P-\alpha_i,
\]

with equality exactly when

\[
\alpha_{i-1}+\alpha_i\ge P.
\]

Because all weighted edge terms are nonnegative, global equality forces termwise equality. Hence the self-orthogonal criterion and the count \(\prod_O\operatorname{tr}(B_P^{L_O})\) are correct.

Dual-containment \(D(C)\subseteq C\) similarly compares the hull contribution with \(a_{i-1}\) on each edge:

\[
\min(P-\alpha_i,\alpha_{i-1})=a_{i-1}
\iff
\alpha_{i-1}+\alpha_i\le P.
\]

The corresponding count should use \((B_P^-)_{a,b}=1\) if \(a+b\le P\), and \(0\) otherwise.

**Audit result: PASS.** BP-01 checked the two criteria against dimension equalities on all exponent words for \(P=1,2,3\) and \(L=1,\ldots,4\).

### 7.4 Mean hull dimension: frozen C5 fails on length-one orbits

For an orbit of length \(L\ge2\), each edge statistic has the same marginal law as \(\min(U,V)\), where \(U,V\) are independent uniform elements of \(\{0,\ldots,P\}\). Its expectation is

\[
\mu_P=\frac{P(2P+1)}{6(P+1)}.
\]

For \(L=1\), however, the previous and current exponents are the same variable \(A\). The statistic is

\[
\min(P-A,A),
\]

not the minimum of two independent uniforms. Its expectation is

\[
\nu_P=\frac{\lfloor P^2/4\rfloor}{P+1}.
\]

The frozen C5 uses \(\mu_P\) for every orbit and therefore fails when \(L=1\).

Counterexamples from the saved prototype cases:

| Case | Orbit data | Brute-force mean hull | Frozen C5 value |
|---|---:|---:|---:|
| \(n_0=3,\ P=2\) | three \(L=1\), \(w=1\) orbits | \(1\) | \(5/3\) |
| \(n_0=5,\ P=2\) | one \(L=1,w=1\); one \(L=2,w=2\) | \(23/9\) | \(25/9\) |

The frozen C5 mean code dimension,

\[
\mathbb E[\dim C]=\frac n2\sum_s m_s,
\]

is correct.

**Audit result: C5 code mean PASS; C5 hull mean FAIL as frozen.** The proposed replacement is recorded only in GAP-01 and requires a separate commander/boss-approved correction command before `02_THEOREM_BLUEPRINT.md` or any manuscript uses it.

### 7.5 Reduction at \(P=1\)

At \(P=1\),

\[
T^{(1)}_w(u,z)=
\begin{pmatrix}
u^w&1\\
u^wz^w&1
\end{pmatrix},
\]

which is exactly the predecessor transfer matrix with the same row/column convention. The edge statistic becomes \(a(1-b)\), the binary directed-boundary statistic.

The hull specialization satisfies

\[
\operatorname{tr}(T_w(1,z)^L)
=
2+\sum_{r=1}^{\lfloor L/2\rfloor}2\binom{L}{2r}z^{rw},
\]

including \(L=1\), where the value is \(2\). BP-01 checked this identity for \(L=1,\ldots,8\).

The total count, code-dimension marginal, LCD count, and self-orthogonal criteria also reduce correctly at \(P=1\).

The exception is the frozen C5 hull mean: at \(P=1\), \(\mu_1=1/4\), but a length-one orbit contributes \(0\), not \(w/4\). Hence the frozen C5 does **not** recover the predecessor’s mean when a length-one orbit is present. GAP-01’s proposed form does.

**Audit result: T5/T6 and C1–C4 PASS the \(P=1\) reduction; frozen C5 FAILS the \(P=1\) mean recovery on length-one orbits; C6 remains open.**

### 7.6 Variance

C6 is not yet a formula, so there is nothing false to preserve as a closed form. The dependency structure is nevertheless clear. Let

\[
X_i=\min(P-\alpha_i,\alpha_{i-1}).
\]

- \(L=1\): \(X_1=\min(P-A,A)\), a single-variable law.
- \(L=2\): the two edges share the same pair of variables; with \(U,V\) independent uniform,
  \[
  X_1+X_2=P-|U-V|.
  \]
  This is a genuine short-orbit exception.
- \(L\ge3\): nonadjacent edges are independent; only cyclically adjacent edges are dependent.

Any future closed form must be tested against brute-force second moments for several \(P,L\), and at \(P=1\) must recover the predecessor’s separate \(L=2\) variance term and zero \(L=1\) contribution.

**Audit result: OPEN (RR-8 / Phase 4), not a blocker for T6.**

### 7.7 Layer decomposition

The identity in `02_THEOREM_BLUEPRINT.md` §2,

\[
\min(P-\alpha_i,\alpha_{i-1})
=
\sum_{t=1}^{P}
\varepsilon_{i-1}^{(t)}
\left(1-\varepsilon_i^{(P-t+1)}\right),
\qquad
\varepsilon_i^{(t)}=1_{\{\alpha_i\ge t\}},
\]

is correct: for fixed \(t\), the summand is \(1\) exactly when \(t\le\alpha_{i-1}\) and \(t\le P-\alpha_i\). It remains a valid optional tool for moments or a layered one-orbit formula.

---

## 8. Proposed manuscript architecture

This architecture refines presentation only; it does not alter frozen statements.

1. **Introduction**  
   State the enumeration gap, the repeated-root multiplicity dial, the main enumerator, and the scoped literature position. Avoid all priority language until Gate G1 closes.

2. **Preliminaries and conventions**  
   Fixed labeled affine decomposition, component fields, code-first pairing, \(\sigma,\rho,\#\), compatibility, global pairing and dimension conversion.

3. **Repeated-root factorization and exponent parametrization**  
   Prove \(x^n-\lambda_s=(x^{n_0}-\mu_s)^P\), T1, T2, and the separable-factor \(\tau\)-action.

4. **Code-first dual and hull**  
   Prove the separability-free Euclidean dual lemma, T3, the \(\operatorname{lcm}\) lemma, and T4.

5. **Local orbit statistic and transfer matrix**  
   Prove T5, including \(L=1\) explicitly.

6. **Global joint enumerator over the affine algebra**  
   Prove T6 by labeled component/orbit independence; state the finite-field specialization and the \(P=1\) recovery.

7. **Counts and structural corollaries**  
   C1–C4: total, code marginal, hull marginal as \(E(1,z)\), LCD, self-orthogonal and dual-containing counts.

8. **Moments**  
   Mean only after GAP-01 is approved/corrected; variance only after RR-8 closes.

9. **Examples and computational validation**  
   Existing GF(4) cases, a direct dual-generator case, an affine multi-component case, an orbit of length at least \(3\), and moment checks. Clearly label computation as validation, not proof.

10. **Limitations and conclusion**  
    Compatible twists only; square-free \(A\) only; labeled counts only; incompatible-twist transformed modulus; no enumerator-only quantum-distance claim.

---

## 9. Computational validation plan

### 9.1 Evidence already available

The saved prototype checks GF(4), \(k=1\), \(\lambda=1\):

| \((n_0,P)\) | \(n\) | Assignments | \(\tau\)-orbit lengths |
|---:|---:|---:|---|
| \((3,2)\) | 6 | 27 | \(1,1,1\) |
| \((5,2)\) | 10 | 27 | \(1,2\) |
| \((7,2)\) | 14 | 27 | \(1,2\) |
| \((5,4)\) | 20 | 125 | \(1,2\) |

Total: \(206\) assignments. In BP-01 the script was rerun and its output matched `code/validation_output.txt` exactly, ending with `ALL PROTOTYPE CHECKS PASSED`.

BP-01 additionally checked:

- direct ideal-generator equality \(\langle h^\#\rangle=D_{\mathrm{CF}}(C)\) for all 27 assignments in the \((n_0,P)=(5,2)\) case;
- the LCD zero-word criterion for \(P=1,\ldots,4\), \(L=1,\ldots,5\);
- the self-orthogonal/dual-containing criteria for \(P=1,2,3\), \(L=1,\ldots,4\);
- the \(P=1\) hull-orbit polynomial for \(L=1,\ldots,8\);
- the frozen and proposed mean formulas against the two saved distributions containing \(L=1\) orbits.

### 9.2 Coverage gaps in the current prototype

The current evidence does **not** cover:

- a multi-component affine product;
- \(p=3\) or an odd-characteristic repeated-root case beyond word-level checks;
- nontrivial compatible \(\lambda\ne1\);
- \(\rho\ne\sigma\) (the GF(4), \(k=1\) case has \(d=2\), so \(\rho=\sigma\));
- a \(\tau\)-orbit of length \(L\ge3\);
- an independent direct test of \(h^\#\) across several fields/twists;
- variance formulas (none exist yet);
- edge cases \(n_0=1\), \(\varrho>d_s\), \(g=1\), and \(g=M_s\) as named tests;
- incompatible twists (outside the theorem; diagnostic only).

### 9.3 Prototype-2 acceptance matrix for a later command

A later Prototype-2 command should not be marked passed unless it includes:

1. A general finite-field implementation independent of the GF(4)-only script.
2. At least one case with \(\rho\ne\sigma\), for example a component with \(d_s=4\), \(k=1\) (so \(\rho\) has exponent \(3\) while \(\sigma\) has exponent \(1\)), checking \(D_{\mathrm{CF}}(C)=\rho(C^{\perp E})\) and the generator \(\langle h^\#\rangle\) directly.
3. At least one nontrivial compatible twist \(\lambda\ne1\).
4. At least one \(p=3\) repeated-root case.
5. At least one genuine multi-component affine case checking global \(\mathbb F_q\)-dimension weights and the product formula at vector level.
6. At least one \(\tau\)-orbit of length \(L\ge3\).
7. Brute-force first and second moments for \(L=1,2,\ge3\), ready to test the corrected mean (after approval) and the future variance formulas.
8. Named edge cases: \(n_0=1\), all-zero and all-\(P\) assignments, \(g=1\), \(g=M_s\), and a \(P=1\) regression against the predecessor formulas.
9. Saved script and saved output in the repo, with the exact command and environment recorded.

The minor prototype-docstring inconsistency (header emphasizes \(P=2\) although a \(P=4\) case is included) is a cleanup item only; BP-01 did not edit the code.

---

## 10. Novelty risks and planned responses

| Reviewer attack | Risk | Blueprint response |
|---|---|---|
| “The hull-dimension formula already appears in Debnath–Islam–Martínez-Moro–Prakash.” | **High** | Credit the earlier formula under its hypotheses/convention. Make the joint bivariate labeled enumerator and transfer trace the headline; use the orbit formula as the explicit foundation. |
| “Multi-twisted GPM theory already gives hull generators.” | **High** | Cite it as a general generator-matrix method. The contribution is the scalar multiplicity-orbit statistic and its exact joint counting over affine components, not a first hull generator. |
| “Repeated-root codes and duals were classified by Dinh and others.” | **Medium–high** | Agree for special lengths/structure. Distinguish the uniform \(n=Pn_0\) exponent-orbit enumerator, Galois action, affine assembly, and joint distribution. |
| “LCD enumeration is already known.” | **Medium** | Present LCD only as a corollary of the joint enumerator; cite Pang–Zhu–Li and the special-length enumerations. |
| “Average hull dimensions are already known.” | **Medium** | Do not headline the mean. If retained, derive it from the enumerator and handle \(L=1\) correctly. |
| “CRT assembly is routine.” | **Medium** | Be explicit that the new combinatorial content is local and repeated-root; the affine step is nevertheless necessary for the exact global \(\mathbb F_q\)-dimension enumerator under labeled components and component twists. |
| “Code-first versus candidate-first is only a convention.” | **Medium** | Keep the frozen convention, prove the transformation, and claim only the code-first generator/orbit form needed by the predecessor line. Do not claim that the dual subspaces are generally equal across conventions. |
| “Where are the new quantum codes?” | **Controllable** | Make no quantum-distance claim from \(E(u,z)\). Include C7 only with independently known distances, or omit it. |

---

## 11. Gate status and sequencing

- **BP-01 blueprint:** complete.
- **Mathematical core T1–T6:** blueprint-consistent, subject to formal proofs.
- **C5:** blocked by GAP-01 until a correction is explicitly approved.
- **C6:** open until Phase 4.
- **Literature Gate G1:** open; Checks A, C, D and new Check E remain, and Check B needs publisher-version closure.
- **Manuscript drafting:** not authorized by BP-01 and remains blocked by the project protocol until Gate G1 is handled.
- **Next recommended step:** one Phase-1 full-text theorem-extraction command covering L1/L4 first, with L3 and L8 closure included. The exact recommended command is given in the BP-01 report and gap register.

---

## 12. Bottom line

The paper remains viable as an **enumeration paper**. Its centre should be T6, supported by T5 and by an explicit repeated-root orbit formula. BP-01 found one real formula error (C5 on \(L=1\) orbits), one unresolved moment problem (C6), and a materially higher literature-overlap risk for the individual hull formula than Audit v1 suggested. None of these findings silently changes the frozen blueprint; all are routed through `04_BLUEPRINT_GAP_REGISTER.md`.
