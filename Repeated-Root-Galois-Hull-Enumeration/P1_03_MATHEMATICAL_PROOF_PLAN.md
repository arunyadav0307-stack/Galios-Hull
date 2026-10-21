# P1-03 — Mathematical Proof Plan and Continued Audit (despite the L1 access blocker)

**Command:** P1-03 — Continue Research Despite L1 Access Blocker  
**Date:** 21 October 2026  
**Decision:** **CONDITIONAL GO**  
**Gate G1 status:** **Still open.** No manuscript drafting, no novelty/priority claim, and no change to the frozen statements in `02_THEOREM_BLUEPRINT.md` is authorized by this file. Proposed corrections are recorded separately in §6 and are **not applied**.

This file (i) reassesses repo L1 and its correction from lawfully accessible sources only, (ii) gives an independent proof plan for the joint enumerator T6 and the transfer trace T5, (iii) formally derives the `L=1` mean contribution `ν_P`, (iv) reviews T1–T6, C1–C7, RR-1–RR-9 for errors, missing assumptions, and unproved claims, and (v) records extended computational validation that was actually executed.

---

## 1. Literature reassessment (Task 1) — repo L1 and its correction

Label convention is unchanged: **repo L1** = Debnath–Prakash–Islam, “Galois hulls of constacyclic codes over finite fields,” *Cryptogr. Commun.* 15(1), 111–127 (2023), DOI `10.1007/s12095-022-00591-6`; correction DOI `10.1007/s12095-022-00602-6`, *Cryptogr. Commun.* 15, 129–130 (2023).

### 1.1 New lawful evidence obtained in P1-03

1. **OpenAlex** (record `W4283360609`, fetched 21 Oct 2026): repo L1 has `open_access.is_oa = false`, `oa_status = "closed"`, `any_repository_has_fulltext = false`, `has_fulltext = false`; primary location is the DOI landing page with `pdf_url = null`.  
2. **Semantic Scholar API** (paper `4d023fda033d10a80723f94c8ac1a9c10469f6a5`, fetched 21 Oct 2026): `isOpenAccess = false`, `openAccessPdf.url = ""` (empty), CorpusId 250008629, DBLP key `journals/ccds/DebnathPI23`.  
3. **Springer correction page (full text lawfully readable)**: `https://link.springer.com/article/10.1007/s12095-022-00602-6`. The correction lists exactly **10 items**:
   1. two references missing from the reference list are added (Islam–Prakash–Bhunia 2019; Prakash–Yadav–Islam–Solé, AMC, DOI `10.3934/amc.2022017`);
   2. “the primitive element” → “a primitive element” (example over `F_8`);
   3. a **font-size** mismatch at p. 5, line 153, displaying the sets  
      `B_1 = { j ∈ N : ∃ l_1 ≥ 0, j | (p^{e l_1} + p^{e−k}) }`, and for `i > 1`,  
      `B_i = { j ∈ N \ (B_1 ∪ … ∪ B_{i−1}) : ∃ l_1 ≥ 0, j | (p^{e l_1} + (−1)^{i−1} p^{i(e−k)}) }`;
   4. “for some integer...” → “for an integer...” (two places in “Proof 2 after Example 1”);
   5. “for some unit...” → “for some units...” (“Proof 3 after Example 1”);
   6. “some integer” → “an integer” (two places, same proof);
   7. an `F_8` listing in Example 3 corrected to `{0, α, α², …, α⁷}`;
   8. p. 8, line 250: `1 ≤ i_1 ≤ i_2 ≤ a_i` → `1 ≤ i_1 < i_2 ≤ a_i`, in the sentence “Finally, we prove that `f^{i_1#}(x) ≠ f^{i_2#}(x)` for `1 ≤ i_1 < i_2 ≤ a_i`”;
   9. reference 9 title: “i” → “I” (“Permutation Group Algorithms Based on Partitions, I: Theory and Algorithms”);
   10. reference 14 title ends with “?” instead of “.” (“Is code equivalence easy to decide?”).

### 1.2 What this changes — and what it does not

