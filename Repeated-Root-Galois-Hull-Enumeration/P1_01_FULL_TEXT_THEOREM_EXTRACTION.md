# P1-01 — Full-Text Theorem Extraction and Overlap Audit

**Command:** P1-01 — Full-Text Theorem Extraction and Overlap Audit  
**Date:** 20 October 2026  
**Gate status after P1-01:** **Gate G1 remains open.**  
**Overall recommendation:** **CONDITIONAL GO** — continue only to the single closure command recommended in §10. No manuscript drafting and no novelty/priority claim is authorized by this file.

This audit compares the frozen project statements in `02_THEOREM_BLUEPRINT.md` (T1–T6, C1–C7) with the closest literature. It does **not** edit those frozen statements and does **not** edit prototype code.

---

## 0. Label map — read this first

The command labels and the repository labels are shifted. This file uses **repository labels** and prints the command label beside them.

| Command label in P1-01 | Repository label used here | Source |
|---|---|---|
| Command “L1” | **Repo L4** | Debnath–Islam–Martínez-Moro–Prakash, affine algebra rings, arXiv:2412.08512, DOI `10.1016/j.disc.2025.114750` |
| Command “L4” | **Repo L8** | Eldin–Solé, multi-twisted Galois hulls, arXiv:2305.15237, DOI `10.1016/j.ffa.2025.102712` |
| Command “L3” | **Repo L1** | Debnath–Prakash–Islam, finite fields, DOI `10.1007/s12095-022-00591-6` |
| Command “L8” | **Ambiguous** | Interpreted here as: publisher-version/scope closure for repo L8, plus repo L9/L10 repeated-root publisher records, repo L3 small-hull, and repo L2 average sources. |

No source was silently renumbered.

---

## 1. Evidence rules used

Evidence levels are kept separate:

- **Level A — theorem text inspected:** exact theorem/proposition statement was read in an accessible full text.
- **Level B — publisher abstract/introduction/table inspected:** scope is verified, but theorem numbers/hypotheses are not all verified.
- **Level C — correction/secondary quotation inspected:** useful for scope, not enough for exact overlap.

**Inaccessible full text is not evidence of absence.** Where only Level B/C evidence exists, the overlap decision is **Unresolved**, not “no overlap”.

The phrase “no counterpart found” below always means: *no counterpart was found in the text actually inspected under the stated evidence level.* It is not a priority proof.

---

## 2. Project baseline used for comparison (frozen; not edited)

Setting: fixed labeled decomposition `A ≅ ∏_s K_s`, `K_s = F_{q^{m_s}} = F_{p^{d_s}}`, `q = p^e`, `d_s = e m_s`; code-first pairing; `n = P n_0`, `P = p^ϱ`, `gcd(n_0,p)=1`; component modulus `x^n − λ_s = (x^{n_0} − μ_s)^P = ∏_{f∈F_s} f^P`; codes parametrized by exponents `a_f ∈ {0,…,P}`; compatible twists only: `λ_s^{1+p^{d_s−k}} = 1` componentwise.

Frozen comparison targets:

- **T3/T4:** dual exponent `β_i = P − α_{i−1}`, hull-generator exponent `max(α_i, P − α_{i−1})`, and hull contribution `w_O Σ_i min(P − α_i, α_{i−1})`.
- **T5/T6:** `(P+1)`-state transfer matrix `T^{(P)}_w(u,z)_{a,b} = u^{w(P−b)} z^{w min(P−b,a)}` and global joint enumerator `E(u,z) = ∏_s ∏_O tr((T^{(P)}_{w_O})^{L_O})`.
- **C3/C4:** LCD count `2^{#τ-orbits}`; self-orthogonal iff cyclically `α_{i−1}+α_i ≥ P`; dual-containing iff cyclically `α_{i−1}+α_i ≤ P`.
- **C5/C6:** mean and variance consequences. C5 is separately investigated in §8 because BP-01 found the frozen hull-mean formula false for `L_O = 1`.

