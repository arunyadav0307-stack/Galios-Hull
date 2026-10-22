#!/usr/bin/env python3
"""
Code-table validator for the ten EAQECC examples added to Section 9 of
P1_15_MANUSCRIPT_DRAFT.tex (Table: ten new finite-field examples).

For every row (single component, lambda = 1, so mu = 1) this script checks,
using the repository GF implementation of validate_p1_14.py:

  * the listed factors are monic irreducible, multiply to x^{n0} - 1, and
    agree (as a set) with factor_distinct;
  * K = n - deg g equals the rank of the generator (shift) matrix;
  * the Galois hull dimension H agrees by two independent computations:
    (i) the exponent formula of Theorem T4 over the tau-orbits (sharp), and
    (ii) dim C - rank of the code-first Gram matrix;
  * the minimum distance d is computed exactly by two implementations of
    the parity-check column-dependency characterization, an explicit
    minimum-weight codeword is exhibited and checked to be a multiple
    of g, and (whenever q^K <= 300000) d is additionally confirmed by
    direct enumeration of all codewords;
  * the EAQECC parameters [[n, K-H, d; n-K-H]] and the EA Singleton defect
    Delta = (n - (K-H) + (n-K-H)) - 2(d-1) = 2(n-K-d+1).

Finite checks are evidence for these ten codes only, not proofs.
"""
import itertools
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from validate_p1_14 import GF, trim, pmul, ppow, pdivmod, pmod, monic_polys, factor_distinct, rank as gf_rank, sharp

FAILS = []


def check(cond, msg):
    if not cond:
        FAILS.append(msg)
        print("FAIL:", msg)


class FF:
    """Table-driven field arithmetic built on a validate_p1_14 GF instance."""

    def __init__(self, G):
        self.G = G
        self.q = G.q
        self.add = [[G.add(a, b) for b in range(G.q)] for a in range(G.q)]
        self.mul = [[G.mul(a, b) for b in range(G.q)] for a in range(G.q)]
        self.neg = [G.neg(a) for a in range(G.q)]
        self.inv = [0] + [G.inv(a) for a in range(1, G.q)]


