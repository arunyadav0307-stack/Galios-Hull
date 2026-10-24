# Phase 7 deliverable — Computational verification

Blueprint Phase 7: build an enumeration path independent of the proposed formula; test small admissible
instances; include zero and nonzero hull dimensions, differing orbit structures, dual-containing cases,
boundary cases and **negative tests**; record versions, commands, outputs, runtimes and limitations.
Finite tests support proofs but do not establish them.

From `4997773`.

---

## 1. Where the code is

| Path | Role |
|---|---|
| `phase2/r3_probe/r3_probe.py` | field/ring arithmetic, RREF, nullspace, code/dual/hull over `R_e` |
| `phase2/r3_probe/r3_dual_formula.py` | independent test of the dual-containment formula |
| `phase2/r3_probe/r3_hull_dim_check.py` | hull additivity across CRT components |
| `phase2/r1_probe/r1_probe.py` | field-level enumeration, **brute force over all subspaces**, lcm cross-check |
| `phase2/r1_probe/r1_orbit_check.py` | orbit-product prediction vs enumeration |
| `phase3/r4_field_joint.py` | exact joint (hull, distance) law at field level |
| `phase3/p3_tables.py` | field-level tables across 5 instances |
| `phase3/p3_ring_gray.py` | Gray weight, bounds, equality cases, `M` admissibility |
| `phase3/p3_quantum_dist.py` | ring-level quantum-parameter distribution |
| `phase3/p3_quantum_table.py` | CSV generator (this phase) |
| `phase3/p3_gray_hull_identity.py` | `dim Hull(ψ(C)) = Σ dim Hull(C_ℓ)` |

Logs: `*_log.txt` beside each script; every number quoted in the Phase 3 documents is in one of them.

## 2. The independence requirement, and what was actually achieved

The blueprint asks for "a direct enumeration path that constructs codes and computes hull intersections
**independently of the proposed formula**". Three genuinely independent paths exist:

| Path | Method | Independent of |
|---|---|---|
| **A. brute force over all subspaces** | enumerate every subspace of `F_9³` (184), test constacyclicity | the divisor↔code bijection, the orbit formula, the lcm formula |
| **B. explicit Gray image** | build `ψ(C)` in `F_{q²}^{en}`, take its rank and its minimum weight | the CRT decomposition and the formula for `K` |
| **C. enumeration vs. closed form** | enumerate divisors, compare with the orbit product | the generating function |

Results: **A** matched on 8/8 values of `α` (counts *and* hull distributions); **B** agreed with the
formula route **504/504**; **C** matched **24/24**.

## 3. Coverage against the blueprint's checklist

| Required check | Where | Result |
|---|---|---|
| zero hull dimension | `P3_1_TABLES` C1, `CONSTITUENT_ENUMERATOR_FORMULA` §8 | present in all instances |
| nonzero hull dimension | as above | up to `⌊n/2⌋` |
| differing orbit structures | `r1_orbit_check` cases A–G | fixed points and 2-cycles both exercised |
| dual-containing cases | `DUAL_CONTAINING_ENUMERATION` | 12, 12, 6 field codes; 144, 144, 216 tuples |
| boundary cases | `p \| n` (v = 1, 2, 3); `e = 2, 3`; `α` square vs non-square | all included |
| **negative tests** | see §4 | deliberately included |
| Gray images rechecked | `p3_gray_hull_identity`, `p3_quantum_table` | 256/256, 504/504 |
| quantum claims rechecked | `QUANTUM_PARAMETER_VERIFICATION` | Singleton per row |

## 4. Negative tests — the ones that matter

A verification suite that only confirms is worthless. These were run and are recorded:

| Test | Expected | Observed |
|---|---|---|
| orbit product with `v` instead of `p^v` | should **fail** | 0/11 matched (`R1_FEASIBILITY` T-4) |
| Gray image built from `basis × basis` | should **fail** (does not span the product code) | 112/256 spurious mismatches (`P3_5` §4) |
| `e = 2` matrix over `F_4` | should be **rejected** (`ν = 2 = 0`) | rejected; Gray distance 0 reproduced (`P3_3` §6) |
| old "keep basis vectors lying in B" intersection | should **fail** on non-aligned intersections | 15/27 before the kernel method (`R3_DECISION` E-4) |
| monic-divisor enumeration **over a ring** | should **fail** (not exhaustive with zero divisors) | failed; fixed by enumerating all `g ∈ R_e^n` (`R3_DECISION` E-1) |
| `σ = 3` predicted tight for `e = 3` | refuted | `d(ψ(D,D,D)) = d(D)`, strict (`P3_3` §5) |
| LCD ⇒ `d ≤ 2` conjecture | refuted | `d = 3` LCD codes exist; LCD MDS found (`P3_1` §2) |
| MDS ⇔ self-orthogonal | refuted both ways | `P3_1` §3 |

Every one of these is a case where the computation *contradicted* an expectation — mine or the code's —
and the contradiction is retained in the record rather than smoothed away.

## 5. Limitations of the computational evidence

* **It does not prove anything.** The blueprint says so explicitly and this project does not lean on
  computation for any universal claim. Where a statement is only computational, it is labelled
  "computed only" (L-1 is the clearest example: four middle distances).
* **Scale.** Instances are `q ∈ {2,3,5}`, `n ≤ 9`, `e ≤ 3`. Cost is `∏_ℓ |C_ℓ|` per tuple (L-8); no
  asymptotic claim is made.
* **No Magma.** Not available in this environment; everything is Python.
* **Single implementation.** No third-party reimplementation of the Gray map; independence is between
  *routines within this codebase*, which is weaker than between authors.
