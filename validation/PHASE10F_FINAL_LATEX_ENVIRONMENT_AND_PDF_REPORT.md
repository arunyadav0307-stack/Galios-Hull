# Phase 10F — Final Genuine LaTeX Environment and Current-PDF Report

**Audit date:** 2026-09-24 (Asia/Calcutta)
**Repository:** `arunyadav0307-stack/Galios-Hull`
**Branch:** `arena/01a0c9d2-galios-hull`
**Required Phase-10F starting commit:** `08ca40cc45a1a8f8eb4e5430a2f03f70a0586254`
**Actual starting HEAD:** `08ca40cc45a1a8f8eb4e5430a2f03f70a0586254`
**Prior environment blocker:** `validation/PHASE10F_ENVIRONMENT_BLOCKER.md` (preserved unchanged as the historical failed-provisioning record)

## 1. Final result at a glance

The earlier Phase-10F environment blocker was overcome with a genuine user-local Tectonic 0.17.0 executable and a cached TeX Live/Tectonic resource set. The current repository source was compiled directly, the bibliography was processed by Tectonic's bundled BibTeX engine, and the resulting current PDF was rendered and inspected page by page.

The final direct build completed with exit status `0` and produced a fresh 19-page PDF. The final log contains no LaTeX errors, fatal stops, undefined citations, or undefined internal references. It does contain non-fatal encoding, hyperref, overfull-box, and underfull-box warnings; these are recorded below and were checked against the rendered pages.

The only source changes made in this final phase were three unambiguous typesetting/source corrections required by the genuine compiler:

1. load `mathrsfs` for the existing `\mathscr` use;
2. keep the Figure 1 `\to` orbit-chain notation in math mode;
3. close the missing inline-math delimiter before `\end{theorem}` near source line 737.

No mathematical statement, convention, validation result, literature claim, N1 status, or Phase-10C evidence was redesigned. No mathematical contradiction was discovered.

## 2. Controlled starting state and preservation

The mandatory starting state was verified before the source corrections:

```text
git rev-parse HEAD
08ca40cc45a1a8f8eb4e5430a2f03f70a0586254

git branch --show-current
arena/01a0c9d2-galios-hull
```

The preceding Phase-10C release commit remains in history:

```text
873f970cc21d8f548d6708e7d73c4e6540119ba2  Repair global affine-product pairing and hull decomposition
```

The following were not deleted, overwritten, or mathematically revised:

- Phase-10C global algebra/module/code/pairing/dual/hull/dimension decomposition;
- the inverse-Frobenius reciprocal and code-first convention;
- hull support, orbit, transfer, global enumerator, moment, and uniform-measure formulas;
- Theorem 8.1 and its dependency chain;
- Phase-10C validation programs and captures;
- Phase-9 architecture and conservative literature-gap wording;
- all earlier Phase-10D, Phase-10E, and validation artifacts;
- `manuscript/references.bib`.

The final source hashes used for the direct build are:

```text
SHA-256  manuscript/main.tex       5a2e1146ecb38bbc761ff3b653f7424b84af1230f54dbcb1e2d2c38ecec7d256
SHA-256  manuscript/references.bib acc788ee15a476e163a4142d8ba081aaa0634543583df07a9afd035d186765cd
```

The current source was compiled directly from `manuscript/main.tex`; the bibliography file was found through the source's `\bibliography{references}` command. A byte-identical source-copy build was used only for diagnosis before the direct clean build.

## 3. Environment and provisioning audit

### 3.1 Operating system and access

The exact checks recorded in the earlier blocker report are retained as the environment audit record for this final audit:

```text
cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"

uname -a
Linux e2b.local 6.1.158+ #1 SMP PREEMPT_DYNAMIC Mon May 11 18:48:24 UTC 2026 x86_64 GNU/Linux

id
uid=1001(user) gid=1001(user) groups=1001(user),27(sudo),100(users)

python3 --version
Python 3.11.2
```

