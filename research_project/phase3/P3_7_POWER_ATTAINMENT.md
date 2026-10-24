# P3-7 — Power attainment for single-orbit repeated-root codes (limitation L-2)

> ## STATUS REVISED (2026-10-24) — L-2 is a KNOWN THEOREM, not an open conjecture
>
> The mathematics below is retained unchanged as an audit trail, but its **framing is wrong**. The
> exact minimum distance of `C_i = ⟨(x−1)^i⟩ ⊆ F_q[x]/⟨x^{p^s}−1⟩` is known for every `i`: see
> H. Q. Dinh, *Finite Fields Appl.* **14**(1):22–40 (2008) — `d_i = (τ+1)p^t` on the band
> `p^s − p^{s−t} + (τ−1)p^{s−t−1} < i <= p^s − p^{s−t} + τ p^{s−t−1}` — restated as Lemma 1 of
> arXiv:2304.00762 and as Thm 2.4 of arXiv:1704.03311. The `s = 1` (MDS) case goes back to
> Massey–Costello–Justesen, *IEEE TIT* **19**(1):101–110 (1973).
>
> Consequences (detailed in `P3_7B_L2_PROVENANCE_AUDIT.md`):
> * **L-2 is closed by citation.** It is **not** a limitation and **not** a contribution.
> * **Theorem A** (`s = 1`) and **Theorem B** (`1 <= a <= p^{s−1}`) below are the `t = 0`, `τ = i` and
>   `t = 0`, `τ = 1` branches of that theorem. **Re-derived, not new.**
> * The "open range" of §6 is **not open** — it is the `t >= 1` branch. The block/`ε`-decomposition
>   obstruction recorded there is a route to a theorem that already exists.
> * `m(a)` was checked against the published formula at **5050 values, 0 mismatches**
>   (`p3_known_formula_check.py`), and the `n = 25` table below matches the published Example 1 of
>   arXiv:2304.00762 band-for-band, including counts.
> * The Weight Lemma, Lemmas H and C, and the two recorded bugs stand as correct work and as a
>   reproducible verification of a known result. **No novelty is claimed for any of it.**
>
> Phase 9 remains **NO-GO**, and this finding reinforces it.


Date: 2026-10-24. Probe: `phase3/p3_power_attainment.py`. Log: `phase3/p3_power_attainment_log.txt`
(212 lines, exit 0, wall time 759 s). Pure stdlib, no numpy, no network.

Status of this document (as originally written): *two proved families + one conjecture.* **Revised:
the conjecture is a known theorem — see the banner above and `P3_7B_L2_PROVENANCE_AUDIT.md`. Nothing
here is new; no novelty is claimed.**

---

## 0. Setting and the statement under test

Fix a prime `p`, put `n = p^s`, and let `R = F_q[x]/(x^n − 1)` with `q = p^m` (only `char = p` is used,
so `F_p` suffices for every computation below). Because `char R = p` and `n = p^s`,

    x^n − 1 = x^{p^s} − 1 = (x − 1)^{p^s} = (x − 1)^n .

So `R = F_q[y]/(y^n)` with `y = x − 1`, and for `0 ≤ a ≤ n` the single-orbit repeated-root code

    C_a = ⟨(x − 1)^a⟩ = y^a R = { f ∈ F_q[x] : deg f < n, (x − 1)^a | f }

is an ideal of `R`. `C_0 = R` (`d = 1`), `C_n = 0` (`d` undefined). Let

    w(f) = #{ j : f_j ≠ 0 }        (Hamming weight in the x-basis),     m(a) = min_{a ≤ j ≤ n−1} w((x−1)^j).

**Conjecture (L-2).** For every prime `p`, every `s ≥ 1` and every `0 ≤ a ≤ n − 1`,

    d(C_a) = m(a).

L-2 was recorded in `P3_2_TWO_ORBIT.md` as a conjecture from the complete `n = 9` table (10/10). It is
the shortest remaining route to a *proved* distance statement for a family in this project, because
`w((x−1)^j)` has a closed form (§1) while `d(C_a)` is otherwise only computable.