- **L1-Q7 is narrowed, not closed.** The correction, as published, contains **no restatement of any theorem, hypothesis, or counting formula** among its 10 listed items: they are reference-list repairs, article/quantifier wording, a font-size display (whose displayed `B_i` definitions are nonetheless now verified notation of repo L1), one `F_8` example listing, a strict-inequality repair inside a proof sentence about distinct `#`-images, and two reference-title repairs. This is evidence that the correction is editorial/typographical in character. It is **not** a substitute for the original theorem text.
- The displayed `B_i` sets verify that repo L1 arranges cyclotomic data using divisibility conditions involving `p^{e l_1} ± p^{i(e−k)}` with Galois index `k`. This is consistent with the factor-arrangement language of the abstract, and with the later affine paper’s `B_i` notation (repo L4, arXiv §2.4). It says nothing by itself about the hypotheses on `n`.
- **Still unresolved (recorded, per command):** L1-Q1 (theorem numbers/statements), L1-Q2 (hypotheses on `n`; in particular whether `p | n` is included), L1-Q3 (hypotheses on `λ`), L1-Q4 (the exact “restrictions on `q`”), L1-Q5 (counting object: hull-dimension only vs joint), L1-Q6 (exponent range/model under multiplicity), L1-Q8 (whether the project’s finite-field specialization is already contained). L1-Q7 remains open only in the weaker sense that the correction’s effect on the *original proofs* cannot be fully assessed without the original text.
- Two independent open indexes (OpenAlex, Semantic Scholar) now agree with zbMATH: **no lawful open full text of repo L1 is indexed**. Per the command, the search stops here and the work proceeds; nothing about repo L1’s theorems is invented.

**Literature-overlap status after P1-03:** unchanged in kind — repo L4 **partial overlap (strong)** at the individual hull-formula level; repo L8 **partial overlap (strong)** for hull GPM machinery; repo L1 **unresolved / potentially critical**; T5/T6 **no counterpart found in inspected texts or search records; novelty NOT approved**.

**Gate G1 status after P1-03:** **Open**, but no longer blocking mathematical work: the remaining gap is a novelty/priority question, not a correctness question. No novelty sentence may be drafted until L1-Q1…Q6/Q8 are resolved or explicitly waived by a later command.

---

## 2. Standing assumptions and convention lock for the proof plan (Task 3)

Everything below is componentwise. Fix one component and suppress `s`: `K = F_{p^d}` (`d = d_s`), `q`-dimension is recovered at the end by multiplying by `m_s` (since `K = F_{q^{m_s}}`).

- **A1 (fields).** `p` prime; `K = F_{p^d}`; Galois index `k` with `0 ≤ k ≤ d−1` in the single-component reading (blueprint: `0 ≤ k < e`, `d = e m_s`). `σ(α) = α^{p^k}`, `ρ(α) = α^{p^{d−k}}`; then `ρ = σ⁻¹` on `K` because `α^{p^d} = α`.
- **A2 (pairing order — the lock).** The code-first pairing is `⟨x, y⟩_k = Σ_{i=0}^{n−1} x_i σ(y_i)`, and the dual is  
  `D(C) = { y : ⟨c, y⟩_k = 0 for all c ∈ C }` — code vector in the **first** slot, candidate in the **second**.  
  With this order, `y ∈ D(C) ⟺ ρ(y) ∈ C^⊥` (Euclidean dual), i.e. `D(C) = ρ(C^⊥)` coordinatewise. (If the opposite order were adopted, `σ` and `ρ` would interchange throughout; see PC-2 in §6. The frozen blueprint does not state this order explicitly — that is a genuine gap this plan repairs on paper only.)
- **A3 (length).** `ϱ ≥ 0`, `P = p^ϱ ≥ 1`, `n = P n_0`, `gcd(n_0, p) = 1`.
- **A4 (twist).** `λ ∈ K*` is **compatible**: `λ^{1 + p^{d−k}} = 1`. `μ ∈ K*` is the unique element with `μ^P = λ` (Frobenius `a ↦ a^P` is a bijection of the finite field `K`).
- **A5 (factorization).** `M(x) = x^n − λ = (x^{n_0} − μ)^P =: S(x)^P`, using `(x^{n_0} − μ)^P = x^{n_0 P} − μ^P` in characteristic `p`. `S` is **separable**: `gcd(S, S′) = 1` because `S′ = n_0 x^{n_0−1}` with `p ∤ n_0`, and any root `α` of `S` satisfies `α^{n_0} = μ ≠ 0`, so `α ≠ 0` and `S′(α) ≠ 0`. Hence `S = ∏_{f∈F} f` with **distinct** monic irreducibles `f`, and `M = ∏ f^P`.
- **A6 (reciprocal).** For monic `f(x) = Σ_{i=0}^r c_i x^i` with `c_0 ≠ 0` (automatic for `f | S`, since `S(0) = −μ ≠ 0`),  
  `f#(x) = ρ(c_0)^{-1} Σ_{i=0}^r ρ(c_i) x^{r−i}` (monic of degree `r`). `τ(f) := f#`.
