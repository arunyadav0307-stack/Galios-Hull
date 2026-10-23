# REFERENCE VERIFICATION REPORT — Phase 2

**Object verified:** the reference apparatus of the source of record — Yadav, Singh, Islam, Prakash, Solé, *Hermitian hull of constacyclic codes over a class of non-chain rings and new quantum codes*, *Comput. Appl. Math.* **43**, art. 269 (2024), DOI `10.1007/s40314-024-02789-1`, PDF `sha256 7f7e6803…` (612 826 B, 23 pp.), version examined **`hal-04825601v1`** (not the version of record — open item U-8).

**Two deliverables are reported separately here:** (A) whether the paper's citation apparatus is internally sound, and (B) whether the cited works are bibliographically real. These are different questions and get different verdicts.

---

## 1. Headline result, including a retraction of my own earlier flag

| Question | Verdict |
|---|---|
| Is the reference list complete and free of duplicates? | **PASS** — 48 entries `[1]`–`[48]`, no gaps, no duplicates |
| Is every listed entry cited in the body? | **PASS** — 48 of 48 |
| Is every in-text citation defined in the list? | **PASS** — no citation refers to a number outside `1…48` |
| Are the key prior-art references real works? | **PASS for the 12 works actually checked** (§5); the remaining 36 were not independently verified |
| Defects to report against the paper | **NONE in this apparatus** |

**Retraction.** An earlier pass in this session flagged (i) `[22]` as "listed but never cited" and (ii) nine numbers `[50, 51, 52, 55, 56, 57, 60, 68, 72]` as "cited but absent from the 48-entry list". **Both flags were artefacts of my own extraction regex, not defects in the paper.** Root causes, each confirmed by inspection of the raw text:

1. **Range notation.** The paper cites in en-dash ranges — `[18–21, 34, 35]`, `[10, 15–17, 25, 26, 33, 43–46]`, `[4, 7, 13, 14, 16, 41]`, `[23, 37, 38]`, `[27, 31, 39]`, `[9, 24]`, `[1, 32]`. The first regex matched only `[digit…]` and never expanded `18–21`, so `[19]` and `[21]` looked uncited.
2. **Annotated citations.** `[22]` *is* cited, in a form the regex rejected:

   > `Lemma 17. [22, Hermitian construction] Let C be a linear code over F_{q^2} with the parameters [n, k, d]_q such that C^{⊥H} ⊆ C. …` (p. ~16)

   A correctly attributed citation with an author annotation, missed because the closing bracket is not adjacent to the number.
3. **Table parameter brackets.** All nine "missing" numbers come from `[n,k,d]` and `[[n,k,≥d]]` code-parameter cells in Tables 2–3, e.g. `[60, 57, 3]`, `[56, 46, ≥ 3]`, `[72, 68, 3]`. E.g. the `[50]` hit is the `50` inside `[[60, 50, 3]]`. These are not citations at all.

No correction to the paper is implied by any of this, and none is recorded.

---

## 2. Method (reproducible)

Text source: `research_project/source_audit/source_text/pages/page_002.txt … page_020.txt` (body, 19 pages) and `page_020.txt … page_023.txt` (reference list). The list begins on printed p. 19 (PDF p. 20) and ends on printed p. 22 (PDF p. 23).

Body pass — a bracket token is accepted as a citation when all of the following hold:

* its content contains no `≥` (that marks a quantum-parameter bracket);
* the character immediately after `]` is not a digit (that marks an `[n,k,d]^q` parameter cell);
* it is not the inner half of a `[[…]]` parameter cell;
* its content matches `digits [ – digits ] ( , … )*` with an optional trailing `, Annotation` and every number ≤ 48;
* en-dash/ASCII-hyphen ranges are expanded.

Reference-list pass — split on `[n]` markers, then check completeness, duplicates (by first-author + year key), presence of a year, presence of a DOI/URL.

Commands are inline `python3`; the audit is re-runnable at any time and uses no network.

---

## 3. Structural audit of the list

| Check | Result |
|---|---|
| Entries parsed | 48 (`[1]`–`[48]`), none missing |
| Duplicates | 0 |
| Entries without a `(year)` | 3 — `[3]`, `[11]` (URL resources with "accessed on" dates), `[13]` (ISIT 2015 proceedings, year present in the prose but not parenthesised) — all legitimate |
| Entries with a DOI or URL | 4 explicit (`[3]`, `[11]`, `[13]` via `doi:`, `[46]` via DOI) — the remaining 44 carry journal/volume/pages instead, which is normal for this journal style |
| Age spread | 1990–2024; the newest entries `[41]` (2021), `[45]`/`[46]` (2023), `[44]` (2021) |
| Self-citations | `[33]`, `[44]`, `[45]`, `[46]` — Prakash/Yadav and co-authors. Four of 48; disclosed rather than flagged |

A journal-style list without DOIs is not a defect. It *is* a limitation on verification (§6).

---

## 4. Citation audit of the body (printed pp. 2–19)

| Metric | Value |
|---|---|
| Citation groups recognised | 45 |
| Distinct numbers cited | 48 |
| Range of cited numbers | 1 – 48 (no citation outside the list) |
| Listed but never cited | none |
| Cited but not listed | none |
| Most-cited entries | `[11]` (Grassl–Rötteler / code tables) ×6, then `[3]`, `[4]`, `[6]`, `[32]`, `[41]` ×3 |

**Conclusion (A): the citation apparatus of the HAL version is internally consistent.** This is a positive finding about the source and is the outcome of a corrected audit, not of the original one.

