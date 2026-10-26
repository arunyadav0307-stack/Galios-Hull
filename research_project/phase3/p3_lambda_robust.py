"""
P3-12: does the P3-11 finding survive removing its two restrictions?

P3-11 computed the exact joint law of (dim Hull_H(psi(C)), d(psi(C))) for the nested e = 2 family
over F_9 and found it is NOT the product of its marginals (TV = 0.2078 at n = 5, 0.1753 at n = 8).
Two restrictions were left in place:

    (i)  lambda = (1, 1): both components CYCLIC, i.e. ideals of F_9[x]/(x^n - 1);
    (ii) C_2 <= C_1 (nested): needed only so that the classical distance formula of P3-10 applies.

Restriction (ii) is dropped here by enumerating psi(C_1 x C_2) directly: for e = 2 the Gray map is
psi(c_1,c_2) = (c_1 + c_2, c_1 - c_2), so

    d(psi) = min over (c_1,c_2) != (0,0) of  w(c_1 + c_2) + w(c_1 - c_2),

which needs no nesting, no formula and no bound.  Restriction (i) is dropped by running all four
lambda of R_2 = F_9 x F_9: each component is lambda_l-constacyclic with lambda_l in {+1,-1}, i.e.
CYCLIC (ideals of F_9[x]/(x^n - 1)) or NEGACYCLIC (ideals of F_9[x]/(x^n + 1)).

Feasibility, stated rather than hidden:
  * n = 2, 3: every pair, all four lambda.  Cost per lambda is (sum over codes of |C|)^2 word-pairs,
    which is 100^2 and 820^2 respectively -- trivial.
  * n = 4: every pair would cost 10000^2 = 10^8 word-pairs per lambda, which is out of reach in
    pure Python.  So for n = 4 we keep the nesting hypothesis (distance from P3-10's proved formula,
    which is cheap) and use n = 4 only to extend P3-11 from cyclic to NEGACYCLIC components.
  * For mixed lambda (one component cyclic, one negacyclic) there is no nontrivial nesting:
    gcd(x^n - 1, x^n + 1) divides 2, so C_2 <= C_1 forces g_1 = 1 or C_2 = 0.  Hence n = 4 mixed
    lambda carries no information and is skipped, not silently omitted.

Pure stdlib, ASCII only.
"""
import itertools
import sys
from fractions import Fraction

P = 3
Q = 9


