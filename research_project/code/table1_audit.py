#!/usr/bin/env python3
"""
TABLE 1 AUDIT -- all 13 rows: transcription, dimensions, EAQECC arithmetic.

Prior work checked only that each printed length is 2n.  This script checks the
dimensions and the internal arithmetic of every row, which is the part of F11
that had not been tested outside Examples 2 and 3.

DATA.  Transcribed from Table 1, p.22 of arXiv:2412.08512v1.  Each row gives
    (q, n, lambda_1, lambda_2, g_1 coefficients, g_2 coefficients,
     printed [len, k, d], printed [[n',k',d;c]], printed "Diff")
with coefficients listed from x^0 upwards, written symbolically as
    ('w', e) = omega^e        ('n', k) = the integer k inside F_q
so that the table's own notation ("2, omega^5, omega^3, 1") is preserved
rather than flattened into integers.

CHECKS
    C0  transcription: g_S divides x^n - lambda_S for both components, in every
        row.  If this fails, the transcription is wrong (it did fail twice
        during development; see FINAL_F11_EVIDENCE_DOSSIER.md section 6).
    C1  deg g_S < n for every component.
    C2  printed k equals sum_S (n - deg g_S) -- the UNWEIGHTED sum.
    C3  printed length equals n * N, with N = 2 for every ring used.
    C4  true F_q-dimension is sum_S |S| (n - deg g_S) = 2 * k.
    C5  feasibility: 2k <= 2n.  If 2k == 2n the image is the whole space (d = 1,
        contradicting the printed d > 1); if 2k > 2n no image exists at all.
    C6  Theorem 10: k' = k - h and c = 2n - k - h must give the same integer h.
    C7  The "Diff" column must equal (n' - k' + c) - 2(d - 1).
"""

import os
import sys
import datetime
import itertools

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from f11_source_audit import Fld, pdivides          # noqa: E402

OUT = []


def say(s=""):
    OUT.append(s)
    print(s)


F4 = Fld(2, 2, [1, 1, 1])
F9 = Fld(3, 2, [2, 2, 1])
F25 = Fld(5, 2, [2, 4, 1])
FLD = {4: F4, 9: F9, 25: F25}
OMEGA = {4: 2, 9: 3, 25: 5}

W = "w"
N = "n"

# q, n, lam1, lam2, g1, g2, (len,k,d), (n',k',d,c), Diff
ROWS = [
    (4, 5, (W, 1), (N, 1),
     [(W, 1), (N, 1), (N, 1)], [(N, 1), (W, 1), (N, 1)],
     (10, 6, 3), (10, 2, 3, 0), 4),
    (9, 4, (N, 1), (N, 1),
     [(W, 2), (W, 7), (N, 1)], [(W, 6), (W, 1), (N, 1)],
     (8, 4, 4), (8, 4, 4, 4), 2),
    (9, 5, (W, 2), (W, 2),
     [(N, 2), (W, 5), (N, 1)], [(W, 6), (N, 1)],
     (10, 7, 4), (10, 5, 4, 1), 0),
    (9, 5, (W, 2), (W, 2),
     [(W, 2), (W, 5), (W, 7), (N, 1)], [(N, 2), (W, 3), (N, 1)],
     (10, 5, 6), (10, 1, 6, 1), 0),
    (9, 5, (N, 2), (N, 1),
     [(N, 1), (N, 2), (N, 1), (N, 2), (N, 1)], [(N, 2), (W, 3), (W, 7), (N, 1)],
     (10, 3, 8), (10, 1, 8, 5), 0),
    (9, 6, (N, 1), (N, 1),
     [(N, 2), (N, 2), (N, 0), (N, 1), (N, 1)], [(N, 2), (N, 1)],
     (12, 7, 4), (12, 5, 4, 3), 4),
    (9, 7, (N, 1), (W, 2),
     [(N, 2), (W, 5), (W, 3), (N, 1)], [(W, 2), (N, 1)],
     (14, 10, 4), (14, 10, 4, 4), 2),
    (9, 7, (N, 1), (N, 2),
     [(N, 1), (W, 7), (N, 2), (W, 5), (N, 1)], [(N, 1), (W, 7), (W, 5), (N, 1)],
     (14, 7, 6), (14, 7, 6, 7), 4),
    (9, 7, (N, 1), (N, 2),
     [(N, 1), (W, 7), (N, 2), (W, 5), (N, 1)],
     [(N, 1), (N, 2), (N, 1), (N, 2), (N, 1), (N, 2), (N, 1)],
     (14, 4, 10), (14, 4, 10, 10), 2),
    (25, 13, (N, 1), (W, 8),
     [(N, 4), (W, 5), (W, 17), (N, 1)], [(W, 20), (N, 1)],
     (26, 22, 4), (26, 20, 4, 2), 2),
    (25, 16, (W, 16), (N, 1),
     [(W, 5), (W, 11), (N, 1)], [(W, 21), (N, 1)],
     (32, 29, 3), (32, 27, 3, 1), 2),
    (25, 20, (W, 8), (N, 1),
     [(W, 8), (W, 10), (N, 1)], [(N, 1), (N, 1)],
     (40, 37, 3), (40, 35, 3, 1), 2),
    (9, 26, (N, 1), (N, 1),
     [(N, 2), (N, 1), (N, 1), (N, 0), (N, 1)], [(N, 1), (N, 1)],
     (52, 47, 3), (52, 44, 3, 2), 6),
]


