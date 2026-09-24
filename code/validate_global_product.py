"""Exhaustive direct-product validation for the Phase-10C global bridge.

The test uses one common base field F_4 and two component fields

    K_1 = F_4,       m_1 = 1,
    K_2 = F_16,      m_2 = 2,

with n=5, lambda=(omega,1), and k=1, where omega is the nontrivial
primitive element of F_4.  The first component has three irreducible factors
(one fixed factor and one reciprocal 2-orbit); the second splits into five
linear factors.  Hence there are 2^3 * 2^5 = 256 distinct labeled
factor-selection codes in the product algebra A = K_1 x K_2.

For every one of those 256 selections this script independently checks:

* component factorisation, square-freeness, inverse-Frobenius factor action,
  and direct code-first duals;
* the fixed tuple-coordinate product algebra, tuple Frobenius, and the
  A-valued componentwise pairing;
* the global CRT/product code and the global dual by an independently built
  binary nullspace of the A-valued pairing equations;
* injectivity of labeled factor selections;
* global F_4-dimension additivity for codes and hulls (implemented through
  an independent F_2 nullspace expansion);
* equality of the exhaustive global histogram with both the product of the
  component histograms and the orbit-boundary/transfer enumerator;
* the stated uniform mean and variance formulas.

No third-party package is required.  The test is intentionally direct rather
than a restatement of the global formulas: global dual equations are expanded
as binary equations in the tuple algebra, while the expected answer is built
from the two independently computed component duals.
"""

from collections import Counter
from itertools import product

from validate_long_orbit_examples import (
    BinaryField,
    direct_dual_from_inner_product,
    generator_rows,
    galois_inner_product,
    matrix_rank,
    normalized_galois_reciprocal,
    product_polynomials,
    roots_and_factors,
    row_basis,
    span,
    transfer_orbit_polynomial,
    boundary_global_polynomial,
    multiply_global_polynomials,
)


N = 5
K_GALOIS = 1
BASE_FIELD_DEGREE = 2  # q=4=2^2.

# F_2[a]/(a^2+a+1), with elements 0, 1, a, a+1; this is the base field
# F_4 and the first component K_1.
F4 = BinaryField(2, 0b111)
# F_2[b]/(b^4+b+1), viewed as K_2=F_{4^2}.
F16 = BinaryField(4, 0b10011)
FIELDS = (F4, F16)
ABSOLUTE_DEGREES = (2, 4)  # [K_s:F_2].
EXTENSION_DEGREES = (1, 2)  # m_s=[K_s:F_4].
INVERSE_FROBENIUS_POWERS = (1, 3)  # e*m_s-k for e=2, k=1.

# Coefficients are low-degree first.  The first modulus is x^5-omega,
# with omega=alpha=2 in the chosen F_4 representation; the second is
# x^5-1.  In characteristic two, subtraction is addition.
LAMBDA = (2, 1)
F4_FACTORS = (
    (3, 1),
    (2, 1, 1),
    (2, 2, 1),
)
F16_FACTORS = roots_and_factors(F16, N)[1]
FACTORS = (F4_FACTORS, F16_FACTORS)
COMPONENT_MODULI = tuple(
    (twist,) + (0,) * (N - 1) + (1,)
    for twist in LAMBDA
)


class ProductAlgebra:
    """The fixed tuple-coordinate realization A = F_4 x F_16."""

    def __init__(self, fields):
        self.fields = tuple(fields)

    def zero(self):
        return tuple(0 for _ in self.fields)

    def one(self):
        return tuple(1 for _ in self.fields)

    def add(self, left, right):
        return tuple(
            field.add(a, b)
            for field, a, b in zip(self.fields, left, right)
        )

    def mul(self, left, right):
        return tuple(
            field.mul(a, b)
            for field, a, b in zip(self.fields, left, right)
        )

    def frobenius(self, value, iteration):
        return tuple(
            field.frobenius(a, iteration)
            for field, a in zip(self.fields, value)
        )

    def pairing(self, left, right, iteration):
        """A-valued pairing on two global vectors."""
        return tuple(
            galois_inner_product(field, x, y, iteration)
            for field, x, y in zip(self.fields, left, right)
        )


