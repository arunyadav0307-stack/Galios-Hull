"""
Side-check of the QUOTED Phase 1 item T10 (Theorems 8/10):
    dim Hull_H(C)  ==  sum_l dim Hull_H(C_l) ?
Over R_e with the paper's involution (conjugate-reciprocal, e | q+1).
Every ideal is enumerated (principally, CRT-free for e=2 by the exhaustive divisor-free route
used in r3_probe), and the hull is computed as C cap C^{perp_H}.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r3_probe import GF, find_irreducible, Ring, rref, nullspace, in_span, field_codes, ring_codes, ring_dual_basis, field_dual_basis


def intersection(F, A, B, ncols):
    """True subspace intersection span(A) cap span(B), by the standard kernel method.

    Unknowns x (one per row of A) and y (one per row of B); solve  sum x_i A_i - sum y_j B_j = 0
    and map the kernel back to the A-side. Keeping only those A-basis vectors that lie in B would
    miss intersections that do not align with the chosen basis of A.
    """
    pa, pb = len(A), len(B)
    rows = []
    for c in range(ncols):
        row = [A[i][c] for i in range(pa)] + [F.neg[B[j][c]] for j in range(pb)]
        rows.append(row)
    kernel = nullspace(F, rows, pa + pb)
    out = []
    for k in kernel:
        v = [0] * ncols
        for i in range(pa):
            if k[i]:
                for c in range(ncols):
                    v[c] = F.add[v[c]][F.mul[k[i]][A[i][c]]]
        out.append(v)
    return rref(F, out, ncols)[0]


def run(p, q, e, n, label):
    m, t = 0, q
    while t % p == 0:
        t //= p
        m += 1
    F = find_irreducible(p, 2 * m)
    F.conj_f = [F.pow(a, q) for a in range(F.Q)]
    R = Ring(F, e)
    R.set_frobenius(q)
    print("=" * 70)
    print(label)
    lam = 1
    alphas = [R.eval_at(lam, b) for b in R.roots]
    fc = [field_codes(F, n, a) for a in alphas]
    field_hull = {}
    for a, codes in zip(alphas, fc):
        for C in codes:
            D = field_dual_basis(F, C, n)
            field_hull[(a, tuple(map(tuple, C)))] = len(intersection(F, C, D, n))
    codes = ring_codes(R, F, n, lam, e)
    ok = bad = 0
    for C in codes:
        D = ring_dual_basis(R, F, C, n, e)
        h = len(intersection(F, C, D, n * e))
        # component-wise hull dimensions, computed independently by evaluation
        comps = []
        for beta in R.roots:
            from r3_probe import components_of
            comps.append(components_of(R, F, C, n, e, beta))
        tot = 0
        for j, Cj in enumerate(comps):
            Dj = field_dual_basis(F, Cj, n)
            tot += len(intersection(F, Cj, Dj, n))
        if h == tot:
            ok += 1
        else:
            bad += 1
    print(f"  lambda=1, alphas={alphas}: ideals {len(codes)}")
    print(f"  dim Hull(C) == sum_l dim Hull(C_l) : {ok}/{len(codes)}  (mismatches {bad})")


if __name__ == "__main__":
    run(3, 3, 2, 2, "T2: q=3, e=2, n=2")
    run(2, 2, 3, 2, "T1: q=2, e=3, n=2")
