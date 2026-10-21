# P1-02 — Literature Closure and Novelty Gate G1

**Command:** P1-02 — Literature Closure and Novelty Gate G1  
**Date:** 21 October 2026  
**Decision:** **CONDITIONAL GO**  
**Gate G1 status:** **Still open.** No manuscript drafting and no novelty/priority claim is authorized by this file.

This file closes as much of Gate G1 as could be closed with lawfully accessible evidence on 21 October 2026. It preserves `P1_01_FULL_TEXT_THEOREM_EXTRACTION.md` unchanged and does **not** edit the frozen statements in `02_THEOREM_BLUEPRINT.md`.

---

## 0. Label map — read this first

The command labels and repository labels are shifted. This file uses **repository labels** and prints the command label beside them.

| Command label in P1-02 | Repository label used here | Source |
|---|---|---|
| Command “L1” | **Repo L4** | Debnath–Islam–Martínez-Moro–Prakash, affine algebra rings, arXiv:2412.08512, DOI `10.1016/j.disc.2025.114750` |
| Command “L4” | **Repo L8** | Eldin–Solé, multi-twisted Galois hulls, arXiv:2305.15237, DOI `10.1016/j.ffa.2025.102712` |
| Command “L3” | **Repo L1** | Debnath–Prakash–Islam, finite fields, DOI `10.1007/s12095-022-00591-6` |

No source was silently renumbered.

Evidence discipline used throughout:

- **Metadata verification** (title, authors, venue, DOI, dates, pages/article number) is not theorem verification.
- **Publisher-snippet verification** (abstract/introduction/section snippets) is not full-text theorem verification.
- **Inaccessible full text is not evidence of absence.**
- “No counterpart found” means only: no counterpart was found in the text/records actually inspected.

---

## 1. Task 1 — Repo L1 lawful full-text closure attempt

**Source.** Indibar Debnath, Om Prakash, Habibul Islam, “Galois hulls of constacyclic codes over finite fields,” *Cryptography and Communications* 15(1), 111–127 (2023). DOI: `10.1007/s12095-022-00591-6`. Published by Springer 23 June 2022; received 23 October 2021; accepted 16 May 2022. Correction: DOI `10.1007/s12095-022-00602-6`, *Cryptogr. Commun.* 15, 129–130 (2023).

### 1.1 Lawful-access routes actually searched on 21 October 2026

Searches were run for an openly available author manuscript, institutional-repository copy, or other lawful theorem-bearing full text. Exact query strings included:

1. `"Galois hulls of constacyclic codes over finite fields" Debnath Prakash Islam PDF`
2. `"Galois hulls of constacyclic codes over finite fields" author manuscript repository`
3. `10.1007/s12095-022-00591-6 filetype:pdf manuscript preprint`
4. `site:researchgate.net/publication "Galois hulls of constacyclic codes over finite fields"`
5. `"Galois hulls of constacyclic codes over finite fields" "IIT Patna" repository OR dspace OR "institutional repository"`
6. `"Galois hulls of constacyclic codes over finite fields" arxiv OR arXiv OR "preprint"`

Records verified:

- Springer article page: bibliographic metadata and abstract only; no open full text.
  `https://link.springer.com/article/10.1007/s12095-022-00591-6`
- ACM record for the same DOI: volume 15, issue 1, pages 111–127; IIT Patna affiliations; “© The Author(s), under exclusive licence to Springer 2022.”
  `https://dl.acm.org/doi/10.1007/s12095-022-00591-6`
- zbMATH Open record Zbl 1518.94136: *Cryptogr. Commun.* 15, No. 1, 111–127 (2023), correction ibid. 15, No. 1, 129–130 (2023); MSC 94B15, 11T71; keywords: constacyclic codes, Galois inner product, Galois hulls, cyclotomic polynomials, LCD codes. Its “Full Text” link is **DOI only** — no open version is indexed for repo L1.
  `https://zbmath.org/1518.94136`