---

## 3. Repo L4 — affine algebra paper (command “L1”)

**Bibliographic record.** Indibar Debnath, Habibul Islam, Edgar Martínez-Moro, Om Prakash, “Galois hulls of constacyclic codes over affine algebra rings,” *Discrete Mathematics* 349(2), February 2026, Article 114750. DOI: `10.1016/j.disc.2025.114750`. Publisher page: `https://www.sciencedirect.com/science/article/abs/pii/S0012365X25003589`. Accessible theorem text: arXiv HTML `https://arxiv.org/html/2412.08512`. The PDF stored in the repository root is **not** the publisher PDF: local extraction of its first page identifies it as `arXiv:2412.08512v1 [cs.IT] 11 Dec 2024`.

**Evidence level:** A for arXiv theorem text; B for publisher version (abstract, introduction, section snippets and references only). Publisher theorem numbering was **not** independently verified against arXiv numbering.

### 3.1 Setting and convention extracted from arXiv text

- Alphabet: affine algebra `𝒜 = F_q[X_1,…,X_ℓ]/I`, `I = ⟨t_1(X_1),…,t_ℓ(X_ℓ)⟩`, each `t_i` square-free.
- §2.1 decomposes the algebra by primitive idempotents `e_{S(ν)}` and identifies `e_{S(ν)}R ≅ F_q(ν_1,…,ν_ℓ)`.
- §2.3 nevertheless presents projection codes `C_{S(ν)} ⊆ F_q^n` and twists `λ_{S(ν)} ∈ F_q`. This presentation must be reconciled with the project’s `K_s`-component code model before any exact domain-equivalence claim is made. **Do not assert that the affine component model is identical to the frozen labeled `K_s` model solely from the arXiv HTML.**
- Pairing (§2.2, Eq. (2)) is candidate-first in the sense used in this audit:
  `⟨α,β⟩_k = Σ_i α_i β_i^{p^k}`, and `C^{⊥_k} = {α : ⟨α,c⟩_k = 0 for all c ∈ C}`.
  This is not the frozen code-first placement; the two are related only through the project’s `ρ`-transport, which must be stated explicitly in any comparison.

### 3.2 Theorem-level extraction (arXiv numbering)

- **Theorem 5:** the Galois dual is generated by  
  `h̃(x) = Σ_{S(ν)} e_{S(ν)} h_{S(ν)}^#(x)`.
- **Theorem 7:** the Galois hull decomposes componentwise and is generated by  
  `Σ_{S(ν)} e_{S(ν)} lcm(g_{S(ν)}(x), h_{S(ν)}^#(x))`.
- **Theorem 8:** for `n = n′ p^{e′}`, `gcd(n′,p)=1`, under `gcd(ord(λ), n′)=1` and `ord(λ) | 1 + p^{e−k}`, the `q`-dimension of the `k`-Galois hull is
  `Σ_{S(ν)} Σ_t Σ_{j∈D_{S(ν)t}} ord_j(q) · b_{S(ν)tj}`,
  where the `b`-terms are built from cyclic sums of
  `a_t p^{e′} − Σ_δ max{u_δ, p^{e′} − u_{δ−1}}`
  and generator exponents satisfy `0 ≤ u ≤ p^{e′}`.
- **Corollary 3.5:** counts **attainable hull-dimension values** (the cardinality of a dimension set), not codes.
- **Conclusion (arXiv §5):** explicitly states that enumeration of non-isometric constacyclic codes for a given Galois hull dimension over `𝒜` is still open and that counting codes for a given hull dimension over `𝒜` may be interesting future work.

### 3.3 What was not found in the inspected L4 text

No joint `(dim C, dim hull)` enumerator, no `(P+1)`-state exponent transfer trace, no code-count by hull dimension, and no mean/variance formula was found in the inspected arXiv text.

### 3.4 Overlap decision for repo L4

**Partial overlap — strong at the individual hull-formula level, not a verified duplicate of T6.**

