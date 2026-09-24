# Validation Report

This report records the actual clean-environment executions of all six validators. It is computational evidence for the listed finite instances only; it is not a substitute for the general mathematical proofs in `new-paper-blueprint.md`.

## Environment

- Working branch: `arena/01a0c9d2-galios-hull`
- Python: `Python 3.11.2`
- Execution environment: `env -i` with `PYTHONDONTWRITEBYTECODE=1`, empty `PYTHONPATH`, and `LANG=C.UTF-8`/`LC_ALL=C`
- Execution date: 2026-09-24 UTC

## Summary

| Validator | Executed? | Exit code | Result | Purpose |
|---|---:|---:|---|---|
| `code/validate_pilot.py` | Yes | 0 | **PASS** | F4 pilot; factor action, direct dual, component/ring hull enumerators, and orbit polynomial checks. |
| `code/validate_long_orbit_examples.py` | Yes | 0 | **PASS** | F8 orbit-length-6 and F16 extension orbit-length-4 examples; direct duals, orbit boundary, transfer matrix, and histograms. |
| `code/validate_nontrivial_constacyclic.py` | Yes | 0 | **PASS** | Compatible nontrivial lambda=omega example over F4; factorization, direct dual, hull boundary, and transfer comparison. |
| `code/diagnose_incompatible_twist.py` | Yes | 0 | **DIAGNOSTIC ONLY** | F4 k=0 incompatible-twist diagnostic with direct sigma computation and no transfer enumeration. |
| `code/validate_n2_extension_convention.py` | Yes | 0 | **PASS** | N2-A over F16; independent direct/principal/alternative reciprocal comparison for all 32 selections. |
| `code/diagnose_n2_incompatible_twist.py` | Yes | 0 | **PASS — DIAGNOSTIC** | N2-B over F16; sigma/rho distinction, both reciprocal candidates, both candidate twists, original-twist failures, and no transfer enumeration. |

## Interpretation and limitations

- `PASS` means the validator executed with exit code 0 and its assertions completed for its stated finite scope.
- `DIAGNOSTIC ONLY` means the run is intentionally outside the compatible main theorem or cannot resolve the reciprocal convention.
- No validator result is presented as a proof of the general affine-product, reciprocal, factor-permutation, hull-support, orbit-boundary, transfer-matrix, moment, LCD, or quantum claims.
- N1 remains `UNSPECIFIED — CANNOT VALIDATE` because no unique N1 run can be reconstructed from the available parameters; no N1 run is included in this report.

## `validation/validate_pilot.out` — PASS

**Mathematical purpose:** F4 pilot; factor action, direct dual, component/ring hull enumerators, and orbit polynomial checks.

**What this does not prove:** This validates only the listed F4 pilot instance. Because the F4 action is involutory here, it does not resolve the general reciprocal convention.

### Complete captured output

```text
COMMAND: env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 LC_ALL=C PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="" python code/validate_pilot.py
UTC_DATE: 2026-09-24T08:49:24+00:00
PYTHON_VERSION: Python 3.11.2

--- STDOUT ---
F4 pilot parameters: q=4, n=5, lambda=1, k=1
  sigma Frobenius power k: 1
  sigma field exponent p^k: 2
  rho Frobenius power em-k: 1
  rho field exponent p^(em-k): 2
  principal reciprocal Frobenius power: 1
orbit polynomial checks: a=1,...,5 PASS
factorisation: x + 1 * x^2 + (a)x + 1 * x^2 + (a+1)x + 1
Hermitian factor action: fixed linear factor; quadratic factors swapped
direct dual-generator checks: 8 of 8
component joint histogram: {(0, 0): 1, (1, 0): 1, (2, 2): 2, (3, 2): 2, (4, 0): 1, (5, 0): 1}
ring joint histogram terms: 65
ring hull histogram: {0: 256, 2: 1024, 4: 1536, 6: 1024, 8: 256}
PASS: direct hulls, factor action, orbit formula, and enumerator agree

--- STDERR ---

--- EXIT CODE ---
0
```

## `validation/validate_long_orbit_examples.out` — PASS

**Mathematical purpose:** F8 orbit-length-6 and F16 extension orbit-length-4 examples; direct duals, orbit boundary, transfer matrix, and histograms.

**What this does not prove:** These are finite checks only; they do not prove the general orbit or transfer theorem.

### Complete captured output

```text
COMMAND: env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 LC_ALL=C PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="" python code/validate_long_orbit_examples.py
UTC_DATE: 2026-09-24T08:49:24+00:00
PYTHON_VERSION: Python 3.11.2

--- STDOUT ---
Example A (m_s=1, orbit length 6):
  q=8, e=3, m_s=1, k=1, n=7
  sigma Frobenius power k=1; field exponent p^k=2
  rho Frobenius power em-k=2; field exponent p^(em-k)=4
  principal reciprocal Frobenius power=2; direct k=1
  tau permutation on root indices: [0, 3, 6, 2, 5, 1, 4]
  orbit lengths: [1, 6]
  orbit-boundary == transfer: True
  direct dual-generator checks: 128 of 128
  direct == theory: True
  joint histogram: {(0, 0): 1, (1, 0): 1, (1, 1): 6, (2, 1): 12, (2, 2): 9, (3, 1): 12, (3, 2): 21, (3, 3): 2, (4, 1): 12, (4, 2): 21, (4, 3): 2, (5, 1): 12, (5, 2): 9, (6, 0): 1, (6, 1): 6, (7, 0): 1}
  hull histogram: {0: 4, 1: 60, 2: 60, 3: 4}
  PASS
Example B (m_s=2, orbit length 4):
  q=4, e=2, m_s=2, k=1, n=5
  sigma Frobenius power k=1; field exponent p^k=2
  rho Frobenius power em-k=3; field exponent p^(em-k)=8
  principal reciprocal Frobenius power=3; direct k=1
  tau permutation on root indices: [0, 2, 4, 1, 3]
  orbit lengths: [1, 4]
  orbit-boundary == transfer: True
  direct dual-generator checks: 32 of 32
  direct == theory: True
  joint histogram: {(0, 0): 1, (2, 0): 1, (2, 2): 4, (4, 2): 8, (4, 4): 2, (6, 2): 8, (6, 4): 2, (8, 0): 1, (8, 2): 4, (10, 0): 1}
  hull histogram: {0: 4, 2: 24, 4: 4}
  PASS
ALL LONG-ORBIT AND m_s>1 VALIDATIONS PASS

--- STDERR ---

--- EXIT CODE ---
0
```

