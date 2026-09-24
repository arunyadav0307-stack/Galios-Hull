# Phase 10F — Genuine LaTeX Environment and Current-PDF Blocker Report

**Audit date:** 2026-09-24 (Asia/Calcutta)

**Repository:** `arunyadav0307-stack/Galios-Hull`

**Branch:** `arena/01a0c9d2-galios-hull`

**Required Phase-10F starting commit:** `08ca40cc45a1a8f8eb4e5430a2f03f70a0586254`

## 1. Controlled starting state

The required Phase-10F starting state was restored before this audit. The local branch now points exactly to `08ca40cc45a1a8f8eb4e5430a2f03f70a0586254`, which is also the fetched `origin/arena/01a0c9d2-galios-hull` target. The project files that were initially visible as untracked were compared against that target tree before the reset; the current manuscript and bibliography matched the target blobs.

The starting-state checks were:

```text
git reset --hard 08ca40cc45a1a8f8eb4e5430a2f03f70a0586254
git rev-parse HEAD
08ca40cc45a1a8f8eb4e5430a2f03f70a0586254

manuscript/main.tex blob:       ac894d3070550f17f6e11287bbedc41e6f6bebb7
manuscript/references.bib blob: 894cb0fcd024f8935261051c68c7891482a69f0b
```

No Phase-10C, Phase-10D, or Phase-10E artifact was deleted or overwritten. The only file added by this Phase-10F attempt is this blocker report. `manuscript/main.tex` and `manuscript/references.bib` were not modified.

The supplied repository PDF remains a different, older source-paper artifact:

```text
Galios hulls of constacclic codes over affine algebra rings'.pdf
```

It was not treated as a PDF generated from the current manuscript.

## 2. Requested operation and decision rule

The requested operation was to obtain a genuine LaTeX environment, compile the current pair

```text
manuscript/main.tex
manuscript/references.bib
```

process the bibliography, and inspect the generated current PDF page by page. A compiler, bibliography run, PDF, or visual inspection is not inferred from source checks or from the older supplied PDF. The audit therefore attempted both system provisioning and a user-local genuine alternative before stopping.

## 3. Operating system, identity, and administrator checks

Exact environment probes:

```text
cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"

uname -a
Linux e2b.local 6.1.158+ #1 SMP PREEMPT_DYNAMIC Mon May 11 18:48:24 UTC 2026 x86_64 GNU/Linux

id
uid=1001(user) gid=1001(user) groups=1001(user),27(sudo),100(users)

python3 --version
Python 3.11.2

apt-get --version | head -1
apt 2.6.1 (amd64)

sudo --version | head -1
Sudo version 1.9.13p3
```

The current user is not root, but passwordless sudo was available for this audit. The checks `sudo -n id -u` and `sudo -n -l` returned root (`0`) and the permitted `NOPASSWD: ALL` rules. No password or credential was requested or stored. Administrator access alone did not solve the provisioning problem because the package indexes and external binary downloads were unavailable.

## 4. Existing compiler, bibliography, and package-manager checks

The complete executable probe was:

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

Result:

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

The filesystem search also found no executable `pdflatex`, `bibtex`, `tectonic`, `xelatex`, `lualatex`, or `latexmk` under `/usr`, `/opt`, `/root`, or `/home`. The installed-package probe was:

```sh
dpkg-query -W -f='${binary:Package}\t${Version}\n' | \
  grep -Ei 'tex|latex|bib|tectonic|miktex'
```

It returned no matching installed TeX, BibTeX, Biber, MiKTeX, or Tectonic package.

Package managers and environment managers were checked as follows:

```text
apt       /usr/bin/apt
apt-get   /usr/bin/apt-get
dpkg      /usr/bin/dpkg
pip       /usr/bin/pip
npm       /usr/local/bin/npm

snap      unavailable
flatpak   unavailable
brew      unavailable
nix       unavailable
guix      unavailable
apk       unavailable
yum       unavailable
dnf       unavailable
pacman    unavailable
conda     unavailable
mamba     unavailable
micromamba unavailable
pipx      unavailable
```

The requested named distributions and tools were therefore specifically checked: TeX Live executables and `tlmgr`, TinyTeX, MiKTeX, Tectonic, Conda/Mamba, and the standard LaTeX/BibTeX/Biber/latexmk engines were not present.

## 5. System installation attempt

Because `apt-get` and passwordless sudo were available, a genuine minimal system installation was attempted rather than assuming that installation was impossible. The exact commands and results were:

```sh
sudo -n apt-get update
```

The command returned status `0` but every configured Debian index fetch failed:

```text
Ign:1 http://deb.debian.org/debian bookworm InRelease
Ign:2 http://deb.debian.org/debian bookworm-updates InRelease
Ign:3 http://deb.debian.org/debian-security bookworm-security InRelease
Err:1 http://deb.debian.org/debian bookworm InRelease
  Connection failed [IP: 151.101.194.132 80]
Err:2 http://deb.debian.org/debian bookworm-updates InRelease
  Connection failed [IP: 151.101.2.132 80]
Err:3 http://deb.debian.org/debian-security bookworm-security InRelease
  Connection failed [IP: 151.101.194.132 80]
W: Failed to fetch all configured Debian indexes; old indexes were used or none were available.
```

The package-index query then produced no candidate package metadata:

```sh
apt-cache policy texlive-latex-base texlive-latex-recommended \
  texlive-fonts-recommended lmodern latexmk tectonic
```

The exact minimal installation command was:

```sh
sudo -n apt-get install -y --no-install-recommends \
  texlive-latex-base texlive-latex-recommended \
  texlive-fonts-recommended lmodern
```

It returned status `100`:

```text
E: Unable to locate package texlive-latex-base
E: Unable to locate package texlive-latex-recommended
E: Unable to locate package texlive-fonts-recommended
E: Unable to locate package lmodern
```

Thus administrator access existed, but no usable Debian package index or package payload was available. Alternate Debian mirror probes also failed: HTTP requests returned an empty reply and HTTPS requests failed with `OpenSSL SSL_connect: SSL_ERROR_SYSCALL`.

## 6. Container, namespace, and alternative-environment checks

The exact runtime probe was:

```sh
for c in docker podman nerdctl containerd ctr crun runc singularity \
         apptainer systemd-nspawn chroot unshare; do
    printf '%-18s' "$c"
    command -v "$c" || echo unavailable
done
unshare -Ur true
```

Results:

```text
docker            unavailable
podman            unavailable
nerdctl           unavailable
containerd        unavailable
ctr               unavailable
crun              unavailable
runc              unavailable
singularity       unavailable
apptainer         unavailable
systemd-nspawn    unavailable
chroot            unavailable
unshare           /usr/bin/unshare
unshare_userns_exit=0
```

A user namespace is not a container image or a LaTeX environment. No Docker, Podman, Singularity, Apptainer, rootless image store, or prebuilt TeX image was available to execute. Consequently, there was no genuine container route in which to mount the current repository and compile it.

## 7. User-local Tectonic provisioning attempt

A user-local Tectonic binary was considered as a genuine alternative to TeX Live. The GitHub release API was reachable and identified the current release metadata as `tectonic@0.17.0`, including the asset for `x86_64-unknown-linux-gnu`. The exact asset download was attempted using:

```sh
curl -fL --max-time 180 --retry 2 \
  'https://github.com/tectonic-typesetting/tectonic/releases/download/tectonic%400.17.0/tectonic-0.17.0-x86_64-unknown-linux-gnu.tar.gz' \
  -o /tmp/phase10f-tools/tectonic.tar.gz
```

GitHub redirected the binary payload to `release-assets.githubusercontent.com`; the download failed before any file was written:

```text
curl: (35) OpenSSL SSL_connect: SSL_ERROR_SYSCALL in connection to release-assets.githubusercontent.com:443
```

The same genuine release download was also attempted with the configured GitHub CLI:

```sh
gh release download tectonic@0.17.0 \
  -R tectonic-typesetting/tectonic \
  -p 'tectonic-0.17.0-x86_64-unknown-linux-gnu.tar.gz' \
  -D /tmp/phase10f-tools
```

It failed with:

```text
Get "https://release-assets.githubusercontent.com/...": EOF
```

No Tectonic executable was installed. A CTAN bootstrap was also not substituted with a fake or partial package: probes to `mirror.ctan.org`, `ctan.org`, and other ordinary binary/package mirrors failed with the same outbound TLS failure. The Tectonic source could not be made into a reproducible compiler in this environment because no Rust toolchain was installed, and no release binary or TeX package payload could be downloaded.

## 8. Compilation and bibliography result

No genuine compiler was successfully provisioned or executed. In particular, none of the following commands was run against the manuscript because the corresponding executable was unavailable:

```text
pdflatex manuscript/main.tex
bibtex main
pdflatex manuscript/main.tex
pdflatex manuscript/main.tex

# or
latexmk -pdf manuscript/main.tex

# or a successfully provisioned genuine Tectonic command
tectonic manuscript/main.tex
```

Therefore:

- no LaTeX compiler version exists to report;
- no BibTeX or Biber version exists to report;
- BibTeX/Biber was not executed;
- no `.aux`, `.bbl`, `.blg`, `.log`, `.fls`, `.fdb_latexmk`, or compiler output was generated by this attempt;
- no partial or stale build was accepted as a result;
- no mathematical contradiction was discovered by compilation, because compilation did not occur.

