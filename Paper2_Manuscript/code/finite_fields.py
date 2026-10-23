#!/usr/bin/env python3
"""
Exact Finite-Field Arithmetic, Polynomial Factorisation, and Linear-Algebra
Primitives for:
"Joint Code-Dimension and k-Galois-Hull Enumerators for Repeated-Root
Constacyclic Codes over Square-Free Affine Algebras"
Authors: Arun Kumar Yadav, Vipin Gupta, Pooja Soni, Manju Pruthi

Provides:
1. Exact prime-extension finite-field arithmetic F_{p^e} (FiniteField, FieldElement).
2. Arbitrary-degree Distinct-Degree + Cantor-Zassenhaus square-free monic
   polynomial factorisation (factor_squarefree_monic, factor_xn_minus_lambda).
3. Inverse-Frobenius reciprocal polynomials and k-Galois Gram-rank hull
   dimension routines.
"""

import csv
import itertools
import json
import math
import os
import random
from collections import defaultdict
from fractions import Fraction


# =============================================================================
# 1. Exact Orbit Enumerators (Propositions 4.4 and 4.15)
# =============================================================================

def trace_recurrence_enumerator(orbits):
    """
    Compute the exact bivariate polynomial E(u, z) = sum c_{kappa, eta} u^kappa z^eta
    using the two-state transfer-matrix trace recurrence of Proposition 4.15.

    Parameters
    ----------
    orbits : list of (int, int)
        List of (a_O, w_O) pairs where a_O >= 1 is orbit length and w_O >= 1
        is global F_q-weight m_s * d_O.

    Returns
    -------
    dict[(int, int), int]
        Mapping (kappa, eta) -> exact integer coefficient [u^kappa z^eta] E(u, z).
    """
    G = {(0, 0): 1}
    for a, w in orbits:
        next_G = defaultdict(int)
        for s0 in (0, 1):
            state = [defaultdict(int), defaultdict(int)]
            for key, val in G.items():
                state[s0][key] = val
            for _ in range(a):
                new_state = [defaultdict(int), defaultdict(int)]
                for r in (0, 1):
                    if not state[r]:
                        continue
                    for t in (0, 1):
                        dk = w * (1 - t)
                        de = w * r * (1 - t)
                        for (kap, eta), val in state[r].items():
                            new_state[t][(kap + dk, eta + de)] += val
                state = new_state
            for key, val in state[s0].items():
                next_G[key] += val
        G = {k: v for k, v in next_G.items() if v != 0}
    return dict(sorted(G.items()))


def closed_form_one_orbit(a, w):
    """
    Compute the one-orbit polynomial tr(T_w(u, z)^a) via the closed binomial
    formula of Proposition 4.4.
    """
    poly = defaultdict(int)
    poly[(0, 0)] += 1
    poly[(w * a, 0)] += 1
    for j in range(1, a):
        max_r = min(j, a - j)
        for r in range(1, max_r + 1):
            coeff = (a * math.comb(j - 1, r - 1) * math.comb(a - j - 1, r - 1)) // r
            poly[(w * j, w * r)] += coeff
    return dict(poly)


def closed_form_enumerator(orbits):
    """
    Compute E(u, z) by multiplying the closed-form one-orbit polynomials of
    Proposition 4.4 over all orbits.
    """
    G = {(0, 0): 1}
    for a, w in orbits:
        orb_poly = closed_form_one_orbit(a, w)
        next_G = defaultdict(int)
        for (k1, e1), v1 in G.items():
            for (k2, e2), v2 in orb_poly.items():
                next_G[(k1 + k2, e1 + e2)] += v1 * v2
        G = {k: v for k, v in next_G.items() if v != 0}
    return dict(sorted(G.items()))