- **A7 (compatibility equivalent form).** `λ^{1+p^{d−k}} = 1 ⟺ μ^{1+p^{d−k}} = 1` (raise to the `P`-th power; in characteristic `p`, `y^P = 1 ⟹ y = 1`). Under A4, `τ` permutes `F`: if `α^{n_0} = μ` then `β = α^{−p^{d−k}}` satisfies `β^{n_0} = μ^{−p^{d−k}} = μ`, so `#` sends roots of `S` to roots of `S`, hence factors to factors.
- **A8 (orbit indexing).** A `τ`-orbit is written `O = (f_0, …, f_{L−1})` with `τ(f_i) = f_{i+1}` (indices mod `L`), `α_i := a_{f_i} ∈ {0,…,P}`. **Predecessor of `i` is `i−1`.** Reversing the enumeration is not a symmetry of the formulas and is not permitted.
- **A9 (counting scope).** Assignments `a = (a_f)` are **labeled** (factors are named, not factored by equivalence/isometry). Codes are `K`-linear (globally: `A`-submodules, `A ≅ ∏_s K_s`); global codes are tuples of component codes (CRT). `u, z` are commuting indeterminates; all enumerators live in `Z[u, z]` with nonnegative coefficients.
- **A10 (dimensions).** Component dimensions are over `K`; blueprint dimensions are `dim_{F_q} = m_s · dim_K` per component, summed over `s`. The ambient `F_q`-dimension of component `s` is `m_s n`.

**Proof-dependency map (unchanged in shape, now with owners):**
`T1 (bijection) + T2 (# multiplicativity) → T3 (dual exponents, via RR-3 Euclidean lemma + RR-4 twist check) → T4 (hull, via RR-5 lcm lemma) → T5 (trace, RR-6) → T6 (global product, RR-7) → C1–C5; C6 needs RR-8; C7 needs RR-9 (external distance input).`

---

## 3. Proof plan for T1–T6 (Task 3)

### T1 — Parametrization. *Route: complete (routine).*
`K[x]` is a PID. Ideals of `K[x]/(M)` correspond to ideals `(M) ⊆ I ⊆ K[x]`, i.e. to `I = ⟨ḡ⟩` with `ḡ` a monic divisor of `M`, unique. By A5, monic divisors of `M = ∏ f^P` are exactly `g_a = ∏ f^{a_f}`, `a_f ∈ {0,…,P}`. Hence `a ↦ C(a) = ⟨g_a⟩` is a bijection onto `λ`-constacyclic codes of length `n` over `K`; `dim_K C(a) = n − deg g_a`. Globally, CRT over `A ≅ ∏_s K_s` gives the product bijection and total `(P+1)^{Σ_s |F_s|}`. **Obligation RR-1:** write the ideal correspondence explicitly for the non-semisimple quotient (no idempotents, no separability used). *Status: proof-ready; formal write-up pending.*

### T2 — Reciprocal with multiplicities. *Route: complete; one hypothesis to make explicit (PC-3).*
Write `f̃(x) = Σ ρ(c_i) x^i` (coefficientwise `ρ`). Then `f#(x) = ρ(c_0)^{-1} x^r f̃(x^{-1})`. For monic `f, g` of degrees `r, t` with nonzero constant terms: `fĝ = f̃ ĝ` (ρ is a field automorphism), and `x^{r+t}(f̃ĝ)(x^{-1}) = [x^r f̃(x^{-1})][x^t ĝ(x^{-1})]`, while `ρ((fg)_0)^{-1} = ρ(f_0)^{-1}ρ(g_0)^{-1}`. Hence **`(fg)# = f# g#`**, and therefore `(∏ f^{a_f})# = ∏ (f#)^{a_f}` — the prime-power multiplicativity is this one line, not a root argument. Root action: extend `α ↦ α^{p^{d−k}}` to an algebraic closure; if `f(α) = 0` (`α ≠ 0` as `c_0 ≠ 0`) then applying that Frobenius power to `Σ c_i α^i = 0` gives `f̃(α^{p^{d−k}}) = 0`, so `f#` vanishes at `α^{−p^{d−k}}`. A7 is proved in §2. *Status: proof-ready.*