**Observation 0.1 (one half is free).** `d(C_a) ≤ m(a)` always: if `j*` minimises, then
`(x − 1)^{j*} = (x−1)^a (x−1)^{j*−a} ∈ C_a` is a nonzero word of weight `m(a)`. Hence

    L-2  ⟺  d(C_a) ≥ m(a)  for all a,

i.e. the whole content of L-2 is a **lower** bound. By Singleton, `d(C_a) ≤ n − dim C_a + 1 = a + 1`, so
L-2 is only consistent if `m(a) ≤ a + 1`; that is checked for every `a` in 16 cases
(`p = 2, s ≤ 5`; `p = 3, s ≤ 4`; `p = 5, s ≤ 3`; `p = 7, s ≤ 2`; `p = 11, 13`) by
`python3 phase3/p3_power_attainment.py --mbound` → `phase3/p3_power_attainment_mbound_log.txt`
(19 lines, exit 0; it weighs powers only and builds no code, so `n = 125` is trivial there).

---

## 1. Lemma W (weight of a power). Proved.

**Lemma W.** Write the base-`p` expansion `j = Σ_{i≥0} d_i p^i` with `0 ≤ j ≤ n − 1` (`n = p^s`). Then

    w((x − 1)^j) = Π_{i=0}^{s−1} (d_i + 1).

*Proof.* In characteristic `p`, `(x − 1)^{p^i} = x^{p^i} − 1`. Hence, with `j = Σ d_i p^i` and `d_i < p`,

    (x − 1)^j = Π_i ((x − 1)^{p^i})^{d_i} = Π_i (x^{p^i} − 1)^{d_i}.

The factor `(x^{p^i} − 1)^{d_i} = Σ_{t=0}^{d_i} C(d_i,t) (−1)^{d_i−t} x^{t p^i}` has all `d_i + 1`
coefficients nonzero, because `d_i < p` and `p` is prime. A monomial `x^{t_0 + t_1 p + … + t_{s−1} p^{s−1}}`
with `0 ≤ t_i ≤ d_i < p` is a *unique* base-`p` expansion, so distinct tuples `(t_i)` give distinct
exponents: no two terms of the product can collide, and no cancellation is possible. Counting the
`Π(d_i+1)` surviving monomials gives the formula. ∎

(For `j = n = p^s` the formula would give `d_s + 1 = 2`, but `(x−1)^n = 0` in `R`; this is why the
minimum in `m(a)` runs only to `n − 1`. The distinction `(x−1)^n = 0` vs `w = 2` was already flagged
as a recorded error avoided in `P3_2_TWO_ORBIT.md`.)

---

## 2. Lemma H (the parity-check matrix is binomial, not factorial). Proved.

Write `f = Σ_j f_j x^j` and substitute `x = 1 + (x − 1)`. Then

    f = Σ_j f_j (1 + (x−1))^j = Σ_i ( Σ_{j ≥ i} f_j C(j,i) ) (x − 1)^i ,

so `(x−1)^a | f` **iff** `H_a f = 0`, where `H_a` is the `a × n` matrix

    H_a[i][j] = C(j,i) mod p ,        0 ≤ i ≤ a−1,  0 ≤ j ≤ n−1,

computed by **Lucas' theorem** (`C(j,i) ≡ Π_t C(j_t, i_t)`, else 0).

**Lemma H.** `C_a = ker H_a` over `F_q`.

*Proof.* Division by `(x−1)^a` in `F_q[x]`: `f = (x−1)^a h` iff the coefficients of `(x−1)^i` in `f`
vanish for `i < a`, which is exactly the displayed system. The change of basis `x ↦ 1 + (x−1)` is
unitriangular, hence invertible; `deg < n` is preserved. ∎

