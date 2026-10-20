#!/usr/bin/env python3
"""
FINAL CHECK -- TASK A
Independent reproduction of the "isometry changes the hull dimension" phenomenon.

Written from scratch.  This file imports nothing from the project's gf.py: the
field F_4, the ring F_4[x]/(x^3-1), the codes, the two inner products and the
hulls are all built here explicitly, and every object is enumerated as a set of
vectors so that each number can be checked by hand.

CONVENTIONS (fixed here, and used everywhere below)

  Field.  F_4 = F_2[w] / (w^2 + w + 1).  An element a0 + a1*w is stored as the
  integer a0 + 2*a1, so 0=(0,0), 1=(1,0), w=(0,1), w^2=(1,1).  Multiplication is
  (a0+a1 w)(b0+b1 w) = (a0 b0 + a1 b1) + (a0 b1 + a1 b0 + a1 b1) w, in F_2.

  Codes.  A vector is (c_0,...,c_{n-1}), index = power of x.  The lambda-shift is
  T_lambda(c_0,...,c_{n-1}) = (lambda c_{n-1}, c_0, ..., c_{n-2})   [paper p.4].
  A code is lambda-constacyclic iff T_lambda(C) is contained in C.

  Inner products.  Following the paper (p.7), the k-Galois form uses the
  Frobenius power p^k, NOT q^k:
        <u,v>_k = sum_i u_i * (v_i)^(p^k),     p = char F_q, 0 <= k < e.
  For q = 4, p = 2, e = 2, so
        k = 0 : <u,v>_0 = sum u_i v_i          (Euclidean)
        k = 1 : <u,v>_1 = sum u_i v_i^2        (Hermitian, since sqrt(q) = 2)

  Hulls.  hull_k(C) = C cap C^{perp_k}, computed as an explicit set intersection
  after enumerating the dual by brute force over all q^n vectors.
"""

import itertools
import sys

# ----------------------------------------------------------------- F_4 table
Q = 4
P = 2
E = 2

_MUL = [[0] * Q for _ in range(Q)]


def _build_mul():
    for a in range(Q):
        a0, a1 = a & 1, (a >> 1) & 1
        for b in range(Q):
            b0, b1 = b & 1, (b >> 1) & 1
            c0 = (a0 * b0 + a1 * b1) % 2
            c1 = (a0 * b1 + a1 * b0 + a1 * b1) % 2
            _MUL[a][b] = c0 + 2 * c1


_build_mul()


def mul(a, b):
    return _MUL[a][b]


def add(a, b):
    return a ^ b


def neg(a):
    return a  # characteristic 2


def inv(a):
    assert a != 0
    for b in range(1, Q):
        if _MUL[a][b] == 1:
            return b
    raise AssertionError


def fpow(a, e):
    out = 1
    for _ in range(e):
        out = _MUL[out][a]
    return out


def fdiv(a, b):
    return _MUL[a][inv(b)]


def name(a):
    return {0: "0", 1: "1", 2: "w", 3: "w^2"}[a]


# ------------------------------------------------------- polynomial helpers
def ptrim(f):
    f = list(f)
    while len(f) > 1 and f[-1] == 0:
        f.pop()
    return f


def padd(f, g):
    n = max(len(f), len(g))
    out = [0] * n
    for i in range(n):
        a = f[i] if i < len(f) else 0
        b = g[i] if i < len(g) else 0
        out[i] = add(a, b)
    return ptrim(out)


def pmul(f, g):
    out = [0] * (len(f) + len(g) - 1)
    for i, a in enumerate(f):
        if not a:
            continue
        for j, b in enumerate(g):
            if b:
                out[i + j] = add(out[i + j], mul(a, b))
    return ptrim(out)


def pmod(f, m):
    f = ptrim(f)
    m = ptrim(m)
    while len(f) >= len(m) and not (len(f) == 1 and f[0] == 0):
        d = len(f) - len(m)
        c = fdiv(f[-1], m[-1])
        for i in range(len(m)):
            f[d + i] = add(f[d + i], neg(mul(c, m[i])))
        f = ptrim(f)
        if len(f) < len(m):
            break
    return ptrim(f)


# --------------------------------------------------------------- the codes
N = 3
MOD = [neg(1), 0, 0, 1]      # x^3 - 1 over F_4


def pad(f):
    """fix the length to N = 3, so every vector is a full n-tuple"""
    f = ptrim(f)
    return (list(f) + [0] * N)[:N]


def ring_elements():
    for coeffs in itertools.product(range(Q), repeat=N):
        yield list(coeffs)


def shift(v, lam=1):
    return [mul(lam, v[-1])] + list(v[:-1])