Passwordless administrator access was available (`sudo -n id -u` returned `0`), but it was not needed for the final user-local compiler. No password, token, or other credential was requested or stored.

### 3.2 Requested compiler and bibliography executable checks

The requested executable probe was:

```sh
for c in pdflatex bibtex biber latexmk tectonic xelatex lualatex tex \
         pdftex luatex etex context context-cli; do
    if command -v "$c" >/dev/null 2>&1; then
        printf '%s: %s\n' "$c" "$(command -v "$c")"
        "$c" --version 2>&1 | head -1
    else
        printf '%s: unavailable\n' "$c"
    fi
done
```

Before user-local provisioning, the system-path result was:

```text
pdflatex: unavailable
bibtex: unavailable
biber: unavailable
latexmk: unavailable
tectonic: unavailable
xelatex: unavailable
lualatex: unavailable
tex: unavailable
pdftex: unavailable
luatex: unavailable
etex: unavailable
context: unavailable
context-cli: unavailable
```

After provisioning, the genuine compiler used for this report was:

```text
/tmp/phase10f-tools/tecto-musl/tecto-0.17.0.data/scripts/tectonic --version
Tectonic 0.17.0
```

There is still no separate system `pdflatex`, `bibtex`, `biber`, `latexmk`, `xelatex`, or `lualatex` executable. Tectonic supplies its XeTeX-based LaTeX engine and invokes its bundled BibTeX implementation when the auxiliary file requests it.

### 3.3 Package-manager, distribution, and container checks

The earlier blocker report contains the complete command output. The relevant exact checks and final conclusions are:

```text
apt, apt-get, dpkg, pip, npm: present
snap, flatpak, brew, nix, guix, apk, yum, dnf, pacman: unavailable
conda, mamba, micromamba, pipx: unavailable
docker, podman, nerdctl, containerd, ctr, crun, runc,
singularity, apptainer, systemd-nspawn, chroot: unavailable
unshare: present, but a user namespace is not a container image or TeX installation
```

A genuine system installation was attempted before the user-local fallback:

```sh
sudo -n apt-get update
sudo -n apt-get install -y --no-install-recommends \
  texlive-latex-base texlive-latex-recommended \
  texlive-fonts-recommended lmodern
```

The Debian index fetches failed with connection errors and the install returned status `100` with `Unable to locate package` for each requested TeX package. No system package was substituted or treated as installed. No Docker/Podman/container route was available.

### 3.4 Genuine Tectonic provisioning

The working executable is the static x86-64 musl binary from the `tecto` 0.17.0 wheel. The wheel metadata identifies it as a repackaging of the official upstream Tectonic release binary. The wheel used was:

```text
/tmp/phase10f-tools/wheels/tecto-0.17.0-py3-none-musllinux_1_2_x86_64.whl
SHA-256 830e64c7383e1aed3544f87c07e8ecfb498ebf2b1c1f2b6b95826dd855d3188b
```

The exact extraction fallback used on this glibc host was:

```sh
rm -rf /tmp/phase10f-tools/tecto-musl
python3 -m zipfile -e \
  /tmp/phase10f-tools/wheels/tecto-0.17.0-py3-none-musllinux_1_2_x86_64.whl \
  /tmp/phase10f-tools/tecto-musl
chmod +x /tmp/phase10f-tools/tecto-musl/tecto-0.17.0.data/scripts/tectonic
/tmp/phase10f-tools/tecto-musl/tecto-0.17.0.data/scripts/tectonic --version
```

The wheel tag was not accepted by pip on this host, so the wheel was extracted and its executable bit restored. This did not alter the binary. The executable is not dynamically linked:

```text
ldd .../tectonic
    not a dynamic executable

SHA-256  /tmp/phase10f-tools/tecto-musl/tecto-0.17.0.data/scripts/tectonic
         a98aa59ad5c1df39a6c9e56cbfc5088f2b11d6c179c0130b97998e4bd46a46da
```

Tectonic's current-layout cached resource directory was used with `--only-cached`:

```text
TECTONIC_CACHE_DIR=/tmp/phase10f-tools/current-tectonic-cache
bundle identifier = 6ffe055852f8faf66c0acbe1a7fb27f87b869a90bad1204f3bf4d9683f597c7c
bundle index SHA-256 = e4631b67215b8d3b10e6c079c8f4a3dc03477e0dfdfe7cded68df65860239a9b
```

This is a genuine TeX Live/Tectonic cache assembled from the available package cache, with the required AMS, booktabs, mathtools, `mathrsfs`, RSFS fonts, and standard `plain.bst` resource added where the converted index identified a missing file. It is explicitly **not** claimed to be a pristine independently downloaded bundle. The standard bibliography style used in the build was:

```text
plain.bst SHA-256 19f2cf88686b86aaa8e65d5f0313a92499815761e04b42e84ea2c3dc3685ada9
```

The cache was sufficient for the complete clean build and was never copied into the repository.

## 4. Source corrections required by actual compilation

The first genuine Tectonic passes were allowed to expose source-level failures. The following corrections were made in `manuscript/main.tex`:

1. `\usepackage{mathrsfs}` was added because the existing `\mathscr` definition expanded to an undefined command without it.
2. Figure 1 changed `...\to\tau$-orbits...` to `...\to\tau\text{-orbits}...`, keeping the arrow chain in math mode and the word “orbits” in text mode.
3. The sentence after coefficient extraction changed the final `dimension $H.` to `dimension $H$.`, closing the inline math before `\end{theorem}`.

The third issue was the failure that had remained at `manuscript/main.tex:738`; it was a delimiter error, not a mathematical contradiction. These changes are limited to package/typesetting correctness and do not alter any formula or theorem content.

## 5. Exact clean build and bibliography workflow

Every build directory below was deleted before use. The final authoritative build was run directly against the current repository source, not against the older repository PDF and not against a stale auxiliary directory.

```sh
set -o pipefail
p=/tmp/phase10f-tools/tecto-musl/tecto-0.17.0.data/scripts/tectonic
cache=/tmp/phase10f-tools/current-tectonic-cache
rm -rf /tmp/phase10f-build-direct
mkdir -p /tmp/phase10f-build-direct
TECTONIC_CACHE_DIR="$cache" "$p" \
  --only-cached \
  --keep-intermediates \
  --keep-logs \
  --print \
  -r 2 \
  -o /tmp/phase10f-build-direct \
  manuscript/main.tex \
  2>&1 | tee /tmp/phase10f-build-direct/tectonic_stdout.log
rc=${PIPESTATUS[0]}
printf 'TECTONIC_DIRECT_EXIT=%s\n' "$rc"
```

Observed workflow:

```text
TeX pass 1: source syntax/typesetting completed; first-pass citations/references were naturally unresolved
BibTeX: Running BibTeX on main.aux ...
BibTeX version: 0.99d
TeX rerun 1: bibliography and cross-reference data incorporated
TeX rerun 2: final cross-reference pass
xdvipdfmx: converted final XDV to PDF
TECTONIC_DIRECT_EXIT=0
```

The first pass emitted expected temporary undefined-citation/reference warnings before BibTeX and reruns. The final `main.log` contains no `undefined`, `Undefined`, `LaTeX Error`, `Emergency stop`, or `Fatal` entry. The final `.blg` contains only:

```text
This is BibTeX, Version 0.99d
The top-level auxiliary file: main.aux
The style file: plain.bst
Database file #1: references.bib
```

Final direct-build artifacts and hashes:

```text
main.pdf  159431 bytes  SHA-256 0aa5b73c00cde4c9b7509652d09a6a48674a8fa76bf0831e98c590c9b32ec21c
main.log   26408 bytes  SHA-256 a931d58f92981ffac37a4e13af43f5b7d3a5bc0a4deb163fbea5741e65b7f856
main.aux    8488 bytes  SHA-256 02d4de5d3d8ff2de41571a4a6dae8b454014a78b799672d3a9ebea1040560133
main.bbl    2802 bytes  SHA-256 8d5189682cd9c6b42cc33ce115f687b39456efd910d151477852b6a28d3b481b
main.blg     191 bytes  SHA-256 36a26a35030c17e6a29ed5fa683a298f907726cf9a3af844f8f4d3b56dd6020e
```