## `validation/validate_nontrivial_constacyclic.out` — PASS

**Mathematical purpose:** Compatible nontrivial lambda=omega example over F4; factorization, direct dual, hull boundary, and transfer comparison.

**What this does not prove:** This validates one compatible nontrivial-twist instance, not the general compatibility theorem.

### Complete captured output

```text
COMMAND: env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 LC_ALL=C PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="" python code/validate_nontrivial_constacyclic.py
UTC_DATE: 2026-09-24T08:49:48+00:00
PYTHON_VERSION: Python 3.11.2

--- STDOUT ---
nontrivial compatible constacyclic example:
  q=4, n=5, lambda=omega != 1, k=1
  sigma Frobenius power k=1; field exponent p^k=2
  rho Frobenius power em-k=1; field exponent p^(em-k)=2
  factorisation: x + omega+1 * x^2 + x + omega * x^2 + (omega)x + omega
  square-free: True
  lambda^(1+principal field exponent)= 1 = 1
  tau permutation: [0, 2, 1]
  orbit lengths: [1, 2]
  direct dual-generator checks: 8 of 8
  direct == orbit-boundary: True
  orbit-boundary == transfer: True
  joint histogram: {(0, 0): 1, (1, 0): 1, (2, 2): 2, (3, 2): 2, (4, 0): 1, (5, 0): 1}
  hull histogram: {0: 4, 2: 4}
PASS: nontrivial compatible constacyclic validation

--- STDERR ---

--- EXIT CODE ---
0
```

## `validation/diagnose_incompatible_twist.out` — DIAGNOSTIC ONLY

**Mathematical purpose:** F4 k=0 incompatible-twist diagnostic with direct sigma computation and no transfer enumeration.

**What this does not prove:** Sigma and rho coincide on F4 in this case, so it cannot resolve the reciprocal convention or prove the extension-field formula.

### Complete captured output

```text
COMMAND: env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 LC_ALL=C PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="" python code/diagnose_incompatible_twist.py
UTC_DATE: 2026-09-24T08:49:48+00:00
PYTHON_VERSION: Python 3.11.2

--- STDOUT ---
basic incompatible-twist sanity diagnostic only:
  q=4, n=5, lambda=omega, k=0
  sigma Frobenius power k: 0
  sigma field exponent p^k: 1
  rho Frobenius power em-k: 2
  rho field exponent p^(em-k): 4
  sigma == inverse automorphism on F_4: True
  direct dual from defining <c,x>_k: checked
  direct equals principal reciprocal: True
  direct equals p^k reciprocal alternative: True
  lambda^(1+principal field exponent)= 3 != 1
  predicted dual twist lambda^(-principal field exponent)= 3 != lambda
  direct dual is predicted-twist constacyclic: True
  direct dual is original-lambda constacyclic: False
This F4,k=0 example cannot distinguish sigma from rho because both are the identity automorphism on F4.
It validates incompatible-twist behavior, but not the principal Frobenius convention or the general extension-field reciprocal formula.
No transfer-matrix enumeration was attempted because the original and dual constacyclic twists are incompatible.
DIAGNOSTIC ONLY: basic incompatible twist correctly left outside the theorem

--- STDERR ---

--- EXIT CODE ---
0
```

## `validation/validate_n2_extension_convention.out` — PASS

**Mathematical purpose:** N2-A over F16; independent direct/principal/alternative reciprocal comparison for all 32 selections.

**What this does not prove:** This is a finite convention-comparison validation, not a proof of the general reciprocal theorem.

### Complete captured output

```text
COMMAND: env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 LC_ALL=C PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="" python code/validate_n2_extension_convention.py
UTC_DATE: 2026-09-24T08:49:48+00:00
PYTHON_VERSION: Python 3.11.2

--- STDOUT ---
N2-A extension-field convention validation:
  K=F_16=F_(4^2), p=2, q=4, e=2, m_s=2, n=5, lambda=1, k=1
  sigma Frobenius power k: 1
  sigma field exponent p^k: 2
  rho Frobenius power em_s-k: 3
  rho field exponent p^(em_s-k): 8
  principal reciprocal Frobenius power: 3
  alternative reciprocal Frobenius power: 1
  principal reciprocal permutation: [0, 2, 4, 1, 3]
  alternative reciprocal permutation: [0, 3, 1, 4, 2]
  direct dual from defining <c,x>_k equations: 32 of 32
  direct equals principal reciprocal: 32 of 32
  direct equals alternative p^k reciprocal: 8 of 32
  example alternative discrepancies: [2, 3, 4]
PASS: direct dual selects the principal inverse-Frobenius convention

--- STDERR ---

--- EXIT CODE ---
0
```

## `validation/diagnose_n2_incompatible_twist.out` — PASS — DIAGNOSTIC

**Mathematical purpose:** N2-B over F16; sigma/rho distinction, both reciprocal candidates, both candidate twists, original-twist failures, and no transfer enumeration.

**What this does not prove:** This is an incompatible-twist convention-resolution diagnostic outside the compatible same-factor-set transfer theorem.

### Complete captured output

```text
COMMAND: env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 LC_ALL=C PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="" python code/diagnose_n2_incompatible_twist.py
UTC_DATE: 2026-09-24T08:49:53+00:00
PYTHON_VERSION: Python 3.11.2

--- STDOUT ---
N2-B incompatible extension-field convention diagnostic:
  p=2, e=2, m_s=2, q=4, K=F_16=F_(4^2), k=1, n=3
  sigma Frobenius power k: 1
  sigma field exponent p^k: 2
  rho Frobenius power em_s-k: 3
  rho field exponent p^(em_s-k): 8
  sigma and rho differ as automorphisms: True
  lambda=alpha^3 (order 5): 8
  lambda^(1+principal field exponent): 15 != 1
  lambda^(1+alternative field exponent p^k): 10 != 1
  defining-inner-product direct dual checks: 8 of 8
  principal reciprocal direct agreements: 8 of 8
  alternative p^k reciprocal direct agreements: 2 of 8
  example alternative discrepancy mask: 1
  predicted principal dual twist lambda^(-principal field exponent): 12
  predicted alternative dual twist lambda^(-p^k): 10
  direct dual constacyclic under principal predicted twist: 8 of 8
  direct dual constacyclic under alternative predicted twist: 2 of 8
  proper nonzero direct duals failing original lambda twist: 6 of 6
  example original-twist failure mask: 1
No transfer-matrix enumeration was attempted because the original and dual constacyclic twists are incompatible.
PASS: N2-B independently selects the finalized principal convention

--- STDERR ---

--- EXIT CODE ---
0
```