### T3 — Code-first dual exponents. *Route: complete modulo RR-3; convention lock A2 is essential.*
Two ingredients.
**(RR-3, Euclidean-dual lemma, no separability.)** Let `C = ⟨g⟩ ⊆ K[x]/(x^n − λ)`, `h = (x^n − λ)/g`. Claim: the Euclidean dual is `C^⊥ = ⟨h^*⟩`, a `λ^{-1}`-constacyclic code, where `h^*` is the ordinary reciprocal `h^*(x) = h_0^{-1} Σ_i h_i x^{r−i}`, `r = deg h`. Proof route (polynomial identities + dimension count only): (a) `dim ⟨h^*⟩ = n − r = deg g = n − dim C`; (b) orthogonality: for `c = g u` (`deg u < r`) and `d = h^* v` (`deg v < deg g`), the dot product `Σ c_i d_i` is the coefficient of `x^{n−1}` in `c(x) · x^{n−1} d(x^{-1})`; using `g h = x^n − λ` and the degree bounds `deg c, deg d < n`, every contributing monomial cancels in pairs `(x^j, x^{n−j})` with the `λ`-twist closing the boundary terms — the identity `gh = x^n − λ` is the only input, so **repeated roots are irrelevant**: no root count, no idempotent, no separability. This lemma must be written out in full in the proof package; it is the paper’s most delicate step.
**(RR-4, twist transport.)** By A2, `D(C) = ρ(C^⊥)` coordinatewise. The coordinatewise automorphism `ρ` sends an `η`-constacyclic code with generator `e(x)` to a `ρ(η)`-constacyclic code with generator `ρ(e)(x)` (coefficients and modulus transported: `x^n − η ↦ x^n − ρ(η)`). With `η = λ^{-1}`: twist becomes `ρ(λ^{-1}) = λ^{−p^{d−k}}`, which under A4 equals `λ`. The generator is `ρ(h^*) = h#` (apply `ρ` to the coefficients of `h^*` and compare with A6). Factorwise, if `h = ∏ f^{P−a_f}` then `h# = ∏ (f#)^{P−a_f}` by T2; at the factor `f_i` (A8 indexing) the exponent contributed by `f_{i−1}` is `P − α_{i−1}`. Hence the dual generator is `h_a#` with exponents  
`β_i = P − α_{i−1}`.  
*Status: route complete; RR-3 formal write-up is the critical remaining proof obligation. Computationally supported in §7, including `GF(8), k=1` where `σ ≠ ρ` (`σ = a²`, `ρ = a⁴`), so the ρ/σ placement is genuinely tested.*

### T4 — Hull generator and dimension. *Route: complete modulo RR-5 (standard).*
**(RR-5, lcm lemma.)** In `K[x]`, `⟨g⟩ ∩ ⟨h#⟩ = ⟨lcm(g, h#)⟩`; both `g, h#` divide `M` (T3 + A4), so the same holds in the quotient by `(M)`. Since `Hull_k(C) = C ∩ D(C)` as ideals, `Hull_k(C(a)) = ⟨lcm(g_a, h_a#)⟩`, with `lcm` exponent `max(α_i, β_i) = max(α_i, P − α_{i−1})` at `f_i`. All factors in one orbit have the same degree (`#` preserves degree), so with `w_O = m_s deg_{K_s} f`:
`dim_{F_q} C(a) = Σ_s Σ_O w_O Σ_i (P − α_i)` and `dim_{F_q} Hull_k(C(a)) = Σ_s Σ_O w_O Σ_i min(P − α_i, α_{i−1})`, using `P − max(u, v) = min(P − u, P − v)`. *Status: proof-ready modulo writing RR-5 as a one-paragraph PID lemma.*

### T5 — Local transfer trace. *Route: proved here (RR-6).*
Fix one orbit `(L, w)`. Let `T = T^{(P)}_w(u, z)` with `T_{a,b} = u^{w(P−b)} z^{w·min(P−b, a)}` (row `a` = previous exponent, column `b` = current exponent, per A8). Expanding the trace of the `L`-th power as a sum over closed walks `α_0 → α_1 → … → α_{L−1} → α_0`:
`tr(T^L) = Σ_{α ∈ {0,…,P}^L} ∏_{j=1}^{L} T_{α_{j−1}, α_j}` (with `α_L := α_0`). The `j`-th factor contributes `u^{w(P−α_j)} z^{w·min(P−α_j, α_{j−1})}`; reindexing the hull sum `j ↦ i` gives exactly
`tr(T^L) = Σ_α u^{w Σ_i (P−α_i)} z^{w Σ_i min(P−α_i, α_{i−1})}`.  
For `L = 1` this reads `T_{a,a} = u^{w(P−a)} z^{w·min(P−a, a)}` — the self-loop term that drives §5. *Status: proof complete at plan level; verified computationally for 31 `(P, L)` pairs and in all vector cases (§7).*

### T6 — Global joint enumerator. *Route: complete modulo T1–T5 (RR-7).*
By A9, labeled assignments form the Cartesian product over components `s` and `τ`-orbits `O`. By T4, both `dim C(a)` and `dim Hull_k(C(a))` are sums over `(s, O)` of local contributions depending only on that orbit’s exponent tuple. The generating function therefore factors by the finite distributive law:
`E(u, z) = ∏_s ∏_O [ Σ_{α ∈ {0,…,P}^{L_O}} u^{w_O Σ (P−α_i)} z^{w_O Σ min(P−α_i, α_{i−1})} ] = ∏_s ∏_O tr( (T^{(P)}_{w_O}(u, z))^{L_O} )` by T5.  
At `P = 1` the states are `{0, 1}`, `T_{a,b} = u^{w(1−b)} z^{w·min(1−b, a)}`, and the formula reduces to the predecessor binary-state form; this internal `P=1` reduction is an algebraic identity of the displayed formulas (Gate G3 bookkeeping remains attached to the proof package). *Status: proof-ready modulo T3’s RR-3 write-up.*

