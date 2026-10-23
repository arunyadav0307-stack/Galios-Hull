#!/usr/bin/env python3
"""
Core exact enumerator for the proposed Paper 2:

    Joint code-dimension and k-Galois-hull enumerators for
    repeated-root constacyclic codes over square-free affine algebras.

Mathematical conventions
------------------------
* n = n' * p^t, gcd(n', p) = 1, and M = p^t is the factor multiplicity.
* A component generator is prod_f f^{e_f}, 0 <= e_f <= M.
* On one reciprocal orbit (a, w), with cyclic exponent word e_0,...,e_{a-1},

      kappa contribution = w * sum_i (M - e_i),
      eta   contribution = w * sum_i min(e_i, M - e_{i+1}).

* Transfer-matrix entry (source alpha, destination beta):
      U^{w(M-beta)} Z^{w min(alpha, M-beta)}.

Only Python's standard library is used.  All counts are Python integers and
all moments are fractions.Fraction objects.
"""

from collections import defaultdict
from fractions import Fraction
import itertools
import math


# ---------------------------------------------------------------------------
# 1. Transfer-matrix / dynamic-programming enumerators
# ---------------------------------------------------------------------------

def trace_dp_global(orbits, M):
    """Compute E(U,Z) directly by the closed-walk transfer-matrix DP.

    Parameters
    ----------
    orbits : iterable of (a, w)
        a = reciprocal-orbit length, w = m_s * (common factor degree).
    M : int
        Repeated-root multiplicity p^t.

    Returns
    -------
    dict[(kappa, eta), int]
    """
    if M < 1:
        raise ValueError("M must be positive")
    G = {(0, 0): 1}
    states = range(M + 1)
    for a, w in orbits:
        if a < 1 or w < 1:
            raise ValueError("orbit lengths and weights must be positive")
        next_G = defaultdict(int)
        for start in states:
            state = {s: defaultdict(int) for s in states}
            for key, val in G.items():
                state[start][key] += val
            for _ in range(a):
                new_state = {s: defaultdict(int) for s in states}
                for alpha in states:
                    if not state[alpha]:
                        continue
                    for beta in states:
                        d_kappa = w * (M - beta)
                        d_eta = w * min(alpha, M - beta)
                        for (kappa, eta), val in state[alpha].items():
                            new_state[beta][(kappa + d_kappa, eta + d_eta)] += val
                state = new_state
            for key, val in state[start].items():
                next_G[key] += val
        G = {k: v for k, v in next_G.items() if v}
    return dict(sorted(G.items()))


def one_orbit_bruteforce(a, w, M):
    """One-orbit enumerator by listing all (M+1)^a exponent words.

    This is intentionally independent of the transfer-matrix implementation.
    Use only for small a and M.
    """
    out = defaultdict(int)
    for word in itertools.product(range(M + 1), repeat=a):
        kappa = w * sum(M - e for e in word)
        eta = w * sum(min(word[i], M - word[(i + 1) % a]) for i in range(a))
        out[(kappa, eta)] += 1
    return dict(sorted(out.items()))


def convolve(poly1, poly2):
    out = defaultdict(int)
    for (k1, e1), v1 in poly1.items():
        for (k2, e2), v2 in poly2.items():
            out[(k1 + k2, e1 + e2)] += v1 * v2
    return {k: v for k, v in out.items() if v}


def enumerator_by_orbit_convolution(orbits, M):
    """Compute E by forming each one-orbit trace polynomial, then convolving."""
    E = {(0, 0): 1}
    for a, w in orbits:
        local = trace_dp_global([(a, w)], M)
        E = convolve(E, local)
    return dict(sorted(E.items()))


# ---------------------------------------------------------------------------
# 2. Exact moments: from coefficients and from theoretical formulas
# ---------------------------------------------------------------------------

def moments_from_enumerator(E):
    total = sum(E.values())
    lcd = sum(v for (_, eta), v in E.items() if eta == 0)
    mean_eta = Fraction(sum(eta * v for (_, eta), v in E.items()), total)
    e_eta2 = Fraction(sum(eta * eta * v for (_, eta), v in E.items()), total)
    var_eta = e_eta2 - mean_eta * mean_eta
    mean_kappa = Fraction(sum(k * v for (k, _), v in E.items()), total)
    e_kappa2 = Fraction(sum(k * k * v for (k, _), v in E.items()), total)
    var_kappa = e_kappa2 - mean_kappa * mean_kappa
    cov = Fraction(sum(k * eta * v for (k, eta), v in E.items()), total) - mean_kappa * mean_eta

    by_kappa = defaultdict(list)
    for (k, eta), v in E.items():
        by_kappa[k].append((eta, v))
    conditional = {}
    for k, vals in sorted(by_kappa.items()):
        phi0 = sum(v for _, v in vals)
        phi1 = sum(eta * v for eta, v in vals)
        phi2 = sum(eta * (eta - 1) * v for eta, v in vals)
        cmean = Fraction(phi1, phi0)
        cvar = Fraction(phi2 + phi1, phi0) - cmean * cmean
        conditional[k] = {
            "Phi0": phi0, "Phi1": phi1, "Phi2": phi2,
            "mean": cmean, "var": cvar,
        }
    return {
        "total": total, "lcd": lcd,
        "mean_kappa": mean_kappa, "var_kappa": var_kappa,
        "mean_eta": mean_eta, "var_eta": var_eta,
        "cov_kappa_eta": cov, "conditional": conditional,
    }