**Recorded error (found and fixed while running this probe, kept as an audit trail).** The first
version used the *falling factorials* `H[i][j] = j(j−1)…(j−i+1)` (the ordinary `i`-th derivative
evaluated at 1). That is wrong in characteristic `p` for `a > p`. Concretely, the ordinary derivative
test cannot see multiplicity beyond `p`: over `F_3`, `(x−1)^3 = x^3 − 1` has *every* ordinary
derivative vanishing at 1, although its root has multiplicity 3. The failure was caught immediately by
the committed `n = 9` table: the factorial version produced `d = 2` for every `a ≥ 3`, contradicting
`[1,2,2,2,3,3,3,6,9]` (`disagree 5`). With `H_a[i][j] = C(j,i)` all 9 non-trivial values agreed. The
binomial version is the "Hasse derivative" test, and it is the only one that is correct here.

A second, independent bug was found and fixed in the enumeration cross-check: the first version of
`code_distance_direct` divided the falling factorial by `k!` mod `p`, which is meaningless when
`k ≥ p`, and returned `d = 3` for `(x−1)^8` over `F_3` instead of `9`. It now expands `(x−1)^j` with
`C(j,k)` via Lucas.

---

## 3. Lemma C (circuit reduction). Proved.

**Lemma C.** `d(C_a)` equals the **girth** (minimum circuit size = smallest size of a linearly
dependent set of columns) of the column matroid of `H_a`.

*Proof.* A word `f` of weight `w` supported on `S = {j : f_j ≠ 0}` lies in `ker H_a` iff
`Σ_{j ∈ S} f_j · col_j(H_a) = 0` is a nontrivial dependency among those `w` columns. Conversely a
dependency supported on `S` is such a word. So the possible weights are exactly the sizes of
dependent column sets, and the minimum of each is the same number. ∎

This is what makes `n = 25, 27` reachable: no codeword enumeration is needed, only a subset search of
increasing size (capped at 7), with the enumeration used only where the dimension is so small that it
is cheap — and precisely there the true distance exceeds the cap, so the two regimes are complementary
rather than redundant.

---

## 4. Theorem A (`s = 1`, `n = p`). Proved.

**Theorem A.** Let `n = p` be prime. For `0 ≤ a ≤ p − 1`, `d(C_a) = a + 1`. In particular `d(C_a) = m(a)`,
since by Lemma W `w((x−1)^j) = j + 1` for `j ≤ p − 1` and therefore `m(a) = a + 1`.

*Proof.* **Upper bound.** `(x−1)^a = Σ_i C(a,i)(−1)^{a−i} x^i` with `a < p`, so all `a + 1` coefficients
are nonzero; hence `d(C_a) ≤ a + 1`.

**Lower bound.** Let `f = Σ_{k=1}^{w} c_k x^{j_k} ∈ C_a` with `c_k ≠ 0` and `0 ≤ j_1 < … < j_w ≤ p − 1`,
and suppose `w ≤ a`. By Lemma H, for every `i = 0, …, a−1`, `Σ_k c_k C(j_k, i) = 0`. Keep the first
`w` of these equations (`w ≤ a`):

    M c = 0,        M_{i,k} = C(j_k, i),   0 ≤ i ≤ w−1, 1 ≤ k ≤ w.

Now `C(j,i) = j^{(i)} / i!` with `j^{(i)} = j(j−1)…(j−i+1)`, and `i! ≠ 0` in `F_p` because `i ≤ w−1 ≤ p−2`.
Moreover `j^{(i)} = j^i + (terms of degree < i)`, so the matrix `(j_k^{(i)})_{i,k} = V · U` where
`V = (j_k^{\,i})_{i,k}` is the Vandermonde matrix of the `j_k` and `U` is upper triangular with `1`s on
the diagonal. The `j_k` are distinct integers in `[0, p)`, hence distinct in `F_p`, so
`det V = Π_{k<l} (j_l − j_k) ≠ 0`; therefore `det M ≠ 0` and `c = 0`, a contradiction. Hence `w ≥ a + 1`
for every nonzero `f ∈ C_a`, i.e. `d(C_a) ≥ a + 1`. ∎

