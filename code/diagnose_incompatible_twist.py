"""Diagnostic for an incompatible twist; no transfer-matrix enumeration is used.

Parameters:
    q=4=2^2, K=F_4, n=5, lambda=omega, k=0 (Euclidean).

Here rho=p^(e-k)=4 and
    lambda^(1+rho)=omega^5=omega^2 != 1.
The direct dual is checked to be lambda^(-rho)=omega^2-constacyclic,
while it is not lambda-constacyclic for the selected code.
"""

from validate_long_orbit_examples import (
    BinaryField,
    generator_rows,
    normalized_galois_reciprocal,
    nullspace,
    product_polynomials,
    row_basis,
)


F = BinaryField(2, 0b111)
OMEGA = F.alpha
LENGTH = 5
LAMBDA = OMEGA
K = 0
RHO = 2 ** (2 - K)  # p^(e-k)=4
SIGMA = 2 ** K        # p^k=1
FACTORS = (
    (3, 1),
    (2, 1, 1),
    (2, 2, 1),
)


def span(rows, length):
    result = {(0,) * length}
    for row in rows:
        updated = set(result)
        for coefficient in range(1, F.size):
            scaled = tuple(F.mul(coefficient, value) for value in row)
            updated.update(
                tuple(a ^ b for a, b in zip(vector, scaled))
                for vector in result
            )
        result = updated
    return result


def vector_frobenius(vector, exponent):
    return tuple(F.frobenius(value, exponent) for value in vector)


def shift(vector, twist):
    return (F.mul(twist, vector[-1]),) + vector[:-1]


def is_constacyclic(code, twist):
    return all(shift(vector, twist) in code for vector in code)


def main():
    # Select one quadratic generator; this produces a nonzero, nontrivial dual.
    generator = FACTORS[1]
    check = product_polynomials(F, [FACTORS[0], FACTORS[2]])
    rows = generator_rows(F, generator, LENGTH)

    code_basis = row_basis(F, rows, LENGTH)
    sigma_rows = [vector_frobenius(row, SIGMA) for row in code_basis]
    direct_dual_basis = nullspace(F, sigma_rows, LENGTH)
    direct_dual = span(direct_dual_basis, LENGTH)

    check_sharp = normalized_galois_reciprocal(F, check, RHO)
    expected_dual_rows = generator_rows(F, check_sharp, LENGTH)
    expected_dual = span(expected_dual_rows, LENGTH)
    assert direct_dual == expected_dual

    lambda_prime = F.inv(F.pow(LAMBDA, RHO))
    assert lambda_prime != LAMBDA
    assert F.pow(LAMBDA, 1 + RHO) != 1
    assert is_constacyclic(direct_dual, lambda_prime)
    assert not is_constacyclic(direct_dual, LAMBDA)

    print("incompatible-twist diagnostic:")
    print("  q=4, n=5, lambda=omega, k=0, rho=4")
    print("  lambda^(1+rho)=", F.pow(LAMBDA, 1 + RHO), "!= 1")
    print("  lambda^(-rho)=", lambda_prime, "!= lambda")
    print("  direct dual equals <h^(#)>:", direct_dual == expected_dual)
    print("  direct dual is lambda^(-rho)-constacyclic:",
          is_constacyclic(direct_dual, lambda_prime))
    print("  direct dual is lambda-constacyclic:",
          is_constacyclic(direct_dual, LAMBDA))
    print("  No transfer-matrix enumeration was attempted.")
    print("PASS: incompatible twist correctly left outside the theorem")


if __name__ == "__main__":
    main()
