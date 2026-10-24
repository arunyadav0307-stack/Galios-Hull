# Phase 3 / P3-5 — Literature checkpoint: attacking B-1 and B-2

**Purpose.** Every remaining claim about the Phase 3 contribution depends on two blockers. This
document records the attack on both, the closest prior art found, a citation error discovered in my
own earlier record and corrected, and the effect (and non-effect) on the novelty verdict.

Probe: `phase3/p3_gray_hull_identity.py`, log `p3_gray_hull_identity_log.txt`. Branch
`arena/831a2e65-galios-hull`, from `b3884ab`.

---

## 1. A citation error in my own record — found and corrected

While resolving B-2 I checked the DOI `10.1007/s12095-022-00591-6` directly. It does **not** belong
to the paper my earlier table said it did.

| | Earlier record (`R1_FEASIBILITY.md`, removed now) | Verified |
|---|---|---|
| Citation | "Debnath & Prakash, *SIST* **325**:309–319, DOI `10.1007/s12095-022-00591-6`" | DOI `10.1007/s12095-022-00591-6` = **Debnath, Prakash & Islam**, *Galois hulls of constacyclic codes over finite fields*, *Cryptogr. Commun.* **15**:111–127 (2023) |
| Authors | two | **three** (Debnath, Prakash, Islam) |
| Ring | described as "affine algebra rings" | **finite field** `F_q` |
| The `SIST` 325:309–319 entry | merged into the row above | a **separate** paper: *Hulls of Cyclic Codes Over a Local Ring*, ICTIS 2025, DOI `10.1007/978-981-95-1365-9_25`, over the **chain** ring `Z_{p³}` |

Two distinct papers had been collapsed into one row. **Corrected in `R1_FEASIBILITY.md` by new
commit, with the correction note left in place.** `LITERATURE_COMPARISON_MATRIX.csv` rows 10 and 12
already had both entries correctly and separately, so the error was confined to that one summary
table and no verdict depended on it. Recorded rather than silently fixed.

## 2. B-2 — still open, but now precisely stated

B-2 was "Debnath–Prakash body text unobtainable". With the papers separated, the blocker is:

> **B-2a.** Debnath, Prakash & Islam, *Cryptogr. Commun.* **15**:111–127 (2023). Their abstract states
> that, *"considering some restrictions on `q`, the number of constacyclic codes of length `n` over
> `F_q` is calculated for a given Galois hull dimension."* This is a **field-level count by hull
> dimension** — prior art for the *hull marginal* of my P3-1 tables. What is unverified: the
> "restrictions on `q`", whether the count is per-dimension, and whether `p \| n` is covered.
>
> **B-2b.** Debnath & Prakash, ICTIS 2025, *SIST* **325**:309–319. A count of cyclic codes over the
> **chain** ring `Z_{p³}` for a fixed `p`-dimension of the hull. Body unread.

Neither affects the Phase 3 object, which is the **joint** (hull, distance) law and its ring-level
distribution. A count by hull dimension alone — however it is restricted — cannot reproduce a joint
law. Both stay open, and per Phase 2 rules **no absence claim** is made.

## 3. B-1 — advanced for the arXiv-available works

Full text was obtainable for one of the two closest works, so that one is upgraded from abstract to
full-text and its claim checked.

| Work | Access | What it does | Does it count? |
|---|---|---|---|
| **Qian, Wang & Wang**, arXiv:2606.22069, *Hulls and sums of separable constacyclic codes over `F_q × (F_q + vF_q)`* | **full text read** (abstract, §1, structure) | generator polynomials of Euclidean/Hermitian **duals, hulls and sums** of separable constacyclic codes over the product ring `S = F_q × (F_q+vF_q)` **and of their Gray images**; two methods producing QECCs | **No.** It derives generators and constructs tables of codes. No enumeration, no distribution |
| **Tian, Gao & Gao**, *Quantum Inf. Process.* **23**(1):9 (2024), *Hulls of constacyclic codes over finite non-chain rings …* | abstract | Euclidean and Hermitian hulls over `F_q + vF_q` (`v² = v`); **"under a special Gray map … dimensions of hulls of Gray images of constacyclic codes are obtained"**; QECCs via construction X | **No** (abstract level) — dimensions, then codes |
| **Zhang, Kong & Zheng**, *Entropy* **28**:407 (2026) | abstract | `ℓ`-Galois hulls of constacyclic codes over a non-chain ring, construction X, new QMDS/QECC | **No** |
| Debnath, Prakash & Islam (2023) | abstract | field-level count by Galois hull dimension | **Yes — but over a field, hull only** |