# Phase 2 regression and proof-related validation

This section was added without deleting or rewriting the Phase-1 evidence above. It records reruns after the Phase-2 blueprint/proof-audit edits and compares their mathematical output with the original Phase-1 captures.

## Phase 2 environment and comparison

- Working branch: `arena/01a0c9d2-galios-hull`
- Python: `Python 3.11.2`
- Execution environment: `env -i` with `PYTHONDONTWRITEBYTECODE=1`, empty `PYTHONPATH`, and `LANG=C.UTF-8`/`LC_ALL=C`
- Phase-2 execution date: 2026-09-24 UTC
- Phase-1 evidence: the six original flat captures and the complete report sections above
- Comparison method: stdout between the `--- STDOUT ---` and `--- STDERR ---` markers was compared byte-for-byte; all six existing-validator stdout bodies are identical to Phase 1.

| Phase-2 capture | Exit code | Phase-2 result | Comparison with Phase 1 |
|---|---:|---|---|
| `validation/phase2_validate_pilot.out` | 0 | **PASS** | stdout identical |
| `validation/phase2_validate_long_orbit_examples.out` | 0 | **PASS** | stdout identical |
| `validation/phase2_validate_nontrivial_constacyclic.out` | 0 | **PASS** | stdout identical |
| `validation/phase2_diagnose_incompatible_twist.out` | 0 | **DIAGNOSTIC ONLY** | stdout identical |
| `validation/phase2_validate_n2_extension_convention.out` | 0 | **PASS** | stdout identical |
| `validation/phase2_diagnose_n2_incompatible_twist.out` | 0 | **PASS — DIAGNOSTIC** | stdout identical |
| `validation/phase2_counterexample_search.out` | 0 | no counterexample in tested finite range | new proof-related search |

The existing validators still provide finite evidence only. In particular, the exact F4 `k=0` result remains **DIAGNOSTIC ONLY**, N2-A/N2-B remain unchanged, incompatible twists remain outside the compatible transfer theorem, and N1 has no run.

## Complete Phase-2 capture: `validation/phase2_validate_pilot.out`

```text
COMMAND: env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 LC_ALL=C PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="" python code/validate_pilot.py
UTC_DATE: 2026-09-24T09:01:49+00:00
PYTHON_VERSION: Python 3.11.2

--- STDOUT ---
F4 pilot parameters: q=4, n=5, lambda=1, k=1
  sigma Frobenius power k: 1
  sigma field exponent p^k: 2
  rho Frobenius power em-k: 1
  rho field exponent p^(em-k): 2
  principal reciprocal Frobenius power: 1
orbit polynomial checks: a=1,...,5 PASS
factorisation: x + 1 * x^2 + (a)x + 1 * x^2 + (a+1)x + 1
Hermitian factor action: fixed linear factor; quadratic factors swapped
direct dual-generator checks: 8 of 8
component joint histogram: {(0, 0): 1, (1, 0): 1, (2, 2): 2, (3, 2): 2, (4, 0): 1, (5, 0): 1}
ring joint histogram terms: 65
ring hull histogram: {0: 256, 2: 1024, 4: 1536, 6: 1024, 8: 256}
PASS: direct hulls, factor action, orbit formula, and enumerator agree

--- STDERR ---

--- EXIT CODE ---
0
```

## Complete Phase-2 capture: `validation/phase2_validate_long_orbit_examples.out`

```text
COMMAND: env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 LC_ALL=C PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="" python code/validate_long_orbit_examples.py
UTC_DATE: 2026-09-24T09:01:49+00:00
PYTHON_VERSION: Python 3.11.2

--- STDOUT ---
Example A (m_s=1, orbit length 6):
  q=8, e=3, m_s=1, k=1, n=7
  sigma Frobenius power k=1; field exponent p^k=2
  rho Frobenius power em-k=2; field exponent p^(em-k)=4
  principal reciprocal Frobenius power=2; direct k=1
  tau permutation on root indices: [0, 3, 6, 2, 5, 1, 4]
  orbit lengths: [1, 6]
  orbit-boundary == transfer: True
  direct dual-generator checks: 128 of 128
  direct == theory: True
  joint histogram: {(0, 0): 1, (1, 0): 1, (1, 1): 6, (2, 1): 12, (2, 2): 9, (3, 1): 12, (3, 2): 21, (3, 3): 2, (4, 1): 12, (4, 2): 21, (4, 3): 2, (5, 1): 12, (5, 2): 9, (6, 0): 1, (6, 1): 6, (7, 0): 1}
  hull histogram: {0: 4, 1: 60, 2: 60, 3: 4}
  PASS
Example B (m_s=2, orbit length 4):
  q=4, e=2, m_s=2, k=1, n=5
  sigma Frobenius power k=1; field exponent p^k=2
  rho Frobenius power em-k=3; field exponent p^(em-k)=8
  principal reciprocal Frobenius power=3; direct k=1
  tau permutation on root indices: [0, 2, 4, 1, 3]
  orbit lengths: [1, 4]
  orbit-boundary == transfer: True
  direct dual-generator checks: 32 of 32
  direct == theory: True
  joint histogram: {(0, 0): 1, (2, 0): 1, (2, 2): 4, (4, 2): 8, (4, 4): 2, (6, 2): 8, (6, 4): 2, (8, 0): 1, (8, 2): 4, (10, 0): 1}
  hull histogram: {0: 4, 2: 24, 4: 4}
  PASS
ALL LONG-ORBIT AND m_s>1 VALIDATIONS PASS

--- STDERR ---

--- EXIT CODE ---
0
```

## Complete Phase-2 capture: `validation/phase2_validate_nontrivial_constacyclic.out`

```text
COMMAND: env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 LC_ALL=C PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="" python code/validate_nontrivial_constacyclic.py
UTC_DATE: 2026-09-24T09:02:13+00:00
PYTHON_VERSION: Python 3.11.2

--- STDOUT ---
nontrivial compatible constacyclic example:
  q=4, n=5, lambda=omega != 1, k=1
  sigma Frobenius power k=1; field exponent p^k=2
  rho Frobenius power em-k=1; field exponent p^(em-k)=2
  factorisation: x + omega+1 * x^2 + x + omega * x^2 + (omega)x + omega
  square-free: True
  lambda^(1+principal field exponent)= 1 = 1
  tau permutation: [0, 2, 1]
  orbit lengths: [1, 2]
  direct dual-generator checks: 8 of 8
  direct == orbit-boundary: True
  orbit-boundary == transfer: True
  joint histogram: {(0, 0): 1, (1, 0): 1, (2, 2): 2, (3, 2): 2, (4, 0): 1, (5, 0): 1}
  hull histogram: {0: 4, 2: 4}
PASS: nontrivial compatible constacyclic validation

--- STDERR ---

--- EXIT CODE ---
0
```

