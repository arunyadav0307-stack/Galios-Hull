"""
fflib.py -- minimal finite-field / polynomial library used to *verify* the
mathematical claims of the proposed blueprint.  Pure Python, no dependencies.

Conventions
-----------
* F_q with q = p^e is represented as F_p[x]/(m(x)) with m monic irreducible of
  degree e; a field element is a tuple of ints (coeffs in F_p, length <= e).
* Polynomials over F_q are lists of field elements, index = degree, monic
  normalization on demand.

Everything here is deliberately explicit so that each verification step can be
read off against paper-and-pencil computations.
"""
from itertools import product


class GF:
    """Finite field F_{p^e} = F_p[x]/(mod)."""

    def __init__(self, p, e, mod):
        self.p, self.e, self.q = p, e, p ** e
        self.mod = list(mod)  # monic, length e+1
        assert len(self.mod) == e + 1 and self.mod[-1] == 1
        self.zero = tuple([0] * e)
        self.one = tuple([1] + [0] * (e - 1))
        self._els = None

    # ---- basic arithmetic -------------------------------------------------
    def red(self, a):
        a = [x % self.p for x in a]
        while len(a) > 1 and a[-1] == 0:
            a.pop()
        return tuple(a + [0] * (self.e - len(a)))

    def add(self, a, b):
        return self.red([(x + y) for x, y in zip(a, b)])

    def neg(self, a):
        return self.red([(-x) for x in a])

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def _polymul(self, a, b):
        res = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    res[i + j] = (res[i + j] + x * y) % self.p
        return res

    def mul(self, a, b):
        prod = self._polymul(list(a), list(b))
        # reduce modulo self.mod
        for i in range(len(prod) - 1, self.e - 1, -1):
            c = prod[i]
            if c:
                for j in range(self.e + 1):
                    prod[i - self.e + j] = (prod[i - self.e + j] - c * self.mod[j]) % self.p
        return self.red(prod)

    def pow(self, a, n):
        n = int(n)
        if n < 0:
            a, n = self.inv(a), -n
        r = self.one
        while n:
            if n & 1:
                r = self.mul(r, a)
            a = self.mul(a, a)
            n >>= 1
        return r

    def _egcd(self, a, b):
        # extended Euclid in F_p[x]; returns (g, s, t) with s*a + t*b = g
        a, b = self._strip(list(a)), self._strip(list(b))
        old_r, r = a, b
        old_s, s = [1], [0]
        old_t, t = [0], [1]
        while any(r):
            q, rem = self._polydivmod(self._strip(old_r), self._strip(r))
            old_r, r = r, self._strip(rem)
            old_s, s = s, self._polysub(old_s, self._polymul(q, s))
            old_t, t = t, self._polysub(old_t, self._polymul(q, t))
        inv_lc = pow(old_r[-1], self.p - 2, self.p)
        strip = GF._strip
        return strip([c * inv_lc % self.p for c in old_r]), \
               strip([c * inv_lc % self.p for c in old_s]), \
               strip([c * inv_lc % self.p for c in old_t])

    @staticmethod
    def _strip(a):
        a = list(a)
        while len(a) > 1 and a[-1] == 0:
            a.pop()
        return a

    @staticmethod
    def _polysub(a, b):
        n = max(len(a), len(b))
        return [(a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0) for i in range(n)]

    def _polydivmod(self, a, b):
        a = self._strip(list(a))
        b = self._strip(list(b))
        if not any(b):
            raise ZeroDivisionError
        inv = pow(b[-1], self.p - 2, self.p)
        q = [0] * max(1, len(a) - len(b) + 1)
        r = a[:]
        while len(r) >= len(b) and any(r):
            d = len(r) - len(b)
            c = r[-1] * inv % self.p
            q[d] = (q[d] + c) % self.p
            for i in range(len(b)):
                r[d + i] = (r[d + i] - c * b[i]) % self.p
            while len(r) > 1 and r[-1] == 0:
                r.pop()
        while len(q) > 1 and q[-1] == 0:
            q.pop()
        return q, r

    def inv(self, a):
        if not any(a):
            raise ZeroDivisionError
        g, s, _ = self._egcd(list(a), self.mod)
        assert g == [1], g
        return self.red(s)

    def elements(self):
        if self._els is None:
            self._els = [tuple(c) for c in product(range(self.p), repeat=self.e)]
        return self._els

    def nonzero(self):
        return [a for a in self.elements() if any(a)]

    def frob(self, a, k=1):
        return self.pow(a, self.p ** (k % self.e) if self.e else 1)

    def order(self, a):
        """multiplicative order of a in F_q^*"""
        a = self.red(a)
        assert any(a), "zero has no multiplicative order"
        o = 1
        cur = a
        while cur != self.one:
            cur = self.mul(cur, a)
            o += 1
            assert o <= self.q, "order exceeded q-1"
        return o

    def primitive(self):
        for a in self.nonzero():
            if self.order(a) == self.q - 1:
                return a
        raise RuntimeError

    def __repr__(self):
        return f"GF({self.q})"


# ---------------------------------------------------------------------------
# polynomials over GF
# ---------------------------------------------------------------------------
def ptrim(f):
    """strip trailing zero coefficients; coefficients are GF elements (tuples)."""
    f = list(f)
    while len(f) > 1 and not any(f[-1]):
        f.pop()
    return f


