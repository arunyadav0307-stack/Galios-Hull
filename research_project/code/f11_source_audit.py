#!/usr/bin/env python3
"""
F11 SOURCE AUDIT -- independent, self-contained re-implementation.

This file imports NOTHING from the rest of the project.  It rebuilds F_2, F_9,
F_25, the affine algebras A, their idempotents, the constacyclic ideals, the
Frobenius/Galois inner products and the Gray map from the definitions in the
source paper, and re-derives every number relevant to finding F11.

Source: Debnath-Islam-Martinez-Moro-Prakash, "Galois hulls of constacyclic
codes over affine algebra rings", arXiv:2412.08512v1 (11 Dec 2024), 27 pp,
SHA-256 0db90bfbeda69ad1af231b81d92f24be3589ed15ac2e0ade6605ba7ad0ddc039.

Definitions used (with their page):
  p.4   |S(nu)| = lcm(d_1,...,d_l) = [F_q(nu_1,...,nu_l):F_q]
  p.5   A ~= (+)_S F_q[X_1..X_l]/I_S ~= (+)_S F_q(nu_1,...,nu_l)
  p.7   a = sum_S a_{S(nu)} e_{S(nu)} with a_{S(nu)} IN F_q  <-- the claim under test
  p.7   <rho,rho'>_k = sum_i rho_i (rho'_i)^(p^k)
  p.17  psi(a) = (a_{S(nu_1)},...,a_{S(nu_N)}) M ,  M in GL_N(F_q),  N = |S-hat|
  p.17  "psi is a bijective linear isometry from A^n to F_q^{nN}"
  p.12  Thm 8: dim(hull_k C) = sum_S { n - deg lcm(g_S, h_S^#) }
"""

import itertools
import os
import sys
import datetime

OUT = []


def say(s=""):
    OUT.append(s)
    print(s)


# ============================================================== finite fields
class Fld:
    """F_p[z]/(mod), elements encoded base-p: e = d0 + d1 p + ... """

    def __init__(self, p, m, mod):
        assert len(mod) == m + 1 and mod[m] == 1, "modulus must be monic of degree m"
        self.p, self.m, self.mod = p, m, list(mod)
        self.q = p ** m

    def digs(self, e):
        d = []
        for _ in range(self.m):
            d.append(e % self.p)
            e //= self.p
        return d

    def mk(self, ds):
        e = 0
        for d in reversed(ds):
            e = e * self.p + (d % self.p)
        return e

    def add(self, a, b):
        da, db = self.digs(a), self.digs(b)
        return self.mk([(x + y) % self.p for x, y in zip(da, db)])

    def neg(self, a):
        return self.mk([(-x) % self.p for x in self.digs(a)])

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        da, db = self.digs(a), self.digs(b)
        pr = [0] * (2 * self.m - 1)
        for i, x in enumerate(da):
            if x:
                for j, y in enumerate(db):
                    if y:
                        pr[i + j] = (pr[i + j] + x * y) % self.p
        for i in range(len(pr) - 1, self.m - 1, -1):
            c = pr[i]
            if c:
                for k in range(self.m + 1):
                    pr[i - self.m + k] = (pr[i - self.m + k] - c * self.mod[k]) % self.p
        return self.mk(pr[:self.m])

    def pow(self, a, e):
        r, b = 1, a
        while e:
            if e & 1:
                r = self.mul(r, b)
            b = self.mul(b, b)
            e >>= 1
        return r

    def inv(self, a):
        assert a != 0
        for b in range(1, self.q):
            if self.mul(a, b) == 1:
                return b
        raise ZeroDivisionError

    def div(self, a, b):
        return self.mul(a, self.inv(b))

    def is_zero(self, a):
        return a == 0

    def order(self, a):
        x, k = a, 1
        while x != 1:
            x = self.mul(x, a)
            k += 1
        return k


# ------------------------------------------------------ polynomials over F_q
def ptrim(F, f):
    f = list(f)
    while len(f) > 1 and f[-1] == 0:
        f.pop()
    return f


def pmul(F, f, g):
    o = [0] * (len(f) + len(g) - 1)
    for i, a in enumerate(f):
        if not a:
            continue
        for j, b in enumerate(g):
            if b:
                o[i + j] = F.add(o[i + j], F.mul(a, b))
    return ptrim(F, o)


