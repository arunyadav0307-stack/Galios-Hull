# Changelog: Source-Paper Restyling (Phase 10F → Reference-Style Revision)

Revision of `manuscript/main.tex` (source: `Galios-Hull-Submission-Phase10F.zip`,
`Galios-Hull-kGalois-Phase10F/manuscript/main.tex`) to match the presentation
and organization of the reference coding-theory article, without changing the
source paper's mathematics. See `STYLE_MAPPING.md` for the full mapping and
`CONSISTENCY_CHECK.md` for the preservation audit.

## Structural changes

- **12 sections → 6 sections.** Old §§2–3 merged into §2 Preliminaries
  (§2.1 algebra/decomposition, §2.2 factor selections/global code, §2.3
  pairing/global code); old §§4–5 into §3 Galois Duality and Hull Support
  (§3.1 reciprocal/compatibility, §3.2 duals/convention, §3.3 support/
  boundary); old §§6–9 into §4 Exact Joint Enumeration (§4.1 orbit
  polynomial, §4.2 transfer matrix, §4.3 joint enumerator, §4.4
  consequences); old §10 into §5 Examples and Computational Validation
  (§5.1 worked examples, §5.2 validation record); old §§11–12 into
  §6 Conclusion (summary + scope + future work). No result moved across
  the preliminaries/results boundary except standard CRT/product lemmas,
  which now sit in §2 as in the reference.
- **Result numbering.** Per-section shared counter → global Theorem 1–3,
  Lemma 1–8, Proposition 1–12, Example 1–2 counters with per-section
  Corollary 4.1–4.6, mirroring the reference (global theorems/lemmas,
  section-based corollaries). Descriptive bracket titles kept.
- **Cross-references by number.** Name-based pointers ("the trace
  identity", "the dual-generator theorem", "the injectivity lemma")
  converted to numbered references ("Proposition 12",
  "Theorem 1", "Lemma 2"); 20 key displays numbered (1)–(20) and cited
  as "Equation (n)". Five `\boxed` displays converted to numbered
  equations (reference uses no boxes). Proof-internal algebra stays
  unnumbered.
- **Introduction rewritten** to background → literature → gap →
  motivation → contributions → significance → organization, using only
  the source's 13 references and claims.
- **Two worked examples added** (§5.1, Example 1 F4 pilot, Example 2 F8
  long orbit) in the reference's "Example N. Consider ..." style. Every
  number is quoted from the source validation captures and every
  computation re-verified by hand (see `CONSISTENCY_CHECK.md` §5).
- **Five figure placeholders removed.** They were empty framed boxes
  ("will be prepared after mathematical review") with no data; the
  reference paper has no figures. Referencing sentences rewritten as
  prose. No figure with scientific content was removed.
- **Tables restyled, data identical.** booktabs + caption-below →
  bordered grid + caption-above (Tables 1–4). Cell text, math, numbers,
  and script names byte-identical. One caption fixed ("in the draft" →
  "in this paper").
- **Limitations folded into §6** (reference has no standalone
  limitations section); all scope content kept, including the scope
  table and the N1-exclusion and literature-caveat statements.
- **Bibliography:** `\bibliographystyle{plain}` → `{unsrt}` (citation
  order, as in the reference). `references.bib` content byte-identical;
  all 13 entries still cited.

## Prose and formatting changes

- Abstract rewritten as prose-only (equations moved out; their content
  already appears in the body), following the reference's
  studies/first/then/further cadence.
- Added `Keywords:` + `2020 MSC: 94B05, 94B15, 05A15` block between
  horizontal rules (reference front-matter style). MSC codes are new
  submission metadata (linear codes; cyclic codes; exact enumeration),
  consistent with the package checklist's suggestion; noted here rather
  than asserted as source content.
- Section headings numbered `1.`, `2.1.` (period after number) via a
  three-line `\@seccntformat` addition; references render unchanged.
- Rewrote passive/defensive and internal-jargon phrasing into active
  journal "we" ("frozen maps/convention", "Phase-10C", bare "N1",
  "audit", "deliberately stated") while keeping every conservative
  qualifier (no priority claim, conditional hypotheses, quantum
  disclaimer, non-universal absence claim).
- Equation displays integrated into sentences; duplicate statements
  removed (source §2 prose decomposition display now only Equation (2);
  source §11 compatibility display now cited as Equation (6)).
- One long example histogram wrapped over three lines (`aligned`) so
  the LaTeX build stays overfull-free; content unchanged.
- Author block left empty (`\author{}`) as in the source; no authors,
  affiliations, funding, or declarations invented.

## Files

- Added: `manuscript/main.tex` (revised source), `manuscript/main.typ`
  (Typst port for PDF rendering), `manuscript/main.pdf` (compiled PDF),
  `manuscript/references.bib` (unchanged copy),
  `manuscript/build_pdf_typst.py` (PDF build script),
  `tools/check_manuscript.py`, `tools/check_math_preservation.py`,
  `tools/check_pdf.py` (validators), `STYLE_MAPPING.md`,
  `CHANGELOG.md` (this file), `CONSISTENCY_CHECK.md`, `README.md`.
- Untouched: `Galios-Hull-Submission-Phase10F.zip`,
  `Galios hulls of constacclic codes over affine algebra rings'.pdf`.

## Build-chain note (sandbox limitation, disclosed)

This sandbox provides no TeX engine and no network route to TeX
distributions (apt, CTAN, TinyTeX, GitHub releases/assets, Anaconda all
unreachable; PyPI/npm carry no TeX engine — verified). `main.pdf` was
therefore rendered from `main.typ`, a line-by-line Typst port with
identical text, mathematics, numbering, tables, and bibliography, using
`typst 0.15.0` (0 warnings, 18 pages). The LaTeX source itself was
validated statically instead of by compilation: balanced environments,
all `\ref`/`\eqref`/`\cite` resolved, all labels/citations used, all
commands defined, ASCII-only, `.bib` balanced with required fields
(`tools/check_manuscript.py` PASS), display-math multiset comparison
against the source (`tools/check_math_preservation.py` PASS), and
PDF content-closure plus full page-by-page visual review
(`tools/check_pdf.py` PASS). Rebuilding with
`pdflatex → bibtex → pdflatex ×3` on any TeX Live system is expected
to succeed cleanly; the unsrt bibliography order is [1]–[13] as listed
in `CONSISTENCY_CHECK.md` §6.