Theorem 8 substantially overlaps the *individual-code* repeated-root exponent hull-dimension computation, but under extra hypotheses (`gcd(ord(λ),n′)=1`, `ord(λ)|1+p^{e−k}`) and in a component presentation that still needs publisher/domain reconciliation. It does not, in the inspected text, count labeled exponent assignments jointly by code dimension and hull dimension.

---

## 4. Repo L8 — multi-twisted paper (command “L4”)

**Bibliographic record.** Ramy F. Taki Eldin, Patrick Solé, “Generator polynomial matrices of the Galois hulls of multi-twisted codes.” arXiv:2305.15237v1, 24 May 2023: `https://arxiv.org/html/2305.15237`. Publisher version verified bibliographically: *Finite Fields and Their Applications* 109 (January 2026), Article 102712, DOI `10.1016/j.ffa.2025.102712`, ScienceDirect PII `S107157972500142X`: `https://www.sciencedirect.com/science/article/abs/pii/S107157972500142X`.

**Evidence level:** A for arXiv theorem text through Theorem 28 / Corollary 29; B for publisher version (same-scope abstract/introduction verified; publisher theorem numbering **not** independently verified).

### 4.1 Setting and convention extracted from arXiv text

- Codes: Λ-multi-twisted codes over `F_q`, `q=p^e`, block lengths `(m_1,…,m_ℓ)`, nonzero twists `Λ=(λ_1,…,λ_ℓ)`. No general `gcd(m_j,p)=1` hypothesis was found in the inspected definitions/theorems.
- Index `ℓ = 1` specializes to constacyclic codes.
- Pairing is candidate-first in the paper’s Galois form: `⟨a,b⟩_κ = ⟨a, σ^κ(b)⟩` (Definition 6, as inspected).
- Main hull hypotheses repeatedly use `Λ^{−p^{−κ}} = Λ`.

### 4.2 Theorem-level extraction (arXiv numbering)

- **Theorem 8:** hull dimension via generator-matrix rank.
- **Theorem 9:** Galois dual twist type.
- **Theorem 10:** Euclidean-dual GPM and `H_κ = σ^{e−κ}(H)`.
- **Corollary 11:** hull MT type under `Λ^{−p^{−κ}} = Λ`.
- **Theorem 21:** with `Q_G` the associated quasi-cyclic code,  
  `dim(Q_G) = dim(C) − dim(h_κ(C))`.
- **Corollary 22:** self-orthogonal iff `𝔅_G = 0`.
- **Theorem 25:** determinantal-divisor formula for hull dimension.
- **Corollary 26:** LCD criterion.
- **Theorem 28:** if `ℌ_G` is a GPM for the κ-Galois dual of `Q_G`, then `ℌ_G G` is a GPM for the Galois hull `h_κ(C)`.
- **Corollary 29:** self-orthogonal/LCD restatements.
- **Conclusion (arXiv §5):** restates dimension formula and GPM for the hull; future work points to chain rings. No enumeration is claimed.

### 4.3 What was not found in the inspected L8 text

No labeled joint `(dim C, dim hull)` enumerator, no `(P+1)`-state exponent transfer trace, no code-count by hull dimension, and no mean/variance formula was found in the inspected arXiv text.

### 4.4 Overlap decision for repo L8

**Partial overlap — strong for hull-generator/hull-dimension machinery, not a verified duplicate of the joint enumerator.**

Because constacyclic codes are the index-1 case and no simple-root restriction was found, T3/T4 must **not** be headlined as “the first repeated-root hull generator/formula”. The defensible centre remains the labeled joint enumerator/transfer trace, subject to Gate G1 closure.

---

## 5. Repo L1 — finite-field paper (command “L3”)

