# Blueprint Gap Register — BP-01

**Command:** BP-01 — Paper Blueprint Preparation  
**Date:** 20 October 2026  
**Purpose:** Record every suspected error, literature risk, proof gap, and validation gap found during BP-01 **without editing** the frozen statements in `02_THEOREM_BLUEPRINT.md`.

## Register rules

- **Original preserved:** BP-01 made no change to `02_THEOREM_BLUEPRINT.md`.
- A “proposed correction” in this register is not adopted until the Commander/Boss explicitly orders a correction command.
- Severity:
  - **Critical:** can invalidate a stated formula or the paper’s novelty positioning.
  - **High:** likely reviewer blocker or gate blocker.
  - **Medium:** must be repaired before manuscript submission, but does not invalidate T6 by itself.
  - **Low:** documentation/reproducibility cleanup.

---

## GAP-01 — Frozen C5 hull-mean formula is false for \(L_O=1\)

**Severity:** Critical (formula-level)  
**Location:** `02_THEOREM_BLUEPRINT.md`, C5  
**Status:** Open; original preserved  
**Blocks:** C5, the \(P=1\) mean-recovery check, and any manuscript use of the frozen mean display. It does not block T1–T6, C1–C4.

### Frozen statement under audit

\[
\mathbb E[\mathrm{Hull}]
=
\frac{P(2P+1)}{6(P+1)}
\sum_O w_OL_O.
\]

Its stated key says that an edge statistic \(\min(P-\alpha_i,\alpha_{i-1})\) is the minimum of two independent uniform variables on \(\{0,\ldots,P\}\).

### Finding

That independence statement fails for a length-one orbit. If \(L_O=1\), then \(\alpha_i=\alpha_{i-1}=A\), and the statistic is

\[
\min(P-A,A),
\]

not \(\min(U,V)\) for independent \(U,V\).

For \(L_O\ge2\), every individual edge still has marginal law \(\min(U,V)\), so the frozen coefficient is correct for those orbits. The failure is exactly the \(L_O=1\) case.

### Evidence

Define

\[
\mu_P=\frac{P(2P+1)}{6(P+1)},
\qquad
\nu_P=\frac{\lfloor P^2/4\rfloor}{P+1}.
\]

For one uniform \(A\in\{0,\ldots,P\}\),

\[
\mathbb E[\min(P-A,A)]=\nu_P.
\]

Counterexamples computed from the saved prototype distributions:

| Case | Orbit lengths/weights | Brute-force mean | Frozen C5 |
|---|---|---:|---:|
| \(n_0=3,\ P=2\) | \(L=1,w=1\) three times | \(1\) | \(5/3\) |
| \(n_0=5,\ P=2\) | \(L=1,w=1\); \(L=2,w=2\) | \(23/9\) | \(25/9\) |

For \(P=2\), \(\nu_2=1/3\), while \(\mu_2=5/9\). Hence the proposed split formula gives \(3(1/3)=1\) in the first case and \(1/3+(5/9)(2)(2)=23/9\) in the second.

The frozen formula also fails its claimed \(P=1\) recovery when an \(L=1\) orbit exists: at \(P=1\), it assigns \(w_O/4\) to such an orbit, whereas the predecessor’s length-one contribution is \(0\).

### Proposed correction — **not applied**

Replace the hull-mean part of C5, only after explicit approval, by

\[
\boxed{
\mathbb E[\mathrm{Hull}]
=
\mu_P
\sum_{O:L_O\ge2} w_OL_O
+
\nu_P
\sum_{O:L_O=1} w_O
}
\]

where

\[
\mu_P=\frac{P(2P+1)}{6(P+1)},
\qquad
\nu_P=\frac{\lfloor P^2/4\rfloor}{P+1}.
\]

At \(P=1\), \(\mu_1=1/4\) and \(\nu_1=0\), so the predecessor’s mean is recovered.

The C5 code-dimension mean

\[
\mathbb E[\dim C]=\frac n2\sum_s m_s
\]

passed the audit and is not part of this gap.

### Required action

A separate correction command must:

1. approve or reject the proposed replacement;
2. if approved, edit C5 in `02_THEOREM_BLUEPRINT.md` with a dated correction note;
3. add a proof that separates \(L=1\) from \(L\ge2\);
4. rerun the two counterexample cases and a \(P=1\) regression;
5. record the correction in `ARENA_WORKLOG.md`.

Until then, no draft may quote the frozen hull-mean formula.

### P1-01 update (20 Oct 2026) — independently confirmed; still not applied

P1-01 re-derived the \(L=1\) case from the actual exponent distribution and ran an exact stdlib-`fractions` check (`/tmp/p1_01_gap01_check.py`, temporary evidence, not a repo artifact; full record in `P1_01_FULL_TEXT_THEOREM_EXTRACTION.md` §8):

- For \(A\) uniform on \(\{0,\ldots,P\}\), \(\mathbb E[\min(P-A,A)]=\lfloor P^2/4\rfloor/(P+1)=\nu_P\); brute force matched \(\nu_P\) for every \(P=1,\ldots,20\).
- Full-orbit brute means matched the proposed split formula for \((P,L)\in\{1,2,3,4\}\times\{1,2,3\}\), matched the frozen formula exactly when \(L\ge2\), and failed exactly at \(L=1\).
- Counterexamples reproduced exactly: \((n_0,P)=(3,2)\): \(1\) vs frozen \(5/3\); \((5,2)\): \(23/9\) vs frozen \(25/9\).

**Decision:** GAP-01 remains **Open**. The split formula is confirmed as the correct candidate correction, but it is still **not approved and not applied**. A separate correction command is still required; `02_THEOREM_BLUEPRINT.md` was not edited during P1-01.

---

### P1-02 update (21 Oct 2026) — exact record made; still not applied

P1-02 (`P1_02_LITERATURE_CLOSURE.md` §4) recorded the length-1 identity exactly: for `A ~ Uniform{0,...,P}`, `E[min(P-A,A)] = floor(P^2/4)/(P+1) = nu_P`. This fully resolves the **first moment** for `L_O = 1` (every `P >= 1`); for `L_O >= 2` each edge has mean `mu_P = P(2P+1)/(6(P+1))` (distinct independent uniforms; linearity needs no edge independence), so `E[H_O] = w_O * L_O * mu_P`. The candidate split formula remains **unapproved and unapplied**; the frozen C5 display is unchanged. Still open: variance (C6) closed forms, dependence on formal T1-T4 proofs, the code-dimension mean bundled in C5, and the Boss's dated correction decision (now folded into P1-03).

**Decision:** GAP-01 remains **Open**. Status (f) of P1-02: derived and recorded; not approved, not applied.

---

### P1-03 update (21 Oct 2026) — formal derivation recorded; PC-1 proposed; still not applied

P1-03 (`P1_03_MATHEMATICAL_PROOF_PLAN.md` section 4) gives the formal derivation: for `L_O = 1`, `E[min(P-A,A)] = floor(P^2/4)/(P+1) = nu_P` (parity argument on `sum_a min(P-a,a)`); for `L_O >= 2`, each edge has mean `mu_P = P(2P+1)/(6(P+1))` (distinct independent uniforms; linearity only). The candidate split formula is now registered as **proposed correction PC-1** (P1-03 section 6). Vector-level counterexamples to the frozen display were reproduced by direct Gram-rank brute force: `GF(2), n0=7, P=2`: brute `11/3` vs frozen `35/9`; `GF(3)`/`GF(9)`, `lambda=1, P=3`: brute `2` vs frozen `7/2`; `GF(8), k=1, P=2`: brute `11/3` vs frozen `35/9`; in `L>=2`-only cases (`lambda=-1`) frozen = corrected = brute (`7/2`), confirming the error is exactly the `L=1` term. The frozen C5 code-dimension mean `(n/2) * sum_s m_s` was re-derived and is **correct**. Frozen blueprint unchanged.

**Decision:** GAP-01 remains **Open**. PC-1 awaits a separate approval decision; variance obligations are in GAP-06.

---
## GAP-02 — L4 affine-algebra paper overlaps repeated-root hull dimensions

**Severity:** Critical (novelty positioning)  
**Location:** `01_LITERATURE_AUDIT.md`, L4; affects T3/T4 positioning  
**Status:** Open; Gate G1 blocker

### Finding

Audit v1 describes L4 as the same affine alphabet but “simple-root.” That description is unsafe for the accessible arXiv text of Debnath–Islam–Martínez-Moro–Prakash, *Galois hulls of constacyclic codes over affine algebra rings* (arXiv:2412.08512).