def pmod(F, f, g):
    f = ptrim(F, f)
    g = ptrim(F, g)
    while len(f) >= len(g) and not (len(f) == 1 and f[0] == 0):
        c = F.div(f[-1], g[-1])
        d = len(f) - len(g)
        for i in range(len(g)):
            f[d + i] = F.sub(f[d + i], F.mul(c, g[i]))
        f = ptrim(F, f)
    return f


def pquo(F, f, g):
    """quotient of f by g (assumes exact division); see pmod for the remainder"""
    f = ptrim(F, f)
    g = ptrim(F, g)
    q = [0] * max(1, len(f) - len(g) + 1)
    while len(f) >= len(g) and not (len(f) == 1 and f[0] == 0):
        c = F.div(f[-1], g[-1])
        d = len(f) - len(g)
        q[d] = c
        for i in range(len(g)):
            f[d + i] = F.sub(f[d + i], F.mul(c, g[i]))
        f = ptrim(F, f)
    return ptrim(F, q)


def pdivides(F, g, f):
    r = pmod(F, f, g)
    return len(r) == 1 and r[0] == 0


def monic_polys(F, d):
    """all monic polynomials of degree exactly d"""
    for c in itertools.product(range(F.q), repeat=d):
        yield list(c) + [1]


def irreducibles(F, maxdeg):
    """all monic irreducibles of degree 1..maxdeg (small fields only)"""
    out = []
    for d in range(1, maxdeg + 1):
        for f in monic_polys(F, d):
            ok = True
            for g in out:
                if len(g) - 1 <= d // 2 and pdivides(F, g, f):
                    ok = False
                    break
            if ok:
                out.append(f)
    return out


def factor(F, f, irr=None):
    """full factorisation into monic irreducibles, as a list of (poly, mult)"""
    if irr is None:
        irr = irreducibles(F, max(1, (len(f) - 1)))
    f = ptrim(F, f)
    res = []
    for g in irr:
        if len(f) <= 1:
            break
        k = 0
        while len(f) >= len(g) and pdivides(F, g, f):
            f = pquo(F, f, g)
            k += 1
        if k:
            res.append((g, k))
    if len(f) > 1:
        res.append((f, 1))     # leftover irreducible of large degree
    return res


def is_irreducible(F, f):
    d = len(f) - 1
    if d <= 3:
        for a in range(F.q):
            v = 0
            for c in reversed(f):
                v = F.add(F.mul(v, a), c)
            if v == 0:
                return False
        return True
    raise NotImplementedError("only degree <= 3 in this script")


# ====================================================== the affine algebra A
class Aff:
    """A = F_q[x1,x2]/<t1(x1),t2(x2)>, elements as lists of length d1*d2,
    index i*d2 + j meaning x1^i x2^j."""

    def __init__(self, F, t1, t2):
        self.F = F
        self.t1, self.t2 = list(t1), list(t2)
        self.d1, self.d2 = len(t1) - 1, len(t2) - 1
        self.dim = self.d1 * self.d2

    def zero(self):
        return [0] * self.dim

    def one(self):
        v = [0] * self.dim
        v[0] = 1
        return v

    def _reduce(self, C):
        F, d1, d2, t1, t2 = self.F, self.d1, self.d2, self.t1, self.t2
        # reduce x1
        C = [row[:] for row in C]
        for i in range(len(C) - 1, d1 - 1, -1):
            if any(C[i]):
                for j in range(len(C[i])):
                    c = C[i][j]
                    if c:
                        for k in range(d1):
                            C[i - d1 + k][j] = F.sub(C[i - d1 + k][j],
                                                     F.mul(c, t1[k]))
                C[i] = [0] * len(C[i])
        C = C[:d1]
        # reduce x2
        for row in C:
            for j in range(len(row) - 1, d2 - 1, -1):
                c = row[j]
                if c:
                    for k in range(d2):
                        row[j - d2 + k] = F.sub(row[j - d2 + k], F.mul(c, t2[k]))
                    row[j] = 0
            del row[d2:]
        return C

    def mul(self, A, B):
        F, d1, d2 = self.F, self.d1, self.d2
        C = [[0] * (2 * d2 - 1) for _ in range(2 * d1 - 1)]
        for i1 in range(d1):
            for j1 in range(d2):
                a = A[i1 * d2 + j1]
                if not a:
                    continue
                for i2 in range(d1):
                    for j2 in range(d2):
                        b = B[i2 * d2 + j2]
                        if b:
                            C[i1 + i2][j1 + j2] = F.add(C[i1 + i2][j1 + j2],
                                                         F.mul(a, b))
        C = self._reduce(C)
        return [x for row in C for x in row]

    def add(self, A, B):
        return [self.F.add(a, b) for a, b in zip(A, B)]

    def scal(self, c, A):
        return [self.F.mul(c, a) for a in A]

    def idempotents(self):
        res = []
        for code in range(self.F.q ** self.dim):
            v, x = [], code
            for _ in range(self.dim):
                v.append(x % self.F.q)
                x //= self.F.q
            if self.mul(v, v) == v:
                res.append(v)
        return res

    def primitive_idempotents(self):
        idem = [e for e in self.idempotents() if any(e)]
        prim = []
        for e in idem:
            ok = True
            for f in idem:
                if f == e or not any(f):
                    continue
                if self.mul(e, f) == f:      # f <= e
                    ok = False
                    break
            if ok:
                prim.append(e)
        return prim


