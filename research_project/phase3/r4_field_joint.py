"""
Phase 3 / K4-2: is the field-level JOINT law (hull dimension, minimum distance) obtainable
from the two known marginal laws, or is the coupling essential?

If the joint law were the product of the marginal laws, then R4's object would be
determined by already-published quantities (hull-dimension law: Sangwisut--Jitman--
Udomkavanich 2017, and the source's Theorem 10; distance law: nothing published, but in
principle separate), and R4 would lose its content.  If it is NOT, then the joint
distribution is an irreducible new object and K4-2 passes on structure.

Instance: F_9, n = 6, alpha = 1.  x^6 - 1 = (x-1)^3 (x+1)^3 over F_9, so there are
(3+1)^2 = 16 distinct cyclic codes, indexed by a, b in {0,1,2,3}:

    C(a,b) = < (x-1)^a (x+1)^b >  in F_9[x]/(x^6 - 1),

with dim = 6 - a - b and hull dim = min(a,3-a) + min(b,3-b) (R1's verified orbit formula).

Distance is computed exactly, by testing membership of all vectors of weight 1, 2, ...
in increasing order, so the answer is a proven minimum and not a bound.

ASCII only, stdlib only.
"""
import itertools
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "phase2", "r1_probe"))
sys.path.insert(0, os.path.join(HERE, "..", "phase2", "r3_probe"))
from r1_probe import make_field, Pol, code_from_generator, hull_dim   # noqa: E402
from r3_probe import in_span                                          # noqa: E402


def min_dist(F, basis, n):
    """Exact minimum distance by increasing weight; returns n+1 for the zero code."""
    if not basis:
        return None
    for w in range(1, n + 1):
        for supp in itertools.combinations(range(n), w):
            for vals in itertools.product(range(1, F.Q), repeat=w):
                v = [F.zero] * n
                for i, c in zip(supp, vals):
                    v[i] = c
                if in_span(F, basis, v, n):
                    return w
    return None


def build(F, n, alpha, a, b):
    """< (x-1)^a (x+1)^b > modulo x^n - alpha."""
    P = Pol(F)
    g = [F.one]
    for _ in range(a):
        g = P.mul(g, [F.neg[F.one], F.one])          # x - 1
    for _ in range(b):
        g = P.mul(g, [F.one, F.one])                 # x + 1
    return code_from_generator(F, g, n, alpha), g


def main():
    F = make_field(3, 3)
    n, alpha, m = 6, 1, 3
    print("=" * 74)
    print(f"F_{F.Q}, n={n}, alpha={alpha}:  x^6 - 1 = (x-1)^3 (x+1)^3,  16 cyclic codes")
    rows = {}
    for a in range(m + 1):
        for b in range(m + 1):
            basis, g = build(F, n, alpha, a, b)
            h = hull_dim(F, basis, n) if basis else 0
            d = min_dist(F, basis, n)
            rows[(a, b)] = (len(basis), h, d)
            print(f"  (a,b)=({a},{b})  dim={len(basis)}  hull={h}  d={d}")
    joint = {}
    for (a, b), (k, h, d) in rows.items():
        joint[(h, d)] = joint.get((h, d), 0) + 1
    N = sum(joint.values())
    print(f"\n  joint distribution of (hull, d) over the {N} codes:")
    for k in sorted(joint, key=lambda t: (t[0], t[1] is None, t[1] or 0)):
        print(f"    hull={k[0]}, d={k[1]}: {joint[k]}")

    hull_law = {}
    d_law = {}
    for (k, h, d) in rows.values():
        hull_law[h] = hull_law.get(h, 0) + 1
        d_law[d] = d_law.get(d, 0) + 1
    print(f"\n  marginal hull law : {dict(sorted(hull_law.items()))}")
    print(f"  marginal d law    : {dict(sorted(d_law.items(), key=lambda t: (t[0] is None, t[0])))}")
    print("\n  is the joint law the product of the marginals?")
    ok = True
    for (h, d), c in sorted(joint.items(), key=lambda t: (t[0][0], t[0][1] is None, t[0][1] or 0)):
        pred = hull_law[h] * d_law[d] / N
        if abs(pred - c) > 1e-9:
            ok = False
            print(f"    hull={h}, d={d}: observed {c}, independent prediction {pred:.3f}")
    print(f"    => joint law = product of marginals: {ok}")

    # the same question for the hull law alone, as a control
    print("\n  control: does the hull law depend only on (a,b) through the per-factor data?")
    print("    hull = min(a,3-a) + min(b,3-b) reproduced for all 16 codes: "
          f"{all(h == min(a, 3 - a) + min(b, 3 - b) for (a, b), (k, h, d) in rows.items())}")

    # does distance see the coupling? compare codes with equal (a,b) symmetry
    print("\n  distance by (a,b) matrix (rows a=0..3, cols b=0..3):")
    for a in range(m + 1):
        print("    a=%d: " % a + "  ".join(
            f"{str(rows[(a, b)][2]):>3}" for b in range(m + 1)))
    print("\n  distance depends on BOTH a and b jointly, not on a+b alone:")
    bysum = {}
    for (a, b), (k, h, d) in rows.items():
        bysum.setdefault(a + b, set()).add(d)
    print("    " + "; ".join(f"a+b={s}: d in {sorted(x for x in v if x is not None)}"
                             for s, v in sorted(bysum.items())))


if __name__ == "__main__":
    main()
