"""N2-B: incompatible twist diagnostic over K=F_16=F_{4^2}.

This is the convention-sensitive incompatible-twist diagnostic.  It uses
q=4=2^2, K=F_16=F_{4^2}, m_s=2, k=1, n=3, and a nontrivial lambda of
order five.  Thus sigma(a)=a^2 and rho(a)=a^8 are genuinely different.

The test exhausts all eight factor selections of x^3-lambda and independently
checks:
  A. the defining dual <c,x>_{s,k}=0 by linear algebra;
  B. the generator h^{#} using the principal rho reciprocal;
  C. the predicted dual twist lambda^{-rho};
  D. constacyclicity under that predicted twist; and
  E. failure of constacyclicity under the original lambda for a proper,
     nonzero selected code.

No transfer-matrix enumeration is used: incompatibility places this test
outside the same-factor-set compatible theorem.
"""

from validate_long_orbit_examples import (
    BinaryField,
    generator_rows,
    normalized_galois_reciprocal,
    nullspace,
    product_polynomials,
    row_basis,
    vector_frobenius,
)


F = BinaryField(4, 0b10011)  # F_16 = F_2[a]/(a^4+a+1)
ALPHA = F.alpha
Q = 4
P = 2
E = 2
M_S = 2
K = 1
N = 3
SIGMA = P ** K                 # 2
RHO = P ** (E * M_S - K)       # 8
LAMBDA = F.pow(ALPHA, 3)       # order five, nontrivial
ROOT_EXPONENTS = (1, 6, 11)    # 3*j = 3 mod 15
FACTORS = tuple((F.pow(ALPHA, j), 1) for j in ROOT_EXPONENTS)


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


def inner_product(codeword, candidate):
    value = 0
    for c, x in zip(codeword, candidate):
        value ^= F.mul(c, F.frobenius(x, SIGMA))
    return value


def shift(vector, twist):
    return (F.mul(twist, vector[-1]),) + vector[:-1]


def is_constacyclic(code, twist):
    return all(shift(vector, twist) in code for vector in code)


def selected_products(mask):
    selected = [FACTORS[i] for i in range(N) if (mask >> i) & 1]
    complement = [FACTORS[i] for i in range(N) if not ((mask >> i) & 1)]
    return product_polynomials(F, selected), product_polynomials(F, complement)


def main():
    assert Q == 4 and P == 2 and E == 2 and M_S == 2 and K == 1
    assert F.frobenius(ALPHA, SIGMA) != F.frobenius(ALPHA, RHO)
    assert F.pow(LAMBDA, 5) == 1 and LAMBDA != 1
    assert product_polynomials(F, FACTORS) == (LAMBDA, 0, 0, 1)
    assert len(set(FACTORS)) == N

    # The same-twist condition fails, so the predicted dual twist differs.
    assert F.pow(LAMBDA, 1 + RHO) != 1
    dual_twist = F.inv(F.frobenius(LAMBDA, RHO))
    assert dual_twist != LAMBDA

    direct_checks = 0
    generator_checks = 0
    predicted_twist_checks = 0
    original_twist_failures = 0
    selected_failure_mask = None

    for mask in range(1 << N):
        generator, check = selected_products(mask)
        rows = generator_rows(F, generator, N)
        code_basis = row_basis(F, rows, N)

        # A: direct dual from <c,x>_{s,k}=0.  Applying rho to the
        # equations gives the ordinary nullspace of rho-transformed rows.
        rho_rows = [vector_frobenius(F, row, RHO) for row in code_basis]
        direct_dual_basis = nullspace(F, rho_rows, N)
        direct_dual = span(direct_dual_basis, N)
        assert all(
            inner_product(codeword, candidate) == 0
            for codeword in code_basis
            for candidate in direct_dual_basis
        )
        direct_checks += 1

        # B: principal inverse-Frobenius reciprocal prediction.
        predicted_generator = normalized_galois_reciprocal(F, check, RHO)
        predicted_dual = span(
            generator_rows(F, predicted_generator, N), N
        )
        assert direct_dual == predicted_dual
        generator_checks += 1

        # C/D: the predicted twist is lambda^{-rho}, not lambda.
        assert is_constacyclic(direct_dual, dual_twist)
        predicted_twist_checks += 1

        # For a proper, nonzero code the original twist must fail.  The
        # zero and whole spaces are constacyclic for every twist, so skip them.
        if mask not in (0, (1 << N) - 1):
            assert not is_constacyclic(direct_dual, LAMBDA)
            original_twist_failures += 1
            if selected_failure_mask is None:
                selected_failure_mask = mask

    assert direct_checks == 8
    assert generator_checks == 8
    assert predicted_twist_checks == 8
    assert original_twist_failures == 6
    assert selected_failure_mask is not None

    print("N2-B incompatible-twist diagnostic:")
    print("  K=F_16=F_(4^2), q=4, p=2, e=2, m_s=2, k=1, n=3")
    print("  lambda=alpha^3 (order 5), sigma=2, rho=8")
    print("  sigma(alpha) != rho(alpha):", True)
    print("  factorization: (x+alpha)(x+alpha^6)(x+alpha^11)")
    print("  lambda^(1+rho) != 1:", True)
    print("  predicted dual twist lambda^(-rho):", dual_twist)
    print("  direct dual checks:", direct_checks, "of 8")
    print("  direct dual == <h^(#_rho)>:", generator_checks, "of 8")
    print("  dual constacyclic under predicted twist:", predicted_twist_checks, "of 8")
    print("  proper nonzero codes failing original twist:", original_twist_failures, "of 6")
    print("  example proper selection mask failing original twist:", selected_failure_mask)
    print("  No transfer-matrix enumeration was attempted.")
    print("PASS: incompatible extension-field twist diagnosed without enumeration")


if __name__ == "__main__":
    main()