- zbMATH correction record Zbl 1518.94137 exists for DOI `10.1007/s12095-022-00602-6`.
- A zbMATH title search `ti:"Galois hulls" & any:constacyclic` returned 5 documents (repo L4, repo L8, repo L2, repo L1 correction, repo L1) and reported only **2 open versions** in that set — the two arXiv-backed records (repo L4 and repo L8), not repo L1.

Dead ends, explicitly **not** used as evidence:

- A web-search snippet on a ResearchGate aggregator page claimed “Full-text available” next to the repo L1 title. Fetching the aggregator page resolved to a different paper (Chen–Fan–Lin–Liu, “Constacyclic Codes over Finite Fields,” *Finite Fields Appl.* 18(6), 2013, DOI `10.1016/j.ffa.2012.10.001`), and an earlier guessed ResearchGate publication ID resolved to an unrelated medical paper. The snippet was therefore **not** verified as a lawful author manuscript and no ResearchGate file was downloaded or relied on.
- An Academia.edu copy of the **correction** was snippet-visible in search results. Its licence/version status as an author manuscript was not verified, so it was not treated as lawful theorem-bearing full text. The one correction line visible in secondary snippets — page-line replacement of `1 ≤ i1 ≤ i2 ≤ ai` by `1 ≤ i1 < i2 ≤ ai` in the proof that `f_{i1}^# ≠ f_{i2}^#` — is recorded here only as an unverified-at-theorem-level lead, not as theorem evidence.
- No institutional-repository (IIT Patna / IIIT Bhopal) copy and no arXiv/preprint version of repo L1 was found. No interlibrary-loan transaction could be executed from this workspace; ILL remains a Boss/library action (see §7).

**Stopping rule applied.** As commanded, the lawful-access search was stopped once the above routes were exhausted. No hypothesis or theorem of repo L1 was inferred from its abstract.

### 1.2 What is verified for repo L1 (Level B only)

From the publisher abstract and the zbMATH summary (which reproduces the abstract), the following **scope** statements are verified:

- The paper presents a formula for the dimension of Galois hulls of constacyclic codes over `F_q`, arranging the irreducible factors of `x^n − λ` “in a suitable way.”
- “Also, considering some restrictions on `q`, the number of constacyclic codes of length `n` over `F_q` is calculated for a given Galois hull dimension.”
- A published correction exists (2 pages, 129–130).

Nothing stronger is verified. In particular, the abstract does **not** state the restrictions on `q`, the hypotheses on `n` or `λ`, or whether the count is joint with code dimension.

### 1.3 Exact unresolved theorem-level questions for repo L1

Until a lawful full text is supplied, the following remain **unresolved** and block any exact overlap verdict:

- **L1-Q1 (theorem identity).** What are the exact theorem numbers and statements of (i) the hull-dimension formula and (ii) the counting result(s)?
- **L1-Q2 (length hypothesis).** Is `n` arbitrary, coprime to `p`, or of repeated-root form `n = n′ p^{e′}` with `gcd(n′,p)=1`? Is the characteristic-`p` part of `n` genuinely included?
- **L1-Q3 (twist hypothesis).** What conditions are imposed on `λ` (e.g. on `ord(λ)`, on `gcd(ord λ, n′)`, or on `ord(λ) | 1 + p^{e−ℓ}`)?
- **L1-Q4 (the “restrictions on q”).** Exactly which restrictions on `q = p^e` and the Galois index `ℓ` are assumed in the counting theorem?
- **L1-Q5 (counting object).** What is counted: labeled generator-polynomial constacyclic codes of length `n` over `F_q`? All constacyclic codes? Codes by hull dimension only, or jointly by `(dim C, dim hull)`?
- **L1-Q6 (exponent model).** How are the irreducible factors of `x^n − λ` arranged when `p | n` (multiplicity `p^{e′}`), what exponent range is used (`0 ≤ a ≤ p^{e′}`?), and does the formula specialize to the project’s T4 form `w_O Σ_i min(P − α_i, α_{i−1})` at `P = p^{e′}`?
- **L1-Q7 (correction effect).** Which statements or proofs does the correction (DOI `10.1007/s12095-022-00602-6`) change, beyond the snippet-visible inequality correction, and does it alter any hypothesis or count?
- **L1-Q8 (project specialization).** Does repo L1’s finite-field case already contain the `N=1, m_1=1` specialization of the project’s joint enumerator marginals (hull-only count, LCD count, mean)?