A = ProductAlgebra(FIELDS)
ZERO_VECTORS = tuple((0,) * N for _ in FIELDS)


def evaluate_polynomial(field, polynomial, value):
    result = 0
    power = 1
    for coefficient in polynomial:
        result ^= field.mul(coefficient, power)
        power = field.mul(power, value)
    return result


def selected_product(field, factors, mask):
    selected = [
        factor for index, factor in enumerate(factors)
        if (mask >> index) & 1
    ]
    complement = [
        factor for index, factor in enumerate(factors)
        if not ((mask >> index) & 1)
    ]
    return (
        product_polynomials(field, selected),
        product_polynomials(field, complement),
    )


def component_data(component, mask):
    """Return component bases, dual bases, and dimensions for one mask."""
    field = FIELDS[component]
    factors = FACTORS[component]
    generator, check = selected_product(field, factors, mask)
    rows = generator_rows(field, generator, N)
    code_basis = row_basis(field, rows, N)
    dual_basis, dual = direct_dual_from_inner_product(
        field,
        code_basis,
        K_GALOIS,
        INVERSE_FROBENIUS_POWERS[component],
        N,
    )
    dual_basis = row_basis(field, dual_basis, N)

    # The direct defining equations and the principal inverse-Frobenius
    # reciprocal are checked independently for every component selection.
    predicted_check = normalized_galois_reciprocal(
        field,
        check,
        INVERSE_FROBENIUS_POWERS[component],
    )
    predicted_dual = span(
        field,
        generator_rows(field, predicted_check, N),
        N,
    )
    assert dual == predicted_dual
    assert all(
        galois_inner_product(field, codeword, candidate, K_GALOIS) == 0
        for codeword in code_basis
        for candidate in dual_basis
    )

    code_dimension = len(code_basis)
    dual_dimension = len(dual_basis)
    hull_dimension = (
        code_dimension
        + dual_dimension
        - matrix_rank(field, code_basis + dual_basis, N)
    )
    return {
        "generator": generator,
        "check": check,
        "code_basis": code_basis,
        "dual_basis": dual_basis,
        "code_dimension": code_dimension,
        "dual_dimension": dual_dimension,
        "hull_dimension": hull_dimension,
    }