# ---------------------------------------------------------------- F_9 = F_3[t]/(t^2+1), a+bt <-> a+3b
def fadd(x, y):
    return (x % 3 + y % 3) % 3 + 3 * ((x // 3 + y // 3) % 3)


def fsub(x, y):
    return (x % 3 - y % 3) % 3 + 3 * ((x // 3 - y // 3) % 3)


def fneg(x):
    return (-x % 3) + 3 * (-(x // 3) % 3)


def fmul(x, y):
    a, b = x % 3, x // 3
    c, d = y % 3, y // 3
    return (a * c + 2 * b * d) % 3 + 3 * ((a * d + b * c) % 3)


def finv(x):
    for y in range(1, 9):
        if fmul(x, y) == 1:
            return y
    raise ZeroDivisionError(x)


def conj(x):
    return (x % 3) + 3 * ((-(x // 3)) % 3)


# ---------------------------------------------------------------- polynomials over F_9
def ptrim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def pmul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    r[i + j] = fadd(r[i + j], fmul(x, y))
    return ptrim(r)


def psub(a, b):
    n = max(len(a), len(b))
    r = [(a[i] if i < len(a) else 0) for i in range(n)]
    for i in range(n):
        if i < len(b) and b[i]:
            r[i] = fsub(r[i], b[i])
    return ptrim(r)


def pdivmod(a, b):
    a = ptrim(list(a))
    b = ptrim(list(b))
    inv = finv(b[-1])
    b = [fmul(inv, c) for c in b]
    q = [0] * max(1, len(a) - len(b) + 1)
    rem = ptrim(list(a))
    while len(rem) >= len(b) and not (len(rem) == 1 and rem[0] == 0):
        shift = len(rem) - len(b)
        coeff = rem[-1]
        q[shift] = coeff
        rem = psub(rem, [0] * shift + [fmul(coeff, c) for c in b])
        if len(rem) == 1 and rem[0] == 0:
            break
    return ptrim(q), ptrim(rem)


def pmod(a, m):
    return pdivmod(a, m)[1]


def is_zero(p):
    return len(p) == 1 and p[0] == 0


def modulus(n, lam):
    """x^n - lam, lam = +1 (cyclic) or -1 (negacyclic)."""
    p = [0] * (n + 1)
    p[0] = fneg(lam)
    p[n] = 1
    return ptrim(p)


def divisors_of(f, max_deg):
    out = []
    for deg in range(max_deg + 1):
        for coeffs in itertools.product(range(9), repeat=deg):
            g = list(coeffs) + [1]
            if is_zero(pmod(f, g)):
                out.append(tuple(g))
    return out


def generator_matrix(g, n, lam):
    f = modulus(n, lam)
    deg = len(g) - 1
    k = n - deg
    if k <= 0:
        return []
    rows = []
    for i in range(k):
        mono = [0] * (i + 1)
        mono[i] = 1
        r = pmod(pmul(list(g), mono), f)
        rows.append([r[j] if j < len(r) else 0 for j in range(n)])
    return rows


# ---------------------------------------------------------------- linear algebra over F_9
def rank(rows):
    m = [list(r) for r in rows]
    if not m:
        return 0
    ncols = len(m[0])
    r = 0
    for c in range(ncols):
        piv = None
        for i in range(r, len(m)):
            if m[i][c]:
                piv = i
                break
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        inv = finv(m[r][c])
        m[r] = [fmul(inv, x) for x in m[r]]
        for i in range(len(m)):
            if i != r and m[i][c]:
                fac = m[i][c]
                m[i] = [fsub(x, fmul(fac, y)) for x, y in zip(m[i], m[r])]
        r += 1
        if r == len(m):
            break
    return r


def hull_dim(G, n):
    k = len(G)
    if k == 0:
        return 0
    cG = [[conj(x) for x in r] for r in G]
    M = []
    for i in range(k):
        row = []
        for j in range(k):
            acc = 0
            for l in range(n):
                if G[i][l] and cG[j][l]:
                    acc = fadd(acc, fmul(G[i][l], cG[j][l]))
            row.append(acc)
        M.append(row)
    return k - rank(M)


def psi_generator(G1, G2):
    rows = []
    for r in G1:
        rows.append(list(r) + list(r))
    for r in G2:
        rows.append(list(r) + [fneg(x) for x in r])
    return rows


def words_of(G, n, cap=1000000):
    k = len(G)
    if k == 0:
        return [[0] * n]
    if 9 ** k > cap:
        return None
    out = []
    for coeffs in itertools.product(range(9), repeat=k):
        v = [0] * n
        for c, r in zip(coeffs, G):
            if c:
                v = [fadd(x, fmul(c, y)) for x, y in zip(v, r)]
        out.append(v)
    return out


def psi_distance(W1, W2, n, cap=2000000):
    """min over (c1,c2) != (0,0) of w(c1+c2) + w(c1-c2)."""
    if len(W1) * len(W2) > cap:
        return None
    best = None
    for a in W1:
        for b in W2:
            w = 0
            for i in range(n):
                if fadd(a[i], b[i]):
                    w += 1
                    if best is not None and w >= best:
                        break
                if fsub(a[i], b[i]):
                    w += 1
                    if best is not None and w >= best:
                        break
            if w == 0:
                continue
            if best is None or w < best:
                best = w
    return best


def independence_stats(dist):
    """Exact independence test, with a degeneracy flag.

    The test P(h,d) = P(h)P(d) is VACUOUS when one marginal is a point mass: then the product
    formula holds identically and says nothing about dependence.  Reporting such a case as
    "independent" without the flag would overstate the evidence, so both are returned.
    """
    N = sum(dist.values())
    if N == 0:
        return {"tv": 0.0, "maxdev": 0.0, "hvals": 0, "dvals": 0, "vacuous": True}
    H, D = {}, {}
    for (h, d), c in dist.items():
        H[h] = H.get(h, 0) + c
        D[d] = D.get(d, 0) + c
    tv = Fraction(0)
    maxdev = Fraction(0)
    for (h, d), c in dist.items():
        exp = Fraction(H[h] * D[d], N)
        dev = abs(Fraction(c) - exp)
        maxdev = max(maxdev, dev)
        tv += dev
    tv = tv / N / 2
    return {"tv": float(tv), "maxdev": float(maxdev),
            "hvals": len(H), "dvals": len(D), "vacuous": (len(H) < 2 or len(D) < 2)}


LAMBDAS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


def name(lam):
    return "(" + ",".join("+" if l == 1 else "-" for l in lam) + ")"


def run_all_pairs(n):
    """Every pair for every lambda, distance by direct enumeration (no nesting assumption)."""
    print("=" * 96)
    print(f"n = {n}: ALL pairs, all four lambda, d(psi) enumerated directly (no nesting)")
    out = []
    for lam in LAMBDAS:
        f1 = modulus(n, lam[0])
        f2 = modulus(n, lam[1])
        d1 = divisors_of(f1, n)
        d2 = divisors_of(f2, n)
        codes1 = {g: generator_matrix(g, n, lam[0]) for g in d1}
        codes2 = {g: generator_matrix(g, n, lam[1]) for g in d2}
        W1 = {g: words_of(G, n) for g, G in codes1.items()}
        W2 = {g: words_of(G, n) for g, G in codes2.items()}
        H1 = {g: hull_dim(G, n) for g, G in codes1.items()}
        H2 = {g: hull_dim(G, n) for g, G in codes2.items()}

        dist = {}
        pairs = 0
        skipped = 0
        hcheck_bad = 0
        for g1 in d1:
            for g2 in d2:
                dpsi = psi_distance(W1[g1], W2[g2], n)
                if dpsi is None or (len(codes1[g1]) == 0 and len(codes2[g2]) == 0):
                    skipped += 1
                    continue
                h = H1[g1] + H2[g2]
                GP = psi_generator(codes1[g1], codes2[g2])
                if hull_dim(GP, 2 * n) != h:
                    hcheck_bad += 1
                dist[(h, dpsi)] = dist.get((h, dpsi), 0) + 1
                pairs += 1
        st = independence_stats(dist)
        out.append((n, lam, pairs, skipped, hcheck_bad, st, dist))
        verdict = ("NOT independent" if st["maxdev"] != 0
                   else ("independent (VACUOUS: marginal degenerate)" if st["vacuous"]
                         else "independent"))
        print(f"  lambda={name(lam)}: {pairs:5d} pairs, {skipped} skipped, "
              f"hull cross-check failures {hcheck_bad}, TV={st['tv']:.4f}, "
              f"MAXDEV={st['maxdev']:.4f}, h-values {st['hvals']}, d-values {st['dvals']}"
              f"  -> {verdict}")
        if st["maxdev"] != 0:
            hs = sorted(set(h for h, _ in dist))
            ds = sorted(set(d for _, d in dist))
            print(f"      h values {hs}, d values {ds}")
            print("      " + "h/d".rjust(4) + " " + " ".join(str(d).rjust(6) for d in ds))
            for h in hs:
                print("      " + str(h).rjust(4) + " " + " ".join(str(dist.get((h, d), 0)).rjust(6) for d in ds))
    return out


def run_nested(n):
    """Nested pairs only, using P3-10's proved formula; for n = 4 where full enumeration is out of reach."""
    print("=" * 96)
    print(f"n = {n}: NESTED pairs only, d = min{{2 d(C_1), d(C_2)}} (P3-10, proved)")
    out = []
    for lam in [(1, 1), (-1, -1)]:
        f1 = modulus(n, lam[0])
        f2 = modulus(n, lam[1])
        d1 = divisors_of(f1, n)
        d2 = divisors_of(f2, n)
        codes1 = {g: generator_matrix(g, n, lam[0]) for g in d1}
        codes2 = {g: generator_matrix(g, n, lam[1]) for g in d2}
        W1 = {g: words_of(G, n) for g, G in codes1.items()}
        W2 = {g: words_of(G, n) for g, G in codes2.items()}
        H1 = {g: hull_dim(G, n) for g, G in codes1.items()}
        H2 = {g: hull_dim(G, n) for g, G in codes2.items()}

        def mind(W):
            b = None
            for wd in W:
                c = sum(1 for x in wd if x)
                if c and (b is None or c < b):
                    b = c
            return b

        dist = {g: mind(W1[g]) for g in d1}
        dist2 = {g: mind(W2[g]) for g in d2}

        joint = {}
        pairs = 0
        hbad = 0
        for g1 in d1:
            for g2 in d2:
                if not is_zero(pmod(list(g2), list(g1))):
                    continue
                if dist[g1] is None or dist2[g2] is None:
                    continue
                dd = min(2 * dist[g1], dist2[g2])
                h = H1[g1] + H2[g2]
                GP = psi_generator(codes1[g1], codes2[g2])
                if hull_dim(GP, 2 * n) != h:
                    hbad += 1
                joint[(h, dd)] = joint.get((h, dd), 0) + 1
                pairs += 1
        st = independence_stats(joint)
        out.append((n, lam, pairs, hbad, st, joint))
        verdict = ("NOT independent" if st["maxdev"] != 0
                   else ("independent (VACUOUS: marginal degenerate)" if st["vacuous"]
                         else "independent"))
        print(f"  lambda={name(lam)}: {pairs:5d} nested pairs, hull cross-check failures {hbad}, "
              f"TV={st['tv']:.4f}, MAXDEV={st['maxdev']:.4f}, h-values {st['hvals']}, "
              f"d-values {st['dvals']}  -> {verdict}")
    return out


def main():
    # conjugation sanity: conj is the Frobenius x -> x^3
    def fpow(x, e):
        r = 1
        for _ in range(e):
            r = fmul(r, x)
        return r
    assert all(conj(x) == fpow(x, 3) for x in range(9)), "conj != Frobenius"
    print("P3-12: robustness of the P3-11 non-product finding -- all pairs, and all four lambda")
    print("sanity: conj(x) == x^3 for all x in F_9   [ok]")
    print()

    res = []
    for n in (2, 3):
        res.extend(run_all_pairs(n))
    res.extend(run_nested(4))
    print()

    print("=" * 96)
    print("SUMMARY")
    print(f"{'n':>3} {'lambda':>8} {'pairs':>7} {'mode':>8} {'TV':>8}  verdict")
    fails = 0
    for row in res:
        n, lam, pairs = row[0], row[1], row[2]
        if len(row) == 7:
            _, _, _, skipped, hbad, st, _ = row
            mode = "all"
        else:
            _, _, _, hbad, st, _ = row
            mode = "nested"
            skipped = 0
        fails += hbad
        if st["maxdev"] != 0:
            verdict = "NOT independent"
        elif st["vacuous"]:
            verdict = "independent (VACUOUS)"
        else:
            verdict = "independent"
        print(f"{n:3d} {name(lam):>8} {pairs:7d} {mode:>8} {st['tv']:8.4f}  {verdict}")
    print()
    print(f"hull cross-check failures across all rows: {fails}")
    print("Overall:", "PASS" if fails == 0 else "FAIL")
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
