# ENVIRONMENT CAPABILITIES — Phase 0

**Probed:** 2026-10-23 (UTC) · **Host:** `e2b.local`, Linux 6.1.158+, Debian GNU/Linux 12 (bookworm), x86_64
**Resources:** 2 vCPU, 3.8 GiB RAM, 20 GiB free on `/`
**Repository:** `/home/user/Galios-Hull`

Every row is a probe result, not an expectation. "Missing" means the binary or
module was absent from `PATH` / `sys.path` at probe time.

---

## 1. Core toolchain

| Tool | Present? | Version | Consequence for this project |
|---|---|---|---|
| `python3` | **yes** | 3.11.2 | primary computational environment |
| `pip3` | **yes** | 23.0.1 | can install wheels from PyPI (verified, §3) |
| `git` | **yes** | 2.39.5 | local commits, history inspection |
| `gh` | **yes** | 2.23.0 (Debian) | GitHub API access (used to fetch the blueprint PDF) |
| `unzip` / `zip` | **yes** | — | archive integrity checks |
| ImageMagick `convert` | **yes** | — | raster image conversion only; no PDF rendering guarantee |
| **`pdflatex` / `latex` / `bibtex` / `latexmk` / `tectonic`** | **no** | — | **Phase 9 cannot compile `main.tex` here**; ship source + report limitation |
| **`pdftotext` / `pdfinfo` / `qpdf` / `gs`** | **no** | — | PDF text must be extracted with `pypdf`; no independent PDF validator |
| **`magma`** | **no** | — | blueprint Phase 7 CAS cross-check unavailable — must be declared |
| **`sage` / `gap`** | **no** | — | same |

## 2. Python modules

| Module | At probe | Version | Note |
|---|---|---|---|
| `pypdf` | **present** | 6.21.2 | PDF page count, metadata, text extraction |
| `fontTools` | absent → **installed this session** | 4.67.0 | silences CFF/Type1 width warnings in `pypdf` |
| `sympy` | absent → **installed this session** | 1.14.0 | exact polynomial arithmetic, finite-field factoring, symbolic checks |
| `numpy` | absent → **installed this session** | 2.4.6 | array/linear algebra support (dependency of `galois`) |
| `galois` | absent → **installed this session** | 0.4.11 | finite fields $\mathbb F_{p^m}$, polynomials, linear codes — an independent implementation path usable in Phase 7 |
| `scipy`, `pandas`, `matplotlib` | **absent** | — | not required by the blueprint; would need installation |

*Caveat:* `pip install` targets `/usr/lib/python3/dist-packages`, which lies
**outside** the workspace root. These installs exist for the current sandbox
session only; they are **not** captured in the repository snapshot. Any Phase 7
program must therefore either (a) be re-runnable after `pip install -r
code/requirements.txt`, or (b) rely only on files and the standard library.
Records of Phase 7 runs must state whether `galois`/`sympy` were available.

*Probe evidence:* `import galois; galois.GF(9)` constructed $\mathbb F_9$ with
defining polynomial $x^2+2x+2$ (primitive), exit status 0.

## 3. Network reachability (as observed from the sandbox)

| Endpoint | Result | How used |
|---|---|---|
| `api.github.com` | **reachable** | fetched the blueprint PDF through `gh api .../contents` |
| `pypi.org` / `files.pythonhosted.org` | **reachable** | installed `sympy`, `numpy`, `galois`, `fontTools` |
| `raw.githubusercontent.com` | **TLS failure** (`SSL_ERROR_SYSCALL`) | fallback: GitHub contents API |
| `link.springer.com` (direct Python HTTPS) | **TLS failure** | publisher text read only through the page-fetch tool |
| `www.sciencedirect.com` / `doi.org` | indirect only (page-fetch tool) | DOI metadata verification |
| general web search | available through the agent's search tool, not through `curl` | literature work in Phase 2 |

**Consequence:** literature verification in Phase 2 must go through the search and
page-fetch tools; paywalled full texts (Object C, and the version of record of
Object A) cannot be retrieved by this environment.

## 4. What the environment can and cannot support

| Blueprint requirement | Feasible here? | Basis |
|---|---|---|
| Phase 0 inventory, hashing, archive inspection | **yes** | `sha256sum`, `zipfile`, `pypdf` |
| Phase 1 source audit (read full text, extract theorems) | **yes for Object A**; no for Object C (absent) | 27-page searchable text layer |
| Phase 1B recalculation of examples | **yes** | exact arithmetic via `sympy`/`galois` or hand-written `F_q` code |
| Phase 2 literature search, metadata checks | **partly** | open pages reachable; paywalled full texts not |
| Phase 4 factorisation of $x^n-\alpha$ over $\mathbb F_{q^2}$ | **yes** | `galois`/`sympy` plus independent implementation |
| Phase 5 symbolic verification (support, not proof) | **yes** | `sympy` |
| Phase 7 Magma cross-check | **no** | Magma absent; must be reported, not simulated |
| Phase 9 LaTeX → PDF | **no compilation** | no TeX binaries; deliver `.tex` + `.bib` |
| Phase 10 re-run of principal tests | **yes**, when TeX is not involved | deterministic Python |

## 5. Reproducibility notes

* Recorded versions: Python 3.11.2; `pypdf` 6.21.2; `sympy` 1.14.0; `numpy` 2.4.6;
  `galois` 0.4.11; `fontTools` 4.67.0; `git` 2.39.5; `gh` 2.23.0.
* Standard-library-only scripts are preferred where exactness suffices, because
  third-party wheels are session-local.
* No GPU, no parallel build system, no TeX, no CAS beyond the above.
* Wall-clock limits: single commands are capped at 30 min in this harness; long
  computations must be chunked and their outputs stored under `data/`.

## 6. Honest limitation statement (to be carried into Phase 7 and Phase 10)

> Magma, SageMath and GAP were **not available**. Finite-field computations in this
> project are performed by purpose-written Python (standard library, and where
> stated `sympy`/`galois`), and are validated against published numbers and by
> independent re-implementation. No computer-algebra cross-check by an external
> system has been performed.