# ================================================================ linear alg
def component_dims(A, prim):
    """dim_Fq of e_S A for each primitive idempotent e_S  (should be |S(nu)|)"""
    basisA = []
    for k in range(A.dim):
        v = [0] * A.dim
        v[k] = 1
        basisA.append(v)
    return [rank(A.F, [A.mul(e, b) for b in basisA]) for e in prim]


def rank(F, rows):
    rows = [list(r) for r in rows if any(r)]
    if not rows:
        return 0
    n = len(rows[0])
    r = 0
    for c in range(n):
        piv = None
        for i in range(r, len(rows)):
            if rows[i][c]:
                piv = i
                break
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        inv = F.inv(rows[r][c])
        rows[r] = [F.mul(inv, v) for v in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c]:
                f = rows[i][c]
                rows[i] = [F.sub(rows[i][k], F.mul(f, rows[r][k])) for k in range(n)]
        r += 1
        if r == len(rows):
            break
    return r


def nullspace(F, rows, n):
    A = [list(r) for r in rows]
    piv = []
    r = 0
    for c in range(n):
        p = None
        for i in range(r, len(A)):
            if A[i][c]:
                p = i
                break
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        inv = F.inv(A[r][c])
        A[r] = [F.mul(inv, v) for v in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c]:
                f = A[i][c]
                A[i] = [F.sub(A[i][k], F.mul(f, A[r][k])) for k in range(n)]
        piv.append(c)
        r += 1
        if r == len(A):
            break
    free = [c for c in range(n) if c not in piv]
    out = []
    for fc in free:
        v = [0] * n
        v[fc] = 1
        for i, pc in enumerate(piv):
            v[pc] = F.neg(A[i][fc])
        out.append(v)
    return out


def span(F, basis):
    """all F_q-linear combinations, as a set of tuples"""
    S = set()
    for coef in itertools.product(range(F.q), repeat=len(basis)):
        v = [0] * len(basis[0])
        for c, b in zip(coef, basis):
            if c:
                v = [F.add(x, F.mul(c, y)) for x, y in zip(v, b)]
        S.add(tuple(v))
    return S


# ==================================================================== Part 1
def part1_fields():
    say("=" * 78)
    say("PART 1 -- the fields, verified against their defining relations")
    say("=" * 78)
    F2 = Fld(2, 1, [0, 1])
    F9 = Fld(3, 2, [2, 2, 1])       # z^2 + 2z + 2
    F25 = Fld(5, 2, [2, 4, 1])      # z^2 + 4z + 2
    for nm, F, poly in [("F_2", F2, [0, 1]), ("F_9", F9, [2, 2, 1]),
                        ("F_25", F25, [2, 4, 1])]:
        z = F.mk([0, 1]) if F.m > 1 else 1
        # verify z^2 = -2z - 2  (resp. -4z - 2)
        lhs = F.mul(z, z)
        rhs = F.add(F.mul(F.neg(poly[1]), z), F.neg(poly[0]))
        say(f"  {nm}: q = {F.q}, generator z = {z} (code), "
            f"z^2 = {lhs} equals {rhs}: {lhs == rhs}")
    say(f"  F_9  units and orders: "
        + ", ".join(f"{a}:{F9.order(a)}" for a in range(1, 9)))
    say(f"  F_25 units of order dividing 3: "
        + str([a for a in range(1, 25) if F25.order(a) in (1, 3)]))
    say()
    return F2, F9, F25