def theoretical_moments_and_lcd(orbits):
    """
    Compute total codes (Corollary 4.7), LCD codes (Corollary 4.10),
    unconditional mean (Corollary 4.11), and variance (Corollary 4.12)
    directly from the orbit formulas.
    """
    total_codes = 1 << sum(a for a, _ in orbits)
    lcd_codes = 1 << len(orbits)
    mean = sum(Fraction(a * w, 4) for a, w in orbits if a >= 2)
    var = sum(
        Fraction(w * w, 4) if a == 2 else (Fraction(a * w * w, 16) if a >= 3 else Fraction(0))
        for a, w in orbits
    )
    return total_codes, lcd_codes, mean, var


def moments_from_enumerator(E):
    """
    Compute total codes, LCD codes, unconditional mean, and variance from the
    coefficients of E(u, z), together with conditional moments Phi_j(kappa)
    (Corollaries 4.13 and 4.14).
    """
    total = sum(E.values())
    lcd = sum(v for (kap, eta), v in E.items() if eta == 0)
    mean = Fraction(sum(eta * v for (kap, eta), v in E.items()), total)
    second_moment = Fraction(sum(eta * eta * v for (kap, eta), v in E.items()), total)
    var = second_moment - mean * mean

    by_kappa = defaultdict(list)
    for (kap, eta), v in E.items():
        by_kappa[kap].append((eta, v))

    cond = {}
    for kap, items in sorted(by_kappa.items()):
        phi0 = sum(v for _, v in items)
        phi1 = sum(eta * v for eta, v in items)
        phi2 = sum(eta * (eta - 1) * v for eta, v in items)
        c_mean = Fraction(phi1, phi0)
        c_var = Fraction(phi2 + phi1, phi0) - c_mean * c_mean
        cond[kap] = {
            "Phi0": phi0,
            "Phi1": phi1,
            "Phi2": phi2,
            "mean": c_mean,
            "var": c_var,
        }
    return total, lcd, mean, var, cond


# =============================================================================
# 2. Finite-Field Linear-Algebra & Root-Orbit Verification (Section 5.2)
# =============================================================================

class PrimeFieldElement:
    """Element of F_{p^d} represented as a polynomial of degree < d over F_p."""
    def __init__(self, coeffs, p, mod_poly):
        self.p = p
        self.mod_poly = mod_poly  # monic tuple of length d + 1 (low to high)
        self.d = len(mod_poly) - 1
        c = [x % p for x in coeffs]
        while len(c) > self.d:
            if c[-1] != 0:
                lead = c[-1]
                shift = len(c) - 1 - self.d
                for i in range(self.d + 1):
                    c[shift + i] = (c[shift + i] - lead * mod_poly[i]) % p
            c.pop()
        while len(c) < self.d:
            c.append(0)
        self.c = tuple(c)

    def __eq__(self, other):
        return isinstance(other, PrimeFieldElement) and self.c == other.c and self.p == other.p

    def __hash__(self):
        return hash((self.c, self.p))

    def is_zero(self):
        return all(x == 0 for x in self.c)

    def __add__(self, other):
        return PrimeFieldElement([a + b for a, b in zip(self.c, other.c)], self.p, self.mod_poly)

    def __sub__(self, other):
        return PrimeFieldElement([a - b for a, b in zip(self.c, other.c)], self.p, self.mod_poly)

    def __neg__(self):
        return PrimeFieldElement([-a for a in self.c], self.p, self.mod_poly)

    def __mul__(self, other):
        prod = [0] * (2 * self.d - 1)
        for i, a in enumerate(self.c):
            if a:
                for j, b in enumerate(other.c):
                    prod[i + j] = (prod[i + j] + a * b) % self.p
        return PrimeFieldElement(prod, self.p, self.mod_poly)

    def __pow__(self, exp):
        res = PrimeFieldElement([1], self.p, self.mod_poly)
        base = self
        e = exp
        while e > 0:
            if e & 1:
                res = res * base
            base = base * base
            e >>= 1
        return res

    def inv(self):
        if self.is_zero():
            raise ZeroDivisionError("Zero element has no inverse")
        return self ** (self.p ** self.d - 2)


