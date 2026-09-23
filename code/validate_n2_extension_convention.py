"""N2: direct-dual versus inverse-Frobenius reciprocal over F_16.

The declared inner product is
    <c,x>_{k} = sum_i c_i x_i^(p^k),
with K=F_16=F_{4^2}, p=2, e=2, m_s=2, k=1.
Consequently sigma=p^k=2 and rho=p^(e*m_s-k)=8.

For every one of the 2^5 factor selections for x^5-1 this script compares:
  A. the direct dual from <c,x>_k=0;
  B. the generator h^{#} using rho=8;
  C. the incorrect generator using p^k=2.

The direct equation is checked in its declared form. For linear algebra,
applying rho to <c,x>_k=0 gives rho(c) dot x=0, so the nullspace uses
rho-transformed code rows. This is exactly the dual-slot convention in the
blueprint.
"""

from validate_long_orbit_examples import (
    BinaryField,
    generator_rows,
    normalized_galois_reciprocal,
    nullspace,
    product_polynomials,
    roots_and_factors,
    row_basis,
    vector_frobenius,
)


F = BinaryField(4, 0b10011)  # F_16 = F_2[a]/(a^4+a+1)
N = 5
SIGMA = 2                 # p^k
RHO = 8                   # p^(e*m_s-k)=p^3
LAMBDA = 1


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


def galois_inner_product(codeword, candidate):
    """The declared <codeword,candidate>_{s,k} with sigma=2."""
    value = 0
    for c, x in zip(codeword, candidate):
        value ^= F.mul(c, F.frobenius(x, SIGMA))
    return value


def selected_product(factors, mask):
    selected = [factors[i] for i in range(len(factors)) if (mask >> i) & 1]
    complement = [factors[i] for i in range(len(factors)) if not ((mask >> i) & 1)]
    return product_polynomials(F, selected), product_polynomials(F, complement)


def main():
    _, factors = roots_and_factors(F, N)
    assert LAMBDA == 1
    assert F.pow(LAMBDA, 1 + RHO) == LAMBDA
    predicted_dual_twist = F.inv(F.frobenius(LAMBDA, RHO))
    assert predicted_dual_twist == LAMBDA
    assert len(factors) == N

    factor_index = {factor: i for i, factor in enumerate(factors)}
    correct_tau = [
        factor_index[normalized_galois_reciprocal(F, factor, RHO)]
        for factor in factors
    ]
    incorrect_tau = [
        factor_index[normalized_galois_reciprocal(F, factor, SIGMA)]
        for factor in factors
    ]
    assert correct_tau == [0, 2, 4, 1, 3]
    assert incorrect_tau == [0, 3, 1, 4, 2]

    direct_equals_correct = 0
    direct_equals_incorrect = 0
    direct_equation_checks = 0
    correct_dual_generators = 0
    incorrect_examples = []

    for mask in range(1 << N):
        generator, check = selected_product(factors, mask)
        rows = generator_rows(F, generator, N)
        code_basis = row_basis(F, rows, N)

        # A: direct dual from <c,x>_k=0, represented as rho(c) dot x=0.
        rho_rows = [vector_frobenius(F, row, RHO) for row in code_basis]
        direct_dual_basis = nullspace(F, rho_rows, N)
        direct_dual = span(direct_dual_basis, N)

        # Check the original declared semilinear equations, not only their
        # rho-translated linear form.
        assert all(
            galois_inner_product(codeword, candidate) == 0
            for codeword in code_basis
            for candidate in direct_dual_basis
        )
        direct_equation_checks += 1

        # B: correct inverse-Frobenius reciprocal.
        correct_sharp = normalized_galois_reciprocal(F, check, RHO)
        correct_rows = generator_rows(F, correct_sharp, N)
        correct_dual = span(correct_rows, N)
        assert direct_dual == correct_dual
        correct_dual_generators += 1
        direct_equals_correct += 1

        # C: deliberately incorrect p^k reciprocal.
        incorrect_sharp = normalized_galois_reciprocal(F, check, SIGMA)
        incorrect_rows = generator_rows(F, incorrect_sharp, N)
        incorrect_dual = span(incorrect_rows, N)
        if direct_dual == incorrect_dual:
            direct_equals_incorrect += 1
        elif len(incorrect_examples) < 3:
            incorrect_examples.append(mask)

    assert direct_equals_correct == 32
    assert correct_dual_generators == 32
    assert direct_equals_incorrect == 8
    assert len(incorrect_examples) > 0

    print("N2 extension-field convention validation:")
    print("  K=F_16=F_(4^2), q=4, e=2, m_s=2, n=5, lambda=1, k=1")
    print("  sigma=p^k=2, rho=p^(e*m_s-k)=8")
    print("  compatible predicted dual twist lambda^(-rho):", predicted_dual_twist)
    print("  correct rho reciprocal permutation:", correct_tau)
    print("  incorrect p^k reciprocal permutation:", incorrect_tau)
    print("  A direct dual from <c,x>_k checked:", direct_equation_checks, "of 32")
    print("  A equals B (rho=8 reciprocal):", direct_equals_correct, "of 32")
    print("  A equals C (incorrect p^k=2 reciprocal):", direct_equals_incorrect, "of 32")
    print("  A differs from C:", 32 - direct_equals_incorrect, "of 32")
    print("  example differing selections:", incorrect_examples)
    print("PASS: A=B for all 32; C differs for at least one code")


if __name__ == "__main__":
    main()