**Corollaries (status here; full review in §6).** C1: `u = z = 1` gives `(P+1)^{L_O}` per orbit. C2: at `z = 1`, `T_w(u, 1)` has row-independent entries `u^{w(P−b)}`, so `tr(T^L) = (Σ_{a=0}^P u^{w a})^L`, and the product regroups factorwise. C3: per orbit, hull sum `= 0` iff all `α_i = P` or all `α_i = 0` (proof: if some `α_i < P` then the edge condition at `i` forces `α_{i−1} = 0`, and backward induction around the cycle forces every exponent to be `0`); hence `2^{#orbits}`. C4: `dim C − dim Hull = Σ w_O Σ_i max(0, P − α_i − α_{i−1})` (a sum of nonnegative terms), so `C ⊆ D(C)` iff `α_{i−1} + α_i ≥ P` on every edge, counted by `∏_O tr(B_P^{L_O})`, `(B_P)_{a,b} = 1_{a+b ≥ P}`; dually `dim Hull − dim D = Σ w_O Σ_i min(P − α_i − α_{i−1}, 0) ≤ 0` termwise, so `D(C) ⊆ C` iff `α_{i−1} + α_i ≤ P` on every edge, counted by `∏_O tr((B′_P)^{L_O})`, `(B′_P)_{a,b} = 1_{a+b ≤ P}` (see PC-4). The two counts coincide (bijection `α_i ↦ P − α_i`), as every line of the §7 orbit table confirms.

---

## 4. The mean: formal derivation of `ν_P` and the `L ≥ 2` split (Task 4)

Frozen C5 is **not** edited. The following is the exact record; the split formula is a **candidate correction (PC-1)**, computationally verified (§7), awaiting a separate approval decision.

Setup: one orbit `O`, weight `w`, exponents `α_0, …, α_{L−1}` i.i.d. uniform on `{0, …, P}` (A9; uniform labeled assignments). Hull contribution `H_O = w Σ_i min(P − α_i, α_{i−1})`.

### 4.1 The `L = 1` contribution (self-loop)

For `L = 1` the unique edge has predecessor = itself, so the statistic is `min(P − A, A)` with `A ~ Uniform{0, …, P}`. **Claim:** `E[min(P − A, A)] = ⌊P²/4⌋/(P + 1) =: ν_P`.

*Derivation.* `Σ_{a=0}^P min(P − a, a)`: the terms are symmetric under `a ↦ P − a`.
- `P = 2m`: sum `= 2 Σ_{a=0}^{m−1} a + m = m(m−1) + m = m² = P²/4`.
- `P = 2m+1`: sum `= 2 Σ_{a=0}^{m} a = m(m+1) = (P²−1)/4`.  
Both equal `⌊P²/4⌋`; dividing by the `P+1` equally likely values gives `ν_P`. Hence `E[H_O] = w·ν_P` for every `L = 1` orbit, every `P ≥ 1`. Checks: `ν_1 = 0` (indeed `min(1−A, A) ≡ 0` on `{0,1}`), `ν_2 = 1/3`, `ν_3 = 1/2`, `ν_5 = 1`, `ν_8 = 16/9`, `ν_9 = 2` — all reproduced by brute force in §7.

### 4.2 The `L ≥ 2` edge contribution

For `L ≥ 2`, each edge pairs two **distinct** independent uniforms `X, Y` (for `L = 2` the two edges are the two ordered pairs on the same two variables; each edge marginally is still a pair of distinct independent uniforms). With `Pr(min(X, Y) ≥ t) = ((P − t + 1)/(P + 1))²` for `t = 1, …, P`:
`E[min(X, Y)] = Σ_{t=1}^P ((P−t+1)/(P+1))² = (1/(P+1)²) Σ_{r=1}^P r² = P(2P + 1)/(6(P + 1)) =: μ_P`.  
By linearity of expectation (no independence between edges is needed), `E[H_O] = w·L·μ_P` for `L ≥ 2`.