class FiniteField:
    """Finite field F_{p^d} with explicit polynomial and matrix operations."""
    def __init__(self, p, mod_poly):
        self.p = p
        self.mod_poly = tuple(mod_poly)
        self.d = len(mod_poly) - 1
        self.size = p ** self.d
        self.zero = PrimeFieldElement([0], p, self.mod_poly)
        self.one = PrimeFieldElement([1], p, self.mod_poly)
        self.gen = PrimeFieldElement([0, 1] if self.d > 1 else [1], p, self.mod_poly)
        self.elements = [
            PrimeFieldElement(list(tup), p, self.mod_poly)
            for tup in itertools.product(range(p), repeat=self.d)
        ]

    def poly_mul(self, f, g):
        if not f or not g:
            return []
        res = [self.zero] * (len(f) + len(g) - 1)
        for i, a in enumerate(f):
            for j, b in enumerate(g):
                res[i + j] = res[i + j] + a * b
        while len(res) > 1 and res[-1].is_zero():
            res.pop()
        return res

    def poly_mod(self, f, g):
        res = list(f)
        while len(res) > 1 and res[-1].is_zero():
            res.pop()
        deg_g = len(g) - 1
        inv_lead = g[-1].inv()
        while len(res) - 1 >= deg_g and not (len(res) == 1 and res[0].is_zero()):
            scale = res[-1] * inv_lead
            shift = len(res) - len(g)
            for i in range(len(g)):
                res[shift + i] = res[shift + i] - scale * g[i]
            while len(res) > 1 and res[-1].is_zero():
                res.pop()
        return res

    def poly_eval(self, f, x):
        acc = self.zero
        for coeff in reversed(f):
            acc = acc * x + coeff
        return acc

    def reciprocal_sigma_inv(self, f, k):
        """Normalized inverse-Frobenius reciprocal f^{#_{s,k}} of Eq. (3.1)."""
        exp = self.p ** (self.d - k)
        r = len(f) - 1
        f0_rho_inv = (f[0] ** exp).inv()
        return [(f[r - i] ** exp) * f0_rho_inv for i in range(r + 1)]

    def matrix_rank(self, rows, ncols):
        mat = [list(row) for row in rows]
        nrows = len(mat)
        r = 0
        for c in range(ncols):
            pivot = None
            for i in range(r, nrows):
                if not mat[i][c].is_zero():
                    pivot = i
                    break
            if pivot is None:
                continue
            mat[r], mat[pivot] = mat[pivot], mat[r]
            inv_p = mat[r][c].inv()
            for j in range(c, ncols):
                mat[r][j] = mat[r][j] * inv_p
            for i in range(nrows):
                if i != r and not mat[i][c].is_zero():
                    factor = mat[i][c]
                    for j in range(c, ncols):
                        mat[i][j] = mat[i][j] - factor * mat[r][j]
            r += 1
        return r

    def direct_hull_dim(self, g, n, k):
        """
        Compute dim_{K_s} Hull_k(<g>) directly by linear algebra over K_s
        using a generator matrix B and Gram matrix G = B sigma(B)^T
        (Remark 3.8(b) / Proposition 2.7).
        """
        deg_g = len(g) - 1
        dim_c = n - deg_g
        if dim_c == 0:
            return 0
        B = []
        for shift in range(dim_c):
            row = [self.zero] * n
            for i, coeff in enumerate(g):
                row[shift + i] = coeff
            B.append(row)
        exp = self.p ** k
        B_sigma = [[elem ** exp for elem in row] for row in B]
        G = []
        for i in range(dim_c):
            g_row = []
            for j in range(dim_c):
                s = self.zero
                for col in range(n):
                    s = s + B[i][col] * B_sigma[j][col]
                g_row.append(s)
            G.append(g_row)
        return dim_c - self.matrix_rank(G, dim_c)