**Bibliographic record.** Indibar Debnath, Om Prakash, Habibul Islam, “Galois hulls of constacyclic codes over finite fields,” *Cryptography and Communications* 15 (2023), 111–127. DOI: `10.1007/s12095-022-00591-6`. Publisher page: `https://link.springer.com/article/10.1007/s12095-022-00591-6`. Correction: *Cryptogr. Commun.* 15 (2023), 129–130, DOI `10.1007/s12095-022-00602-6`: `https://link.springer.com/article/10.1007/s12095-022-00602-6`.

**Evidence level:** B/C only. The publisher abstract and the open correction were inspected. No lawful open full text with theorem bodies was located through the Springer route or targeted searches in P1-01. Exact theorem numbers therefore remain **unresolved**, not absent.

### 5.1 What is verified

Publisher abstract verifies:

- a formula for the dimension of Galois hulls of constacyclic codes over a finite field;
- “considering some restrictions on `q`”, the number of constacyclic codes of length `n` over `F_q` is calculated **for a given Galois hull dimension**.

The correction (DOI `10.1007/s12095-022-00602-6`) verifies repeated-root-flavoured machinery in the paper’s notation:

- sets `B_i` defined by divisibility conditions involving `p^{e l_1}`, `p^{e−k}` and `p^{i(e−k)}`;
- the corrected sentence: “we prove that `f^{i_1#}(x) ≠ f^{i_2#}(x)` for `1 ≤ i_1 < i_2 ≤ a_i`.”

Accordingly, Audit v1’s wording that repo L1 is “simple-root only” is **unsafe and must not be used**.

### 5.2 What remains unresolved

The following could not be lawfully extracted in P1-01 and must not be guessed:

- exact theorem/proposition numbers;
- standing hypotheses on `n,p,q,λ,k`;
- whether generator exponents run over `{0,…,P}` or a restricted subset;
- exact hull-dimension formula and orbit restrictions;
- exact counting theorem: hull dimension alone vs jointly with code dimension; labeled codes vs another counting convention;
- any transfer-matrix or moment formula.

### 5.3 Overlap decision for repo L1

**Unresolved overlap — potentially critical.**

The abstract already verifies hull-dimension counting over a single finite field under restrictions on `q`. Until the full text is lawfully obtained, the project may not claim that counting repeated-root codes by Galois hull dimension is new, and may not describe repo L1 as simple-root only.

---

## 6. Ambiguous command “L8”: publisher-version and neighbouring-scope closure

This section records the publisher/scope evidence for the remaining named neighbours. Unless “theorem text inspected” is stated, the evidence is Level B (publisher abstract/introduction/table).

### 6.1 Repo L8 publisher version

Verified: *Finite Fields and Their Applications* 109 (January 2026), Article 102712, DOI `10.1016/j.ffa.2025.102712`. The publisher abstract confirms the same GPM/hull scope as the arXiv text. Publisher theorem numbering was not independently verified; the manuscript must not cite arXiv theorem numbers as publisher theorem numbers without a separate publisher-PDF check.

### 6.2 Repo L3 — small Galois hull dimensions

**Record.** Indibar Debnath, Habibul Islam, Shikha Yadav, Om Prakash, “Study of small Galois hull dimensions of constacyclic codes,” *Advances in Mathematics of Communications* 22 (2026), 1–18. DOI: `10.3934/amc.2025054`. Publisher page: `https://www.aimsciences.org/article/doi/10.3934/amc.2025054`.

**Evidence level:** B. Abstract, introduction and Table 1 were inspected; theorem bodies were not exposed in the fetched publisher chunks, and the linked no-login full-text HTML fetch did not yield the bodies. Exact surrounding hypotheses/conventions therefore still require full-text confirmation.

Table 1 verifies **existence results only** for hull dimensions 1 and 2:

| Result | Condition (as tabulated) | Conclusion |
|---|---|---|
| Thm. 3.1 | `p ∣ n`, `ord(α) ∣ (1+p^{e−ℓ})`, `α^n = λ` | `dim(hull_ℓ(C)) = 1` |
| Thm. 3.9 | `gcd(p,n)=1`, `ord(α) ∣ n` but `∤ (1+p^{e−ℓ})` | `dim(hull_ℓ(C)) = 1` |
| Thm. 3.18 | `n = p^m`, `ord(α) ∣ (1+p^{e−ℓ})`, `α^n = λ` | `dim(hull_ℓ(C)) = 2` |
| Thm. 3.20 | `n ≥ 4` even, `2p ∣ n`, `ord(λ) ∣ gcd(n−1, 1+p^{e−ℓ})` | `dim(hull_ℓ(C)) = 2` |

EAQECC examples follow (Tables 2–3). No code-count, joint enumerator, transfer trace, mean or variance is verified by the inspected table/abstract.

**Decision:** **Partial overlap** for small-hull existence in repeated-root regimes (`p∣n`, `n=p^m`, `2p∣n`); no verified overlap with the joint enumerator.

### 6.3 Repo L2 — average Galois hull dimensions

**Record.** Indibar Debnath, Om Prakash, “Average dimensions of Galois hulls of constacyclic codes,” *Advances in Mathematics of Communications* 19(6) (2025), 1569–1604. DOI: `10.3934/amc.2025010`. Publisher page: `https://www.aimsciences.org/article/doi/10.3934/amc.2025010`.

**Evidence level:** B. Abstract and introduction were inspected; the full text is access-restricted.

Verified scope:

- formula for average dimensions of Galois hulls of constacyclic codes over **finite fields**;
- Galois inner product/dual over the ring `R_{m,q} = F_q[u]/⟨u^m − u⟩`;
- formulae for Galois hull dimensions and **average** Galois hull dimensions over `R_{m,q}`;
- LCD construction over `R_{m,q}` and examples;
- the finite-field average is organized around `Δ_1`, described in the introduction as the sum of degrees of irreducible factors `f` of `x^n − λ` with `f^#(x) = u f(x)` for a unit `u`.

No joint distribution, transfer trace or variance is verified by the inspected text.

**Decision:** **Partial overlap for the mean only.** The mean cannot be a headline novelty. Exact formula-level comparison with the corrected repeated-root affine mean remains open until L2’s theorem bodies/hypotheses are inspected.

### 6.4 Repo L9/L10 — repeated-root publisher-scope table (Check C, abstract level)

All rows below are **Euclidean** (not `k`-Galois) unless stated, over a **single finite field** (not the affine product), and at publisher-abstract scope.

| Record | Length/setting verified | What the publisher record verifies | Distance from project |
|---|---|---|---|
| Zhang–Wang–Luo–Li, *Finite Fields Appl.* 101 (Jan. 2025), Art. 102542, DOI `10.1016/j.ffa.2024.102542`, `https://www.sciencedirect.com/science/article/abs/pii/S1071579724001813` | Length `k^s ℓ^m p^n`, distinct odd primes `k,ℓ,p`, char. `p` | Explicit factorization of `x^{k^sℓ^mp^n} − λ`; all repeated-root constacyclic codes and duals characterized; characterization + enumeration of LCD cyclic/negacyclic codes | Special length; Euclidean LCD only; no Galois joint enumerator; no affine product |
| Chen–Dinh–Liu, *Finite Fields Appl.* 33 (2015), 137–159, DOI `10.1016/j.ffa.2014.11.006`, `https://www.sciencedirect.com/science/article/pii/S1071579714001282` | Length `2ℓ^m p^n` over `F_q`, char. `p` | Structure of constacyclic codes and duals via generator polynomials; characterization + enumeration of LCD and self-dual constacyclic codes | Special length; Euclidean; no Galois/affine/joint enumeration |
| Anuradha Sharma, *Cryptogr. Commun.* 7 (2015), 229–255, DOI `10.1007/s12095-014-0106-5`, `https://link.springer.com/article/10.1007/s12095-014-0106-5` | Length `ℓ^t p^s` over `F_{p^m}`, `ℓ≡1 (mod 2)`, distinct primes | Classification/structure of all repeated-root constacyclic codes and duals; self-dual cyclic/negacyclic listed when `p=2`; all self-orthogonal cyclic/negacyclic determined | Special length; Euclidean; structure/duals, not Galois hull counting |
| Wu–Zhu–Liu–Li, *Adv. Math. Commun.* 17(5) (2023), 1154–1180, DOI `10.3934/amc.2021044`, `https://www.aimsciences.org/article/doi/10.3934/amc.2021044` | Length `6ℓ^m p^n` over `F_q`, char. `p` | Structure of constacyclic codes and duals via generator polynomials; characterization + enumeration of LCD negacyclic and self-dual constacyclic codes | Special length; Euclidean; no Galois/affine/joint enumeration |
| Pang–Zhu–Li (repo L10), *J. Appl. Math. Comput.* 56 (2018), 625–635, DOI `10.1007/s12190-017-1118-z`, `https://link.springer.com/article/10.1007/s12190-017-1118-z` | General `n = n′ p^r`, `gcd(n′,p)=1`, cyclic over `F_q` | Necessary/sufficient LCD criterion for repeated-root cyclic codes; minimum distance of LCD repeated-root cyclic codes; enumeration of LCD repeated-root cyclic codes | General length but cyclic/Euclidean/single-field; LCD only — C3 must remain a corollary, never a headline |

