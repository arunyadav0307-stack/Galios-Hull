# JOINT_ENUMERATOR_FEASIBILITY — the Phase 2 gate decision

**Question put to this audit.**
> Can the joint Hermitian hull-dimension enumerator support a genuinely new theorem?

**Answer.**
> **No — not as defined.** The joint enumerator is, provably, a product of
> constituent enumerators (Proposition J), and the constituent enumerator is
> already published for the finite-field case — with explicit restrictions on `q`
> in `[D23]`, and in full generality for the Euclidean/Hermitian cyclic and
> negacyclic cases in `[SJL15]`. The object is therefore classified
> **K (known or routine)** under the blueprint's own taxonomy: its novelty is
> *identical* to that of the local enumerator, and that is not this project's
> question. The Phase 2 gate is **NOT PASSED** for this object, and per the
> blueprint's stop condition the correct deliverable is this feasibility report,
> not a manuscript.
>
> **However**, the audit identifies one direction in this neighbourhood that is
> genuinely open, and one that is a defect rather than a gap. Both are stated in §5.

**Evidence class of the answer:** the *negative* half is a **proof** (Proposition J)
plus a documented literature comparison; it does not depend on any paywalled
full text. The *positive* half (§5) is **proposed**, not proved.

---

## 1. The three independent reasons

### 1.1 The joint enumerator factorises — this is a theorem, not an opinion

With `A = ⊕_{S∈Ŝ} A_S` the CRT decomposition and `h_S(C_S) = dim_{A_S} hull_k(C_S)`:

```
H_joint(z⃗) = ∏_{S∈Ŝ} H_S(z_S),        H_total(z) = ∏_{S∈Ŝ} H_S(z).
```

*Proof* (full version in `literature/NOVELTY_ASSESSMENT.md` §2): `[S1]` Theorem 2
and Theorem 3 give a **bijection** between `λ`-constacyclic codes over `A` and
tuples `(C_S)` of `λ_S`-constacyclic codes over the component fields; `[S1]`
Theorem 7 gives `hull_k(C) = ⊕_S hull_k(C_S)`, so the statistic is **additive**.
A product bijection with an additive statistic has a multiplicative generating
function. ∎

*Independent numerical confirmation* (`verification/verify_corollary_3_5.out`,
Test 3): for `A = F_4[x]/⟨x²+x+ω⟩`, local distributions `{0:2, 1:2, 2:1}`;
convolution `{0:4, 1:8, 2:8, 3:4, 4:1}`; direct enumeration over `A`
`{0:4, 1:8, 2:8, 3:4, 4:1}`; `25 = 5 × 5` codes both ways. Exact agreement.

**Consequence.** `H_joint` has no information beyond the tuple `(H_S)`. Its
novelty is *identically* the novelty of `H_S`. Nothing about "jointness" can add
content, because the jointness is a direct product.

### 1.2 The constituent enumerator is already published

`[D23]` (Debnath–Prakash–Islam, *Cryptogr. Commun.* **15** (2023) 111–127):

> "considering some restrictions on `q`, **the number of constacyclic codes of
> length `n` over `F_q` is calculated for a given Galois hull dimension**."

and, per the same record, formulae enumerating `ℓ`-Galois self-orthogonal and
self-dual constacyclic codes. This is `H_S` for `A_S = F_q`, **up to the stated
restriction on `q`** — which is why the local enumerator is classified **K** in the
restricted range and **U** outside it (see §5, C2). The special cases `k = 0`
(Euclidean) and Hermitian, for cyclic and negacyclic codes, are `[SJL15]` without
such a restriction.

Crucially, **`[S1]` itself says so**, in its introduction (p.2):

> "In 2023, Debnath et al. [9] … They also counted the number of constacyclic
> codes of a given Galois hull dimension."

So the source paper does not merely fail to contain the local enumerator; it
*points at the paper that contains it*.

### 1.3 The same construction is already published over a product ring

`[S25]` (Shukla–Pandey–Mishra–Pathak–Upadhyay, *Adv. Math. Commun.* 2025,
DOI 10.3934/amc.2025037), *Hulls of `Z_pZ_p[v]`-cyclic codes and construction of
EAQECCs*:

> "we derive the generator polynomials of the hulls of separable cyclic codes
> (SCCs) over `Z_pZ_p[v]` and determine their dimensions **using the concept of a
> generating function in combinatorics**. We also **enumerate the SCCs over
> `Z_pZ_p[v]` with hulls of a fixed dimension**." (Thm 3.5 generating function;
> Thm 3.7 + Cor. 3.8 enumeration; Thm 4.10 non-separable case)

`Z_pZ_p[v]` with `v² = v` is a product of finite fields — structurally the same
alphabet as `A`. `[S25]` differs from a "joint enumerator over `A`" only by taking
a prime field, cyclic rather than constacyclic codes, and the Euclidean rather
than the Galois inner product. Those are **specialisations**, so a generalisation
is a routine extension, not a new theorem — and the blueprint forbids presenting
"a restatement, reparameterization, special case, or routine corollary as a new
theorem" (p.2).

---

## 2. Why the obvious counter-arguments do not work

### 2.1 "But `[S1]` explicitly says the enumeration is open"
It does (Conclusion, p.23 of the arXiv text). Its published abstract and
introduction — the parts readable without a subscription — announce no enumeration
theorem, so the statement is not contradicted by the version of record, but the
published conclusion itself was **not** inspected.
It says the **isometry-class** enumeration is open — *"the enumeration of
non-isometric constacyclic codes for a given Galois hull dimension is an
interesting problem. This problem is still open over `A`."* That is a different question
(§5, C1). And the sentence immediately after — *"it may be interesting to count the
number of constacyclic codes for a given Galois hull dimension over `A`"* — is
answered by Proposition J plus `[D23]`. An author naming a problem does not make
the problem hard; here it makes it *easy*, because the authors had already proved
the additivity theorem needed to solve it.

### 2.2 "But nobody wrote down the formula for `A`"
Correct, and irrelevant. The formula is a three-line corollary. The blueprint's own
rules (p.2, p.4; Phase 5 "Required proof standard") exclude routine corollaries.

### 2.3 "But the Hermitian case is special"
Not in a way that helps. In the Yadav-style ring
`R_e = F_{q²}[u]/⟨u^e−1⟩`, `e | (q+1)`, one has `e | q²−1`, so `u^e−1` **splits**
over `F_{q²}`; every component is `F_{q²}` and `N = e`. This is the cleanest
possible case of Proposition J: `H_joint = ∏_{l=1}^{e} H_l(z_l)`, with each `H_l`
a Hermitian constacyclic hull enumerator over `F_{q²}` — i.e. `[D23]`/`[SJL15]`
territory. The splitting hypothesis that makes the blueprint's setting *well
defined* is exactly the hypothesis that makes the product formula *transparent*.

### 2.4 "But the Gray map / quantum codes make it new"
No: `[S1]` Lemma 9 proves `ψ(hull_k(C)) = hull_k(ψ(C))`. The Gray map preserves the
`k`-Galois inner product up to a nonzero scalar `γ` — from `M M^{(p^k)T} = γI` one
gets `⟨ψ(a),ψ(b)⟩_k = γ⟨a,b⟩_k`, which is an isometry exactly when `γ = 1`, as in
both worked examples (checked: `γ = 1` for the printed `M` in Example 2 and
Example 3). Because `γ ≠ 0`, orthogonality and therefore the hull dimension are
preserved in general, so the Gray map **cannot change the hull-dimension
distribution**. We verified this numerically (hull of `ψ(C)` is `0` and `2` in
Examples 2 and 3, matching the ring-level values). Any "enumerator of Gray images"
is the same enumerator. And an enumerator, by construction, carries no distance information, so
it cannot produce quantum parameters beyond what Theorem 10 already gives.

### 2.5 "But the components might not be independent"
They are, and this is the content of `[S1]` Theorems 2 and 3. This is the one place
where a reader might reasonably expect a subtlety, and there is none: the CRT
decomposition is a ring isomorphism, so the code families are literally a Cartesian
product.

---

## 3. What is genuinely *established* here (so it is not lost)

This audit did produce results; they are just not the ones the blueprint hoped for.

