"""
Minimal exact finite-field / polynomial / linear-code library.

Purpose: independent re-computation for the Phase 1B source audit of
Debnath, Islam, Martinez-Moro, Prakash, "Galois hulls of constacyclic codes
over affine algebra rings" (arXiv:2412.08512v1).

No external dependencies. Everything is exact integer arithmetic mod p.

Element representation
----------------------
GF(p, m, modulus) with modulus a monic irreducible polynomial of degree m.
An element of GF(p^m) is an integer 0 <= e < p^m whose base-p digits are the
coefficients of the representative polynomial in the generator alpha.

Polynomial representation
-------------------------
A polynomial over GF(p^m) is a list of GF elements, index = exponent,
least significant first, with no trailing zero (except the zero polynomial [0]).
"""


class GF:
    def __init__(self, p, m, modulus):
        assert modulus[-1] == 1, "modulus must be monic"
        self.p, self.m = p, m
        self.q = p ** m
        self.mod = list(modulus)
        d = len(modulus)-1
        assert d == m
        # tables
        self._mul = [[None]*self.q for _ in range(self.q)]

    # ---------- coefficient <-> element ----------
    def digits(self, e):
        out = []
        for _ in range(self.m):
            out.append(e % self.p)
            e //= self.p
        return out

    def from_digits(self, ds):
        e = 0
        for i in range(len(ds)-1, -1, -1):
            e = e*self.p + (ds[i] % self.p)
        return e

    # ---------- field ops ----------
    def add(self, a, b):
        p, out, sh = self.p, 0, 1
        for _ in range(self.m):
            out += ((a % p + b % p) % p) * sh
            a //= p
            b //= p
            sh *= p
        return out

    def neg(self, a):
        p, out, sh = self.p, 0, 1
        for _ in range(self.m):
            out += ((-(a % p)) % p) * sh
            a //= p
            sh *= p
        return out

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        c = self._mul[a][b]
        if c is not None:
            return c
        p, m, mod = self.p, self.m, self.mod
        da, db = self.digits(a), self.digits(b)
        tmp = [0]*(2*m-1)
        for i in range(m):
            if da[i] == 0:
                continue
            for j in range(m):
                if db[j]:
                    tmp[i+j] = (tmp[i+j] + da[i]*db[j]) % p
        # reduce by mod: x^m = -(mod[0..m-1])
        for k in range(2*m-2, m-1, -1):
            coef = tmp[k]
            if coef:
                for i in range(m):
                    tmp[k-m+i] = (tmp[k-m+i] - coef*mod[i]) % p
        out = self.from_digits(tmp[:m])
        self._mul[a][b] = out
        self._mul[b][a] = out
        return out

    def pow(self, a, e):
        assert e >= 0
        r, b = 1, a
        while e:
            if e & 1:
                r = self.mul(r, b)
            b = self.mul(b, b)
            e >>= 1
        return r

    def inv(self, a):
        assert a != 0
        return self.pow(a, self.q-2)

    def is_zero(self, a):
        return a == 0


# ---------------------------------------------------------------- polynomials
def ptrim(f):
    while len(f) > 1 and f[-1] == 0:
        f.pop()
    return f


def pzero():
    return [0]


def pone():
    return [1]


def pdeg(f):
    return len(ptrim(list(f)))-1 if any(f) else -1


def padd(F, f, g):
    n = max(len(f), len(g))
    out = [0]*n
    for i in range(n):
        a = f[i] if i < len(f) else 0
        b = g[i] if i < len(g) else 0
        out[i] = F.add(a, b)
    return ptrim(out)


def pneg(F, f):
    return ptrim([F.neg(a) for a in f])


def psub(F, f, g):
    return padd(F, f, pneg(F, g))


def pmul(F, f, g):
    if not any(f) or not any(g):
        return [0]
    out = [0]*(len(f)+len(g)-1)
    for i, a in enumerate(f):
        if not a:
            continue
        for j, b in enumerate(g):
            if b:
                out[i+j] = F.add(out[i+j], F.mul(a, b))
    return ptrim(out)


def pscalar(F, c, f):
    return ptrim([F.mul(c, a) for a in f])


def pdivmod(F, f, g):
    """returns (quotient, remainder) over GF"""
    assert any(g), "division by zero polynomial"
    f = list(ptrim(list(f)))
    g = ptrim(list(g))
    dg = len(g)-1
    if len(f) < len(g):
        return [0], ptrim(f)
    inv_lc = F.inv(g[-1])
    quo = [0]*(len(f)-dg)
    rem = list(f)
    for k in range(len(f)-1, dg-1, -1):
        coef = rem[k]
        if coef:
            c = F.mul(coef, inv_lc)
            quo[k-dg] = c
            for i in range(dg+1):
                rem[k-dg+i] = F.sub(rem[k-dg+i], F.mul(c, g[i]))
    return ptrim(quo), ptrim(rem[:dg] if dg > 0 else [0])