---

## 5. Bibliographic verification of the cited works

I verified the works that carry weight in the Phase 2 comparison. Status vocabulary: **VERIFIED** = title/authors/venue/volume confirmed against an independent publisher or arXiv record; **CONSISTENT** = matches several independent citing bibliographies but no primary record was opened; **UNVERIFIED** = not checked.

| # | Work | Status | Evidence |
|---|---|---|---|
| 19 | Jitman & Sangwisut, average Hermitian hull of constacyclic codes, *AMC* 12(3):451–463 (2018) | **VERIFIED** | arXiv:1702.00275 record (journal-ref) and the AIMS page for the same authors' 2025 paper |
| 21 | Jitman, Sangwisut, Udomkavanich, *Hulls of cyclic codes over Z₄*, *Discrete Math.* 343(1):111621 (2020) | **VERIFIED** | ScienceDirect `S0012365X19302833` (Jan 2020, art. 111621, three authors, `10.1016/j.disc.2019.111621`), arXiv:1806.07590 |
| 34 | Sangwisut, Jitman, Ling, Udomkavanich, *Hulls of cyclic and negacyclic codes over finite fields*, *FFA* 33:232–257 (2015) | **CONSISTENT** | matches multiple independent citing bibliographies; primary record not opened |
| 36 | Sendrier, *On the dimension of the hull*, *SIAM J. Discrete Math.* 10(2):282–293 (1997) | **CONSISTENT** | as above |
| 40 | Skersys, *The average dimension of the hull of cyclic codes*, *DAM* 128(1):275–292 (2003) | **CONSISTENT** | as above |
| 41 | Shi, Huang, Yue, *AAECC* 32(5):603–620 (2021) | **VERIFIED** | the source paper's own Springer landing page reproduces this reference in its reference list, and an independent 2021 Springer article (`10.1007/s10773-021-04910-0`) cites it identically |
| 11 | Grassl–Rötteler, ISIT 2015, pp. 1104–1108, `doi:10.1109/ISIT.2015.7282626` | **CONSISTENT** | DOI well formed; record not opened |
| 3 | `quantumcodes.info/Z4` (accessed 15/5/23) | **CONSISTENT** | resource exists and is the standard Grassl Z₄ table; URL not re-fetched |
| 6 | Calderbank–Rains–Shor–Sloane, *IEEE TIT* 44:1369–1387 (1998) | **CONSISTENT** | canonical; not re-fetched |
| 30 | Massey, *Discrete Math.* 106/107:337–342 (1992) | **CONSISTENT** | canonical |
| 33 | Prakash, Yadav, Islam, Solé, *Comput. Appl. Math.* 41(6) (2022) | **CONSISTENT** | same authors, same journal family as the source |
| 46 | Yadav & Prakash, LNNS 447:241–249 (2023), `10.1007/978-981-19-1607-6_21` | **CONSISTENT** | DOI well formed |
| 1, 2, 4, 5, 7–10, 12–18, 20, 22–29, 31, 32, 35, 37–39, 42–45, 47, 48 | remaining entries | **UNVERIFIED** | not opened; no claim is made about them |

**No bibliographic error was found in the 12 entries checked.** The one defect found was in my own Phase 2 matrix, not in the paper: the CSV row for `[21]` had dropped Udomkavanich from the author list. **Corrected** in `LITERATURE_COMPARISON_MATRIX.csv` (row now reads `Jitman, Sangwisut, Udomkavanich, … doi 10.1016/j.disc.2019.111621 (2020)`), audit trail = this paragraph.

---

## 6. Limits of this verification — read before quoting it

1. **The version of record was not examined (open item U-8).** All page numbers in this project are *physical* PDF pages of `hal-04825601v1`. The HAL preprint may differ in pagination and, in principle, in referencing from the Springer article. A citation audit of one version says nothing certain about the other.
2. **Only 12 of 48 entries were checked against anything.** "No defect found" means "no defect found among 12", not "the list is correct".
3. **Network access to publisher HTML (Springer, HAL, ScienceDirect bodies) was unavailable and is frozen** by standing instruction; verification relied on search snippets, arXiv records and publisher reference lists. A snippet is weaker evidence than a record.
4. **DOI resolution was not performed** for the 44 entries that print a journal but no DOI.
5. Books and web resources (`[5]` Magma handbook, `[3]`, `[11]`) are not verifiable in the same way as journal articles and were graded `CONSISTENT` at best.

**What would close the gap:** one library visit, or a single authenticated pass through the Springer version of record plus a CrossRef batch lookup for the 48 titles. Until then, this report supports the claim "the apparatus is internally consistent and the twelve load-bearing references are real", and nothing stronger.

---

## 7. Verdict

* **(A) Internal consistency: PASS.** 48/48 cited, 0 orphans, 0 undefined numbers, 0 duplicates. The two earlier flags are **retracted** as extraction artefacts (§1).
* **(B) Bibliographic reality: PASS for the 12 checked works; 36 unchecked.** Nothing in the checked set is fabricated or misattributed.
* **Defects recorded against the source paper: none from this report.**
* **Defect recorded against Phase 2's own output: one** — the `[21]` author list in `LITERATURE_COMPARISON_MATRIX.csv`; fixed, with the trail above.
* **Residual risk.** A reference list that is internally consistent can still cite a work whose content does not support the citing sentence. Checking *that* — the claim-level audit — was Phase 1's job for the source's own theorems; for the 48 cited works it was not attempted and is not claimed.