| # | Result | Class | Where |
|---|---|---|---|
| E-1 | Proposition J (joint enumerator factorises, with the `d_S` correction) | `[PROVED]` | §1.1, `literature/NOVELTY_ASSESSMENT.md` §2 |
| E-2 | Complete theorem register of `[S1]`: 10 theorems, 9 lemmas, 5 corollaries; **zero** enumeration results | `[VERIFIED]` | `SOURCE_THEOREM_REGISTER.md` |
| E-3 | All three worked examples of `[S1]` recomputed from scratch, including exact minimum distances by parity-check column dependence | `[VERIFIED]` | `SOURCE_EXAMPLE_RECALCULATION.md` |
| E-4 | Corollary 3.5(1) and (2) confirmed by brute force in admissible regimes | `[VERIFIED]` | `verification/verify_corollary_3_5.out` |
| E-5 | Corollary 3.5(2) is **false as printed** when `e' = 0` (`n` odd) | **defect** | audit F3 |
| E-6 | Lemma 5's proof is invalid (statement true, two-line repair) | **defect** | audit F4 |
| E-7 | Theorem 8's range bound is asserted without proof (true; short proof supplied) | **defect** | audit F5 |
| E-8 | `[S1]` §2.3 treats component fields as `F_q`; this holds only when every `t_i` splits, which its own examples violate | **defect (F11)** | audit F11 |
| E-9 | The inner-product slot convention is asymmetric; 385 codes checked, no dimension difference found, but no proof | `[VERIFIED-EMPIRICAL]` | audit F6 |
| E-10 | Literature map with 19 matrix entries and 31 verified references, closest precedents identified and read | `[ESTABLISHED]`, **extended 2026-10-20** with the mass-formula and isometry-class strata | `literature/` |

E-5, E-6, E-7, E-8 are **new observations about a published paper**. They are
contributions to the record. They are not, individually or together, a research
programme.

---

## 4. A note on the *kind* of object the joint enumerator is

It is worth naming precisely why the blueprint's instinct fails, because the same
trap recurs.

The blueprint treats the joint enumerator as a *new invariant*. It is not: it is
the **image of a product** under a linearisation. Whenever

- the alphabet decomposes as a finite product of fields (CRT), and
- the code family is defined by an ideal condition that is componentwise, and
- the statistic is additive over components,

the enumeration is a product, and the whole difficulty retreats into one component.
All three conditions hold here, and all three are theorems in `[S1]`
(Thm 2/3, Thm 3/6/Cor 3.1, Thm 7).

To get a non-product enumeration one must break one of the three. The only
available break is the **third**: count objects for which the hull dimension is
*not* determined componentwise — i.e. count **up to an equivalence that mixes the
components**. That is precisely the open problem `[S1]` names.

---

## 5. What survives, ranked

### C1 — Enumeration up to isometry (open only at the intersection — see the revision note below)

> **Revision, 2026-10-20.** Independent verification (`INDEPENDENT_VERIFICATION_REPORT.md`
> §4.4) found two well-developed lines that the original text of this section missed:
> class counts of constacyclic codes up to `n`-isometry (`[CFLL12]`, `[ISO24]`), and
> closed mass formulas for linear codes with a prescribed hull dimension (`[LSL25]`,
> `[LS24]`, `[LSL24]`). The statement "no result found in the literature" is therefore
> **too strong**. What remains open is only the *intersection* of the two, and it may
> be trivial or intractable — see `RESEARCH_DIRECTION_DECISION.md` §C1.

**Status: `[OPEN]` at the intersection only; declared open by `[S1]` p.23.**
**Why it is non-product:** the isometry group of `A^n` includes the Galois action
on `Ŝ` (permuting idempotents) together with the constacyclic shift acting
simultaneously on all components. Two tuples `(C_S)` and `(C'_S)` that differ only
by a permutation of the components induced by Frobenius are *the same code up to
isometry*, so orbit counting genuinely couples the components. Burnside is the
natural tool.
**Why it is hard, and where the risk is:** "isometry" must be defined first
(monomial? semilinear? `A`-linear?) and the answer changes with the definition.
There is a real risk of a definitional paper with no theorem.
**Feasibility:** a *mass formula* for one explicit small ring (e.g.
`A = F_q × F_q`, `ℓ = 1`, `t(u) = u² − 1`) and fixed `(n, λ, k)` is realistic and
would be a genuine theorem. A general formula is not realistic in one paper.

### C2 — The exact local enumerator over `F_q` without `[D23]`'s restriction on `q`
**Status: `[U]`.** `[D23]`'s abstract says "considering some restrictions on `q`";
the full text was not available, so whether the restriction is essential is unknown.
**Value:** if essential, removing it is a real finite-field theorem. **Risk:** it is
`[D23]`'s own problem, and it is a finite-field problem — the ring `A` plays no role.
**Note:** this is *not* the joint enumerator, and pursuing it would be a different
paper.