**Decision for L9/L10:** **Verified partial overlap** for repeated-root structure/duals and for Euclidean LCD/self-dual/self-orthogonal enumerations in special (and, for L10, general cyclic) lengths. No inspected record gives a `k`-Galois affine labeled joint `(dim C, dim hull)` enumerator.

---

## 7. Five-way comparison against the proposed contributions

### 7.1 Repeated-root exponent-level hull formula

- Repo L4 Thm. 8 (arXiv) already gives an exponent-level repeated-root hull-dimension formula over the affine algebra under extra twist/order hypotheses.
- Repo L8 GPM theory gives hull dimension/generator machinery for MT codes, hence for index-1 constacyclic codes, without a found simple-root restriction.
- Repo L1’s exact formula remains unresolved; its correction proves repeated-root machinery is present.

**Verdict: Partial overlap (strong).** T4 must be positioned as the project’s labeled `K_s`-component exponent form under its stated compatibility, not as the first repeated-root hull formula.

### 7.2 Joint code-dimension/hull-dimension enumerator

- No joint `(dim C, dim hull)` enumerator was found in the inspected L4, L8, L3 or L2 texts.
- L4 Corollary 3.5 counts attainable dimension values, not codes; L4’s conclusion explicitly leaves code-counting by hull dimension over `𝒜` open.
- L1 verifies hull-dimension counting over a finite field under restrictions on `q`, but whether code dimension is recorded jointly is unresolved.

**Verdict: No counterpart found in inspected text; novelty not approved.** This remains the defensible centre **only conditionally**, because L1 is unresolved.

### 7.3 Transfer-matrix trace formula

- No `(P+1)`-state exponent transfer matrix or trace formula was found in the inspected texts.
- Repo L8 uses generator polynomial matrices, determinantal divisors and Hermite normal forms — a different mechanism from the frozen `(P+1)`-state exponent transfer trace.

**Verdict: No counterpart found in inspected text; novelty not approved** (same L1 caveat).

### 7.4 LCD count and self-orthogonality criteria

- Criteria-level overlap is verified: L4 Corollary 3.1/Theorem 9 context, L8 Corollaries 22/26/29, and L9/L10 Euclidean LCD/self-dual/self-orthogonal characterizations/enumerations.
- The specific labeled Galois affine consequence `#{a : Hull = 0} = 2^{#τ-orbits}` as a specialization of the joint enumerator was not found as such in the inspected text.

**Verdict: Partial overlap.** C3/C4 are corollaries/consequences only; they must never be headlined as new LCD enumeration.

### 7.5 Mean hull dimension and variance