def _poly_trim(K, f):
    res = list(f)
    while len(res) > 1 and res[-1].is_zero():
        res.pop()
    return res or [K.zero]


def _poly_monic(K, f):
    f = _poly_trim(K, f)
    inv_lc = f[-1].inv()
    return [c * inv_lc for c in f]


def _poly_add(K, f, g):
    m = max(len(f), len(g))
    res = [(f[i] if i < len(f) else K.zero) + (g[i] if i < len(g) else K.zero) for i in range(m)]
    return _poly_trim(K, res)


def _poly_sub(K, f, g):
    m = max(len(f), len(g))
    res = [(f[i] if i < len(f) else K.zero) - (g[i] if i < len(g) else K.zero) for i in range(m)]
    return _poly_trim(K, res)


def _poly_divmod(K, f, g):
    rem = _poly_trim(K, f)
    g = _poly_trim(K, g)
    deg_g = len(g) - 1
    if len(rem) - 1 < deg_g or (len(rem) == 1 and rem[0].is_zero()):
        return [K.zero], rem
    q = [K.zero] * (len(rem) - deg_g)
    inv_lc = g[-1].inv()
    while len(rem) - 1 >= deg_g and not (len(rem) == 1 and rem[0].is_zero()):
        shift = len(rem) - len(g)
        scale = rem[-1] * inv_lc
        q[shift] = scale
        for i, coeff in enumerate(g):
            rem[shift + i] = rem[shift + i] - scale * coeff
        rem = _poly_trim(K, rem)
    return _poly_trim(K, q), rem


def _poly_gcd(K, a, b):
    a, b = _poly_trim(K, a), _poly_trim(K, b)
    while not (len(b) == 1 and b[0].is_zero()):
        _, r = _poly_divmod(K, a, b)
        a, b = b, r
    return _poly_monic(K, a)


def _poly_powmod(K, base, exp, mod):
    res = [K.one]
    b = K.poly_mod(base, mod)
    e = exp
    while e > 0:
        if e & 1:
            res = K.poly_mod(K.poly_mul(res, b), mod)
        e >>= 1
        if e:
            b = K.poly_mod(K.poly_mul(b, b), mod)
    return res


def factor_squarefree_monic(K, f, seed=20261023):
    """
    Arbitrary-degree Distinct-Degree + Cantor-Zassenhaus factorisation of a
    square-free monic polynomial f over any finite field K = F_{p^d} (both p = 2
    via trace splitting and odd p via (q^deg - 1)//2 power splitting).
    """
    f = _poly_monic(K, f)
    if len(f) - 1 <= 0:
        return []
    rng = random.Random(seed)
    q = K.size
    rem = f
    x_poly = [K.zero, K.one]
    xp = x_poly
    dd_blocks = []
    deg = 1
    while len(rem) - 1 > 0:
        if len(rem) - 1 < 2 * deg:
            dd_blocks.append((len(rem) - 1, rem))
            break
        xp = _poly_powmod(K, xp, q, rem)
        g = _poly_gcd(K, _poly_sub(K, xp, x_poly), rem)
        if len(g) - 1 > 0:
            dd_blocks.append((deg, g))
            rem, _ = _poly_divmod(K, rem, g)
            xp = K.poly_mod(xp, rem)
        deg += 1

    irreducibles = []
    for d, block in dd_blocks:
        stack = [block]
        while stack:
            h = stack.pop()
            if len(h) - 1 == d:
                irreducibles.append(_poly_monic(K, h))
                continue
            while True:
                rand_poly = _poly_trim(K, [rng.choice(K.elements) for _ in range(len(h) - 1)])
                if len(rand_poly) == 1 and rand_poly[0].is_zero():
                    continue
                if K.p == 2:
                    acc = [K.zero]
                    cur = rand_poly
                    for _ in range(K.d * d):
                        acc = _poly_add(K, acc, cur)
                        cur = K.poly_mod(K.poly_mul(cur, cur), h)
                    split = _poly_gcd(K, acc, h)
                else:
                    half = (q ** d - 1) // 2
                    split = _poly_gcd(K, _poly_sub(K, _poly_powmod(K, rand_poly, half, h), [K.one]), h)
                if 0 < len(split) - 1 < len(h) - 1:
                    q_poly, _ = _poly_divmod(K, h, split)
                    stack.append(split)
                    stack.append(q_poly)
                    break
    irreducibles.sort(key=lambda poly: (len(poly) - 1, [el.c for el in poly]))
    return irreducibles


