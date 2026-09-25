# Mathematical Consistency Check

Claim under test: the revision changed **presentation only** — no theorem,
lemma, proposition, corollary, definition, proof, equation, parameter,
example datum, table entry, or reference of the source paper was altered,
and no unsupported statement was added.

Source: `Galios-Hull-Submission-Phase10F.zip`
(`Galios-Hull-kGalois-Phase10F/manuscript/main.tex`, 947 lines).
Revision: `manuscript/main.tex` (+ `references.bib`, byte-identical).

## 1. Automated checks (all PASS)

| Check | Tool | Result |
|---|---|---|
| Environments balanced (96 `\begin`) | `tools/check_manuscript.py` | PASS |
| 62 labels each defined once; 60 `\ref` + 17 `\eqref` all resolve | same | PASS |
| 13/13 `.bib` entries cited; every `\cite` key exists | same | PASS |
| `$`, `\[...\]`, `\(...\)` balanced; all commands defined; ASCII-only | same | PASS |
| No figure placeholders, `\boxed`, or internal jargon | same | PASS |
| `.bib` braces balanced; article/journal/author/title/year present | same | PASS |
| Display-math multiset vs source (see §3) | `tools/check_math_preservation.py` | PASS |
| PDF closure: all headings/numbers/refs/citations resolve; 18 pp. | `tools/check_pdf.py` | PASS |

`check_manuscript.py` emits 4 benign warnings for labels on terminal
corollary displays (`eq:code-dist`, `eq:lcd`, `eq:mean`, `eq:var`) that
are displayed but never cross-referenced; their corollaries are
referenced. LaTeX never warns on these.

## 2. Result-by-result inventory (29/29 preserved)

Old = source section/number; New = revised number. "Same" = statement
and proof logically identical (only numbering, equation environment,
and connective prose changed).

| # | Old | New | Title | Status |
|---|---|---|---|---|
| 1 | §2 Prop | Prop 2 | Code-first dual translation | Same |
| 2 | §3 Prop | Prop 1 | Square-free component decomposition | Same |
| 3 | §3 Lem | Lem 1 | Factor-selection parametrization | Same |
| 4 | §3 Lem | Lem 2 | Global CRT ambient module and factor-selection code | Same |
| 5 | §3 Lem | Lem 3 | Global Frobenius and code-first pairing | Same |
| 6 | §3 Lem | Lem 4 | Global code-first dual decomposition | Same |
| 7 | §3 Lem | Lem 5 | Global hull decomposition | Same |
| 8 | §3 Prop | Prop 3 | Global F_q-dimension additivity | Same |
| 9 | §4 Lem | Lem 6 | Normalized inverse-Frobenius reciprocal | Same |
| 10 | §4 Lem | Lem 7 | Root action | Same |
| 11 | §4 Prop | Prop 4 | Compatible factor permutation | Same |
| 12 | §4 Lem | Lem 8 | Ordinary constacyclic reciprocal | Same |
| 13 | §4 Thm | Thm 1 | Code-first dual generator | Same |
| 14 | §4 Prop | Prop 5 | Same-twist compatibility criterion | Same |
| 15 | §4 Prop | Prop 6 | Candidate-first/code-first convention transformation | Same |
| 16 | §4 Prop | Prop 7 | Same-code hull-dimension and LCD invariance | Same |
| 17 | §5 Thm | Thm 2 | Component hull support | Same |
| 18 | §5 Prop | Prop 8 | Weighted cyclic boundary statistic | Same |
| 19 | §5 Prop | Prop 9 | Cyclic boundary interpretation | Same |
| 20 | §6 Prop | Prop 10 | One-orbit polynomial | Same |
| 21 | §7 Prop | Prop 11 | Weighted transfer matrix | Same |
| 22 | §7 Prop | Prop 12 | Local trace identity | Same |
| 23 | §8 Thm | Thm 3 | Exact labeled joint enumerator | Same |
| 24 | §9 Cor | Cor 4.1 | (total count, untitled) | Same |
| 25 | §9 Cor | Cor 4.2 | Code-dimension distribution | Same |
| 26 | §9 Cor | Cor 4.3 | Hull-dimension distribution | Same |
| 27 | §9 Cor | Cor 4.4 | LCD count | Same |
| 28 | §9 Cor | Cor 4.5 | Mean hull dimension | Same |
| 29 | §9 Cor | Cor 4.6 | Variance of hull dimension | Same |

Proofs: all 29 kept with identical logical steps; only citation forms
changed ("the trace identity" → "Proposition 12"). ProseLead-ins added
(e.g., §4.2 opener) contain no new claims.

## 3. Displayed-equation inventory (79 → 80)

Multiset comparison after whitespace normalization and `\boxed`
unwrapping:
- **Removed (4), all allowlisted:** the 2 abstract display blocks
  (pairing; enumerator+matrix — abstract is now prose-only; both appear
  identically in the body as Equation (4) and Equations (12)/(15));
  the §11 compatibility display (duplicated §4; now cited as
  Equation (6)); the §2 prose decomposition display (duplicated the
  proposition; now Equation (2)).
- **Added (5), all in §5.1 worked examples:** F4 factorization;
  `(u+1)(1+u^4+2u^2z^2)` expansion; `(4+4z^2)^4` expansion;
  `2P_{6,1}(z)` expansion; F8 joint histogram. Each verified in §5.