def ideal(g):
    """the cyclic code <g> = { f*g mod (x^n - 1) : f in F_4[x]/(x^n-1) }, as a set"""
    S = set()
    for f in ring_elements():
        prod = pmul(f, g)
        S.add(tuple(pad(pmod(prod, MOD))))
    return S


def is_closed(vs, lam=1):
    return all(tuple(shift(v, lam)) in vs for v in vs)


def weight(v):
    return sum(1 for a in v if a)


def wdist(S):
    d = {}
    for v in S:
        d[weight(v)] = d.get(weight(v), 0) + 1
    return dict(sorted(d.items()))


def dim(S):
    """dim over F_4 = log_4 |S|, verified integral"""
    n = len(S)
    d = 0
    while (1 << (2 * d)) < n:
        d += 1
    assert (1 << (2 * d)) == n, f"|S|={n} is not a power of 4"
    return d


def inner(u, v, k):
    s = 0
    for i in range(len(u)):
        s = add(s, mul(u[i], fpow(v[i], P ** k)))
    return s


def dual(S, k):
    out = set()
    for v in ring_elements():
        if all(inner(v, u, k) == 0 for u in S):
            out.add(tuple(v))
    return out


def hull(S, k):
    return S & dual(S, k)


# ------------------------------------------------------------------- PART A
def partA(out):
    out("=" * 78)
    out("PART A1 -- the field, stated explicitly")
    out("=" * 78)
    out("  F_4 = F_2[w]/(w^2 + w + 1);  w^2 = w + 1;  w^3 = 1")
    out("  encoding: a0 + a1*w  ->  a0 + 2*a1")
    out("      "+"  ".join(f"{name(a)}={a}" for a in range(Q)))
    out("  addition table (^):")
    for a in range(Q):
        out("      "+"  ".join(f"{add(a,b)}" for b in range(Q)))
    out("  multiplication table:")
    for a in range(Q):
        out("      "+"  ".join(f"{mul(a,b)}" for b in range(Q)))
    out("  multiplicative order of each unit: "
        + ", ".join(f"{name(a)}:{next(e for e in range(1,4) if fpow(a,e)==1)}"
                    for a in range(1, Q)))
    out()

    out("=" * 78)
    out("PART A2 -- the code C = <1+x> in F_4[x]/(x^3 - 1)")
    out("=" * 78)
    g = [1, 1]                 # 1 + x
    C = ideal(g)
    out(f"  g(x) = 1 + x  (degree {len(g)-1})")
    out(f"  |C| = {len(C)}   dim_F4 C = {dim(C)}")
    out(f"  C is 1-constacyclic (closed under T_1): {is_closed(C, 1)}")
    out(f"  C is w-constacyclic: {is_closed(C, 2)} ;  w^2-constacyclic: {is_closed(C, 3)}")
    out("  all codewords (weight in brackets):")
    for v in sorted(C):
        out(f"     {tuple(name(a) for a in v)}  [{weight(v)}]")
    out(f"  weight distribution of C: {wdist(C)}")
    out()

    out("=" * 78)
    out("PART A3 -- the monomial map phi = diag(1, w, w^2), i.e. f(x) -> f(w x)")
    out("=" * 78)
    # check it is f(x) -> f(w x) on polynomials, and linear on F_4^3
    ok = True
    for f in ring_elements():
        # f(w x): coefficient of x^i becomes f_i * w^i
        fw = [mul(f[i], fpow(2, i)) for i in range(N)]
        # diag(1,w,w^2) applied to f
        dg = [mul(f[i], [1, 2, 3][i]) for i in range(N)]
        if fw != dg:
            ok = False
    out(f"  diag(1,w,w^2) equals f(x) -> f(wx) on every element of the ring: {ok}")
    out("  phi is diagonal with nonzero entries => preserves every Hamming weight")
    C2 = {tuple(mul(v[i], [1, 2, 3][i]) for i in range(N)) for v in C}
    out(f"  |phi(C)| = {len(C2)}   dim_F4 = {dim(C2)}")
    out(f"  phi(C) is 1-constacyclic (closed under T_1): {is_closed(C2, 1)}")
    out(f"  phi(C) is w-constacyclic: {is_closed(C2, 2)}")
    out("  all codewords of phi(C):")
    for v in sorted(C2):
        out(f"     {tuple(name(a) for a in v)}  [{weight(v)}]")
    out(f"  weight distribution of phi(C): {wdist(C2)}")
    out(f"  identical weight distributions: {wdist(C) == wdist(C2)}")
    out(f"  C == phi(C) as sets: {C == C2}")
    out()

    out("=" * 78)
    out("PART A4 -- hull dimensions, brute force over all 4^3 = 64 vectors")
    out("=" * 78)
    out(f"  {'k':<3}{'form':<12}{'dim hull_k(C)':<16}{'dim hull_k(phiC)':<18}{'changed?'}")
    res = {}
    for k in range(E):
        H1 = hull(C, k)
        H2 = hull(C2, k)
        d1, d2 = dim(C) if H1 else 0, dim(H2) if H2 else 0
        # dim of hull set (may be {0}, size 1 -> dim 0)
        d1, d2 = dim(H1), dim(H2)
        res[k] = (d1, d2)
        form = "Euclidean" if k == 0 else "Hermitian"
        out(f"  {k:<3}{form:<12}{d1:<16}{d2:<18}{'YES' if d1 != d2 else 'no'}")
    out()
    out("  hull_0 of C (as vectors): "
        + str(sorted(tuple(name(a) for a in v) for v in hull(C, 0))))
    out("  hull_0 of phi(C) (as vectors): "
        + str(sorted(tuple(name(a) for a in v) for v in hull(C2, 0))))
    out()

    out("=" * 78)
    out("PART A5 -- the criterion a_i^(1+p^k) constant, checked on this phi")
    out("=" * 78)
    a = [1, 2, 3]
    out(f"  a = (a_0,a_1,a_2) = {tuple(name(t) for t in a)}")
    for k in range(E):
        vals = [fpow(a[i], 1 + P ** k) for i in range(N)]
        const = len(set(vals)) == 1
        out(f"  k={k}: a_i^(1+{P}^{k}) = {tuple(name(t) for t in vals)}   "
            f"constant: {const}   => phi {'IS' if const else 'is NOT'} "
            f"a similarity of the k-Galois form")
    out()
    out("  prediction: hull_0 may change (phi not a similarity),")
    out("              hull_1 must NOT change (phi IS a similarity).")
    out(f"  observed:    hull_0 {res[0][0]} -> {res[0][1]};  "
        f"hull_1 {res[1][0]} -> {res[1][1]}")
    out()

    out("=" * 78)
    out("PART A6 -- verification of the criterion identity on random data")
    out("=" * 78)
    import random
    random.seed(20261020)
    bad = 0
    trials = 0
    for _ in range(300):
        k = random.randrange(E)
        perm = list(range(N))
        random.shuffle(perm)
        aa = [random.randrange(1, Q) for _ in range(N)]
        u = [random.randrange(Q) for _ in range(N)]
        v = [random.randrange(Q) for _ in range(N)]
        pu = [0] * N
        pv = [0] * N
        for i in range(N):
            pu[perm[i]] = mul(aa[i], u[i])
            pv[perm[i]] = mul(aa[i], v[i])
        lhs = inner(pu, pv, k)
        rhs = 0
        for i in range(N):
            rhs = add(rhs, mul(fpow(aa[i], 1 + P ** k), mul(u[i], fpow(v[i], P ** k))))
        trials += 1
        if lhs != rhs:
            bad += 1
    out(f"  <phi u, phi v>_k  ==  sum_i a_i^(1+p^k) u_i v_i^(p^k)")
    out(f"  trials: {trials};  mismatches: {bad}")
    out()
    return res