def factor_xn_minus_lambda(K, n, lam):
    """
    Find all monic irreducible factors of x^n - lam over K (arbitrary degree,
    assuming gcd(n, p) = 1 so x^n - lam is square-free).
    """
    target = [-lam] + [K.zero] * (n - 1) + [K.one]
    factors = factor_squarefree_monic(K, target)
    assert sum(len(f) - 1 for f in factors) == n, "Incomplete factorization"
    return factors


def direct_family_histogram(K, n, lam, k, m_s=1):
    """
    Exhaustively enumerate all 2^|F_s| factor selections of x^n - lam over K,
    compute each code's k-Galois hull dimension directly via linear algebra,
    verify that it matches the orbit boundary formula (Proposition 3.11), and
    return the joint histogram {(kappa, eta): count} and orbit list.
    """
    factors = factor_xn_minus_lambda(K, n, lam)
    tau = {}
    for idx, f in enumerate(factors):
        rec = K.reciprocal_sigma_inv(f, k)
        for idx2, f2 in enumerate(factors):
            if rec == f2:
                tau[idx] = idx2
                break
    assert len(tau) == len(factors), "Reciprocal did not permute factors"

    visited = set()
    orbits = []
    orbit_cycles = []
    for i in range(len(factors)):
        if i not in visited:
            cyc = []
            curr = i
            while curr not in cyc:
                cyc.append(curr)
                visited.add(curr)
                curr = tau[curr]
            orbit_cycles.append(cyc)
            orbits.append((len(cyc), m_s * (len(factors[i]) - 1)))
    orbits.sort()

    hist = defaultdict(int)
    num_f = len(factors)
    for bits in itertools.product((0, 1), repeat=num_f):
        g = [K.one]
        for idx, b in enumerate(bits):
            if b == 1:
                g = K.poly_mul(g, factors[idx])
        kap = m_s * (n - (len(g) - 1))
        eta_direct = m_s * K.direct_hull_dim(g, n, k)

        # Boundary formula (Proposition 3.11)
        eta_orbit = 0
        for cyc in orbit_cycles:
            a_o = len(cyc)
            w_o = m_s * (len(factors[cyc[0]]) - 1)
            b_o = sum(bits[cyc[j]] * (1 - bits[cyc[(j + 1) % a_o]]) for j in range(a_o))
            eta_orbit += w_o * b_o

        assert eta_direct == eta_orbit, f"Mismatch at selection {bits}: {eta_direct} != {eta_orbit}"
        hist[(kap, eta_direct)] += 1

    return dict(sorted(hist.items())), orbits


def verify_quotient_coordinates_mixed_algebra():
    """
    Verify the mixed algebra A = F_4[X]/<X(X^2 + X + omega)> with n = 5, k = 1,
    and lambda = omega(1 + X + X^2) directly in the polynomial-quotient basis
    1, X, X^2 over F_4 (Section 5.2, paragraph 3).
    """
    F4 = FiniteField(2, [1, 1, 1])  # F_4 = F_2[a]/(a^2 + a + 1)
    omega = F4.gen
    F16 = FiniteField(2, [1, 1, 0, 0, 1])  # F_16 = F_2[b]/(b^4 + b + 1)

    hist_f4, orb_f4 = direct_family_histogram(F4, 5, omega, k=1, m_s=1)
    hist_f16, orb_f16 = direct_family_histogram(F16, 5, F16.one, k=1, m_s=2)

    combined = defaultdict(int)
    for (k1, e1), v1 in hist_f4.items():
        for (k2, e2), v2 in hist_f16.items():
            combined[(k1 + k2, e1 + e2)] += v1 * v2
    combined = dict(sorted(combined.items()))
    expected = trace_recurrence_enumerator(orb_f4 + orb_f16)
    assert combined == expected, "Mixed algebra componentwise vs trace recurrence mismatch"
    return combined, orb_f4 + orb_f16