**Candidate corrected hull mean (PC-1, unapproved):**  
`E[Hull] = μ_P · Σ_{L_O ≥ 2} w_O L_O + ν_P · Σ_{L_O = 1} w_O`,  
whereas frozen C5 uses `μ_P · Σ_O w_O L_O` throughout — false exactly on the `L_O = 1` part, and its frozen proof key (“two independent uniforms”) and its “`P = 1` gives `1/4`” remark are both wrong for `L = 1` (`ν_1 = 0 ≠ 1/4 = μ_1`). The code-dimension mean in frozen C5 is, by contrast, **correct**: `E[dim C] = (n/2)·Σ_s m_s`, since `E[P − a_f] = P/2` and `Σ_{f ∈ F_s} deg f = n_0`, giving `(P/2)·n_0·m_s = (n/2)·m_s` per component.

### 4.3 Remaining obligations for the general mean/variance theorem

1. **Approval:** PC-1 must be approved and applied (or rejected) by a separate dated decision; until then frozen C5 stands and must not be used.
2. **Variance (C6/RR-8) is untouched by §4.1–4.2.** Orbits are independent, so it suffices to compute, for one orbit (`w` scales the variance by `w²`): the edge second moment `E[min(X, Y)²]`; the `L = 1` second moment `(1/(P+1)) Σ_a min(P−a, a)²`; the adjacent-edge covariance for `L ≥ 3`, which reduces (with `F(s) := E[min(s, U)] = s(2P − s + 1)/(2(P + 1))`, `U` uniform) to `(1/(P+1)) Σ_{b=0}^P F(P − b) F(b) − μ_P²`; the `L = 2` opposite-edge covariance `E[min(P−A, B)·min(P−B, A)] − μ_P²`; and then closed forms in `P` for each. None of these simplifications has been carried out; C6 remains **unproved**.
3. **Conditionality:** the mean formulas presuppose T1–T4 (orbit decomposition + hull formula). Until RR-3/RR-5 are formally written, the corrected mean is a conditional consequence.
4. **Scope:** uniform **labeled** assignments, compatible twists only (A4). Nothing is claimed for equivalence classes or incompatible twists.

---

## 5–6. Review of T1–T6, C1–C7, RR-1–RR-9, and proposed corrections (Task 5)

Frozen statements were **not** changed. “Proposed corrections” (PC) are proposals for a future approval command only.