def gf2_rref(matrix, columns):
    rows = [list(row) for row in matrix if any(row)]
    pivots = []
    pivot_row = 0
    for column in range(columns):
        selected = next(
            (row for row in range(pivot_row, len(rows)) if rows[row][column]),
            None,
        )
        if selected is None:
            continue
        rows[pivot_row], rows[selected] = rows[selected], rows[pivot_row]
        for row in range(len(rows)):
            if row != pivot_row and rows[row][column]:
                rows[row] = [
                    left ^ right
                    for left, right in zip(rows[row], rows[pivot_row])
                ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return [tuple(row) for row in rows], pivots


def gf2_rank(matrix, columns):
    return len(gf2_rref(matrix, columns)[1])


def gf2_row_basis(matrix, columns):
    rows, _ = gf2_rref(matrix, columns)
    return [row for row in rows if any(row)]


def gf2_nullspace(matrix, columns):
    rref, pivots = gf2_rref(matrix, columns)
    pivot_set = set(pivots)
    free_columns = [column for column in range(columns) if column not in pivot_set]
    basis = []
    for free in free_columns:
        vector = [0] * columns
        vector[free] = 1
        for row, pivot in enumerate(pivots):
            vector[pivot] = rref[row][free]
        basis.append(tuple(vector))
    return basis


def field_vector_bits(field, vector):
    """Flatten K^n into F_2^(n*[K:F_2])."""
    return tuple(
        (value >> bit) & 1
        for value in vector
        for bit in range(field.degree)
    )


def binary_basis_for_field_rows(field, rows, offset, total_columns):
    """Expand a K-basis into an F_2-basis in the global coordinates."""
    result = []
    for row in rows:
        for scalar in (1 << bit for bit in range(field.degree)):
            scaled = tuple(field.mul(scalar, value) for value in row)
            local = field_vector_bits(field, scaled)
            flat = [0] * total_columns
            flat[offset:offset + len(local)] = local
            result.append(tuple(flat))
    return result


def global_binary_basis_from_rows(component_bases):
    """Canonical binary basis for C_1 x C_2 or D_1 x D_2."""
    total_columns = N * sum(ABSOLUTE_DEGREES)
    offsets = (0, N * ABSOLUTE_DEGREES[0])
    rows = []
    for component in range(2):
        rows.extend(
            binary_basis_for_field_rows(
                FIELDS[component],
                component_bases[component],
                offsets[component],
                total_columns,
            )
        )
    return gf2_row_basis(rows, total_columns)


def global_pairing_equations(component_bases):
    """Build binary equations for <c,x>_{A,k}=0 from global code rows."""
    total_columns = N * sum(ABSOLUTE_DEGREES)
    offsets = (0, N * ABSOLUTE_DEGREES[0])
    equations = []

    for component in range(2):
        field = FIELDS[component]
        offset = offsets[component]
        for codeword in component_bases[component]:
            values = []
            for column in range(total_columns):
                if not (offset <= column < offset + N * field.degree):
                    values.append(0)
                    continue
                local = column - offset
                coordinate, bit = divmod(local, field.degree)
                candidate = [0] * N
                candidate[coordinate] = 1 << bit
                values.append(
                    galois_inner_product(
                        field,
                        codeword,
                        tuple(candidate),
                        K_GALOIS,
                    )
                )
            for output_bit in range(field.degree):
                equations.append([
                    (value >> output_bit) & 1
                    for value in values
                ])
    return equations, total_columns


def global_shift(field, vector, twist=1):
    return (field.mul(twist, vector[-1]),) + vector[:-1]


def row_space_contains(field, basis, vector):
    return matrix_rank(field, basis + [vector], N) == matrix_rank(field, basis, N)


def component_orbit_data(component):
    field = FIELDS[component]
    factors = FACTORS[component]
    reciprocal_power = INVERSE_FROBENIUS_POWERS[component]
    index = {factor: i for i, factor in enumerate(factors)}
    permutation = []
    for factor in factors:
        image = normalized_galois_reciprocal(
            field, factor, reciprocal_power
        )
        assert image in index
        permutation.append(index[image])

    visited = set()
    orbits = []
    for start in range(len(factors)):
        if start in visited:
            continue
        orbit = []
        current = start
        while current not in visited:
            visited.add(current)
            orbit.append(current)
            current = permutation[current]
        assert current == start
        orbits.append(orbit)

    weight_by_factor = {
        index: EXTENSION_DEGREES[component] * (len(factors[index]) - 1)
        for index in range(len(factors))
    }
    data = [
        (len(orbit), weight_by_factor[orbit[0]])
        for orbit in orbits
    ]
    return permutation, orbits, data


def polynomial_product(polynomials):
    result = Counter({(0, 0): 1})
    for polynomial in polynomials:
        next_result = Counter()
        for (dimension, hull), left_count in result.items():
            for (new_dimension, new_hull), right_count in polynomial.items():
                next_result[(dimension + new_dimension, hull + new_hull)] += (
                    left_count * right_count
                )
        result = next_result
    return result


def assert_product_algebra_and_pairing():
    """Exercise the tuple algebra and distinguish A-valued from traced pairings."""
    elements = list(product(range(F4.size), range(F16.size)))
    zero = A.zero()
    one = A.one()

    for left in elements:
        assert A.add(left, zero) == left
        assert A.mul(left, one) == left
        assert A.add(left, left) == zero
        assert A.frobenius(left, K_GALOIS) == (
            F4.frobenius(left[0], K_GALOIS),
            F16.frobenius(left[1], K_GALOIS),
        )
        for right in elements:
            assert A.add(left, right) == A.add(right, left)
            assert A.mul(left, right) == A.mul(right, left)
            assert A.frobenius(A.add(left, right), K_GALOIS) == A.add(
                A.frobenius(left, K_GALOIS),
                A.frobenius(right, K_GALOIS),
            )
            assert A.frobenius(A.mul(left, right), K_GALOIS) == A.mul(
                A.frobenius(left, K_GALOIS),
                A.frobenius(right, K_GALOIS),
            )

    e1 = ((1,) + (0,) * (N - 1), (0,) * N)
    e2 = ((0,) * N, (1,) + (0,) * (N - 1))
    assert A.pairing(e1, e1, K_GALOIS) == (1, 0)
    assert A.pairing(e2, e2, K_GALOIS) == (0, 1)
    assert A.pairing(e1, e2, K_GALOIS) == zero


def main():
    assert_product_algebra_and_pairing()

    assert product_polynomials(F4, F4_FACTORS) == COMPONENT_MODULI[0]
    assert product_polynomials(F16, F16_FACTORS) == COMPONENT_MODULI[1]
    for field, twist, inverse_power in zip(
        FIELDS, LAMBDA, INVERSE_FROBENIUS_POWERS
    ):
        assert twist != 0
        assert field.pow(
            twist, 1 + field.characteristic ** inverse_power
        ) == 1
    assert len(set(F4_FACTORS)) == len(F4_FACTORS)
    assert len(set(F16_FACTORS)) == len(F16_FACTORS)
    for factor in F4_FACTORS[1:]:
        assert all(
            evaluate_polynomial(F4, factor, value) != 0
            for value in range(F4.size)
        )

    orbit_data = []
    component_histograms = []
    component_cache = []
    for component in range(2):
        permutation, orbits, data = component_orbit_data(component)
        orbit_data.extend(data)
        assert sum(len(orbit) for orbit in orbits) == len(FACTORS[component])
        assert all(
            len({len(FACTORS[component][index]) for index in orbit}) == 1
            for orbit in orbits
        )
        component_cache.append([])
        histogram = Counter()
        for mask in range(1 << len(FACTORS[component])):
            info = component_data(component, mask)
            component_cache[component].append(info)
            histogram[
                (
                    EXTENSION_DEGREES[component] * info["code_dimension"],
                    EXTENSION_DEGREES[component] * info["hull_dimension"],
                )
            ] += 1

        boundary = boundary_global_polynomial(data)
        transfer = multiply_global_polynomials([
            transfer_orbit_polynomial(length, weight)
            for length, weight in data
        ])
        assert histogram == boundary
        assert boundary == transfer
        component_histograms.append(histogram)
        print(
            f"component {component + 1}: factors={len(FACTORS[component])}, "
            f"tau={permutation}, orbit-data={data}, histogram="
            f"{dict(sorted(histogram.items()))}"
        )

    direct_global_histogram = Counter()
    distinct_global_codes = set()
    global_dual_checks = 0
    global_hull_checks = 0
    global_shift_checks = 0

    for mask1 in range(1 << len(FACTORS[0])):
        for mask2 in range(1 << len(FACTORS[1])):
            infos = (component_cache[0][mask1], component_cache[1][mask2])
            code_bases = tuple(info["code_basis"] for info in infos)
            dual_bases = tuple(info["dual_basis"] for info in infos)

            code_binary = global_binary_basis_from_rows(code_bases)
            dual_binary_expected = global_binary_basis_from_rows(dual_bases)
            distinct_global_codes.add(tuple(code_binary))

            equations, total_columns = global_pairing_equations(code_bases)
            dual_binary_direct = gf2_row_basis(
                gf2_nullspace(equations, total_columns),
                total_columns,
            )
            assert dual_binary_direct == dual_binary_expected
            global_dual_checks += 1

            binary_code_dimension = len(code_binary)
            binary_dual_dimension = len(dual_binary_direct)
            binary_hull_dimension = (
                binary_code_dimension
                + binary_dual_dimension
                - gf2_rank(code_binary + dual_binary_direct, total_columns)
            )
            expected_code_dimension = sum(
                EXTENSION_DEGREES[component] * infos[component]["code_dimension"]
                for component in range(2)
            )
            expected_hull_dimension = sum(
                EXTENSION_DEGREES[component] * infos[component]["hull_dimension"]
                for component in range(2)
            )
            assert binary_code_dimension == BASE_FIELD_DEGREE * expected_code_dimension
            assert binary_hull_dimension == BASE_FIELD_DEGREE * expected_hull_dimension
            assert binary_code_dimension % BASE_FIELD_DEGREE == 0
            assert binary_hull_dimension % BASE_FIELD_DEGREE == 0
            code_dimension = binary_code_dimension // BASE_FIELD_DEGREE
            hull_dimension = binary_hull_dimension // BASE_FIELD_DEGREE
            global_hull_checks += 1
            direct_global_histogram[(code_dimension, hull_dimension)] += 1

            # Check the A-valued pairing on component-supported basis rows,
            # including the cross-component zero forced by the product.
            zero1, zero2 = ZERO_VECTORS
            for codeword in code_bases[0]:
                for candidate in dual_bases[0]:
                    assert A.pairing(
                        (codeword, zero2), (candidate, zero2), K_GALOIS
                    ) == (0, 0)
                for candidate in dual_bases[1]:
                    assert A.pairing(
                        (codeword, zero2), (zero1, candidate), K_GALOIS
                    ) == (0, 0)
            for codeword in code_bases[1]:
                for candidate in dual_bases[1]:
                    assert A.pairing(
                        (zero1, codeword), (zero1, candidate), K_GALOIS
                    ) == (0, 0)
                for candidate in dual_bases[0]:
                    assert A.pairing(
                        (zero1, codeword), (candidate, zero2), K_GALOIS
                    ) == (0, 0)

            # The component generator rows are closed under the global
            # lambda=(omega,1) shift, which is the affine-product module action.
            for component in range(2):
                field = FIELDS[component]
                for row in code_bases[component]:
                    assert row_space_contains(
                        field,
                        code_bases[component],
                        global_shift(field, row, LAMBDA[component]),
                    )
                global_shift_checks += len(code_bases[component])

    assert len(distinct_global_codes) == 256
    assert sum(direct_global_histogram.values()) == 256

    predicted_global_histogram = polynomial_product(component_histograms)
    assert direct_global_histogram == predicted_global_histogram

    orbit_histogram = boundary_global_polynomial(orbit_data)
    transfer_histogram = multiply_global_polynomials([
        transfer_orbit_polynomial(length, weight)
        for length, weight in orbit_data
    ])
    assert direct_global_histogram == orbit_histogram
    assert orbit_histogram == transfer_histogram
    assert sum(orbit_histogram.values()) == 256

    # Uniform selection moments, computed both from the exhaustive histogram
    # and from the stated orbit formulas.
    mean_from_histogram = sum(
        hull * count for (_, hull), count in direct_global_histogram.items()
    ) / 256
    second_from_histogram = sum(
        hull * hull * count
        for (_, hull), count in direct_global_histogram.items()
    ) / 256
    variance_from_histogram = second_from_histogram - mean_from_histogram ** 2
    mean_formula = sum(
        length * weight / 4
        for length, weight in orbit_data
        if length >= 2
    )
    variance_formula = sum(
        weight * weight / 4 if length == 2 else length * weight * weight / 16
        for length, weight in orbit_data
        if length >= 2
    )
    assert mean_from_histogram == mean_formula
    assert variance_from_histogram == variance_formula

    print("global product:")
    print("  A = F_4 x F_16 over F_4; n=5; lambda=(omega,1); k=1")
    print("  labeled selections:", 256)
    print("  distinct canonical global code spaces:", len(distinct_global_codes))
    print("  global dual nullspace checks:", global_dual_checks)
    print("  global F_4 dimension/hull checks:", global_hull_checks)
    print("  global shift checks on component bases:", global_shift_checks)
    print("  direct == component product:", direct_global_histogram == predicted_global_histogram)
    print("  direct == orbit boundary:", direct_global_histogram == orbit_histogram)
    print("  orbit boundary == transfer:", orbit_histogram == transfer_histogram)
    print("  joint histogram:", dict(sorted(direct_global_histogram.items())))
    print("  uniform mean:", mean_from_histogram)
    print("  uniform variance:", variance_from_histogram)
    print("PASS: exhaustive global-product and global-enumerator validation")


if __name__ == "__main__":
    main()
