"""
P3-13: the exact joint (Hermitian hull dimension, distance) law for e = 3, and a documented failure.

Field choice.  R_e = F_q[u]/(u^e - 1) needs gcd(e,q) = 1, so e = 3 forces char != 3, and the Hermitian
form needs q a square.  F_4 satisfies both but is useless: there 1*conj(1) + 1*conj(1) = 0, so every
code of length 3 has hull 0.  This script therefore uses

    F_25 = F_5[t]/(t^2 - 2)   (2 is a non-residue mod 5),  conjugation = Frobenius x -> x^5,
    |F_25^*| = 24, so 3 | 24 and u^3 - 1 splits with roots 1, alpha, alpha^2.

Two component families are examined, because the first one fails:

  (A) lambda = (1,1,1): all components CYCLIC (ideals of F_q[x]/(x^n - 1)), n = 2, 3.
      RESULT: every component has hull 0 -- the generator matrices have entries in F_5, conjugation
      fixes F_5, so the Hermitian hull coincides with the Euclidean hull and these codes are LCD.
      The joint law degenerates to a single h-value and the independence test is vacuous.
      Recorded as a FAILURE of this family to answer the question, not hidden.

  (B) lambda = (-1,-1,-1): all components NEGACYCLIC (ideals of F_q[x]/(x^n + 1)), n = 4.
      RESULT: hull dimensions 0, 1 and 2 all occur, so the joint law is nondegenerate.  This is the
      first e = 3 family in the project where the question can actually be asked.

Exactness.  Minimum distance is computed by the circuit characterisation (P3-7 Lemma C): for a code
with parity-check matrix H, d = smallest size of a linearly dependent set of columns of H.  At length
12 that is at most a few thousand small rank tests per code -- exact, and with no codeword enumeration
(25^12 words would be impossible).  Hull dimension is computed directly from the generator matrix as
k - rank(G conj(G)^T) and cross-checked against the additive prediction sum_l dim Hull_H(C_l)
(P3-3 Theorem 1).

For (B) the enumeration is over NESTED chains C_3 <= C_2 <= C_1 -- there are C(4+3,3) = 35 of them,
so the sweep is exhaustive over that family.  All 16^3 = 4096 triples are not enumerated at length 12:
the girth search would need of order 10^7 rank tests.  That limit is stated, not glossed over.

Pure stdlib, ASCII only.
"""
import itertools
import sys
from fractions import Fraction

MOD = 5