def rank_ff(F, rows):
    A = [list(r) for r in rows if any(v != 0 for v in r)]
    if not A:
        return 0
    ncol = len(A[0])
    r0 = rk = 0
    for c in range(ncol):
        piv = next((i for i in range(r0, len(A)) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r0], A[piv] = A[piv], A[r0]
        iv = F.inv[A[r0][c]]
        A[r0] = [F.mul[v][iv] for v in A[r0]]
        for i in range(len(A)):
            if i != r0 and A[i][c] != 0:
                fac = A[i][c]
                A[i] = [F.add[v][F.mul[fac][F.neg[w]]] for v, w in zip(A[i], A[r0])]
        r0 += 1
        rk += 1
        if r0 == len(A):
            break
    return rk


def nullspace_ff(F, rows, n):
    A = [list(r) for r in rows]
    pivots = []
    r0 = 0
    for c in range(n):
        piv = next((i for i in range(r0, len(A)) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r0], A[piv] = A[piv], A[r0]
        iv = F.inv[A[r0][c]]
        A[r0] = [F.mul[v][iv] for v in A[r0]]
        for i in range(len(A)):
            if i != r0 and A[i][c] != 0:
                fac = A[i][c]
                A[i] = [F.add[v][F.mul[fac][F.neg[w]]] for v, w in zip(A[i], A[r0])]
        pivots.append(c)
        r0 += 1
        if r0 == len(A):
            break
    free = [c for c in range(n) if c not in pivots]
    basis = []
    for f in free:
        v = [0] * n
        v[f] = 1
        for i, pc in enumerate(pivots):
            v[pc] = F.neg[A[i][f]]
        basis.append(v)
    return basis


def dependent_insertion(F, cols):
    basis = {}
    for col in cols:
        v = list(col)
        while True:
            piv = next((i for i, x in enumerate(v) if x != 0), None)
            if piv is None:
                return True
            if piv not in basis:
                iv = F.inv[v[piv]]
                basis[piv] = [F.mul[x][iv] for x in v]
                break
            fac = v[piv]
            b = basis[piv]
            v = [F.add[x][F.mul[fac][F.neg[y]]] for x, y in zip(v, b)]
    return False


def min_distance_a(F, parity_rows, n, K):
    """Column dependency via incremental basis insertion."""
    m = n - K
    cols = [tuple(parity_rows[r][j] for r in range(m)) for j in range(n)]
    for w in range(1, m + 2):
        for subset in itertools.combinations(range(n), w):
            if dependent_insertion(F, [cols[j] for j in subset]):
                return w
    return m + 1


def min_distance_b(F, parity_rows, n, K):
    """Column dependency via explicit submatrix ranks (independent code)."""
    m = n - K
    for w in range(1, m + 2):
        for subset in itertools.combinations(range(n), w):
            rows_sub = [[parity_rows[r][j] for j in subset] for r in range(m)]
            if rank_ff(F, rows_sub) < w:
                return w
    return m + 1


def min_codeword(F, parity_rows, n, d, G, g):
    """Exhibit one codeword of weight d: solve H y = 0 on a dependent support."""
    for subset in itertools.combinations(range(n), d):
        rows_sub = [[parity_rows[r][j] for j in subset] for r in range(len(parity_rows))]
        if rank_ff(F, rows_sub) < d:
            y = nullspace_ff(F, rows_sub, d)[0]
            cw = [0] * n
            for j, val in zip(subset, y):
                cw[j] = val
            return cw
    return None


def brute_min_distance(F, gen_rows, n, K):
    best = n + 1
    for coeffs in itertools.product(range(F.q), repeat=K):
        if not any(coeffs):
            continue
        vec = [0] * n
        for i, c in enumerate(coeffs):
            if c:
                row = gen_rows[i]
                vec = [F.add[v][F.mul[c][w]] for v, w in zip(vec, row)]
        wt = sum(1 for v in vec if v != 0)
        if wt < best:
            best = wt
    return best


def hull_gram(G, k, g, n, K):
    if K == 0:
        return 0
    gam = list(g) + [G.zero] * (n - len(g))
    degg = len(g) - 1
    Phi = {}
    for delta in range(-(K - 1), K):
        tot = G.zero
        for s in range(max(0, -delta), min(degg, degg - delta) + 1):
            tot = G.add(tot, G.mul(gam[s], G.frob(gam[s + delta], k)))
        Phi[delta] = tot
    N = [[Phi[t - r] for r in range(K)] for t in range(K)]
    return K - gf_rank(G, N)


GF4 = GF(2, 2, [1, 1, 1])
GF8 = GF(2, 3, [1, 1, 0, 1])
GF9 = GF(3, 2, [1, 0, 1])

# (label, field, k, P, n0, ordered factors of x^{n0}-1, exponents,
#  expected (n, K, d, H))
ROWS = [
    ("F2, P=2, n0=3", GF(2, 1, [0, 1]), 0, 2, 3,
     [(1, 1), (1, 1, 1)], (2, 0), (6, 4, 2, 0)),
    ("F3, P=3, n0=2", GF(3, 1, [0, 1]), 0, 3, 2,
     [(1, 1), (2, 1)], (1, 3), (6, 2, 4, 1)),
    ("F4, P=1, n0=5", GF4, 1, 1, 5,
     [(1, 1), (1, 2, 1), (1, 3, 1)], (0, 0, 1), (5, 3, 3, 2)),
    ("F4, P=2, n0=3", GF4, 1, 2, 3,
     [(1, 1), (2, 1), (3, 1)], (0, 1, 2), (6, 3, 3, 1)),
    ("F5, P=5, n0=2", GF(5, 1, [0, 1]), 0, 5, 2,
     [(1, 1), (4, 1)], (1, 3), (10, 6, 4, 3)),
    ("F7, P=7, n0=2", GF(7, 1, [0, 1]), 0, 7, 2,
     [(1, 1), (6, 1)], (1, 3), (14, 10, 4, 4)),
    ("F8, P=1, n0=7", GF8, 1, 1, 7,
     [(c, 1) for c in range(1, 8)], (0, 0, 0, 0, 1, 1, 1), (7, 4, 4, 1)),
    ("F8, P=2, n0=3", GF8, 1, 2, 3,
     [(1, 1), (1, 1, 1)], (2, 0), (6, 4, 2, 0)),
    ("F9, P=1, n0=8", GF9, 1, 1, 8,
     [(c, 1) for c in range(1, 9)], (0, 1, 0, 0, 0, 1, 1, 1), (8, 4, 5, 2)),
    ("F9, P=3, n0=2", GF9, 1, 3, 2,
     [(1, 1), (2, 1)], (1, 2), (6, 3, 3, 2)),
]


def run_row(label, G, k, P, n0, facs, exps, expected):
    F = FF(G)
    n = P * n0
    lam = G.one
    check(G.pow(lam, 1 + G.p ** (G.d - k)) == G.one, f"{label}: compatibility")
    # x^{n0} - 1 (mu = 1)
    S = [G.zero] * (n0 + 1)
    S[0] = G.neg(G.one)
    S[n0] = G.one
    S = trim(G, S)
    prod = (G.one,)
    for f in facs:
        check(f[-1] == G.one, f"{label}: factor not monic: {f}")
        degf = len(f) - 1
        irred = all(
            pmod(G, f, cand) != (G.zero,)
            for dd in range(1, degf // 2 + 1)
            for cand in monic_polys(G, dd)
        ) if degf > 1 else True
        check(irred, f"{label}: factor reducible: {f}")
        prod = pmul(G, prod, tuple(f))
    check(prod == S, f"{label}: product of factors != x^n0 - 1")
    check(set(map(tuple, factor_distinct(G, S))) == set(map(tuple, facs)),
          f"{label}: factor list disagrees with factor_distinct")
    check(all(0 <= a <= P for a in exps), f"{label}: exponent out of range")

    g = (G.one,)
    for f, a in zip(facs, exps):
        g = pmul(G, g, ppow(G, tuple(f), a))
    degg = len(g) - 1
    K = n - degg

    gen_rows = []
    for i in range(K):
        row = [0] * n
        for j, cj in enumerate(g):
            row[i + j] = cj
        gen_rows.append(row)
    check(rank_ff(F, gen_rows) == K, f"{label}: generator rank != K")

    # H by the T4 exponent formula over tau-orbits
    fidx = {tuple(f): i for i, f in enumerate(facs)}
    seen = set()
    orbits = []
    for f in facs:
        tf = tuple(f)
        if tf in seen:
            continue
        orb = []
        cur = tf
        while cur not in seen:
            seen.add(cur)
            orb.append(cur)
            cur = sharp(G, k, cur)
        orbits.append(orb)
    check(set().union(*[set(o) for o in orbits]) == set(map(tuple, facs)),
          f"{label}: tau does not permute the factors")
    H_formula = 0
    for orb in orbits:
        idx = [fidx[f] for f in orb]
        w = len(orb[0]) - 1  # m_s = 1, so w_O = deg f
        for i in range(len(idx)):
            H_formula += w * min(P - exps[idx[i]], exps[idx[i - 1]])
    H_gram = hull_gram(G, k, g, n, K)
    check(H_formula == H_gram, f"{label}: H formula {H_formula} != Gram {H_gram}")
    H = H_formula

    parity_rows = nullspace_ff(F, gen_rows, n)
    check(len(parity_rows) == n - K, f"{label}: parity-check rank")
    d_a = min_distance_a(F, parity_rows, n, K)
    d_b = min_distance_b(F, parity_rows, n, K)
    check(d_a == d_b, f"{label}: distance implementations disagree {d_a} vs {d_b}")
    d = d_a
    cw = min_codeword(F, parity_rows, n, d, G, g)
    check(cw is not None and sum(1 for v in cw if v != 0) == d,
          f"{label}: no explicit minimum-weight codeword")
    if cw is not None:
        rem = pdivmod(G, trim(G, tuple(cw)), g)[1]
        check(rem == (G.zero,), f"{label}: minimum-weight word not a multiple of g")
    brute_note = "skipped (q^K > 300000)"
    if G.q ** K <= 300000:
        d_brute = brute_min_distance(F, gen_rows, n, K)
        check(d_brute == d, f"{label}: brute-force distance {d_brute} != {d}")
        brute_note = f"brute force agrees ({G.q}^{K} codewords)"

    kappa, c = K - H, n - K - H
    defect = (n - kappa + c) - 2 * (d - 1)
    check(defect == 2 * (n - K - d + 1), f"{label}: defect identity")
    check(kappa >= 1 and c >= 0, f"{label}: EA parameters out of range")
    en, eK, ed, eH = expected
    check((n, K, d, H) == expected,
          f"{label}: got (n,K,d,H)={(n, K, d, H)}, expected {expected}")
    mark = "*" if defect == 0 else ("dagger" if defect == 2 else "none")
    print(f"{label}: a={exps}  [{n},{K},{d}]  H={H}  "
          f"EAQECC=[[{n},{kappa},{d};{c}]]  Delta={defect} ({mark})  "
          f"[H: formula==Gram; d: two implementations + min-weight word; {brute_note}]")


if __name__ == "__main__":
    for row in ROWS:
        run_row(*row)
    print()
    if FAILS:
        print(f"{len(FAILS)} CHECK(S) FAILED")
        raise SystemExit(1)
    print("ALL 10 CODE-TABLE ROWS VERIFIED")
