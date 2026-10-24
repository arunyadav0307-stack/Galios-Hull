"""
P3-7b: check the *published* closed-form minimum distance for C_i = <(x-1)^i> of length p^s
against the quantity m(a) = min_{a <= j <= n-1} w((x-1)^j) that P3-7 conjectured to equal d(C_a).

Published statement (H. Q. Dinh, "On the linear ordering of some classes of negacyclic and cyclic
codes and their distance distributions", Finite Fields Appl. 14(1):22-40, 2008), quoted verbatim as
Lemma 1 of arXiv:2304.00762 (Zhao, Li, Yang, Fu, Shum) citing [20] and [41] (Massey-Costello-
Justesen 1973):

    For i = 1, 2, ..., p^s - 1, the cyclic code C_{i,s} = <(x-1)^i> in F_q[x]/<x^{p^s} - 1> has
    minimum distance d_i = (tau + 1) p^t, where tau and t are the unique integers with
    1 <= tau <= p-1, 0 <= t <= s-1, and

        p^s - p^{s-t} + (tau-1) p^{s-t-1} < i <= p^s - p^{s-t} + tau p^{s-t-1}.

So the claim under test is:  m(a) == d_a(published)  for every a.

If this holds at scale, L-2 is not an open conjecture at all -- it is a known theorem, and the P3-7
conjecture is a correct re-derivation of it (the Weight Lemma supplies an alternative route to the
same numbers).  This script exists to make that verdict reproducible rather than asserted.

Pure stdlib, ASCII only.
"""
import sys


def binom_mod_p(j, i, p):
    if i < 0 or i > j:
        return 0
    out = 1
    while i:
        jt, it = j % p, i % p
        if it > jt:
            return 0
        num, den = 1, 1
        for k in range(it):
            num = num * (jt - k) % p
            den = den * (k + 1) % p
        out = out * num % p * pow(den, p - 2, p) % p
        j //= p
        i //= p
    return out


def weight_of_power(j, p):
    """Lemma W: w((x-1)^j) = prod (d_i + 1) over the base-p digits d_i of j."""
    w = 1
    while j:
        w *= (j % p) + 1
        j //= p
    return w


def m_of(a, p, s):
    """min_{a <= j <= n-1} w((x-1)^j);  None for the zero code a = n."""
    n = p ** s
    if a >= n:
        return None
    return min(weight_of_power(j, p) for j in range(a, n))


def published_d(i, p, s):
    """Dinh 2008 formula as quoted in arXiv:2304.00762 Lemma 1.  None at i = 0 and i = p^s."""
    n = p ** s
    if i == 0:
        return 1                       # trivial code <1>, d = 1
    if i == n:
        return None                    # zero code
    for t in range(0, s):
        for tau in range(1, p):
            lo = n - p ** (s - t) + (tau - 1) * p ** (s - t - 1)
            hi = n - p ** (s - t) + tau * p ** (s - t - 1)
            if lo < i <= hi:
                return (tau + 1) * p ** t
    raise AssertionError("uncovered i=%d p=%d s=%d" % (i, p, s))


def main():
    print("Agreement test: m(a)  vs  published d_a  (Dinh 2008, as quoted in arXiv:2304.00762 Lemma 1)")
    tot = bad = 0
    for p in [2, 3, 5, 7, 11, 13]:
        maxs = 8 if p == 2 else (4 if p == 3 else 3)
        for s in range(1, maxs + 1):
            n = p ** s
            if n > 3000:
                continue
            bad_here = 0
            for a in range(0, n + 1):
                tot += 1
                if m_of(a, p, s) != published_d(a, p, s):
                    bad += 1
                    bad_here += 1
                    if bad <= 10:
                        print("  MISMATCH p=%d s=%d a=%d: m=%s published=%s"
                              % (p, s, a, m_of(a, p, s), published_d(a, p, s)))
            print("  p=%2d s=%d n=%4d: %4d values checked, %d mismatches"
                  % (p, s, n, n + 1, bad_here))
    print()
    print("TOTAL %d values, %d mismatches" % (tot, bad))

    print()
    print("Spot check against the published table (arXiv:2304.00762, Example 1: n = 25 over F_5,")
    print("d = 2,3,4,5,10,15,20,25 for i = 1-5, 6-10, 11-15, 16-20, 21, 22, 23, 24):")
    got = [m_of(i, 5, 2) for i in range(1, 25)]
    bands = []
    for v in got:
        if not bands or bands[-1][0] != v:
            bands.append([v, 1])
        else:
            bands[-1][1] += 1
    print("  m(a) by bands (value, count):", [tuple(b) for b in bands])
    expect = [2, 3, 4, 5, 10, 15, 20, 25]
    expect_counts = [5, 5, 5, 5, 1, 1, 1, 1]
    ok = [b[0] for b in bands] == expect and [b[1] for b in bands] == expect_counts
    print("  matches the published example:", ok)
    return 0 if (bad == 0 and ok) else 1


if __name__ == "__main__":
    sys.exit(main())