**Status (a) — prior finite-field hull-dimension counting:** **UNRESOLVED / PARTIAL OVERLAP (potentially critical).** Repo L1 certainly publishes a finite-field hull-dimension formula and a hull-dimension counting result under unstated-in-abstract restrictions on `q`. Whether it duplicates the hull-only marginal of the project’s enumerator in the repeated-root case cannot be decided without the theorem text. It is **not** evidence of absence, and it is also **not** yet a verified duplicate of T6: no joint `(dim C, dim hull)` enumerator was verified in any inspected record.

---

## 2. Task 2 — Publisher-version verification for repo L4 and repo L8

### 2.1 Repo L4 (command “L1”) — affine algebra rings

**Publisher record verified (metadata level).**

- *Discrete Mathematics* 349, Issue 2, February 2026, Article 114750. DOI `10.1016/j.disc.2025.114750`. PII `S0012365X25003589`.
- Authors (publisher order): Indibar Debnath, Habibul Islam, Edgar Martínez-Moro, Om Prakash.
- zbMATH Open Zbl 1582.94185: *Discrete Math.* 349, No. 2, Article ID 114750, **18 p.** (2026); MSC 94B15, 11T71; Full Text links: DOI and arXiv.
  `https://zbmath.org/1582.94185`
- Publisher page: `https://www.sciencedirect.com/science/article/abs/pii/S0012365X25003589`
- arXiv version: `https://arxiv.org/html/2412.08512` (v1, 11 Dec 2024). The PDF stored in the repository root is this arXiv v1, **not** the publisher PDF (verified in P1-01).

**Publisher-snippet comparison (not full-text verification).**

- The publisher abstract matches the arXiv abstract in scope: square-free affine algebra `A = F_q[X_1,…,X_ℓ]/I`; `k`-Galois dual and hull generators; hull-dimension formula; LCD condition; EAQECC examples.
- The publisher introduction matches the arXiv introduction’s literature positioning, including the sentence that Debnath et al. (2023) “presented a formula to calculate the Galois hull dimensions of constacyclic codes over finite fields. They also counted the number of constacyclic codes of a given Galois hull dimension.”
- A publisher section snippet headed “Theorem 4” begins “Let λ be a unit in A. If C = Σ_{S(ν)} C_{S(ν)} e_{S(ν)} …”, matching the opening of **arXiv Theorem 4** (dual twist type). A publisher “Lemma 7” EAQECC snippet likewise matches the arXiv Lemma 7 citation pattern. These are **spot consistencies only**.
- No publisher snippet inspected in P1-02 exposed the publisher numbering or exact hypotheses of arXiv Theorem 8 (repeated-root hull dimension) or Corollary 3.5 (cardinality of attainable dimension values). No change in assumptions or results was observed in the inspected snippets, but absence of an observed change is **not** proof that the publisher text is identical to arXiv v1.

**Status (b) — affine-algebra repeated-root overlap:** **PARTIAL OVERLAP (STRONG), verified at arXiv theorem level; publisher metadata verified; publisher theorem-level equivalence UNRESOLVED.** As established in P1-01, arXiv Theorem 8 already gives an individual-code repeated-root exponent hull-dimension formula under extra hypotheses (`gcd(ord λ, n′)=1`, `ord(λ) | 1+p^{e−k}`), and the arXiv conclusion explicitly leaves enumeration of (non-isometric) codes by Galois hull dimension over `A` open. No joint `(dim C, dim hull)` enumerator, transfer trace, code-count by hull dimension, or moment formula was found in the inspected text. The affine component presentation (§2.1 field components vs §2.3 `F_q`-projection codes) still must be reconciled with the project’s labeled `K_s`-component model before any exact domain-equivalence sentence is used.

### 2.2 Repo L8 (command “L4”) — multi-twisted codes

**Publisher record verified (metadata level).**