class Poly:
    def __init__(self, F, coeffs):
        self.F = F
        self.c = ptrim(coeffs)

    def __len__(self):
        return len(self.c)

    def deg(self):
        return len(self.c) - 1

    def __repr__(self):
        return "+".join(f"{c}x^{i}" if i else str(c) for i, c in enumerate(self.c))

    def __eq__(self, other):
        return self.c == other.c

    def add(self, o):
        return Poly(self.F, self.F.add_poly(self.c, o.c) if hasattr(self.F, 'add_poly')
                    else [self.F.add(a, b) for a, b in zip(self.c + [self.F.zero] * len(o.c),
                                                           o.c + [self.F.zero] * len(self.c))])

    def mul(self, o):
        res = [self.F.zero] * (len(self.c) + len(o.c) - 1)
        for i, a in enumerate(self.c):
            for j, b in enumerate(o.c):
                res[i + j] = self.F.add(res[i + j], self.F.mul(a, b))
        return Poly(self.F, res)

    def scale(self, a):
        return Poly(self.F, [self.F.mul(a, b) for b in self.c])

    def sub(self, o):
        return self.add(o.scale(self.F.neg(self.F.one)))

    def divmod_(self, o):
        F = self.F
        a, b = list(self.c), ptrim(list(o.c))
        assert b and any(b)
        inv = F.inv(b[-1])
        q = [F.zero] * max(1, len(a) - len(b) + 1)
        r = a[:]
        while len(r) >= len(b) and any(map(any, r)):
            d = len(r) - len(b)
            c = F.mul(r[-1], inv)
            q[d] = F.add(q[d], c)
            for i in range(len(b)):
                r[d + i] = F.sub(r[d + i], F.mul(c, b[i]))
            r = ptrim(r)
        return Poly(F, q), Poly(F, r)

    def is_zero(self):
        return not any(map(any, self.c))

    def monic(self):
        if self.is_zero():
            return self
        return self.scale(self.F.inv(self.c[-1]))

    def eval(self, a):
        acc = self.F.zero
        for c in reversed(self.c):
            acc = self.F.add(self.F.mul(acc, a), c)
        return acc

    def mod(self, o):
        return self.divmod_(o)[1]


def xpoly(F):
    return Poly(F, [F.zero, F.one])


def const(F, a):
    return Poly(F, [a])


def xpow_mod(F, a, f):
    """x^a mod f, as an element of F_q[x]/(f)."""
    res = const(F, F.one)
    base = xpoly(F).mod(f)
    while a:
        if a & 1:
            res = res.mul(base).mod(f)
        base = base.mul(base).mod(f)
        a >>= 1
    return res


def ord_of_poly(F, f):
    """order of the polynomial f, i.e. least a>=1 with x^a = 1 mod f."""
    if f.deg() == 0:
        return 1
    one = const(F, F.one)
    cur = xpoly(F).mod(f)
    a = 1
    limit = 10 ** 7
    while cur != one:
        cur = cur.mul(xpoly(F).mod(f)).mod(f)
        a += 1
        assert a < limit, "order computation exceeded limit"
    return a


def monic_divisors(F, g, max_deg=None):
    """all monic divisors of g by brute force (small fields only)."""
    n = g.deg() if max_deg is None else max_deg
    out = []
    for d in range(0, n + 1):
        for coeffs in product(F.elements(), repeat=d):
            cand = list(coeffs) + [F.one]
            h = Poly(F, cand)
            if h.deg() != d:
                continue
            if g.mod(h).is_zero():
                out.append(h)
    return out


# ---------------------------------------------------------------------------
# linear algebra over GF (for brute-force duals of codes over the ring alphabet
# and for code membership tests)
# ---------------------------------------------------------------------------
def vec_add(F, u, v):
    return [F.add(a, b) for a, b in zip(u, v)]


def vec_scale(F, a, u):
    return [F.mul(a, b) for b in u]


def poly_to_vec(F, p, n):
    v = [F.zero] * n
    for i, c in enumerate(p.c[:n]):
        v[i] = c
    return v


def mat_rank(F, rows):
    rows = [r[:] for r in rows]
    m = len(rows)
    if m == 0:
        return 0
    n = len(rows[0])
    r = 0
    for c in range(n):
        piv = None
        for i in range(r, m):
            if any(rows[i][c]):
                piv = i
                break
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        inv = F.inv(rows[r][c])
        rows[r] = vec_scale(F, inv, rows[r])
        for i in range(m):
            if i != r and any(rows[i][c]):
                f = rows[i][c]
                rows[i] = vec_add(F, rows[i], vec_scale(F, F.neg(f), rows[r]))
        r += 1
        if r == m:
            break
    return r


def nullspace(F, rows, n):
    """basis of {v : sum_i rows[j][i] v_i = 0} (over F_q)."""
    A = [r[:] for r in rows]
    m = len(A)
    piv_cols = []
    r = 0
    for c in range(n):
        piv = None
        for i in range(r, m):
            if any(A[i][c]):
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = F.inv(A[r][c])
        A[r] = vec_scale(F, inv, A[r])
        for i in range(m):
            if i != r and any(A[i][c]):
                A[i] = vec_add(F, A[i], vec_scale(F, F.neg(A[i][c]), A[r]))
        piv_cols.append(c)
        r += 1
        if r == m:
            break
    free = [c for c in range(n) if c not in piv_cols]
    basis = []
    for fc in free:
        v = [F.zero] * n
        v[fc] = F.one
        for i, pc in enumerate(piv_cols):
            v[pc] = F.neg(A[i][fc])
        basis.append(v)
    return basis


def code_from_generator(F, gvecs):
    """span of the given vectors (list of basis vectors)."""
    return gvecs


def in_span(F, basis, v):
    R = mat_rank(F, basis + [v])
    return R == mat_rank(F, basis)


def sigma_dual(F, basis, n, k=1):
    """sigma-Galois dual: {v : sum_i v_i sigma(u_i) = 0 for all u in basis}."""
    rows = []
    for u in basis:
        rows.append([F.pow(u[i], F.p ** k) for i in range(n)])
    return nullspace(F, rows, n)
