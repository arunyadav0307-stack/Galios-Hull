# ENVIRONMENT_CAPABILITIES

Probed on 2026-10-20 (UTC) by direct execution, not assumed from documentation.
Blueprint §0 requires this to be recorded *before* any work starts.

## 1. What exists

| Capability | Status | Version / evidence |
|---|---|---|
| Python 3 | **available** | 3.11.2 (main, Apr 8 2026) `[GCC 12.2.0]` |
| `pypdf` | **available** | 6.21.1 (installed via `pip --break-system-packages`) |
| `unzip` | available | `/usr/bin/unzip` |
| `git` | available | 2.39.5 |
| `gh` | available | 2.23.0 |
| Disk | 20 GB free | `df -h /home/user` |

## 2. What does **not** exist (important negative results)

| Capability | Status | Consequence for this project |
|---|---|---|
| **Magma** | **absent** | Blueprint §7 says "use Magma if it is genuinely available … If Magma is unavailable, state this explicitly." Stated: **unavailable**. No Magma output is claimed anywhere. |
| **SageMath** | **absent** | No Sage finite-field or code objects used. |
| **GAP** | **absent** | No group/Burnside computation was run in GAP. |
| **LaTeX / pdflatex / latexmk / bibtex** | **absent** | No PDF can be compiled here. Blueprint §9: "If no PDF compiler is available, report the limitation and provide the LaTeX source package." Reported. *(The prior package's `main.pdf` was produced elsewhere, in a different environment; it is not a product of this audit.)* |
| `sympy`, `numpy`, `galois` | **absent** | Not used. All arithmetic is hand-written exact integer arithmetic. |

## 3. What was built instead

Because no computer-algebra system was available, a dependency-free exact
library was written and validated against the source paper's own published
numbers:

`code/gf.py` — `GF(p,m)` arithmetic with arbitrary monic irreducible modulus;
polynomial arithmetic; irreducibility testing; square-free decomposition and
Cantor–Zassenhaus factorization; row reduction; nullspace; `k`-Galois hull
dimension; exact minimum distance by parity-check column dependence.

`code/verify_examples.py` — recomputes Examples 2 and 3 end to end.

`code/verify_corollary_3_5.py` — brute-force attainable hull-dimension sets and
the product factorization test.

**Validation of the library itself:** it reproduces, without being told them, the
paper's factorizations of `x^7−1`, `x^7−ω^2`, `x^13−1`, `x^13−ω^8`; both stated
hull dimensions (0 and 2); both stated Gray-image parameters (`[14,10,4]_9`,
`[26,22,4]_25`) with exact minimum distances; and both stated EAQECC parameter
sets. That is a strong end-to-end check of the tool, since a bug would have to
conspire to reproduce four independent published numbers.

## 4. Reproducibility

All scripts are deterministic. The only randomness (Cantor–Zassenhaus splitting)
is seeded with a fixed constant `12345` inside `gf.split_equal_degree`.
Raw outputs with timestamps are in `verification/`.

```
$ cd research_project/code
$ python3 verify_examples.py        > ../verification/verify_examples.out
$ python3 verify_corollary_3_5.py   > ../verification/verify_corollary_3_5.out
```

Runtime: < 1 s and < 1 s respectively on this machine.

## 5. Limitations that affect the strength of conclusions

1. **No computer-algebra cross-check.** The library was written by the auditor
   and validated only against the paper's own outputs plus internal consistency.
   Mitigation: the checks are exact and the outputs are published numbers, so an
   error would have to be systematic; but an independent CAS re-run is desirable
   before submission.
2. **No LaTeX.** No compilation, no typeset artifact, no page-geometry checks.
3. **Paywalled full texts.** Several closest competitors were verified only at
   abstract/metadata level (see `literature/REFERENCE_VERIFICATION_REPORT.md`).
   This caps the strength of every novelty statement at "documented comparison",
   never "established priority".
4. **Single-version source.** Only arXiv v1 of the source was readable. The
   Discrete Mathematics version of record was not.