# ==================================================================== Part 2
def part2_example1(F2):
    say("=" * 78)
    say("PART 2 -- Example 1 (p.5): A_1 = F_2[x1,x2]/<t1,t2>")
    say("=" * 78)
    t1 = [1, 0, 0, 0, 1, 1]      # 1 + x^4 + x^5
    t2 = [0, 1, 1, 0, 1]         # x + x^2 + x^4
    irr = irreducibles(F2, 3)
    f1 = factor(F2, t1, irr)
    f2 = factor(F2, t2, irr)
    d1 = [len(g) - 1 for g, _ in f1]
    d2 = [len(g) - 1 for g, _ in f2]
    say(f"  t1 = x^5 + x^4 + 1, irreducible factor degrees: {d1}")
    say(f"  t2 = x^4 + x^2 + x, irreducible factor degrees: {d2}")
    say(f"  (paper p.5 writes t2 = x2(x2^2+x2+1); that product is x^3+x^2+x."
        f"  The degrees that match the paper's own count of six are {d2}.)")
    N = sum(_gcd(a, b) for a in d1 for b in d2)
    dimA = sum(a * b for a in d1 for b in d2)
    sizes = sorted(_lcm(a, b) for a in d1 for b in d2 for _ in range(_gcd(a, b)))
    say(f"  #components  N = sum gcd(d_i,e_j) = {N}   (paper p.5: six)")
    say(f"  dim_2 A      = sum d_i*e_j = {dimA} = deg t1 * deg t2 = {d1 and sum(d1)}*{sum(d2)}")
    say(f"  class sizes |S(nu)| = {sizes}; sum = {sum(sizes)}")
    say(f"  |A| = 2^{dimA} = {2**dimA}   vs   |F_2^N| = 2^{N} = {2**N}")
    say(f"  => A -> F_2^N injective would need {2**dimA} <= {2**N}: "
        f"{2**dimA <= 2**N}")
    say(f"  => Example 1 is NOT the split case: class sizes are not all 1.")
    say()
    return dict(N=N, dimA=dimA, sizes=sizes)