- *Finite Fields and Their Applications* 109, January 2026, Article 102712. DOI `10.1016/j.ffa.2025.102712`. PII `S107157972500142X`.
- Authors: Ramy Taki Eldin, Patrick Solé.
- zbMATH Open Zbl 1576.94064: *Finite Fields Appl.* 109, Article ID 102712, **25 p.** (2026); MSC 94B15, 13C10, 11T71; Full Text links: DOI and arXiv.
  `https://zbmath.org/1576.94064`
- Publisher page: `https://www.sciencedirect.com/science/article/abs/pii/S107157972500142X`
- arXiv version: `https://arxiv.org/html/2305.15237` (v1, 24 May 2023).

**Publisher-snippet comparison (numbering demonstrably differs).**

- The publisher abstract, introduction, and conclusion snippets describe the same results in scope as the arXiv text: GPM for the `κ`-Galois dual; associated quasi-cyclic code `Q_G` with `dim Q_G = dim C − dim h_κ(C)`; determinantal-divisor hull-dimension formula; GPM for `h_κ(C)`; self-orthogonal/LCD criteria. The Section 4 snippet retains the same hypothesis `Λ^{−p^{−κ}} = Λ` and the same `Q_G` dimension relation.
- **Numbering is not the same as arXiv.** The publisher introduction names the main GPM result as **“Theorem 18”**, where arXiv v1 names it **Theorem 28**. The publisher Section 4 opening cites **“Theorem 4”** and **“Corollary 7”** at the exact points where the arXiv text cites **Theorem 8** and **Corollary 11**. The publisher version therefore appears condensed/renumbered relative to arXiv v1.
- Consequently: arXiv theorem numbers (8, 9, 10, 11, 21, 25, 28, …) must **never** be cited as publisher theorem numbers. Result-level equivalence of every hypothesis and statement between the publisher version and arXiv v1 remains **unverified** without the publisher full text.

**Status (c) — multi-twisted publisher-version equivalence:** **METADATA VERIFIED; SNIPPET-LEVEL SCOPE CONSISTENT; THEOREM NUMBERING DIFFERS; FULL THEOREM EQUIVALENCE UNRESOLVED.** The overlap classification from P1-01 stands unchanged: **Partial overlap (strong)** for hull-generator/dimension machinery at arXiv level; no labeled joint enumerator, transfer trace, or moment formula found in the inspected text.

---

## 3. Task 3 — Check D database-search record

**Date of searches:** 21 October 2026.  
**Platforms actually searched:** general web discovery (`web_search`); publisher/discovery pages (SpringerLink, ScienceDirect, AIMS, ACM Digital Library records surfaced through search); arXiv search (`https://arxiv.org/search/`); zbMATH Open (`https://zbmath.org/`).  
**Platforms NOT searched (no lawful access from this workspace):** MathSciNet, Scopus, Web of Science, and any interlibrary-loan catalogue. Google Scholar was not queried as a separate systematic platform. Coverage is therefore **documented but non-exhaustive**.

### 3.1 Exact queries and outcomes

**General web discovery (`web_search`):**

| # | Exact query | Relevant results | Verdict |
|---|---|---|---|
| D1 | `"Galois hull" "repeated-root" enumeration constacyclic` | Repo L1 ACM record; general Galois-hull papers; repeated-root references inside other papers | No joint enumerator found |
| D2 | `"hull enumeration" constacyclic affine algebra Galois` | Repo L4 ScienceDirect/arXiv; repo L2; repo L1 | No code-count by hull dimension over `A`; repo L4 counts dimension *values* only |
| D3 | `"Galois hull" "transfer matrix" enumeration codes` | Only unrelated transfer-matrix enumerations (statistical mechanics/combinatorics) and hull-dimension papers without transfer matrices | No transfer-trace hull enumerator found |
| D4 | `"joint distribution" "hull dimension" "code dimension" constacyclic enumerator` | Joint **weight** enumerator of an LCD code and its dual (different object); repo L2; repo L4; small-hull repo L3 | No joint `(dim C, dim hull)` enumerator found |
| D5 | `"hull" "multiplicity" "transfer matrix" cyclic codes enumeration` | No relevant record returned | No counterpart found |
| D6 | `"number of constacyclic codes" "Galois hull dimension"` | Repo L1 and its correction; repo L4 | Closest threat remains repo L1 (unresolved, §1) |
| D7 | `"bivariate" generating polynomial "hull dimension" codes enumeration` | Weight-enumerator references; double/four-circulant hull enumeration (Euclidean, different family) | No counterpart found |
| D8 | `"repeated-root" "Galois hull" codes` | Repo L1/L4 and citing works; serial-code hull enumerations over other alphabets (e.g. `Z_pZ_p[v]`, Euclidean) | No Galois repeated-root **joint** enumeration found |

