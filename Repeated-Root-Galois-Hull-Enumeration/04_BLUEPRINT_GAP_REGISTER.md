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
**Status:** Executed as P1-02 on 21 October 2026 — CONDITIONAL GO; Gate G1 remains open; superseded by the single P1-03 recommendation in `P1_02_LITERATURE_CLOSURE.md` section 7

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