### C3 — Correcting `[S1]`'s component-field bookkeeping (audit F11)
**Status: `[PROVED DEFECT]`, repair not yet written.**
`[S1]` §2.3 assumes component fields are `F_q`; its own Examples 2–3 have
`t_1` irreducible of degree 2, so the components are `F_{q²}` and `dim_q A = 4`
while `N = 2`. Consequences: the Gray map is not injective, Theorem 8 computes
`Σ_S dim_{A_S}` rather than `dim_q`, and the claimed `[14,10,4]_9`, `[26,22,4]_25`
cannot be images of the stated modules.
**Value:** a corrected theorem (with the factor `d_S = |S(ν)|`) plus corrected
parameters is a legitimate contribution — an erratum with content.
**Risk:** it is an erratum, it requires the journal version to be checked first
(not possible here), and it does not build a programme.

### C4 — Distance-aware enumeration
**Status: `[OPEN]` but likely infeasible in closed form.** No paper found counts
codes by `(hull dimension, minimum distance)`. Exact results exist only for tiny
instances. `[S1]` Remark 1 concedes the Gray map with `M = I_N` cannot improve
distance, so the natural construction gives nothing.
**Verdict:** not a theorem-sized target on current evidence.

### C5 — The rejected candidates, for the record
| Candidate | Why rejected |
|---|---|
| joint enumerator | Proposition J; `[D23]`, `[S25]` — **K** |
| total enumerator | same — **K** |
| bivariate `(dim, hull)` | product structure; `[LYL26]` uses a two-variable product enumerator — **K** |
| dual-containing restricted enumerator | `[S1]` Thm 6 makes it componentwise — **K** |
| Gray-image enumerator | `[S1]` Lemma 9: the statistic is invariant — **F** as novelty |
| average hull over `A` | `[DP25]` for `R_{m,q}` — **K** |
| "quantum codes from the enumerator" | enumerator carries no distance — **F** |

---

## 6. Recommendation

1. **Do not write the manuscript the blueprint describes.** The central object is
   routine; a paper built on it would be a re-derivation with a generalisation
   claim, and the blueprint's own referee standard ("Do not present a
   restatement, reparameterization, special case, or routine corollary as a new
   theorem") would reject it.
2. **If the project continues, retarget to C1** (isometry classes, one ring, mass
   formula). It is the only direction in this neighbourhood with a defensible
   novelty claim, and it is the direction the source paper itself names.
3. **Publish the audit findings separately if desired.** F3, F4, F5, F11 are
   concrete, checkable statements about a published paper (E-5…E-8). A short
   corrigendum-style note on F11 in particular has clear value: the component-field
   bookkeeping affects every quantum parameter in the paper.
4. **Before any resubmission or extension**, obtain the version of record
   (*Discrete Math.* **349**(2) (2026) 114750) and check whether F3/F4/F5/F11 are
   already addressed there. This audit could read only arXiv v1.

---

## 7. What this document does *not* claim

- It does **not** claim `[S1]` is wrong in its main line. On the contrary:
  Theorems 2, 3, 5, 6, 7 and 10 and Lemma 9 survive, and both worked examples
  reproduce exactly.
- It does **not** claim the author of the blueprint was careless. The gap is real
  and the authors of `[S1]` name it; it is simply already bridged.
- It does **not** claim that no new theorem exists anywhere in this area — only
  that the **joint enumerator** cannot support one, and it names what can.
- It does **not** claim priority for any of the audit's own observations. They are
  presented as corrections, not as discoveries of new mathematics.

---

## 8. Gate status

| Gate | Requirement | Status |
|---|---|---|
| Gate 0 | exact source PDF and usable environment identified | **PASS** (with bibliographic mismatch recorded) |
| Gate 1 | central source results and hypotheses understood and documented | **PASS** |
| Gate 2 | proposed main contribution distinguishable from the closest known results | **FAIL for the joint enumerator** — it is a product of known results |
| Phase 5 precondition | at least one substantive proved theorem, defensible novelty, independent small-case verification | **1 of 3 met** (verification yes; novelty no; substantive new theorem no) |
| Manuscript phase | — | **BLOCKED by the above** |