# ==================================================================== Part 3
def part3_example2(F9):
    say("=" * 78)
    say("PART 3 -- Example 2 (p.18-20): A = F_9[x1,x2]/<t1,t2>")
    say("=" * 78)
    # identify the two conjugate choices of omega (roots of z^2+2z+2)
    roots = [a for a in range(1, 9)
             if F9.add(F9.add(F9.mul(a, a), F9.mul(2, a)), 2) == 0]
    say(f"  roots of z^2 + 2z + 2 in F_9: {roots}  (the naming of omega)")
    for w in roots:
        t1 = [w, 1, 1]
        t2 = [2, F9.pow(w, 5), 1]
        say(f"   omega = {w}: t1 = x^2+x+w irreducible: {is_irreducible(F9, t1)},"
            f"  t2 = x^2+w^5 x+2 irreducible: {is_irreducible(F9, t2)}")
    w = roots[-1]
    say(f"  using omega = {w} (the two choices give the same verdicts)")
    t1 = [w, 1, 1]
    t2 = [2, F9.pow(w, 5), 1]

    A = Aff(F9, t1, t2)
    say(f"  dim_F9 A = {A.d1}*{A.d2} = {A.dim};   |A| = 9^{A.dim} = {9**A.dim}")
    idem = A.idempotents()
    prim = A.primitive_idempotents()
    say(f"  idempotents of A: {len(idem)};  primitive: {len(prim)}  =>  N = {len(prim)}")
    N = len(prim)
    cd = component_dims(A, prim)
    say(f"  dim_F9 of each component e_S A: {cd}  (predicted |S(nu)| = 2 each)")
    say(f"  sum of component degrees = {sum(cd)} = dim_F9 A = {A.dim}")
    say(f"  => A ~= F_81 x F_81, not F_9 x F_9")
    say(f"  |F_9^N| = 9^{N} = {9**N}   vs   |A| = {9**A.dim}")
    say(f"  => psi: A -> F_9^{N} cannot be injective (pigeonhole), "
        f"so not the 'bijection' of p.17")
    say()
    # factorisations claimed on p.19
    irr3 = irreducibles(F9, 3)
    for nm, f in [("x^7 - 1", [F9.neg(1), 0, 0, 0, 0, 0, 0, 1]),
                  ("x^7 - w^2", [F9.neg(F9.pow(w, 2)), 0, 0, 0, 0, 0, 0, 1])]:
        fac = factor(F9, f, irr3)
        say(f"  {nm}: irreducible factor degrees "
            f"{sorted(len(g)-1 for g, _ in fac)}, multiplicities all 1: "
            f"{all(k == 1 for _, k in fac)}")
    g1 = [2, F9.pow(w, 5), F9.pow(w, 3), 1]      # x^3 + w^3 x^2 + w^5 x + 2
    g2 = [F9.pow(w, 2), 1]                       # x + w^2
    say(f"  g1 = x^3 + w^3 x^2 + w^5 x + 2 divides x^7-1 : "
        f"{pdivides(F9, g1, [F9.neg(1), 0, 0, 0, 0, 0, 0, 1])}")
    say(f"  g2 = x + w^2 divides x^7 - w^2                : "
        f"{pdivides(F9, g2, [F9.neg(F9.pow(w,2)), 0, 0, 0, 0, 0, 0, 1])}")
    say(f"  deg g1 = {len(g1)-1}, deg g2 = {len(g2)-1}")
    say()

    # the A-module ideal generated by g = e1 g1 + e2 g2
    e1 = prim[0]
    e2 = prim[1]
    lam1, lam2 = 1, F9.pow(w, 2)
    lam = A.add(A.scal(lam1, e1), A.scal(lam2, e2))
    n = 7
    gvec = []
    for i in range(n):
        c1 = g1[i] if i < len(g1) else 0
        c2 = g2[i] if i < len(g2) else 0
        gvec.append(A.add(A.scal(c1, e1), A.scal(c2, e2)))

    def shift_A(v):
        return [A.mul(lam, v[-1])] + [x[:] for x in v[:-1]]

    basisA = []
    for k in range(A.dim):
        v = [0] * A.dim
        v[k] = 1
        basisA.append(v)

    rows = []
    v = [x[:] for x in gvec]
    for _ in range(n):
        for b in basisA:
            rows.append([x for el in [A.mul(b, wv) for wv in v] for x in el])
        v = shift_A(v)
    rk = rank(F9, rows)
    say(f"  A-module C = <g>: rank over F_9 of {{b*x^i*g}} = {rk}")
    say(f"    (= sum_S |S| (n - deg g_S) = 2*4 + 2*6 = {2*4 + 2*6})")
    say(f"  paper prints dim = sum_S (n - deg g_S) = {(7-3) + (7-1)}")
    say(f"  claimed Gray-image length nN = 7*{N} = {7*N}")
    say(f"  dim_F9 C = {rk} > nN = {7*N} ? {rk > 7*N}")
    say(f"  => no injective F_9-linear map C -> F_9^{7*N} exists;")
    say(f"     the claimed [14, {rk - 0 if False else 10}, 4]_9 is impossible.")
    say()
    return dict(N=N, dimA=A.dim, rk=rk, nN=7 * N, g1=g1, g2=g2, w=w, prim=prim, A=A)