The existing Phase-10E source-level bibliography audit remains the applicable static evidence: 13 entries, 13 cited keys, no duplicate BibTeX keys, balanced BibTeX braces, all cited keys present, and all entries cited. Those checks are not a substitute for executing BibTeX/Biber or for inspecting rendered references.

## 9. PDF generation and visual inspection result

```text
Current PDF generated from manuscript/main.tex: NO
Current PDF inspected page by page: NO
```

The only repository PDF is the older supplied source-paper artifact named above. It has a different provenance and was deliberately not used to claim compilation, bibliography processing, current-PDF generation, or visual inspection. No PDF was fabricated, copied, renamed, or presented as current.

Because there is no current generated PDF, the following remain unmeasured rather than reported as zero:

- page count and page-by-page visual appearance;
- equation and theorem rendering;
- table widths, alignment, and float placement;
- figure-placeholder dimensions and placement;
- font/encoding behavior;
- overfull and underfull boxes;
- package, float, font, and bibliography warnings;
- final reference typography and hyperlinks.

## 10. Preserved static manuscript and bibliography checks

No source correction was made during Phase 10F. The prior Phase-10D and Phase-10E audits remain preserved and report the following source-level results for the current manuscript:

- environments and braces are balanced;
- 15 internal labels and 16 reference occurrences resolve without duplicate or unreferenced labels;
- all citation keys resolve statically, with 13 entries and no duplicate keys;
- exactly four manuscript data tables are present: literature comparison, notation and assumptions, computational validation, and scope boundaries;
- exactly five intended figure placeholders are present: workflow, square-free decomposition, factor orbit and hull support, transfer matrix, and local-to-global enumerator;
- no external figure file is required;
- package/environment declarations are statically balanced;
- forbidden priority and overclaim language was not introduced;
- N1 was not reconstructed or turned into a numerical manuscript case.

These are source-level checks only. They do not claim successful LaTeX, BibTeX, PDF, or visual execution.

## 11. Frozen Phase-10C global validation record

The Phase-10C mathematics and evidence were not changed. The exact global-product validation record remains in `validation/phase10c_full_validation.out` and `validation/PHASE10C_GLOBAL_PRODUCT_REPAIR_AUDIT.md`:

```text
256 selections
256 canonical global code spaces
256 global dual checks
256 global dimension/hull checks
1280 affine-product shift checks
all three histogram equalities
uniform mean 3
uniform variance 2
```

More explicitly, the three histogram equalities are:

1. direct global histogram equals the component-product histogram;
2. direct global histogram equals the orbit-boundary histogram;
3. orbit-boundary histogram equals the transfer histogram.

The manuscript's Section 10 computational-validation table retains the global product bridge with `2^3 * 2^5 = 256` selections and the direct product dual/hull, dimension-additivity, orbit, and transfer scope. The complete exact counts above remain in the preserved Phase-10C capture; no validation number was changed or inferred during this blocker audit.

## 12. Mathematical freeze and N1

The following remain frozen and were not redesigned:

- global algebra/module/code/pairing/dual/hull/dimension decomposition;
- inverse-Frobenius reciprocal and code-first convention;
- hull support, orbit and transfer formulas;
- global enumerator, moments, and uniform measure;
- Theorem 8.1 and its dependency chain;
- Phase-10C validation outputs and literature-gap wording;
- Phase-9 manuscript architecture.

N1 remains exactly:

```text
UNSPECIFIED — CANNOT VALIDATE
```

Only the known metadata `q=16`, `n=15`, and `32768=2^15` remain acknowledged in the prior evidence. No missing twist, factorization, orbit structure, histogram, or numerical result was reconstructed or implied.

## 13. Errors, warnings, and remaining issues

### Environment errors

1. No TeX engine or bibliography engine was installed.
2. Debian package-index downloads failed with connection errors, so the minimal TeX Live installation could not resolve packages.
3. GitHub release asset and CTAN binary/package downloads failed at outbound TLS/asset endpoints.
4. No Docker/Podman/container runtime or prebuilt LaTeX image was available.

### Compiler warnings and errors

No compiler or bibliography log exists. Therefore warning/error counts cannot be classified. They remain unverified, not zero.

### Remaining issues

1. Run a genuine LaTeX engine and BibTeX/Biber against the unchanged current manuscript and bibliography in an environment with the required packages.
2. Confirm the complete build is fresh and non-stale, and retain the compiler and bibliography logs.
3. Inspect the resulting current PDF page by page.
4. Classify overfull/underfull boxes, package and float warnings, bibliography rendering, table/placeholder placement, and any genuine source errors.
5. Perform the final authoritative publisher-metadata check for the already recorded abbreviated neighboring-literature author fields.

No mathematical issue was discovered. No source correction is requested by this environment-blocked result.

## 14. Final verdict

**ACTUAL LATEX COMPILATION CANNOT BE EXECUTED IN THE AVAILABLE ARENA ENVIRONMENT.**