This is a small but complete result: length-`p` repeated-root codes with generator `(x−1)^a` are MDS
with `d = a + 1`, established here without appealing to any outside theorem. It settles L-2 completely
in the `s = 1` case.

---

## 5. Theorem B (a low-order slice for every `s`). Proved.

**Theorem B.** For `s ≥ 2` and `1 ≤ a ≤ p^{s−1}`, `d(C_a) = 2`. Hence `d(C_a) = m(a)`, since
`w((x−1)^{p^{s−1}}) = 2` by Lemma W and `p^{s−1} ≥ a`, while `m(a) ≥ 2` for `a ≥ 1`.

*Proof.* **Lower bound.** A word of weight 1 is `c x^j` with `c ≠ 0`, a unit of `R` (`x` is a unit). But
`C_a = (x−1)^a R ⊆ (x−1)R` is a proper ideal for `a ≥ 1` (it is contained in the kernel of evaluation at
1), so no unit lies in `C_a`; hence `d(C_a) ≥ 2`.

**Upper bound.** Let `v = s − 1`, so `p^{s−1} < n`. Take the word `f = 1 − x^{p^{v}} ≠ 0`, of weight 2.
For `0 < i < p^{v}` the base-`p` digit `i_v` of `i` is `0` while the digit of `p^v` in position `v` is
`1`, so Lucas gives `C(p^{v}, i) = 0`; and `C(p^{v}, 0) = 1 = C(0,0)`. Hence every row of `H_{p^v}`
kills `f`, i.e. `f ∈ C_{p^v} ⊆ C_a` whenever `a ≤ p^v`. So `d(C_a) ≤ 2`. ∎

Equivalently, in matrix language: for `a ≤ p^v` every index `i < a` has `i_t = 0` for `t ≥ v`, so by
Lucas `C(j,i) = Π_{t<v} C(j_t, i_t)` depends only on `j mod p^v`; the columns of `H_a` are therefore
periodic with period `p^v`, and columns `0` and `p^v` coincide.

**Sharpness (why the range is exactly right).** The bound `a ≤ p^{s−1}` cannot be improved: for
`a = p^{s−1} + 1` the row `i = p^{s−1}` is added and `C(j, p^{s−1})` depends on the top digit `j_{s−1}`,
so the columns stop repeating and the weight-2 word dies. The data confirm the boundary in every case:
`n = 25`: `a = 5 → 2`, `a = 6 → 3`; `n = 27`: `a = 9 → 2`, `a = 10 → 3`; `n = 16` (`p = 2`):
`a = 8 → 2`, `a = 9 → 4`; `n = 9`: `a = 3 → 2`, `a = 4 → 3`.

---

## 6. What is left of L-2

By §4 and §5 the conjecture is now *proved* on

* all of `s = 1` (Theorem A), and
* the block `1 ≤ a ≤ p^{s−1}` for `s ≥ 2` (Theorem B),

and the only open range is

    p^{s−1} < a ≤ p^s − 1 = n − 1    (s ≥ 2).

On that range the periodicity argument fails exactly as described in §5, and the lower bound
`d(C_a) ≥ m(a)` must come from somewhere else. The natural route, not completed here, is the block
decomposition

    R_s = F_p[x]/(x^{p^s} − 1) ≅ R_{s−1}[ε]/(ε^p),     ε = y^{p^{s−1}} = x^{p^{s−1}} − 1,

