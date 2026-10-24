"""
Phase 3 / literature checkpoint companion: is dim Hull_H(psi(C)) equal to dim Hull_H(C)?

Motivation.  Tian, Gao & Gao (Quantum Inf. Process. 23(1):9, 2024) obtain "dimensions of hulls
of Gray images of constacyclic codes" over F_q + vF_q.  That is the closest ring-level prior art
to P3-3, so it matters whether the Gray-image hull is a new invariant or the same one.

The source paper's Lemma 3 gives psi(C^perp_H) = psi(C)^perp_H, and psi is bijective, so
psi restricts to a bijection Hull_H(C) -> Hull_H(psi(C)).  Hence

    dim Hull_H(psi(C)) = dim Hull_H(C) = sum_l dim Hull_H(C_l)      (Theorem 1 of P3-3),

i.e. the hull dimension of the Gray image is NOT a new invariant.  This script checks that
directly, computing the two sides by independent routes:

  left  : build psi(C) explicitly in F_{q^2}^{en} and take its Hermitian hull dimension there
          (field-level machinery, no reference to the ring);
  right : sum of the constituent hull dimensions (Theorem 1), each computed by the kernel method.

If they agree on every tuple, the identity holds on the instance and Tian-Gao-Gao's object is
the same number for e = 2.

ASCII only, stdlib only.
"""
import itertools
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "phase2", "r1_probe"))
sys.path.insert(0, os.path.join(HERE, "..", "phase2", "r3_probe"))
sys.path.insert(0, os.path.join(HERE, "..", "phase2", "r2_probe"))
from r1_probe import make_field, divisors, code_from_generator, hull_dim   # noqa: E402
from r2_probe import LightRing                                             # noqa: E402


def psibasis(F, R, roots, C1, C2, M, n):
    """Image of the code C1 x C2 under psi, as a spanning list in F_{q^2}^{2n}."""
    # per-component scalars: s_k = c_k / eta_k(mu_k)
    scale = []
    for mu in roots:
        eta = R.lagrange_numerator(mu)
        val = R.eval_at(eta, mu)
        inv = next(c for c in range(1, F.Q) if F.mul[val][c] == F.one)
        scale.append(inv)
    # The product code C1 x C2 has basis {(a,0)} union {(0,b)}; the set
    # {a in basis1} x {b in basis2} does NOT span it.  (First version used the product of
    # the two bases and reported 112 spurious mismatches.)
    pairs = [(a, None) for a in C1] + [(None, b) for b in C2]
    rows = []
    for a, b in pairs:
        s1 = [F.mul[scale[0]][x] for x in a] if a is not None else [F.zero] * n
        s2 = [F.mul[scale[1]][x] for x in b] if b is not None else [F.zero] * n
        out = []
        for i in range(n):
            for j in range(2):
                acc = F.zero
                for k, s in enumerate((s1, s2)):
                    if M[k][j] % F.p:
                        acc = F.add[acc][F.mul[M[k][j] % F.p][s[i]]]
                out.append(acc)
        rows.append(out)
    return rows


def rref_basis(F, rows, ncols):
    from r3_probe import rref
    return rref(F, rows, ncols)[0]


def main():
    F = make_field(3, 3)
    R = LightRing(F, 2)
    roots = R.roots()
    print(f"F_{F.Q}, e=2, roots of u^2-1: {roots}")
    n = 2
    M = ((1, 1), (1, -1))
    codes = []
    for alpha in range(1, F.Q):
        for g in divisors(F, n, alpha):
            codes.append((alpha, g, code_from_generator(F, g, n, alpha)))
    codes = [c for c in codes if c[2]]
    print(f"  field codes: {len(codes)}")
    agree = differ = 0
    for i, ci in enumerate(codes):
        for j, cj in enumerate(codes):
            psi = rref_basis(F, psibasis(F, R, roots, ci[2], cj[2], M, n), 2 * n)
            left = hull_dim(F, psi, 2 * n) if psi else 0
            right = (hull_dim(F, ci[2], n) if ci[2] else 0) + \
                    (hull_dim(F, cj[2], n) if cj[2] else 0)
            if left == right:
                agree += 1
            else:
                differ += 1
                if differ <= 5:
                    print(f"    MISMATCH alpha={ci[0],cj[0]} psi-hull={left} sum-hull={right}")
    print(f"  pairs: {len(codes)**2};  dim Hull(psi(C)) = sum_l dim Hull(C_l):  "
          f"{agree} agree, {differ} differ")
    print("  => the Gray-image hull dimension is the same invariant, not a new one"
          if differ == 0 else "  => identity FAILS on this instance")


if __name__ == "__main__":
    main()
