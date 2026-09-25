# Style/Structure Mapping: Reference Paper vs Source Paper

This document records the inspection of both papers and the mapping that guides
the revision. The reference paper is used **only** as a stylistic and structural
model. No result, proof, sentence, or notation specific to the reference paper is
imported; the revised manuscript keeps the source paper's mathematics unchanged.

Source package: `Galios-Hull-Submission-Phase10F.zip`
(`Galios-Hull-kGalois-Phase10F/manuscript/main.tex`, 947 lines, 12 sections).
Reference: `Galios hulls of constacclic codes over affine algebra rings'.pdf`
(arXiv:2412.08512v1, 27 pages, 5 sections, elsarticle preprint layout).

---

## 1. REFERENCE STYLE (to imitate: form, not content)

- **Title/author layout.** Centered title; author names with affiliations;
  corresponding-author footnote with e-mail addresses.
- **Abstract style.** One prose paragraph, no displayed equations; cadence
  "This paper studies ... For this, first, we ... Then, we ... Further, we ...
  Finally, we ...".
- **Keywords + MSC style.** `Keywords:` line followed by a `2020 MSC:` line with
  three codes, set between horizontal rules with the abstract.
- **Introduction structure.** Background (hull concept and applications) →
  literature survey in stages (codes over fields, Galois hulls, codes over
  rings, hulls over rings) → "Motivated by the above works..." (setting and
  main objective) → application/significance paragraph → "This paper is
  organized as follows..." paragraph.
- **Section/subsection hierarchy.** 5 sections: 1. Introduction;
  2. Preliminaries (2.1 alphabet/decomposition, 2.2 pairing, 2.3 codes over the
  ring, 2.4 factorization); 3. Main results (duals, hulls, dimension formula,
  LCD condition, run continuously); 4. Application (4.1 method, 4.2 worked
  examples + table); 5. Conclusion (summary + scope + future work). Headings
  numbered `1.`, `2.1.`, etc. (period after the number).
- **Theorem/proof style.** `amsthm` style: Theorem 1–10 and Lemma 1–9 numbered
  globally across sections; Corollary 3.1–3.5 numbered within the section;
  Example 1–3 and Remark 1–2 numbered globally; every result followed by
  `Proof. ...` ending in a QED box. Results cited by number
  ("from Theorem 8", "From Lemma 5").
- **Notation style.** Standard coding-theory notation introduced in prose as
  needed (`[n,k,d]_q`, hull, LCD); no notation table; no boxed formulas.
- **Equation style.** About ten key displays numbered globally (1), (2), ... and
  cited as "Equation (1)" / "combining Equations (8) and (9)". Proof-internal
  algebra is unnumbered. Displays are integrated into sentences.
- **Example style.** "Example N. Let us consider ..." with fully worked
  parameters, factorizations, and dimension computations applying the paper's
  own theorems.
- **Table style.** A single bordered grid table (`|c|c|...|` with `\hline`),
  caption **above** the table ("Table 1: ...").
- **Conclusion style.** Summary of what was proved, scope remarks, and future
  research directions; no new claims.
- **Bibliography style.** Numbered citations `[1]`, `[23, 24, ...]` in order of
  appearance; reference list in that order ("References" section).
- **Overall language/register.** Active "we" ("we find", "we derive"),
  present tense, standard transitions ("Let ... be ...", "Then ...", "Now, ...",
  "Thus, ...", "Hence, ...").

## 2. SOURCE PAPER (content to preserve exactly)

- **Current structure.** 12 sections: 1 Introduction; 2 Preliminaries;
  3 Decomposition/factor-selection/global module; 4 Component duality;
  5 Hull support/orbits; 6 Orbit enumeration; 7 Transfer matrix; 8 Joint
  enumerator; 9 Consequences (six corollaries); 10 Computational validation;
  11 Limitations; 12 Conclusion. Plus 4 tables and 5 figure *placeholders*
  (empty framed boxes, no scientific content).
- **Mathematical contribution.** Exact labeled joint generating polynomial
  `E(u,z)` for global F_q-code dimension and code-first k-Galois hull dimension
  over a square-free affine algebra, factored over reciprocal factor orbits as
  transfer-matrix traces; with total-count, marginal-distribution, LCD-count,
  mean, and variance specializations.