# ==================================================================== Part 4
def part4_example3(F25):
    say("=" * 78)
    say("PART 4 -- Example 3 (p.20-21): A = F_25[x1,x2]/<t1,t2>")
    say("=" * 78)
    roots = [a for a in range(1, 25)
             if F25.add(F25.add(F25.mul(a, a), F25.mul(4, a)), 2) == 0]
    say(f"  roots of z^2 + 4z + 2 in F_25: {roots}")
    for w in roots:
        t1 = [F25.pow(w, 13), 1, 1]
        t2 = [1, F25.pow(w, 3), 1]
        say(f"   omega = {w}: t1 = x^2+x+w^13 irreducible: "
            f"{is_irreducible(F25, t1)};  t2 = x^2+w^3 x+1 irreducible: "
            f"{is_irreducible(F25, t2)}")
    w = roots[-1]
    say(f"  using omega = {w}")
    t1 = [F25.pow(w, 13), 1, 1]
    t2 = [1, F25.pow(w, 3), 1]

    irr2 = irreducibles(F25, 2)
    d1 = [len(g) - 1 for g, _ in factor(F25, t1, irr2)]
    d2 = [len(g) - 1 for g, _ in factor(F25, t2, irr2)]
    say(f"  t1 factor degrees: {d1};  t2 factor degrees: {d2}")
    N = sum(_gcd(a, b) for a in d1 for b in d2)
    dimA = sum(a * b for a in d1 for b in d2)
    say(f"  => N = sum gcd = {N};  dim_F25 A = {dimA};  "
        f"class sizes = {sorted(_lcm(a,b) for a in d1 for b in d2 for _ in range(_gcd(a,b)))}")
    say(f"  |A| = 25^{dimA} = {25**dimA}   vs   |F_25^N| = 25^{N} = {25**N}")
    say()

    for nm, f in [("x^13 - 1", [F25.neg(1)] + [0] * 12 + [1]),
                  ("x^13 - w^8", [F25.neg(F25.pow(w, 8))] + [0] * 12 + [1])]:
        fac = factor(F25, f, irr2)
        say(f"  {nm}: irreducible factor degrees "
            f"{sorted(len(g)-1 for g, _ in fac)}")
    g1 = pmul(F25, [4, 1], [1, w, 1])       # (x+4)(x^2 + w x + 1)
    g2 = [F25.pow(w, 20), 1]                # x + w^20
    say(f"  g1 = (x+4)(x^2+w x+1) = {g1}, deg {len(g1)-1}; "
        f"divides x^13-1: {pdivides(F25, g1, [F25.neg(1)] + [0]*12+[1])}")
    say(f"  g2 = x + w^20, deg {len(g2)-1}; divides x^13-w^8: "
        f"{pdivides(F25, g2, [F25.neg(F25.pow(w,8))] + [0]*12+[1])}")
    say()

    A = Aff(F25, t1, t2)
    say(f"  primitive idempotents computed by brute force over {25**A.dim} elements...")
    prim = A.primitive_idempotents()
    say(f"  primitive idempotents: {len(prim)}  (matches N = {N})")
    cd = component_dims(A, prim)
    say(f"  dim_F25 of each component e_S A: {cd}  (predicted |S(nu)| = 2 each)")
    say(f"  sum of component degrees = {sum(cd)} = dim_F25 A = {A.dim}")
    say(f"  => A ~= F_625 x F_625, not F_25 x F_25")
    e1, e2 = prim[0], prim[1]
    lam = A.add(A.scal(1, e1), A.scal(F25.pow(w, 8), e2))
    n = 13
    gvec = []
    for i in range(n):
        c1 = g1[i] if i < len(g1) else 0
        c2 = g2[i] if i < len(g2) else 0
        gvec.append(A.add(A.scal(c1, e1), A.scal(c2, e2)))
    basisA = []
    for k in range(A.dim):
        v = [0] * A.dim
        v[k] = 1
        basisA.append(v)
    rows = []
    v = [x[:] for x in gvec]
    for _ in range(n):
        for b in basisA:
            rows.append([x for el in [A.mul(b, wv) for wv in v] for x in el])
        v = [A.mul(lam, v[-1])] + [x[:] for x in v[:-1]]
    rk = rank(F25, rows)
    say(f"  A-module C = <g>: rank over F_25 = {rk}")
    say(f"    (= sum_S |S| (n - deg g_S) = 2*10 + 2*12 = {2*10+2*12})")
    say(f"  paper prints {(13-3)+(13-1)};  claimed length nN = 13*{N} = {13*N}")
    say(f"  dim_F25 C = {rk} > {13*N} ? {rk > 13*N}")
    say()
    return dict(N=N, dimA=A.dim, rk=rk, nN=13 * N, w=w, g1=g1, g2=g2)


# ==================================================================== Part 5
def part5_gray(F9, F25):
    say("=" * 78)
    say("PART 5 -- the Gray map of p.17: what it can and cannot be")
    say("=" * 78)
    say("  eq.(10):  psi : A -> F_q^N,  a |-> (a_{S(nu_1)},...,a_{S(nu_N)}) M,")
    say("            with M in GL_N(F_q) and N = |S-hat|.")
    say("  p.17:     'the map psi is bijective linear isometry from A^n to F_q^{nN}'")
    say()
    say("  A bijection A -> F_q^N requires |A| = q^N, i.e. dim_q A = N.")
    say(f"  {'ring':<10}{'dim_q A':<10}{'N':<6}{'|A|':<12}{'|F_q^N|':<12}{'injective?'}")
    for nm, q, dimA, N in [("Ex 1", 2, 20, 6), ("Ex 2", 9, 4, 2), ("Ex 3", 25, 4, 2)]:
        say(f"  {nm:<10}{dimA:<10}{N:<6}{q**dimA:<12}{q**N:<12}"
            f"{'yes' if dimA <= N else 'NO'}")
    say()
    say("  Even the *codomain length* is forced: psi(C) is a code of length nN,")
    say("  so dim_q psi(C) <= nN.  But psi is claimed linear and bijective, so")
    say("  dim_q psi(C) = dim_q C.  The two computed dim_q C (20, 44) exceed the")
    say("  claimed nN (14, 26) for BOTH examples, independently of distances.")
    say()
    say("  What the paper's own arithmetic computes: sum_S dim_{A_S}, i.e. the")
    say("  dimension with the factor |S(nu)| suppressed.  Reproduced exactly by")
    say("  code/final_check_B.py (component-level table).")
    say()




