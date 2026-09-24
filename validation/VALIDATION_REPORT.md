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
- N1 remains `VERIFY BEFORE MANUSCRIPT FINALIZATION` because no N1 run is included in this report.

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