def elem(q, spec):
    F = FLD[q]
    kind, v = spec
    return F.pow(OMEGA[q], v) if kind == W else v % F.q


def check_transcription():
    """C0 for every conjugate naming of omega, so the verdict is naming-free."""
    say("CHECK C0 -- transcription: does g_S divide x^n - lambda_S ?")
    say("-" * 100)
    combos = list(itertools.product([2, 3], [3, 7], [5, 21]))
    results = []
    for w4, w9, w25 in combos:
        global OMEGA
        old = dict(OMEGA)
        OMEGA = {4: w4, 9: w9, 25: w25}
        good = []
        for i, row in enumerate(ROWS, 1):
            q, n, l1, l2, g1, g2 = row[0], row[1], row[2], row[3], row[4], row[5]
            F = FLD[q]
            m1 = [F.neg(elem(q, l1))] + [0] * (n - 1) + [1]
            m2 = [F.neg(elem(q, l2))] + [0] * (n - 1) + [1]
            if (pdivides(F, [elem(q, c) for c in g1], m1) and
                    pdivides(F, [elem(q, c) for c in g2], m2)):
                good.append(i)
        results.append(((w4, w9, w25), good))
        OMEGA = old
    for om, good in results:
        say(f"  omega = {om}:  {len(good)}/13 rows satisfy g_S | x^n - lambda_S"
            f"   {'ALL' if len(good) == 13 else 'missing ' + str([i for i in range(1,14) if i not in good])}")
    allok = all(len(g) == 13 for _, g in results)
    say(f"  => transcription {'VALIDATED in every naming' if allok else 'NOT validated'}")
    say()
    return allok