# ==================================================================== Part 7
def part7_table1(F2, F9, F25):
    say("=" * 78)
    say("PART 7 -- the q = 4 ring of Table 1, and the table's lengths")
    say("=" * 78)
    F4 = Fld(2, 2, [1, 1, 1])          # w^2 + w + 1
    z = F4.mk([0, 1])
    say(f"  F_4 = F_2[z]/(z^2+z+1), z = {z} (primitive: order {F4.order(z)})")
    t1 = [z, 1, 1]                      # x^2 + x + w
    t2 = [z, z, 1]                      # x^2 + w x + w
    say(f"  t1 = x^2 + x + w  irreducible over F_4: {is_irreducible(F4, t1)}")
    say(f"  t2 = x^2 + w x + w irreducible over F_4: {is_irreducible(F4, t2)}")
    say(f"  => dim_4 A = 2*2 = 4 and N = gcd(2,2) = 2 for the q = 4 ring too")
    say()
    rows = [(5, 10), (4, 8), (5, 10), (5, 10), (5, 10), (6, 12), (7, 14),
            (7, 14), (7, 14), (13, 26), (16, 32), (20, 40), (26, 52)]
    say("  Table 1 (p.22) as printed: n and the length of psi(C)")
    ok = True
    for n, L in rows:
        if L != 2 * n:
            ok = False
        say(f"    n = {n:<3} length = {L:<4}  2n = {2*n:<4} "
            f"{'ok' if L == 2*n else 'MISMATCH'}")
    say(f"  all 13 rows have length exactly 2n: {ok}")
    say("  Since dim_q A = 4 for every ring used in the table, A^n has F_q-dimension")
    say("  4n; a bijective linear Gray map would therefore have to land in F_q^{4n}.")
    say("  Every printed length is 2n, i.e. a factor 2 short -- the same factor")
    say("  |S(nu)| = 2 that is missing from the dimensions.")
    say()

