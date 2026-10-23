"""
R3 feasibility probe -- NOT Phase 3, NOT a deliverable of any later phase.

Question tested: over R_e = F_{q^2}[u]/(u^e - 1), is

        C^{perp_H} <= C

a PRODUCT condition over the e CRT components, so that

    #{dual-containing lambda-constacyclic codes of length n over R_e}
  = PRODUCT_{l=1..e} #{dual-containing alpha_l-constacyclic codes of length n over F_{q^2}} ?

If it is, R3 ("count dual-containing lambda-constacyclic codes over R_e") is a routine
product of field-level counts and carries no independent content.

Ring side is CRT-FREE: ideals are enumerated as principal ideals <g> with g a monic
divisor of x^n - lambda, found by brute-force divisibility testing over ALL monic g of
degree <= n in R_e[x]. The Hermitian dual uses the paper's own definition,
<x,y>_H = sum_i x_i conj(y_i) in R_e (p.4 of the source).

Cases:
  T2 (primary, smallest ring): q=3, e=2, n=2  -> |R_2| = 81, e | q+1
  T1 (confirmatory):           q=2, e=3, n=3  -> |R_3| = 64, 512 ideals expected

ASCII only, stdlib only, deterministic.
"""

import itertools


# --------------------------------------------------------------------------- field
class GF:
    """GF(p^deg) as integers 0..Q-1 with base-p digits, modulo a monic irreducible."""

    def __init__(self, p, deg, mod):
        self.p, self.deg, self.mod = p, deg, mod
        self.Q = p ** deg
        self.digit = [[(x // p ** i) % p for i in range(deg)] for x in range(self.Q)]
        self.enc = {tuple(d): x for x, d in enumerate(self.digit)}

        self.add = [[self.enc[tuple((self.digit[a][i] + self.digit[b][i]) % p
                                    for i in range(deg))]
                     for b in range(self.Q)] for a in range(self.Q)]

        self.mul = [[0] * self.Q for _ in range(self.Q)]
        for a in range(self.Q):
            da = self.digit[a]
            for b in range(self.Q):
                db = self.digit[b]
                prod = [0] * (2 * deg - 1)
                for i in range(deg):
                    if da[i]:
                        for j in range(deg):
                            prod[i + j] = (prod[i + j] + da[i] * db[j]) % p
                for k in range(len(prod) - 1, deg - 1, -1):
                    c = prod[k]
                    if c:
                        prod[k] = 0
                        for j in range(deg + 1):
                            prod[k - deg + j] = (prod[k - deg + j] - c * mod[j]) % p
                self.mul[a][b] = self.enc[tuple(prod[i] % p for i in range(deg))]

        self.neg = [self.enc[tuple((-d) % p for d in self.digit[a])] for a in range(self.Q)]
        self.zero = 0
        self.one = self.enc[tuple([1] + [0] * (deg - 1))]

    def pow(self, a, k):
        r, base = self.one, a
        while k:
            if k & 1:
                r = self.mul[r][base]
            base = self.mul[base][base]
            k >>= 1
        return r


def find_irreducible(p, deg):
    for tail in itertools.product(range(p), repeat=deg):
        mod = list(tail) + [1]
        F = GF(p, deg, mod)
        ok = all(len({F.mul[a][b] for b in range(F.Q)}) == F.Q for a in range(1, F.Q))
        if ok:
            return F
    raise RuntimeError("no irreducible polynomial found")


# --------------------------------------------------------------------------- ring
class Ring:
    """R_e = F[u]/(u^e - 1)."""

    def __init__(self, F, e):
        self.F, self.e = F, e
        self.size = F.Q ** e
        self.digits = [[(x // F.Q ** i) % F.Q for i in range(e)] for x in range(self.size)]
        self.enc = {tuple(d): x for x, d in enumerate(self.digits)}

        self.add = [[self.enc[tuple(F.add[self.digits[a][i]][self.digits[b][i]]
                                    for i in range(e))]
                     for b in range(self.size)] for a in range(self.size)]

        self.mul = [[0] * self.size for _ in range(self.size)]
        for a in range(self.size):
            da = self.digits[a]
            for b in range(self.size):
                db = self.digits[b]
                out = []
                for k in range(e):
                    acc = 0
                    for i in range(e):
                        acc = F.add[acc][F.mul[da[i]][db[(k - i) % e]]]
                    out.append(acc)
                self.mul[a][b] = self.enc[tuple(out)]

        self.neg = [self.enc[tuple(F.neg[c] for c in self.digits[a])] for a in range(self.size)]
        self.one = self.enc[tuple([F.one] + [F.zero] * (e - 1))]

    def set_frobenius(self, q, reciprocal=True):
        """The involution y -> y^q of the ring.

        The paper's Hermitian form is <x,y>_H = sum_i x_i y_i^q with the RING q-th power.
        Since (sum c_i u^i)^q = sum c_i^q u^{qi} and u^e = 1, the exponent qi is reduced mod e.
        Under the paper's hypothesis e | q+1 one has q = -1 (mod e), so u^{qi} = u^{-i} and the
        involution is conjugate-RECIPROCAL, not coefficientwise.  (For e = 2 the two coincide,
        because u^{-1} = u.)  Using coefficientwise conjugation for e >= 3 is a different,
        non-Hermitian form and gives wrong duals.
        """
        F = self.F
        conjF = [F.pow(a, q) for a in range(F.Q)]
        out = []
        for x in range(self.size):
            d = self.digits[x]
            if reciprocal:
                coords = [F.zero] * self.e
                for i in range(self.e):
                    coords[(-i) % self.e] = conjF[d[i]]
            else:
                coords = [conjF[c] for c in d]
            out.append(self.enc[tuple(coords)])
        self.conj = out
        self.roots = [b for b in range(1, F.Q) if F.pow(b, self.e) == F.one]
        assert len(self.roots) == self.e, (len(self.roots), self.e)

    def eval_at(self, a, beta):
        F = self.F
        acc = F.zero
        for c in range(self.e):
            acc = F.add[acc][F.mul[self.digits[a][c]][F.pow(beta, c)]]
        return acc

    def is_unit(self, a):
        # a is a unit in R_e iff gcd(a(u), u^e - 1) = 1, i.e. a(beta) != 0 for every
        # e-th root of unity beta. This is NOT the same as "all coefficients nonzero".
        return all(self.eval_at(a, b) != 0 for b in self.roots)

    def elt(self, coords):
        return self.enc[tuple(coords)]


# --------------------------------------------------------------------------- polynomials
class Poly:
    def __init__(self, R):
        self.R = R

    def mul(self, a, b):
        R = self.R
        if not a or not b:
            return []
        out = [0] * (len(a) + len(b) - 1)
        for i, ai in enumerate(a):
            if ai == 0:
                continue
            row = R.mul[ai]
            for j, bj in enumerate(b):
                if bj:
                    out[i + j] = R.add[out[i + j]][row[bj]]
        return out

    def trim(self, f):
        while len(f) > 1 and f[-1] == 0:
            f.pop()
        return f

    def rem_monic(self, f, g):
        """remainder of f modulo monic g."""
        R = self.R
        f = list(f)
        dg = len(g) - 1
        if len(f) - 1 < dg:
            return self.trim(f)
        for k in range(len(f) - 1, dg - 1, -1):
            c = f[k]
            if c == 0:
                continue
            for j in range(dg + 1):
                f[k - dg + j] = R.add[f[k - dg + j]][R.neg[R.mul[c][g[j]]]]
        return self.trim(f)

    def is_zero(self, p):
        return all(c == 0 for c in p)


# --------------------------------------------------------------------------- linear algebra over F
def rref(F, rows, ncols):
    rows = [list(r) for r in rows if any(r)]
    piv = []
    r = 0
    for c in range(ncols):
        p = None
        for i in range(r, len(rows)):
            if rows[i][c]:
                p = i
                break
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        lead = rows[r][c]
        inv = next(x for x in range(1, F.Q) if F.mul[lead][x] == F.one)
        rows[r] = [F.mul[inv][v] for v in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c]:
                f = rows[i][c]
                rows[i] = [F.add[rows[i][j]][F.neg[F.mul[f][rows[r][j]]]] for j in range(ncols)]
        piv.append(c)
        r += 1
        if r == len(rows):
            break
    return rows[:r], piv


def nullspace(F, rows, ncols):
    red, piv = rref(F, rows, ncols)
    basis = []
    for fc in [c for c in range(ncols) if c not in piv]:
        v = [0] * ncols
        v[fc] = F.one
        for i, pc in enumerate(piv):
            v[pc] = F.neg[red[i][fc]]
        basis.append(v)
    return basis


def in_span(F, basis, v, ncols):
    if not any(v):
        return True
    return len(rref(F, basis + [v], ncols)[0]) == len(basis)


# --------------------------------------------------------------------------- codes over F_{q^2}
def field_dual_basis(F, basis, n):
    conj = F.conj_f
    rows = [[conj[y[i]] for i in range(n)] for y in basis]
    return nullspace(F, rows, n)


def field_is_dc(F, basis, n):
    dual = field_dual_basis(F, basis, n)
    return all(in_span(F, basis, v, n) for v in dual)


def field_codes(F, n, alpha):
    """all alpha-constacyclic codes of length n over F, as RREF bases."""
    P = Poly(F)
    f = [F.neg[alpha]] + [0] * (n - 1) + [F.one]
    divisors = [[F.one], f]
    for d in range(1, n):
        for tail in itertools.product(range(F.Q), repeat=d):
            g = list(tail) + [F.one]
            if P.is_zero(P.rem_monic(f, g)):
                divisors.append(g)
    seen = {}
    for g in divisors:
        vecs = []
        for j in range(n):
            r = P.rem_monic(P.mul([0] * j + [F.one], g), f)
            r = r + [0] * (n - len(r))
            vecs.append(r[:n])
        b, _ = rref(F, vecs, n)
        seen[tuple(tuple(v) for v in b)] = b
    return list(seen.values())


# --------------------------------------------------------------------------- codes over R_e
def ring_codes(R, F, n, lam, e):
    """ALL ideals of R[x]/(x^n - lam), CRT-free.

    R[x]/(x^n - lam) is a principal ideal ring (R = F^e, so R[x] = product of PIDs,
    and a quotient of a PIR is a PIR). Hence every ideal is <g> for some g, and it is
    enough to run over every g in R^n -- NOT only over monic divisors of x^n - lam,
    which would miss ideals such as <e_1 (x-1)> whose leading coefficient is a
    zero divisor.
    """
    P = Poly(R)
    f = [R.neg[lam]] + [0] * (n - 1) + [R.one]
    ncols = n * e
    seen = {}
    total = R.size ** n
    for idx in range(total):
        g = [(idx // R.size ** j) % R.size for j in range(n)]
        while len(g) > 1 and g[-1] == 0:
            g.pop()
        vecs = []
        for a in range(e):
            ua = R.elt([F.one if i == a else F.zero for i in range(e)])
            for j in range(n):
                red = P.rem_monic(P.mul([0] * j + [ua], g), f)
                red = (red + [0] * n)[:n]
                vec = []
                for c in red:
                    vec.extend(R.digits[c])
                vecs.append(vec)
        b, _ = rref(F, vecs, ncols)
        seen[tuple(tuple(v) for v in b)] = b
    return list(seen.values())


def ring_dual_basis(R, F, basis, n, e):
    ncols = n * e
    rows = []
    for y in basis:
        ycoords = [R.elt([y[i * e + t] for t in range(e)]) for i in range(n)]
        for a in range(e):
            row = [0] * ncols
            for i in range(n):
                cy = R.conj[ycoords[i]]
                for t in range(e):
                    xi = R.elt([F.one if s == t else F.zero for s in range(e)])
                    row[i * e + t] = R.digits[R.mul[xi][cy]][a]
            rows.append(row)
    return nullspace(F, rows, ncols)


def ring_is_dc(R, F, basis, n, e):
    dual = ring_dual_basis(R, F, basis, n, e)
    return all(in_span(F, basis, v, n * e) for v in dual)


def components_of(R, F, basis, n, e, beta):
    """image of the code under u -> beta: F-linear code in F^n."""
    vecs = []
    for v in basis:
        w = []
        for i in range(n):
            coords = v[i * e:(i + 1) * e]
            acc = F.zero
            for c in range(e):
                if coords[c]:
                    acc = F.add[acc][F.mul[coords[c]][F.pow(beta, c)]]
            w.append(acc)
        vecs.append(w)
    b, _ = rref(F, vecs, n)
    return b


# --------------------------------------------------------------------------- driver
def run_case(p, q, e, n, label, struct_check=True):
    m, t = 0, q
    while t % p == 0:
        t //= p
        m += 1
    assert p ** m == q
    F = find_irreducible(p, 2 * m)
    F.conj_f = [F.pow(a, q) for a in range(F.Q)]
    R = Ring(F, e)
    R.set_frobenius(q)

    print("=" * 80)
    print(f"{label}")
    print(f"  p={p}, q={q}, F = F_{F.Q}, e={e}, n={n}, e | q+1 = {q+1} -> {(q+1) % e == 0},"
          f" gcd(n,p) = {1 if n % p else p}")
    print(f"  R_e = F_{F.Q}[u]/(u^{e}-1), |R_e| = {R.size}, units = {sum(1 for a in range(R.size) if R.is_unit(a))}")
    print(f"  Hermitian form: <x,y> = sum_i x_i * y_i^{q} in R_e; y^{q} = conjugate-reciprocal (u -> u^-1), since e | q+1")

    field_total, field_dc, field_codes_by_alpha = {}, {}, {}
    for alpha in range(1, F.Q):
        codes = field_codes(F, n, alpha)
        field_codes_by_alpha[alpha] = codes
        field_total[alpha] = len(codes)
        field_dc[alpha] = sum(1 for b in codes if field_is_dc(F, b, n))
    print(f"  per-component counts over F_{F.Q} (n={n}):")
    for alpha in sorted(field_total):
        print(f"      alpha={alpha:2d}: total ideals {field_total[alpha]:3d}, dual-containing {field_dc[alpha]:3d}")

    roots = [b for b in range(1, F.Q) if F.pow(b, e) == F.one]
    assert len(roots) == e, (len(roots), e, "e-th roots of unity in F")

    units = [a for a in range(R.size) if R.is_unit(a)]
    ok_dc = ok_tot = ok_struct = 0
    bad = []
    for lam in units:
        alphas = []
        for beta in roots:
            acc = F.zero
            for c in range(e):
                acc = F.add[acc][F.mul[R.digits[lam][c]][F.pow(beta, c)]]
            alphas.append(acc)
        assert all(a != 0 for a in alphas)

        codes = ring_codes(R, F, n, lam, e)
        dc_flags = [ring_is_dc(R, F, b, n, e) for b in codes]
        pred_tot = 1
        pred_dc = 1
        for a in alphas:
            pred_tot *= field_total[a]
            pred_dc *= field_dc[a]
        if len(codes) == pred_tot:
            ok_tot += 1
        if sum(dc_flags) == pred_dc:
            ok_dc += 1
        else:
            bad.append((lam, alphas, sum(dc_flags), pred_dc))

        if struct_check:
            good = True
            for b, is_dc in zip(codes, dc_flags):
                comps = [components_of(R, F, b, n, e, beta) for beta in roots]
                d = len(b)
                if d != sum(len(c) for c in comps):
                    good = False
                    break
                if is_dc != all(field_is_dc(F, c, n) for c in comps):
                    good = False
                    break
            if good:
                ok_struct += 1

    print(f"  lambda in R_e^* tested: {len(units)}")
    print(f"    #ideals(R_e) == PROD #ideals(F)          : {ok_tot}/{len(units)}")
    print(f"    #dual-containing(R_e) == PROD #DC(F)     : {ok_dc}/{len(units)}")
    if struct_check:
        print(f"    dim C == sum_l dim C_l and DC(C) <=> ALL DC(C_l) for every ideal : {ok_struct}/{len(units)}")
    if bad:
        print("    MISMATCHES:", bad[:3])
    return ok_tot, ok_dc, ok_struct, len(units)


if __name__ == "__main__":
    r2 = run_case(3, 3, 2, 2, "T2  primary: q=3, e=2, n=2  (smallest ring)")
    r1 = run_case(2, 2, 3, 2, "T1  confirmatory: q=2, e=3, n=2  (three components)")
    print("=" * 80)
    print(f"T2: totals {r2[0]}/{r2[3]}, dual-containing {r2[1]}/{r2[3]}, structural {r2[2]}/{r2[3]}")
    print(f"T1: totals {r1[0]}/{r1[3]}, dual-containing {r1[1]}/{r1[3]}, structural {r1[2]}/{r1[3]}")
