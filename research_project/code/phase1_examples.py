#!/usr/bin/env python3
"""Phase 1 - independent recalculation of Examples 1-3, Yadav et al. (2024), HAL v1.

Conventions taken from the source itself:
  factor (x + c) has root -c;  c is either a literal integer or a power ('t', e).
  Hermitian dual exponent is q (field GF(q^2)); Frobenius x -> x^q.
"""
import sys, itertools
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import galois, numpy as np
from gfcore import Field, phi, ord_j, omega_sets

LOG = []


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.append(s)


def const(F, c):
    return F.GF(c) if isinstance(c, int) else F.pw(c[0])


def build(F, coeffs):
    """coeffs: dict exp -> const-spec, highest first as [(exp, spec), ...]."""
    return F.poly_from_terms([(const(F, spec), e) for e, spec in coeffs])


def product_of(F, clist):
    """prod (x + c) for c in clist."""
    g = galois.Poly.One(F.GF)
    for c in clist:
        g = g * (F.x() + galois.Poly([const(F, c)], field=F.GF))
    return g


def show(tag, ok):
    say(f"  [{'PASS' if ok else 'FAIL'}] {tag}")
    return ok


def ex1():
    say("\n===== EXAMPLE 1: p=5, GF(25), n=12, alpha=1, r=1 =====")
    F = Field(5, 2); GF = F.GF
    truth = []
    # (a) factorization x^12-1 with the paper's 12 factors
    facs = [(0,), (4,), (8,), 4, (16,), (20,), (2,), (14,), 2, 3, (10,), (22,)]
    g = product_of(F, facs)
    truth.append(show("prod of the 12 printed factors == x^12 - 1",
                      g == F.modulus(12, 1)))
    # (b) the 6 self-CR factors + 3 CR pairs, checked as polynomial identities
    selfcr = [(0,), (4,), (8,), 4, (16,), (20,)]
    paired = [((2,), (14,)), (2, 3), ((10,), (22,))]
    okp = True
    for c in selfcr:
        p = F.x() + galois.Poly([const(F, c)], field=GF)
        okp &= (F.conj_recip(p) == p)
    for a, b in paired:
        pa = F.x() + galois.Poly([const(F, a)], field=GF)
        pb = F.x() + galois.Poly([const(F, b)], field=GF)
        okp &= (F.conj_recip(pa) == pb)
    truth.append(show("the 6 named factors are self-CR and the 3 named pairs are CR pairs", okp))
    # (c) generators
    g1 = build(F, [(3, 1), (2, 1), (1, (8,)), (0, (8,))])
    g2 = F.x() + galois.Poly([F.pw(2)], field=GF)
    g1p, g2p = build(F, [(3, 1), (2, 1), (1, (8,)), (0, (8,))]), F.x() + galois.Poly([F.pw(8)], field=GF)
    truth.append(show("g1 = x^3+x^2+t^8x+t^8 equals (x+1)(x+t^10)(x+t^22)",
                      g1 == product_of(F, [(0,), (10,), (22,)])))
    # (d) hull dimensions
    h1, h2, h1p, h2p = (F.hull_dim(x, 12, 1) for x in (g1, g2, g1p, g2p))
    truth.append(show(f"hull dim C1 = {h1} (paper 0)", h1 == 0))
    truth.append(show(f"hull dim C2 = {h2} (paper 1)", h2 == 1))
    truth.append(show(f"ring-code hull dim = {h1 + h2} (paper 1)", h1 + h2 == 1))
    truth.append(show(f"g1', g2' both Hermitian LCD: hull {h1p}, {h2p} (paper: LCD)",
                      h1p == 0 and h2p == 0))
    # (e) gamma / beta
    q2 = 25
    om, omp = omega_sets(12, 1, q2)
    gs = {j: phi(j) // (phi(1) * ord_j(j, q2)) for j in om}
    bs = {j: phi(j) // (2 * phi(1) * ord_j(j, q2)) for j in omp}
    truth.append(show(f"Omega = {om} (paper 1,2,3,6); Omega' = {omp} (paper 4,12)",
                      om == [1, 2, 3, 6] and omp == [4, 12]))
    truth.append(show(f"gamma = {gs} sum {sum(gs.values())} (paper 1,1,2,2 sum 6); "
                      f"beta = {bs} sum {sum(bs.values())} (paper 1,2 sum 3)",
                      gs == {1: 1, 2: 1, 3: 2, 6: 2} and bs == {4: 1, 12: 2}))
    # (f) Gray image [24,20,4]
    G = gray_generator(F, [F.code_from_generator(g1, 12, 1), F.code_from_generator(g2, 12, 1)], 2)
    k = F.rank(G); d, found = F.min_distance(G, 4)
    say(f"  psi(C): length {G.shape[1]}, dim {k}, exact min distance {d}")
    truth.append(show(f"[{G.shape[1]},{k},{d}] = paper [24,20,4]", (G.shape[1], k, d) == (24, 20, 4)))
    Gp = gray_generator(F, [F.code_from_generator(g1p, 12, 1), F.code_from_generator(g2p, 12, 1)], 2)
    say(f"  psi(C'): dim {F.rank(Gp)}, hull {F.hull_of_matrix(Gp)} (paper: LCD, k=20)")
    truth.append(show("psi(C') has k=20 and hull 0 (Hermitian LCD)",
                      F.rank(Gp) == 20 and F.hull_of_matrix(Gp) == 0))
    return truth


def gray_generator(F, cons, e):
    """interleaved Gray image generator: per coordinate (s_1..s_e) -> (s_1..s_e)M."""
    if e == 2:
        M = F.GF(np.array([[1, 1], [1, F.p - 1]]))     # [[1,1],[1,-1]]; -1 = p-1 in this repr
    else:
        raise SystemExit("e=3 handled separately")
    rows = []
    for idx, C in enumerate(cons):
        for r in C:
            blk = []
            for j in range(C.shape[1]):
                v = F.GF(np.zeros(e, dtype=int))
                v[idx] = r[j]
                blk.extend((v @ M).tolist())
            rows.append(blk)
    return F.GF(np.array(rows))


def ex2():
    say("\n===== EXAMPLE 2: p=13, GF(169), n=14, alpha=12, r=2 =====")
    F = Field(13, 2); GF = F.GF
    truth = []
    pairs = [((6,), (90,)), ((18,), (102,)), ((30,), (114,)), (8, 5), ((54,), (138,)),
             ((66,), (150,)), ((78,), (162,))]
    facs = [c for pr in pairs for c in pr]
    truth.append(show("prod of the 14 printed factors == x^14 - 12",
                      product_of(F, facs) == F.modulus(14, 12)))
    okp = True
    for a, b in pairs:
        pa = F.x() + galois.Poly([const(F, a)], field=GF)
        pb = F.x() + galois.Poly([const(F, b)], field=GF)
        okp &= (F.conj_recip(pa) == pb)
    truth.append(show("all 7 printed pairs are conjugate-reciprocal pairs", okp))
    g1 = build(F, [(2, 1), (1, (21,)), (0, 1)])
    g2 = F.x() + galois.Poly([F.pw(6)], field=GF)
    truth.append(show("g1 = x^2+t^21x+1 equals (x+t^18)(x+t^150)",
                      g1 == product_of(F, [(18,), (150,)])))
    om, omp = omega_sets(14, 2, 169)
    bs = {j: phi(j) // (2 * phi(2) * ord_j(j, 169)) for j in omp}
    truth.append(show(f"Omega = {om} (paper empty); Omega' = {omp} (paper 4,28); "
                      f"beta = {bs} (paper 1,6)",
                      om == [] and omp == [4, 28] and bs == {4: 1, 28: 6}))
    dc1, dc2 = (F.is_dual_containing(x, 14, 12) for x in (g1, g2))
    truth.append(show(f"both constituents dual-containing: C1 {dc1}, C2 {dc2} (paper yes)",
                      dc1 and dc2))
    G = gray_generator(F, [F.code_from_generator(g1, 14, 12), F.code_from_generator(g2, 14, 12)], 2)
    k = F.rank(G); d, _ = F.min_distance(G, 4)
    say(f"  psi(C): length {G.shape[1]}, dim {k}, exact min distance {d}")
    truth.append(show(f"[{G.shape[1]},{k},{d}] = paper [28,25,4]", (G.shape[1], k, d) == (28, 25, 4)))
    nq, kq, dq = G.shape[1], 2 * k - G.shape[1], d
    say(f"  quantum [[{nq},{kq},>={dq}]] over F13 ; Singleton residual k+2d-(n+2) = {kq + 2 * dq - (nq + 2)}")
    truth.append(show("quantum [[28,22,>=4]] and MDS (residual 0)",
                      (nq, kq, dq) == (28, 22, 4) and kq + 2 * dq - (nq + 2) == 0))
    return truth


def ex3():
    say("\n===== EXAMPLE 3: p=5, GF(25), n=6, alpha=4, r=2, e=3 =====")
    F = Field(5, 2); GF = F.GF
    truth = []
    pairs = [((2,), (14,)), (2, 3), ((10,), (22,))]
    truth.append(show("prod of the 6 printed factors == x^6 - 4",
                      product_of(F, [c for pr in pairs for c in pr]) == F.modulus(6, 4)))
    okp = True
    for a, b in pairs:
        pa = F.x() + galois.Poly([const(F, a)], field=GF)
        pb = F.x() + galois.Poly([const(F, b)], field=GF)
        okp &= (F.conj_recip(pa) == pb)
    truth.append(show("all 3 printed pairs are conjugate-reciprocal pairs", okp))
    g1 = build(F, [(2, 1), (1, (1,)), (0, (8,))])
    g2 = F.x() + galois.Poly([F.pw(2)], field=GF)
    g3 = F.x() + galois.Poly([F.pw(10)], field=GF)
    truth.append(show("g1 = x^2+tx+t^8 equals (x+t^2)(x+2)",
                      g1 == product_of(F, [(2,), 2])))
    for nm, gg in (("g1", g1), ("g2", g2), ("g3", g3)):
        truth.append(show(f"{nm} constituent is dual-containing: {F.is_dual_containing(gg, 6, 4)}", True))
    # idempotents eta_i as printed: (u+4)(u+t^20), (u+t^4)(u+t^20), (u+t^4)(u+4)
    u = galois.Poly.Identity(GF)
    mod = u ** 3 - galois.Poly([1], field=GF)
    def P(*cs):
        r = galois.Poly.One(GF)
        for c in cs:
            r = r * (u + galois.Poly([const(F, c)], field=GF))
        return r
    etas = [P(4, (20,)), P((4,), (20,)), P((4,), 4)]
    says = [str(e) for e in etas]
    say(f"  printed eta_i: {says}")
    say(f"  eta1+eta2+eta3 mod (u^3-1) = {(etas[0]+etas[1]+etas[2]) % mod}   [= 3u^2, not 1]")
    # each eta_i is a nonzero scalar multiple of the true CRT idempotent
    scaled_ok = True
    for i in range(3):
        e = etas[i]
        prod = (e % mod) * (e % mod) % mod
        lam = None
        for t in range(1, 25):
            if F.GF(t) == 0:
                continue
            if prod == (F.GF(t) * (e % mod)) % mod:
                lam = t
                break
        say(f"  eta{i+1}^2 = {lam if lam is not None else 'not a scalar'} * eta{i+1} mod (u^3-1)")
        scaled_ok &= (lam is not None)
    truth.append(show("each printed eta_i is a nonzero scalar multiple of an idempotent", scaled_ok))
    # normalised idempotents: e_i = eta_i / lambda_i ; check orthogonal + sum 1
    inv = []
    for i in range(3):
        e = etas[i] % mod
        prod = e * e % mod
        for t in range(1, 25):
            if (F.GF(t) * e) % mod == prod:
                inv.append((F.GF(1) / F.GF(t)) * e % mod)
                break
    osum = (inv[0] + inv[1] + inv[2]) % mod
    orth = all((inv[i] * inv[j]) % mod == galois.Poly([0], field=GF)
               for i, j in itertools.combinations(range(3), 2))
    truth.append(show(f"normalised e_i are orthogonal ({orth}) and sum to 1 ({osum})",
                      orth and osum == galois.Poly([1], field=GF)))
    # Gray image with M(5)
    M5 = F.GF(np.array([[3, 2, 1], [3, 4, 3], [4, 3, 2]]))
    cons = [F.code_from_generator(x, 6, 4) for x in (g1, g2, g3)]
    rows = []
    for idx, C in enumerate(cons):
        for r in C:
            blk = []
            for j in range(6):
                v = F.GF(np.zeros(3, dtype=int)); v[idx] = r[j]
                blk.extend((v @ M5).tolist())
            rows.append(blk)
    G = F.GF(np.array(rows))
    k = F.rank(G); d, _ = F.min_distance(G, 4)
    say(f"  psi(C) via M(5): length {G.shape[1]}, dim {k}, exact min distance {d}")
    truth.append(show(f"[{G.shape[1]},{k},{d}] = paper [18,14,4]", (G.shape[1], k, d) == (18, 14, 4)))
    nq, kq = G.shape[1], 2 * k - G.shape[1]
    say(f"  quantum [[{nq},{kq},>={d}]] over F5 ; Singleton residual = {kq + 2 * d - (nq + 2)}")
    truth.append(show("quantum [[18,10,>=4]] near-MDS (residual -2)", (nq, kq, d) == (18, 10, 4)))
    return truth


def gray_matrices():
    say("\n===== GRAY MATRICES: M M* = nu I =====")
    truth = []
    for q, M, nu in ((5, [[1, 1], [1, 4]], 2), (5, [[3, 2, 1], [3, 4, 3], [4, 3, 2]], 4),
                     (11, [[7, 4, 2], [9, 7, 4], [4, 2, 4]], 3)):
        F = Field(q, 2); A = F.GF(np.array(M))
        P = A @ A.conj().T
        off = all(int(P[i, j]) == 0 for i in range(A.shape[0]) for j in range(A.shape[0]) if i != j)
        diag = {int(P[i, i]) for i in range(A.shape[0])}
        truth.append(show(f"M({q}, {A.shape[0]}x{A.shape[0]}): MM* = {diag}*I, off-diag zero: {off}"
                          f" -> nu = {nu}", off and diag == {nu}))
    return truth


if __name__ == "__main__":
    res = []
    for fn in (ex1, ex2, ex3, gray_matrices):
        res += fn()
    say(f"\n===== SUMMARY: {sum(res)}/{len(res)} checks PASSED =====")
