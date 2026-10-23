# Phase 3 / P3-1 — Exact joint (hull, distance) tables

Five instances, **169 codes**, of which **144 have exactly computed distances** (the rest are the
zero code or a code too large to enumerate; never guessed). Probe: `phase3/p3_tables.py`, log
`p3_tables_log.txt` (85 lines), ≈ 16 s.

Both conjectures recorded in `K4_2_FEASIBILITY.md` §2.1 are **refuted**. They were stated as
conjectures precisely so this could happen.

## 1. The tables

| Inst | `q` | `n` | codes | `d` computed | `hull=0` codes: distances | max | MDS | self-orth. | SO ∩ MDS |
|---|---|---|---|---|---|---|---|---|---|
| A | 3 | 3 | 32 | 24 | `{1, 2, 3}` | **3** | 16 | 4 | 4 |
| B | 3 | 6 | 80 | 72 | `{1, 2, 3}` | **3** | 16 | 24 | 8 |
| D | 2 | 2 | 9 | 6 | `{1}` | 1 | 3 | 3 | 3 |
| E | 2 | 4 | 15 | 12 | `{1}` | 1 | 6 | 6 | 3 |
| F | 2 | 6 | 33 | 30 | `{1, 2, 3}` | **3** | 6 | 9 | 3 |

## 2. C1 — "every LCD code has `d ≤ 2`" — **REFUTED**

`hull = 0` codes attain `d = 3` in three of five instances (A, B, F). The single-instance
observation in `K4_2_FEASIBILITY.md` was an artefact of that instance (over `F_9`, `n = 6`,
`α = 1`, where the LCD codes happen to have `d ≤ 2`).

Concretely, instance A contains `[3,1,3]` and `[3,2,2]` codes over `F_9` with `hull = 0`, i.e.
**LCD MDS constacyclic codes**. So the sharp negative statement I was worried about is false, and
the project's headline is *not* "LCD implies bad distance".

## 3. C2 — "MDS ⟺ self-orthogonal" — **REFUTED (both directions)**

* MDS does not imply self-orthogonal: instance A has 16 MDS codes of which only 4 are
  self-orthogonal; the rest include **LCD** ones (hull 0) and hull-1 codes with `k > 1`.
* Self-orthogonal does not imply MDS: instance B has 24 self-orthogonal codes, only 8 of them MDS;
  instance E has 6 self-orthogonal, 3 MDS.

The only pattern that survives in all five instances is the trivial one: a self-orthogonal code
with `k = 1` is the `[n,1,n]` repetition-type code and is MDS.

## 4. C3 — the joint law is not a function of its marginals — **CONFIRMED, 5/5**

In every instance the joint `(hull, d)` distribution differs from the product of its marginals
(cells violating independence: 5/5, 11/11, 2/2, 3/4, 9/9). This is the finding that keeps R4 alive,
and it is now supported across two fields and five lengths rather than one instance.

## 5. What Phase 3 now stands on

| Claim | Status |
|---|---|
| Joint `(hull, d)` law is irreducible (not the marginals combined) | supported on 5 instances, 144 exact distances |
| LCD codes can be MDS constacyclic codes | **counterexamples exhibited** (instance A) |
| MDS ⟺ self-orthogonal in these families | **false**, both directions refuted |
| Closed form for `d(a,b)` in the two-orbit family | not found; reframed as a two-point multiplicity-code problem |
| Ring-level (`R_e`, Gray coupling) statement — the actual R4 question | **not started** (P3-3) |

Nothing here is a theorem; the instances are small and chosen to be exactly computable. What they do
is remove two plausible-sounding conjectures from the programme before any effort was spent proving
them, and confirm the one structural property Phase 3 depends on.
