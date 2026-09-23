"""Basic incompatible-twist sanity diagnostic; no transfer-matrix enumeration.

Parameters:
    q=4=2^2, K=F_4, n=5, lambda=omega, k=0 (Euclidean).

Here sigma=p^k=1 and the inverse automorphism exponent is
p^(e*m-k)=4.  Both induce the identity on F_4.  Therefore this test is
DIAGNOSTIC ONLY and is not a convention-resolution test.

The direct dual is computed from the defining equation <c,x>_k=0.  It is
then compared separately with the finalized principal reciprocal and with
the p^k reciprocal alternative; those candidates coincide here because the
field automorphisms coincide.
"""

from validate_long_orbit_examples import (
    BinaryField,
    generator_rows,
    galois_inner_product,
    normalized_galois_reciprocal,
    nullspace,
    product_polynomials,
    row_basis,
    span,
    vector_frobenius,
)


F = BinaryField(2, 0b111)
OMEGA = F.alpha
LENGTH = 5
LAMBDA = OMEGA
K = 0
SIGMA_EXPONENT = 2 ** K
INVERSE_AUTOMORPHISM_EXPONENT = 2 ** (2 * 1 - K)
PRINCIPAL_RECIPROCAL_EXPONENT = INVERSE_AUTOMORPHISM_EXPONENT
ALTERNATIVE_RECIPROCAL_EXPONENT = SIGMA_EXPONENT
FACTORS = (
    (3, 1),
    (2, 1, 1),
    (2, 2, 1),
)


def main():
    # Select one quadratic generator; this produces a nonzero, nontrivial dual.
    generator = FACTORS[1]
    check = product_polynomials(F, [FACTORS[0], FACTORS[2]])
    rows = generator_rows(F, generator, LENGTH)
    code_basis = row_basis(F, rows, LENGTH)

    # A: direct dual from the actual defining inner product.  In this
    # k=0 diagnostic SIGMA_EXPONENT=1, so the requested sigma-row nullspace
    # is exactly the direct Euclidean nullspace; no inverse-automorphism row is used here.
    sigma_rows = [
        vector_frobenius(F, row, SIGMA_EXPONENT)
        for row in code_basis
    ]
    direct_basis = nullspace(F, sigma_rows, LENGTH)
    direct_dual = span(F, direct_basis, LENGTH)
    assert all(
        galois_inner_product(F, codeword, candidate, SIGMA_EXPONENT) == 0
        for codeword in code_basis
        for candidate in direct_basis
    )

    # B: finalized principal reciprocal; C: p^k alternative comparator.
    principal_sharp = normalized_galois_reciprocal(
        F, check, PRINCIPAL_RECIPROCAL_EXPONENT
    )
    principal_dual = span(
        F, generator_rows(F, principal_sharp, LENGTH), LENGTH
    )
    alternative_sharp = normalized_galois_reciprocal(
        F, check, ALTERNATIVE_RECIPROCAL_EXPONENT
    )
    alternative_dual = span(
        F, generator_rows(F, alternative_sharp, LENGTH), LENGTH
    )
    assert direct_dual == principal_dual
    assert direct_dual == alternative_dual

    predicted_twist = F.inv(
        F.frobenius(LAMBDA, PRINCIPAL_RECIPROCAL_EXPONENT)
    )
    assert predicted_twist != LAMBDA
    assert F.pow(
        LAMBDA, 1 + PRINCIPAL_RECIPROCAL_EXPONENT
    ) != 1

    def shift(vector, twist):
        return (F.mul(twist, vector[-1]),) + vector[:-1]

    def is_constacyclic(code, twist):
        return all(shift(vector, twist) in code for vector in code)

    assert is_constacyclic(direct_dual, predicted_twist)
    assert not is_constacyclic(direct_dual, LAMBDA)

    print("basic incompatible-twist sanity diagnostic only:")
    print("  q=4, n=5, lambda=omega, k=0")
    print("  sigma exponent p^k:", SIGMA_EXPONENT)
    print("  inverse automorphism exponent p^(e*m-k):", INVERSE_AUTOMORPHISM_EXPONENT)
    print("  sigma == inverse automorphism on F_4: True")
    print("  direct dual from defining <c,x>_k: checked")
    print("  direct equals principal reciprocal: True")
    print("  direct equals p^k reciprocal alternative: True")
    print("  lambda^(1+principal exponent)=", F.pow(
        LAMBDA, 1 + PRINCIPAL_RECIPROCAL_EXPONENT
    ), "!= 1")
    print("  predicted dual twist lambda^(-principal)=", predicted_twist, "!= lambda")
    print("  direct dual is predicted-twist constacyclic: True")
    print("  direct dual is original-lambda constacyclic: False")
    print("This F4,k=0 example cannot distinguish sigma from rho because both are the identity automorphism on F4.")
    print("It validates incompatible-twist behavior, but not the principal Frobenius convention or the general extension-field reciprocal formula.")
    print("No transfer-matrix enumeration was attempted because the original and dual constacyclic twists are incompatible.")
    print("DIAGNOSTIC ONLY: basic incompatible twist correctly left outside the theorem")


if __name__ == "__main__":
    main()