together with `x^{p^{s−1}} = 1 + ε`, which is a unit of `F_p[ε]/(ε^p)`. Indeed every `f` has a unique
"block" form `f = Σ_{r=0}^{p−1} x^{r p^{s−1}} f_r` with `deg f_r < p^{s−1}`, and for this form the
weight is exactly additive, `w(f) = Σ_r w(f_r)` (the exponent blocks `[r p^{s−1}, (r+1)p^{s−1})` are
disjoint); while the divisibility condition reads `Σ_r (1+ε)^r f_r = Σ_i ε^i h_i` with
`h_i = Σ_r C(r,i) f_r` and `ord_y f = min_i ( i p^{s−1} + ord_y h_i )`. The obstruction is that the two
descriptions use different filtrations: additivity of the weight is in the `r`-decomposition, whereas
divisibility is a condition on the `i`-decomposition, and the change of basis between them is the
binomial matrix `(C(r,i))` of §2 — exactly the object that is *not* weight-controlled in general. A
proof of L-2 needs a statement comparing `w(Σ_r x^{r p^{s−1}} f_r)` with `min_i(i p^{s−1} + ord h_i)`;
no such statement is proved here, and the route is recorded as open rather than sketched as if it worked.

**Lower bounds that are all we currently have in the open range:** `d(C_a) ≥ 2` always (§5), and
`d(C_a) ≥ m(a)` is what must be shown. Singleton gives nothing here (it bounds `d` from above by
`a + 1`, and `m(a) ≤ a + 1`).

---

## 7. Computational verification (exact, reproducible)

`python3 research_project/phase3/p3_power_attainment.py > phase3/p3_power_attainment_log.txt`
(single command, no arguments; 759 s; exit 0). Both quantities are computed exactly: `d(C_a)` by the
circuit reduction (§3) with a subset cap of 7, falling back to full codeword enumeration where the
dimension is small, and `m(a)` from Lemma W.

### 7.1 Result of record

| `p` | `s` | `n` | values of `a` checked | agree | disagree | undetermined |
|---|---|---|---|---|---|---|
| 2 | 1 | 2 | 0–1 | 2 | 0 | 0 |
| 2 | 2 | 4 | 0–3 | 4 | 0 | 0 |
| 2 | 3 | 8 | 0–7 | 8 | 0 | 0 |
| 2 | 4 | 16 | 0–15 | 16 | 0 | 0 |
| 3 | 1 | 3 | 0–2 | 3 | 0 | 0 |
| 3 | 2 | 9 | 0–8 | 9 | 0 | 0 |
| 3 | 3 | 27 | 0–26 | 27 | 0 | 0 |
| 5 | 1 | 5 | 0–4 | 5 | 0 | 0 |
| 5 | 2 | 25 | 0–24 | 25 | 0 | 0 |
| 7 | 1 | 7 | 0–6 | 7 | 0 | 0 |
| 11 | 1 | 11 | 0–10 | 11 | 0 | 0 |
| **total** | | | | **117** | **0** | **0** |

Every non-trivial `a` in every one of the 11 cases is decided; nothing was left "above cap". This
extends the earlier `n = 9` evidence (`10/10`) to `n = 4, 8, 16, 25, 27` and to the `s = 1` primes
`2, 3, 5, 7, 11`.

### 7.2 Independent two-method cross-check

For each case, every `a` with `p^{n−a} ≤ 50 000` was computed **both** by the circuit matroid and by
direct codeword enumeration (`cross_check`): 70 values compared, **0 mismatches**
(`p=2,n=2`:2, `n=4`:4, `n=8`:8, `n=16`:15; `p=3,n=3`:3, `n=9`:9, `n=27`:9; `p=5,n=5`:5, `n=25`:6;
`p=7,n=7`:5; `p=11,n=11`:4). The two methods share only Lemma H, so this also validates the subset
search itself.

### 7.3 The two informative tables

`n = 27` (`p = 3`), `w((x−1)^j) = [1,2,3,2,4,6,3,6,9,2,4,6,4,8,12,…]`:

| `a` | 0 | 1–9 | 10–18 | 19–21 | 22–24 | 25 | 26 |
|---|---|---|---|---|---|---|---|
| `d(C_a)` computed | 1 | 2 | 3 | 6 | 9 | 18 | 27 |
| `m(a)` | 1 | 2 | 3 | 6 | 9 | 18 | 27 |