## Complete Phase-2 capture: `validation/phase2_diagnose_incompatible_twist.out`

```text
COMMAND: env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 LC_ALL=C PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="" python code/diagnose_incompatible_twist.py
UTC_DATE: 2026-09-24T09:02:13+00:00
PYTHON_VERSION: Python 3.11.2

--- STDOUT ---
basic incompatible-twist sanity diagnostic only:
  q=4, n=5, lambda=omega, k=0
  sigma Frobenius power k: 0
  sigma field exponent p^k: 1
  rho Frobenius power em-k: 2
  rho field exponent p^(em-k): 4
  sigma == inverse automorphism on F_4: True
  direct dual from defining <c,x>_k: checked
  direct equals principal reciprocal: True
  direct equals p^k reciprocal alternative: True
  lambda^(1+principal field exponent)= 3 != 1
  predicted dual twist lambda^(-principal field exponent)= 3 != lambda
  direct dual is predicted-twist constacyclic: True
  direct dual is original-lambda constacyclic: False
This F4,k=0 example cannot distinguish sigma from rho because both are the identity automorphism on F4.
It validates incompatible-twist behavior, but not the principal Frobenius convention or the general extension-field reciprocal formula.
No transfer-matrix enumeration was attempted because the original and dual constacyclic twists are incompatible.
DIAGNOSTIC ONLY: basic incompatible twist correctly left outside the theorem

--- STDERR ---

--- EXIT CODE ---
0
```

## Complete Phase-2 capture: `validation/phase2_validate_n2_extension_convention.out`

```text
COMMAND: env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 LC_ALL=C PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="" python code/validate_n2_extension_convention.py
UTC_DATE: 2026-09-24T09:02:13+00:00
PYTHON_VERSION: Python 3.11.2

--- STDOUT ---
N2-A extension-field convention validation:
  K=F_16=F_(4^2), p=2, q=4, e=2, m_s=2, n=5, lambda=1, k=1
  sigma Frobenius power k: 1
  sigma field exponent p^k: 2
  rho Frobenius power em_s-k: 3
  rho field exponent p^(em_s-k): 8
  principal reciprocal Frobenius power: 3
  alternative reciprocal Frobenius power: 1
  principal reciprocal permutation: [0, 2, 4, 1, 3]
  alternative reciprocal permutation: [0, 3, 1, 4, 2]
  direct dual from defining <c,x>_k equations: 32 of 32
  direct equals principal reciprocal: 32 of 32
  direct equals alternative p^k reciprocal: 8 of 32
  example alternative discrepancies: [2, 3, 4]
PASS: direct dual selects the principal inverse-Frobenius convention

--- STDERR ---

--- EXIT CODE ---
0
```

## Complete Phase-2 capture: `validation/phase2_diagnose_n2_incompatible_twist.out`

```text
COMMAND: env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 LC_ALL=C PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="" python code/diagnose_n2_incompatible_twist.py
UTC_DATE: 2026-09-24T09:02:18+00:00
PYTHON_VERSION: Python 3.11.2

--- STDOUT ---
N2-B incompatible extension-field convention diagnostic:
  p=2, e=2, m_s=2, q=4, K=F_16=F_(4^2), k=1, n=3
  sigma Frobenius power k: 1
  sigma field exponent p^k: 2
  rho Frobenius power em_s-k: 3
  rho field exponent p^(em_s-k): 8
  sigma and rho differ as automorphisms: True
  lambda=alpha^3 (order 5): 8
  lambda^(1+principal field exponent): 15 != 1
  lambda^(1+alternative field exponent p^k): 10 != 1
  defining-inner-product direct dual checks: 8 of 8
  principal reciprocal direct agreements: 8 of 8
  alternative p^k reciprocal direct agreements: 2 of 8
  example alternative discrepancy mask: 1
  predicted principal dual twist lambda^(-principal field exponent): 12
  predicted alternative dual twist lambda^(-p^k): 10
  direct dual constacyclic under principal predicted twist: 8 of 8
  direct dual constacyclic under alternative predicted twist: 2 of 8
  proper nonzero direct duals failing original lambda twist: 6 of 6
  example original-twist failure mask: 1
No transfer-matrix enumeration was attempted because the original and dual constacyclic twists are incompatible.
PASS: N2-B independently selects the finalized principal convention

--- STDERR ---

--- EXIT CODE ---
0
```

## Complete Phase-2 capture: `validation/phase2_counterexample_search.out`

```text
COMMAND: env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 LC_ALL=C PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="" python validation/phase2_counterexample_search.py
UTC_DATE: 2026-09-24T09:02:18+00:00
PYTHON_VERSION: Python 3.11.2

--- STDOUT ---
orbit-polynomial identity checked for lengths 1 through 12
transfer trace checked for lengths 1 through 8 and weights 1, 2, 3
support/boundary orientation checked for every binary word of lengths 1 through 12
No combinatorial counterexample found in the tested finite range.
This search is computational evidence only, not a general proof.

--- STDERR ---

--- EXIT CODE ---
0
```

The independent proof-related search checks every binary word of lengths 1–12 for the orbit-polynomial and hull-support orientation identities, and checks the transfer trace for lengths 1–8 and weights 1, 2, and 3. It is computational evidence only and is not used as a proof of the general theory.

The rebuilt `Galios-Hull-main-files.zip` was also extracted to a clean temporary directory and its `run_all_validations.sh` was executed with the same empty-environment settings: exit code `0`, 116 stdout lines, and empty stderr. This package-level runtime check included all six existing validators and the Phase-2 counterexample search.

# Phase 3 Adversarial Audit and Independent Cross-Check

This section is appended after the complete Phase-1 and Phase-2 captures above. It records the Phase-3 manuscript-level audit, the independent checker, its exact capture, and the conservative disposition of unresolved items. The full 40-section audit is in `validation/PHASE3_ADVERSARIAL_AUDIT.md`.

## Phase-3 scope and result

The Phase-3 audit independently challenged all 19 Phase-2 theorems, their hypotheses and edge cases, the reciprocal/root/factor-action/dual/hull/enumerator chain, labeled-code injectivity, dimensions and counts, literature/convention claims, manuscript structure, quantum scope, and Burnside/Pólya boundaries. It found no critical mathematical counterexample under the declared square-free, simple-root, compatible-twist, componentwise-Frobenius, and labeled-code hypotheses.

