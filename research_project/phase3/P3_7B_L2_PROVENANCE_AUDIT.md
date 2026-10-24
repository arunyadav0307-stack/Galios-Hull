# P3-7b — Provenance audit: L-2 is a **known theorem**, not an open conjecture

Date: 2026-10-24. Supersedes the *status* of `P3_7_POWER_ATTAINMENT.md` (the mathematics in that file
stands; its framing of L-2 as a partly-open conjecture does not).

Commands (both logged, both exit 0):
* `python3 phase3/p3_known_formula_check.py` → `phase3/p3_known_formula_check_log.txt` (32 lines;
  **5050 values, 0 mismatches**)
* `python3 phase3/p3_weight2_field.py` → `phase3/p3_weight2_field_log.txt` (39 lines; 90 weight-2
  values, 0 disagreements; F_3 vs F_9 distance agreement 9/9)

---

## 1. What was believed, and what is true

`P3_7_POWER_ATTAINMENT.md` treated

    d(C_a) = m(a) = min { w((x-1)^j) : a <= j <= n-1 },     C_a = <(x-1)^a> <= F_q[x]/(x^n - 1), n = p^s

as a **conjecture** (limitation L-2), proved there only for `s = 1` and `1 <= a <= p^{s-1}`, and
verified for 117 values at `n <= 27`.

That is **not** the situation. The exact minimum distance of these codes has been known since at least
2008, and the `s = 1` case since 1973.

**Published statement** (quoted verbatim; H. Q. Dinh, *On the linear ordering of some classes of
negacyclic and cyclic codes and their distance distributions*, **Finite Fields Appl. 14(1):22–40,
2008**, as restated as Lemma 1 of arXiv:2304.00762, which cites `[20] = Dinh 2008` and
`[41] = Massey–Costello–Justesen, IEEE TIT 19(1):101–110, 1973`):

> For `i = 1, 2, ..., p^s − 1`, the cyclic code `C_{i,s} = ⟨(x−1)^i⟩ ⊆ F_q[x]/⟨x^{p^s} − 1⟩` has the
> minimum distance `d_i = (τ + 1) p^t`, where `τ` and `t` are the unique integers satisfying
> `1 <= τ <= p−1`, `0 <= t <= s−1`, and
>
>     p^s − p^{s−t} + (τ−1) p^{s−t−1} < i <= p^s − p^{s−t} + τ p^{s−t−1}.

The same formula is restated as Theorem 2.4 of arXiv:1704.03311 (attributing it to `[6]`), and as
Lemma 1 of the combinatorialpress 2024 note on `F_{p^m}[u]/⟨u^3⟩`. It is used as a standard
building block in the symbol-pair / `b`-symbol literature (e.g. arXiv:1704.03311, arXiv:1911.07542
Theorem 3.13, arXiv:2206.10806).

**Verdict: L-2 is CLOSED — by citation, not by proof.** It was never an open problem. The P3-7
conjecture is a *correct re-derivation* of a known theorem, and Theorems A and B there are its first
two branches.

---

## 2. Verification that the published formula and `m(a)` coincide

`phase3/p3_known_formula_check.py` compares, for every `a` in `[0, p^s]`:

* `m(a)` from the Weight Lemma (`w((x−1)^j) = ∏(d_i+1)`), and
* `published_d(a, p, s)` — Dinh's formula as displayed above.

| `p` | `s` | `n` | values | mismatches |
|---|---|---|---|---|
| 2 | 1–8 | 2 … 256 | 518 | 0 |
| 3 | 1–4 | 3 … 81 | 124 | 0 |
| 5 | 1–3 | 5 … 125 | 158 | 0 |
| 7 | 1–3 | 7 … 343 | 402 | 0 |
| 11 | 1–3 | 11 … 1331 | 1466 | 0 |
| 13 | 1–3 | 13 … 2197 | 2382 | 0 |
| **total** | | | **5050** | **0** |

(Each per-`(p,s)` count is exactly `n + 1`, one for each `a`; the totals per `p` are the sums
over `s`: 518 + 124 + 158 + 402 + 1466 + 2382 = 5050.)

**Independent anchor against a published table.** arXiv:2304.00762, Example 1 states: for `n = 25`
over `F_5`, the distances of `⟨(x−1)^i⟩` are `2` for `i = 1..5`, `3` for `6..10`, `4` for `11..15`,
`5` for `16..20`, and `10, 15, 20, 25` for `i = 21, 22, 23, 24`. My `m(a)` produces exactly the band
structure `[(2,5), (3,5), (4,5), (5,5), (10,1), (15,1), (20,1), (25,1)]` — identical, including the
counts. This is a match against a *published* table reached by a completely different route (my
`n = 25` numbers in P3-7 §7.3 were computed by matroid girth / codeword enumeration, not by the
formula), so it validates the P3-7 machinery as well as the identification.

---

## 3. Consequences for the P3-7 claims — reclassification

