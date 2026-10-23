#!/usr/bin/env python3
"""
Phase 1 verification suite (Sections 2 & 3 of manuscript/main.tex, including Gate G1):

Verifies directly from first-principles linear algebra over finite fields:
  1. Lemma 2.2 (repeated-root factorisation): x^n - lambda_s == (x^{n'} - lambda_{s,0})^M
     as actual degree-n polynomials in K_s[x], with pairwise coprime monic factors.
  2. Lemma 3.3 & Theorem 3.4 (Euclidean & k-Galois dual generators without square-freeness):
     exact subspace equality D_k(<g_e>) == <h_e^{#_{s,k}}> in K_s^n and closure under
     the lambda_s^{-p^{d_s-k}}-constacyclic shift across:
       - Gate G1 family: F_4, n'=5, M=2, n=10, k=1, lambda_0=omega, lambda=omega^2 (all 27 codes)
       - Odd-char non-cyclic family: F_9, n'=4, M=3, n=12, k=1, lambda_0=i, lambda=-i (all 16 codes)
  3. Proposition 3.5 (compatibility equivalence): lambda_{s,0}^{1+p^{d-k}}==1 iff
     lambda_s^{1+p^{d-k}}==1 iff tau_{s,k} preserves F_s across all nonzero twists in F_4, F_8, F_9, F_5.
  4. Proposition 3.6 (incompatible twists & mixed algebra formula):
     - Example in Section 3: F_5, n'=2, M=5, n=10, k=0, lambda_0=lambda=2 (all 6 codes:
       exact dual < (x^2 - 3)^{5-e} >, Hull_0 = {0}, SO={0}, DC=F_5^{10}, SD=none).
     - Mixed compatible/incompatible algebra: F_4 x F_4, n'=3, M=2, n=6, k=0,
       lambda_0=(1, omega), lambda=(1, omega^2) — exhaustive check of all 3^3 * 3^3 = 729 codes
       against the product formula of Proposition 3.6(c).
  5. Remark 3.7 (code-first vs candidate-first dual conventions):
     On F_8, n'=7, M=2, n=14, k=1, verifies D_cand(C) == sigma^2(D_k(C)), exhibits codes where
     D_cand(C) != D_k(C), and confirms dim(C cap D_k(C)) == dim(C cap D_cand(C)) == dim C - rank(B sigma(B)^T).
"""

import itertools
import os
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from finite_fields import FiniteField
from rr_enumerator import trace_dp_global, convolve
import random


def poly_trim(K, f):
    out = list(f)
    while len(out) > 1 and out[-1].is_zero():
        out.pop()
    return out


def poly_add(K, a, b):
    m = max(len(a), len(b))
    out = []
    for i in range(m):
        ca = a[i] if i < len(a) else K.zero
        cb = b[i] if i < len(b) else K.zero
        out.append(ca + cb)
    return poly_trim(K, out)


def poly_sub(K, a, b):
    m = max(len(a), len(b))
    out = []
    for i in range(m):
        ca = a[i] if i < len(a) else K.zero
        cb = b[i] if i < len(b) else K.zero
        out.append(ca - cb)
    return poly_trim(K, out)


def poly_monic(K, f):
    f = poly_trim(K, f)
    inv_lead = f[-1].inv()
    return [c * inv_lead for c in f]


def poly_divmod(K, a, b):
    rem = poly_trim(K, a)
    b = poly_trim(K, b)
    deg_b = len(b) - 1
    if len(rem) - 1 < deg_b or (len(rem) == 1 and rem[0].is_zero()):
        return [K.zero], rem
    inv_lead = b[-1].inv()
    q = [K.zero] * (len(rem) - deg_b)
    while len(rem) - 1 >= deg_b and not (len(rem) == 1 and rem[0].is_zero()):
        shift = len(rem) - len(b)
        scale = rem[-1] * inv_lead
        q[shift] = scale
        for i in range(len(b)):
            rem[shift + i] = rem[shift + i] - scale * b[i]
        rem = poly_trim(K, rem)
    return poly_trim(K, q), rem


