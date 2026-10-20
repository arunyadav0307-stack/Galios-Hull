# FINAL GO / NO-GO DECISION — F11

**Date:** 2026-10-20 · **Branch:** `arena/1625045b-galios-hull`
**Subject:** whether to invest in a correction note on finding F11 (the missing
component-degree factor in the Gray-map/dimension bookkeeping of the source paper).

**Nothing was drafted, committed or pushed. No manuscript, no correction note, no
submission letter exists.**

---

## 0. The decision

> ## **BLOCKED.**
>
> The mathematics is settled for **arXiv v1** and is now settled for **all 13 rows of
> Table 1**, not only for the worked examples. What is **not** settled is the object the
> decision is about: the **published** article. Its `§2` body is behind a paywall, and no
> legitimate free copy of the published version exists at the time of writing
> (`verification/VOR_INSPECTION_2026-10-20.md` §5).
>
> BLOCKED here is **a statement about access, not about the mathematics**. The
> decision rule that converts this into GO or NO-GO is one sentence long and is in §6.

---

## 1. Verified facts about arXiv v1

**Identity.** Debnath–Islam–Martínez-Moro–Prakash, *Galois hulls of constacyclic codes
over affine algebra rings*, **arXiv:2412.08512v1**, submitted 11 Dec 2024, 27 pp,
291 546 B, SHA-256 `0db90bfbeda69ad1af231b81d92f24be3589ed15ac2e0ade6605ba7ad0ddc039`.
Hash unchanged at every check in this project, including today (re-extracted after a
sandbox reset and re-hashed).

**F1 — The algebra's components are extension fields.** For
`A = F_q[X₁,…,X_ℓ]/⟨t₁(X₁),…,t_ℓ(X_ℓ)⟩` with each `t_i` square-free,
`A ≅ ⊕_S A_S` with `A_S = F_q(ν₁,…,ν_ℓ)` and, by the paper's own p.4,
`|S(ν)| = lcm(d₁,…,d_ℓ) = [F_q(ν₁,…,ν_ℓ) : F_q]`. (p.4–5)

**F2 — The paper writes every element of A with coefficients in F_q.** p.7, verbatim:
"Every a ∈ A can be expressed as a = Σ_{S(ν)∈Ŝ} a_{S(ν)} e_{S(ν)}, where
**a_{S(ν)} ∈ F_q for all S(ν) ∈ Ŝ**." This is equivalent to asserting
`dim_q A = N = |Ŝ|`.

**F3 — That assertion is false in all three of the paper's own examples.**
`dim_q A = Σ_S |S(ν)|`, which equals `N` only when every `|S(ν)| = 1`. Computed:
Example 1 `N = 6`, `dim_q A = 20`, sizes `[2,3,3,3,3,6]`; Example 2 `N = 2`,
`dim_q A = 4`, `A ≅ F₈₁ × F₈₁`; Example 3 `N = 2`, `dim_q A = 4`,
`A ≅ F₆₂₅ × F₆₂₅`. Hence `|A| = q^{dim A}` strictly exceeds `|F_q^N|`
(`2²⁰` vs `2⁶`; `6561` vs `81`; `390625` vs `625`).

**F4 — The Gray map cannot be what the paper says it is.** p.17, eq. (10):
`ψ : A → F_q^N`, `a ↦ (a_{S(ν₁)},…,a_{S(ν_N)})·M` with `M ∈ GL_N(F_q)`, followed by
"It is easy to verify that the map ψ is bijective linear isometry from A^n (Gray
distance) to F_q^{nN} (Hamming distance)". By F3 the map is not injective, so it is
not bijective and — because a non-injective map cannot preserve Hamming distance on
the nose — not an isometry either.

**F5 — Code dimensions in the examples are wrong by the factor |S(ν)|.**
Independent rank computations: Example 2 `dim₉ C = 20`, not 10, so `[14,10,4]₉` is
impossible because `20 > 14 = nN`; Example 3 `dim₂₅ C = 44`, not 22, so `[26,22,4]₂₅`
is impossible because `44 > 26 = nN`.