def verify_f32_subsample(num_samples=50, seed=2026):
    """
    Verify a seeded random subsample of individual codes over F_32 with n = 31,
    lambda = 1, k = 1 by direct linear algebra over F_32 against the cyclic
    boundary formula (Section 5.2 and Appendix A).
    """
    F32 = FiniteField(2, [1, 0, 1, 0, 0, 1])  # x^5 + x^2 + 1
    factors = factor_xn_minus_lambda(F32, 31, F32.one)
    tau = {}
    for idx, f in enumerate(factors):
        rec = F32.reciprocal_sigma_inv(f, k=1)
        for idx2, f2 in enumerate(factors):
            if rec == f2:
                tau[idx] = idx2
                break

    visited = set()
    orbit_cycles = []
    for i in range(len(factors)):
        if i not in visited:
            cyc = []
            curr = i
            while curr not in cyc:
                cyc.append(curr)
                visited.add(curr)
                curr = tau[curr]
            orbit_cycles.append(cyc)

    rng = random.Random(seed)
    for _ in range(num_samples):
        bits = [rng.randint(0, 1) for _ in range(31)]
        g = [F32.one]
        for idx, b in enumerate(bits):
            if b == 1:
                g = F32.poly_mul(g, factors[idx])
        eta_direct = F32.direct_hull_dim(g, 31, k=1)
        eta_orbit = sum(
            sum(bits[cyc[j]] * (1 - bits[cyc[(j + 1) % len(cyc)]]) for j in range(len(cyc)))
            for cyc in orbit_cycles
        )
        assert eta_direct == eta_orbit, "F_32 subsample check failed"
    return sorted((len(c), 1) for c in orbit_cycles)


# =============================================================================
# 3. Export CSV Coefficient Tables & Run All Benchmarks
# =============================================================================