| P3-7 item | Status now |
|---|---|
| Weight Lemma `w((x−1)^j) = ∏(d_i+1)` | **correct, elementary, and almost certainly classical**; no novelty claimed |
| Lemma H (`C_a = ker H_a`, binomial/Hasse, *not* falling factorials) | correct; the falling-factorial error remains a genuine recorded error |
| Lemma C (distance = matroid girth) | correct and useful as a computational tool; no novelty claimed |
| **Theorem A** (`s = 1`: `d = a + 1`, MDS) | **classical** — this is `τ = i`, `t = 0` in Dinh's formula; the `g = (x−1)^{p−2}` MDS case is stated explicitly in the literature (e.g. *Electronics Letters* 2016, repeated-single-root codes). **Re-derived, not new.** |
| **Theorem B** (`1 <= a <= p^{s−1}` ⇒ `d = 2`) | **classical** — the `τ = 1, t = 0` branch. **Re-derived, not new.** |
| **Theorem C** (`p^{s−1} < a <= 2p^{s−1}` ⇒ `d = 3`) | **classical** — the `τ = 2, t = 0` branch. Verified 3/3 bands (`n = 9, 25, 27`), but **not new**. |
| "Open range" `p^{s−1} < a < p^s` | **not open** — fully covered by `t >= 1` in the published formula. My block/`ε`-decomposition "obstruction" was a route to a theorem that already exists; recorded as wasted effort, not as an open problem. |
| "`n = 49, 81, 125` not computed — out of reach" | **moot**: the published formula gives all of them. `n = 343, 1331, 2197` are now settled by citation and checked against `m(a)`. |
| L-2 as a limitation of the project | **removed from the limitation list** (closed by citation). It is not a limitation and not a contribution. |

The `n = 9` table `[1,2,2,2,3,3,3,6,9]` and every other P3-2/P3-7 figure are consistent with the
published formula; nothing computed earlier has to be withdrawn.

---

## 4. Two small things that survive as genuinely mine (but are not contributions)

Neither is claimed as new; both are recorded only because they are correct and were verified here.

1. **Field independence (proved, trivial).** `H_a[i][j] = C(j,i) mod p` lies in `F_p`, and rank over
   an extension field equals rank over `F_p` (rank = largest non-vanishing minor). Hence `d(C_a)` is
   the same over every `F_q` of characteristic `p`. Checked concretely over `F_9` vs `F_3` at `n = 9`
   (`p3_weight2_field.py` §A: 9/9 agree, cap-limited at 4 for the two large distances, which agree as
   "`> 4`" in both fields). The published formula is field-independent by construction, so this is
   consistent rather than new.
2. **Weight-2 classification (proved, and exactly the `τ = 1` branch).** A word of weight `<= 2`
   exists in `C_a` iff `a = 0` (weight 1) or `1 <= a <= p^{s−1}` (weight 2); verified exhaustively at
   90 values over 10 `(p,s)` pairs, 0 disagreements. This is a restatement of the first published
   branch, obtained by a different argument (column periodicity of `H_a`).

---

## 5. Effect on the project's standing decisions

* **Phase 9 remains NO-GO, and is now reinforced.** The one route that looked like it might reach the
  blueprint's "at least one substantive proved theorem" bar — decide L-2 — turns out to lead to a
  2008 theorem. There is now *nothing* in the project's proved inventory that is not either (a) an
  elementary re-derivation, (b) a two-line support count, or (c) a known theorem. The honest
  conclusion is unchanged and better supported.
* **No novelty is claimed anywhere.** The prior-art matrix gains one row (§6) recording that exact
  distances for `⟨(x−1)^i⟩` of length `p^s` are settled in the literature, so that no future reader of
  this repository mistakes the P3-7 tables for a contribution.
* **Withdrawal rule untouched.** This finding is about the *distance side* of the single-orbit family.
  It does not bear on R4 (the joint hull/distance distribution), and it does not change the standing
  rule that R4 is **withdrawn, not narrowed**, if B-1/B-2a/B-2b or Tian–Gao–Gao contains a joint
  distribution.
* **Methodological lesson, recorded.** The blueprint's Phase 2 rule — read complete theorem statements,
  not abstracts — applies with full force here. The formula sits in a 2008 *Finite Fields Appl.* paper
  about *negacyclic* codes whose title does not mention cyclic length `p^s` distances, and it is
  restated in a 2025 arXiv paper about *weight distributions*. It was found only by searching for the
  specific object (`⟨(x−1)^i⟩`, length `p^s`), not for the project's topic (hulls). A gap in the
  project's literature pass, now closed.

---

## 6. Prior-art row added

Appended to `phase2/LITERATURE_COMPARISON_MATRIX.csv`:

| Paper | Ring or field | Code family | Hull type | Main theorem | Exact enumeration? | Quantum construction? | Difference from proposed work |
|---|---|---|---|---|---|---|---|
| Dinh, *On the linear ordering of some classes of negacyclic and cyclic codes and their distance distributions*, Finite Fields Appl. 14(1):22–40 (2008); formula restated as Lemma 1 of arXiv:2304.00762 and Thm 2.4 of arXiv:1704.03311 | `F_q[x]/⟨x^{p^s}−1⟩`, char `p` | `⟨(x−1)^i⟩`, `0 <= i <= p^s` | none (no hull) | **Exact** minimum distance `d_i = (τ+1)p^t` for all `i` | yes — exact distance for every `i`, all `p`, all `s` | no | **Settles the whole distance side of the single-orbit repeated-root family.** The P3-7 "conjecture" is this theorem; the P3-7 tables are reproductions. No hull content, so R4 is unaffected |

---

## 7. Status bookkeeping

* `phase3/P3_7_POWER_ATTAINMENT.md` — uncorrected mathematics kept intact (audit trail); a
  **STATUS REVISED** banner at the top points here and restates the reclassification of §3 above.
* `phase3/P3_7B_L2_PROVENANCE_AUDIT.md` — this file.
* `PHASE_STATUS.md` — L-2 marked **CLOSED (known theorem)** and removed from the open-limitation list;
  P3-7b section added.
* Scripts/logs added: `p3_known_formula_check.py` + `_log.txt` (5050 values),
  `p3_weight2_field.py` + `_log.txt` (field independence + weight-2 classification).
