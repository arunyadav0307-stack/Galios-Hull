#!/usr/bin/env python3
"""
Independent finite-field verification for the repeated-root formulas.

For each test family this script:
  1. factors x^{n'} - lambda0 over K via Distinct-Degree + Cantor-Zassenhaus;
  2. builds g_e = prod f_i^{e_i}, 0 <= e_i <= M, a divisor of
     (x^{n'} - lambda0)^M = x^n - lambda0^M;
  3. computes the k-Galois hull dimension DIRECTLY from a generator matrix
     and the Gram matrix B * sigma(B)^T (no orbit formula);
  4. compares with sum_i deg(f_{tau(i)}) * min(e_i, M-e_{tau(i)});
  5. for exhaustive families, compares the full joint histogram with
     rr_enumerator.trace_dp_global.

Run from the workspace root:
    python3 code/verify_rr.py [--quick]   (from the repository root)
"""
import argparse, itertools, os, random, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from finite_fields import FiniteField, factor_xn_minus_lambda
from rr_enumerator import trace_dp_global


def orbit_data(K, factors, k):
    tau = {}
    for i, f in enumerate(factors):
        rec = K.reciprocal_sigma_inv(f, k)
        tau[i] = factors.index(rec)
    seen, cycles = set(), []
    for i in range(len(factors)):
        if i not in seen:
            cyc, j = [], i
            while j not in seen:
                seen.add(j); cyc.append(j); j = tau[j]
            cycles.append(cyc)
    return tau, cycles


def predicted_eta(factors, tau, word, M, m_s):
    return m_s * sum(
        (len(factors[tau[i]]) - 1) * min(word[i], M - word[tau[i]])
        for i in range(len(factors))
    )


def check_family(label, K, n_prime, lambda0, M, k, m_s=1, sample=None, seed=2026):
    n = n_prime * M
    factors = factor_xn_minus_lambda(K, n_prime, lambda0)
    tau, cycles = orbit_data(K, factors, k)
    orbits = sorted((len(c), m_s * (len(factors[c[0]]) - 1)) for c in cycles)
    F = len(factors)
    if sample is None:
        words = itertools.product(range(M + 1), repeat=F)
        total_words = (M + 1) ** F
    else:
        rng = random.Random(seed)
        words = [tuple(rng.randrange(M + 1) for _ in range(F)) for _ in range(sample)]
        total_words = sample

    hist = defaultdict(int)
    for word in words:
        g = [K.one]
        for f, e in zip(factors, word):
            for _ in range(e):
                g = K.poly_mul(g, f)
        kappa = m_s * (n - (len(g) - 1))
        eta_direct = m_s * K.direct_hull_dim(g, n, k)
        eta_pred = predicted_eta(factors, tau, word, M, m_s)
        assert eta_direct == eta_pred, f"{label}: word={word}, direct={eta_direct}, predicted={eta_pred}"
        hist[(kappa, eta_direct)] += 1

    if sample is None:
        expected = trace_dp_global(orbits, M)
        assert dict(hist) == expected, f"{label}: joint histogram mismatch"
        print(f"[PASS exhaustive] {label}: words={total_words}, orbits={orbits}, joint terms={len(hist)}")
    else:
        print(f"[PASS sample]     {label}: sampled words={total_words}, orbits={orbits}")
    return dict(hist), orbits