**arXiv search (All fields, abstracts shown, sorted by announcement date):**

| # | Exact query | Outcome |
|---|---|---|
| A1 | `"Galois hull" "repeated-root"` | “produced no results” |
| A2 | `"Galois hull" "transfer matrix"` | “produced no results” |
| A3 | `"hull enumerator" constacyclic` | “produced no results” |

**zbMATH Open (fielded one-line search):**

| # | Exact query | Outcome |
|---|---|---|
| Z1 | `ti:"Galois hulls" & any:constacyclic` | **Found 5 Documents**: repo L4 (Zbl 1582.94185), repo L8 (Zbl 1576.94064), repo L2 (Zbl 1579.94062, *Adv. Math. Commun.* 19, No. 6, 1569–1604 (2025)), repo L1 correction (Zbl 1518.94137), repo L1 (Zbl 1518.94136). Only 2 indexed as open versions (the arXiv-backed repo L4/L8). |
| Z2 | `any:"repeated-root" & any:"Galois hull"` | “No Documents Found” |
| Z3 | `any:"transfer matrix" & any:"hull" & any:enumeration` | “No Documents Found” |

### 3.2 Closest relevant non-duplicates found by Check D

These were checked as neighbours; none is the project’s labeled joint enumerator in the inspected records:

- **Repo L1** (finite fields): hull-dimension formula + hull-dimension counting under restrictions on `q` — unresolved, §1. This is the principal remaining threat.
- **Repo L4** (affine): cardinality of the *set of attainable hull-dimension values*; code enumeration explicitly left open in the arXiv conclusion.
- **Repo L2** (DOI `10.3934/amc.2025010`): average Galois hull dimensions over finite fields and `R_{m,q}` — a mean, not a joint distribution.
- Classical hull counting for general linear/cyclic codes (Sendrier; Skersys, as cited inside repo L4’s introduction) — different code families and pairings.
- Double/four-circulant hull enumeration (arXiv:2307.05449) — Euclidean hulls of circulant families, not the Galois affine repeated-root exponent model.
- Serial-code hull enumerations over other alphabets (e.g. `Z_pZ_p[v]`-cyclic codes) — different alphabet and pairing.

### 3.3 Limitations (binding)

- MathSciNet, Scopus, and Web of Science were **not** searched; zbMATH phrase syntax may miss records whose abstracts use different terminology (e.g. “distribution”, “counting”, “generating function” without the word “enumerator”).
- arXiv search covers arXiv metadata/abstracts as indexed on the search date; it is not a full-text search of all preprints, and non-arXiv manuscripts are invisible to it.
- Web discovery is ranking-dependent and is not a systematic-review protocol.
- **Non-discovery is not novelty.** Check D found no exact duplicate of T5/T6 in the searched records, but Gate G1 cannot convert that into a priority claim while repo L1’s theorems remain uninspected and major databases remain unsearched.

**Status (d) — joint enumerator and transfer-trace novelty:** **NO COUNTERPART FOUND in the inspected full texts (repo L4, repo L8) and in the Check-D records above; NOVELTY NOT APPROVED.** T5/T6 may be described only as “no counterpart found in the text/records inspected so far.”

**Status (e) — database-search coverage:** **DOCUMENTED BUT NON-EXHAUSTIVE.** Platforms, exact queries, date, relevant results, and limitations are recorded in this §3. No exhaustive-coverage claim is made.

