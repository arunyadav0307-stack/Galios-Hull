"""
Phase 3 / P3-1: exact tables of the joint (Hermitian hull dimension, minimum distance) law
for lambda-constacyclic codes over F_{q^2}, across several q, n and alpha, including p | n.

Three things are being tested, all of them stated in K4_2_FEASIBILITY.md:

  (C1) the LCD-distance conjecture: every code with hull = 0 has d <= 2;
  (C2) MDS <=> self-orthogonal inside these families;
  (C3) whether the joint law keeps failing to be a function of its marginals.

Distances are exact.  Strategy per code:
  * weights 1,2,3 are tested by membership (cheap, and most codes have d <= 3);
  * otherwise the code is small enough (q^k <= 700000) to enumerate completely;
  * if neither applies the distance is reported as None and the code is counted as
    'distance not computed' -- never guessed.

Output is a compact table per (q, n, alpha) so that the run stays inside a few minutes.

ASCII only, stdlib only.
"""
import itertools
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "phase2", "r1_probe"))
sys.path.insert(0, os.path.join(HERE, "..", "phase2", "r3_probe"))
from r1_probe import make_field, divisors, code_from_generator, hull_dim   # noqa: E402
from r3_probe import in_span                                               # noqa: E402

CAP = 700000


def all_words(F, basis, n):
    """Every word of the span, as a list of tuples (pure stdlib, iterated doubling)."""
    ADD, MUL = F.add, F.mul
    words = [tuple([F.zero] * n)]
    for row in basis:
        extra = []
        for w in words:
            for c in range(1, F.Q):
                extra.append(tuple(ADD[w[i]][MUL[c][row[i]]] for i in range(n)))
        words = words + extra
    return words


def dist_of_span(F, basis, n):
    """Exact minimum distance of the span; None if it could not be computed.

    Weights 1..3 are settled by membership testing first (cheap, and most codes are small
    distance); otherwise the code is fully enumerated when q^k is within CAP.  A code that
    fits neither is reported as None -- never guessed.

    NOTE: this replaced a numpy version whose dependency is no longer present in the
    environment.  The replacement reproduces the previously committed numbers exactly;
    see P3_3_RING_GRAY.md section 5.
    """
    k = len(basis)
    if k == 0:
        return None
    for w in (1, 2, 3):
        if w > n:
            break
        for supp in itertools.combinations(range(n), w):
            for vals in itertools.product(range(1, F.Q), repeat=w):
                v = [F.zero] * n
                for i, c in zip(supp, vals):
                    v[i] = c
                if in_span(F, basis, v, n):
                    return w
    if F.Q ** k > CAP:
        return None
    best = None
    for v in all_words(F, basis, n):
        w = sum(1 for x in v if x != F.zero)
        if w and (best is None or w < best):
            best = w
            if best == 1:
                return 1
    return best


def instance(p, q, n, alphas, label):
    F = make_field(p, q)
    print("=" * 88)
    print(f"{label}:  q={q}, n={n}, F_{F.Q}")
    rows = []
    for alpha in alphas:
        for g in divisors(F, n, alpha):
            b = code_from_generator(F, g, n, alpha)
            k = len(b)
            h = hull_dim(F, b, n) if k else 0
            d = dist_of_span(F, b, n)
            rows.append((alpha, k, h, d))
    known = [r for r in rows if r[3] is not None]
    print(f"  codes: {len(rows)}  (distance computed for {len(known)})")
    # C1
    lcd = [r for r in known if r[2] == 0]
    lcd_d = sorted({r[3] for r in lcd})
    print(f"  C1  hull=0 codes: {len(lcd)};  distances seen: {lcd_d}"
          f"  ->  max = {max(lcd_d) if lcd_d else None}")
    # C2
    mds = [r for r in known if r[1] > 0 and r[1] < n and r[3] == n - r[1] + 1]
    print(f"  C2  MDS codes: {len(mds)}")
    for (al, k, h, d) in mds:
        tag = "self-orthogonal" if h == k else ("LCD" if h == 0 else "hull=%d" % h)
        print(f"        alpha={al} [{n},{k},{d}] hull={h}  {tag}")
    so = [r for r in known if r[1] > 0 and r[2] == r[1]]
    so_mds = [r for r in so if r[3] == n - r[1] + 1]
    print(f"      self-orthogonal codes: {len(so)},  of which MDS: {len(so_mds)}")
    # C3
    joint = {}
    for (_, k, h, d) in known:
        joint[(h, d)] = joint.get((h, d), 0) + 1
    hull_law, d_law = {}, {}
    for (_, k, h, d) in known:
        hull_law[h] = hull_law.get(h, 0) + 1
        d_law[d] = d_law.get(d, 0) + 1
    N = len(known)
    bad = 0
    for (h, d), c in joint.items():
        if abs(hull_law[h] * d_law[d] / N - c) > 1e-9:
            bad += 1
    print(f"  C3  joint cells: {len(joint)};  cells violating independence: {bad}"
          f"  -> independent: {bad == 0}")
    return rows


def main():
    F9 = [1, 2, 3, 4, 5, 6, 7, 8]      # every alpha in F_9^*
    F4 = [1, 2, 3]
    instance(3, 3, 3, F9, "A")
    instance(3, 3, 6, F9, "B")
    instance(2, 2, 2, F4, "D")
    instance(2, 2, 4, F4, "E")
    instance(2, 2, 6, F4, "F")


if __name__ == "__main__":
    main()
