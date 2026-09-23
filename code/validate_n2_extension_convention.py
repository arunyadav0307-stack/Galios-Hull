"""N2-A: independent convention comparison over K=F_16.

The defining inner product is
    <c,x>_k = sum_i c_i x_i^(p^k),
with K=F_16=F_{4^2}, p=2, e=2, m_s=2, k=1.
Thus sigma has exponent p^k=2 and its inverse has exponent
p^(e*m_s-k)=8.

The direct dual is computed from the defining equations, independently of
both reciprocal candidates.  The finalized code-first convention predicts the
inverse-Frobenius reciprocal; the p^k reciprocal is retained only as an
explicit alternative comparator.
"""

from validate_long_orbit_examples import (
    BinaryField,
    direct_dual_from_inner_product,
    generator_rows,
    galois_inner_product,
    normalized_galois_reciprocal,
    product_polynomials,
    roots_and_factors,
    row_basis,
    span,
)


F = BinaryField(4, 0b10011)  # F_16 = F_2[a]/(a^4+a+1)
P = 2
Q = 4
E = 2
M_S = 2
K = 1
N = 5
SIGMA_EXPONENT = P ** K
INVERSE_AUTOMORPHISM_EXPONENT = P ** (E * M_S - K)
PRINCIPAL_RECIPROCAL_EXPONENT = INVERSE_AUTOMORPHISM_EXPONENT
ALTERNATIVE_RECIPROCAL_EXPONENT = SIGMA_EXPONENT
LAMBDA = 1


def selected_product(factors, mask):
    selected = [factors[i] for i in range(len(factors)) if (mask >> i) & 1]
    complement = [
        factors[i] for i in range(len(factors))
        if not ((mask >> i) & 1)
    ]
    return product_polynomials(F, selected), product_polynomials(F, complement)


def main():
    _, factors = roots_and_factors(F, N)
    assert Q == P ** E
    assert LAMBDA == 1
    assert F.pow(LAMBDA, 1 + INVERSE_AUTOMORPHISM_EXPONENT) == LAMBDA
    assert len(factors) == N

    factor_index = {factor: i for i, factor in enumerate(factors)}
    principal_tau = [
        factor_index[
            normalized_galois_reciprocal(
                F, factor, PRINCIPAL_RECIPROCAL_EXPONENT
            )
        ]
        for factor in factors
    ]
    alternative_tau = [
        factor_index[
            normalized_galois_reciprocal(
                F, factor, ALTERNATIVE_RECIPROCAL_EXPONENT
            )
        ]
        for factor in factors
    ]
    assert principal_tau == [0, 2, 4, 1, 3]
    assert alternative_tau == [0, 3, 1, 4, 2]
    assert principal_tau != alternative_tau

    direct_equation_checks = 0
    direct_equals_principal = 0
    direct_equals_alternative = 0
    principal_generator_checks = 0
    alternative_generator_checks = 0
    alternative_examples = []

    for mask in range(1 << N):
        generator, check = selected_product(factors, mask)
        rows = generator_rows(F, generator, N)
        code_basis = row_basis(F, rows, N)

        # A: actual direct dual from <c,x>_k=0.  The helper introduces
        # y=sigma(x), solves c dot y=0, and maps y back through sigma^{-1}.
        direct_basis, direct_dual = direct_dual_from_inner_product(
            F,
            code_basis,
            SIGMA_EXPONENT,
            INVERSE_AUTOMORPHISM_EXPONENT,
            N,
        )
        assert all(
            galois_inner_product(
                F, codeword, candidate, SIGMA_EXPONENT
            ) == 0
            for codeword in code_basis
            for candidate in direct_basis
        )
        direct_equation_checks += 1

        # B: finalized principal reciprocal convention.
        principal_sharp = normalized_galois_reciprocal(
            F, check, PRINCIPAL_RECIPROCAL_EXPONENT
        )
        principal_dual = span(
            F, generator_rows(F, principal_sharp, N), N
        )
        assert direct_dual == principal_dual
        direct_equals_principal += 1
        principal_generator_checks += 1

        # C: independently implemented p^k reciprocal alternative.
        alternative_sharp = normalized_galois_reciprocal(
            F, check, ALTERNATIVE_RECIPROCAL_EXPONENT
        )
        alternative_dual = span(
            F, generator_rows(F, alternative_sharp, N), N
        )
        alternative_generator_checks += 1
        if direct_dual == alternative_dual:
            direct_equals_alternative += 1
        elif len(alternative_examples) < 3:
            alternative_examples.append(mask)

    assert direct_equation_checks == 32
    assert direct_equals_principal == 32
    assert principal_generator_checks == 32
    assert alternative_generator_checks == 32
    assert direct_equals_alternative == 8
    assert alternative_examples

    print("N2-A extension-field convention validation:")
    print("  K=F_16=F_(4^2), p=2, q=4, e=2, m_s=2, n=5, lambda=1, k=1")
    print("  sigma exponent p^k:", SIGMA_EXPONENT)
    print("  inverse automorphism exponent p^(e*m_s-k):", INVERSE_AUTOMORPHISM_EXPONENT)
    print("  principal reciprocal exponent:", PRINCIPAL_RECIPROCAL_EXPONENT)
    print("  alternative reciprocal exponent:", ALTERNATIVE_RECIPROCAL_EXPONENT)
    print("  principal reciprocal permutation:", principal_tau)
    print("  alternative reciprocal permutation:", alternative_tau)
    print("  direct dual from defining <c,x>_k equations:", direct_equation_checks, "of 32")
    print("  direct equals principal reciprocal:", direct_equals_principal, "of 32")
    print("  direct equals alternative p^k reciprocal:", direct_equals_alternative, "of 32")
    print("  example alternative discrepancies:", alternative_examples)
    print("PASS: direct dual selects the principal inverse-Frobenius convention")


if __name__ == "__main__":
    main()