`n = 25` (`p = 5`):

| `a` | 0 | 1–5 | 6–10 | 11–15 | 16–20 | 21 | 22 | 23 | 24 |
|---|---|---|---|---|---|---|---|---|---|
| `d(C_a)` computed | 1 | 2 | 3 | 4 | 5 | 10 | 15 | 20 | 25 |
| `m(a)` | 1 | 2 | 3 | 4 | 5 | 10 | 15 | 20 | 25 |

Both tables are consistent with `d(C_a) ≤ a + 1` (Singleton) and with `d ≥ 2` (§5). The plateaus are
explained by Lemma W: on `10 ≤ a ≤ 18` the minimiser is `j = 18 = 2·3^2` with `w = 3`, on `19 ≤ a ≤ 21`
it is `j = 21 = 3 + 2·9` with `w = 6`, and so on.

### 7.4 The `m(a) ≤ a + 1` (Singleton consistency) check

    python3 research_project/phase3/p3_power_attainment.py --mbound > phase3/p3_power_attainment_mbound_log.txt

19 lines, exit 0, no code constructed: `m(a) <= a+1` for **all** `a` in `p = 2 (s = 1..5)`,
`p = 3 (s = 1..4)`, `p = 5 (s = 1..3)`, `p = 7 (s = 1..2)`, `p = 11`, `p = 13` — 16 cases, no violation.

### 7.5 What is *not* claimed from these numbers

* Not a proof of L-2 (§6).
* No statement about non-prime-power `n`, about `s ≥ 4` except `p = 2, n = 16`, or about `n = 49, 81,
  125`; the subset search is exponential in the answer, and `n = 27` already costs 257 s. The open
  cases `n = 49` (`p = 7, s = 2`) and `n = 81` (`p = 3, s = 4`) are **not computed** — the cap-7 search
  over `C(49,7) ≈ 8.6·10^7` subsets is out of reach in pure Python. This is a genuine limitation, not
  a skipped check.
* `m(a)` is a statement about the ideal `C_a` in the *single-orbit* family. It says nothing about the
  ring-level `R_e` / Gray-map question of P3-3, and it does not interact with the hull distribution of
  P3-1/P3-4. In particular L-2 remains a limitation of the *distance* side only.

---

## 8. Standing constraints respected

* Every number above comes from the logged single command; no figure is estimated.
* L-2 is labelled a conjecture except on the two ranges where §4 and §5 prove it.
* Novelty is claimed nowhere. B-1, B-2a, B-2b and the Tian–Gao–Gao full text remain unread, so even
  Theorem A (a short Vandermonde argument, likely classical for length-`p` cyclic codes) is presented
  as *proved here*, not as *new*.
* Phase 9 remains **NO-GO**. This document does not reverse that decision: L-2 is still open in its
  main range, so the blueprint's "at least one substantive proved theorem" bar is not met by §4–§5
  (Theorems A and B are correct but small, and both are special cases of a conjecture, not a new
  method).

---

## 9. Deliverable and status bookkeeping

* Probe: `research_project/phase3/p3_power_attainment.py` (stdlib only, ASCII).
* Logs: `research_project/phase3/p3_power_attainment_log.txt` (212 lines, main run) and
  `research_project/phase3/p3_power_attainment_mbound_log.txt` (19 lines, `--mbound`).
* `PHASE_STATUS.md`: the `P3_2_TWO_ORBIT.md` row `n = 9` `10/10` conjecture remains as a historical
  record; a new `P3-7` section records Theorem A, Theorem B and the widened verification, and the
  limitation line for L-2 was updated from "conjecture, 10/10 at n=9" to "proved for s=1 and for
  1 ≤ a ≤ p^{s−1}; conjecture on p^{s−1} < a < p^s" — and then **superseded by P3-7b**: L-2 is a
  known theorem (Dinh 2008) and is no longer counted as a limitation.