def _mu_edge(M):
    """E[min(X,M-Y)] for independent uniform X,Y on {0,...,M}."""
    return Fraction(M * (2 * M + 1), 6 * (M + 1))


def _a1_mean(M):
    """E[min(X,M-X)], X uniform on {0,...,M}."""
    return Fraction((M * M) // 4, M + 1)


def _a1_variance(M):
    """Var(min(X,M-X)), X uniform on {0,...,M} (unweighted)."""
    if M % 2 == 0:
        return Fraction(M * (M + 2) * (M * M + 2 * M + 4), 48 * (M + 1) ** 2)
    return Fraction((M - 1) * (M + 3), 48)


def theoretical_moments(orbits, M):
    """Total, LCD count, and unconditional eta mean/variance from formulas.

    Variance contributions (before multiplying by w^2):
    * a = 1: parity formulas in _a1_variance;
    * a = 2: M(M+2)(M^2+2M+3) / (18(M+1)^2);
    * a >= 3: a * M(M+2)(M^2+2M+2) / (60(M+1)^2).
    At M=1 these reduce to 0, 1/4, and a/16.
    """
    Orbits = list(orbits)
    total = (M + 1) ** sum(a for a, _ in Orbits)
    lcd = 2 ** len(Orbits)
    mean = Fraction(0)
    var = Fraction(0)
    for a, w in Orbits:
        if a == 1:
            mean += w * _a1_mean(M)
            var += w * w * _a1_variance(M)
        elif a == 2:
            mean += a * w * _mu_edge(M)
            var += w * w * Fraction(
                M * (M + 2) * (M * M + 2 * M + 3), 18 * (M + 1) ** 2
            )
        else:
            mean += a * w * _mu_edge(M)
            var += w * w * a * Fraction(
                M * (M + 2) * (M * M + 2 * M + 2), 60 * (M + 1) ** 2
            )
    return {"total": total, "lcd": lcd, "mean_eta": mean, "var_eta": var}


# ---------------------------------------------------------------------------
# 3. Extremal classes: LCD, self-orthogonal, dual-containing, self-dual
# ---------------------------------------------------------------------------

def cyclic_relation_count(a, M, relation):
    """Count cyclic exponent words satisfying a condition on every edge.

    relation is a function (previous, current) -> bool.  The count is the
    trace of the a-th power of the corresponding (M+1)x(M+1) 0-1 matrix,
    computed here by DP over the initial state.
    """
    count = 0
    for first in range(M + 1):
        dp = {first: 1}  # current/last value after placing position 0
        for _ in range(1, a):
            ndp = defaultdict(int)
            for prev, val in dp.items():
                for curr in range(M + 1):
                    if relation(prev, curr):
                        ndp[curr] += val
            dp = ndp
        for last, val in dp.items():
            if relation(last, first):
                count += val
    return count


def extremal_counts(orbits, M):
    """Counts per orbit and globally for the four extremal classes.

    * LCD: min(alpha, M-beta) = 0 on every edge (expected: 2 per orbit);
    * self-orthogonal C <= D_k(C): alpha + beta >= M on every edge
      (condition written for consecutive pair (e_{i-1}, e_i));
    * dual-containing D_k(C) <= C: alpha + beta <= M;
    * self-dual: alpha + beta = M.
    Global compatible-component counts are products over orbits.
    """
    relations = {
        "lcd": lambda x, y: min(x, M - y) == 0,
        "self_orthogonal": lambda x, y: x + y >= M,
        "dual_containing": lambda x, y: x + y <= M,
        "self_dual": lambda x, y: x + y == M,
    }
    per_orbit = []
    totals = {k: 1 for k in relations}
    for a, w in orbits:
        row = {"a": a, "w": w}
        for name, rel in relations.items():
            row[name] = cyclic_relation_count(a, M, rel)
            totals[name] *= row[name]
        per_orbit.append(row)
    return {"per_orbit": per_orbit, "total": totals}


def self_dual_count_formula(a, M):
    """Closed form for the number of self-dual words on one orbit."""
    if a % 2 == 0:
        return M + 1
    return 1 if M % 2 == 0 else 0


# ---------------------------------------------------------------------------
# 4. Support helpers
# ---------------------------------------------------------------------------

def one_orbit_support(a, w, M):
    E = one_orbit_bruteforce(a, w, M) if (M + 1) ** a <= 250000 else trace_dp_global([(a, w)], M)
    return set(E)


def predicted_one_orbit_support(a, w, M):
    """Target support description (unweighted R=sum(M-e_i), H=hull/w):

        min(R, M, aM-R) <= H <= min(R, aM-R).

    This function is provided so the conjectural/target proposition can be
    tested systematically while its proof is being written.
    """
    out = set()
    W = a * M
    for R in range(W + 1):
        lo = min(R, M, W - R)
        hi = min(R, W - R)
        for H in range(lo, hi + 1):
            out.add((w * R, w * H))
    return out


if __name__ == "__main__":
    demo_orbits = [(1, 1), (6, 1)]
    E = trace_dp_global(demo_orbits, M=2)
    print("orbits", demo_orbits, "M=2")
    print("joint terms", len(E), "total", sum(E.values()))
    print("theoretical", theoretical_moments(demo_orbits, 2))
    print("from coefficients", {k: v for k, v in moments_from_enumerator(E).items() if k != "conditional"})
