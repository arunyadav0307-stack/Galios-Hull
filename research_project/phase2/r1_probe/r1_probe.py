"""
R1 feasibility probe -- repeated roots (p | n), FIELD level then RING level.
NOT Phase 3, NOT a deliverable of a later phase.

Purpose: is "count lambda-constacyclic codes of length n by Hermitian hull dimension,
in the repeated-root regime" a mechanical computation?

Three independent routes are compared on the smallest cases:

  (R1-a)  brute force over ALL F_q2-subspaces of F_q2^n  (n = 3 only: 184 subspaces),
          keep the alpha-constacyclic ones, compute the Hermitian hull by linear algebra;
  (R1-b)  enumerate the monic divisors g of x^n - alpha (over a field these biject with
          the codes), compute the hull by linear algebra;
  (R1-c)  the closed formula  dim Hull = n - deg lcm(g, h^dagger),  h = (x^n - alpha)/g,
          with the conjugate-reciprocal dagger -- the formula the source uses in the
          proof of its Theorem 8.

Plus, for the ring R_e, the product over components established in R3_DECISION.md.

ASCII only, stdlib only, deterministic.
"""

import itertools
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r3_probe"))
from r3_probe import find_irreducible, rref, nullspace, in_span


# --------------------------------------------------------------------------- field
def make_field(p, q):
    m, t = 0, q
    while t % p == 0:
        t //= p
        m += 1
    assert p ** m == q
    F = find_irreducible(p, 2 * m)
    F.conj_f = [F.pow(a, q) for a in range(F.Q)]
    F.q = q
    return F


# --------------------------------------------------------------------------- polynomials over F
class Pol:
    def __init__(self, F):
        self.F = F

    def trim(self, a):
        a = list(a)
        while len(a) > 1 and a[-1] == 0:
            a.pop()
        return a

    def add(self, a, b):
        F = self.F
        n = max(len(a), len(b))
        out = [0] * n
        for i in range(n):
            x = a[i] if i < len(a) else 0
            y = b[i] if i < len(b) else 0
            out[i] = F.add[x][y]
        return self.trim(out)

    def sub(self, a, b):
        F = self.F
        return self.add(a, [F.neg[x] for x in b])

    def mul(self, a, b):
        F = self.F
        if not a or not b:
            return [0]
        out = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            if x == 0:
                continue
            for j, y in enumerate(b):
                if y:
                    out[i + j] = F.add[out[i + j]][F.mul[x][y]]
        return self.trim(out)

    def divmod_(self, a, b):
        F = self.F
        a = self.trim(a)
        b = self.trim(b)
        assert b != [0]
        if len(a) < len(b):
            return [0], a
        inv = next(x for x in range(1, F.Q) if F.mul[b[-1]][x] == F.one)
        q = [0] * (len(a) - len(b) + 1)
        r = list(a)
        for k in range(len(a) - len(b), -1, -1):
            c = F.mul[r[k + len(b) - 1]][inv]
            if c == 0:
                continue
            q[k] = c
            for j in range(len(b)):
                r[k + j] = F.add[r[k + j]][F.neg[F.mul[c][b[j]]]]
        return self.trim(q), self.trim(r[:len(b) - 1] + [0])

    def gcd(self, a, b):
        a, b = self.trim(a), self.trim(b)
        while b != [0]:
            _, r = self.divmod_(a, b)
            a, b = b, r
        inv = next(x for x in range(1, self.F.Q) if self.F.mul[a[-1]][x] == self.F.one)
        return self.trim([self.F.mul[inv][c] for c in a])

    def lcm(self, a, b):
        g = self.gcd(a, b)
        q, _ = self.divmod_(self.mul(a, b), g)
        return self.trim(q)

    def dagger(self, a):
        """Conjugate-reciprocal: p^dagger(x) = a_0^{-q} * sum_i a_i^q x^{s-i}."""
        F = self.F
        a = self.trim(a)
        s = len(a) - 1
        lead = F.pow(a[0], F.q)          # a_0^q
        inv = next(x for x in range(1, F.Q) if F.mul[lead][x] == F.one)
        out = [0] * (s + 1)
        for i in range(s + 1):
            out[s - i] = F.mul[inv][F.pow(a[i], F.q)]
        return self.trim(out)