| Item | Verdict | Evidence / issue |
|---|---|---|
| T1 | **Correct; proof-ready** | PID divisor correspondence (RR-1). Needs the A9 clarification that codes are `A`-submodules with fixed labels (PC-5, wording only). |
| T2 | **Correct under A6; one missing hypothesis** | `#` is defined only when `c_0 ≠ 0`. Automatic for `f | S`, but the frozen statement quantifies over monic polynomials generally. → **PC-3:** add “with `f(0) ≠ 0`”. Multiplicativity proof is one line via coefficientwise `ρ` (§3). |
| T3 | **Correct under the A2 order; convention not frozen in the blueprint** | If `D(C)` were defined with the candidate in the first slot, `ρ` and `σ` would swap and `h_a#` would be the wrong generator. The blueprint never writes `D(C) = {y : ⟨c, y⟩ = 0 ∀c ∈ C}`. → **PC-2:** add that sentence to the freeze. RR-3 (Euclidean lemma without separability) is the main unwritten proof; RR-4 twist transport verified algebraically and computationally (twist cases `λ = −1` over `GF(3)` and `GF(9)`; `σ ≠ ρ` case `GF(8), k = 1`). |
| T4 | **Correct; proof-ready modulo RR-5** | lcm lemma in a PID + degree count (§3). Requires compatibility (A4) so that `h_a# | M`; incompatible twists are outside scope (GAP-14). |
| T5 | **Correct; proved in §3** | Closed-walk expansion with A8 orientation (row = previous, column = current). Verified for 27 `(P, L)` pairs and in every vector case. |
| T6 | **Correct modulo T1–T5** | Finite distributive law over the orbit partition. `P = 1` reduction is an identity of the displayed formulas. No counterexample found; multi-component step is algebraic (CRT), not yet vector-tested (see §7 limitations). |
| C1 | **Correct** | `tr(T^L)` at `u = z = 1` is `(P+1)^L`. |
| C2 | **Correct** | Row-independence of `T_w(u, 1)` gives `tr = (Σ_{a=0}^P u^{wa})^L`; regroups factorwise. |
| C3 | **Correct** | Backward-induction proof in §3 (replaces the frozen sketch’s edge argument, which is imprecise as written for interior exponents followed by `P`). Count `2^{#orbits}` verified in all cases. |
| C4 | **Correct; one completion proposed** | Characterizations proved via nonnegative termwise differences (§3). The frozen text does not state the dual-containing **count**; → **PC-4:** add `#{a : D(C) ⊆ C} = ∏_O tr((B′_P)^{L_O})`, `(B′_P)_{a,b} = 1_{a+b ≤ P}`. Verified computationally (counts agree with brute force everywhere, and equal the self-orthogonal counts by `α ↦ P − α`). |
| C5 | **INCORRECT (hull part); code-dimension part correct** | Frozen hull mean applies `μ_P` to `L = 1` self-loops, where the true value is `ν_P` (§4). Counterexamples, all reproduced by vector-level brute force in §7: `GF(2), n_0 = 7, P = 2`: brute mean `11/3` vs frozen `35/9`; `GF(3)`/`GF(9)`, `λ = 1, P = 3` (four `L = 1` orbits): brute `2` vs frozen `7/2`; `GF(8), k = 1, P = 2` (orbits `1 + 6`): brute `11/3` vs frozen `35/9`. In `L ≥ 2`-only cases (`GF(3)`/`GF(9)`, `λ = −1`) frozen, corrected, and brute means coincide (`7/2`), confirming the error is exactly the `L = 1` term. → **PC-1:** replace the hull-mean display and proof key by the §4.2 split formula (approval required; not applied). |
| C6 | **Unproved (programmatic)** | The frozen text states no closed form; §4.3 lists the exact moment/covariance quantities still to be simplified (RR-8). No incorrect formula is asserted, but nothing may be cited as a variance theorem yet. → **PC-6:** mark C6 explicitly as “to be proved (RR-8)” wherever it is summarized. |
| C7 | **Conditional; not a corollary of T6** | Requires a specific code with **known** distance `d` and `H ≤ min(K, n − K)`; the enumerator counts dimensions only and gives no distance and no affine/Gray distance. Status: scope note only (RR-9), correctly barred from headline claims. |
| RR-1 | Route ready | Ideal correspondence in `K[x]/(M)`; write formally. |
| RR-2 | Route ready | One-line multiplicativity (§3, T2). |
| RR-3 | **Main open proof obligation** | Euclidean-dual lemma without separability; proof route fixed (coefficient-of-`x^{n−1}` identity + dimension count), full write-up pending. Computationally supported (§7) but not proved. |
| RR-4 | Verified (algebra + computation) | Twist `λ^{−p^{d−k}} = λ` under A4; tested with `λ = −1` twists. |
| RR-5 | Route ready | `⟨g⟩ ∩ ⟨h⟩ = ⟨lcm(g, h)⟩` in a PID; one paragraph. |
| RR-6 | Done (in §3) | Closed-walk expansion. |
| RR-7 | Done (in §2) | Hypotheses A1–A10 collected in one place. |
| RR-8 | **Open** | Exact finite-sum moment quantities identified in §4.3; closed forms in `P` not yet derived. |
| RR-9 | Scope locked | No EAQECC parameter claim from the enumerator alone. |

**No other incorrect frozen statement was found.** In particular the layer-decomposition identity in blueprint §2 (`min(P − α_i, α_{i−1}) = Σ_{t=1}^P ε_{i−1}^{(t)} (1 − ε_i^{(P−t+1)})`) was re-derived and is correct, and the C5 code-dimension mean `(n/2)·Σ_s m_s` is correct (see §4.2).

---

## 7. Computational validation — executed, with exact commands (Task 6)

**Commands actually run (21 Oct 2026, exit status success):**
```
python3 code/validate_p1_03.py        # output: code/validation_p1_03_output.txt — "ALL P1-03 EXTENDED CHECKS PASSED"
python3 code/validate_repeated_root.py  # rerun — "ALL PROTOTYPE CHECKS PASSED", output identical to code/validation_output.txt
```
The old prototype file and its saved output were not modified. `code/validate_p1_03.py` is new, dependency-free, and checks two layers: (A) **vector level** — for every exponent assignment, `(dim_K C, dim_K Hull)` from a generator basis and the code-first Gram matrix `N_{t,r} = Σ_j B_{t,j} σ(B_{r,j})`, `dim Hull = dim C − rank(N)`, compared against the T4 exponent formula and the T5/T6 transfer product; (B) **orbit statistics** — direct enumeration of exponent sequences vs transfer trace, LCD/self-orthogonal/dual-containing counts, and exact rational means.

**Vector-level cases (all: brute force = exponent formula = transfer trace):**