The required status labels are used conservatively:

| Audited item | Phase-3 status |
|---|---|
| Theorems 1–19 under explicit hypotheses | **PASS WITH CONDITIONS** |
| Forward hull-support orientation | **PASS WITH CONDITIONS** |
| Inverse-orientation comparison | **PASS WITH CONDITIONS** |
| Factor-selection-to-code injectivity | **PASS WITH CONDITIONS** |
| Dimension and counting formulas | **PASS WITH CONDITIONS** |
| N1 | **VERIFY** |
| Literature/source convention and exact theorem transfer | **VERIFY** |
| Novelty boundary | **VERIFY** |
| Quantum applications | **FUTURE WORK** |
| Burnside/Pólya equivalence enumeration | **FUTURE WORK** |
| Repository Phase-2 commit provenance | **PASS WITH CONDITIONS** |

The exact overall Phase-3 verdict is:

> **VERIFY — MATERIAL AUDIT GAPS REMAIN**

N1 is explicitly **`UNSPECIFIED — CANNOT VALIDATE`**: only `q=16`, `n=15`, and `2^15=32768` are recoverable, so no `k`, twist, factorization, orbit data, or expected histogram is fabricated. The accessible source preprint also uses a candidate-first displayed dual definition, so its reciprocal theorem is not cited as direct support for the frozen code-first convention without reconciliation.

## Independent checker

The checker is `validation/phase3_independent_enumerator_check.py`. It does not import the repository validators or reuse their finite-field, reciprocal, dual, hull, orbit, transfer, or enumeration implementations. It independently computes finite-field arithmetic, polynomial factors, the normalized rho reciprocal and inverse sigma reciprocal, direct code-first semilinear duals, direct hull dimensions, both support orientations, orbit decompositions, transfer traces, global products, code signatures, and the candidate-first literature-convention probe.

The exact captured command, timestamp, Python version, stdout, stderr, and exit code are in `validation/phase3_independent_enumerator_check.out`. The run was:

```text
Command: env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 LC_ALL=C PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="" python validation/phase3_independent_enumerator_check.py
UTC timestamp: 2026-09-24T09:41:56+00:00
Python version: Python 3.11.2
Exit code: 0
```

The captured stdout reports:

- F4 `lambda=1`: 8 selections, 8 unique codes, 0 selection collisions, orbit lengths `[1,2]`;
- F4 nontrivial compatible `lambda`: 8 selections, 8 unique codes, 0 selection collisions, orbit lengths `[1,2]`;
- F8 `k=1`: 128 selections, 128 unique codes, 0 selection collisions, orbit lengths `[1,6]`;
- F8 `k=2`: 128 selections, 128 unique codes, 0 selection collisions, orbit lengths `[1,6]`;
- F16 over F4 `k=1`: 32 selections, 32 unique codes, 0 selection collisions, orbit lengths `[1,4]`;
- F4 × F4 labeled product: 64 unique product codes and 0 product collisions;
- all direct dual/generator, dimension, hull-support, and transfer comparisons passed;
- the literal candidate-first convention matched the sigma reciprocal and differed from the frozen rho reciprocal on the F8 `n=7` probe;
- the incompatible F4 diagnostic confirmed the predicted changed twist and failure of the original twist.

## Orientation comparison

The direct code-first derivation gives

\[
(F_s\setminus J_s)\cap\tau_{s,k}(J_s),
\]

which is the forward `1\to0` boundary. The checker also computes

\[
(F_s\setminus J_s)\cap\tau_{s,k}^{-1}(J_s).
\]

The forward formula agrees with every direct hull dimension tested. The two supports differ for 90 selections in each tested F8 six-cycle and 16 selections in the tested F16-over-F4 four-cycle; they coincide in the tested F4 two-cycle cases. The inverse candidate had zero **dimension** mismatches in these examples only because factors within each orbit have equal degree, so the labeled support comparison remains necessary and catches the orientation error.

## Injectivity and package evidence

For every tested component selection, a canonical reduced row-space signature was enumerated and no two distinct factor selections collided. The two-component F4 × F4 signature product likewise had 64 unique labeled product codes. The mathematical reason is the unique monic divisor generator of each square-free component ideal followed by primitive-idempotent projection; this is not a claim about equivalence classes.

The Phase-3 ZIP rebuild and clean extraction are recorded in `validation/phase3_package_verification.out`. The extraction comparison, SHA-256 verification, and validation-suite execution are required package checks; no generated archive is treated as a mathematical proof.

# PHASE 4 — LITERATURE / CONVENTION / NOVELTY AUDIT

This section is appended after the preserved Phase-1, Phase-2, and Phase-3 evidence. The full report is `validation/PHASE4_LITERATURE_CONVENTION_AUDIT.md`; the literature claim ledger is `validation/LITERATURE_CLAIM_LEDGER.md`.

## Phase-4 convention result

The accessible source preprint `arXiv:2412.08512v1` Section 2.2 defines

```text
<alpha,beta>_k = sum_i alpha_i beta_i^(p^k)
C^(perp_k) = { alpha : <alpha,c>_k = 0 for every c in C }.
```

This is candidate-first. The frozen present convention is code-first:

```text
<c,x>_k = sum_i c_i x_i^(p^k).
```

For `sigma(a)=a^(p^k)` and `rho=sigma^(-1)`, the exact relation is

```text
D_code-first(C) = rho(C^(perp_E))
D_candidate-first(C) = sigma(C^(perp_E))
D_candidate-first(C) = sigma^2(D_code-first(C)).
```

The source displays a rho-based reciprocal and rho-based twist while displaying the candidate-first dual. The literal candidate-first equations instead select the sigma reciprocal and twist. The source formulas are therefore convention-mismatched for non-involutory parameters and are not transferred as printed.

## Phase-4 independent convention capture

The new independent checker is `validation/phase4_convention_equivalence.py`. It does not import the Phase-3 checker or existing validator dual routines. The captured run is in `validation/phase4_convention_equivalence.out` and records command, UTC timestamp, Python version, stdout, stderr, and exit code.

Finite results:

