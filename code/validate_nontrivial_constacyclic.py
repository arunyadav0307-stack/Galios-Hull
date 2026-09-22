"""Exhaustive validation for a nontrivial compatible constacyclic example.

Parameters:
    q=4=2^2, K=F_4, n=5, lambda=omega != 1, k=1.

Here r=(-k) mod e=1, rho=p^r=2 and lambda^(1+rho)=omega^3=1.  The polynomial
x^5-lambda factors as one linear factor and two irreducible quadratics.
The two quadratic factors form a tau-orbit of length 2.

The script checks factorisation, square-freeness, tau, direct constacyclic
codes, direct k-Galois duals, direct hulls, the orbit formula, and the
transfer-matrix joint enumerator for all 2^3 codes.
"""

from collections import Counter
from itertools import product
from validate_long_orbit_examples import (
    BinaryField,
    direct_hull_dimensions,
    generator_rows,
    normalized_galois_reciprocal,
    nullspace,
    product_polynomials,
    row_basis,
    boundary_global_polynomial,
    multiply_global_polynomials,
    transfer_orbit_polynomial,
)


F = BinaryField(2, 0b111)  # F_4 = F_2[omega], omega^2+omega+1=0
OMEGA = F.alpha
LENGTH = 5
LAMBDA = OMEGA
K = 1
R_EXP = (-K) % 2     # r=(-k) mod e=1
RHO = 2 ** R_EXP      # p^r=2
SIGMA = 2 ** K        # p^k=2

# x^5-lambda = x^5+lambda in characteristic two.
MODULUS = (LAMBDA, 0, 0, 0, 0, 1)
FACTORS = (
    (3, 1),        # x + omega + 1
    (2, 1, 1),     # x^2 + x + omega
    (2, 2, 1),     # x^2 + omega*x + omega
)


def p_eval(p, value):
    result = 0
    power = 1
    for coefficient in p:
        result ^= F.mul(coefficient, power)
        power = F.mul(power, value)
    return result


def p_repr(p):
    names = ["0", "1", "omega", "omega+1"]
    terms = []
    for degree in range(len(p) - 1, -1, -1):
        coefficient = p[degree]
        if coefficient == 0:
            continue
        monomial = "1" if degree == 0 else ("x" if degree == 1 else f"x^{degree}")
        if degree == 0:
            terms.append(names[coefficient])
        elif coefficient == 1:
            terms.append(monomial)
        else:
            terms.append(f"({names[coefficient]}){monomial}")
    return " + ".join(terms) or "0"


def span(FIELD, rows, length):
    result = {(0,) * length}
    for row in rows:
        updated = set(result)
        for coefficient in range(1, FIELD.size):
            scaled = tuple(FIELD.mul(coefficient, value) for value in row)
            updated.update(
                tuple(a ^ b for a, b in zip(vector, scaled))
                for vector in result
            )
        result = updated
    return result


def vector_frobenius(vector, exponent):
    return tuple(F.frobenius(value, exponent) for value in vector)


def log_q(size):
    dimension = 0
    while size > 1:
        assert size % F.size == 0
        size //= F.size
        dimension += 1
    return dimension


def constacyclic_shift(vector, twist):
    return (F.mul(twist, vector[-1]),) + vector[:-1]


def is_constacyclic(code, twist):
    return all(constacyclic_shift(vector, twist) in code for vector in code)


def main():
    assert LAMBDA != 1
    assert F.pow(LAMBDA, 1 + RHO) == 1

    factor_product = product_polynomials(F, FACTORS)
    assert factor_product == MODULUS
    assert len(set(FACTORS)) == len(FACTORS)
    # Each quadratic has no root in F_4, so the displayed factorisation is
    # into distinct irreducibles. Distinct factors imply square-freeness here.
    for factor in FACTORS[1:]:
        assert all(p_eval(factor, value) != 0 for value in range(F.size))

    factor_index = {factor: i for i, factor in enumerate(FACTORS)}
    tau = []
    for factor in FACTORS:
        image = normalized_galois_reciprocal(F, factor, RHO)
        assert image in factor_index
        tau.append(factor_index[image])

    visited = set()
    orbits = []
    for start in range(len(FACTORS)):
        if start in visited:
            continue
        orbit = []
        current = start
        while current not in visited:
            visited.add(current)
            orbit.append(current)
            current = tau[current]
        assert current == start
        orbits.append(orbit)

    orbit_data = [
        (len(orbit), len(FACTORS[orbit[0]]) - 1)
        for orbit in orbits
    ]

    direct_joint = Counter()
    dual_checks = 0
    for mask in range(1 << len(FACTORS)):
        selected = [
            FACTORS[i]
            for i in range(len(FACTORS))
            if (mask >> i) & 1
        ]
        complement = [
            FACTORS[i]
            for i in range(len(FACTORS))
            if not ((mask >> i) & 1)
        ]
        generator = product_polynomials(F, selected)
        check = product_polynomials(F, complement)
        rows = generator_rows(F, generator, LENGTH)
        code = span(F, rows, LENGTH)
        assert is_constacyclic(code, LAMBDA)

        # Direct k-Galois dual: nullspace of x dot c^(p^k)=0.
        code_basis = row_basis(F, rows, LENGTH)
        sigma_rows = [vector_frobenius(row, SIGMA) for row in code_basis]
        direct_dual_basis = nullspace(F, sigma_rows, LENGTH)
        direct_dual = span(F, direct_dual_basis, LENGTH)

        check_sharp = normalized_galois_reciprocal(F, check, RHO)
        expected_dual_rows = generator_rows(F, check_sharp, LENGTH)
        expected_dual = span(F, expected_dual_rows, LENGTH)
        assert direct_dual == expected_dual
        assert row_basis(F, direct_dual_basis, LENGTH) == row_basis(
            F, expected_dual_rows, LENGTH
        )
        dual_checks += 1

        hull = code & direct_dual
        code_dimension = log_q(len(code))
        hull_dimension = log_q(len(hull))
        rank_code_dimension, rank_hull_dimension = direct_hull_dimensions(
            F, rows, SIGMA
        )
        assert (code_dimension, hull_dimension) == (
            rank_code_dimension,
            rank_hull_dimension,
        )
        direct_joint[(code_dimension, hull_dimension)] += 1

    boundary = boundary_global_polynomial(orbit_data)
    transfer = multiply_global_polynomials(
        [transfer_orbit_polynomial(length, weight)
         for length, weight in orbit_data]
    )

    assert direct_joint == boundary
    assert boundary == transfer
    assert sum(direct_joint.values()) == 2 ** len(FACTORS)

    print("nontrivial compatible constacyclic example:")
    print("  q=4, n=5, lambda=omega != 1, k=1, r=1, rho=2")
    print("  factorisation:", " * ".join(p_repr(factor) for factor in FACTORS))
    print("  square-free: True")
    print("  lambda^(1+rho)=", F.pow(LAMBDA, 1 + RHO), "= 1")
    print("  tau permutation:", tau)
    print("  orbit lengths:", [len(orbit) for orbit in orbits])
    print("  direct dual-generator checks:", dual_checks, "of", 2 ** len(FACTORS))
    print("  direct == orbit-boundary:", direct_joint == boundary)
    print("  orbit-boundary == transfer:", boundary == transfer)
    print("  joint histogram:", dict(sorted(direct_joint.items())))
    hull_histogram = Counter()
    for (_, hull_dimension), count in direct_joint.items():
        hull_histogram[hull_dimension] += count
    print("  hull histogram:", dict(sorted(hull_histogram.items())))
    print("PASS: nontrivial compatible constacyclic validation")


if __name__ == "__main__":
    main()