def pmod(F, f, g):
    return pdivmod(F, f, g)[1]


def pgcd(F, f, g):
    f = ptrim(list(f))
    g = ptrim(list(g))
    while any(g):
        f, g = g, pmod(F, f, g)
    # normalize monic
    if any(f):
        inv = F.inv(f[-1])
        f = pscalar(F, inv, f)
    return f if any(f) else [0]


def plcm(F, f, g):
    if not any(f) or not any(g):
        return [0]
    q, _ = pdivmod(F, pmul(F, f, g), pgcd(F, f, g))
    return pscalar(F, F.inv(q[-1]), q)


def ppowmod(F, base, e, mod):
    r = [1]
    b = pmod(F, base, mod)
    while e:
        if e & 1:
            r = pmod(F, pmul(F, r, b), mod)
        b = pmod(F, pmul(F, b, b), mod)
        e >>= 1
    return r


def pderiv(F, f):
    out = []
    for i in range(1, len(f)):
        c = f[i]
        # coefficient i in char p maps to i mod p
        k = i % F.p
        out.append(F.mul(c, k) if k else 0)
    return ptrim(out) if out else [0]


# ---------------------------------------------------------- irreducibility
def is_irreducible(F, f):
    f = ptrim(list(f))
    d = len(f)-1
    if d <= 0:
        return False
    if f[-1] != 1:
        inv = F.inv(f[-1])
        f = pscalar(F, inv, f)
    # gcd(x^{q^i} - x, f) == 1 for i = 1..floor(d/2)
    x = [0, 1]
    h = x
    for i in range(1, d//2 + 1):
        h = ppowmod(F, h, F.q, f)          # h <- h^q mod f
        g = pgcd(F, psub(F, h, x), f)
        if len(g)-1 > 0:
            return False
    return True


def factor_squarefree_distinct(F, f):
    """full irreducible factorization of monic f (no multiplicities handled
    separately); returns list of monic irreducible factors WITH multiplicity."""
    f = ptrim(list(f))
    if len(f) == 1:
        return []
    if f[-1] != 1:
        f = pscalar(F, F.inv(f[-1]), f)
    out = []

    def rec(g, dmin):
        dg = len(g)-1
        if dg == 0:
            return
        if is_irreducible(F, g):
            out.append(g)
            return
        # find a factor by trial over monic polys of degree dmin..dg//2 is too slow;
        # use distinct-degree + Cantor-Zassenhaus
        # distinct degree step
        x = [0, 1]
        h = x
        for d in range(1, dg//2 + 1):
            h = ppowmod(F, h, F.q, g)      # x^{q^d} mod g
            gg = pgcd(F, psub(F, h, x), g)
            if len(gg)-1 > 0 and len(gg)-1 < dg:
                rec(gg, d)
                rec(pdivmod(F, g, gg)[0], d)
                return
        # g must be a power of an irreducible
        # find it by splitting
        d = 1
        while True:
            cand = split_equal_degree(F, g, d)
            if cand is not None:
                rec(cand, d)
                rec(pdivmod(F, g, cand)[0], d)
                return
            d += 1
            if d > dg:
                out.append(g)
                return

    rec(f, 1)
    return out


def split_equal_degree(F, g, d):
    """find a proper factor of g all of whose irreducible factors have degree d"""
    import random
    dg = len(g)-1
    if dg <= d:
        return None
    n = dg//d
    if n <= 1:
        return None
    q = F.q
    # Cantor-Zassenhaus
    rnd = random.Random(12345)
    for _ in range(200):
        a = [rnd.randrange(q) for _ in range(dg)]
        a = ptrim(a)
        if len(a) <= 1:
            continue
        if q % 2 == 1:
            e = (q**d - 1)//2
            b = ppowmod(F, a, e, g)
            c = pgcd(F, psub(F, b, [1]), g)
        else:
            # trace map
            b = a
            acc = a
            for _ in range(d-1):
                b = ppowmod(F, b, 2, g)
                acc = padd(F, acc, b)
            c = pgcd(F, acc, g)
        if 0 < len(c)-1 < dg:
            return c
    return None


def factor(F, f):
    """returns list of (monic irreducible factor, multiplicity)"""
    f = ptrim(list(f))
    if len(f) == 1:
        return []
    if f[-1] != 1:
        f = pscalar(F, F.inv(f[-1]), f)
    # square-free decomposition in char p
    out = []
    g = f
    # repeated division by gcd(g, g')
    while True:
        d = pderiv(F, g)
        if not any(d):
            break
        c = pgcd(F, g, d)
        if len(c) == 1:
            break
        g = c
    # standard squarefree decomposition
    result = []
    # multiplicity handling
    mult = 1
    remaining = ptrim(list(f))
    # handle p-th powers: f = prod a_i(x)^{p^i} with squarefree a_i
    cur = remaining
    m = 1
    while len(cur)-1 > 0:
        d = pderiv(F, cur)
        if not any(d):
            # cur is a p-th power
            root = pth_root(F, cur)
            sub = factor(F, root)
            for (h, e) in sub:
                result.append((h, e*F.p))
            return result
        c = pgcd(F, cur, d)
        w = pdivmod(F, cur, c)[0]
        i = 1
        while len(w)-1 > 0:
            y = pgcd(F, w, c)
            z = pdivmod(F, w, y)[0]
            if len(z)-1 > 0:
                for h in factor_squarefree_distinct(F, z):
                    result.append((h, i))
            w = y
            c = pdivmod(F, c, y)[0]
            i += 1
        cur = c
        m *= F.p
        if len(cur)-1 == 0:
            break
    # merge
    merged = {}
    for h, e in result:
        key = tuple(h)
        merged[key] = merged.get(key, 0) + e
    return [(list(k), v) for k, v in merged.items()]


def pth_root(F, f):
    """f is a p-th power; return its p-th root"""
    # f(x) = sum a_i x^i with i divisible by p, a_i = b_{i/p}^p
    out = [0]*(len(f)//F.p + 1)
    for i, a in enumerate(f):
        if a == 0:
            continue
        assert i % F.p == 0, "not a p-th power"
        j = i//F.p
        # b = a^{p^{m-1}}
        b = F.pow(a, F.p**(F.m-1))
        out[j] = b
    return ptrim(out)


# ----------------------------------------------------------------- codes
def span_rank(F, rows, n):
    """row-reduce a list of length-n vectors over GF; return (rank, rref rows)"""
    rows = [list(r) for r in rows]
    piv = []
    r = 0
    for c in range(n):
        p = None
        for i in range(r, len(rows)):
            if rows[i][c]:
                p = i
                break
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        inv = F.inv(rows[r][c])
        rows[r] = [F.mul(inv, v) for v in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c]:
                f = rows[i][c]
                rows[i] = [F.sub(rows[i][k], F.mul(f, rows[r][k])) for k in range(n)]
        piv.append(c)
        r += 1
        if r == len(rows):
            break
    return r, rows[:r]


def frobenius_pow(F, v, k):
    """apply x -> x^{p^k} entrywise"""
    return [F.pow(a, F.p**k) for a in v]


def hull_dim(F, basis, n, k):
    """dim of C cap C^{perp_k}, where basis spans C (length n over GF)."""
    rC, rrefC = span_rank(F, basis, n)
    # C^{perp_k} = {v : sum v_i * c_i^{p^k} = 0 for all c in C}
    # = Euclidean dual of C^{(p^k)}
    rowsT = []
    for c in rrefC:
        rowsT.append(frobenius_pow(F, c, k))
    # nullspace of rowsT (rC x n)
    null = nullspace(F, rowsT, n)
    rCk = len(null)
    stacked = [list(c) for c in rrefC] + null
    rS, _ = span_rank(F, stacked, n)
    return rC + rCk - rS


def nullspace(F, rows, n):
    """basis of {v in GF^n : rows . v = 0}"""
    if not rows:
        return [[1 if j == i else 0 for j in range(n)] for i in range(n)]
    m = len(rows)
    A = [list(r) for r in rows]
    piv = []
    r = 0
    for c in range(n):
        p = None
        for i in range(r, m):
            if A[i][c]:
                p = i
                break
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        inv = F.inv(A[r][c])
        A[r] = [F.mul(inv, v) for v in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                f = A[i][c]
                A[i] = [F.sub(A[i][k], F.mul(f, A[r][k])) for k in range(n)]
        piv.append(c)
        r += 1
        if r == m:
            break
    free = [c for c in range(n) if c not in piv]
    basis = []
    for fc in free:
        v = [0]*n
        v[fc] = 1
        for i, pc in enumerate(piv):
            v[pc] = F.neg(A[i][fc])
        basis.append(v)
    return basis


def min_distance_from_parity(F, H, n, maxw=None):
    """Exact minimum distance of the code {v : H v^T = 0} by checking
    column dependence for w = 1,2,...; returns (d, witness) or (None,...)
    WARNING: exponential; use only for tiny n and small d."""
    from itertools import combinations
    m = len(H)
    if maxw is None:
        maxw = n
    for w in range(1, maxw+1):
        for S in combinations(range(n), w):
            cols = [[H[i][j] for i in range(m)] for j in S]
            r, _ = span_rank(F, [list(c) for c in cols], m)
            if r < w:
                return w, S
    return None, None