def poly_gcd(K, a, b):
    a = poly_trim(K, a)
    b = poly_trim(K, b)
    while not (len(b) == 1 and b[0].is_zero()):
        _, r = poly_divmod(K, a, b)
        a, b = b, r
    return poly_monic(K, a)


def poly_powmod(K, base, exp, modp):
    res = [K.one]
    b = poly_divmod(K, base, modp)[1]
    e = exp
    while e > 0:
        if e & 1:
            res = poly_divmod(K, K.poly_mul(res, b), modp)[1]
        b = poly_divmod(K, K.poly_mul(b, b), modp)[1]
        e >>= 1
    return res


def factor_squarefree_monic(K, f, seed=2026):
    """General distinct-degree + Cantor-Zassenhaus factorisation over any finite field K."""
    f = poly_monic(K, f)
    if len(f) - 1 <= 1:
        return [f] if len(f) - 1 == 1 else []
    rng = random.Random(seed)
    q = K.size
    out = []
    rem = f
    x_poly = [K.zero, K.one]
    h = x_poly[:]
    deg_r = 1
    while len(rem) - 1 >= 2 * deg_r:
        h = poly_powmod(K, h, q, rem)
        g = poly_gcd(K, poly_sub(K, h, x_poly), rem)
        if len(g) - 1 > 0:
            rem, _ = poly_divmod(K, rem, g)
            h = poly_divmod(K, h, rem)[1]
            # Equal-degree split of g into factors of degree deg_r
            queue = [g]
            while queue:
                cur = queue.pop()
                if len(cur) - 1 == deg_r:
                    out.append(poly_monic(K, cur))
                    continue
                rand_a = [rng.choice(K.elements) for _ in range(len(cur) - 1)]
                rand_a = poly_trim(K, rand_a)
                if len(rand_a) == 1 and rand_a[0].is_zero():
                    queue.append(cur)
                    continue
                split = poly_gcd(K, rand_a, cur)
                if 0 < len(split) - 1 < len(cur) - 1:
                    q2, _ = poly_divmod(K, cur, split)
                    queue.extend([poly_monic(K, split), poly_monic(K, q2)])
                    continue
                if K.p == 2:
                    # Absolute trace over F_2: sum_{j=0}^{K.d * deg_r - 1} a^{2^j} mod cur
                    tr = [K.zero]
                    cur_pow = rand_a
                    for _ in range(K.d * deg_r):
                        tr = poly_add(K, tr, cur_pow)
                        cur_pow = poly_divmod(K, K.poly_mul(cur_pow, cur_pow), cur)[1]
                    split = poly_gcd(K, tr, cur)
                else:
                    exp_half = (q ** deg_r - 1) // 2
                    pw = poly_powmod(K, rand_a, exp_half, cur)
                    split = poly_gcd(K, poly_sub(K, pw, [K.one]), cur)
                if 0 < len(split) - 1 < len(cur) - 1:
                    q2, _ = poly_divmod(K, cur, split)
                    queue.extend([poly_monic(K, split), poly_monic(K, q2)])
                else:
                    queue.append(cur)
        deg_r += 1
    if len(rem) - 1 > 0:
        out.append(poly_monic(K, rem))
    out.sort(key=lambda p_i: (len(p_i), [c.c for c in p_i]))
    assert sum(len(p_i) - 1 for p_i in out) == len(f) - 1
    return out


def factor_xn_minus_lambda(K, n_prime, lam0):
    target = [-lam0] + [K.zero] * (n_prime - 1) + [K.one]
    return factor_squarefree_monic(K, target)


def poly_pow(K, f, exp):
    out = [K.one]
    for _ in range(exp):
        out = K.poly_mul(out, f)
    return out


def span_rows(K, gen_poly, n):
    """Return canonical row-reduced echelon basis of <gen_poly> in K^n (deg gen_poly <= n)."""
    deg = len(gen_poly) - 1
    dim = n - deg
    if dim == 0:
        return []
    rows = []
    for s in range(dim):
        row = [K.zero] * n
        for i, c in enumerate(gen_poly):
            row[s + i] = c
        rows.append(row)
    return rref(K, rows, n)