| Case | Dual-code differences | Hull-dimension differences | LCD-criterion differences | Code/Candidate LCD counts | Support differences | Source rho-display disagreements |
|---|---:|---:|---:|---:|---:|---:|
| F4 `lambda=1`, `k=1` | 0/8 | 0/8 | 0/8 | 4/4 | 0/8 | 0/8 |
| F8 `lambda=1`, `k=1` | 120/128 | 0/128 | 0/128 | 4/4 | 90/128 | 120/128 |
| F8 `lambda=1`, `k=2` | 120/128 | 0/128 | 0/128 | 4/4 | 90/128 | 120/128 |
| F16 over F4 `lambda=1`, `k=1` | 24/32 | 0/32 | 0/32 | 4/4 | 16/32 | 24/32 |
| F16 over F4 `lambda=alpha^3`, `k=1` | 6/8 | 0/8 | 0/8 | 8/8 | not applicable: incompatible twists | 6/8 |

The exact relation `D_candidate-first=sigma^2(D_code-first)` passed for every tested selection. The equal hull dimensions in these constacyclic tests do not imply equal dual codes or equal hull supports.

## Phase-4 N1 search

The new repository search is `validation/search_n1_specification.py`; its complete capture is `validation/search_n1_specification.out`. It searched current source/document text files (excluding generated output captures) and all available Git history without inferring values. It recovered only:

```text
q=16
n=15
2^15=32768
```

It found no `lambda`, `k`, factorization, orbit decomposition, expected histogram, or executable output. The result remains:

> **N1: `UNSPECIFIED — CANNOT VALIDATE`.**

N1 is optional numerical evidence, not a dependency of Theorems 1–19. It must not be presented as a passing validation row.

## Phase-4 literature and novelty result

`validation/LITERATURE_CLAIM_LEDGER.md` records source-specific claims, exact accessible results, convention status, DOI status, and manuscript actions. The primary source supports the broad affine-algebra Galois-hull setting and displays Theorems 4–8, but its candidate-first definition and rho-based formulas require explicit conversion. Related finite-field hull formulas and enumerations are verified only at their stated publisher/abstract scope and do not establish the present labeled bivariate transfer product.

The conservative contribution statement is a conditional, self-contained code-first theory and labeled joint enumerator with independent finite validation. No first-ever, novel, state-of-the-art, or priority claim is made. The exact novelty boundary remains `VERIFY`.

## Phase-4 package and regression status

The existing Phase-1/Phase-2/Phase-3 captures remain unchanged. The Phase-4 checker passed its finite assertions; the N1 search exited 0 with unresolved metadata; and the package rebuild, clean extraction comparison, hash check, and extracted validation-suite run are recorded in `validation/phase3_package_verification.out` after the final Phase-4 package rebuild.

**Phase-4 status: `VERIFY — MATERIAL LITERATURE OR CONVENTION GAPS REMAIN`.**

# PHASE 5 — CONVENTION TRANSFORMATION AND INVARIANCE

This section is appended after the preserved Phase-1 through Phase-4 evidence. The full audit is `validation/PHASE5_CONVENTION_INVARIANCE_AUDIT.md`; the independent search is `validation/phase5_convention_counterexamples.py` and its capture is `validation/phase5_convention_counterexamples.out`.

## Exact dual transformation

The frozen code-first dual is

```text
D_code(C) = { x : sum_i c_i sigma(x_i) = 0 for every c in C }.
```

The verified source candidate-first dual is

```text
D_cand(C) = { y : sum_i y_i sigma(c_i) = 0 for every c in C }.
```

With `rho=sigma^(-1)` and `T=sigma^2`, direct transformation of the defining equations gives

```text
D_cand(C) = T(D_code(C)) = sigma^2(D_code(C)).
```

Here `sigma^2(a)=a^(p^(2k))`, with the Frobenius iteration reduced modulo `e*m_s` as a field automorphism. The dual codes are not generally equal; they are coordinatewise Frobenius-conjugate and dimension-preserving.

## Twist and family transformation

Coordinatewise `T` maps a `lambda`-constacyclic code to a `sigma^2(lambda)`-constacyclic code. The separately derived dual twists are

```text
code-first:      rho(lambda^(-1)) = lambda^(-p^(e*m_s-k))
candidate-first: sigma(lambda^(-1)) = lambda^(-p^k).
```

The frozen compatibility condition and the candidate-first compatibility condition are equivalent, and under compatibility `sigma^2(lambda)=lambda`. Thus the compatible family is stable under `T`, but an individual selected-factor code need not be Frobenius-invariant.

## Hull and LCD invariance

The exact subspace identity is

```text
T(C intersect D_code(C)) = T(C) intersect D_cand(C).
```

It reduces to a same-code hull transformation only when `T(C)=C`; that individual-code condition fails for many non-involutory selections.

Nevertheless, for any finite-field-linear code with basis `c_1,...,c_r`, let

```text
G_ij = sum_l c_i[l] sigma(c_j[l]).
```

The code-first hull has coefficient nullity `r-rank(G)`, while the candidate-first hull has coefficient nullity `r-rank(G transpose)`. Therefore

```text
dim(C intersect D_code(C)) = dim(C intersect D_cand(C))
```

for every finite-field-linear code. LCD decisions are consequently invariant as well. This is a dimension theorem, not equality of hull subspaces.

## Supports, factor permutations, and enumerators

For a compatible simple-root factor set, the reciprocal root actions are

```text
rho action:   alpha -> alpha^(-p^(e*m_s-k))
sigma action: alpha -> alpha^(-p^k).
```

Their factor permutations satisfy `tau_sigma=tau_rho^(-1)`. The actual dual-generator supports are `tau_rho(F minus J)` and `tau_sigma(F minus J)`; the hull-generator supports are obtained by adjoining `J`, while the complementary dimension-support sets are `(F minus J) intersect tau_rho(J)` and `(F minus J) intersect tau_sigma(J)`. These supports can differ: the Phase-5 search found 120/128 dual-support and 90/128 hull-support differences in each tested F8 non-involutory case, and 24/32 dual-support and 16/32 hull-support differences in the tested F16 `k=1` and `k=3` cases, even though weighted hull dimensions agreed.

Because hull dimension is invariant term by term on the same code collection, the following are invariant under the two dual conventions:

- total labeled-code count;
- code-dimension distribution;
- hull-dimension distribution;
- joint code/hull enumerator;
- LCD count;
- mean hull dimension;
- hull-dimension variance.

The present enumerator remains explicitly code-first and uses the frozen inverse-Frobenius support formula. Support labels and dual-generator polynomials are not silently identified with the candidate-first objects.

## Phase-5 independent search

The fresh implementation directly computes both annihilators separately and tests F4, F8, and F16 with `k=0`, every nonzero admissible `k`, `lambda=1`, compatible nontrivial twists where available, and incompatible twists where relevant. It exhausts the listed factor selections and samples 1,182 arbitrary rank-2 codes in `F8^3`.