def save_joint_csv(filepath, E):
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["kappa", "eta_k", "multiplicity"])
        for (kap, eta), mult in sorted(E.items()):
            writer.writerow([kap, eta, mult])


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tables_dir = os.path.join(base_dir, "tables")
    os.makedirs(tables_dir, exist_ok=True)

    print("=" * 72)
    print("RUNNING EXACT ENUMERATION & LINEAR-ALGEBRA VERIFICATION SUITE")
    print("=" * 72)

    # 1. Verify all families in Table 3 via both Proposition 4.15 and Proposition 4.4
    families = [
        ("Example 5.1 (F_4^4, n=5, lam=1, k=1)", [(1, 1), (2, 2)] * 4, "example5_1_F4x4_n5_joint_enumerator.csv"),
        ("Example 5.2 (F_8, n=7, lam=1, k=1)", [(1, 1), (6, 1)], "table2_F8_n7_joint_enumerator.csv"),
        ("F_16/F_4 (n=5, lam=1, k=1)", [(1, 2), (4, 2)], None),
        ("F_4 (n=5, lam=omega, k=1)", [(1, 1), (2, 2)], None),
        ("Example 5.3 (F_4 x F_16, n=5, lam=(omega,1), k=1)", [(1, 1), (2, 2), (1, 2), (4, 2)], "example5_3_F4xF16_n5_joint_enumerator.csv"),
        ("F_3 (n=4, lam=1, k=0)", [(1, 1), (1, 1), (1, 2)], None),
        ("F_3 (n=4, lam=-1, k=0)", [(2, 2)], None),
        ("F_9 (n=4, lam=1, k=1)", [(1, 1)] * 4, None),
        ("F_9 (n=4, lam=i, k=1)", [(2, 2)], None),
        ("F_9 (n=4, lam=-1, k=1)", [(2, 1), (2, 1)], None),
        ("F_9 (n=8, lam=1, k=1)", [(1, 1)] * 4 + [(2, 1)] * 2, None),
        ("F_25 (n=6, lam=1, k=1)", [(1, 1)] * 6, None),
        ("Example 5.4 (F_32, n=31, lam=1, k=1)", [(1, 1)] + [(10, 1)] * 3, "example5_4_F32_n31_joint_enumerator.csv"),
    ]

    summary_rows = []
    for name, orbits, csv_name in families:
        E_rec = trace_recurrence_enumerator(orbits)
        E_closed = closed_form_enumerator(orbits)
        assert E_rec == E_closed, f"Trace vs closed-form mismatch on {name}"

        tot_th, lcd_th, mean_th, var_th = theoretical_moments_and_lcd(orbits)
        tot_em, lcd_em, mean_em, var_em, cond = moments_from_enumerator(E_rec)
        assert (tot_th, lcd_th, mean_th, var_th) == (tot_em, lcd_em, mean_em, var_em)

        if csv_name:
            save_joint_csv(os.path.join(tables_dir, csv_name), E_rec)

        summary_rows.append({
            "family": name,
            "orbits": str(orbits),
            "total_codes": tot_th,
            "nonzero_joint_terms": len(E_rec),
            "lcd_codes": lcd_th,
            "mean_hull_dim": str(mean_th),
            "var_hull_dim": str(var_th),
        })
        print(f"[PASS] {name}: codes={tot_th}, joint_terms={len(E_rec)}, LCD={lcd_th}, mean={mean_th}, var={var_th}")

    # Save F_32 conditional moments table
    _, _, _, _, cond_f32 = moments_from_enumerator(trace_recurrence_enumerator([(1, 1)] + [(10, 1)] * 3))
    with open(os.path.join(tables_dir, "example5_4_F32_n31_conditional_moments.csv"), "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["kappa", "Phi0", "Phi1", "Phi2", "E[eta_k | kappa]", "Var(eta_k | kappa)"])
        for kap, d in sorted(cond_f32.items()):
            writer.writerow([kap, d["Phi0"], d["Phi1"], d["Phi2"], str(d["mean"]), str(d["var"])])

    # 2. Direct finite-field linear-algebra checks across characteristics 2, 3, and 5
    print("-" * 72)
    print("Running direct finite-field linear-algebra checks (characteristics 2, 3, 5)...")
    F3 = FiniteField(3, [1, 1])
    F4 = FiniteField(2, [1, 1, 1])
    F8 = FiniteField(2, [1, 1, 0, 1])
    F9 = FiniteField(3, [1, 0, 1])  # x^2 + 1
    F25 = FiniteField(5, [2, 0, 1])  # x^2 + 2

    direct_tests = [
        ("F_4, n=5, lam=1, k=1", F4, 5, F4.one, 1, 1),
        ("F_4, n=5, lam=omega, k=1", F4, 5, F4.gen, 1, 1),
        ("F_8, n=7, lam=1, k=1", F8, 7, F8.one, 1, 1),
        ("F_3, n=4, lam=1, k=0", F3, 4, F3.one, 0, 1),
        ("F_3, n=4, lam=-1, k=0", F3, 4, -F3.one, 0, 1),
        ("F_9, n=4, lam=1, k=1", F9, 4, F9.one, 1, 1),
        ("F_9, n=4, lam=i, k=1", F9, 4, F9.gen, 1, 1),
        ("F_9, n=4, lam=-1, k=1", F9, 4, -F9.one, 1, 1),
        ("F_9, n=8, lam=1, k=1", F9, 8, F9.one, 1, 1),
        ("F_25, n=6, lam=1, k=1", F25, 6, F25.one, 1, 1),
    ]
    for label, K, n, lam, k, m_s in direct_tests:
        hist_dir, orbs = direct_family_histogram(K, n, lam, k, m_s=m_s)
        hist_tr = trace_recurrence_enumerator(orbs)
        assert hist_dir == hist_tr, f"Direct linear-algebra histogram mismatch on {label}"
        print(f"[PASS] Direct linear-algebra check: {label} -> orbits={orbs}, terms={len(hist_dir)}")

    hist_mixed, orbs_mixed = verify_quotient_coordinates_mixed_algebra()
    print(f"[PASS] Mixed algebra F_4 x F_16 direct check -> orbits={orbs_mixed}, terms={len(hist_mixed)}")

    orbs_f32 = verify_f32_subsample(num_samples=50, seed=2026)
    print(f"[PASS] F_32 (n=31) direct linear-algebra subsample check (50 random codes, seed=2026) -> orbits={orbs_f32}")

    # 3. Sangwisut et al. (2015) Euclidean cyclic benchmarks: (q, n) = (2, 21) and (3, 16)
    # (q=2, n=21): irreducible factor degrees of x^21 - 1 over F_2 are:
    # deg 1 (fixed): (1, 1); deg 2 (self-reciprocal): (1, 2);
    # two deg 3 (reciprocal pair): (2, 3); two deg 6 (reciprocal pair): (2, 6).
    orbs_2_21 = [(1, 1), (1, 2), (2, 3), (2, 6)]
    E_2_21 = trace_recurrence_enumerator(orbs_2_21)
    hull_6_count = sum(v for (kap, eta), v in E_2_21.items() if eta == 6)
    assert sum(E_2_21.values()) == 64 and hull_6_count == 16
    print(f"[PASS] Sangwisut et al. [9] Example 16 benchmark (q=2, n=21): total=64, hull_dim_6={hull_6_count}")

    # (q=3, n=16): x^16 - 1 over F_3 has:
    # two deg 1 (x-1, x+1, fixed): (1, 1)^2; one deg 2 (x^2+1, self-reciprocal): (1, 2);
    # two deg 2 (x^2+x-1, x^2-x-1, reciprocal pair): (2, 2);
    # two deg 4 (reciprocal pair): (2, 4).
    orbs_3_16 = [(1, 1), (1, 1), (1, 2), (2, 2), (2, 4)]
    E_3_16 = trace_recurrence_enumerator(orbs_3_16)
    hull_4_count = sum(v for (kap, eta), v in E_3_16.items() if eta == 4)
    assert sum(E_3_16.values()) == 128 and hull_4_count == 32
    print(f"[PASS] Sangwisut et al. [9] Example 17 benchmark (q=3, n=16): total=128, hull_dim_4={hull_4_count}")

    save_joint_csv(os.path.join(tables_dir, "benchmark_q2_n21_joint_enumerator.csv"), E_2_21)
    save_joint_csv(os.path.join(tables_dir, "benchmark_q3_n16_joint_enumerator.csv"), E_3_16)

    with open(os.path.join(tables_dir, "table3_all_families_summary.csv"), "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["family", "orbits", "total_codes", "nonzero_joint_terms", "lcd_codes", "mean_hull_dim", "var_hull_dim"],
        )
        writer.writeheader()
        writer.writerows(summary_rows)

    with open(os.path.join(tables_dir, "summary_results.json"), "w") as f:
        json.dump(summary_rows, f, indent=2)

    print("=" * 72)
    print("ALL THEORETICAL, COMBINATORIAL, AND LINEAR-ALGEBRA CHECKS PASSED 100%!")
    print(f"CSV coefficient tables written to: {tables_dir}")
    print("=" * 72)


if __name__ == "__main__":
    main()