- Mean: repo L2 already publishes average Galois hull dimensions over finite fields and over `R_{m,q}`. The frozen C5 mean is additionally **false for `L_O=1`** (see §8). A corrected split mean may survive only as an enumerator consequence for the repeated-root labeled affine model, after approval.
- Variance: no variance formula was found in the inspected L2/L4/L8/L3 texts. But frozen C6 has no derived closed form yet, so variance is not presently a claimable contribution.

**Verdict: Mean — partial overlap, not headline. Variance — no counterpart found in inspected text, but unproved; not claimable until RR-8 is derived and tested.**

---

## 8. GAP-01 / C5 — independent investigation (recorded separately; frozen file NOT modified)

### 8.1 Derivation for `L = 1`

For a length-one τ-orbit, the hull edge statistic is not a minimum of two independent uniforms. With `A` uniform on `{0,…,P}`, the statistic is

`X = min(P − A, A)`.

Hence

`E[X] = (1/(P+1)) Σ_{A=0}^P min(A, P−A) = ⌊P²/4⌋ / (P+1) =: ν_P`.

Proof of the numerator identity: pair `A` with `P−A`; the values `min(A,P−A)` are `0,1,…,⌊P/2⌋,…,1,0`, whose sum is `⌊P²/4⌋` (check separately for `P` even and `P` odd).

For `L ≥ 2`, a fixed edge uses two **distinct** orbit positions, so its marginal law is `min(U,V)` with `U,V` independent uniform on `{0,…,P}`, and

`E[min(U,V)] = Σ_{t=1}^P ((P−t+1)/(P+1))² = P(2P+1) / (6(P+1)) =: μ_P`.

Linearity of expectation needs no independence between different edges. Therefore the correct mean shape is the split form already recorded as a **proposal** in GAP-01:

`E[Hull] = μ_P Σ_{O: L_O≥2} w_O L_O + ν_P Σ_{O: L_O=1} w_O`,

with `μ_1 = 1/4`, `ν_1 = 0`, recovering the predecessor at `P=1`.

### 8.2 Executed check (P1-01)

A stdlib-`fractions` exact computation was run in `/tmp/p1_01_gap01_check.py` during P1-01 (temporary evidence; not a repo artifact). Results:

- `E[min(P−A,A)] = ν_P` matched brute force for every `P = 1,…,20`.
- Full-orbit brute means matched the split prediction for `(P,L) ∈ {1,2,3,4} × {1,2,3}` and matched the frozen formula exactly when `L ≥ 2`; the frozen formula failed exactly at `L = 1`.
- Blueprint counterexamples reproduced exactly:
  - `(n_0,P) = (3,2)`: brute/split mean `1` vs frozen C5 `5/3`.
  - `(n_0,P) = (5,2)`: brute/split mean `23/9` vs frozen C5 `25/9`.
  - Constants: `μ_2 = 5/9`, `ν_2 = 1/3`, `μ_1 = 1/4`, `ν_1 = 0`.

### 8.3 Decision

**GAP-01 is confirmed.** The frozen C5 hull-mean formula is false whenever an `L_O = 1` orbit occurs. The split formula above is the independently derived candidate correction, but it is **not approved and not applied** here. `02_THEOREM_BLUEPRINT.md` remains unchanged; a separate correction command must approve/reject it, edit C5 with a dated note, add the `L=1` vs `L≥2` proof, and rerun the counterexamples plus a `P=1` regression.

---

## 9. Per-contribution verdicts and overall recommendation

| Proposed contribution | Verdict | Basis |
|---|---|---|
| Repeated-root exponent-level hull formula (T4) | **Partial overlap (strong)** | L4 Thm. 8; L8 Thms. 21/25/28; L1 unresolved |
| Joint `(dim C, dim hull)` enumerator (T6) | **No counterpart found in inspected text — novelty NOT approved** | Absent in inspected L4/L8/L3/L2; L4 leaves counting open; L1 counting scope unresolved |
| Transfer-matrix trace formula (T5) | **No counterpart found in inspected text — novelty NOT approved** | L8 uses GPM/determinantal divisors, not exponent-state traces; L1 unresolved |
| LCD count + self-orthogonality criteria (C3/C4) | **Partial overlap** | L4/L8 criteria; L9/L10 Euclidean enumerations; keep as corollaries only |
| Mean hull dimension (C5) | **Partial overlap + frozen formula false for `L=1`** | L2 averages exist; GAP-01 confirmed; split correction unapproved |
| Variance (C6) | **No counterpart found in inspected text — unproved** | RR-8 closed forms still underived/untested |