def main():
    say("### table1_audit.py")
    say(datetime.datetime.now().strftime("%a %b %d %H:%M:%S UTC %Y"))
    say(f"Python {sys.version.split()[0]}")
    say()
    say("=" * 100)
    say("TABLE 1 (p.22) -- all 13 rows")
    say("Every ring used has dim_q A = 4 and N = |S-hat| = 2 (checked in")
    say("f11_source_audit.py), so |S(nu)| = 2 for both components and the true")
    say("F_q-dimension of each code is twice the printed k.")
    say("=" * 100)
    say()

    c0 = check_transcription()

    hdr = (f"{'#':<3}{'n':<4}{'deg g1':<8}{'deg g2':<8}{'sum(n-d)':<10}"
           f"{'k_pr':<6}{'C2':<4}{'len':<5}{'2n':<5}{'2k':<5}{'C5':<21}{'h':<4}{'C6':<4}{'C7'}")
    say(hdr)
    say("-" * 100)

    c2_bad = c3_bad = c6_bad = c7_bad = 0
    c5_bad, c5_degen = [], []

    for i, (q, n, l1, l2, g1, g2, codew, eaq, diff) in enumerate(ROWS, 1):
        d1, d2 = len(g1) - 1, len(g2) - 1
        s = (n - d1) + (n - d2)
        k_pr, L = codew[1], codew[0]
        c2 = (s == k_pr)
        c2_bad += (not c2)
        c3 = (L == 2 * n)
        c3_bad += (not c3)
        k_true = 2 * s
        if k_true > 2 * n:
            c5 = "IMPOSSIBLE"
            c5_bad.append(i)
        elif k_true == 2 * n:
            c5 = "whole space, d=1"
            c5_degen.append(i)
        else:
            c5 = "ok"
        n2, k2, dd, c = eaq
        ha, hb = k_pr - k2, 2 * n - k_pr - c
        c6 = (ha == hb and ha >= 0)
        c6_bad += (not c6)
        c7 = ((n2 - k2 + c) - 2 * (dd - 1) == diff)
        c7_bad += (not c7)
        say(f"{i:<3}{n:<4}{d1:<8}{d2:<8}{s:<10}{k_pr:<6}{'ok' if c2 else 'BAD':<4}"
            f"{L:<5}{2*n:<5}{k_true:<5}{c5:<21}{ha:<4}"
            f"{'ok' if c6 else 'BAD':<4}{'ok' if c7 else 'BAD'}")

    say("-" * 100)
    say()
    say("CHECK RESULTS")
    say(f"  C0  g_S | x^n - lambda_S (transcription) : {'13/13, naming-free' if c0 else 'FAILED'}")
    say(f"  C1  deg g_S < n in every component       : "
        f"{all(len(r[4])-1 < r[1] and len(r[5])-1 < r[1] for r in ROWS)}")
    say(f"  C2  k_printed = sum_S (n - deg g_S)       : {13-c2_bad}/13")
    say(f"  C3  length = 2n                           : {13-c3_bad}/13")
    say(f"  C4  true dim_q = 2 * k_printed            : by construction (|S|=2)")
    say(f"  C5  2k <= 2n                              : violated in {len(c5_bad)} rows "
        f"{c5_bad}; degenerate in {len(c5_degen)} rows {c5_degen}")
    say(f"  C6  Theorem 10 arithmetic                  : {13-c6_bad}/13 consistent")
    say(f"  C7  'Diff' column identity                 : {13-c7_bad}/13 consistent")
    say()
    say("=" * 100)
    say("WHAT THIS MEANS")
    say("=" * 100)
    say("  1. C0 validates the transcription: all 13 rows are self-consistent with the")
    say("     paper's own definition of a constacyclic generator, under every conjugate")
    say("     naming of omega.  The table data was read correctly.")
    say()
    say("  2. C2 holds in all 13 rows.  Every printed code dimension is the sum of the")
    say("     COMPONENT dimensions with no factor |S(nu)| = 2.  The defect found in")
    say("     Examples 2-3 is uniform across the whole table, not local to them.")
    say()
    say(f"  3. In {len(c5_bad)} of 13 rows the true dimension 2k exceeds the printed length 2n,")
    say("     so those printed Gray images cannot exist as subspaces of F_q^{2n}.")
    say(f"     In {len(c5_degen)} more rows (2, 4, 8) 2k equals 2n, so the image would be the")
    say("     whole space and d = 1, contradicting the printed d.")
    say("     Only rows 5 and 9 escape the dimension argument entirely.")
    say()
    say("  4. C6 and C7 hold in all 13 rows: the EAQECC arithmetic is internally")
    say("     consistent.  The error is upstream, in the inputs -- a confirmation of")
    say("     the diagnosis, not a new defect.")
    say()
    say("  LIMITATION. Dimensional/arithmetic audit only.  The printed minimum")
    say("  distances were NOT verified, and corrected parameters were NOT computed")
    say("  (FINAL_F11_EVIDENCE_DOSSIER.md section 4.3, item c1).")

    path = os.path.abspath(os.path.join(HERE, "..", "verification", "table1_audit.out"))
    with open(path, "w") as fh:
        fh.write("\n".join(OUT) + "\n")
    print(f"\nwritten to {path}")


if __name__ == "__main__":
    main()