- **All other 75 displays byte-identical** up to the `\[...\]` →
  `equation` environment change (20 numbered).

## 4. Tables, notation, references

- Tables 1–4: every cell (text, math, numbers, script names) identical
  to source `tab:literature`, `tab:notation`, `tab:computations`,
  `tab:scope`; only rules (`\hline` grid) and caption position changed.
- Notation macros (`\F \A \Fs \Os \Epoly \Hull \rank \CF
  \Candidate \perpE` etc.): definitions unchanged; no symbol redefined
  or silently altered; no reference-paper notation imported.
- References: `references.bib` byte-identical (13 entries); all 13
  cited at least once. unsrt order in the revised text: [1]
  sangwisut2015, [2] debnathConstacyclic2023, [3] debnathCorrection2023,
  [4] debnathAverage2025, [5] debnathSmall2026, [6] talbi2021,
  [7] jitmanZ4, [8] pathakZ4, [9] gao2023, [10] aliabadi2026,
  [11] zhang2026, [12] debnathAffinePreprint, [13] debnathAffine2026.
  2026-09-26 expansion: the 13 original entries are unchanged and 17
  independently verified entries were added (30 total, all cited). New
  unsrt order: [1] massey1992, [2] sendrier2004, [3] sendrier1997,
  [4] brun2006, [5] wildeBrun2008, [6] fanZhang2017,
  [7] huffmanPless2003, [8] sangwisut2015, [9] yangMassey1994,
  [10] debnathConstacyclic2023, [11] debnathCorrection2023,
  [12] liuPan2020, [13] fuLiu2022, [14] debnathAverage2025,
  [15] debnathSmall2026, [16] skersys2003, [17] jitmanSangwisut2018,
  [18] cao2020, [19] dinhLopezPermouth2004, [20] nortonSalagean2000,
  [21] talbi2021, [22] jitmanZ4, [23] pathakZ4, [24] gao2023,
  [25] aliabadi2026, [26] zhang2026, [27] dinh2010,
  [28] debnathAffinePreprint, [29] debnathAffine2026,
  [30] vanLintWilson2001.
- Placeholders removed (5 figures) carried no data; nothing scientific
  deleted. The notation-table caption "in the draft" → "in this paper"
  is the only table-text fix.

## 5. New worked examples: data provenance (no fabrication)

Every number below is quoted from the source validation captures
(`validation/phase2_*.out`, `phase10c_full_validation.out`) and every
"recorded X equals formula Y" claim was re-derived by hand:

- **Example 1 (F4 pilot):** parameters, `8^4=4096`, factorization
  `x^5-1=(x+1)(x^2+ax+1)(x^2+(a+1)x+1)`, fixed-linear/swapped-quadratics
  action, component joint histogram
  `{(0,0):1,(1,0):1,(2,2):2,(3,2):2,(4,0):1,(5,0):1}`, ring hull
  histogram `{0:256,2:1024,4:1536,6:1024,8:256}`, 65 joint terms — all
  recorded. Hand checks: orbits `[1,2]` with weights `1,2` give
  `(u+1)(1+u^4+2u^2z^2)` expanding exactly to the recorded histogram;
  `(4+4z^2)^4` expands exactly to the recorded ring histogram; LCD
  counts 4/component and 256/ring match Corollary 4.4 and the
  histograms' zero entries.
- **Example 2 (F8 long orbit):** parameters, `2^7=128`, orbit lengths
  `[1,6]`, joint histogram (16 terms, sums to 128), hull histogram
  `{0:4,1:60,2:60,3:4}` — all recorded. Hand checks: 7 factors of
  total degree 7 are linear, so weights are all 1;
  `2P_{6,1}(z)=2(2+30z+30z^2+2z^3)=4+60z+60z^2+4z^3` matches the
  recorded hull histogram; 4 LCD selections match Corollary 4.4;
  transfer agreement is the capture's recorded `True`.
- **§5.2 global-product sentence:** recorded uniform mean 3.0 and
  variance 2.0 from the capture; hand check against Corollaries 4.5–4.6
  with the recorded orbit data (lengths 2,4; weights 2,2):
  `(2·2+4·2)/4=3`, `2²/4+4·2²/16=2`. ✓
- The "73 rank-two planes in F_8^3" sentence is the source's own,
  kept verbatim in content.

## 6. Claims and qualifiers preserved

Kept verbatim in meaning: no priority claim; results conditional on
stated hypotheses; candidate-first/code-first duals and hull subspaces
not generally equal (Gram argument gives dimensions/LCD only); labeled
(not equivalence-class) enumeration; repeated roots excluded;
incompatible twists diagnostic-only; no quantum distance/parameter/
optimality/fault-tolerance conclusion from the enumerator alone;
conservative literature comparison (preprint vs publisher records
distinct; corrected finite-field text unchecked; non-universal absence
statement); underspecified N1 artifact excluded. New metadata only:
MSC line (see CHANGELOG) and section/equation numbers.

## Verdict

No source-paper theorem, lemma, proposition, corollary, proof,
equation, parameter, table entry, or reference was altered in
mathematical content; no unsupported claim, datum, or citation was
introduced. The revision is presentation-only. ✔