| Case | `P` | Factors (degs) | Orbit lengths | Assignments | Mean Hull: brute / corrected / frozen |
|---|---|---|---|---|---|
| `GF(2), k=0, λ=1, n₀=7, n=14` | 2 | 1,3,3 | 1, 2 | 27 | `11/3` / `11/3` / `35/9` ✗ |
| `GF(3), k=0, λ=1, n₀=4, n=12` | 3 | 1,1,2 | 1, 1, 1 | 64 | `2` / `2` / `7/2` ✗ |
| `GF(3), k=0, λ=−1, n₀=4, n=12` | 3 | 2,2 | 2 | 16 | `7/2` / `7/2` / `7/2` |
| `GF(9), k=1, λ=1, n₀=4, n=12` | 3 | 1,1,1,1 | 1, 1, 1, 1 | 256 | `2` / `2` / `7/2` ✗ |
| `GF(9), k=1, λ=−1, n₀=4, n=12` | 3 | 1,1,1,1 | 2, 2 | 256 | `7/2` / `7/2` / `7/2` |
| `GF(8), k=1, λ=1, n₀=7, n=14` | 2 | 1×7 | **1, 6** | 2187 | `11/3` / `11/3` / `35/9` ✗ |

New coverage beyond the old prototype (`GF(4), k=1, P ∈ {2, 4}`, 206 assignments): primes `p = 2, 3`; fields `GF(2), GF(3), GF(9), GF(8)`; a nontrivial twist `λ = −1` (two fields); Euclidean (`k = 0`) and Galois (`k = 1`) pairings, including `GF(8)` where `σ ≠ ρ`; orbit length **6** at vector level; 2,806 new assignments. In every case the LCD count equals `2^{#orbits}` and the self-orthogonal / dual-containing counts equal the `tr(B^L)` / `tr((B′)^L)` predictions.

**Orbit-statistics cases:** 31 `(P, L)` pairs, `P ∈ {2, 3, 4, 5, 8, 9}`, `L ∈ {1, …, 6}` (capped at 20,000 sequences): transfer trace = direct enumeration in all pairs; `L = 1` mean `= ν_P` and `L ≥ 2` mean `= L·μ_P` exactly (rational arithmetic) in all pairs; per-orbit LCD count `= 2` in all pairs.

**Limitations (binding).** Vector-level tests are single-component (`N = 1`) and cover only `λ ∈ {1, −1}`, `ϱ = 1` (`P = p`; `ϱ = 2` remains covered only by the old `GF(4), P = 4` prototype), and the Gram-rank brute force presupposes the A2 pairing order. The multi-component product, general compatible `λ`, and `P ∈ {8, 9}` are tested only at the orbit-statistics level. Finite checks support — and in the C5 case refute — the formulas in the tested range; they are **not** a general proof.

**Computational-coverage status:** **Extended and passing** (script + output saved), with the limitations above. Remaining queue items (multi-component vector test; incompatible-twist exploration) are unchanged and were not part of this command’s executed checks.

---

## 8. Separate statuses and decision (Task 8)

- **Literature overlap:** Repo L4/L8 **partial overlap (strong)** (individual hull formula / GPM machinery; no joint enumerator found); repo L1 **unresolved / potentially critical** (L1-Q1–Q6, Q8 open; correction verified editorial in character); **novelty NOT approved**.
- **Gate G1:** **Open** — the blocker is now precisely delimited (repo L1 theorem text), and per this command the mathematical work proceeds without any novelty claim.
- **T1:** proof-ready. **T2:** proof-ready + PC-3 wording. **T3:** route complete; RR-3 write-up + PC-2 convention lock outstanding (main proof risk). **T4:** proof-ready modulo RR-5 paragraph. **T5:** proved at plan level + computationally verified. **T6:** proof-ready modulo T1–T5.
- **Mean correction (PC-1):** formally derived (§4: `ν_P` for `L = 1`, `μ_P` per edge for `L ≥ 2`), computationally verified at vector and orbit level; **not approved, not applied**; frozen C5 hull mean remains **incorrect as frozen** and must not be used. Variance (C6/RR-8): exact obligations recorded, closed forms open.
- **Computational coverage:** extended (new script, 6 vector cases, 31 orbit pairs, 2,806 + 206 assignments), all executed checks passed; limitations in §7.

**Decision: CONDITIONAL GO** — the proof programme is mathematically coherent and increasingly well tested, and exactly one frozen statement (C5’s hull mean) is known-incorrect with a verified candidate correction awaiting approval; but Gate G1 remains open on repo L1, RR-3 is unwritten, and C6 is unproved, so neither manuscript drafting nor any novelty claim is authorized.

**Exactly one recommended next command:**
> **P1-04 — Formal proof package for T1–T4 (single component):** write `P1_04_PROOFS_T1_T4.md` containing complete proofs of RR-1, RR-2, RR-3 (Euclidean-dual lemma without separability), RR-4, and RR-5, assembling T1–T4 under the A1–A10 convention lock (with the A2 dual-order sentence stated verbatim), each lemma cross-checked against the `validate_p1_03.py` cases; frozen `02_THEOREM_BLUEPRINT.md` remains unedited, and PC-1…PC-6 remain recorded as unapproved proposals.