**Overall: CONDITIONAL GO.** The joint labeled enumerator/transfer trace remains a coherent centre, but Gate G1 stays open because (i) repo L1’s counting theorem is unresolved at theorem level, (ii) publisher-vs-arXiv theorem equivalence is unverified for L4/L8, (iii) the L4 component-model equivalence with the frozen `K_s` model is unreconciled, and (iv) Check D database searches (MathSciNet/zbMATH/Scopus-style) have not been performed. Until those close, the manuscript may use no “first/new enumeration/priority” wording.

---

## 10. Exactly one recommended next command

> **P1-02 — Lawful full-text closure for repo L1 and publisher-version comparison (L1/L4/L8), with a Check-D database-search record.**

Scope of that single command: obtain repo L1’s full text by a lawful route (library/institutional access supplied by the Boss, inter-library loan, or author manuscript) and extract its exact counting theorem; reconcile L4/L8 publisher theorem numbering and the L4 component model against the versions inspected here; record MathSciNet/zbMATH/Scopus-style searches for “Galois hull” + “repeated-root”, “hull enumeration” + “constacyclic” + “affine”, and “hull” + “multiplicity” + “transfer matrix”. Deliverable: a closure note that either closes Gate G1 or converts the L1 overlap verdict from **Unresolved** to an evidence-backed decision. No manuscript drafting under P1-02 either.

---

## Appendix A — Stable source list for P1-01

1. Repo L4: arXiv `https://arxiv.org/abs/2412.08512`; HTML `https://arxiv.org/html/2412.08512`; DOI `10.1016/j.disc.2025.114750`; publisher `https://www.sciencedirect.com/science/article/abs/pii/S0012365X25003589`.
2. Repo L8: arXiv `https://arxiv.org/abs/2305.15237`; HTML `https://arxiv.org/html/2305.15237`; DOI `10.1016/j.ffa.2025.102712`; publisher `https://www.sciencedirect.com/science/article/abs/pii/S107157972500142X`.
3. Repo L1: DOI `10.1007/s12095-022-00591-6`; article `https://link.springer.com/article/10.1007/s12095-022-00591-6`; correction DOI `10.1007/s12095-022-00602-6`; correction `https://link.springer.com/article/10.1007/s12095-022-00602-6`.
4. Repo L3: DOI `10.3934/amc.2025054`; `https://www.aimsciences.org/article/doi/10.3934/amc.2025054`.
5. Repo L2: DOI `10.3934/amc.2025010`; `https://www.aimsciences.org/article/doi/10.3934/amc.2025010`.
6. Repo L9/L10 scope records: DOI `10.1016/j.ffa.2024.102542`; DOI `10.1016/j.ffa.2014.11.006`; DOI `10.1007/s12095-014-0106-5`; DOI `10.3934/amc.2021044`; DOI `10.1007/s12190-017-1118-z`.

## Appendix B — Limitations of P1-01

- No publisher PDF of L4 or L8 was lawfully inspected; the repository’s affine PDF is arXiv v1, not the publisher version.
- Repo L1 and repo L2 full texts are access-restricted; repo L3 theorem bodies were not exposed by the fetched publisher chunks.
- Check D (MathSciNet/zbMATH/Scopus-style exhaustive database search) was not performed in P1-01.
- The GAP-01 computation script was run from `/tmp` and is reported here as temporary evidence; saving it as a repo artifact is left to a later code command if the Commander so orders.