---

## 4. Task 4 — C5 hull-mean correction: exact record (not approved, not applied)

The frozen blueprint `02_THEOREM_BLUEPRINT.md` was **not** edited in P1-02. Its original C5 hull-mean display remains in place (line 82 at the time of P1-02). The following is the exact mathematical record required by the command; it approves nothing.

### 4.1 The length-1 orbit identity

Let `A ~ Uniform{0, …, P}`. For a `τ`-orbit of length `L = 1`, the single hull edge is a self-loop, so the per-edge hull statistic is `min(P − A, A)` (the predecessor exponent is the exponent itself). Then

```
E[min(P − A, A)] = ⌊P²/4⌋ / (P + 1)  =: ν_P.
```

Derivation (recorded exactly): the values `min(P−a, a)` for `a = 0,…,P` are symmetric under `a ↔ P−a`, and

- if `P = 2m`: `Σ_{a=0}^{P} min(P−a,a) = 2·Σ_{a=0}^{m−1} a + m = m² = P²/4`;
- if `P = 2m+1`: `Σ_{a=0}^{P} min(P−a,a) = 2·Σ_{a=0}^{m} a = m(m+1) = (P²−1)/4`.

In both cases the sum is `⌊P²/4⌋`; dividing by the `P+1` equally likely values gives `ν_P`. Checks: `ν_1 = 0` (for `P=1`, `min(1−A,A) ≡ 0`), `ν_2 = 1/3`, `ν_3 = 1/2`, `ν_5 = ⌊25/4⌋/6 = 1` — see the exact rational checks already recorded in P1-01 §8 (`(P,L)=(3,2)`: brute force `1` vs frozen `5/3`; `(P,L)=(5,2)`: `23/9` vs `25/9`; formula verified exactly for `P = 1…20` and orbit cases `P ∈ {1,2,3,4} × L ∈ {1,2,3}`).

### 4.2 What this resolves, orbit length by orbit length

Under the frozen standing hypotheses (labeled exponent assignments; each exponent uniform on `{0,…,P}`; distinct factors independent; compatible twists only; T4’s hull contribution `w_O Σ_i min(P − α_i, α_{i−1})` taken as given):

- **`L = 1` — fully resolved at first-moment level.** For every `P ≥ 1`, `E[H_O] = w_O · ν_P` with `ν_P = ⌊P²/4⌋/(P+1)`. The frozen C5 edge mean `μ_P` is **false** here because it wrongly treats the self-loop as two independent uniforms.
- **`L ≥ 2` — edge mean confirmed; orbit mean follows by linearity.** For each edge, the two exponents are *distinct* independent uniforms, so with `X, Y` independent uniform on `{0,…,P}`,
  `E[min(X,Y)] = Σ_{t=1}^{P} ((P−t+1)/(P+1))² = P(2P+1) / (6(P+1)) =: μ_P`,
  and hence `E[H_O] = w_O · L · μ_P`. Linearity of expectation needs no independence between edges; this holds also for `L = 2` (two opposite edges on one pair) and `L = 3` (adjacent edges share exponents) **as a statement about the mean only**.
- **Candidate corrected total (UNAPPROVED, not applied to the frozen file):**
  `E[H] = μ_P · Σ_{L_O ≥ 2} w_O L_O  +  ν_P · Σ_{L_O = 1} w_O`,
  with `μ_P = P(2P+1)/(6(P+1))` and `ν_P = ⌊P²/4⌋/(P+1)`.

### 4.3 What remains unproved / undecided in the general mean theorem