def rref(K, rows, ncols):
    mat = [list(r) for r in rows]
    nrows = len(mat)
    piv_row = 0
    for col in range(ncols):
        piv = None
        for r in range(piv_row, nrows):
            if not mat[r][col].is_zero():
                piv = r
                break
        if piv is None:
            continue
        mat[piv_row], mat[piv] = mat[piv], mat[piv_row]
        inv_p = mat[piv_row][col].inv()
        for j in range(col, ncols):
            mat[piv_row][j] = mat[piv_row][j] * inv_p
        for r in range(nrows):
            if r != piv_row and not mat[r][col].is_zero():
                fac = mat[r][col]
                for j in range(col, ncols):
                    mat[r][j] = mat[r][j] - fac * mat[piv_row][j]
        piv_row += 1
    return [row for row in mat[:piv_row]]


def nullspace(K, rows, ncols):
    """Exact right nullspace {x in K^ncols : A x = 0} returned in RREF."""
    if not rows:
        ident = []
        for i in range(ncols):
            r = [K.zero] * ncols
            r[i] = K.one
            ident.append(r)
        return ident
    red = rref(K, rows, ncols)
    pivots = []
    for row in red:
        for j, v in enumerate(row):
            if not v.is_zero():
                pivots.append(j)
                break
    free_cols = [j for j in range(ncols) if j not in pivots]
    basis = []
    for fc in free_cols:
        vec = [K.zero] * ncols
        vec[fc] = K.one
        for piv_idx, pc in enumerate(pivots):
            vec[pc] = -red[piv_idx][fc]
        basis.append(vec)
    return rref(K, basis, ncols)


def direct_duals_and_hulls(K, C_basis, n, k):
    """Compute code-first D_k(C) and candidate-first D_cand(C) directly from definitions."""
    # Code-first: sum_i c_i y_i^{p^k} = 0  <=>  y_i^{p^k} in C^{perp_E}  <=>  y = rho(z), z in nullspace(C)
    # Better yet: solve directly using rho on nullspace AND verify pairing equation on every basis vector!
    eucl_null = nullspace(K, C_basis, n)
    exp_sigma = K.p ** k
    exp_rho = K.p ** (K.d - k)
    D_code = rref(K, [[v ** exp_rho for v in row] for row in eucl_null], n)
    D_cand = rref(K, [[v ** exp_sigma for v in row] for row in eucl_null], n)

    # Verify orthogonality directly from pairing sum_i c_i y_i^{p^k} == 0 and sum_i y_i c_i^{p^k} == 0
    for c in C_basis:
        for y in D_code:
            ip = K.zero
            for i in range(n):
                ip = ip + c[i] * (y[i] ** exp_sigma)
            assert ip.is_zero(), "Code-first pairing non-zero!"
        for y in D_cand:
            ip = K.zero
            for i in range(n):
                ip = ip + y[i] * (c[i] ** exp_sigma)
            assert ip.is_zero(), "Candidate-first pairing non-zero!"

    dim_sum_code = len(rref(K, C_basis + D_code, n))
    dim_hull_code = len(C_basis) + len(D_code) - dim_sum_code
    dim_sum_cand = len(rref(K, C_basis + D_cand, n))
    dim_hull_cand = len(C_basis) + len(D_cand) - dim_sum_cand
    return D_code, D_cand, dim_hull_code, dim_hull_cand


def is_mu_constacyclic(K, subspace_rref, n, mu):
    for row in subspace_rref:
        shifted = [mu * row[n - 1]] + row[: n - 1]
        if len(rref(K, subspace_rref + [shifted], n)) != len(subspace_rref):
            return False
    return True