Results:

- zero dual-transformation failures;
- zero hull-dimension counterexamples;
- zero LCD counterexamples;
- zero reciprocal-composition failures;
- zero inverse-factor-permutation failures;
- zero twist-transformation failures;
- nonzero individual-code Frobenius-invariance failures;
- nonzero dual-code, hull-subspace, and factor-support differences;
- zero arbitrary-code hull/LCD counterexamples in the deterministic sample.

The finite output is evidence for the implementation; the Gram-matrix derivation is the proof of hull-dimension/LCD invariance.

**Phase-5 status: `PASS WITH CONDITIONS — INVARIANCE PROVED UNDER EXPLICIT CONDITIONS`.**

# PHASE 6 — FINAL CONSOLIDATION AND PUBLICATION-SAFETY AUDIT

This section is appended after the preserved Phase-1 through Phase-5 evidence. It does not rewrite historical captures. The full final audit is `validation/PHASE6_FINAL_CONSOLIDATION_AUDIT.md`; the current literature transfer record is `validation/LITERATURE_TRANSFER_MATRIX.md`.

## Phase-6 consolidated chain

The final publication-safe dependency order is:

```text
square-free affine decomposition
        |
        v
finite-field component constacyclic quotients
        |
        v
labeled irreducible factor selections and injectivity
        |
        v
code-first second-slot k-Galois dual
        |
        v
inverse-Frobenius change of variables and normalized reciprocal
        |
        v
root action, compatible twist, and factor permutation
        |
        v
lcm/intersection hull support
        |
        v
cyclic boundary statistic with orbit weights
        |
        v
orbit polynomial and transfer matrix
        |
        v
global labeled joint enumerator
        |
        v
distributions, LCD count, mean, and variance
```

The main result is conditional on the consolidated square-free, finite-field, simple-root, compatibility, fixed-label, and labeled-selection hypotheses. Repeated roots, incompatible two-modulus transfer, Burnside/Pólya equivalence counts, and unconditional quantum-distance claims remain outside the main theorem.

## Formal convention transformation and separate invariants

For `sigma(a)=a^(p^k)` and `rho=sigma^(-1)=a^(p^(e*m_s-k))`, the two defining annihilators are implemented independently:

```text
D_code(C) = {x : sum_i c_i sigma(x_i)=0 for every c in C}
D_cand(C) = {y : sum_i y_i sigma(c_i)=0 for every c in C}
D_code(C) = rho(C^(perp_E))
D_cand(C) = sigma(C^(perp_E))
D_cand(C) = sigma^2(D_code(C)).
```

The dual codes and factor-labelled supports are not generally equal. For a basis matrix `B`, the restricted Gram matrix `G=B sigma(B)^T` gives both same-code hull coefficient nullities as `rank-nullity` (right versus left nullspace), hence

```text
dim(C intersect D_code(C)) = dim(C intersect D_cand(C))
```

for every finite-field-linear code. The resulting LCD decision and same-code dimension/hull enumerator agree; this does not assert equality of hull subspaces or support sets. The exact subspace identity retained is

```text
sigma^2(C intersect D_code(C))
  = sigma^2(C) intersect D_cand(C),
```

and `sigma^2(C)=C` is not silently assumed.

## Support, boundary, and enumerator closure

The code-first support is

```text
(F_s minus J_s) intersect tau_rho(J_s)
  = tau_rho(J_s) minus J_s,
```

with `tau_sigma=tau_rho^(-1)` under compatibility. On an orbit of length `a` the statistic is `sum_i epsilon_i(1-epsilon_(i+1))`, cyclically, with weight `w_O=m_s*d_O`. Reversal preserves the statistic because a Frobenius orbit has equal factor degrees and hence equal weights at all positions; arbitrary unequal weights within one cycle are not claimed invariant. Unequal weights across separate orbits remain allowed because the product enumerator factors orbitwise.

The matrix is

```text
T_w(u,z) = [[u^w, 1], [u^w z^w, 1]],
E(u,z) = product_s product_O trace(T_(w_O)(u,z)^(a_O)).
```

The lcm support proof, factor/ideal injectivity proof, trace/closed-walk argument, and moment derivations are consolidated in `PHASE6_FINAL_CONSOLIDATION_AUDIT.md` and the blueprint.

## Final source-PDF and literature record

A final local source-PDF check was made against the available `arXiv:2412.08512v1` PDF record. The standard-library structural extraction is `validation/source_pdf_theorem_check.py`, with capture `validation/source_pdf_theorem_check.out`. It confirmed the displayed candidate-first inner product/dual definition, the source displayed reciprocal/twist, component lcm/hull results, and the later Gray-map material. This confirms the convention mismatch that must be transformed; it does not make the external theorem directly transferable. The final/corrected source applicability and exact novelty boundary remain `VERIFY`. The exact source-PDF limitation and hash are recorded in the Phase-6 audit; historical Phase-4 records remain preserved.

`validation/LITERATURE_TRANSFER_MATRIX.md` uses only the required transfer statuses: `DIRECT`, `DIRECT AFTER CONVENTION TRANSFORMATION`, `PARTIAL`, `NOT TRANSFERABLE`, and `UNVERIFIED`.

## Final N1 search

`validation/search_n1_specification.py` now searches current files and filenames, generated captures, ZIP members and text, available PDF bytes/filenames, Git patch history, and Git-history filenames. It recovers only `q=16`, `n=15`, and the proposed count `32768=2^15`. It does not recover `lambda`, `k`, a factorization, orbit data, an expected histogram, or an executable output.

> **N1: `UNSPECIFIED — CANNOT VALIDATE`.**

No N1 value is inferred or fabricated, and no N1 result is used in the main theorem evidence.

## Independent Phase-6 end-to-end evidence

`validation/phase6_end_to_end_check.py` is standalone and imports no earlier checker. Its capture is `validation/phase6_end_to_end_check.out`. It checks F4, F8, and F16 with `k=0` and every admissible nonzero `k`, compatible and incompatible nontrivial twists where available, direct annihilators, direct intersections, restricted Gram dimensions, inverse-Frobenius reciprocal generators, support/boundary weights, factor-selection injectivity, and orbit-transfer enumerators. It also checks all 73 rank-two planes in `F8^3` and explicitly demonstrates that unequal within-orbit weights cannot be given an unconditional reversal-invariance claim.

The independent capture ends with:

```text
PHASE6 END-TO-END CHECK: PASS
```