1. **Approval.** The split formula above is a *candidate correction only*. It has not been approved by the Boss and has not been applied to `02_THEOREM_BLUEPRINT.md`. Any future use requires a separate, dated correction decision; the frozen display must not be silently replaced.
2. **Variance (C6) is untouched.** The identity in §4.1 settles only the first moment. Still required: the `L=1` second moment of `min(P−A,A)`; the `L=2` covariance of the two opposite edges `min(P−α_0,α_1)` and `min(P−α_1,α_0)`; and the `L≥3` adjacent-edge covariances, each as closed forms in `P`. None of these is proved by the mean computation.
3. **Conditionality on T1–T4.** The mean computation presupposes the τ-orbit decomposition and T4’s exponent hull formula. Until those are formally proved in the frozen labeled `K_s`-model, the corrected mean is a conditional consequence, not a proved theorem.
4. **Code-dimension mean not re-decided.** P1-02 re-derived only the hull-edge expectations above. The `E[dim C]` display bundled into frozen C5 was not independently re-approved in P1-02 and inherits the same “do not use without approval” status.
5. **Scope.** The computation is for uniform **labeled** exponent assignments with independent exponents, in the compatible-twist case only. It says nothing about equivalence/isometry classes, incompatible twists, or non-uniform code distributions.

**Status (f) — C5 correction and remaining mean obligations:** **DERIVED AND EXACTLY RECORDED; CONFIRMED computationally in P1-01; NOT APPROVED AND NOT APPLIED.** First moments are resolved for every orbit length (`L=1` by `ν_P`; `L≥2` by `μ_P` per edge). Variance, formal T1–T4 dependence, and the Boss’s correction decision remain open.

---

## 5. Consolidated Gate G1 status table

| # | Question | Status after P1-02 | Evidence level |
|---|---|---|---|
| (a) | Prior finite-field hull-dimension counting (repo L1) | **Unresolved / partial overlap (potentially critical)** | B (abstract + zbMATH summary); no lawful full text |
| (b) | Affine-algebra repeated-root overlap (repo L4) | **Partial overlap (strong)** for individual hull formula; enumeration left open by its authors | A at arXiv; B (metadata/snippets) for publisher version |
| (c) | Multi-twisted publisher-version equivalence (repo L8) | **Metadata verified; numbering differs (Thm 18 vs arXiv Thm 28); full equivalence unresolved** | A at arXiv; B (metadata/snippets) for publisher version |
| (d) | Joint enumerator / transfer-trace novelty (T5/T6) | **No counterpart found in inspected texts/records; novelty NOT approved** | A for repo L4/L8 texts; Check-D record §3 |
| (e) | Database-search coverage (Check D) | **Documented but non-exhaustive** (MathSciNet/Scopus/WoS not searched) | Search record §3, dated 21 Oct 2026 |
| (f) | C5 correction / mean obligations | **Derived and recorded; not approved, not applied; variance unproved** | Exact derivation §4; P1-01 computation |

---

## 6. Decision

**CONDITIONAL GO.**

Rationale: no exact duplicate of the joint enumerator T6 or the transfer trace T5 was found in any inspected text or Check-D record, and the closest affine source explicitly leaves code enumeration over `𝒜` open — so the project is not stopped. But Gate G1 cannot be declared closed, and no novelty/priority claim is authorized, because (i) repo L1’s counting theorems remain uninspected for lack of a lawful full text, (ii) publisher-version theorem equivalence for repo L4/L8 is unverified (and repo L8’s publisher numbering demonstrably differs from arXiv), and (iii) Check D is non-exhaustive. The frozen C5 display remains uncorrected in the blueprint and must not be used.

---

## 7. Exactly one recommended next command

> **P1-03 — Boss-enabled repo L1 full-text closure and Gate-G1 re-vote:** obtain the lawful full text of repo L1 (Debnath–Prakash–Islam, DOI `10.1007/s12095-022-00591-6`, including its correction DOI `10.1007/s12095-022-00602-6`) through the Boss’s institutional/library access, interlibrary loan, or a direct author request, and supply it to the workspace; Arena then extracts the exact theorem numbers, hypotheses on `n`, `λ`, and `q`, exponent range, and counting object (resolving L1-Q1…L1-Q8), re-votes Gate G1, and records the Boss’s separate decision on whether the §4.2 split mean formula may replace frozen C5. Until then: no manuscript drafting, no novelty/priority wording, and no edit to frozen C5.

**One question for the Commander:** Can you obtain the repo L1 publisher PDF (or a lawful author manuscript) through your institution/library/ILL or from the authors? That single document is now the main blocker for closing Gate G1.
