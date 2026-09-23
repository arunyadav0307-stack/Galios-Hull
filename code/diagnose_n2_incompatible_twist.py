"""N2-B: incompatible extension-field convention diagnostic.

Parameters are q=4=2^2, K=F_16=F_{4^2}, p=2, e=2, m_s=2,
k=1, n=3, and lambda=alpha^3 of order five.  The defining dual slot
is the code-first slot <c,x>_k=0 for
    <c,x>_k = sum_i c_i x_i^(p^k).

This script computes the direct dual from those defining equations.  It then
compares both independently implemented reciprocal candidates:
  A. the finalized principal inverse-Frobenius exponent p^(e*m_s-k)=8;
  B. the p^k exponent 2 as an explicitly labeled alternative.

It also checks the twist predicted by each candidate.  Because the original
and principal predicted twists are incompatible, no transfer-matrix
enumeration is attempted.
"""

from validate_long_orbit_examples import (
    BinaryField,
    direct_dual_from_inner_product,
    generator_rows,
    galois_inner_product,
    normalized_galois_reciprocal,
    product_polynomials,
    row_basis,
    span,
)


F = BinaryField(4, 0b10011)  # F_16 = F_2[a]/(a^4+a+1)
P = 2
Q = 4
E = 2
M_S = 2
K = 1
N = 3
ALPHA = F.alpha
SIGMA_EXPONENT = P ** K
INVERSE_AUTOMORPHISM_EXPONENT = P ** (E * M_S - K)
PRINCIPAL_RECIPROCAL_EXPONENT = INVERSE_AUTOMORPHISM_EXPONENT
ALTERNATIVE_RECIPROCAL_EXPONENT = SIGMA_EXPONENT
LAMBDA = F.pow(ALPHA, 3)  # order five, nontrivial
ROOT_EXPONENTS = (1, 6, 11)
FACTORS = tuple((F.pow(ALPHA, exponent), 1) for exponent in ROOT_EXPONENTS)


def shift(vector, twist):
    return (F.mul(twist, vector[-1]),) + vector[:-1]


def is_constacyclic(code, twist):
    return all(shift(vector, twist) in code for vector in code)


def selected_products(mask):
    selected = [FACTORS[i] for i in range(N) if (mask >> i) & 1]
    complement = [FACTORS[i] for i in range(N) if not ((mask >> i) & 1)]
    return product_polynomials(F, selected), product_polynomials(F, complement)


def reciprocal_generated_dual(check, exponent):
    reciprocal = normalized_galois_reciprocal(F, check, exponent)
    return span(F, generator_rows(F, reciprocal, N), N)


def main():
    assert Q == P ** E
    assert M_S == 2 and K == 1 and N == 3
    assert F.frobenius(ALPHA, SIGMA_EXPONENT) != F.frobenius(
        ALPHA, INVERSE_AUTOMORPHISM_EXPONENT
    )
    assert F.pow(LAMBDA, 5) == 1 and LAMBDA != 1
    assert product_polynomials(F, FACTORS) == (LAMBDA, 0, 0, 1)
    assert len(set(FACTORS)) == N

    principal_incompatibility = F.pow(
        LAMBDA, 1 + PRINCIPAL_RECIPROCAL_EXPONENT
    )
    alternative_incompatibility = F.pow(
        LAMBDA, 1 + ALTERNATIVE_RECIPROCAL_EXPONENT
    )
    assert principal_incompatibility != 1
    assert alternative_incompatibility != 1

    principal_twist = F.inv(
        F.frobenius(LAMBDA, PRINCIPAL_RECIPROCAL_EXPONENT)
    )
    alternative_twist = F.inv(
        F.frobenius(LAMBDA, ALTERNATIVE_RECIPROCAL_EXPONENT)
    )
    assert principal_twist != LAMBDA
    assert alternative_twist != LAMBDA
    assert principal_twist != alternative_twist

    direct_checks = 0
    principal_generator_agreements = 0
    alternative_generator_agreements = 0
    principal_twist_checks = 0
    alternative_twist_checks = 0
    original_twist_failures = 0
    example_alternative_discrepancy = None
    example_original_failure = None

    for mask in range(1 << N):
        generator, check = selected_products(mask)
        rows = generator_rows(F, generator, N)
        code_basis = row_basis(F, rows, N)

        # A: direct dual from the actual defining inner product.
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
        direct_checks += 1

        # B: finalized principal reciprocal convention.
        principal_dual = reciprocal_generated_dual(
            check, PRINCIPAL_RECIPROCAL_EXPONENT
        )
        assert direct_dual == principal_dual
        principal_generator_agreements += 1

        # C: independently implemented p^k reciprocal alternative.
        alternative_dual = reciprocal_generated_dual(
            check, ALTERNATIVE_RECIPROCAL_EXPONENT
        )
        if direct_dual == alternative_dual:
            alternative_generator_agreements += 1
        elif example_alternative_discrepancy is None:
            example_alternative_discrepancy = mask

        # D: twist predictions.  The principal predicted twist is the one
        # attached to the finalized reciprocal convention.
        assert is_constacyclic(direct_dual, principal_twist)
        principal_twist_checks += 1
        if is_constacyclic(direct_dual, alternative_twist):
            alternative_twist_checks += 1

        # Zero and whole spaces are constacyclic under every twist.  Check
        # original-twist failure for all six proper nonzero selections.
        if mask not in (0, (1 << N) - 1):
            assert not is_constacyclic(direct_dual, LAMBDA)
            original_twist_failures += 1
            if example_original_failure is None:
                example_original_failure = mask

    assert direct_checks == 8
    assert principal_generator_agreements == 8
    assert alternative_generator_agreements < 8
    assert example_alternative_discrepancy is not None
    assert principal_twist_checks == 8
    assert original_twist_failures == 6
    assert example_original_failure is not None

    print("N2-B incompatible extension-field convention diagnostic:")
    print("  p=2, e=2, m_s=2, q=4, K=F_16=F_(4^2), k=1, n=3")
    print("  sigma exponent p^k:", SIGMA_EXPONENT)
    print("  rho exponent p^(e*m_s-k):", INVERSE_AUTOMORPHISM_EXPONENT)
    print("  sigma and rho differ as automorphisms:", True)
    print("  lambda=alpha^3 (order 5):", LAMBDA)
    print("  lambda^(1+principal exponent):", principal_incompatibility, "!= 1")
    print("  lambda^(1+alternative p^k exponent):", alternative_incompatibility, "!= 1")
    print("  defining-inner-product direct dual checks:", direct_checks, "of 8")
    print("  principal reciprocal direct agreements:", principal_generator_agreements, "of 8")
    print("  alternative p^k reciprocal direct agreements:", alternative_generator_agreements, "of 8")
    print("  example alternative discrepancy mask:", example_alternative_discrepancy)
    print("  predicted principal dual twist lambda^(-principal):", principal_twist)
    print("  predicted alternative dual twist lambda^(-p^k):", alternative_twist)
    print("  direct dual constacyclic under principal predicted twist:", principal_twist_checks, "of 8")
    print("  direct dual constacyclic under alternative predicted twist:", alternative_twist_checks, "of 8")
    print("  proper nonzero direct duals failing original lambda twist:", original_twist_failures, "of 6")
    print("  example original-twist failure mask:", example_original_failure)
    print("No transfer-matrix enumeration was attempted because the original and dual constacyclic twists are incompatible.")
    print("PASS: N2-B independently selects the finalized principal convention")


if __name__ == "__main__":
    main()
