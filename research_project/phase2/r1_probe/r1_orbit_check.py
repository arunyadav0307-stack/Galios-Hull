"""
R1 probe, part 2: is the repeated-root hull-dimension distribution a PRODUCT of explicit
univariate polynomials attached to the conjugate-reciprocal orbits of the factors of
x^n - alpha?

For n = p^v * n' with gcd(n', p) = 1, x^n - alpha = (x^{n'} - c)^{p^v}.  Write
x^{n'} - c = prod_i g_i (distinct monic irreducible).  A code corresponds to an exponent
vector a = (a_i), 0 <= a_i <= p^v, and its generator is g = prod g_i^{a_i}, h = prod g_i^{p^v - a_i}.
With dim Hull = n - deg lcm(g, h^dagger), and g_i^dagger proportional to g_{sigma(i)}:

  fixed point i :  contribution = m_i * min(a_i, p^v - a_i)
  2-cycle {i,j} :  contribution = m * min(s, 2*p^v - s),  s = a_i + a_j,
                   attained by  s+1  pairs when s <= p^v,  2p^v+1-s  pairs otherwise.

So the whole distribution is a product of these little polynomials.  This script builds the
prediction from the orbit data and compares it with the brute-force enumeration.

Only alpha with alpha^{q+1} = 1 is treated (the source's hypothesis r_l | q+1, which makes
x^n - alpha = x^n - alpha^{-q} so that the dagger permutes its own factors).

ASCII only, stdlib only.
"""
import os
import sys
import itertools

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "r3_probe"))
import r1_probe as R


def monic(F, p):
    p = R.Pol(F).trim(p)
    if p == [0]:
        return [0]
    inv = next(x for x in range(1, F.Q) if F.mul[p[-1]][x] == F.one)
    return [F.mul[inv][c] for c in p]


def irred_factors(F, poly):
    """distinct monic irreducible factors (poly assumed squarefree), small degrees only."""
    P = R.Pol(F)
    out = []
    rest = list(poly)
    deg = len(rest) - 1
    for d in range(1, deg // 2 + 1):
        for tail in itertools.product(range(F.Q), repeat=d):
            g = monic(F, list(tail) + [F.one])
            if len(g) - 1 != d:
                continue
            while True:
                q, r = P.divmod_(rest, g)
                if r == [0] and len(rest) - 1 >= d:
                    out.append(g)
                    rest = q
                else:
                    break
    if len(rest) - 1 > 0:
        out.append(monic(F, rest))
    return out


def divisors_from_factors(F, factors, mult):
    """All monic divisors of prod g_i^mult, i.e. all prod g_i^{a_i}, 0 <= a_i <= mult.

    Exhaustive by unique factorisation: divisors of a power of a squarefree product
    are exactly the exponent-tuple products.
    """
    P = R.Pol(F)
    out = []
    for exps in itertools.product(range(mult + 1), repeat=len(factors)):
        d = [F.one]
        for g, a in zip(factors, exps):
            for _ in range(a):
                d = P.mul(d, g)
        out.append(d)
    return out


def sigma_of(F, factors):
    P = R.Pol(F)
    sig = {}
    for i, g in enumerate(factors):
        d = monic(F, P.dagger(g))
        j = next((k for k, h in enumerate(factors) if h == d), None)
        sig[i] = j
    return sig


def orbit_distribution(F, factors, sig, mult):
    """dict hull-dim -> count, as a product over orbits."""
    P = R.Pol(F)
    seen = set()
    dist = {0: 1}
    for i in range(len(factors)):
        if i in seen:
            continue
        mi = len(factors[i]) - 1
        if sig[i] == i:
            seen.add(i)
            local = {}
            for a in range(mult + 1):
                v = mi * min(a, mult - a)
                local[v] = local.get(v, 0) + 1
        else:
            j = sig[i]
            seen.add(i)
            seen.add(j)
            mj = len(factors[j]) - 1
            assert mi == mj, (mi, mj, "a CR pair must have equal degree")
            local = {}
            for a in range(mult + 1):
                for b in range(mult + 1):
                    ss = a + b
                    v = mi * min(ss, 2 * mult - ss)
                    local[v] = local.get(v, 0) + 1
        new = {}
        for x, cx in dist.items():
            for y, cy in local.items():
                new[x + y] = new.get(x + y, 0) + cx * cy
        dist = new
    return dist


def run(p, q, n, label):
    F = R.make_field(p, q)
    P = R.Pol(F)
    pv, np_ = 0, n
    while np_ % p == 0:
        np_ //= p
        pv += 1
    print("=" * 78)
    print(f"{label}   n={n}={np_}*{p}^{pv}, F=F_{F.Q}")
    ok = bad = skipped = 0
    for alpha in range(1, F.Q):
        if F.pow(alpha, q + 1) != F.one:
            skipped += 1
            continue
        # c with c^{p^v} = alpha
        c = next(x for x in range(1, F.Q) if F.pow(x, p ** pv) == alpha)
        base = [F.neg[c]] + [0] * (np_ - 1) + [F.one]
        factors = irred_factors(F, base)
        sig = sigma_of(F, factors)
        pred = orbit_distribution(F, factors, sig, p ** pv)
        # brute force the real distribution
        gs = divisors_from_factors(F, factors, p ** pv)
        if n <= 6:  # keep the independent coefficient-box enumeration as a cross-check
            assert sorted(map(tuple, gs)) == sorted(map(tuple, R.divisors(F, n, alpha))), \
                "structural divisor list != exhaustive coefficient-box divisor list"
        codes = {}
        for g in gs:
            b = R.code_from_generator(F, g, n, alpha)
            codes[tuple(map(tuple, b))] = b
        actual = {}
        for b in codes.values():
            h = R.hull_dim(F, b, n)
            actual[h] = actual.get(h, 0) + 1
        match = pred == actual
        ok += match
        bad += (not match)
        print(f"  alpha={alpha:2d}  factors={factors}  sigma={sig}")
        print(f"      predicted {dict(sorted(pred.items()))}")
        print(f"      actual    {dict(sorted(actual.items()))}   {'MATCH' if match else 'MISMATCH'}")
    print(f"  matched {ok}, mismatched {bad}, skipped (alpha^{q+1} != 1) {skipped}")


if __name__ == "__main__":
    run(3, 3, 3, "A: q=3, n=3=p")
    run(3, 3, 6, "B: q=3, n=6=2*3  (mixed orbits)")
    run(2, 2, 2, "C: q=2, n=2=p, one factor repeated")
    run(3, 3, 9, "D: q=3, n=9=p^2, multiplicity p^2")
    run(2, 2, 4, "E: q=2, n=4=p^2 over F_4")
    run(2, 2, 8, "F2: q=2, n=8=p^3 over F_4")
    run(2, 2, 6, "G: q=2, n=6=3*2 over F_4 (higher-degree fixed orbit)")