No generated build file was added to Git. The old repository PDF was not used as evidence for this result.

## 6. Compilation errors, warnings, and package/environment balance

### 6.1 Errors

The initial source-level failures and their corrections are listed in Section 4. After those corrections:

- final compiler exit status: `0`;
- final fatal LaTeX errors: `0`;
- final undefined citations: `0`;
- final undefined internal references: `0`;
- final BibTeX errors: `0`;
- mathematical contradictions discovered by compilation: none.

### 6.2 Final non-fatal warnings

The final `main.log` reports:

```text
1  inputenc warning:
   inputenc package ignored with utf8 based engines.

2  hyperref warnings at source line 372:
   Token not allowed in a PDF string (Unicode); removing math shift.

8  overfull hbox warnings:
   one long dimension display near source line 719;
   seven lines in the compact computational-validation table near lines 873--881.

35 underfull hbox warnings:
   five compact literature-table lines near lines 81--85;
   twenty-six compact computational-validation-table lines near lines 872--879;
   four compact limitation/scope lines near lines 913--917.
```

The `inputenc` warning is expected under Tectonic's XeTeX-based engine and does not stop compilation. The two hyperref warnings arise from the mathematical `$k$` in the section title; the PDF section text remains present and readable. The box warnings are layout-quality warnings in deliberately compact tables/long displays, not failed output. They were checked during visual inspection; no clipped page content, missing character, or unreadable table was observed. They remain explicit publication-polish items rather than hidden or reclassified as zero.

The final package load was successful for every declared package, including `amsmath`, `amssymb`, `amsthm`, `mathtools`, `mathrsfs`, `booktabs`, `array`, `enumitem`, `geometry`, `hyperref`, and `microtype`. The source has 79 `begin` environments and 79 matching `end` environments, with zero brace imbalance in the manuscript and bibliography.

## 7. Citation, bibliography, reference, and theorem audit

### 7.1 Bibliography

Static and executed checks agree:

```text
BibTeX entries:              13
Unique BibTeX keys:          13
Unique cited keys:           13
Missing cited keys:           0
Uncited bibliography keys:    0
Duplicate BibTeX keys:        0
Final .bbl \bibitem count:   13
```

The final PDF's References section begins on page 18 and continues on page 19. All 13 rendered reference entries are present. No DOI, author, year, title, or literature result was invented during this phase. The abbreviated neighboring-literature author fields retained from the earlier audit remain a publisher-metadata verification item before submission; no missing names were guessed.

### 7.2 Internal labels and references

The current source has 15 unique labels and 16 reference occurrences. The final auxiliary file contains all 15 labels, and the final log contains no undefined-reference warning. The final label placement is:

```text
tab:literature          Table 1, page 2
fig:workflow             Figure 1, page 3
tab:notation             Table 2, page 5
lem:global-code          Lemma 3.3, page 6
lem:global-pairing       Lemma 3.4, page 6
lem:global-dual          Lemma 3.5, page 6
lem:global-hull          Lemma 3.6, page 7
prop:global-dimensions   Proposition 3.7, page 7
fig:decomposition        Figure 2, page 7
fig:orbit                Figure 3, page 11
fig:matrix               Figure 4, page 13
thm:central              Theorem 8.1, page 13
fig:global               Figure 5, page 14
tab:computations         Table 3, page 17
tab:scope                Table 4, page 18
```

### 7.3 Theorem dependency and displayed-equation narrative

The frozen dependency bridge remains explicit and compiles in the intended order:

```text
Proposition 3.1  square-free affine decomposition
  -> Lemma 3.2       component factor selections
  -> Lemma 3.3       global CRT ambient module and code
  -> Lemma 3.4       global Frobenius and code-first pairing
  -> Lemma 3.5       global code-first dual decomposition
  -> Lemma 3.6       global hull decomposition
  -> Proposition 3.7  global F_q dimension additivity
  -> Theorem 5.1     component hull support
  -> Theorem 8.1     global labeled enumerator
  -> Section 9       corollaries
```

The compiled displays for the reciprocal, compatibility condition, global pairing, dual/hull decomposition, orbit polynomial, transfer matrix, global enumerator, coefficient extraction, uniform measure, mean, and variance all appear with their surrounding narrative. No equation-label or `\eqref` failure exists. Compilation verified syntax and cross-reference execution; it does not replace the prior mathematical proof audits.

## 8. Exactly four tables and five intended figure placeholders

### 8.1 Tables

The manuscript contains exactly four data tables; validation reports and dependency artifacts are not manuscript tables:

1. **Table 1, page 2:** literature comparison;
2. **Table 2, page 5:** core notation and assumptions;
3. **Table 3, page 17:** computational validation;
4. **Table 4, page 18:** scope boundaries.

Each has a caption, label, textual callout, and rendered placement. No fifth manuscript data table was created.

### 8.2 Figure placeholders

The manuscript contains exactly five intended placeholders, all rendered as labeled text boxes rather than fabricated scientific figures:

1. **Figure 1, page 3:** workflow;
2. **Figure 2, page 7:** square-free affine decomposition and factor sets;
3. **Figure 3, page 11:** reciprocal factor orbit and hull-support mechanism;
4. **Figure 4, page 13:** two-state transfer matrix;
5. **Figure 5, page 14:** local-to-global enumerator construction.

There is no `\includegraphics` dependency and no external figure file. The placeholders explicitly say that final drawings await mathematical review, as required by the frozen scope.

## 9. PDF generation and page-by-page visual inspection

### 9.1 PDF identity and structural checks

The authoritative PDF was generated at:

```text
/tmp/phase10f-build-direct/main.pdf
```

PyMuPDF 1.28.2 was installed temporarily outside the repository solely for inspection. It reported:

```text
PDF format:          1.5
Creator:             LaTeX with hyperref
Producer:            xdvipdfmx (0.1)
Page count:          19
Page size:           612 x 792 points on every page
Embedded raster images: 0 on every page
```

Each page was rendered at 1.5 scale to a 918 x 1188 PNG. The direct-build renders were byte-identical to the diagnostic renders already inspected. Text-block bounds were checked for every page; all 19 pages had zero text blocks outside the page rectangle.

### 9.2 Page-by-page visual record

The following is the page-by-page inspection record for the current generated PDF:

```text
01  Title, abstract, keywords, and Introduction opening: clean title/abstract layout; equations and citations render; no clipping.
02  Introduction continuation and Table 1: literature table fits; text remains readable; paragraphs and callouts are intact.
03  Figure 1 placeholder and Section 2 opening: boxed workflow is present; headings and displayed preliminaries are intact.
04  Sections 2.3 and 3 opening: pairing, dual, hull, and Proposition 3.1 displays render with proofs and no cutoff.
05  Table 2 and factor-selection preliminaries: notation table is aligned and readable; subsequent equations/prose fit.
06  Section 3.1 global product module/code: global CRT, pairing, and code lemmas render; proof endings are visible.
07  Global hull/dimension material and Figure 2: theorem statements, formulas, and decomposition placeholder are visible and unclipped.
08  Section 4 reciprocal lemmas and compatibility: reciprocal/root-action displays and boxed condition render cleanly.
09  Ordinary reciprocal, Theorem 4.5, and Proposition 4.6: theorem/proof text and transformed-twist formulas are complete.
10  Candidate-first comparison and Section 5 opening: boxed transformation, Gram statement, and hull-support theorem render without clipping.
11  Weighted boundary/orbit propositions and Figure 3: equations, proof endings, and orbit placeholder are present and readable.
12  Section 6 orbit polynomial and Section 7 transfer matrix: boxed polynomial/matrix displays and proofs render correctly.
13  Local trace identity, Figure 4, and beginning of Theorem 8.1: matrix placeholder and theorem opening are intact.
14  Theorem 8.1 continuation, coefficient extraction, Figure 5, and Section 9 opening: global enumerator and placeholder are complete.
15  Code/hull/LCD distributions and uniform measure: corollaries, formulas, and proof endings render cleanly.
16  Mean/variance, Section 10, and Section 11 opening: boxed variance and computational introduction fit; no bottom clipping.
17  Table 3 and Limitations continuation: validation rows wrap within the table; N1 limitation text is visible and complete.
18  Table 4, Conclusion, and References opening: scope table is readable; conclusion and first references render.
19  Remaining references 4–13: all entries are present, readable, and contained within the page.
```

