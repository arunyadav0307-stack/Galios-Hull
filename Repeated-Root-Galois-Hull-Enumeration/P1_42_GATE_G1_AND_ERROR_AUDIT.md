# P1-42 — Gate G1 Comparison Status and Focused Error-Audit Record

**Date:** 22 October 2026. **Manuscript:** reading copy at `3e4f87f`;
IEEE single-column review version at `6ad0e87` (both compiled; see §4).

## A. Gate G1 — status: DEFERRED (not resolved)

**Access attempt (22 Oct 2026).** The publisher page for Debnath–Prakash–
Islam, *Galois hulls of constacyclic codes over finite fields*, Cryptogr.
Commun. 15(1), 111–127 (2023), doi:10.1007/s12095-022-00591-6, was
re-examined. Only the **abstract and reference list** are lawfully
readable without a subscription ("This is a preview of subscription
content"); the correction (doi:10.1007/s12095-022-00602-6) is known only
to exist (pp. 129–130). A bounded search for a lawful author/institutional
copy found none (ResearchGate listings were not used as a lawful source;
no paywall circumvention was attempted).

**What can and cannot be compared.** From the publisher abstract alone,
L1 (i) gives "a formula for the dimension of Galois hulls of constacyclic
codes" by arranging the irreducible factors of \(x^n-\lambda\) over
\(\mathbb{F}_q\), and (ii) under "some restrictions on \(q\)" calculates
"the number of constacyclic codes of length \(n\) over \(\mathbb{F}_q\)
for a given Galois hull dimension". Theorem numbers, hypotheses (in
particular whether \(p\mid n\) / repeated roots are allowed), counting
objects, and formulas of L1 are **not** available, so no theorem-level
comparison is possible. The comparison below is therefore limited to
abstract-level scope; it establishes neither overlap nor non-overlap.

| Aspect | L1 (2023), abstract-level only | This manuscript (exact locations) |
|---|---|---|
| Setting | constacyclic codes over \(\mathbb{F}_q\) (root multiplicity not stated in abstract) | repeated-root length \(n=Pn_0\), \(P\) a power of \(\mathrm{char}\), finite products of fields, compatible twists (Thm. V.2/5.2) |
| Hull dimension | formula for a given code's Galois hull dimension | hull generator \(\mathrm{lcm}(g_a,h_a^\#)\) and dimension formula (Thm. V.2/5.2) |
| Counting | number of codes with a given Galois hull dimension, under unstated restrictions on \(q\) | joint enumerator \(\prod \mathrm{tr}((T^{(P)}_{w_O})^{L_O})\) for the pair \((\dim C, \dim\mathrm{Hull}_k(C))\) (Thm. VI.3/6.3); LCD/SO/DC specializations (Cors. VII.3–VII.6); moments incl. Var/Cov (Thm. VIII.4, Cor. VIII.5) |
| Proof technique | not available (full text unread) | transfer-matrix traces over reciprocal-involution orbits; predecessor convention fixed by the code-first pairing (Sec. II) |

**Conclusion.** G1 remains **DEFERRED**: resolution requires a lawfully
read full text of L1 and its correction (e.g. interlibrary loan, author
copy via the P1-35 draft, or library subscription). No novelty, priority,
or non-overlap claim is made anywhere in the manuscript, and the
introduction's abstract-level fence around [9], [10] stays as written.

## B. Focused error audit — no confirmed errors found; nothing corrected

The checks below were performed; they corroborate, but (per the task
rule) do not by themselves prove, the manuscript's results.

1. **Existing validators (re-run, all exit 0):**
   `validate_p1_14.py` (orbit-level enumeration vs transfer traces on the
   52-pair \((P,L)\) grid, moment closed forms), `validate_p1_20.py`,
   `validate_code_table.py` (all 10 EAQECC rows: hull dimension both from
   Thm. 5.2 and the code-first Gram matrix; distances independently),
   `validate_audit_fixes.py` (Example 9.4 orientation: \(h^\#\) exponents
   match predecessor 2187/2187 vs successor 27/2187 over \(\mathbb{F}_8\);
   Example 9.6 twist; P = 4, 8, 9 cases).
2. **New independent edge checks** (`code/validate_p1_42_edge_checks.py`,
   output saved alongside): for 48 \((P,L,w)\) cases, fresh enumeration
   of all assignments reproduces (i) the transfer-matrix trace
   distribution (via independent bivariate-polynomial matrix powers),
   (ii) \(\mathbb{E}[\dim C]\), \(\mathbb{E}[\mathrm{Hull}]\)
   (\(\mu_P\), \(\nu_P\) regimes), (iii) \(V_1/V_2/V_{\ge3}\) variances,
   (iv) \(\mathrm{Var}(\dim C)=\frac{P(P+2)}{12}\sum w_f^2\) and
   \(\mathrm{Cov}(\dim C,\dim\mathrm{Hull}_k(C))=0\) of Corollary VIII.5,
   (v) the \(K\leftrightarrow\Delta-K\) symmetry, (vi) LCD count \(2\)
   per orbit, (vii) SO count = DC count. All passed.
3. **Conventions/notation:** predecessor index \(\alpha_{i-1}\) is used
   consistently with the code-first pairing (Definition II.1); hull
   generator exponent \(\max(\alpha_i, P-\alpha_{i-1})\); dimension
   counts are over labeled assignments (scope stated in Sec. X); the
   \(L=1\) vs \(L\ge2\) mean constants \(\nu_P,\mu_P\) are not
   interchanged; Corollary VIII.5 says "uncorrelated", not "independent".
4. **References/citations:** 25 bibliography entries, all cited, no
   unresolved keys in either compiled version (0 undefined references in
   both logs); the seven P1-39 entries were verified against publisher
   records; citation-to-claim wording in the introduction matches what
   those papers establish (mass formulas, one-dimensional hulls,
   double-cyclic hull counts, relative hulls, Galois-hull constructions).
5. **IEEE formatting:** both logs are error-free; the IEEE version is 18
   pages in the required single-column review format (limit 50).

**Mathematical errors: none confirmed in the checks above; none
corrected; none knowingly left unresolved.** This is not a claim that
the manuscript is error-free: the audit is a focused corroboration of
the stated formulas on the grids and cases listed, and Gate G1 (Part A)
is still open.

## C. Version consistency

Reading copy `.tex` `362710c00998…`, IEEE `.tex` (same content under
IEEEtran; conversion commit `6ad0e87`), both PDFs/logs in `compiled/`,
this record, the validators (including the new P1-42 script/output), and
the refreshed package/manifest all correspond to the same manuscript
content; only packaging files changed in P1-42, so the manuscripts were
not recompiled.