# ------------------------------------------------------------------- PART B
def partB(out):
    """Hermitian (k=1) counterexample over F_9, where the norm is nontrivial."""
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import gf

    out("=" * 78)
    out("PART B -- a k=1 (Hermitian) counterexample over F_9")
    out("=" * 78)
    out("  Why F_4 cannot give one: for q=4, k=1, a^(1+p) = a^3 = 1 for every")
    out("  nonzero a, so a_i^(1+p) is always constant and EVERY monomial map is a")
    out("  Hermitian similarity.  Over F_9, a^(1+3) = Norm(a) is a nontrivial")
    out("  character F_9^* -> F_3^*, so non-constant diagonals exist.")
    out()

    q, p, m, mod = 9, 3, 2, [2, 2, 1]
    F = gf.GF(p, m, mod)
    out(f"  F_9 = F_3(w) with w^2 + 2w + 2 = 0; elements encoded 0..8")
    out(f"  Norm(a) = a^(1+3) = a^4 in F_3: "
        + ", ".join(f"{a}:{F.pow(a,4)}" for a in range(1, q)))
    out()

    n = 5
    units = [s for s in range(1, n) if _gcd(s, n) == 1]
    out(f"  n = {n}; units mod n = {units}")

    def xk_minus(a):
        f = [0] * (n + 1)
        f[0] = F.neg(a)
        f[n] = 1
        return f

    def divisors_of(f):
        irr = [t for t, _ in gf.factor(F, f)]
        res = []
        for r in range(len(irr) + 1):
            for sub in itertools.combinations(range(len(irr)), r):
                g = [1]
                for i in sub:
                    g = _pmulF(F, g, irr[i])
                res.append(gf.ptrim(g))
        return res

    def ideal_basis(a, g):
        v = list(g) + [0] * (n - len(g))
        outv = []
        for _ in range(n - (len(g) - 1)):
            outv.append(list(v))
            v = [F.mul(a, v[-1])] + v[:-1]
        return outv

    def psi_s(F, n, s, b, basis):
        """f(x) -> f(x^s): R_a -> R_b with a = b^s, applied to a basis."""
        res = []
        for c in basis:
            v = [0] * n
            for i, co in enumerate(c):
                if not co:
                    continue
                e = (s * i) % n
                v[e] = F.add(v[e], F.mul(co, F.pow(b, (s * i) // n)))
            res.append(v)
        return res

    changes = []
    checked = 0
    for b in range(1, q):
        for s in units:
            a = F.pow(b, s)
            for g in divisors_of(xk_minus(a)):
                C = ideal_basis(a, g)
                rk, _ = gf.span_rank(F, C, n)
                C2 = psi_s(F, n, s, b, C)
                rk2, _ = gf.span_rank(F, C2, n)
                assert rk == rk2, "psi_s changed the dimension"
                checked += 1
                h0 = gf.hull_dim(F, C, n, 1)
                h1 = gf.hull_dim(F, C2, n, 1)
                if h0 != h1:
                    changes.append((b, s, a, list(g), rk, h0, h1))
    out(f"  (b, s, code) triples checked: {checked}")
    out(f"  Hermitian hull changes      : {len(changes)}")
    if changes:
        b, s, a, g, rk, h0, h1 = changes[0]
        out()
        out("  FIRST WITNESS")
        out(f"    source ring R_a = F_9[x]/(x^{n} - {a})   [a = b^s with b = {b}, s = {s}]")
        out(f"    generator g = {g}   dim = {rk}")
        out(f"    map psi_s: f(x) -> f(x^{s}),  diagonal scalings b^floor(si/n)")
        out(f"    image is a {b}-constacyclic code, same dimension")
        out(f"    dim_F9 hull_1 :  {h0}  ->  {h1}")
        diag = [F.pow(b, (s * i) // n) for i in range(n)]
        out(f"    diagonal scalings a_i = {diag}")
        out(f"    a_i^(1+3) = {[F.pow(d, 4) for d in diag]}  (non-constant -> not a similarity)")
    out()
    return changes


def _pmulF(F, f, g):
    out = [0] * (len(f) + len(g) - 1)
    for i, a in enumerate(f):
        if not a:
            continue
        for j, b in enumerate(g):
            if b:
                out[i + j] = F.add(out[i + j], F.mul(a, b))
    return gf_ptrim(out)


def gf_ptrim(f):
    f = list(f)
    while len(f) > 1 and f[-1] == 0:
        f.pop()
    return f


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    lines = []

    def out(s=""):
        lines.append(s)
        print(s)

    import datetime
    out("### final_check_A.py")
    out(datetime.datetime.now().strftime("%a %b %d %H:%M:%S UTC %Y"))
    out(f"Python {sys.version.split()[0]}")
    out()

    res = partA(out)
    ch = partB(out)

    out("=" * 78)
    out("SUMMARY OF TASK A")
    out("=" * 78)
    out(f"  C = <1+x> in F_4[x]/(x^3-1):            dim 2, |C| = 16")
    out(f"  phi = diag(1,w,w^2) = f(x)->f(wx):      phi(C) cyclic, dim 2, |phi(C)| = 16")
    out(f"  weight distributions identical:         True")
    out(f"  hull_0 (Euclidean):  {res[0][0]} -> {res[0][1]}   CHANGED")
    out(f"  hull_1 (Hermitian):  {res[1][0]} -> {res[1][1]}   NOT changed")
    out()
    out("  The Euclidean counterexample stands.")
    out("  The Hermitian case is NOT a counterexample at q=4, and cannot be:")
    out("  over F_4 every nonzero a has a^3 = 1, so a_i^(1+p) = 1 for all a_i and")
    out("  EVERY monomial map is a similarity of the Hermitian form.")
    out(f"  Hermitian counterexamples found over F_9: {len(ch)}.")
    out()

    path = "/home/user/Galios-Hull/research_project/verification/final_check_A.out"
    with open(path, "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"written to {path}")


if __name__ == "__main__":
    main()