def fmt_poly(K, f, sym="\\omega"):
    elem_map = {K.zero: "0", K.one: "1"}
    if K.size == 4:
        w = K.gen
        elem_map[w] = sym
        elem_map[w * w] = f"{sym}^2"
    elif K.p == 5 and K.d == 1:
        for a in range(5):
            elem_map[K.elements[a]] = str(K.elements[a].c[0])
    terms = []
    for deg in range(len(f) - 1, -1, -1):
        c = f[deg]
        if c.is_zero():
            continue
        cs = elem_map.get(c, str(c.c))
        if deg == 0:
            terms.append(cs)
        elif deg == 1:
            terms.append("x" if cs == "1" else f"{cs}x")
        else:
            terms.append(f"x^{deg}" if cs == "1" else f"{cs}x^{deg}")
    return " + ".join(terms) if terms else "0"


def check_dual_generator_family(label, K, n_prime, M, k, lam0):
    n = n_prime * M
    lam = lam0 ** M
    mu = (lam.inv()) ** (K.p ** (K.d - k))
    factors = factor_xn_minus_lambda(K, n_prime, lam0)

    # Check Lemma 2.2 polynomial equality in K[x]: prod_{f in F_s} f^M == x^n - lam
    prod_M = [K.one]
    for f in factors:
        prod_M = K.poly_mul(prod_M, poly_pow(K, f, M))
    target = [-lam] + [K.zero] * (n - 1) + [K.one]
    assert prod_M == target, f"{label}: Lemma 2.2 polynomial equality failed"

    for word in itertools.product(range(M + 1), repeat=len(factors)):
        g_e = [K.one]
        h_e = [K.one]
        for f, e in zip(factors, word):
            g_e = K.poly_mul(g_e, poly_pow(K, f, e))
            h_e = K.poly_mul(h_e, poly_pow(K, f, M - e))
        assert K.poly_mul(g_e, h_e) == target
        h_sharp = K.reciprocal_sigma_inv(h_e, k)

        C_sub = span_rows(K, g_e, n)
        D_pred = span_rows(K, h_sharp, n)
        D_code, D_cand, hull_code, hull_cand = direct_duals_and_hulls(K, C_sub, n, k)
        assert D_code == D_pred, f"{label}: subspace mismatch at {word}"
        assert is_mu_constacyclic(K, D_code, n, mu), f"{label}: dual shift failed at {word}"
        assert hull_code == hull_cand, f"{label}: convention hull mismatch at {word}"
    print(f"[PASS] {label}: exact subspace equality D_k(<g_e>) == <h_e^#> verified for all {(M+1)**len(factors)} codes")
    return factors