# --------------------------------------------------------------------------- codes
def code_from_generator(F, g, n, alpha):
    """<g> inside F[x]/(x^n - alpha), as an RREF basis of F^n."""
    P = Pol(F)
    f = [F.neg[alpha]] + [0] * (n - 1) + [F.one]
    vecs = []
    for j in range(n):
        prod = P.mul([0] * j + [F.one], g)
        _, r = P.divmod_(prod, f)
        r = (r + [0] * n)[:n]
        vecs.append(r)
    return rref(F, vecs, n)[0]


def divisors(F, n, alpha):
    P = Pol(F)
    f = [F.neg[alpha]] + [0] * (n - 1) + [F.one]
    out = []
    # enumerate monic divisors by brute force over the coefficient box (small n only)
    for d in range(n + 1):
        if d == 0:
            out.append([F.one])
            continue
        for tail in itertools.product(range(F.Q), repeat=d):
            g = list(tail) + [F.one]
            _, r = P.divmod_(f, g)
            if r == [0]:
                out.append(g)
    return out


def hull_dim(F, basis, n):
    dual = nullspace(F, [[F.conj_f[y[i]] for i in range(n)] for y in basis], n)
    return inter_dim(F, basis, dual, n)


def inter_dim(F, A, B, ncols):
    pa, pb = len(A), len(B)
    rows = []
    for c in range(ncols):
        rows.append([A[i][c] for i in range(pa)] + [F.neg[B[j][c]] for j in range(pb)])
    return len(nullspace(F, rows, pa + pb))


def min_dist(F, basis, n):
    if not basis:
        return None
    words = set()
    k = len(basis)
    for coeff in itertools.product(range(F.Q), repeat=k):
        w = [0] * n
        for c, b in zip(coeff, basis):
            if c:
                for i in range(n):
                    w[i] = F.add[w[i]][F.mul[c][b[i]]]
        words.add(tuple(w))
    best = None
    for w in words:
        if all(v == 0 for v in w):
            continue
        d = sum(1 for v in w if v != 0)
        if best is None or d < best:
            best = d
    return best


# --------------------------------------------------------------------------- brute force: all subspaces
def all_subspaces(F, n):
    """Every F-subspace of F^n, as an RREF basis (canonical)."""
    for k in range(n + 1):
        for piv in itertools.combinations(range(n), k):
            free = [c for c in range(n) if c not in piv]
            used = [(row, fc) for row in range(k) for fc in free if fc > piv[row]]
            for vals in itertools.product(range(F.Q), repeat=len(used)):
                basis = [[0] * n for _ in range(k)]
                it = iter(vals)
                for row, pc in enumerate(piv):
                    basis[row][pc] = F.one
                    for fc in free:
                        if fc > pc:
                            basis[row][fc] = next(it)
                yield basis


def is_constacyclic(F, basis, n, alpha):
    if not basis:
        return True
    for v in basis:
        w = [0] * n
        w[0] = F.mul[alpha][v[-1]]
        for i in range(1, n):
            w[i] = v[i - 1]
        if not in_span(F, basis, w, n):
            return False
    return True