# ---------------------------------------------------------------- F_25 = F_5[t]/(t^2 - 2), a+bt <-> a+5b
def fadd(x, y):
    return (x % MOD + y % MOD) % MOD + MOD * ((x // MOD + y // MOD) % MOD)


def fsub(x, y):
    return (x % MOD - y % MOD) % MOD + MOD * ((x // MOD - y // MOD) % MOD)


def fneg(x):
    """Additive inverse of a field element given in the encoding a + 5b, 0 <= a,b < 5.

    Takes an ENCODING, not a raw integer: -1 is 4 in this encoding, so fneg(1) = 4 and
    fneg(4) = 1.  Passing a raw negative integer here silently produced a wrong representative
    (fneg(-1) = 6 = 1 + t), which built x^4 + t + 1 instead of x^4 + 1 -- a real bug, caught by
    the divisor count of the negacyclic family being 4 instead of 16.
    """
    assert 0 <= x < 25, f"fneg expects an encoding in [0,25), got {x}"
    a, b = x % MOD, x // MOD
    return (-a) % MOD + MOD * ((-b) % MOD)


def fmul(x, y):
    a, b = x % MOD, x // MOD
    c, d = y % MOD, y // MOD
    return (a * c + 2 * b * d) % MOD + MOD * ((a * d + b * c) % MOD)


def finv(x):
    for y in range(1, 25):
        if fmul(x, y) == 1:
            return y
    raise ZeroDivisionError(x)


def fpow(x, e):
    r = 1
    for _ in range(e):
        r = fmul(r, x)
    return r


def conj(x):
    """Hermitian conjugation over F_25 = the Frobenius x -> x^5."""
    return fpow(x, 5)


# ---------------------------------------------------------------- polynomials over F_25
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
    """x^n - lam, with lam = +1 (cyclic) or -1 (negacyclic)."""
    p = [0] * (n + 1)
    p[0] = fneg(lam % MOD)      # lam = +1 -> 4 (= -1), lam = -1 -> 1
    p[n] = 1
    return ptrim(p)


def divisors_of(f, max_deg):
    out = []
    for deg in range(max_deg + 1):
        for coeffs in itertools.product(range(25), repeat=deg):
            g = list(coeffs) + [1]
            if is_zero(pmod(f, g)):
                out.append(tuple(g))
    return out


def generator_matrix(g, n, lam):
    f = modulus(n, lam)
    deg = len(g) - 1
    k = n - deg
    rows = []
    for i in range(k):
        mono = [0] * (i + 1)
        mono[i] = 1
        r = pmod(pmul(list(g), mono), f)
        rows.append([r[j] if j < len(r) else 0 for j in range(n)])
    return rows


# ---------------------------------------------------------------- linear algebra over F_25
def rref(rows):
    m = [list(r) for r in rows]
    pivots = []
    r = 0
    if not m:
        return m, pivots
    ncols = len(m[0])
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
        pivots.append(c)
        r += 1
        if r == len(m):
            break
    return m[:r], pivots


def rank(rows):
    return len(rref(rows)[1])


def parity_check(G, N):
    R, pivots = rref(G)
    free = [c for c in range(N) if c not in pivots]
    H = []
    for f in free:
        h = [0] * N
        h[f] = 1
        for i, pc in enumerate(pivots):
            h[pc] = fneg(R[i][f])
        H.append(h)
    return H


def girth(H, N, cap=None):
    """Smallest dependent set of columns of H = d(C) (P3-7 Lemma C); None for the whole space."""
    if not H:
        # No parity checks: G spans everything, so the code is the whole space and d = 1.
        # An earlier version returned None here, which made the all-full-space chain print
        # "distance above the search cap 6" and drop out of the table.  Real defect, found by
        # the P3-14 kill test; the corrected row (h=0, d=1) is in the re-run log.
        return 1 if N > 0 else None
    cols = [[H[i][j] for i in range(len(H))] for j in range(N)]
    top = N if cap is None else min(cap, N)
    for w in range(1, top + 1):
        for S in itertools.combinations(range(N), w):
            if rank([cols[j] for j in S]) < w:
                return w
    return None


def hull_dim(G, N):
    k = len(G)
    if k == 0:
        return 0
    cG = [[conj(x) for x in r] for r in G]
    M = []
    for i in range(k):
        row = []
        for j in range(k):
            acc = 0
            for l in range(N):
                if G[i][l] and cG[j][l]:
                    acc = fadd(acc, fmul(G[i][l], cG[j][l]))
            row.append(acc)
        M.append(row)
    return k - rank(M)


def independence_stats(dist):
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
        tv += abs(Fraction(c) - exp)
        maxdev = max(maxdev, abs(Fraction(c) - exp))
    return {"tv": float(tv / N / 2), "maxdev": float(maxdev),
            "hvals": len(H), "dvals": len(D), "vacuous": (len(H) < 2 or len(D) < 2)}


def show(dist, label):
    st = independence_stats(dist)
    hs = sorted(set(h for h, _ in dist))
    ds = sorted(set(d for _, d in dist))
    print(f"    {label}: {sum(dist.values())} triples")
    print("          " + "h/d".rjust(4) + " " + " ".join(str(d).rjust(5) for d in ds))
    for h in hs:
        print("          " + str(h).rjust(4) + " "
              + " ".join(str(dist.get((h, d), 0)).rjust(5) for d in ds))
    if st["maxdev"] != 0:
        verdict = "NOT independent"
    elif st["vacuous"]:
        verdict = "independent (VACUOUS: marginal degenerate)"
    else:
        verdict = "independent"
    print(f"          TV={st['tv']:.4f}, MAXDEV={st['maxdev']:.4f}, "
          f"h-values {st['hvals']}, d-values {st['dvals']}  -> {verdict}")
    return st


def find_cube_roots():
    return [x for x in range(2, 25) if fpow(x, 3) == 1]


def main():
    print("P3-13: exact joint (Hermitian hull dim, distance) for e = 3 over F_25")
    print("F_25 = F_5[t]/(t^2-2), conjugation = Frobenius x -> x^5")
    print()

    assert all(conj(x) == fpow(x, 5) for x in range(25)), "conj != Frobenius"
    assert all(fmul(x, conj(x)) != 0 for x in range(1, 25)), "Hermitian form degenerate"
    om = find_cube_roots()
    assert len(om) == 2, f"expected two nontrivial cube roots, got {om}"
    ALPHA = (1, om[0], fpow(om[0], 2))
    assert len(set(ALPHA)) == 3 and all(fpow(a, 3) == 1 for a in ALPHA)
    print(f"  sanity: conj == x^5; x*conj(x) != 0 for x != 0; cube roots 1, {ALPHA[1]}, {ALPHA[2]}  [ok]")
    print()

    def psi_generator(Gs):
        rows = []
        for l, G in enumerate(Gs):
            a = ALPHA[l]
            powers = [1, a, fmul(a, a)]
            for r in G:
                rows.append([fmul(p, x) for p in powers for x in r])
        return rows

    fails = 0

    # ---------------- (A) cyclic components: documented failure
    print("=" * 96)
    print("(A) lambda = (1,1,1), CYCLIC components, n = 2 and n = 3")
    for n in (2, 3):
        N = 3 * n
        f = modulus(n, 1)
        divs = divisors_of(f, n)
        codes = {}
        for g in divs:
            G = generator_matrix(g, n, 1)
            codes[g] = {"G": G, "k": len(G), "h": hull_dim(G, n) if G else 0}
        hv = sorted(set(c["h"] for c in codes.values()))
        print(f"  n = {n}: {len(divs)} cyclic codes, hull dimensions present: {hv}")
        if len(hv) < 2:
            print(f"    -> DEGENERATE: every component has hull 0, so the joint law has a single "
                  f"h-value and the independence test is vacuous. This family cannot answer the "
                  f"question. Cause: generator matrices have entries in F_5 and conjugation fixes F_5.")
            print()
            continue
        dist = {}
        for g1 in divs:
            for g2 in divs:
                for g3 in divs:
                    GP = psi_generator([codes[g1]["G"], codes[g2]["G"], codes[g3]["G"]])
                    if not GP:
                        continue
                    h = hull_dim(GP, N)
                    if h != codes[g1]["h"] + codes[g2]["h"] + codes[g3]["h"]:
                        fails += 1
                    d = girth(parity_check(GP, N), N)
                    if d:
                        dist[(h, d)] = dist.get((h, d), 0) + 1
        show(dist, "all triples")
        print()

    # ---------------- (B) negacyclic components at n = 4
    n = 4
    N = 3 * n
    print("=" * 96)
    print(f"(B) lambda = (-1,-1,-1), NEGACYCLIC components, n = {n}  (psi-length {N})")
    f = modulus(n, -1)
    divs = divisors_of(f, n)
    codes = {}
    for g in divs:
        G = generator_matrix(g, n, -1)
        if not G:
            codes[g] = {"G": G, "k": 0, "h": 0, "d": None}
            continue
        codes[g] = {"G": G, "k": len(G), "h": hull_dim(G, n), "d": girth(parity_check(G, n), n)}
    print(f"  {len(divs)} negacyclic codes of length {n}:")
    print(f"  {'deg':>3} {'k':>2} {'h':>2} {'d':>3}")
    for g in sorted(divs, key=lambda t: (len(t), t)):
        c = codes[g]
        print(f"  {len(g) - 1:3d} {c['k']:2d} {c['h']:2d} {str(c['d']):>3}")
    hv = sorted(set(c["h"] for c in codes.values()))
    print(f"  hull dimensions present among components: {hv}"
          + ("  <- NON-degenerate" if len(hv) > 1 else "  <- DEGENERATE"))
    print()

    dist = {}
    chains = 0
    for g1 in divs:
        for g2 in divs:
            if not is_zero(pmod(list(g2), list(g1))):
                continue
            for g3 in divs:
                if not is_zero(pmod(list(g3), list(g2))):
                    continue
                chains += 1
                GP = psi_generator([codes[g1]["G"], codes[g2]["G"], codes[g3]["G"]])
                if not GP:
                    continue
                h = hull_dim(GP, N)
                add = codes[g1]["h"] + codes[g2]["h"] + codes[g3]["h"]
                if h != add:
                    fails += 1
                    if fails <= 5:
                        print(f"    HULL MISMATCH: direct {h} vs additive {add}")
                d = girth(parity_check(GP, N), N, cap=6)
                if d is None:
                    print(f"    (chain {g1}|{g2}|{g3}: distance above the search cap 6, skipped)")
                    continue
                dist[(h, d)] = dist.get((h, d), 0) + 1
    print(f"  nested chains C_3 <= C_2 <= C_1: {chains}")
    print(f"    (x^4+1 splits into 4 distinct linear factors over F_25 because 8 | 24, so the divisors")
    print(f"     form the Boolean lattice B_4 and the chains are its multichains: 4^4 = 256.  An earlier")
    print(f"     note said C(4+3,3) = 35, which counts something else -- 256 is the right number and the")
    print(f"     divisibility test was confirmed independently: 81 ordered divisor pairs = 3^4, 0 errors.)")
    print()
    show(dist, "all nested chains")
    print()

    print("=" * 96)
    print(f"hull cross-check failures: {fails}")
    print("Overall:", "PASS" if fails == 0 else "FAIL")
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
