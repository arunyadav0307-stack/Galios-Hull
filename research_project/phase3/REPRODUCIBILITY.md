# Phase 7 deliverable — Reproducibility

Every result in Phases 2–3 can be regenerated from a clean checkout. This document records the exact
commands, the interpreter, and the runtime actually measured.

From `4997773`. Branch `arena/831a2e65-galios-hull`.

---

## 1. Environment

| Item | Value |
|---|---|
| Python | `3.11.2` (`/usr/bin/python3`) |
| Third-party packages | **none** — everything is stdlib. `numpy` was present early in the project and later disappeared; all code that used it was rewritten in stdlib and re-verified (`P3_3_RING_GRAY.md` §7.1) |
| Magma | **not available** |
| PDF tooling | `pypdf` is **no longer installed**, so `tools/preflight.py` cannot run (environment regression, not a broken artifact). Its source check was substituted by `sha256sum` — see §4 |
| Network | not needed for any computation |

## 2. Commands, in order, with measured runtimes

Run from the repository root `research_project/..`:

```bash
# Phase 1 machinery self-tests
python3 research_project/tools/preflight.py        # needs pypdf; currently blocked
python3 research_project/tools/selftest_gate.py    # PASS 7/7

# Phase 2 probes (R3)
python3 research_project/phase2/r3_probe/r3_probe.py
python3 research_project/phase2/r3_probe/r3_dual_formula.py
python3 research_project/phase2/r3_probe/r3_hull_dim_check.py

# Phase 2 probes (R1)
python3 research_project/phase2/r1_probe/r1_probe.py        # ~40 s
python3 research_project/phase2/r1_probe/r1_orbit_check.py  # ~11 s, 24/24

# Phase 3
python3 research_project/phase3/r4_field_joint.py           # ~4 s
python3 research_project/phase3/p3_tables.py                # ~15 s
python3 research_project/phase3/p3_ring_gray.py             # ~13 s
python3 research_project/phase3/p3_quantum_dist.py          # ~24 s
python3 research_project/phase3/p3_quantum_table.py         # ~54 s, writes the CSV
python3 research_project/phase3/p3_gray_hull_identity.py    # <1 s, 256/256
```

Total under four minutes. Logs are written next to each script as `<name>_log.txt` with the command,
interpreter version and full output.

## 3. Expected headline outputs

If a run reproduces these, it is the same computation:

| Where | Expected |
|---|---|
| `r1_probe` | 184 subspaces; 8/8 `α` MATCH; 32/32 and 80/80 lcm checks |
| `r1_orbit_check` | `matched 4, 0, 3, 4, 3, 3, 3` — 24/24, no mismatches |
| `p3_tables` | C1 maxima 3,3,1,1,3; MDS 16,16,3,6,6; SO 4,24,3,6,9; independence violations 5,11,2,3,9 |
| `p3_ring_gray` | 0 bound violations everywhere; 40/40 and 40/40 equality cases; `e=3` σ=3 strict in 6/6 |
| `p3_quantum_dist` | 144, 144, 216 tuples; parameter multiplicities 8/8/64/64, 16/64/64, 27/81/81/27 |
| `p3_quantum_table` | 504 rows; `rank_eq_sum_of_dims` yes in 504/504 |
| `p3_gray_hull_identity` | 256 agree, 0 differ |

## 4. Source-paper integrity

`tools/preflight.py` cannot run (missing `pypdf`). The check it performs was done directly:

```bash
sha256sum "research_project/source_paper/Hermitian hull of constacyclic codes and quantum Codes.pdf"
# 7f7e6803dffe8d42912c506cc0b6d8910187be169e14c869f3275d896c27d249
ls -l  # 612 826 bytes
```

Both match the Phase 0 verification log. This is stated as a substitution, not passed off as the
original check.

## 5. Known non-determinism / fragility

* **No randomness anywhere.** No seeds to record.
* **Runtime blowups are the main hazard.** `find_matrix(F, 3)` searches `|F|^9`; it is restricted to
  `F_4` for that reason, and the `F_9` call site is guarded.
* **`numpy` presence changes nothing** — the stdlib path is now the only path.
* **Two silent-failure modes were hit and are now guarded:** a `timeout` inside a pipeline returned
  exit status 0 with an *empty* log (fixed by redirecting directly rather than piping), and the local
  `.git` was reset to the branch base three times, which silently detaches the working tree from the
  committed history. Recovery procedure is in `P3_3_RING_GRAY.md` §7.2: `git fetch` then
  `git reset --mixed FETCH_HEAD`; the remote is the source of truth and no commit was ever lost.

## 6. What is *not* reproducible from this repository

| Item | Why |
|---|---|
| Full text of B-2a, B-2b, Tian–Gao–Gao | paywalled; blockers, not failures |
| The source paper's Magma computations | the paper's own; not re-run here |
| `preflight.py`'s manifest check | missing `pypdf` |