# --------------------------------------------------------------------------- driver
def run_field(p, q, n, label, brute):
    F = make_field(p, q)
    P = Pol(F)
    print("=" * 80)
    print(label)
    print(f"  p={p}, q={q}, F=F_{F.Q}, n={n}, gcd(n,p)={n if n % p == 0 else 1}"
          f"  -> repeated root: {n % p == 0}")

    # x^n - alpha = (x^{n'} - c)^{p^v}
    pv, np_ = 0, n
    while np_ % p == 0:
        np_ //= p
        pv += 1
    print(f"  n = {n} = {np_} * {p}^{pv};  x^n - alpha = (x^{np_} - c)^{{{p}^{pv}}} with c^{{{p}^{pv}}} = alpha")

    results = {}
    for alpha in range(1, F.Q):
        gs = divisors(F, n, alpha)
        codes = {}
        gens = {}
        for g in gs:
            b = code_from_generator(F, g, n, alpha)
            key = tuple(map(tuple, b))
            codes[key] = b
            gens[key] = g
        dist = {}
        for key, b in codes.items():
            h = hull_dim(F, b, n)
            dist[h] = dist.get(h, 0) + 1
        results[alpha] = (len(codes), dist, codes, gens)
    tot = sum(v[0] for v in results.values())
    print(f"  monic divisors of x^n - alpha, summed over alpha: {tot}")
    for alpha in sorted(results):
        cnt, dist, _, _ = results[alpha]
        print(f"    alpha={alpha:2d}: {cnt:2d} codes; hull-dim distribution {dict(sorted(dist.items()))}")

    if brute:
        # independent route: every subspace of F^n, filtered by constacyclic invariance
        print("  independent check: enumerating ALL subspaces of F^n")
        subs = list(all_subspaces(F, n))
        print(f"    total subspaces: {len(subs)}")
        for alpha in sorted(results):
            cnt, dist, codes, _ = results[alpha]
            bf = {}
            for b in subs:
                if is_constacyclic(F, b, n, alpha):
                    bf[tuple(map(tuple, b))] = b
            bf_dist = {}
            for b in bf.values():
                h = hull_dim(F, b, n)
                bf_dist[h] = bf_dist.get(h, 0) + 1
            ok = (len(bf) == cnt) and (bf_dist == dist)
            print(f"    alpha={alpha:2d}: brute force {len(bf)} codes, distribution {dict(sorted(bf_dist.items()))}"
                  f"   {'MATCH' if ok else 'MISMATCH'}")

    # cross-check the lcm formula and record distances of dual-containing codes
    print("  cross-check dim Hull = n - deg lcm(g, h^dagger):")
    bad = 0
    checked = 0
    for alpha in sorted(results):
        _, _, codes, gens = results[alpha]
        f = [F.neg[alpha]] + [0] * (n - 1) + [F.one]
        for key, b in codes.items():
            g = gens[key]
            h, _ = P.divmod_(f, g)
            l = P.lcm(g, P.dagger(h))
            pred = n - (len(l) - 1)
            got = hull_dim(F, b, n)
            checked += 1
            if pred != got:
                bad += 1
                if bad <= 3:
                    print(f"    MISMATCH alpha={alpha} g={g} pred={pred} got={got}")
    print(f"    {checked - bad}/{checked} codes agree with the lcm formula")

    print("  dual-containing codes and their parameters:")
    for alpha in sorted(results):
        _, _, codes, _ = results[alpha]
        for key, b in codes.items():
            hd = hull_dim(F, b, n)
            k = len(b)
            dual = nullspace(F, [[F.conj_f[y[i]] for i in range(n)] for y in b], n)
            dc = all(in_span(F, b, v, n) for v in dual)
            if dc:
                d = min_dist(F, b, n)
                print(f"    alpha={alpha:2d} dim={k} hull={hd} d={d}"
                      f"  -> [[{n}, {2*k-n}, >= {d}]]_{q}")
    return results


def key_to_poly(F, key, n):
    """Recover the monic generator from the RREF basis of the code.

    The generator is the lowest-degree monic polynomial whose span is the code:
    for an ideal <g> in F[x]/(x^n - alpha) of dimension k, g is the unique monic
    polynomial of degree n - k in the code.
    """
    P = Pol(F)
    vecs = [list(v) for v in key]
    k = len(vecs)
    target = n - k
    # enumerate the code and take the monic element of degree target
    FQ = F.Q
    for coeff in itertools.product(range(FQ), repeat=k):
        w = [0] * n
        for c, b in zip(coeff, vecs):
            if c:
                for i in range(n):
                    w[i] = F.add[w[i]][F.mul[c][b[i]]]
        w = P.trim(w)
        if len(w) - 1 == target and w[target] == F.one:
            return w
    raise RuntimeError("generator not found")


if __name__ == "__main__":
    run_field(3, 3, 3, "A: q=3, n=3=p  (single factor x-c, repeated root)", brute=True)
    run_field(3, 3, 6, "B: q=3, n=6=2*3  (n'=2, CR pairing can occur)", brute=False)
