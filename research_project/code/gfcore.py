"""Minimal exact helpers over GF(q^2) for Phase 1 recalculation (galois backend)."""
import math, itertools
import galois
import numpy as np


class Field:
    def __init__(self, p, m=2):
        self.GF = galois.GF(p ** m)
        self.p, self.m = p, m
        self.q = p            # Hermitian/Frobenius exponent (field is GF(q^2))
        self.Q = p ** m       # field order
        self.t = self.GF.primitive_element

    def pw(self, k):
        return self.t ** int(k)

    def x(self):
        return galois.Poly.Identity(self.GF)

    def modulus(self, n, alpha):
        """x^n - alpha as a Poly."""
        x = self.x()
        return x ** n - galois.Poly([int(alpha)], field=self.GF)

    def monic_from_ints(self, coeffs_desc):
        """Poly from integer coefficients, highest degree first."""
        return galois.Poly([int(c) for c in coeffs_desc], field=self.GF)

    def poly_from_terms(self, terms):
        """terms: list of (coefficient in GF, exponent) -> Poly."""
        if not terms:
            return galois.Poly([0], field=self.GF)
        deg = max(e for _, e in terms)
        acc = [0] * (deg + 1)
        for c, e in terms:
            acc[e] = int(self.GF(c))
        return galois.Poly(acc[::-1], field=self.GF)

    def conj_recip(self, poly):
        """p^dagger(x) = a0^{-q} * sum_i a_i^q x^{s-i}; the q-th powers of the
        ascending coefficient list already form the descending-degree list."""
        a = poly.coefficients(order="asc")
        q = self.q
        scaled = a ** q
        inv = self.GF(1) / (a[0] ** q)
        return galois.Poly(scaled * inv, field=self.GF)

    def code_from_generator(self, g, n, alpha):
        """Row basis (n x n) of the cyclic-type code <g> in GF[x]/(x^n-alpha)."""
        GF = self.GF
        mod = self.modulus(n, alpha)
        k = n - g.degree
        if k <= 0:
            return GF(np.zeros((0, n), dtype=int))
        rows = []
        for i in range(k):
            c = (g * self.x() ** i) % mod
            rows.append(self._vec(c, n))
        return GF(np.array(rows))

    def herm_dual(self, C):
        """C^perp_H = {y : sum_j c_j y_j^q = 0} = Frobenius of the Euclidean dual."""
        E = self.GF(C).null_space()          # Euclidean dual basis
        return E ** self.q                    # raise every entry to the q-th power

    def _vec(self, poly, n):
        c = poly.coefficients(n, order="asc")
        return self.GF(np.array(c))

    def rank(self, M):
        if M.size == 0:
            return 0
        return int(self.GF(M).row_space().shape[0])

    def hull_dim(self, g, n, alpha):
        C = self.code_from_generator(g, n, alpha)
        return self.hull_of_matrix(C)

    def hull_of_matrix(self, C):
        H = self.herm_dual(C)
        rC, rH = self.rank(C), self.rank(H)
        rM = self.rank(self.GF(np.vstack([C, H])))
        return rC + rH - rM

    def is_dual_containing_matrix(self, C):
        H = self.herm_dual(C)
        return self.rank(self.GF(np.vstack([C, H]))) == self.rank(C)

    def is_dual_containing(self, g, n, alpha):
        C = self.code_from_generator(g, n, alpha)
        H = self.herm_dual(C)
        return self.rank(self.GF(np.vstack([C, H]))) == self.rank(C)

    def min_distance(self, G, maxw=5):
        """Exact min distance: smallest w with a dependent w-subset of parity-check columns."""
        G = self.GF(G)
        H = G.null_space()
        n = G.shape[1]
        for w in range(1, maxw + 1):
            for S in itertools.combinations(range(n), w):
                if self.rank(H[:, list(S)]) < w:
                    return w, True
        return None, False


def phi(m):
    return sum(1 for k in range(1, m + 1) if math.gcd(k, m) == 1)


def ord_j(j, q2):
    """multiplicative order of q2 in (Z/jZ)^*, with ord_1 = 1."""
    if j == 1:
        return 1
    a, y, k = q2 % j, q2 % j, 1
    while y != 1:
        y = (y * a) % j
        k += 1
    return k


def pi(j, q2):
    """0 if j | q^{2k}+q for some k>=0 else 1."""
    for k in range(0, 4 * j + 8):
        if (pow(q2, k, j) + q2 % j * 0 + (int(q2 ** 0.5) if False else 0)) == 0:
            pass
    # direct: iterate k, compute q^{2k}+q mod j
    q = int(round(q2 ** 0.5))
    for k in range(0, 4 * j + 8):
        if (pow(q2, k, j) + q) % j == 0:
            return 0
    return 1


def omega_sets(n_prime, r, q2):
    """(Omega, Omega') as defined in the paper: divisors j of n'r with gcd(n'r/j, r)=1."""
    N = n_prime * r
    om, omp = [], []
    for j in range(1, N + 1):
        if N % j:
            continue
        if math.gcd(N // j, r) != 1:
            continue
        (om if pi(j, q2) == 0 else omp).append(j)
    return om, omp