**F6 — Theorem 8's formula is right, its labelling is not.** As a statement about
`A_S`-dimensions, `dim(hull_k C) = Σ_S dim_{A_S} hull_k(C_S)` is correct; it equals the
`q`-dimension only when every `|S(ν)| = 1`.

**F7 — Table 1 fails in all 13 rows.** See §4. This is new in this round and is the
main strengthening: the defect is not confined to Examples 2–3.

**F8 — The paper's own arithmetic is internally consistent.** Theorem 10 applied to the
printed inputs reproduces the printed entanglement `c` and the printed "Diff" column in
13/13 table rows (`14−10−0 = 4`, `26−22−2 = 2`, and so on). The defect is *upstream*, in
the inputs — a single omitted factor, not a computational error.

**Not verified, and not claimed:** the printed minimum distances; any corrected
distance; any corrected quantum-code parameter set (§5).

---

## 2. Verified facts about the published version

**Identity (complete).** *Discrete Mathematics* (Elsevier), ISSN 0012-365X,
**volume 349, issue 2, February 2026, article number 114750**, DOI
**10.1016/j.disc.2025.114750**, PII `S0012365X25003589`, research article, 45 references,
cited once. Crossref record type `journal-article` (not "article in press").

**P1 — The published version is materially different from v1.** 45 references against
v1's 44; the published introduction cites "Example 2, **Example 4**, and **Table 2**",
neither of which exists in v1; a new counting result on
`𝒟_k(n,q,λ)` = the number of distinct `q`-dimensions attained; theorem numbering has
shifted (published **Theorem 4** = v1 Theorem 2; published **Lemma 7** = v1 Lemma 8).
**Extrapolating a v1 defect into the published text is therefore unsafe, and is not
done anywhere in this project.**

**P2 — The "q-dimension" framing survives into the published version.** The published
introduction says "Our main objective is to derive a formula for the **q-dimensions**
of the k-Galois hulls…", and the published `§3` snippet says "…derive a formula for the
**q-dimension of the k-Galois hull**". These are the exact terms implicated in F11.
*This raises the prior. It establishes nothing about the body.*

**P3 — The published article is not open access.** Crossref lists only Elsevier TDM
licences; OpenAlex records `primary_location.is_oa = false`, `license = null`,
`version = publishedVersion`, with `oa_status = green` pointing **only** at
`arxiv.org/pdf/2412.08512`. The publisher page offers just
`Access through your organization` and `Purchase PDF`, and a direct request to
`/science/article/pii/…` redirects to the `/abs/pii/…` preview. See
`verification/VOR_INSPECTION_2026-10-20.md` §5.

**P4 — The green open-access copy is v1, not the published version.** arXiv submission
history shows a single entry: `[v1] Wed, 11 Dec 2024`. There is no v2.

---

## 3. Unresolved or inaccessible evidence

| # | Question | Status |
|---|---|---|
| b1 | Does the published `§2` still write `a_{S(ν)} ∈ F_q`? | **BLOCKED — decisive item** |
| b2 | Does the published eq. (10) still set `N = |Ŝ|` with `M ∈ GL_N(F_q)` and call ψ bijective? | **BLOCKED** |
| b3 | Do the published Examples 2–4 and Tables 1–2 still print length `2n` with the unweighted `k`? | **BLOCKED** |
| b4 | Are the published quantum parameters still `[[14,10,4;4]]₉` and `[[26,22,4;2]]₂₅`? | **BLOCKED** |
| b5 | Does published **Theorem 4** (v1 Theorem 2) print the same hull formula? | **BLOCKED** |
| b6 | Does the published conclusion still call non-isometric enumeration open? | **BLOCKED** — the snippet stops mid-sentence at "have yet to be" |
| b7 | Is the new `|𝒟_k(n,q,λ)|` result affected by the same factor? | **BLOCKED**, and guessing would be speculation |

**Not used, and not to be used, as substitutes:** the abstract, the introduction, the
section snippets, the reference list, the arXiv v1, or any third-party summary.
Six legitimate routes to the full text are listed in
`verification/VOR_INSPECTION_2026-10-20.md` §5.6.