def verify_repeated_root_quotient_algebra(F4, F16, sample=40, seed=20261023):
    """
    Direct verification in the raw polynomial-quotient basis {1, X, X^2} over F_4
    for A = F_4[X] / <X(X^2 + X + omega)> ~= F_4 x F_16 at repeated-root length
    n = 10 (n' = 5, M = 2), k = 1, testing BOTH:
      (a) non-identity compatible twist lambda_0(X) with CRT image (omega, 1),
          so lambda(X) = lambda_0(X)^2 = (omega^2, 1) in A^*;
      (b) mixed compatible/incompatible twist lambda_0(X) with CRT image (omega, beta),
          where component 1 (F_4) is compatible and component 2 (F_16) is incompatible!
    """
    # Identify omega in F4 with beta^2 + beta in F16 (where beta^4 + beta + 1 = 0):
    beta = F16.gen
    omega4 = F4.gen
    omega16 = beta * beta + beta  # satisfies omega16^2 + omega16 + 1 == 0 in F16
    assert omega16 * omega16 + omega16 + F16.one == F16.zero

    def f4_to_f16(a):
        # a = c0 + c1 * omega4
        c0 = F16.one if a.c[0] else F16.zero
        c1 = F16.one if (len(a.c) > 1 and a.c[1]) else F16.zero
        return c0 + c1 * omega16

    # Build lookup map F16 -> (c0, c1) in F4^2 such that elem = f4_to_f16(c0) + f4_to_f16(c1)*beta
    decomp_f16 = {}
    for c0 in F4.elements:
        for c1 in F4.elements:
            val = f4_to_f16(c0) + f4_to_f16(c1) * beta
            decomp_f16[val] = (c0, c1)
    assert len(decomp_f16) == 16

    inv_omega4 = omega4.inv()

    def crt_to_A(a1, a2):
        # Returns (u0, u1, u2) in F4^3 for u0 + u1*X + u2*X^2 mod X(X^2 + X + omega4)
        diff = a2 - f4_to_f16(a1)
        c0, c1 = decomp_f16[diff]
        u2 = inv_omega4 * c0
        u1 = c1 + u2
        return (a1, u1, u2)

    # Ring multiplication in A = F4[X] / <X^3 + X^2 + omega4 * X>:
    # X^3 = X^2 + omega4 * X, X^4 = (1 + omega4)*X^2 + omega4*X = omega4^2 * X^2 + omega4 * X
    def mul_A(u, v):
        p = [F4.zero] * 5
        for i in range(3):
            for j in range(3):
                p[i + j] = p[i + j] + u[i] * v[j]
        # Reduce degree 4 and 3 using X^3 = X^2 + omega4 * X
        for deg in (4, 3):
            if not p[deg].is_zero():
                c = p[deg]
                p[deg - 1] = p[deg - 1] + c
                p[deg - 2] = p[deg - 2] + omega4 * c
                p[deg] = F4.zero
        return (p[0], p[1], p[2])

    def add_A(u, v):
        return (u[0] + v[0], u[1] + v[1], u[2] + v[2])

    def sq_A(u):
        # Intrinsic Frobenius Z -> Z^2 on A applies sigma_{s,1}(x) = x^2 on BOTH components!
        return mul_A(u, u)

    n_prime, M, n, k = 5, 2, 10, 1
    rng = random.Random(seed)

    # Case (a): Compatible twist lambda_0 = (omega4, 1), lambda = (omega4^2, 1)
    lam_comp = crt_to_A(omega4 * omega4, F16.one)
    fac1 = factor_xn_minus_lambda(F4, n_prime, omega4)
    tau1, _ = orbit_data(F4, fac1, k)
    fac2 = factor_xn_minus_lambda(F16, n_prime, F16.one)
    tau2, _ = orbit_data(F16, fac2, k)

    # Case (b): Mixed compatible/incompatible twist lambda_0 = (omega4, beta), lambda = (omega4^2, beta^2)
    lam_mix = crt_to_A(omega4 * omega4, beta * beta)
    fac2_inc = factor_xn_minus_lambda(F16, n_prime, beta)

    def hull_dim_in_F4_30(g1, g2, lam_A):
        # Lift monic/padded polynomials g1 in F4[x], g2 in F16[x] to G(x) in A[x]
        L = max(len(g1), len(g2))
        G_A = [
            crt_to_A(
                g1[i] if i < len(g1) else F4.zero,
                g2[i] if i < len(g2) else F16.zero,
            )
            for i in range(L)
        ]
        # Span C over F4 inside A^n ~= F4^{3n} by multiplying x^t * X^r * G_A(x) mod (x^n - lam_A)
        basis_X = [(F4.one, F4.zero, F4.zero), (F4.zero, F4.one, F4.zero), (F4.zero, F4.zero, F4.one)]
        cand_rows = []
        # Reduce G_A(x) modulo (x^n - lam_A) into a length-n vector in A^n:
        cur = [(F4.zero, F4.zero, F4.zero)] * n
        for idx_c in range(L - 1, -1, -1):
            last = cur[-1]
            cur = [add_A(G_A[idx_c], mul_A(lam_A, last))] + cur[:-1]
        for _ in range(n):
            for xb in basis_X:
                row = []
                for i in range(n):
                    prod = mul_A(xb, cur[i])
                    row.extend(prod)
                cand_rows.append(row)
            # Multiply cur by x mod (x^n - lam_A)
            last = cur[-1]
            cur = [mul_A(lam_A, last)] + cur[:-1]

        # Extract independent rows of C in F4^{3n}
        indep_C = []
        rref = []
        pivs = []
        for row in cand_rows:
            v = list(row)
            for pr, pc in zip(rref, pivs):
                if not v[pc].is_zero():
                    fac = v[pc]
                    for col in range(pc, 3 * n):
                        v[col] = v[col] - fac * pr[col]
            pc_new = next((col for col in range(3 * n) if not v[col].is_zero()), None)
            if pc_new is not None:
                inv_v = v[pc_new].inv()
                v = [x * inv_v for x in v]
                rref.append(v)
                pivs.append(pc_new)
                indep_C.append(row)

        dim_C = len(indep_C)
        if dim_C == 0:
            return 0, 0

        # Direct computation of dim_{F4}(C cap D_{A,1}(C)):
        # A codeword c = sum_{r=0}^{dim_C-1} alpha_r * indep_C[r] (alpha_r in F4) lies in D_{A,1}(C)
        # iff for EVERY generator indep_C[j] and EVERY component coordinate,
        # sum_{i=0}^{n-1} indep_C[j][i] * sq_A(c[i]) == (0, 0, 0) in A!
        # Wait: squaring sq_A is F4-semilinear (since alpha^2 for alpha in F4), so apply inverse
        # Frobenius alpha_r = beta_r^2 (a bijection on F4!): then sq_A(c[i]) is F4-LINEAR in beta_r!
        eq_cols = []  # build constraints matrix of shape (#constraints) x dim_C over F4
        # Each r in 0..dim_C-1 has c^{(r)} = indep_C[r]; sq_A applied to each A-slot of c^{(r)}:
        c_sq = []
        for r in range(dim_C):
            c_sq.append([sq_A(indep_C[r][3 * i : 3 * i + 3]) for i in range(n)])
        constraints = []
        for j in range(dim_C):
            row_j = [indep_C[j][3 * i : 3 * i + 3] for i in range(n)]
            # Three F4-coordinates of sum_i row_j[i] * c_sq[r][i] in A:
            for comp_idx in range(3):
                eq_row = []
                for r in range(dim_C):
                    acc = (F4.zero, F4.zero, F4.zero)
                    for i in range(n):
                        acc = add_A(acc, mul_A(row_j[i], c_sq[r][i]))
                    eq_row.append(acc[comp_idx])
                constraints.append(eq_row)
        rk = F4.matrix_rank(constraints, dim_C)
        return dim_C, dim_C - rk

    for _ in range(sample):
        w1 = [rng.randrange(M + 1) for _ in range(len(fac1))]
        w2 = [rng.randrange(M + 1) for _ in range(len(fac2))]
        g1 = [F4.one]
        for f, e in zip(fac1, w1):
            for _ in range(e):
                g1 = F4.poly_mul(g1, f)
        g2 = [F16.one]
        for f, e in zip(fac2, w2):
            for _ in range(e):
                g2 = F16.poly_mul(g2, f)
        kap_raw, eta_raw = hull_dim_in_F4_30(g1, g2, lam_comp)
        kap_exp = (n - (len(g1) - 1)) + 2 * (n - (len(g2) - 1))
        eta_exp = predicted_eta(fac1, tau1, w1, M, 1) + predicted_eta(fac2, tau2, w2, M, 2)
        assert (kap_raw, eta_raw) == (kap_exp, eta_exp)

        # Also check mixed compatible+incompatible twist in raw F4^{30}:
        w2_inc = [rng.randrange(M + 1) for _ in range(len(fac2_inc))]
        g2_inc = [F16.one]
        for f, e in zip(fac2_inc, w2_inc):
            for _ in range(e):
                g2_inc = F16.poly_mul(g2_inc, f)
        kap_m, eta_m = hull_dim_in_F4_30(g1, g2_inc, lam_mix)
        kap_m_exp = (n - (len(g1) - 1)) + 2 * (n - (len(g2_inc) - 1))
        eta_m_exp = predicted_eta(fac1, tau1, w1, M, 1) + 0
        assert (kap_m, eta_m) == (kap_m_exp, eta_m_exp)

    print(f"[PASS quotient-ring F4[X]/<X(X^2+X+omega)> in F4^30] {sample} compatible + {sample} mixed-twist repeated-root codes verified directly!")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--quick', action='store_true', help='skip the slowest exhaustive family (F8, n=14)')
    args = ap.parse_args()

    F3 = FiniteField(3, [1, 1])
    F4 = FiniteField(2, [1, 1, 1])
    F8 = FiniteField(2, [1, 1, 0, 1])
    F9 = FiniteField(3, [1, 0, 1])       # x^2 + 1, gen = i
    F16 = FiniteField(2, [1, 1, 0, 0, 1])
    F25 = FiniteField(5, [2, 0, 1])      # x^2 + 2
    F32 = FiniteField(2, [1, 0, 1, 0, 0, 1])

    check_family('F4, n=10 (n\'=5,M=2), lambda=1, k=1', F4, 5, F4.one, 2, 1)
    check_family('F4, n=10 (n\'=5,M=2), lambda0=omega, k=1', F4, 5, F4.gen, 2, 1)
    check_family('F3, n=12 (n\'=4,M=3), lambda=1, k=0', F3, 4, F3.one, 3, 0)
    check_family('F9, n=12 (n\'=4,M=3), lambda0=i, k=1', F9, 4, F9.gen, 3, 1)
    check_family('F9, n=12 (n\'=4,M=3), lambda0=-1, k=1', F9, 4, -F9.one, 3, 1)
    if not args.quick:
        check_family('F8, n=14 (n\'=7,M=2), lambda=1, k=1', F8, 7, F8.one, 2, 1)

    # Mixed algebra F4 x F16 over F4, n=10, lambda=(1,1): componentwise product.
    h1, o1 = check_family('F4 component, n=10, lambda=1, k=1', F4, 5, F4.one, 2, 1, m_s=1)
    h2, o2 = check_family('F16/F4 component, n=10, lambda=1, k=1', F16, 5, F16.one, 2, 1, m_s=2)
    combined = defaultdict(int)
    for (k1, e1), v1 in h1.items():
        for (k2, e2), v2 in h2.items():
            combined[(k1 + k2, e1 + e2)] += v1 * v2
    assert dict(combined) == trace_dp_global(o1 + o2, 2)
    print(f"[PASS exhaustive] F4 x F16, n=10: orbits={o1 + o2}, joint terms={len(combined)}")

    # Higher-degree factor families testing general Cantor-Zassenhaus factorisation:
    check_family('F4, n=14 (n\'=7,M=2), lambda=1, k=1 [deg-3 cubics]', F4, 7, F4.one, 2, 1)
    check_family('F3, n=24 (n\'=8,M=3), lambda0=-1, k=0 [deg-4 quartics]', F3, 8, -F3.one, 3, 0)

    # Larger families: seeded random exponent words, checked one code at a time.
    check_family('F9, n=24 (n\'=8,M=3), lambda=1, k=1', F9, 8, F9.one, 3, 1, sample=60)
    check_family('F25, n=30 (n\'=6,M=5), lambda=1, k=1', F25, 6, F25.one, 5, 1, sample=60)
    check_family('F32, n=62 (n\'=31,M=2), lambda=1, k=1', F32, 31, F32.one, 2, 1, sample=12)

    # Direct quotient-basis {1, X, X^2} verification over A = F4[X]/<X(X^2 + X + omega)>
    # in F4^{30} at repeated-root length n = 10 (n' = 5, M = 2), k = 1:
    verify_repeated_root_quotient_algebra(F4, F16, sample=40, seed=20261023)
    print('ALL DIRECT FINITE-FIELD CHECKS PASSED')


if __name__ == '__main__':
    main()