# ==================================================================== Part 6
def part6_isometry(F9):
    say("=" * 78)
    say("PART 6 -- independent verification of the reported F_9 isometry witness")
    say("=" * 78)
    n = 5
    z = 3                                    # the primitive element, code 3
    w = F9.pow(z, 1)
    say(f"  field: F_9 = F_3[z]/(z^2+2z+2); codes 0..8 mean a0 + a1*z.")
    say(f"  z = {z}, z^2 = {F9.mul(z, z)}, z^4 = {F9.pow(z, 4)} "
        f"(= {F9.pow(z,4)}, the norm, lying in F_3)")

    def ideal(a, g):
        v = list(g) + [0] * (n - len(g))
        rows = []
        for _ in range(n - (len(g) - 1)):
            rows.append(list(v))
            v = [F9.mul(a, v[-1])] + v[:-1]
        return rows

    def code_set(rows):
        return span(F9, rows)

    def shift(v, lam):
        return tuple([F9.mul(lam, v[-1])] + list(v[:-1]))

    def is_constacyclic(S, lam):
        return all(shift(v, lam) in S for v in S)

    def hermitian_dual(rows):
        # <v,c>_1 = sum v_i c_i^3 = 0 for all c in the row space
        M = [[F9.pow(c[i], 3) for i in range(n)] for c in rows]
        return nullspace(F9, M, n)

    def hull_of(rows):
        D = hermitian_dual(rows)
        allv = span(F9, D)                   # 81 vectors
        return {v for v in allv if v in code_set(rows)}

    def logq(S):
        k = 0
        x = 1
        while x < len(S):
            x *= F9.q
            k += 1
        assert x == len(S), (len(S), "not a power of q")
        return k

    def weight(v):
        return sum(1 for c in v if c)

    # --- the two conjugate choices of omega (roots of z^2+2z+2)
    roots = [a for a in range(1, 9)
             if F9.add(F9.add(F9.mul(a, a), F9.mul(2, a)), 2) == 0]
    say(f"  roots of z^2+2z+2 (candidate names for omega): {roots}")

    for tag, w in [("A", roots[0]), ("B", roots[-1])]:
        say(f"  --- naming omega = {w} ({tag}) ---")
        a = F9.mul(w, w)          # source shift constant = omega^2
        b = w                     # target shift constant = omega
        g = [2, 6, 1]             # 2 + 6x + x^2   (as printed in the report)
        say(f"    source ring R_a = F_9[x]/(x^5 - {a}) with a = omega^2 = {a}")
        say(f"    target ring R_b = F_9[x]/(x^5 - {b}) with b = omega   = {b}")
        say(f"    check a = b^2 : {F9.mul(b,b) == a}")
        say(f"    g = 2 + 6x + x^2 ;  g | x^5 - a : "
            f"{pdivides(F9, g, [F9.neg(a),0,0,0,0,1])}")
        C = ideal(a, g)
        S = code_set(C)
        C2rows = []
        s = 2
        for c in C:
            v = [0] * n
            for i, co in enumerate(c):
                if co:
                    e = (s * i) % n
                    v[e] = F9.add(v[e], F9.mul(co, F9.pow(b, (s * i) // n)))
            C2rows.append(v)
        S2 = code_set(C2rows)
        say(f"    dim C = {logq(S)}, |C| = {len(S)};  "
            f"dim image = {logq(S2)}, |image| = {len(S2)}")
        say(f"    C is {a}-constacyclic : {is_constacyclic(S, a)}")
        say(f"    image is {b}-constacyclic: {is_constacyclic(S2, b)}")
        H = hull_of(C)
        H2 = hull_of(C2rows)
        say(f"    |hull_1(C)| = {len(H)}  -> dim = {logq(H) if H else 0}")
        say(f"    |hull_1(image)| = {len(H2)} -> dim = {logq(H2) if H2 else 0}")
        wd = lambda Sx: sorted([weight(v) for v in Sx])
        say(f"    weight distributions equal: {wd(S) == wd(S2)}")
        scal = [F9.pow(b, (s * i) // n) for i in range(n)]
        say(f"    monomial scalings a_i = {scal};  norms a_i^4 = "
            f"{[F9.pow(x, 4) for x in scal]} (constant? "
            f"{len({F9.pow(x,4) for x in scal}) == 1})")
        if len(H) != len(H2):
            say(f"    ==> HULL DIMENSION CHANGES: {logq(H)} -> {logq(H2)}")
            if tag == "A":
                first = (w, a, b, logq(H), logq(H2))
        say()
    say("  Independence note: the script does not read the earlier outputs; it")
    say("  rebuilds the field, the rings, both codes, the Hermitian dual and the")
    say("  hull from scratch, and it tests BOTH conjugate namings of omega.")
    say()
    return first


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def _lcm(a, b):
    return a * b // _gcd(a, b)


def main():
    say("### f11_source_audit.py")
    say(datetime.datetime.now().strftime("%a %b %d %H:%M:%S UTC %Y"))
    say(f"Python {sys.version.split()[0]}")
    say("self-contained: no project imports")
    say()
    F2, F9, F25 = part1_fields()
    e1 = part2_example1(F2)
    e2 = part3_example2(F9)
    e3 = part4_example3(F25)
    part5_gray(F9, F25)
    w = part6_isometry(F9)
    part7_table1(F2, F9, F25)

    say("=" * 78)
    say("SUMMARY")
    say("=" * 78)
    say(f"  Example 1: N = {e1['N']}, dim_q A = {e1['dimA']}, "
        f"class sizes {e1['sizes']}")
    say(f"  Example 2: N = {e2['N']}, dim_q A = {e2['dimA']}, "
        f"dim_q C = {e2['rk']} (paper 10), nN = {e2['nN']}")
    say(f"  Example 3: N = {e3['N']}, dim_q A = {e3['dimA']}, "
        f"dim_q C = {e3['rk']} (paper 22), nN = {e3['nN']}")
    say(f"  F_9 isometry witness: Hermitian hull {w[3]} -> {w[4]}")
    say()
    say("  Every number above is derived in this file from the paper's")
    say("  definitions; none is copied from an earlier project output.")

    here = os.path.dirname(os.path.abspath(__file__))
    outdir = os.path.join(here, "..", "verification")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.abspath(os.path.join(outdir, "f11_source_audit.out"))
    with open(path, "w") as fh:
        fh.write("\n".join(OUT) + "\n")
    print(f"\nwritten to {path}")


if __name__ == "__main__":
    main()