**Third pass, later the same day.** Seven access routes were tried and all are closed
(publisher full-text URL → preview redirect; preview → "Access through your
organization" / "Purchase PDF"; Crossref → TDM licences only, no Creative Commons;
OpenAlex → `is_oa: false` on the published version, green OA points at the arXiv v1;
arXiv → `[v1]` only, no v2; `uvadoc.uva.es` → no deposit; ResearchGate → the Dec 2024
preprint). Itemised in `FINAL_F11_VERIFICATION_LOG.md` §1, which also names the missing
evidence one item at a time (§1.1). Shadow libraries and third-party summaries were not
used. **Status unchanged: BLOCKED.**

---

## 4. The 13-row Table 1 audit

### 4.1 What was established, and how

The audit rests on three facts that need no numerical input:

1. **Every ring in Table 1 has `dim_q A = 4`.** Both defining polynomials are
   quadratic in all three cases (`q=4` ring on p.21; Example 2's ring on p.18;
   Example 3's ring on p.20), so `dim_q A = ∏ deg t_i = 4`.
2. **Every component degree is at most 2.** Each `ν_i` is a root of a quadratic, so
   `F_q(ν₁,ν₂) ⊆ F_{q²}` and `|S(ν)| = [F_q(ν₁,ν₂):F_q] ≤ 2`.
3. **The printed length is `2n`, and eq. (10) gives `ψ : A → F_q^N` with `N = |Ŝ|`.**
   So the printed length asserts `N = 2`.

From `4 = dim_q A = Σ_S |S(ν)|` over `N = 2` components with each `|S(ν)| ≤ 2`, both
component degrees equal 2. Therefore

> `dim_q C = Σ_S [A_S:F_q]·dim_{A_S}C_S = Σ_S |S(ν)|·(n − deg g_S) = 2·[(n−deg g₁) + (n−deg g₂)] = 2k_printed`

and the printed dimension is wrong by a factor of two **in every row**, because
`k_printed > 0` always.

Equivalently, and independent of whether any `t_i` splits:

| if … | then … |
|---|---|
| some `t_i` is non-split | `N = 2`, the printed length `2n` is right and the printed `k` should be `2k` |
| both `t_i` split | `N = 4`, the printed `k` is right and the printed length should be `4n` |

There is no algebra in Table 1 for which `[2n, k, d]` is correct. The computed
structures confirm which case actually occurs:

| `q` | `t₁`, `t₂` | splitting | `N` | `|S(ν)|` | `dim_q A` | `Σ = ∏ deg t_i` |
|---|---|---|---|---|---|---|
| 4 | `x²+x+ω`, `x²+ωx+ω` | both irreducible over `F₄` | 2 | `[2,2]` | 4 | ✓ |
| 9 | `x²+x+ω`, `x²+ω⁵x+2` | both irreducible over `F₉` | 2 | `[2,2]` | 4 | ✓ |
| 25 | `x²+x+ω¹³`, `x²+ω³x+1` | `t₁` irreducible, **`t₂` splits** over `F₂₅` | 2 | `[2,2]` | 4 | ✓ |

All six polynomials are square-free, as the paper requires. Note that `t₂` in
Example 3 splitting is **not** an error: the paper's hypothesis is square-free, not
irreducible. (An earlier note in this project called it "a paper slip"; that note was
wrong and is corrected here.)

### 4.2 The 13 rows

`k = (n − deg g₁) + (n − deg g₂)`; `2k` is the true `F_q`-dimension.

| # | `q` | `n` | `deg g₁` | `deg g₂` | arithmetic | `k` printed | `2k` | printed length | verdict |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 4 | 5 | 2 | 2 | (5−2)+(5−2) = 6 | 6 | **12** | 10 | **impossible** |
| 2 | 9 | 4 | 2 | 2 | (4−2)+(4−2) = 4 | 4 | **8** | 8 | whole space ⇒ `d = 1` |
| 3 | 9 | 5 | 2 | 1 | (5−2)+(5−1) = 7 | 7 | **14** | 10 | **impossible** |
| 4 | 9 | 5 | 3 | 2 | (5−3)+(5−2) = 5 | 5 | **10** | 10 | whole space ⇒ `d = 1` |
| 5 | 9 | 5 | 4 | 3 | (5−4)+(5−3) = 3 | 3 | **6** | 10 | dimension feasible, `k` wrong |
| 6 | 9 | 6 | 4 | 1 | (6−4)+(6−1) = 7 | 7 | **14** | 12 | **impossible** |
| 7 | 9 | 7 | 3 | 1 | (7−3)+(7−1) = 10 | 10 | **20** | 14 | **impossible** |
| 8 | 9 | 7 | 4 | 3 | (7−4)+(7−3) = 7 | 7 | **14** | 14 | whole space ⇒ `d = 1` |
| 9 | 9 | 7 | 4 | 6 | (7−4)+(7−6) = 4 | 4 | **8** | 14 | dimension feasible, `k` wrong |
| 10 | 25 | 13 | 3 | 1 | (13−3)+(13−1) = 22 | 22 | **44** | 26 | **impossible** |
| 11 | 25 | 16 | 2 | 1 | (16−2)+(16−1) = 29 | 29 | **58** | 32 | **impossible** |
| 12 | 25 | 20 | 2 | 1 | (20−2)+(20−1) = 37 | 37 | **74** | 40 | **impossible** |
| 13 | 9 | 26 | 4 | 1 | (26−4)+(26−1) = 47 | 47 | **94** | 52 | **impossible** |

**Totals.** 8 rows impossible (1, 3, 6, 7, 10, 11, 12, 13); 3 rows degenerate,
`2k = 2n` forcing `d = 1` against printed `d ∈ {4,4,6}` (2, 4, 8); 2 rows
dimensionally feasible (5, 9) but with the printed `k` still half the true dimension.
In **all 13** rows the printed `(length, dimension)` pair is mutually inconsistent.

### 4.3 The two distinct failures, kept apart

* **Invalid input parameters** (`2k > 2n`, 8 rows). No `F_q`-subspace of `F_q^{2n}` has
  dimension `2k`. The printed `[2n, k, d]` is not a code with a wrong distance; it is
  not a code at all. Nothing is said about `d`, which is then irrelevant.
* **Incorrect distance claim** (`2k = 2n`, 3 rows). The dimension is realisable: the
  subspace is all of `F_q^{2n}`, which contains a weight-1 vector, so `d = 1`. The
  dimension is fine and the printed `d > 1` is false.
* **Dimension understated** (`2k < 2n`, 2 rows). Neither failure applies, but the
  printed `k` is still half the true dimension.

The bound `2k ≤ 2n` is not an extra assumption. It follows from the paper's own claims:
ψ is linear and injective (p.17), its codomain is `F_q^{nN}` (eq. (10)), and
`dim_q C = Σ_S [A_S:F_q] dim_{A_S}C_S` (CRT, p.5). Its hypothesis list is written out
in full in `code/table1_forensics.py`, PART 6.

**The exhaustive dilemma.** Either ψ is injective, in which case `dim ψ(C) = 2k ≠ k`
and the printed parameters are false; or ψ is not injective, in which case the proof of
Lemma 9(2) fails — that proof says, verbatim, "Since ψ is an injective map, we have
c = c′" — and Theorem 10's application collapses with it. The paper cannot have both.

### 4.4 EAQECC arithmetic, checked separately

Theorem 10: `k′ = k − h` and `c = nN − k − h` with `h = dim_q(hull_k C)`. Solving the
first for `h` and predicting the second from the printed `k, k′` alone reproduces the
printed `c` in **13/13** rows (`h = 4,0,2,4,2,2,0,0,0,2,2,2,3`). The "Diff" column
`(n′ − k′ + c) − 2(d−1)` is reproduced in **13/13**, and the `*`/`†` decoration matches
`Diff ∈ {0,2}` in **13/13**.

This is deliberately a check of the *arithmetic*, not of its applicability. The
arithmetic is right; the input to it is wrong, because Theorem 10 is applied to
`D = ψ(C)` with `dim D = k_printed` when `dim D = 2k_printed`.

*Observation, reading-dependent:* Lemma 8 is quoted as requiring `d ≤ (n+2)/2`; the
extracted text reads "d ≤ n+22", which is only sensible as `(n+2)/2`. Rows **5 and 9**
violate that hypothesis, so their "Diff" entry compares quantities outside the lemma's
stated domain. This affects nothing above.

### 4.5 Reproducibility

Two scripts, both pure Python 3, no third-party imports:

| Script | What it does | Result |
|---|---|---|
| `code/table1_audit.py` | checks C0–C7 on all 13 rows; imports `Fld`/`pdivides` from `code/f11_source_audit.py` | exit 0 |
| `code/table1_forensics.py` | **self-contained**: rebuilds `F₄, F₉, F₂₅` and `F₁₆, F₈₁, F₆₂₅`, finds roots, counts Galois orbits, and runs checks C0–C10 including a transcription cross-check against the raw text | exit 0 |

`code/table1_forensics.py` does not import anything from the project, so its verification of
the algebras is independent of every earlier script.

**A transcription error was caught by the new checks during this round**, which is the
reason the checks exist. The λ-cell of row 1 reads `ω e₁ + e₂`; the PDF text layer
writes it as `w^e1 +e2` because `^I` is part of the UTF-8 encoding of ω itself
(bytes `CF 89`), not a caret. Read hastily it looks like `ω^{e₁+e₂}`. The divisibility
test settled it: of the nine assignments in `(F₄*)²`, **only** `(λ₁,λ₂) = (ω,1)` makes
both `g_S` divide `xⁿ − λ_S`. Two further errors of mine were caught the same way in
the previous round (integer-flattened symbolic coefficients; one `λ` used for both
components).

Guards in place:

* **C0 / PART 2b — divisibility.** `g_S | xⁿ − λ_S` for both components, in **13/13**
  rows, under **all 8** admissible namings of `ω` (`ω` a root of its defining
  quadratic: `{2,3}`, `{3,7}`, `{5,21}` — the complete set, not a sample). This is the
  test that makes the transcription trustworthy.
* **PART 2 — double transcription.** Every printed tuple of every row occurs verbatim
  in an independently copied raw text block: **13/13**.
* **C2** `k = Σ(n − deg g_S)`: 13/13. **C3** length `= 2n`: 13/13.
  **C9** `d` agrees between the two columns: 13/13. **C10** `n′ = length`: 13/13.
  **C6/C7/C8**: 13/13.

`verification/table1_forensics.out` and `verification/table1_audit.out` were both
**re-produced from a clean unzip of `FINAL_F11_EVIDENCE_DOSSIER.zip`** in a scratch
directory; the outputs are identical to the stored logs apart from the timestamp line
and the path of the log file itself.

---

## 5. Precise scope of any potential correction

This is what a correction note **could** say on the evidence in hand. It is a scope
statement, not a draft.

**In scope — supported by §1 and §4, for arXiv v1:**

1. The coefficient in p.7's idempotent expansion must lie in `A_{S(ν)}`, not in `F_q`;
   equivalently the p.7 assertion forces `dim_q A = N`, which fails in all three
   examples (`20 ≠ 6`, `4 ≠ 2`, `4 ≠ 2`).
2. Eq. (10)'s `ψ : A → F_q^N` is therefore not injective, so the "bijective linear
   isometry" of p.17 does not exist for these rings.
3. Code dimensions carry the factor `|S(ν)|`: `dim_q C = Σ_S |S(ν)| dim_{A_S}C_S`.
   Concretely, Example 2's code has `dim₉ = 20`, not 10, and Example 3's has
   `dim₂₅ = 44`, not 22.
4. Consequently `[14,10,4]₉`, `[26,22,4]₂₅` and **all 13 rows of Table 1** are
   mis-stated: 8 are impossible, 3 force `d = 1`, and the remaining 2 have the wrong
   `k`.
5. Because Theorem 10 is applied to the mis-stated `ψ(C)`, every EAQECC parameter in
   the paper inherits the error *even though the arithmetic is right*.

**Out of scope — not supported, and must not appear:**

| Not assertable | Why |
|---|---|
| Any corrected code or EAQECC parameter set | the true hull dimension per row was not computed, and the distance of the true image was not computed |
| Any corrected minimum distance | never computed |
| That the published version has the same defect | `§2` body unread — BLOCKED |
| What the authors "meant" | intent is not evidence |
| That other theorems are invalid | Theorems 2–7 are correct as statements about `A_S`; only the `q`-dimension labelling and its downstream uses fail |
| Any priority or novelty claim | the component-field distinction is elementary and very likely familiar to specialists |

**A correction would be a one-line statement plus its consequences** — the missing
factor `|S(ν)|` — not a new theory. That is precisely why it is not a manuscript.

---

## 6. Recommendation

### 6.1 The decision rule

One sentence in the published `§2` decides it. In v1 that sentence is on **p.7**:

> "Every a ∈ A can be expressed as a = Σ_{S(ν)∈Ŝ} a_{S(ν)} e_{S(ν)}, where
> **a_{S(ν)} ∈ F_q for all S(ν) ∈ Ŝ**."

| Finding at the corresponding place in the published `§2` | Decision |
|---|---|
| still `a_{S(ν)} ∈ F_q` | **GO** — the defect is in the version of record; a correction note is warranted, scoped by §5 |
| changed to `∈ A_{S(ν)}` or `∈ F_{q^{\|S(ν)\|}}` | **NO-GO, permanently** — the defect was v1-only and has been repaired; record the negative result and close the direction |

Two confirmation checks, to be run in the same sitting:

1. published eq. (10) — does it still set `N = |Ŝ|` and call ψ bijective?
2. published Tables 1 and 2, plus the new Example 4 — do they still print length `2n`
   with the unweighted `k`?

If (1) or (2) has changed but the `§2` sentence has not, the note's scope narrows
accordingly; it does not widen.

### 6.2 Why BLOCKED rather than GO or NO-GO

* **Not GO**, because GO means "write the correction", and the correction would be
  against the published article, whose text has not been read. Two of this project's
  standing rules forbid exactly that: do not infer the version of record's content,
  and do not draft a correction note.
* **Not NO-GO**, because NO-GO would assert the published version is clean, and
  nothing supports that: it is materially different from v1, it retains the
  "`q`-dimension" framing in the introduction and the `§3` snippet, and it adds a
  counting result in the same territory.
* **BLOCKED is the honest state**: the mathematics for v1 is finished and the decision
  is waiting on one unread sentence behind a paywall.

### 6.3 What to do next, in order

1. Obtain the published `§2` by any of the six legitimate routes in
   `verification/VOR_INSPECTION_2026-10-20.md` §5.6 (institutional access, purchase,
   interlibrary loan, author request, TDM agreement, repository deposit).
2. Read the single sentence above, then the two confirmation checks.
3. Apply the table in §6.1. Nothing else in this project needs to be revisited: §1 and
   §4 stand as the complete mathematical record for v1 either way.

**If the answer is GO,** the note must: claim only the missing factor and its listed
consequences (§5); cite the **published** numbering (Theorem 4, Lemma 7), not v1's;
acknowledge the new `|𝒟_k(n,q,λ)|` result and say plainly that its status could not be
determined; and make **no** novelty claim.

**In no branch** should the abandoned Phase-5 manuscript be revived. That object was
assessed as known-or-routine, and nothing in this round changes that assessment.

---

## 7. Artifacts

Everything below is reproduced in `FINAL_F11_EVIDENCE_DOSSIER.zip` (23 zip entries:
20 files = 19 content members plus `MANIFEST.txt`). `MANIFEST.txt` lists every member
with its SHA-256 and size, and every member was **re-hashed after a clean unzip** —
19/19 verified. All six scripts were then executed from the unzipped archive: each
exited 0, and both audit logs reproduced **identically**.

The archive's own byte size and SHA-256 are deliberately **not** printed here: this file
sits inside that archive, so any such value would be stale the moment it was written.
They are recorded instead in `verification/zip_validation_2026-10-20.log`, which is kept
in the project tree **outside** the archive, together with the full validation
transcript.

Hashes of the **scripts and logs** (stable; these files were not edited after the
archive was built):

| Path | Bytes | SHA-256 |
|---|---|---|
| `code/f11_source_audit.py` | 29 558 | `433c4124d509496cb1f06da4c7960186950339ce53d5d41c810e893db9df6df1` |
| `verification/f11_source_audit.out` | 9 012 | `e4d3b064c446ff85a69c16d4c2c68458526631e7f816ec74013c43511530831d` |
| `code/table1_audit.py` | 9 428 | `665e6f3fbd6f1dafcf6eddcbe5dd554beb672bb763a79fab93acfbfb3ebc8cca` |
| `verification/table1_audit.out` | 4 642 | `8c2d11d485f8723c6b7e22827318591e7f76c6e5286fa273eb62a909fe3e5caa` |
| `code/table1_forensics.py` | 30 091 | `848ac72ad01e22df7126066bd3b3754af73588692fd6b0168421a77ca7272ad1` |
| `verification/table1_forensics.out` | 15 309 | `cc6c25d5facf046667653608f945ffef0765442bfcd8ba560cc173b6007f7380` |
| `code/final_check_A.py` | 15 392 | `4e13e8a98e77b12f12e7d0b0a355cf3b9c2b39941588857988aad7213cdf054e` |
| `verification/final_check_A.out` | 5 916 | `35d8349b186a2153576055a776a83d86e59ba39e5a10e85582bbb8751f48ac67` |
| `code/final_check_B.py` | 18 208 | `4cee6242b56657e1c5d5211cff347f2e0c3637bec3826509dba8ff93bd39f51d` |
| `verification/final_check_B.out` | 5 870 | `6140cea82c7b27b52a52321c37616ae4e47c918e3695ba1b08d432b769f511ca` |
| `code/gf.py` | 13 517 | `1547539a33432cd19ee7d8d3306234b00640a6a9b336b923dbd05d9f07b3b903` |
| `code/isometry_hull_screening.py` | 8 600 | `5d9a696eacb14abcd8138a7655a4d4ca67beb8994ed8de95f4cc793c27068a1a` |
| `verification/isometry_hull_screening.out` | 2 239 | `49a3cf2f70c1e461dd2cccb2813a52654a97c21a42443a011e5d6658aa0cad0f` |

Hashes of the **documents** are in `MANIFEST.txt` only. They are deliberately not
reproduced here: editing this file changes its own hash, so any self-referential value
would be stale on arrival. `MANIFEST.txt` is generated after the last edit and is the
authoritative record.

**Test outputs, verbatim.**

* `code/table1_audit.py` → exit **0**; `C0 13/13 naming-free`; `C2 13/13`;
  `C3 13/13`; `C5 violated in 8 rows [1,3,6,7,10,11,12,13], degenerate in 3 [2,4,8]`;
  `C6 13/13`; `C7 13/13`.
* Clean-room re-run of both scripts from a pristine unzip
  (`verification/cleanroom_run_2026-10-20.log`): exit **0** each; every manifest member
  verified before running; each console output **identical** to its archived `.out`;
  the two scripts agree on every row set.
* `code/table1_forensics.py` → exit **0**; `PART 1` all three rings `N = 2`,
  `|S| = [2,2]`, `dim_q A = 4`, `CONSISTENT`; `PART 2 13/13`; `PART 2b 13/13` in all
  8 namings; `C2 13/13`, `C3 13/13`, `C6 13/13`, `C7 13/13`, `C8 13/13`, `C9 13/13`,
  `C10 13/13`.
* Both were re-run from a clean unzip in `/tmp`; `diff` against the stored logs shows
  **no difference** apart from the timestamp line and the log's own path.

**Source integrity.** The source PDF was not modified:
`sha256 = 0db90bfbeda69ad1af231b81d92f24be3589ed15ac2e0ade6605ba7ad0ddc039`,
re-verified at the start and at the end of this round.

**Nothing was committed or pushed.** `research_project/` remains untracked in the
working tree on branch `arena/1625045b-galios-hull`.