This is finite computational evidence only. It does not replace the conditional proofs.

## Conservative scope and publication status

- Novelty/priority: no priority claim; exact boundary remains `VERIFY`.
- Quantum: conditional/future work; no distance or quantum parameter is inferred.
- Burnside/Pólya: future work; no equivalence-class count is claimed.
- Repeated-root: future work; excluded by `gcd(n,p)=1`.
- Incompatible twists: direct diagnostics only; no same-family transfer enumeration.
- Abstract/conclusion/examples: conditional language and N1/source limitations are explicit.

The final status is:

> **Phase-6 manuscript-readiness verdict: `NOT READY — MATERIAL GAPS REMAIN`.**

The outstanding issues are publication-critical literature theorem transfer/source verification, the exact novelty boundary, and the absent N1 artifact; they are not hidden by the passing finite regression.

## Phase-6 package closure

`Galios-Hull-main-files.zip` is rebuilt after the Phase-6 files and captures are finalized. The clean-extraction/package regression, manifest comparison, source-PDF hash, Git-metadata exclusion, and extracted validation-suite run are captured in `validation/phase3_package_verification.out`. The package contains the Phase-6 audit, transfer matrix, standalone validator/output, updated blueprint/report, all historical audits/captures, and the source PDF. No fake `.tex` or `.bib` file is added.

**Phase-6 status: `NOT READY — MATERIAL GAPS REMAIN`.**

---

# Phase 7 final literature and manuscript preparation validation

**Date:** 2026-09-24
**Branch:** `arena/01a0c9d2-galios-hull`
**Base:** `3c064a06a7fa32a402b3dd965bc239967c912c62`

## Scope and verdict

Phase 7 adds the final source/reference audit, final literature claim ledger, final transfer matrix, conservative novelty boundary, manuscript draft specification, and N1 exclusion policy. The Phase-1–6 evidence and frozen mathematics are preserved. No `.tex` or `.bib` file is fabricated.

> **Phase-7 manuscript-readiness verdict: `NOT READY — MATERIAL GAPS REMAIN`.**

The publisher identity and broad scope of the primary article are verified, but complete final/corrected theorem transfer remains inaccessible and the exact external novelty boundary is not established. N1 remains `UNSPECIFIED — CANNOT VALIDATE` and is excluded from manuscript evidence.

## Final source checks

- Primary publisher record: title, authors, venue, volume/issue, date, article number, DOI, abstract, introduction, and section snippets checked at the ScienceDirect record listed in `validation/FINAL_REFERENCE_AUDIT.md`.
- Readable source: arXiv:2412.08512 HTML checked for the candidate-first pairing, displayed rho formulas, affine theorem family, and conditional quantum section.
- Local PDF: `validation/source_pdf_theorem_check.py` and `.out`; SHA-256 `0db90bfbeda69ad1af231b81d92f24be3589ed15ac2e0ade6605ba7ad0ddc039`.
- Related publisher records: finite-field article/correction, cyclic/negacyclic article, Hermitian average article, general Galois-hull article, 2025 average article, and non-chain Hermitian article checked as recorded in `validation/FINAL_REFERENCE_AUDIT.md`.

The source's candidate-first definition is not silently identified with the code-first definition. The final ledger records the source formula as `CONVENTION MISMATCH` for literal non-involutory candidate-first transfer and records the transformed structural use separately.

## New Phase-7 artifacts

- `validation/PHASE7_FINAL_LITERATURE_AND_MANUSCRIPT_AUDIT.md`
- `validation/FINAL_REFERENCE_AUDIT.md`
- `validation/NOVELTY_BOUNDARY.md`
- `validation/MANUSCRIPT_DRAFT_SPECIFICATION.md`
- Phase-7 final sections of `validation/LITERATURE_CLAIM_LEDGER.md` and `validation/LITERATURE_TRANSFER_MATRIX.md`
- Phase-7 manuscript-facing closure appended to `new-paper-blueprint.md`

The manuscript specification contains a conservative abstract, introduction/literature-review policy, fixed preliminaries, the 19-result theorem architecture, separate convention/invariance propositions, an acyclic dependency graph, fully specified examples, limitations, and conclusion requirements. It contains no N1 evidence.

## Root regression

The complete clean-environment command was rerun with `env -i`, `PYTHONDONTWRITEBYTECODE=1`, and the standard-library-only suite:

```text
env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 LC_ALL=C PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="" bash -c 'python code/validate_pilot.py; python code/validate_long_orbit_examples.py; python code/validate_nontrivial_constacyclic.py; python code/diagnose_incompatible_twist.py; python code/validate_n2_extension_convention.py; python code/diagnose_n2_incompatible_twist.py; python validation/phase2_counterexample_search.py; python validation/phase3_independent_enumerator_check.py; python validation/phase4_convention_equivalence.py; python validation/phase5_convention_counterexamples.py; python validation/phase6_end_to_end_check.py; python validation/source_pdf_theorem_check.py; python validation/search_n1_specification.py'
```

**Exit code:** `0`
**Result:** all listed finite validators and the Phase-6 independent end-to-end check passed. The final line of the independent capture remains `PHASE6 END-TO-END CHECK: PASS`.

## Phase-7 status summary

| Item | Status |
|---|---|
| Frozen convention and formulas | `RESOLVED` |
| Candidate-first/code-first separation | `RESOLVED` |
| Publisher metadata | `RESOLVED WITH CONDITIONS` |
| Final/corrected central theorem transfer | `UNRESOLVED` |
| Exact novelty boundary | `UNRESOLVED` |
| N1 manuscript evidence | `EXCLUDED` |
| Fully specified computations | `RESOLVED WITH CONDITIONS` |
| Manuscript specification | `RESOLVED WITH CONDITIONS` |
| Repeated-root/Burnside/unconditional quantum extensions | `FUTURE WORK` |
| Final package verification | `RESOLVED WITH CONDITIONS` |

The status values in the table are restricted to the Phase-7 vocabulary required by the audit.

## Final Phase-7 package verification

The final archive was rebuilt after all Phase-7 files and the package capture were present. It passed `unzip -t`, exact manifest/content comparison, Git-metadata exclusion, required-file checks, manuscript-specification N1 exclusion, and a clean extracted validation-suite run with zero stderr lines. The extracted suite ended with the preserved `PHASE6 END-TO-END CHECK: PASS` and the internal artifact status `N1 UNSPECIFIED — CANNOT VALIDATE`. The final archive contains 53 manifest files; its SHA-256 is reported with the final deliverable.
