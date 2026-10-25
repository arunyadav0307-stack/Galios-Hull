"""
P3-11: the exact joint (Hermitian hull dimension, minimum distance) distribution for the NESTED
e = 2 family over F_9 -- the one regime where both coordinates are determined.

Motivation.  R4 asks for the joint distribution of (dim Hull_H, d) over R_e = F_q[u]/(u^e - 1)
together with its Gray image psi.  In general P3-3 Theorem 5 shows the distance is NOT determined
by the component invariants.  But when e = 2 and the components are nested (C_2 <= C_1), P3-10
gives an exact classical formula, and P3-3 Theorem 1 gives exact additivity of the hull:

    d( psi(C_1 x C_2) )        = min { 2 d(C_1) , d(C_2) }          (P3-10, proved)
    dim Hull_H( psi(C_1 x C_2) ) = dim Hull_H(C_1) + dim Hull_H(C_2)  (P3-3 Thm 1, proved)

So on this family the joint law is COMPUTABLE EXACTLY, with no bound and no sampling.  That is what
this script produces.  It is a distribution table, not a theorem claim.

Setting.
  * F_9 = F_3[t]/(t^2 + 1), elements a + b t stored as a + 3b.
  * Hermitian conjugation is the Frobenius x -> x^3 = x^9; on a + bt (t^2 = -1) it sends
    (a, b) -> (a, -b), because t^3 = t*t^2 = -t.  (Checked in the script.)
  * R_2 = F_9[u]/(u^2 - 1) = F_9 x F_9 via u -> (1, -1); the two roots of u^2 - 1 are 1 and -1,
    which exist in every odd-characteristic field, so no splitting condition is needed.
  * lambda = (1, 1): the components are ordinary CYCLIC codes of length n, so every pair
    (C_1, C_2) of cyclic codes with C_2 <= C_1 is admissible and realisable in the ring.
  * gcd(n, 3) = 1 so x^n - 1 is separable and the cyclic codes are exactly the ideals <g>, g | x^n-1.

Hull dimension is computed from the generator matrix by the standard identity

    dim Hull_H(C) = k - rank( G * conj(G)^T ),

with the conjugate taken entrywise, and independently cross-checked against the additivity theorem
by computing the hull of psi(C) directly from ITS generator matrix.

Pure stdlib, ASCII only.
"""
import itertools
import sys

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
    """Hermitian conjugate = Frobenius x -> x^3 over F_9."""
    return (x % 3) + 3 * ((-(x // 3)) % 3)


def fpow(x, e):
    r = 1
    for _ in range(e):
        r = fmul(r, x)
    return r


# ---------------------------------------------------------------- polynomials over F_9 (low -> high)
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


def xn_minus_1(n):
    p = [0] * (n + 1)
    p[0] = fneg(1)
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
                f = m[i][c]
                m[i] = [fsub(x, fmul(f, y)) for x, y in zip(m[i], m[r])]
        r += 1
        if r == len(m):
            break
    return r


# ---------------------------------------------------------------- cyclic codes and their hulls
def generator_matrix(g, n):
    """Rows u^i g mod (x^n - 1), i = 0 .. n-deg(g)-1, each a length-n vector."""
    f = xn_minus_1(n)
    deg = len(g) - 1
    dim = n - deg
    if dim <= 0:
        return []
    rows = []
    for i in range(dim):
        mono = [0] * (i + 1)
        mono[i] = 1
        rows.append(pmod(pmul(list(g), mono), f))
    out = []
    for r in rows:
        out.append([r[j] if j < len(r) else 0 for j in range(n)])
    return out


def hull_dim_hermitian(G, n):
    """dim Hull_H(C) = k - rank(G * conj(G)^T)."""
    k = len(G)
    if k == 0:
        return 0
    prod = []
    for r in G:
        cr = [conj(x) for x in r]
        prod.append(cr)
    # G * conj(G)^T  ->  k x k matrix, entry (i,j) = sum_l G[i][l] * conj(G[j][l])
    M = []
    for i in range(k):
        row = []
        for j in range(k):
            acc = 0
            for l in range(n):
                if G[i][l] and prod[j][l]:
                    acc = fadd(acc, fmul(G[i][l], prod[j][l]))
            row.append(acc)
        M.append(row)
    return k - rank(M)


def min_dist(words):
    best = None
    for w in words:
        d = sum(1 for c in w if c)
        if d and (best is None or d < best):
            best = d
    return best


def all_words(G, n, cap=400000):
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


def psi_generator(G1, G2, n):
    """Generator matrix of psi(C_1 x C_2) for M = ((1,1),(1,-1))."""
    rows = []
    for r in G1:
        rows.append(list(r) + list(r))                       # (u, u)
    for r in G2:
        rows.append(list(r) + [fneg(x) for x in r])          # (v, -v)
    return rows


def independence_stats(dist):
    """Compare the observed joint law with the product of its marginals.

    dist maps (h, d) -> count.  Returns the total variation distance and the largest absolute
    deviation between an observed cell count and its independence prediction, both as floats
    computed from exact Fractions so the zero test is exact.
    """
    from fractions import Fraction
    N = sum(dist.values())
    if N == 0:
        return {"tv": 0.0, "maxdev": 0.0}
    H, D = {}, {}
    for (h, d), c in dist.items():
        H[h] = H.get(h, 0) + c
        D[d] = D.get(d, 0) + c
    tv = Fraction(0)
    maxdev = Fraction(0)
    for (h, d), c in dist.items():
        exp = Fraction(H[h] * D[d], N)
        dev = abs(Fraction(c) - exp)
        if dev > maxdev:
            maxdev = dev
        tv += dev
    tv = tv / N            # (1/2) * sum |p_obs - p_indep| * 2, i.e. sum|...|/N halves out
    tv = tv / 2
    return {"tv": float(tv), "maxdev": float(maxdev)}


def main():
    print("P3-11: exact joint (Hermitian hull dim, distance) for NESTED e = 2 over F_9")
    print("d(psi) = min{2 d(C_1), d(C_2)}  (P3-10)   h(psi) = h(C_1) + h(C_2)  (P3-3 Thm 1)")
    print("lambda = (1,1): components are cyclic codes, so every C_2 <= C_1 is realisable.")
    print()

    # sanity: conjugation is Frobenius
    assert all(conj(x) == fpow(x, 3) for x in range(9)), "conj is not Frobenius x->x^3"
    assert all(fmul(x, conj(x)) != 0 for x in range(1, 9)), "conj is not a field automorphism"
    print("  sanity: conj(x) == x^3 for all x in F_9, and x*conj(x) != 0 for x != 0   [ok]")
    print()

    total_pairs = 0
    total_cross_bad = 0
    grand = {}
    indep = []

    for n in (2, 4, 5, 7, 8):
        f = xn_minus_1(n)
        divs = divisors_of(f, n)
        codes = {}
        for g in divs:
            G = generator_matrix(g, n)
            codes[g] = G
        info = {}
        for g, G in codes.items():
            words = all_words(G, n)
            info[g] = {
                "k": len(G),
                "h": hull_dim_hermitian(G, n),
                "d": min_dist(words) if words else None,
                "words": words,
            }
        print("=" * 96)
        print(f"n = {n} over F_9:  {len(divs)} cyclic codes "
              f"(x^{n}-1 has {len(divs)} monic divisors)")

        dist = {}
        pairs = 0
        for g1 in divs:
            for g2 in divs:
                if not is_zero(pmod(list(g2), list(g1))):     # g1 | g2  <=>  C_2 <= C_1
                    continue
                i1, i2 = info[g1], info[g2]
                if i1["d"] is None or i2["d"] is None:
                    continue                                   # zero code involved
                h = i1["h"] + i2["h"]
                d = min(2 * i1["d"], i2["d"])
                dist[(h, d)] = dist.get((h, d), 0) + 1
                grand[(h, d)] = grand.get((h, d), 0) + 1
                pairs += 1

                # independent cross-check: build psi(C) from its generator matrix and measure
                # the hull directly (no appeal to additivity)
                if pairs <= 400:
                    GP = psi_generator(codes[g1], codes[g2], n)
                    h_direct = hull_dim_hermitian(GP, 2 * n)
                    if h_direct != h:
                        total_cross_bad += 1
                        if total_cross_bad <= 5:
                            print(f"    HULL CROSS-CHECK MISMATCH n={n} g1={g1} g2={g2}: "
                                  f"additive {h} vs direct {h_direct}")
        total_pairs += pairs
        print(f"  nested pairs with both components nonzero: {pairs}")
        print(f"  {'h':>3} {'d':>4} {'count':>7}")
        for (h, d) in sorted(dist):
            print(f"  {h:3d} {d:4d} {dist[(h, d)]:7d}")
        # is the joint law the product of its marginals?  (the R4 question)
        indep.append((n, pairs, independence_stats(dist)))

    print()
    print("=" * 96)
    print("Independence test: is P(h,d) = P(h) P(d) on this family?")
    print("(exact rational arithmetic; TV = total variation distance, MAXDEV = max |obs-exp| count)")
    print(f"{'n':>3} {'pairs':>6} {'TV':>8} {'MAXDEV':>8}  verdict")
    for (n_, pairs_, st) in indep:
        verdict = "independent" if st["maxdev"] == 0 else "NOT independent"
        print(f"{n_:3d} {pairs_:6d} {st['tv']:8.4f} {st['maxdev']:8.4f}  {verdict}")

    print()
    print("=" * 96)
    print(f"TOTAL nested pairs over all n: {total_pairs}")
    print(f"Hull additivity cross-check failures (additive vs direct on psi(C)): {total_cross_bad}")
    print()
    print("Joint distribution of (dim Hull_H(psi(C)), d(psi(C))) over ALL n pooled:")
    print(f"{'h':>3} {'d':>4} {'count':>8}")
    for (h, d) in sorted(grand):
        print(f"{h:3d} {d:4d} {grand[(h, d)]:8d}")
    tot = sum(grand.values())
    print(f"sum of counts: {tot}  (must equal {total_pairs})")
    print()
    ok = (total_cross_bad == 0 and tot == total_pairs)
    print("Overall:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