**Qian–Wang–Wang is the closest work in shape**: a product ring with a Gray map, hulls, and hulls of
Gray images. It is full-text and it does not count. That is the single strongest piece of evidence
that the distribution I computed is not already in the literature — and it is still only one paper.

## 4. New verified fact: the Gray-image hull is not a new invariant

Tian–Gao–Gao's headline object is "dimensions of hulls of **Gray images**". That invites the question
whether my Theorem 1 (hull additivity over CRT components) covers it, or whether they have something
extra. It does not need anything extra:

**Proposition.** `dim Hull_H(ψ(C)) = dim Hull_H(C) = Σ_ℓ dim Hull_H(C_ℓ)`.

*Proof.* The source paper's Lemma 3 gives `ψ(C^{⊥_H}) = ψ(C)^{⊥_H}`, and `ψ` is bijective linear, so
`ψ` restricts to a bijection `Hull_H(C) → Hull_H(ψ(C))`; dimensions are equal. The second equality is
Theorem 1 of `P3_3_RING_GRAY.md`. ∎

**Checked**, `F_9`, `e = 2`, `n = 2`, all **256** ordered pairs, by two independent routes: the
Hermitian hull dimension of `ψ(C)` computed directly in `F_9⁴` (field machinery, no reference to the
ring), versus the sum of constituent hull dimensions. **256/256 agree.**

Consequence for the novelty discussion: Tian–Gao–Gao's Gray-image hull dimension is the *same number*
as the ring-level hull dimension, hence already covered by the source's Theorem 10 and by their own
statement. Their contribution is the construction of codes, not a new invariant — so it does not
pre-empt, and is not pre-empted by, the distribution.

**Bug found in this check, recorded.** The first version of the script built the Gray image from
`{a ∈ basis(C_1)} × {b ∈ basis(C_2)}`, which does **not** span the product code `C_1 × C_2`; the
correct spanning set is `{(a,0)} ∪ {(0,b)}`. The buggy version reported **112 spurious mismatches**
out of 256. The corrected version reports 256/256. Kept in the audit trail because a plausible
"the identity fails" conclusion was one line away from being written down.

## 5. Effect on the verdict

| Claim | Before this checkpoint | Now |
|---|---|---|
| Closest ring-level work does not count/distribute | abstract-level guess | **verified in full text** for arXiv:2606.22069 |
| Tian–Gao–Gao's Gray-image hull is separate prior art | assumed distinct | **shown to be the same invariant** as the hull dimension (Prop. §4), 256/256 |
| Field-level hull counting is prior art | known | confirmed, and now correctly cited (three authors, *Cryptogr. Commun.*, finite fields) |
| Novelty of the Phase 3 distribution | not claimed | **still not claimed** |

**Verdict unchanged: GO on the narrowed distributional contribution; NO-GO on a structural-theorem
headline.** The literature position is now *stronger* — one of the two closest works is verified in
full text to contain no counting, and the other's headline object is the same invariant as one already
in the source paper — but **absence is still not established**, because:

* **B-2a/B-2b** bodies remain unread;
* Tian–Gao–Gao's full text was not obtainable (abstract only);
* the publisher paywall (B-1) still covers ScienceDirect, Springer and AIMS.

## 6. What would eliminate the contribution

Unchanged and now sharper:

1. a published joint (hull dimension, minimum distance) distribution for a constacyclic family, over
   any field or ring — kills the object;
2. a statement of Theorem 2's bounds for `R_e` — kills the bounds as a result (not the distribution);
3. any full text among B-2a, B-2b, Tian–Gao–Gao containing such a distribution or the bounds.

**Next action:** these three are library-access tasks, not computation tasks. Nothing in the Phase 3
programme should be re-derived before they are answered; and if a full-text check does contain a joint
distribution, the honest response is to withdraw the claim, not to narrow it post hoc.