The visual review found no blank page, missing page, clipped equation, missing theorem/proof tail, table overflow into an unreadable region, placeholder loss, or broken bibliography page. The intentional compact-box warnings noted in Section 6 are visible as tight line wrapping but did not make the output unreadable.

## 10. Frozen Phase-10C mathematics and Section 10 validation record

The exact Phase-10C global test remains unchanged and is preserved in `validation/phase10c_full_validation.out`:

```text
256 selections
256 canonical global code spaces
256 global dual checks
256 global dimension/hull checks
1280 shift checks
all three histogram equalities
uniform mean 3
uniform variance 2
```

The three histogram equalities are exactly:

1. direct global histogram equals the component-product histogram;
2. direct global histogram equals the orbit-boundary histogram;
3. orbit-boundary histogram equals the transfer histogram.

Section 10 of the manuscript retains the global-product bridge with `2^3 * 2^5 = 256` selections and the direct dual/hull, dimension-additivity, orbit, and transfer scope. No validation output was recomputed into a different number for this typesetting phase.

The final compilation did not expose a contradiction in the frozen mathematics. This phase therefore does not return the manuscript to Phase 10C.

## 11. Scope limitations and N1

The manuscript remains conditional on square-free, simple-root, compatible-twist, fixed-component, and labeled-factor hypotheses. It continues to exclude repeated roots, incompatible same-factor-set transfer, equivalence-class/Burnside/Pólya enumeration, unrestricted ring families, and unconditional quantum-code performance claims. No firstness, uniqueness, state-of-the-art, universal-absence, or unsupported novelty statement was introduced.

N1 remains exactly:

```text
UNSPECIFIED — CANNOT VALIDATE
```

Only the known metadata `q=16`, `n=15`, and `32768=2^15` are acknowledged in the preserved evidence. No twist, factorization, orbit decomposition, histogram, or numerical result was reconstructed or implied.

## 12. Remaining issues after successful compilation

The environment blocker is resolved, but the following non-fatal publication items remain honestly recorded:

1. The 1 `inputenc`, 2 hyperref, 8 overfull-box, and 35 underfull-box warnings should be considered in a final publisher/typesetting polish pass; they did not prevent or invalidate this build.
2. The five boxes are intentionally placeholders, not final scientific figures; replacing them is outside this frozen mathematical/typesetting audit.
3. Existing abbreviated neighboring-literature author fields still require authoritative publisher-metadata verification before submission.
4. The generated PDF and auxiliary files remain in `/tmp/phase10f-build-direct` rather than Git, consistent with the repository's validation-artifact convention. Their hashes and the exact build command are recorded above.

No unresolved LaTeX error, bibliography failure, undefined reference, source delimiter failure, or mathematical contradiction remains from this audit.

## 13. Final verdict

**FINAL VERDICT: GENUINE TECTONIC 0.17.0 LATEX COMPILATION AND BIBTEX PROCESSING SUCCEEDED; THE FRESH 19-PAGE CURRENT PDF WAS GENERATED AND INSPECTED PAGE BY PAGE; NO MATHEMATICAL CONTRADICTION WAS DISCOVERED.**