The accessible text:

- writes \(n=n'p^{e'}\) with \(\gcd(n',p)=1\);
- factorizes \(x^n-\lambda\) with multiplicity \(p^{e'}\);
- writes a component generator with exponents \(0\le u\le p^{e'}\);
- derives the hull generator as an \(\operatorname{lcm}(g,h^\#)\);
- expands the hull-dimension formula using \(\max\) terms;
- gives attainable hull-dimension set results under additional hypotheses, including \(\gcd(\operatorname{ord}\lambda,n')=1\).

Therefore T4’s individual hull-dimension formula cannot be presented as new merely because it is repeated-root and affine.

### What may still distinguish the project

Subject to full-text confirmation:

- code-first rather than candidate-first generator convention;
- component fields \(K_s\) with \(\mathbb F_q\)-dimension weights \(m_s\);
- componentwise compatibility without the additional \(\gcd(\operatorname{ord}\lambda,n_0)=1\) hypothesis;
- all labeled exponent assignments counted jointly by \((\dim C,\dim\mathrm{Hull})\);
- \((P+1)\)-state transfer trace and \(P=1\) recovery;
- LCD/self-orthogonal counts and moments as consequences of the joint enumerator.

### Required action

In the next Phase-1 command, produce a theorem-by-theorem extraction for L4, including:

1. arXiv versus publisher-version differences;
2. exact alphabet/component model;
3. pairing convention;
4. twist hypotheses;
5. generator exponent range;
6. hull formula;
7. whether it counts codes by hull dimension, only lists attainable dimensions, or neither;
8. whether code dimension is recorded jointly;
9. a line-by-line overlap table against T3, T4, C3, C4, and the hull marginal \(E(1,z)\).

### P1-01 update (20 Oct 2026) — arXiv extraction done; publisher/domain closure still open

P1-01 completed the arXiv theorem-level extraction (record: `P1_01_FULL_TEXT_THEOREM_EXTRACTION.md` §3). Verified from arXiv:2412.08512:

- candidate-first pairing \(\langle\alpha,\beta\rangle_k=\sum_i\alpha_i\beta_i^{p^k}\) (§2.2, Eq. (2));
- Theorem 5 dual generator \(\tilde h(x)=\sum e_{S(\nu)}h_{S(\nu)}^\#\(x)\); Theorem 7 hull generator \(\sum e_{S(\nu)}\operatorname{lcm}(g_{S(\nu)},h_{S(\nu)}^\#)\);
- Theorem 8 repeated-root hull-dimension formula for \(n=n'p^{e'}\) under \(\gcd(\operatorname{ord}\lambda,n')=1\) and \(\operatorname{ord}(\lambda)\mid 1+p^{e-k}\), with exponents \(0\le u\le p^{e'}\);
- Corollary 3.5 counts **attainable dimension values**, not codes; the conclusion explicitly leaves counting codes by hull dimension over \(\mathcal A\) open;
- no joint \((\dim C,\dim\mathrm{Hull})\) enumerator, \((P+1)\)-state transfer trace, code-count by hull dimension, or mean/variance was found in the inspected text.

The publisher record (*Discrete Math.* 349(2), 2026, Art. 114750, DOI `10.1016/j.disc.2025.114750`) was verified at abstract/introduction/snippet level only. The repository PDF is arXiv v1, **not** the publisher PDF. Two cautions remain open: (i) publisher theorem numbering was not verified against arXiv numbering; (ii) §2.1 identifies idempotent components with fields \(\mathbb F_q(\nu_1,\ldots,\nu_\ell)\) while §2.3 presents projection codes/twists over \(\mathbb F_q\) — exact equivalence with the frozen labeled \(K_s\)-component model must not be asserted until reconciled.

**Decision:** **Partial overlap (strong)** for the individual repeated-root hull formula; **no counterpart found in inspected text** for T5/T6. GAP-02 remains open as a Gate G1 item until publisher/domain closure (see GAP-16).

---

### P1-02 update (21 Oct 2026) — publisher metadata verified; theorem equivalence still unresolved

Publisher record verified at metadata level: *Discrete Mathematics* 349(2), February 2026, Article 114750, DOI `10.1016/j.disc.2025.114750`, PII `S0012365X25003589`; zbMATH Zbl 1582.94185 (18 p.; MSC 94B15, 11T71; Full Text: DOI + arXiv). Publisher abstract/introduction match the arXiv scope. Spot consistency only: a publisher snippet headed "Theorem 4" opens exactly as arXiv Theorem 4, and the EAQECC "Lemma 7" snippet matches the arXiv pattern. The publisher numbering/hypotheses of arXiv Theorem 8 and Corollary 3.5 were **not** verified, and no snippet-level change in assumptions/results was observed (which is not proof of identity). The section 2.1/2.3 component-model reconciliation with the frozen labelled `K_s` model is still open.

**Decision:** GAP-02 remains open. Status (b) of P1-02: **Partial overlap (strong)** at arXiv level; publisher theorem-level equivalence unresolved.

---
## GAP-03 — L1 finite-field hull count may already include repeated roots

**Severity:** Critical (novelty positioning)  
**Location:** `01_LITERATURE_AUDIT.md`, L1; affects T4 and the hull marginal  
**Status:** Open; Gate G1 blocker

### Finding

The publisher abstract for Debnath–Prakash–Islam, *Galois hulls of constacyclic codes over finite fields*, Cryptogr. Commun. 15 (2023), verifies:

- a formula for Galois hull dimensions;
- under restrictions on \(q\), the number of constacyclic codes with a given Galois hull dimension.

Audit v1’s label “simple-root” was not verified from the abstract. Moreover, L4 imports from L1 a factorization of the form \(n=n'p^{e'}\), which strongly indicates that L1’s scope and counting restrictions must be extracted before the project describes L1 as simple-root only.

### Required action

Extract from L1:

1. standing hypotheses on \(n,p,q,\lambda,k\);
2. whether generator factors carry exponents \(0,\ldots,P\) or only binary selections;
3. the exact hull-dimension formula;
4. the exact counting theorem and its restrictions on \(q\);
5. whether the count is for hull dimension alone or jointly with code dimension;
6. whether \(\tau\)-orbit lengths are restricted;
7. overlap with T4, \(E(1,z)\), C3, and any mean formula.

Until this is done, the manuscript may not claim that counting repeated-root codes by Galois hull dimension is new.

### P1-01 update (20 Oct 2026) — still unresolved; “simple-root only” wording confirmed unsafe

P1-01 inspected the publisher abstract and the open correction (record: `P1_01_FULL_TEXT_THEOREM_EXTRACTION.md` §5):

- Abstract verifies a Galois hull-dimension formula and, under restrictions on \(q\), the number of constacyclic codes **for a given Galois hull dimension** over a finite field.
- Correction DOI `10.1007/s12095-022-00602-6` verifies repeated-root machinery: \(B_i\) sets defined via \(p^{el_1}\), \(p^{e-k}\), \(p^{i(e-k)}\), and “we prove that \(f^{i_1\#}(x)\ne f^{i_2\#}(x)\) for \(1\le i_1<i_2\le a_i\)”.
- No lawful open full text with theorem bodies was located; exact theorem numbers, hypotheses, exponent range, orbit restrictions, and whether the count is hull-only or joint with code dimension remain **unresolved**.

**Decision:** **Unresolved overlap — potentially critical.** Inaccessible full text is not evidence of absence. GAP-03 remains a Gate G1 blocker; closure is assigned to the single next command in GAP-16.

---

### P1-02 update (21 Oct 2026) — lawful-access search exhausted; still unresolved

P1-02 searched lawful routes for the repo L1 full text (exact queries in `P1_02_LITERATURE_CLOSURE.md` section 1): Springer and ACM records give metadata/abstract only; zbMATH Zbl 1518.94136 indexes "Full Text: DOI" only, with no open version; no arXiv/preprint or IIT Patna / IIIT Bhopal institutional-repository copy was found; no ILL could be executed from the workspace. A ResearchGate "Full-text available" snippet was **not** verified (fetched pages resolved to other papers) and an Academia.edu correction copy had unverified licence status; neither was used as evidence. The correction (DOI `10.1007/s12095-022-00602-6`, pp. 129-130; Zbl 1518.94137) is bibliographically verified, but its theorem-level effect is unverified. The exact unresolved questions are listed as L1-Q1...L1-Q8 in P1-02 section 1.3 (theorem numbers; hypotheses on `n`, `lambda`, `q`; exponent range; counting object; correction effect; project specialization).

**Decision:** GAP-03 remains a **Gate G1 blocker**. Status (a) of P1-02: **Unresolved / partial overlap (potentially critical)**. Closure now requires a Boss-supplied lawful copy (P1-03).

---

### P1-03 update (21 Oct 2026) — correction verified editorial; theorem text still unresolved

P1-03 (section 1) obtained new lawful evidence: OpenAlex (`W4283360609`) records repo L1 as `oa_status: closed`, `any_repository_has_fulltext: false`; Semantic Scholar (`4d023fda033d10a80723f94c8ac1a9c10469f6a5`) records `isOpenAccess: false` with an empty `openAccessPdf.url`. The Springer correction page (DOI `10.1007/s12095-022-00602-6`) is lawfully readable in full and lists exactly 10 items: two missing references added; "the/a primitive element"; a font-size display of the `B_i` sets (whose definitions, involving `p^{e l_1} +/- p^{i(e-k)}`, are now verified notation of repo L1); grammar repairs (some->a/an, unit->units); an `F_8` example listing; `i_1 <= i_2` -> `i_1 < i_2` in the proof sentence on distinct `#`-images; two reference-title repairs. **No listed item restates a theorem, hypothesis, or counting formula** — the correction is editorial/typographical in character (L1-Q7 narrowed). L1-Q1-Q6 and L1-Q8 remain unresolved; no theorem was inferred.

**Decision:** GAP-03 remains a **Gate G1 blocker for novelty purposes only**. Per P1-03, mathematical work proceeds without any novelty claim; Gate G1 re-vote still requires the theorem text or an explicit waiver.

---
## GAP-04 — Multi-twisted GPM theory may cover the hull generator

**Severity:** High  
**Location:** `01_LITERATURE_AUDIT.md`, Check B / L8; affects T3/T4 headlines  
**Status:** Partially answered; not closed

### Finding

In the arXiv text inspected for Eldin–Solé, *Generator polynomial matrices of the Galois hulls of multi-twisted codes* (arXiv:2305.15237), the definitions and theorem statements reviewed do not impose a general \(\gcd(m_j,p)=1\) condition. Multi-twisted codes are treated as modules over a PID, Galois dual/hull generator polynomial matrices are derived, and constacyclic codes are the index-one special case.

Thus the hoped-for answer to Check B — “multi-twisted theory is simple-root only” — is not supported by the inspected text.

### Remaining uncertainty

- The published Finite Fields and Their Applications version must be compared with the arXiv version.
- The general GPM theorem must be specialized explicitly to a one-block repeated-root constacyclic code to see exactly which parts of T3/T4 are corollaries.

### Required action

Produce a short specialization note:

\[
\text{MT GPM theorem}
\quad\Longrightarrow\quad
\text{scalar generator }h^\#\text{ and }\operatorname{lcm}(g,h^\#)
\]

or identify precisely where the specialization fails. In either case, the paper’s headline must remain the joint enumerator, not the hull generator.

### P1-01 update (20 Oct 2026) — arXiv extraction done; publisher numbering still unverified

P1-01 completed the arXiv theorem-level extraction for Eldin–Solé (record: `P1_01_FULL_TEXT_THEOREM_EXTRACTION.md` §4). Verified from arXiv:2305.15237: Definition 6 candidate-first Galois pairing; Theorem 8 (rank formula), Theorem 9 (dual twist type), Theorem 10 (dual GPM), Corollary 11 (hull MT type), Theorem 21 \(\dim(\mathcal Q_{\mathbf G})=\dim(\mathcal C)-\dim(h_\kappa(\mathcal C))\), Corollary 22 (self-orthogonal iff \(\mathfrak B_{\mathbf G}=\mathbf 0\)), Theorem 25 (determinantal-divisor dimension formula), Corollary 26 (LCD criterion), Theorem 28 (\(\mathfrak H_{\mathbf G}\mathbf G\) is a GPM for \(h_\kappa(\mathcal C)\)), Corollary 29. Block lengths carry no found general \(\gcd(m_j,p)=1\) restriction; index \(\ell=1\) is the constacyclic case under \(\Lambda^{-p^{-\kappa}}=\Lambda\). No labeled joint enumerator, transfer trace, moments, or code-count by hull dimension was found in the inspected text. The conclusion points future work to chain rings, not enumeration.

Publisher version verified bibliographically: *Finite Fields Appl.* 109 (Jan. 2026), Art. 102712, DOI `10.1016/j.ffa.2025.102712`. Publisher theorem numbering was **not** independently verified against arXiv numbering.

**Decision:** **Partial overlap (strong)** for hull-generator/dimension machinery. The headline must remain the joint enumerator. The explicit scalar index-1 specialization note is still required before any T3/T4 positioning sentence is drafted; GAP-04 remains open for that note and for publisher closure (GAP-16).

---

### P1-02 update (21 Oct 2026) — publisher numbering demonstrably differs from arXiv

Publisher record verified at metadata level: *Finite Fields and Their Applications* 109, January 2026, Article 102712, DOI `10.1016/j.ffa.2025.102712`, PII `S107157972500142X`; zbMATH Zbl 1576.94064 (25 p.; MSC 94B15, 13C10, 11T71; Full Text: DOI + arXiv). Abstract/introduction/conclusion snippets are scope-consistent with arXiv v1 (same `Q_G` dimension relation; same `Lambda^{-p^{-kappa}} = Lambda` hypothesis in Section 4). **But the numbering differs:** the publisher introduction names the main GPM result "Theorem 18" where arXiv v1 says Theorem 28, and the publisher Section 4 opening cites "Theorem 4"/"Corollary 7" where arXiv cites Theorem 8/Corollary 11. ArXiv theorem numbers must never be cited as publisher numbers. Full result-level equivalence of hypotheses/statements remains unverified without the publisher full text.

**Decision:** GAP-04 remains open for the index-1 specialization note and publisher closure. Status (c) of P1-02: metadata verified; numbering differs; full theorem equivalence unresolved.

---
## GAP-05 — RR-3 proof route is verified, but the formal proof is still unwritten

**Severity:** Medium  
**Location:** `02_THEOREM_BLUEPRINT.md`, RR-3 / T3  
**Status:** Open proof-writing task; not a mathematical blocker

### Finding

BP-01 verified that the Euclidean dual generator argument works without separability:

- compare coefficients of \(GH=x^n-a\) in degrees \(1,\ldots,n-1\);
- use non-wrapped shifts and dimension counting;
- identify \(D_{\mathrm{CF}}(C)=\rho(C^{\perp E})\);
- transport the generator to \(h^\#\) by the coefficientwise quotient isomorphism.

A finite check also confirmed \(\langle h^\#\rangle=D_{\mathrm{CF}}(C)\) for all 27 assignments in the GF(4), \((n_0,P)=(5,2)\), \(\lambda=1\) case.

### Why this remains a gap

- The project files do not yet contain the formal repeated-root proof.
- The finite check has \(d=2,k=1\), hence \(\rho=\sigma\); it does not test the inverse-Frobenius choice.
- Prototype success is not a proof.

### Required action

A later proof command must write RR-3 as a standalone lemma, with the pitfalls listed in `04_PAPER_BLUEPRINT.md` §6.5 explicitly avoided.

---

### P1-03 update (21 Oct 2026) — RR-3 proof route fixed in detail; formal write-up is the next command

P1-03 section 3 fixes the RR-3 route precisely: (a) dimension count `dim <h^*> = deg g`; (b) orthogonality by the coefficient-of-`x^{n-1}` identity using only `g h = x^n - lambda` and degree bounds — no roots, idempotents, or separability. RR-4 (twist transport `lambda^{-p^{d-k}} = lambda` under compatibility, generator `rho(h^*) = h#`) was verified algebraically and computationally, including the `GF(8), k=1` case where `sigma != rho`, so the Frobenius placement is genuinely tested. P1-03 also identified that the blueprint never states the dual-order sentence `D(C) = {y : <c,y> = 0 for all c in C}`; without it, `rho`/`sigma` swap. That lock is registered as proposed correction **PC-2** and as GAP-17.

**Decision:** GAP-05 remains **Open**; its write-up is exactly the recommended next command P1-04.

---
## GAP-06 — C6 variance has no closed form yet

**Severity:** High for Phase 4; Medium for the main paper  
**Location:** `02_THEOREM_BLUEPRINT.md`, C6 / RR-8  
**Status:** Open

### Finding

C6 currently promises separate closed forms for \(L=1\), \(L=2\), and \(L\ge3\), but no formulas have been derived or tested.

The dependency cases are genuinely different:

- \(L=1\): \(X=\min(P-A,A)\);
- \(L=2\): \(X_1+X_2=P-|U-V|\) for independent uniform \(U,V\);
- \(L\ge3\): only cyclically adjacent edge variables are dependent.

### Required action

Phase 4 must derive rational closed forms in \(P\), then test them against brute-force variances for multiple \(P\) and \(L\), including the \(P=1\) predecessor recovery. If closed forms become too unwieldy, C6 should be reduced in scope by an explicit commander decision rather than left as a vague promise.

---

### P1-03 update (21 Oct 2026) — exact moment obligations recorded; closed forms still open

P1-03 section 4.3 reduces the variance problem to explicit finite sums: the edge second moment `E[min(X,Y)^2]`; the `L=1` second moment `(1/(P+1)) sum_a min(P-a,a)^2`; the adjacent-edge covariance for `L>=3`, via `F(s) = s(2P-s+1)/(2(P+1))`, as `(1/(P+1)) sum_b F(P-b)F(b) - mu_P^2`; and the `L=2` opposite-edge covariance `E[min(P-A,B) min(P-B,A)] - mu_P^2`. Orbits are independent, so the global variance is the `w_O^2`-weighted sum over orbits. None of the simplifications to closed forms in `P` has been carried out.

**Decision:** GAP-06 remains **Open** (RR-8). C6 must be marked "to be proved" wherever summarized (proposed correction PC-6).

---
## GAP-07 — Prototype coverage is too narrow for the frozen hypotheses

**Severity:** High before manuscript drafting  
**Location:** `code/validate_repeated_root.py`, `code/validation_output.txt`, `03_RESEARCH_PLAN.md` Phase 2  
**Status:** Open

### Current coverage

- one field, GF(4);
- \(k=1\), \(\lambda=1\);
- \(P=2,4\);
- \(\tau\)-orbit lengths only \(1\) and \(2\);
- \(\rho=\sigma\) because \(d=2,k=1\);
- no multi-component affine product;
- no \(p=3\) case;
- no nontrivial twist;
- no direct dual-generator test in the saved prototype output.

### BP-01 temporary evidence

BP-01 reran the saved prototype and obtained an exact match with `code/validation_output.txt`. A temporary `/tmp` audit script also checked the direct dual generator in one case and several exponent-word identities. That script was not added to the repository during BP-01, so its evidence is reported in the blueprint but is not yet a reproducible project artifact.

### Required action

A later Prototype-2 command must satisfy the acceptance matrix in `04_PAPER_BLUEPRINT.md` §9.3 and save both script and output in the repo. In particular, it must include \(\rho\ne\sigma\), \(\lambda\ne1\), \(p=3\), a multi-component affine case, and an orbit of length at least \(3\).

---

### P1-03 update (21 Oct 2026) — coverage extended and executed; limitations recorded

New dependency-free script `code/validate_p1_03.py` (output `code/validation_p1_03_output.txt`, final line "ALL P1-03 EXTENDED CHECKS PASSED") adds vector-level Gram-rank brute force over `GF(2)` (k=0, P=2, n0=7), `GF(3)` (k=0, P=3, lambda=+1/-1, n0=4), `GF(9)` (k=1, P=3, lambda=+1/-1, n0=4), and `GF(8)` (k=1, P=2, n0=7; `sigma != rho`; orbit lengths 1 and **6**) — 2,806 new assignments, all matching the exponent formula and transfer trace, with LCD/self-orthogonal/dual-containing counts matching `2^#orbits` / `tr(B^L)` / `tr((B')^L)`. Orbit-statistics checks cover 31 `(P,L)` pairs (`P in {2,3,4,5,8,9}`, `L<=6`). The old prototype was rerun and passed, output identical to `code/validation_output.txt`. Limitations: single-component only; `lambda in {1,-1}`; vector-level `P = p` (rho=2 only via the old `GF(4), P=4` case); Gram method presupposes the A2 pairing order; finite checks are not a proof.

**Decision:** GAP-07 remains **Open** for the multi-component vector test and broader twists, but coverage is materially extended.

---
## GAP-08 — Global code definition and labeled decomposition need an explicit lock

**Severity:** Medium  
**Location:** `02_THEOREM_BLUEPRINT.md`, T1/T6  
**Status:** Open wording task

### Finding

T1/T6 use a Cartesian product over components. This is correct for \(A\)-submodules under a fixed labeled CRT isomorphism. It is not a parametrization of arbitrary \(\mathbb F_q\)-linear subspaces of \(A^n\) that mix components.

### Required action

The eventual Preliminaries must state, in one place:

- \(A\cong\prod_sK_s\) is fixed and labeled;
- codes are \(A\)-submodules of \(A^n\);
- component twists assemble as \(\lambda=(\lambda_s)\);
- the global code-first pairing is componentwise;
- dimensions in \(E(u,z)\) are over \(\mathbb F_q\);
- labels are not quotiented by algebra automorphisms or code equivalence.

No change to the frozen theorem statements was made in BP-01.

---

## GAP-09 — Checks A, C, and D remain open

**Severity:** High  
**Location:** `01_LITERATURE_AUDIT.md` §4  
**Status:** Open; Gate G1 remains open

### Finding

- **Check A:** L3’s small-hull results are verified at abstract/table level, but its theorems have not been extracted one by one.
- **Check C:** Major repeated-root LCD/self-dual enumerations are verified at abstract level, but no exact scope table has been produced.
- **Check D:** MathSciNet/zbMATH/Scopus-style database searches have not been performed.

### Required action

Close these in Phase 1. Until then, use no “first,” “new enumeration,” or priority wording in a manuscript.

### P1-01 update (20 Oct 2026) — Check A partial, Check C done at abstract level, Check D still open

- **Check A (repo L3): partially closed.** Abstract/introduction/Table 1 inspected for DOI `10.3934/amc.2025054`: existence only for hull dimensions 1–2 (Thm. 3.1: \(p\mid n\); Thm. 3.9: \(\gcd(p,n)=1\); Thm. 3.18: \(n=p^m\); Thm. 3.20: \(2p\mid n\)), then EAQECC examples. Theorem bodies were not exposed; exact surrounding hypotheses/conventions still need full-text confirmation. No counting/enumerator/moments verified.
- **Check B (repo L8): answered at arXiv level** — see GAP-04 P1-01 update. No general \(\gcd(m_j,p)=1\) restriction found; headline stays with the enumerator.
- **Check C (repo L9/L10): closed at publisher-abstract level.** Scope table recorded in `P1_01_FULL_TEXT_THEOREM_EXTRACTION.md` §6.4: \(k^s\ell^mp^n\) (DOI `10.1016/j.ffa.2024.102542`), \(2\ell^mp^n\) (DOI `10.1016/j.ffa.2014.11.006`), \(\ell^tp^s\) (DOI `10.1007/s12095-014-0106-5`), \(6\ell^mp^n\) (DOI `10.3934/amc.2021044`), and Pang–Zhu–Li general \(n=n'p^r\) cyclic LCD enumeration (DOI `10.1007/s12190-017-1118-z`). All are Euclidean/single-field (special lengths except L10); none gives the \(k\)-Galois affine joint enumerator.
- **Check D: still open.** MathSciNet/zbMATH/Scopus-style database searches were not performed in P1-01 and are assigned to GAP-16.

**Decision:** GAP-09 remains **Open** (Gate G1 still open) on Check A theorem bodies and Check D.

---

### P1-02 update (21 Oct 2026) — Check D performed and recorded; Check A still unresolved

Check D was executed on 21 October 2026 and is recorded with platforms, exact queries, results, and limitations in `P1_02_LITERATURE_CLOSURE.md` section 3. Platforms: general web discovery; SpringerLink/ScienceDirect/AIMS/ACM records; arXiv search (three exact phrase queries, all "produced no results"); zbMATH Open (fielded queries: 5 known documents for `ti:"Galois hulls" & any:constacyclic`; "No Documents Found" for repeated-root/Galois-hull and transfer-matrix/hull/enumeration combinations). **Not searched:** MathSciNet, Scopus, Web of Science, ILL catalogues — coverage is documented but non-exhaustive, and non-discovery is not novelty. No exact duplicate of the joint enumerator/transfer trace was found; the closest neighbours remain repo L1 (unresolved), repo L4 (dimension values only), repo L2 (mean), and Euclidean/circulant/serial enumerations in different models.

**Decision:** GAP-09 remains **Open** (Check A theorem bodies unresolved; Check D non-exhaustive). Gate G1 remains open.

---

### P1-03 update (21 Oct 2026) — Check A narrowed via the correction; still unresolved at theorem level

P1-03 section 1 records the new Check-A evidence (OpenAlex/Semantic Scholar closed-access confirmations; full Springer correction text with its 10 editorial items; verified `B_i` notation fragment). Check D remains as recorded in P1-02 (documented, non-exhaustive; MathSciNet/Scopus/Web of Science not searched). No exact duplicate of T5/T6 has been found in any inspected text or record, and novelty remains **not approved**.

**Decision:** GAP-09 remains **Open** on Check A theorem bodies. Gate G1 remains open for novelty purposes; mathematical proof work proceeds per P1-03.

---
## GAP-10 — Accessible and publisher versions must not be conflated

**Severity:** High  
**Location:** L1, L4, L8 literature records  
**Status:** Open

### Finding

BP-01 used a mixture of publisher abstracts/pages and accessible arXiv/full texts. For L4 in particular, the accessible theorem-bearing text may differ from the final publisher version. The same caution applies to L8’s arXiv text versus its journal version.

### Required action

For every close neighbour, record separately:

- version inspected;
- date/version identifier where available;
- theorem numbers inspected;
- whether the claim comes from abstract, introduction, theorem statement, proof, or secondary quotation.

A novelty sentence may cite only the version actually inspected, and the final manuscript must use publisher-verified bibliographic data.

### P1-01 update (20 Oct 2026) — version discipline now recorded per source

`P1_01_FULL_TEXT_THEOREM_EXTRACTION.md` records, for every close neighbour: stable URL/DOI, version inspected, and evidence level (A = theorem text, B = abstract/introduction/table, C = correction/secondary). Key facts locked in P1-01:

- Repo L4: arXiv HTML is the theorem-bearing text inspected; the repository-root PDF is `arXiv:2412.08512v1`, not the publisher PDF; publisher theorem numbering unverified.
- Repo L8: arXiv:2305.15237v1 is the theorem-bearing text inspected; publisher version is *FFA* 109 (2026), Art. 102712, DOI `10.1016/j.ffa.2025.102712`; publisher theorem numbering unverified.
- Repo L1/L2: publisher abstract/introduction only (access-restricted full texts); repo L3: abstract/introduction/Table 1 only.

**Decision:** GAP-10 remains **Open** until GAP-16 verifies publisher numbering/models. No novelty sentence may cite a version not actually inspected.

---

### P1-02 update (21 Oct 2026) — version discipline strengthened with hard numbering evidence

P1-02 verified publisher metadata for repo L4 and repo L8 separately from theorem content (P1-02 section 2). New hard fact: repo L8's publisher version is renumbered relative to arXiv v1 (main result "Theorem 18" vs arXiv Theorem 28; "Theorem 4"/"Corollary 7" vs arXiv Theorem 8/Corollary 11), so version conflation is now a demonstrated risk, not a hypothetical one. Repo L4 shows only spot consistency (Theorem 4 / Lemma 7 snippet openings). The repository-root PDF remains arXiv v1 of repo L4, not a publisher PDF.

**Decision:** GAP-10 remains **Open**. No sentence may cite a theorem number from a version that was not actually inspected.

---
## GAP-11 — C7 EAQECC statement is conditional and may not belong in the main results

**Severity:** Medium  
**Location:** `02_THEOREM_BLUEPRINT.md`, C7 / RR-9  
**Status:** Open scope decision

### Finding

The enumerator \(E(u,z)\) records dimensions only. It does not determine minimum distance. Therefore it cannot by itself produce EAQECC parameters.

### Required action

Either:

- omit C7 from the main theorem/corollary chain and mention quantum constructions only as motivation; or
- include a clearly conditional corollary for a named code whose distance is independently proved, with all EAQECC hypotheses stated.

No quantum optimality or new-parameter claim is authorized by BP-01.

---

## GAP-12 — Mean/variance literature must be positioned as supporting, not headline, results

**Severity:** Medium  
**Location:** C5/C6; L2 and average-dimension literature  
**Status:** Open positioning task

### Finding

Average Galois hull dimensions over finite fields and \(R_{m,q}\) are already in the literature. Even after GAP-01 is corrected, the mean should be presented as a consequence of the joint enumerator for the repeated-root affine labeled model, not as the paper’s main novelty.

### Required action

After Gate G1, compare the corrected mean and any variance formula with L2’s exact hypotheses and formulas. If L2 already implies a special case, cite it as such and keep only the genuinely broader joint-distribution consequence.

### P1-01 update (20 Oct 2026) — repo L2 scope fixed at abstract/introduction level

P1-01 verified (record: `P1_01_FULL_TEXT_THEOREM_EXTRACTION.md` §6.3) that Debnath–Prakash, DOI `10.3934/amc.2025010`, publishes average Galois hull dimensions over finite fields and over \(R_{m,q}=\mathbb F_q[u]/\langle u^m-u\rangle\), with the finite-field average organized around \(\Delta_1\) (sum of degrees of self-\(\#\) irreducible factors). Full text is access-restricted, so exact hypotheses/formulas still need theorem-body comparison after Gate G1.

**Decision:** Mean stays a supporting consequence, never a headline. Variance had no counterpart in the inspected texts but remains unproved (GAP-06). GAP-12 remains **Open** for the post-G1 formula comparison.

---

### P1-02 update (21 Oct 2026) — repo L2 bibliographic record completed; positioning unchanged

zbMATH Open (Zbl 1579.94062) confirms repo L2 as *Advances in Mathematics and Communications* 19, No. 6, 1569-1604 (2025), DOI `10.3934/amc.2025010`. No theorem-body comparison was possible (access-restricted), and P1-02's section 4 confirms the corrected C5 candidate is a first-moment consequence only, with variance still unproved.

**Decision:** GAP-12 remains **Open**. The mean stays a supporting consequence of the enumerator, never a headline; exact comparison with repo L2 formulas is still a post-G1 task.

---
## GAP-13 — Prototype documentation and BP-01 audit reproducibility

**Severity:** Low  
**Location:** `code/validate_repeated_root.py`; BP-01 temporary checks  
**Status:** Open cleanup

### Findings

1. The prototype docstring emphasizes \(P=2\), although the script also runs a \(P=4\) case.
2. BP-01’s additional audit script was run from `/tmp` and was not saved as a project artifact.
3. The saved prototype output remains valid for its stated GF(4) cases; BP-01’s rerun matched it exactly.

### Required action

During the next code command, either:

- fold the BP-01 checks into the Prototype-2 script and save the output; or
- save a separate `code/bp01_audit.py` and `code/bp01_audit_output.txt` if the Commander wants BP-01 evidence preserved as an artifact.

BP-01 did not edit code.

---

## GAP-14 — Incompatible twists remain a hard scope boundary

**Severity:** Medium  
**Location:** T3–T6 hypotheses  
**Status:** Boundary confirmed; no action inside this paper unless separately commanded

### Finding

If

\[
\lambda_s^{1+p^{d_s-k}}\ne1,
\]

then the code-first dual belongs to the transformed modulus

\[
x^n-\lambda_s^{-p^{d_s-k}},
\]

so the same factor set, the \(\tau\)-orbit decomposition, and T6 are not asserted.

### Required action

Keep incompatible twists only in Limitations/Future Work. Any experiment with them is diagnostic and must not be described as validating or extending T6.

---

## GAP-15 — Recommended next command

**Severity:** Gate decision  
**Status:** BP-01 recommendation

### Recommendation

Issue exactly one next command:

> **P1-01 — Full-text theorem extraction and overlap audit for L1/L4, with L3 extraction and L8 publisher-version closure.**

That command should produce theorem-extraction notes and an overlap table for:

1. L1 finite-field Galois hulls and hull-dimension counts;
2. L4 affine-algebra Galois hulls, including arXiv/publisher comparison;
3. L3 small Galois hull dimensions;
4. L8 multi-twisted GPM specialization to repeated-root constacyclic codes.

### Reason

BP-01 showed that the mathematical core is coherent apart from C5/C6, but the largest immediate risk is no longer RR-3. The largest risk is that the individual hull formula and hull-only counting overlap prior work more closely than Audit v1 suggested. Gate G1 should therefore be attacked before proof drafting or manuscript drafting.

### P1-01 outcome (20 Oct 2026) — this recommendation was executed; superseded by GAP-16

P1-01 was executed and delivered `P1_01_FULL_TEXT_THEOREM_EXTRACTION.md` with per-contribution verdicts and an overall **CONDITIONAL GO**. Gate G1 remains open for the reasons listed in GAP-16. The single next command is now GAP-16, not a repeat of P1-01.

---

## GAP-16 — P1-01 outcome: Gate G1 closure requires repo L1 full text, publisher verification, and Check D

**Severity:** Gate decision  
**Status:** Executed as P1-03 on 21 October 2026 — CONDITIONAL GO; Gate G1 remains open (novelty only); superseded by the single P1-04 recommendation in `P1_03_MATHEMATICAL_PROOF_PLAN.md` section 8

### What P1-01 settled

- Repo L4 (arXiv-level): exponent-level repeated-root hull formula overlaps T4 strongly, but no joint enumerator/transfer trace/code-count/moments were found; counting over \(\mathcal A\) is explicitly left open there.
- Repo L8 (arXiv-level): GPM hull machinery overlaps T3/T4 strongly for index-1 constacyclic codes, but no labeled joint enumerator/transfer trace/moments were found.
- Repo L3: existence only for hull dimensions 1–2 (table level). Repo L2: mean already published over fields and \(R_{m,q}\). Repo L9/L10: Euclidean structure/LCD-type enumerations at abstract level.
- GAP-01/C5 was independently re-derived and computed: frozen hull-mean is false for \(L_O=1\); split correction confirmed as candidate, **not applied**.

### What still blocks Gate G1

1. Repo L1’s exact counting theorem (theorem numbers, hypotheses, exponent range, hull-only vs joint) is **unresolved** — no lawful full text obtained.
2. L4/L8 publisher theorem numbering and the L4 component-model equivalence with the frozen \(K_s\) model are unverified.
3. Repo L3 theorem bodies and repo L2 exact mean formulas were not inspected.
4. Check D database searches (MathSciNet/zbMATH/Scopus-style) were not performed.

### The single recommended next command

> **P1-02 — Lawful full-text closure for repo L1 and publisher-version comparison (L1/L4/L8), with a Check-D database-search record.**

Until P1-02 (or an equivalent Boss-approved closure) is done: no manuscript drafting, no “first/new enumeration/priority” wording, no edit to frozen C5, and no novelty claim for T5/T6 beyond “no counterpart found in the text inspected so far”.

### P1-02 outcome (21 Oct 2026) — CONDITIONAL GO; Gate G1 still open

P1-02 delivered `P1_02_LITERATURE_CLOSURE.md` with separate statuses (a)-(f). Summary: (a) repo L1 finite-field counting **unresolved / potentially critical** — lawful full text not obtained, exact questions L1-Q1...L1-Q8 recorded, search stopped as commanded; (b) repo L4 **partial overlap (strong)** at arXiv level, publisher metadata verified (DM 349(2), Art. 114750, 18 p., Zbl 1582.94185), publisher theorem equivalence unresolved; (c) repo L8 publisher metadata verified (FFA 109, Art. 102712, 25 p., Zbl 1576.94064) but numbering demonstrably differs from arXiv (Theorem 18 vs 28), so full equivalence is unresolved; (d) T5/T6: no counterpart found in inspected texts or Check-D records — **novelty not approved**; (e) Check D documented but non-exhaustive (MathSciNet/Scopus/Web of Science not searched); (f) C5: `E[min(P-A,A)] = floor(P^2/4)/(P+1)` recorded exactly, first moments resolved for all orbit lengths, correction still **not approved and not applied**, variance unproved.

**The single recommended next command is now P1-03** (Boss-enabled repo L1 full-text closure and Gate-G1 re-vote), as stated in `P1_02_LITERATURE_CLOSURE.md` section 7. Until then: no manuscript drafting, no "first/new enumeration/priority" wording, no edit to frozen C5, and no novelty claim for T5/T6 beyond "no counterpart found in the text/records inspected so far".

### P1-03 outcome (21 Oct 2026) — CONDITIONAL GO; proof plan delivered; Gate G1 open for novelty only

P1-03 delivered `P1_03_MATHEMATICAL_PROOF_PLAN.md` and `code/validate_p1_03.py` (+ output). Summary: (i) repo L1 correction verified as 10 editorial items from the lawful Springer page; OpenAlex/Semantic Scholar confirm closed access; L1-Q1-Q6/Q8 unresolved and recorded — mathematical work proceeds with **no novelty claim**. (ii) Independent proof plan for T1-T6 under convention lock A1-A10; T5 proved at plan level by closed-walk expansion; T3's RR-3 route fixed (coefficient identity + dimension count, no separability); the blueprint's missing dual-order sentence identified (PC-2 / GAP-17). (iii) `nu_P = floor(P^2/4)/(P+1)` formally derived for `L=1`; `mu_P` per edge for `L>=2`; candidate split registered as PC-1, **not applied**; frozen C5 hull mean confirmed incorrect exactly on `L=1` orbits by vector-level counterexamples; C5 code-dimension mean re-derived correct. (iv) Review verdicts: T1, T2 (with PC-3), T4, T5, T6 proof-ready/route-complete; C1-C4 correct (C4 completed by PC-4); C6 unproved (exact obligations recorded); C7 conditional only. (v) Extended validation executed: 6 vector cases (2,806 assignments, incl. `GF(8)` orbit length 6, `lambda=-1` twists, `sigma != rho`) and 31 `(P,L)` orbit pairs — all passed; old prototype rerun identical.

**The single recommended next command is now P1-04** (formal proof package for T1-T4), as stated in `P1_03_MATHEMATICAL_PROOF_PLAN.md` section 8. Until further commands: no manuscript drafting, no novelty/priority wording, no edit to frozen C5 or any frozen statement, and PC-1...PC-6 remain unapproved proposals.

---

## GAP-17 — Dual-order convention (rho vs sigma) is not frozen in the blueprint; proposed corrections register

**Severity:** Proof blocker (convention)  
**Status:** Open; identified in P1-03

### Issue

The frozen blueprint defines the pairing `⟨x,y⟩ = Σ_i x_i σ(y_i)` but never writes the dual set with its argument order. If `D(C) = {y : ⟨c, y⟩ = 0 ∀ c ∈ C}` (code first), then `D(C) = ρ(C^⊥)` and the dual generator is `h_a#` as frozen. If the opposite order were read, `σ` and `ρ` would interchange and `h_a#` would be wrong. The old `GF(4), k=1` prototype cannot distinguish the two readings (`σ = ρ` there); the new `GF(8), k=1` validation (`σ = a²`, `ρ = a⁴`) supports the code-first reading computationally, but the freeze itself is ambiguous on paper.

### Proposed corrections register (all unapproved; frozen file untouched)

- **PC-1** (C5): replace the hull-mean display/proof key by the split formula `mu_P * Σ_{L>=2} w_O L_O + nu_P * Σ_{L=1} w_O`. Verified; awaiting approval.
- **PC-2** (T3 freeze): add the sentence `D(C) = {y : ⟨c, y⟩_{s,k} = 0 for all c ∈ C}` to the convention freeze.
- **PC-3** (T2): add the hypothesis `f(0) ≠ 0` to the definition range of `#`.
- **PC-4** (C4): add the dual-containing count `∏_O tr((B'_P)^{L_O})`, `(B'_P)_{a,b} = 1` iff `a + b ≤ P`. Verified computationally.
- **PC-5** (T1): state explicitly that codes are `A`-submodules (component `K_s`-linear codes) with fixed component/factor labels.
- **PC-6** (C6): mark the variance corollary "to be proved (RR-8)" wherever it is summarized.

### Resolution required

A single future approval command should decide PC-1...PC-6 together, with any blueprint edit made as a dated correction note, never silently. Until then the proof package (P1-04) must state the A2 order verbatim in its own text.


---

### P1-04 outcome (21 Oct 2026) — CONDITIONAL GO; T1–T4 proved (single component)

`P1_04_PROOFS_T1_T4.md` delivers complete, self-contained proofs of RR-1 (divisor/exponent/dimension correspondence), RR-2 (coefficientwise-`ρ` automorphism; `#` multiplicative; root transport via the Frobenius automorphism of the algebraic closure; `τ` a degree-preserving permutation of `F`; the two compatibility forms equivalent), RR-3 (Euclidean dual `C^⊥ = ⟨h^♮⟩` from `gh = x^n − λ` alone — coefficient-of-`x^{n-1}` identity plus dimension count; **no** separability, `gcd(n,p)=1`, `P`-structure, or compatibility used; conditions on `g, h, n, λ` listed exhaustively), RR-4 in the command's naming (= blueprint RR-4 twist transport `D(C) = ρ(C^⊥)` + blueprint RR-5 PID/quotient lcm lemma, with its same-modulus applicability condition stated), and hence T1, T2, T3 (generator `⟨h_a#⟩`, exponents `β_i = P − α_{i−1}`, twist `λ^{−p^{d−k}}`, equal to `λ` under compatibility), T4 (hull generator `lcm(g_a, h_a#)` and the `min(P − α_i, α_{i−1})` dimension identity). The code-first dual-order sentence (S7) is stated verbatim in the proof file; `D(C)`, `C^⊥`, and the candidate-first reading are distinguished, and the exact step using the order is flagged in Proposition 4.2.

**Counterexamples:** none — no lemma fails under the locked hypotheses A1–A10. Three necessity witnesses are recorded instead (not counterexamples): `#` undefined when the constant term vanishes (PC-3 hypothesis is necessary; such factors never divide `S` here); compatibility is necessary for the same-modulus T4 step (order-8 `λ ∈ GF(9)`, `k = 1` example, where `λ^{1+3} = λ^4 = −1 ≠ 1`); reversing the dual order swaps `ρ`/`σ` (PC-2). T3 is proved in a stronger two-modulus form, so only T4's lcm step consumes compatibility.

**Verification (executed, supporting only):** `code/validate_p1_03.py` rerun — exit 0, output byte-identical to the saved file, all checks passed; plus 619 assignments in which `⟨h^♮⟩ = C^⊥` was verified directly (inclusion by orthogonality, equality by dimension). No frozen file edited; PC-1…PC-6 still unapproved; Gate G1 untouched (open for novelty only).

**The single recommended next command is now P1-05** (formal proof package for T5–T6 and corollaries C1–C4: transfer trace, global joint enumerator, `P = 1` recovery, multi-component assembly).


---

### P1-05 outcome (21 Oct 2026) — CONDITIONAL GO; T5–T6, C1–C4 proved; RR-6/RR-7 discharged

`P1_05_PROOFS_T5_T6_COROLLARIES.md` (+ PDF) gives self-contained proofs of: **T5** (trace = closed walks over labeled orbit positions; walk/assignment bijection; edge weight `u^{w(P-b)} z^{w·min(P-b, a)}` matched term-by-term to T4's current/predecessor orientation, including the `L = 1` self-loop); **T6** via a separately proved CRT/product assembly (Proposition 3.1: ideals of a product ring are products of ideals; `D_A = ∏ D_s`; `F_q`-dimensions add with weights `m_s`; no cross-component coprimality is needed — the only coprimality is `gcd(n_0, p) = 1` inside each component; common `P, n, k`, per-component compatibility, common length, fixed labels, `A`-submodule codes all stated) and the finite distributive law; **C1** (`J^L` trace), **C2** (rank-one trace at `z = 1`, regrouped factorwise), **C3** (termwise-vanishing + cycle argument giving exactly the all-`0`/all-`P` tuples; rigorous replacement of the frozen sketch's imprecise wording — statement unchanged), **C4** (both characterizations via the nonnegative edge identities `(P−α_i) − min(P−α_i, α_{i−1}) = max(0, P−α_i−α_{i−1})` and `α_{i−1} − min(P−α_i, α_{i−1}) = max(0, α_i+α_{i−1}−P)`, `dim D(C)` computed from T3's `β_i`; self-orthogonal count as frozen). The dual-containing **count** `∏_O tr((B'_P)^{L_O})` is proved only as labeled proposal **PC-4** (still unapproved). **P = 1 recovery** is proved algebraically: `T^{(1)}_w = [[u^w, 1], [u^w z^w, 1]]`, hull edge = indicator of the `1→0` transition, C1–C4 specialized; C5's frozen "`P = 1` gives `1/4`" remark is explicitly excluded from the recovery (false for `L_O = 1`, GAP-01/PC-1). Convention recheck (command item 3): P1-04's RR-2 (`#` = coefficientwise-`ρ` reciprocal, multiplicative), RR-3 (ordinary reciprocal `h^♮`, no separability), RR-4 (`D(C) = ρ(C^⊥)` from the second-slot code-first order; opposite order would give `β_i = P − α_{i+1}`) are tabulated at every point of use in §1 of the proof file. RR-6 and RR-7 are **discharged**.

**Counterexamples/obstructions:** none for T5/T6/C1–C4 under (G1)–(G6). Remaining open items unchanged: C5 hull mean (PC-1 unapproved), C6 variance (RR-8), C7 (RR-9), PC-1…PC-6 approvals, Gate G1 (novelty).

**Verification (executed, supporting only):** `code/validate_p1_03.py` rerun — exit 0, output byte-identical to the saved file. New `code/validate_p1_05.py` (+ `code/validation_p1_05_output.txt`): first multi-component check, `A = GF(2) × GF(4)` (`k = 0`, `λ = (1,1)`, `P = 2`, `n = 14`), 729 labeled global assignments — additive `F_q` dimensions from per-component Gram-rank brute force equal the convolution, the T6 orbit-trace product (weights `(1,1), (2,3), (1,2), (2,6)`), and the C1–C4 global counts (C3: `16 = 2^4`; C4: `144 = 144`). It cannot prove the CRT correspondence or the general formulas; it tests one example with `k = 0, λ = 1, P = 2, N = 2`.

**The single recommended next command is now P1-06** (moments package: formal proof of the C5 mean split as mathematics — blueprint change still subject to PC-1 approval — and the C6 variance closed forms, RR-8).


---

### P1-06 outcome (21 Oct 2026) — CONDITIONAL GO; C5 mean split and C6 variance proved (mathematics); PC-1/PC-6 adoption still pending

`P1_06_MOMENT_PROOFS_C5_C6.md` (+ PDF) transcribes frozen C5/C6 first, then proves: **C5 code-dimension mean** `(n/2)·Σ_s m_s` (frozen, correct, re-derived). **Hull mean (Theorem 2.4):** `E[Hull] = ν_P·Σ_{L_O=1} w_O + μ_P·Σ_{L_O≥2} w_O L_O` with `ν_P = ⌊P²/4⌋/(P+1)` (self-loop `min(P−A,A)`, parity derivation) and `μ_P = P(2P+1)/(6(P+1))` (two-independent-uniform edge, tail-sum derivation) — independently re-derived, not assumed. This is exactly proposal **PC-1**; the frozen C5 hull display and its "`P=1` gives `1/4`" remark are incorrect whenever an `L_O = 1` orbit exists (smallest counterexample family: any `L=1` orbit; `P=2`: `ν_2 = 1/3 ≠ 5/9 = μ_2`). **C6 variance (RR-8 discharged mathematically):** with `X_i = min(P−A_i, A_{i−1})`, `S_L = Σ X_i`: edge `E[min²] = P(P²+P+1)/(6(P+1))`, `Var_edge = P(P+2)(2P²+4P+3)/(36(P+1)²)`; adjacent covariance (exactly one shared variable, via conditioning and `F(c) = c(2P−c+1)/(2(P+1))`) `κ_P = −P(P+2)(7P²+14P+9)/(360(P+1)²) < 0`; non-adjacent edge pairs (`L ≥ 4`) independent (disjoint variable sets); `L=2` cross moment by a tail double-sum, `Cov = −P²(P+2)²/(36(P+1)²)`. Hence `Var(S_1)` = parity-split closed forms, `Var(S_2) = P(P+2)(P²+2P+3)/(18(P+1)²)`, `Var(S_L) = L·P(P+2)(P²+2P+2)/(60(P+1)²)` for `L ≥ 3`, and globally `Var(dim Hull) = Σ_{s,O} w_O²·Var(S_{L_O})` (variance adds with squared weights by component/orbit independence of the product-uniform model). Nothing remains as an unsimplified finite sum for the hull variance; `dim C` variance and `Cov(dim C, dim Hull)` were not part of C6 and are not claimed.

**Verification (executed, supporting only):** new `code/validate_p1_06.py` (+ output) — exact rational arithmetic, three layers (closed forms vs building-block finite sums vs direct enumeration) for `P ∈ {1,2,3,4,5,8,9}`, `L ∈ {1,2,3,4,6}` (two largest `(P,L)` pairs covered by finite sums only), plus global weighted assembly vs direct enumeration (`P=2`, 729 tuples) and exact convolution (`P=3`): `ALL P1-06 MOMENT CHECKS PASSED`. `validate_p1_03.py` rerun byte-identical; `validate_p1_05.py` rerun passed. Earlier artifacts unmodified.

**Status changes requested (not applied):** GAP-01/PC-1 mathematics now fully proved (blueprint adoption pending approval); RR-8 (GAP entry for C6) mathematics discharged — blueprint adoption likewise pending. PC-1…PC-6 remain unapproved; frozen blueprint untouched; Gate G1 open.

**The single recommended next command is now P1-07** (single approval-and-integration command: decide PC-1…PC-6 together, apply approved corrections to the blueprint as dated correction notes, and close Gates G1/G3 bookkeeping for the proved core T1–T6/C1–C6 — or record explicit rejection).


---

### P1-07 outcome (21 Oct 2026) — decision dossier delivered; ALL PC STATUSES STILL PENDING

`P1_07_PC_DECISION_DOSSIER.md` (+ PDF) documents each proposal with exact frozen text, exact old→new change, reason, proof/evidence locations, classification, accept/reject/defer consequences, and a **recommendation only**: PC-1 APPROVE (theorem correctness; frozen C5 hull mean false, split proved in P1-06 Theorem 2.4, `P=1` case verified: `ν_1 = 0`, `μ_1 = 1/4`); PC-2 APPROVE (add `D(C) = {y : ⟨c, y⟩_{s,k} = 0 ∀ c ∈ C}`; trace through RR-2/RR-3/RR-4 with `ρ/σ/h^♮/h_a#` roles; opposite order would change the generator); PC-3 APPROVE (add `f(0) ≠ 0`; else `#` undefined, witness `f(x) = x`); PC-4 APPROVE (add dual-containing count `∏ tr((B'_P)^{L_O})`; proved in P1-05 §5 and computationally verified; pure completion); PC-5 APPROVE (state `A`-submodule/fixed-label scope in T1; product parametrization fails for arbitrary mixing `F_q`-subspaces); PC-6 **REJECT as superseded** (the "to be proved (RR-8)" label was correct when proposed, but RR-8 is now proved in P1-06 Theorem 3.7, so the label would be false; the right follow-up is integrating the C6 closed forms, a different edit proposed inside the dossier). **No PC was approved, rejected, or integrated by P1-07.** Integration must be a separate future command applying accepted items as dated correction notes (GAP-17 rule). Checks rerun unmodified: `validate_p1_03.py` (byte-identical), `validate_p1_05.py`, `validate_p1_06.py` — all passed. Frozen blueprint untouched; Gate G1 open and unrelated to the PCs.

**The single recommended next command is now P1-08** (Boss/Commander decision-and-integration: record APPROVE/REJECT/DEFER for PC-1…PC-6, apply accepted changes as dated correction notes in one blueprint edit, and record the new frozen state).


---

### P1-08 outcome (21 Oct 2026) — integration applied; blueprint re-frozen with corrections (commit recorded below by hash in `P1_08_INTEGRATION_AUDIT.md`)

Commander decisions applied exactly as given: **PC-1 APPROVED, PC-2 APPROVED, PC-3 APPROVED, PC-4 APPROVED, PC-5 APPROVED, PC-6 REJECTED (obsolete "to be proved" label; C6 proved status/formulas recorded instead)**. One controlled edit of `02_THEOREM_BLUEPRINT.md` (dated Correction Notes section at the top + `[P1-08 …]` notes at each location): C5 hull mean corrected to `μ_P·Σ_{L_O≥2} w_O L_O + ν_P·Σ_{L_O=1} w_O` with the `P=1` case (`ν_1 = 0`; `1/4` only on the `L_O≥2` part), code-dimension mean preserved; dual-order sentence `D(C) = {y : ⟨c,y⟩_{s,k} = 0 ∀c∈C}` added with `D(C) = ρ(C^⊥)`, `h^♮` (ordinary reciprocal) and `h_a# = ρ̄(h_a^♮)` reconciled (P1-04 RR-3/Prop. 4.2); `#` domain `f(0) ≠ 0` stated in §0 and T2; dual-containing count `∏_O tr((B′_P)^{L_O})` added to C4 with its compatible/labeled hypotheses; T1 global scope (`A`-submodule, fixed labeled CRT) stated; C6 now carries the proved variance formulas of P1-06 Theorem 3.7 (mean weights `w_O`, variance weights `w_O²` distinguished) with **no** "to be proved" label. **GAP-01: CLOSED** (correction approved and applied). **GAP-06/RR-8: CLOSED** (proved in P1-06; formulas integrated). **GAP-17: CLOSED** (PC-2/PC-3/PC-5 applied; PC-4 applied; PC-1 applied under GAP-01; PC-6 rejected as superseded). Blueprint SHA-256 before: `013ef5a20742b3de735d49edb6f2fdde074b0d134adea9c85d30d24cab739ce3`; after: `ec2fd8d58f8d2a986314f83997d750d689f7c88e98ec8f87753ab4c9cf438cff`. Validation rerun unmodified: `validate_p1_03.py` byte-identical, `validate_p1_05.py`, `validate_p1_06.py`, `validate_repeated_root.py` — all passed. Remaining open: **Gate G1 (novelty)**; C7/RR-9 conditional scope only; no manuscript drafting yet.

**The single recommended next command is now P1-09** (Gate-G1-focused closure attempt: final literature/novelty decision package — repo L1 status, safe novelty sentence, and Gate-G1 vote — since the mathematical core is now frozen and proved).


---

### P1-09 outcome (21 Oct 2026) — Gate G1: DEFER (cannot close); NO-GO for novelty claims; overall CONDITIONAL GO

`P1_09_GATE_G1_NOVELTY_AUDIT.md` + `P1_09_OVERLAP_MATRIX.md` (+ PDFs) deliver the Gate-G1 assessment. Freeze verified first (blueprint SHA-256 `ec2fd8d5…cf438cff`, identical to the P1-08 after-hash; commit `33a8c28`; no blueprint/proof/validation artifact modified — the local-checkout reset was again repaired from the remote with a backup + `diff -r` identity check, no history rewrite). **Repo L1 remains UNRESOLVED:** fresh lawful attempts on 21 Oct 2026 (OpenAlex: `is_oa=false`, `any_repository_has_fulltext=false`; Semantic Scholar: `isOpenAccess=false`, empty `openAccessPdf`; Springer: abstract only; title+preprint web search: no author/institutional copy) found no lawful theorem-bearing full text; the comparisons L1-Q1…Q6 (in particular `p | n` scope, joint-vs-marginal count, `B_i` vs `τ`-orbits) therefore cannot be made, and no theorem was inferred from the abstract. **Overlap headlines:** L4 (arXiv full text) substantially pre-occupies K1 (Thms. 5/7/8, Cor. 3.5, arXiv numbering; extra `ord λ` hypotheses; attainable-dimension-value counts; code enumeration over `A` left open); L8 (arXiv full text) is strong hull machinery in the GPM family (Thms. 8–11, 25–29); L2 owns mean-as-headline in its model; L3 covers hull dims 1–2 incl. `p | n`. No inspected source contains K2+K3 (joint labeled affine repeated-root enumerator by per-orbit transfer traces) or K6 (variance in `P`); MathSciNet/Scopus/WoS remain unsearched, so coverage is non-exhaustive. The safest defensible statement (internal use), a six-item must-not-claim list (no "first" hull formula/count/mean/small-dim claims, no priority over L1, no unqualified "novel"), the single missing item (lawful L1 full text — an author/institutional copy is realistic since L1's third author is this project's advisor — followed by extraction answering L1-Q1…Q6), and a journal-risk assessment (medium with conservative wording today, high with any "first" wording, low–medium after L1 is read) are all recorded in the audit. **Gate G1 stays OPEN (deferred, not closed); manuscript drafting remains gated.** Validations rerun unmodified as sanity (p1_03 byte-identical; p1_05, p1_06 passed).

**The single recommended next command is now P1-10** (lawful L1 full-text acquisition via the author/institutional channel and theorem-level extraction answering L1-Q1…Q6; Gate G1 re-vote immediately after).