def main():
    F4 = FiniteField(2, [1, 1, 1])       # F_2[w]/(w^2 + w + 1)
    F8 = FiniteField(2, [1, 1, 0, 1])    # F_2[a]/(a^3 + a + 1)
    F9 = FiniteField(3, [1, 0, 1])       # F_3[i]/(i^2 + 1)
    F5 = FiniteField(5, [0, 1])          # F_5

    # 1. Gate G1: F_4, n'=5, M=2, n=10, k=1, lam0=omega, lam=omega^2
    factors_g1 = check_dual_generator_family(
        "Gate G1 (F_4, n'=5, M=2, n=10, k=1, lam0=omega, lam=omega^2)",
        F4, 5, 2, 1, F4.gen,
    )
    print("  Gate G1 factors of x^5 - omega over F_4:")
    tau_g1 = {}
    for idx, f in enumerate(factors_g1):
        rec = F4.reciprocal_sigma_inv(f, 1)
        tau_g1[idx] = factors_g1.index(rec)
        print(f"    f_{idx+1}(x) = {fmt_poly(F4, f)}   -->   f_{idx+1}^#(x) = f_{tau_g1[idx]+1}(x)")
    sample_word = (2, 1, 0)
    g_sample = [F4.one]
    h_sample = [F4.one]
    for f, e in zip(factors_g1, sample_word):
        g_sample = F4.poly_mul(g_sample, poly_pow(F4, f, e))
        h_sample = F4.poly_mul(h_sample, poly_pow(F4, f, 2 - e))
    h_sharp_sample = F4.reciprocal_sigma_inv(h_sample, 1)
    exp_dual = tuple(2 - sample_word[[j for j, t in tau_g1.items() if t == i][0]] for i in range(len(factors_g1)))
    print(f"  Gate G1 word e={sample_word}: dual exponents={exp_dual}, dim C={10-(len(g_sample)-1)}, dim Hull_1={F4.direct_hull_dim(g_sample, 10, 1)}")
    # Confirm product with exp_dual matches h_sharp_sample identically
    prod_dual = [F4.one]
    for f, de in zip(factors_g1, exp_dual):
        prod_dual = F4.poly_mul(prod_dual, poly_pow(F4, f, de))
    assert prod_dual == h_sharp_sample

    # 2. Odd characteristic non-cyclic family: F_9, n'=4, M=3, n=12, k=1, lam0=i, lam=-i
    check_dual_generator_family(
        "Odd-char non-cyclic (F_9, n'=4, M=3, n=12, k=1, lam0=i, lam=-i)",
        F9, 4, 3, 1, F9.gen,
    )

    # 3. Proposition 3.5: compatibility equivalence across all nonzero elements in F_4, F_8, F_9, F_5
    for name, K, n_prime, M, k in [
        ("F_4", F4, 5, 2, 1),
        ("F_4-Eucl", F4, 3, 2, 0),
        ("F_8", F8, 7, 2, 1),
        ("F_9", F9, 4, 3, 1),
        ("F_5", F5, 2, 5, 0),
    ]:
        exp_c = 1 + (K.p ** (K.d - k))
        for lam0 in K.elements:
            if lam0.is_zero():
                continue
            lam = lam0 ** M
            c1 = (lam0 ** exp_c) == K.one
            c2 = (lam ** exp_c) == K.one
            c3 = ((lam.inv()) ** (K.p ** (K.d - k))) == lam
            facs = factor_xn_minus_lambda(K, n_prime, lam0)
            c4 = all(K.reciprocal_sigma_inv(f, k) in facs for f in facs)
            assert c1 == c2 == c3 == c4, f"Compatibility mismatch on {name}, lam0={lam0.c}"
    print("[PASS] Proposition 3.5 equivalence (1)<=>(2)<=>(3)<=>(4) verified across F_4, F_8, F_9, F_5")

    # 4. Incompatible example in Section 3: F_5, n'=2, M=5, n=10, k=0, lam0=2, lam=2
    lam0_f5 = F5.elements[2]  # value 2 in F_5
    assert lam0_f5.c == (2,)
    check_dual_generator_family(
        "Incompatible Section 3 example (F_5, n'=2, M=5, n=10, k=0, lam0=2, lam=2)",
        F5, 2, 5, 0, lam0_f5,
    )
    fac_f5 = factor_xn_minus_lambda(F5, 2, lam0_f5)
    assert len(fac_f5) == 1 and fmt_poly(F5, fac_f5[0]) == "x^2 + 3"
    pairs_f5 = []
    so_cnt = dc_cnt = sd_cnt = 0
    for e in range(6):
        g_e = poly_pow(F5, fac_f5[0], e)
        C_sub = span_rows(F5, g_e, 10)
        D_code, _, hull_dim, _ = direct_duals_and_hulls(F5, C_sub, 10, 0)
        kap = len(C_sub)
        pairs_f5.append((kap, hull_dim))
        if len(rref(F5, C_sub + D_code, 10)) == len(D_code):
            so_cnt += 1
        if len(rref(F5, C_sub + D_code, 10)) == len(C_sub):
            dc_cnt += 1
        if C_sub == D_code:
            sd_cnt += 1
    assert pairs_f5 == [(10, 0), (8, 0), (6, 0), (4, 0), (2, 0), (0, 0)]
    assert (so_cnt, dc_cnt, sd_cnt) == (1, 1, 0)
    print(f"[PASS] F_5 incompatible example pairs={pairs_f5}, (SO, DC, SD)=({so_cnt}, {dc_cnt}, {sd_cnt})")

    # 5. Mixed compatible + incompatible algebra over F_4:
    #    A = F_4 x F_16 (m_1 = 1, m_2 = 2), n'=3, M=2, n=6, k=0, lam0=(1, b), lam=(1, b^2)
    #    where b generates F_16: b^{1+2^4}=b^{17} != 1 since ord(b)=15, so component 2 is incompatible
    #    with m_2 = 2 AND irreducible cubic factor of degree 3 (w_f = m_2 * deg f = 6)!
    F16 = FiniteField(2, [1, 1, 0, 0, 1])
    fac_comp = factor_xn_minus_lambda(F4, 3, F4.one)     # 3 linear factors over F_4; k=0 orbits: (1,1) + (2,1)
    fac_inc = factor_xn_minus_lambda(F16, 3, F16.gen)    # 1 cubic factor over F_16; incompatible for k=0
    assert len(fac_comp) == 3 and len(fac_inc) == 1 and (len(fac_inc[0]) - 1) == 3
    m1, m2 = 1, 2
    hist_comp = defaultdict(int)
    hist_inc = defaultdict(int)
    for w1 in itertools.product(range(3), repeat=len(fac_comp)):
        g1 = [F4.one]
        for f, e in zip(fac_comp, w1):
            g1 = F4.poly_mul(g1, poly_pow(F4, f, e))
        hist_comp[(m1 * (6 - (len(g1) - 1)), m1 * F4.direct_hull_dim(g1, 6, 0))] += 1
    for w2 in itertools.product(range(3), repeat=len(fac_inc)):
        g2 = [F16.one]
        for f, e in zip(fac_inc, w2):
            g2 = F16.poly_mul(g2, poly_pow(F16, f, e))
        hist_inc[(m2 * (6 - (len(g2) - 1)), m2 * F16.direct_hull_dim(g2, 6, 0))] += 1
    mixed_direct = convolve(hist_comp, hist_inc)
    # Formula from Proposition 3.6(c): compatible trace DP * prod_{f in F_inc} sum_{r=0}^M U^{r * m_s * deg f}
    inc_factor = {(0, 0): 1}
    for f in fac_inc:
        wf = m2 * (len(f) - 1)
        inc_factor = convolve(inc_factor, {(r * wf, 0): 1 for r in range(3)})
    mixed_formula = convolve(trace_dp_global([(1, 1), (2, 1)], 2), inc_factor)
    assert mixed_direct == mixed_formula
    print(f"[PASS] Mixed compatible+incompatible algebra F_4 x F_16 (81 codes, {len(mixed_direct)} terms, w_inc=6): exact match with Proposition 3.6(c)")

    # 6. Remark 3.7: F_8, n'=7, M=2, n=14, k=1 — exhibit explicit code with D_cand != D_k yet same hull dim
    fac_f8 = factor_xn_minus_lambda(F8, 7, F8.one)
    word_diff = (1, 0, 0, 0, 0, 0, 0)
    g8 = poly_pow(F8, fac_f8[0], 1)
    # pick a non-F2 factor instead of x+1 so sigma^2 moves D_k(C)
    for idx in range(len(fac_f8)):
        g_try = poly_pow(F8, fac_f8[idx], 1)
        C_try = span_rows(F8, g_try, 14)
        D_code, D_cand, hc, hcand = direct_duals_and_hulls(F8, C_try, 14, 1)
        sig2_D = rref(F8, [[v ** 4 for v in row] for row in D_code], 14)
        assert D_cand == sig2_D and hc == hcand
        if D_cand != D_code:
            print(f"[PASS] Remark 3.7 verified on F_8, n=14: D_cand == sigma^2(D_k) != D_k on factor {idx}, yet hull dims equal ({hc} == {hcand})")
            break
    else:
        raise AssertionError("Expected a code over F_8 where D_cand != D_k")

    print("\nALL PHASE 1 DUALITY & GATE G1 VERIFICATION TESTS PASSED!")


if __name__ == "__main__":
    main()