- **Definitions.** Square-free affine algebra and fixed labeled decomposition;
  simple-root component moduli; labeled factor selections; code-first
  second-slot pairing and hull; global A-valued pairing; inverse-Frobenius
  reciprocal; compatibility condition; reciprocal orbits; boundary statistic;
  one-orbit polynomial; transfer matrix; joint enumerator.
- **Main results.** 3 theorems (dual generator; hull support; joint enumerator),
  8 lemmas, 12 propositions, 6 corollaries, each with a proof (29 proofs).
- **Proofs.** Self-contained; all kept verbatim in logical content.
- **Examples.** No `Example` environments; Section 10 lists finite validation
  cases in a table, with full numeric captures (histograms, factorizations,
  orbit data) in the accompanying validation logs.
- **Computational results.** F4 pilot (4096 selections), F8 long orbit (128),
  F16 extension (32), compatible twist (8), N2-A/N2-B convention cases
  (32/8), global product bridge (256), end-to-end checks incl. 73 planes.
- **Tables/figures.** 4 content tables (literature, notation, computations,
  scope); 5 placeholder figures with no data.
- **References.** 13 BibTeX entries, all cited; kept with identical content.

## 3. TRANSFORMATION PLAN (presentation only)

| Aspect | Source (before) | Revised (after, reference-like) |
|---|---|---|
| Sections | 12 narrow sections | 6 sections: 1 Introduction; 2 Preliminaries (2.1–2.3); 3 Duality/support (3.1–3.3); 4 Enumeration (4.1–4.4); 5 Examples/validation (5.1–5.2); 6 Conclusion |
| Heading numbers | `1`, `2.1` | `1.`, `2.1.` (period, reference style) |
| Result numbering | per-section shared counter | global Theorem/Lemma/Proposition/Example counters; per-section Corollary (4.1–4.6), as in the reference |
| Cross-references | mostly by name ("the trace identity") | by number ("Proposition 12", "Equation (13)") |
| Equations | all unnumbered `\[...\]`, five `\boxed` | 20 key displays numbered (1)–(20); boxes removed; proof algebra stays unnumbered |
| Abstract | contains displayed equations | prose only, first/then/further cadence |
| Keywords/MSC | keywords only | `Keywords:` + added `2020 MSC:` line (new metadata, see changelog) |
| Introduction | question-first, figure pointer | background → literature → gap → motivation → contributions → significance → organization |
| Tables | booktabs, caption below | bordered grid, caption above (Tables 1–4, data identical) |
| Figures | 5 empty placeholders | removed (reference has none; boxes carry no data) |
| Examples | none | Example 1 (F4 pilot), Example 2 (F8 long orbit), using recorded capture data only |
| Validation | Section 10 prose + table | Section 5.2 prose + table (same data) + recorded mean/variance sentence |
| Limitations | separate Section 11 | folded into Section 6 with scope table (same content) |
| Bibliography | `plain` (alphabetical) | `unsrt` (citation order, reference style); `.bib` content unchanged |
| Prose | passive/defensive, jargon ("frozen", "Phase-10C", "N1", "audit") | active journal "we", de-jargonized; all conservative qualifiers kept |
| Preamble | article 11pt, 1in margins | identical, plus section-number periods and new theorem counters |

## 4. NON-NEGOTIABLE GUARDS

1. Every theorem/lemma/proposition/corollary statement and proof keeps its
   mathematical content; only numbering, titles retained, and prose glue change.
2. Every displayed equation keeps its content; only the environment
   (`\[...\]`/`\boxed` → `equation`) changes.
3. All four tables keep their data/captions' meaning; only rule/caption style
   changes.
4. All 13 references keep their content and remain cited.
5. No quantum-code, priority, or literature-absence claim beyond the source's
   own conservative statements.
6. The two new examples use only numbers recorded in the source validation
   captures, combined with the paper's own formulas (hand-verified).
7. The LaTeX must be statically clean: balanced environments, every
   `\ref`/`\eqref`/`\cite` resolved, every label/citation used.
