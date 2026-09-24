"""Independent Phase-6 end-to-end validator.

The validator is intentionally standalone: it imports no production or earlier
Phase-2--5 checker.  It uses separate routes for

* direct code-first and candidate-first annihilators, direct intersections, and
  the restricted Gram matrix;
* factorization/reciprocal support and the weighted boundary statistic; and
* the full enumerator, computed once from every direct code and once from
  orbit transfer matrices.

All calculations are finite evidence only.  The theorem and its hypotheses
are recorded in PHASE6_FINAL_CONSOLIDATION_AUDIT.md.
"""

from itertools import product
from pathlib import Path


class GF2m:
    """Small binary extension fields represented by polynomial bit strings."""

    def __init__(self, degree, modulus):
        self.degree = degree
        self.modulus = modulus
        self.size = 1 << degree
        self.mask = self.size - 1

    def add(self, a, b):
        return a ^ b

    sub = add

    def mul(self, a, b):
        result = 0
        left = a
        right = b
        while right:
            if right & 1:
                result ^= left
            right >>= 1
            left <<= 1
            if left & self.size:
                left ^= self.modulus
        return result & self.mask

    def power(self, value, exponent):
        result = 1
        base = value
        while exponent:
            if exponent & 1:
                result = self.mul(result, base)
            base = self.mul(base, base)
            exponent >>= 1
        return result

    def inverse(self, value):
        if value == 0:
            raise ZeroDivisionError("zero has no inverse")
        return self.power(value, self.size - 2)

    def frobenius(self, value, iteration):
        return self.power(value, 1 << (iteration % self.degree))

    def neg(self, value):
        return value


def trim(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return tuple(poly)


def poly_mul(field, left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] ^= field.mul(a, b)
    return trim(result)


def poly_divmod(field, numerator, denominator):
    numerator = list(trim(numerator))
    denominator = trim(denominator)
    if denominator == (0,):
        raise ZeroDivisionError("polynomial division by zero")
    quotient = [0] * max(1, len(numerator) - len(denominator) + 1)
    while len(numerator) >= len(denominator) and any(numerator):
        coefficient = field.mul(
            numerator[-1], field.inverse(denominator[-1])
        )
        shift = len(numerator) - len(denominator)
        quotient[shift] = coefficient
        for i, value in enumerate(denominator):
            numerator[i + shift] ^= field.mul(coefficient, value)
        while len(numerator) > 1 and numerator[-1] == 0:
            numerator.pop()
    return trim(quotient), trim(numerator)


def monic(field, poly):
    poly = trim(poly)
    scale = field.inverse(poly[-1])
    return tuple(field.mul(scale, value) for value in poly)


def factor_poly(field, poly):
    """Factor a small polynomial by exhaustive monic-divisor search."""
    poly = monic(field, poly)
    degree = len(poly) - 1
    if degree <= 1:
        return [poly]
    for divisor_degree in range(1, degree // 2 + 1):
        for coefficients in product(
            range(field.size), repeat=divisor_degree
        ):
            if coefficients[0] == 0:
                continue
            divisor = tuple(coefficients) + (1,)
            quotient, remainder = poly_divmod(field, poly, divisor)
            if remainder == (0,):
                return factor_poly(field, divisor) + factor_poly(field, quotient)
    return [poly]


def poly_product(field, factors):
    result = (1,)
    for factor in factors:
        result = poly_mul(field, result, factor)
    return result


def reciprocal(field, poly, iteration):
    """Normalized Frobenius reciprocal with the stated slot exponent."""
    poly = monic(field, poly)
    degree = len(poly) - 1
    scale = field.inverse(field.frobenius(poly[0], iteration))
    result = [0] * (degree + 1)
    for index, coefficient in enumerate(poly):
        result[degree - index] = field.mul(
            scale, field.frobenius(coefficient, iteration)
        )
    return monic(field, result)


def rref(field, rows, columns):
    matrix = [list(row) for row in rows if any(row)]
    pivots = []
    pivot_row = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(pivot_row, len(matrix))
             if matrix[row][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        scale = field.inverse(matrix[pivot_row][column])
        matrix[pivot_row] = [
            field.mul(scale, value) for value in matrix[pivot_row]
        ]
        for row in range(len(matrix)):
            if row == pivot_row or matrix[row][column] == 0:
                continue
            scale = matrix[row][column]
            matrix[row] = [
                value ^ field.mul(scale, pivot_value)
                for value, pivot_value in zip(
                    matrix[row], matrix[pivot_row]
                )
            ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return [tuple(row) for row in matrix], pivots


def basis(field, rows, columns):
    reduced, _ = rref(field, rows, columns)
    return tuple(row for row in reduced if any(row))


def rank(field, rows, columns):
    return len(basis(field, rows, columns))


def nullspace(field, rows, columns):
    reduced, pivots = rref(field, rows, columns)
    pivot_set = set(pivots)
    free = [column for column in range(columns)
            if column not in pivot_set]
    result = []
    for free_column in free:
        vector = [0] * columns
        vector[free_column] = 1
        for row, pivot in zip(reduced, pivots):
            # In characteristic two, subtraction is addition.
            vector[pivot] = row[free_column]
        result.append(tuple(vector))
    return tuple(result)


def vector_add(left, right):
    return tuple(a ^ b for a, b in zip(left, right))


def vector_scale(field, scalar, vector):
    return tuple(field.mul(scalar, value) for value in vector)


def combination(field, coefficients, rows, columns):
    result = (0,) * columns
    for coefficient, row in zip(coefficients, rows):
        result = vector_add(result, vector_scale(field, coefficient, row))
    return result


def intersection(field, left, right, columns):
    """Compute span(left) ∩ span(right), independently of Gram matrices."""
    left = basis(field, left, columns)
    right = basis(field, right, columns)
    equations = []
    for column in range(columns):
        equations.append(
            [row[column] for row in left]
            + [row[column] for row in right]
        )
    coefficients = nullspace(field, equations, len(left) + len(right))
    common = [
        combination(field, vector[:len(left)], left, columns)
        for vector in coefficients
    ]
    return basis(field, common, columns)


def frobenius_rows(field, rows, iteration):
    return basis(
        field,
        [tuple(field.frobenius(value, iteration) for value in row)
         for row in rows],
        len(rows[0]) if rows else 0,
    )


def direct_code_first_dual(field, code, k, length):
    """Directly solve sum c_i sigma(x_i)=0, without a Gram matrix."""
    y_basis = nullspace(field, code, length)
    inverse_iteration = (field.degree - k) % field.degree
    candidates = [
        tuple(field.frobenius(value, inverse_iteration) for value in row)
        for row in y_basis
    ]
    result = basis(field, candidates, length)
    for x in result:
        assert all(
            sum_field(
                field.mul(c_i, field.frobenius(x_i, k))
                for c_i, x_i in zip(c, x)
            ) == 0
            for c in code
        )
    return result


def direct_candidate_first_dual(field, code, k, length):
    """Directly solve sum x_i sigma(c_i)=0 from its own equations."""
    sigma_code = [
        tuple(field.frobenius(value, k) for value in row)
        for row in code
    ]
    result = basis(field, nullspace(field, sigma_code, length), length)
    for x in result:
        assert all(
            sum_field(
                field.mul(x_i, field.frobenius(c_i, k))
                for x_i, c_i in zip(x, c)
            ) == 0
            for c in code
        )
    return result


def sum_field(values):
    result = 0
    for value in values:
        result ^= value
    return result


def gram_hull_dimension(field, code, k):
    """Restricted Gram route: nullity of B sigma(B)^T."""
    rows = len(code)
    if rows == 0:
        return 0
    gram = []
    sigma_code = [
        tuple(field.frobenius(value, k) for value in row)
        for row in code
    ]
    for left in code:
        gram.append([
            sum_field(field.mul(a, b) for a, b in zip(left, right))
            for right in sigma_code
        ])
    return rows - rank(field, gram, rows)


def direct_hull_dimension(field, code, dual, length):
    return len(intersection(field, code, dual, length))


def shift(field, vector, twist):
    return (field.mul(twist, vector[-1]),) + tuple(vector[:-1])


def constacyclic(field, code, twist, length):
    code = basis(field, code, length)
    return all(
        rank(field, list(code) + [shift(field, row, twist)], length)
        == len(code)
        for row in code
    )


def modulus(field, length, twist):
    result = [0] * (length + 1)
    result[0] = field.neg(twist)
    result[length] = 1
    return tuple(result)


def generator_rows(generator, length):
    degree = len(generator) - 1
    return tuple(
        tuple(
            generator[index - shift]
            if shift <= index < shift + len(generator) else 0
            for index in range(length)
        )
        for shift in range(length - degree)
    )


def factor_permutation(field, factors, iteration):
    permutation = []
    for factor in factors:
        image = reciprocal(field, factor, iteration)
        positions = [index for index, other in enumerate(factors)
                     if other == image]
        if len(positions) != 1:
            return None
        permutation.append(positions[0])
    return tuple(permutation)


def orbit_decomposition(permutation):
    unseen = set(range(len(permutation)))
    orbits = []
    while unseen:
        start = min(unseen)
        orbit = []
        current = start
        while current not in orbit:
            orbit.append(current)
            unseen.remove(current)
            current = permutation[current]
        orbits.append(tuple(orbit))
    return tuple(orbits)


def boundary(permutation, selected):
    selected = set(selected)
    return {
        permutation[index]
        for index in selected
        if permutation[index] not in selected
    }


def weighted(factors, support):
    return sum(len(factors[index]) - 1 for index in support)


def compatible(field, twist, k):
    return field.mul(twist, field.frobenius(twist, k)) == 1


def nontrivial_compatible(field, k):
    return next(
        (value for value in range(2, field.size)
         if compatible(field, value, k)),
        None,
    )


def nontrivial_incompatible(field, k):
    return next(
        (value for value in range(2, field.size)
         if not compatible(field, value, k)),
        None,
    )


def histogram_add(left, right):
    result = dict(left)
    for key, value in right.items():
        result[key] = result.get(key, 0) + value
    return {key: value for key, value in result.items() if value}


def histogram_mul(left, right):
    result = {}
    for (u0, z0), count0 in left.items():
        for (u1, z1), count1 in right.items():
            key = (u0 + u1, z0 + z1)
            result[key] = result.get(key, 0) + count0 * count1
    return result


def matrix_mul(left, right):
    result = [[{} for _ in range(2)] for __ in range(2)]
    for i in range(2):
        for j in range(2):
            value = {}
            for middle in range(2):
                value = histogram_add(
                    value, histogram_mul(left[i][middle], right[middle][j])
                )
            result[i][j] = value
    return result


def matrix_identity():
    one = {(0, 0): 1}
    zero = {}
    return [[one, zero], [zero, one]]


def matrix_power(matrix, exponent):
    result = matrix_identity()
    base = matrix
    while exponent:
        if exponent & 1:
            result = matrix_mul(result, base)
        base = matrix_mul(base, base)
        exponent >>= 1
    return result


def transfer_orbit(weight, length):
    return matrix_power(
        [[{(weight, 0): 1}, {(0, 0): 1}],
         [{(weight, weight): 1}, {(0, 0): 1}]],
        length,
    )


def transfer_enumerator(factors, permutation):
    result = {(0, 0): 1}
    for orbit in orbit_decomposition(permutation):
        orbit_weight = len(factors[orbit[0]]) - 1
        trace = histogram_add(
            transfer_orbit(orbit_weight, len(orbit))[0][0],
            transfer_orbit(orbit_weight, len(orbit))[1][1],
        )
        result = histogram_mul(result, trace)
    return result


def moments(histogram):
    total = sum(histogram.values())
    mean = sum(hull * count for (_, hull), count in histogram.items()) / total
    variance = sum(
        (hull - mean) ** 2 * count
        for (_, hull), count in histogram.items()
    ) / total
    return total, mean, variance


def unequal_weight_reversal_diagnostic():
    """Show why reversal is restricted to equal-weight Frobenius orbits."""
    weights = (1, 2, 4)
    bits = (1, 0, 0)
    forward = sum(
        weights[(index + 1) % 3]
        for index in range(3)
        if bits[index] and not bits[(index + 1) % 3]
    )
    reverse = sum(
        weights[(index - 1) % 3]
        for index in range(3)
        if bits[index] and not bits[(index - 1) % 3]
    )
    assert forward != reverse
    return forward, reverse


def evaluate_case(label, field, length, twist, k):
    modulus_poly = modulus(field, length, twist)
    factors = factor_poly(field, modulus_poly)
    assert len(set(factors)) == len(factors)
    assert poly_product(field, factors) == monic(field, modulus_poly)
    factor_count = len(factors)
    selection_count = 1 << factor_count
    rho_iteration = (field.degree - k) % field.degree
    sigma2_iteration = (2 * k) % field.degree
    same_factor_set = compatible(field, twist, k)
    rho_perm = factor_permutation(field, factors, rho_iteration)
    sigma_perm = factor_permutation(field, factors, k)
    if same_factor_set:
        assert rho_perm is not None and sigma_perm is not None
        assert sorted(rho_perm) == list(range(factor_count))
        assert sorted(sigma_perm) == list(range(factor_count))
        for index in range(factor_count):
            assert rho_perm[sigma_perm[index]] == index
            assert sigma_perm[rho_perm[index]] == index
    else:
        # The two reciprocal images are still valid factors of their own
        # transformed moduli, but are not entered into the same-family support
        # or transfer calculation.
        assert rho_perm is None or sigma_perm is None

    direct_enum = {}
    support_enum = {}
    candidate_enum = {}
    direct_hull_checks = 0
    gram_failures = 0
    convention_relation_failures = 0
    transformed_intersection_failures = 0
    reciprocal_failures = 0
    support_failures = 0
    dual_generator_failures = 0
    constacyclic_failures = 0
    distinct_generator_failures = 0
    first_difference = {}
    generators = set()
    code_first_twist = field.inverse(field.frobenius(twist, rho_iteration))
    candidate_first_twist = field.inverse(field.frobenius(twist, k))

    for mask in range(selection_count):
        selected = tuple(index for index in range(factor_count)
                         if mask & (1 << index))
        generator = poly_product(field, [factors[index] for index in selected])
        if generator in generators:
            distinct_generator_failures += 1
        generators.add(generator)
        check, remainder = poly_divmod(field, modulus_poly, generator)
        assert remainder == (0,)
        code = basis(field, generator_rows(generator, length), length)
        assert constacyclic(field, code, twist, length)
        code_dim = len(code)
        code_dual = direct_code_first_dual(field, code, k, length)
        candidate_dual = direct_candidate_first_dual(field, code, k, length)
        hull_basis = intersection(field, code, code_dual, length)
        candidate_hull_basis = intersection(
            field, code, candidate_dual, length
        )
        hull_dim = len(hull_basis)
        candidate_hull_dim = len(candidate_hull_basis)
        direct_hull_checks += 1
        if gram_hull_dimension(field, code, k) != hull_dim:
            gram_failures += 1
            first_difference.setdefault("gram", mask)
        transformed_code = frobenius_rows(field, code, sigma2_iteration)
        transformed_dual = frobenius_rows(
            field, code_dual, sigma2_iteration
        )
        if transformed_dual != candidate_dual:
            convention_relation_failures += 1
            first_difference.setdefault("dual_transform", mask)
        transformed_hull = frobenius_rows(field, hull_basis, sigma2_iteration)
        expected_hull = intersection(
            field, transformed_code, candidate_dual, length
        )
        if transformed_hull != expected_hull:
            transformed_intersection_failures += 1
            first_difference.setdefault("hull_transform", mask)
        if not constacyclic(
            field, transformed_code,
            field.frobenius(twist, sigma2_iteration), length
        ):
            constacyclic_failures += 1
        if candidate_hull_dim != hull_dim:
            first_difference.setdefault("hull_dimension", mask)
        if (candidate_hull_dim == 0) != (hull_dim == 0):
            first_difference.setdefault("lcd", mask)
        direct_enum[(code_dim, hull_dim)] = (
            direct_enum.get((code_dim, hull_dim), 0) + 1
        )
        candidate_enum[(code_dim, candidate_hull_dim)] = (
            candidate_enum.get((code_dim, candidate_hull_dim), 0) + 1
        )

        # The support route is deliberately separate from the direct hull.
        if same_factor_set:
            assert rho_perm is not None and sigma_perm is not None
            selected_set = set(selected)
            complement = set(range(factor_count)) - selected_set
            rho_dual_support = {
                rho_perm[index] for index in complement
            }
            sigma_dual_support = {
                sigma_perm[index] for index in complement
            }
            rho_hull_support = selected_set | rho_dual_support
            sigma_hull_support = selected_set | sigma_dual_support
            rho_boundary = boundary(rho_perm, selected)
            sigma_boundary = boundary(sigma_perm, selected)
            rho_weight = weighted(factors, rho_boundary)
            sigma_weight = weighted(factors, sigma_boundary)
            if rho_weight != hull_dim:
                support_failures += 1
                first_difference.setdefault("code_support", mask)
            if sigma_weight != candidate_hull_dim:
                support_failures += 1
                first_difference.setdefault("candidate_support", mask)
            if length - weighted(factors, rho_hull_support) != hull_dim:
                support_failures += 1
            if length - weighted(factors, sigma_hull_support) != candidate_hull_dim:
                support_failures += 1
            support_enum[(code_dim, rho_weight)] = (
                support_enum.get((code_dim, rho_weight), 0) + 1
            )
            rho_dual_generator = reciprocal(field, check, rho_iteration)
            sigma_dual_generator = reciprocal(field, check, k)
            rho_rows = basis(
                field, generator_rows(rho_dual_generator, length), length
            )
            sigma_rows = basis(
                field, generator_rows(sigma_dual_generator, length), length
            )
            if rho_rows != code_dual or sigma_rows != candidate_dual:
                dual_generator_failures += 1
            assert constacyclic(field, rho_rows, code_first_twist, length)
            assert constacyclic(
                field, sigma_rows, candidate_first_twist, length
            )

    assert len(generators) == selection_count
    assert distinct_generator_failures == 0
    assert direct_hull_checks == selection_count
    assert gram_failures == 0
    assert convention_relation_failures == 0
    assert transformed_intersection_failures == 0
    assert support_failures == 0
    assert dual_generator_failures == 0
    assert constacyclic_failures == 0
    assert direct_enum == candidate_enum
    if same_factor_set:
        assert direct_enum == support_enum
        transfer = transfer_enumerator(factors, rho_perm)
        assert direct_enum == transfer
        enum_route = "direct=support=transfer"
    else:
        transfer = None
        enum_route = "direct only; incompatible twist excluded from transfer"
    total, mean, variance = moments(direct_enum)
    print(
        f"{label}: factors={factor_count}, selections={selection_count}, "
        f"compatible={same_factor_set}, direct_hull_checks={direct_hull_checks}, "
        f"gram_failures={gram_failures}, relation_failures="
        f"{convention_relation_failures}, support_failures={support_failures}, "
        f"dual_generator_failures={dual_generator_failures}, "
        f"hull_dimension_distribution={tuple(sorted(direct_enum.items()))}, "
        f"mean={mean:.12g}, variance={variance:.12g}, "
        f"enumerator_route={enum_route}"
    )
    if first_difference:
        print(f"{label}: unexpected_differences={first_difference}")
    return {
        "compatible": same_factor_set,
        "direct_enum": direct_enum,
        "mean": mean,
        "variance": variance,
    }


def cases():
    fields = (
        ("F4", GF2m(2, 0b111), 3),
        ("F8", GF2m(3, 0b1011), 7),
        ("F16", GF2m(4, 0b10011), 5),
    )
    result = []
    for name, field, length in fields:
        result.append((f"{name} lambda=1 k=0", field, length, 1, 0))
        for k in range(1, field.degree):
            result.append((f"{name} lambda=1 k={k}", field, length, 1, k))
            compatible_twist = nontrivial_compatible(field, k)
            if compatible_twist is not None:
                result.append((
                    f"{name} compatible nontrivial k={k}",
                    field, 3, compatible_twist, k,
                ))
            incompatible_twist = nontrivial_incompatible(field, k)
            if incompatible_twist is not None:
                result.append((
                    f"{name} incompatible nontrivial k={k}",
                    field, 3, incompatible_twist, k,
                ))
    return result


def arbitrary_f8_plane_check():
    """Check all 2-planes of F8^3 by their normalized linear functional."""
    field = GF2m(3, 0b1011)
    checked = 0
    gram_failures = 0
    relation_failures = 0
    lcd_failures = 0
    for first_nonzero in range(3):
        prefix = (0,) * first_nonzero + (1,)
        for suffix in product(range(field.size), repeat=2 - first_nonzero):
            normal = prefix + suffix
            code = basis(field, nullspace(field, [normal], 3), 3)
            assert len(code) == 2
            dual = direct_code_first_dual(field, code, 1, 3)
            candidate = direct_candidate_first_dual(field, code, 1, 3)
            direct_dimension = len(intersection(field, code, dual, 3))
            if direct_dimension != gram_hull_dimension(field, code, 1):
                gram_failures += 1
            if frobenius_rows(field, dual, 2) != candidate:
                relation_failures += 1
            candidate_dimension = len(intersection(field, code, candidate, 3))
            if (direct_dimension == 0) != (candidate_dimension == 0):
                lcd_failures += 1
            checked += 1
    print(
        f"arbitrary F8^3 rank-2 planes: checked={checked}, "
        f"gram_failures={gram_failures}, relation_failures={relation_failures}, "
        f"lcd_failures={lcd_failures}"
    )
    assert checked == 73
    assert gram_failures == relation_failures == lcd_failures == 0


def main():
    results = [evaluate_case(*case) for case in cases()]
    arbitrary_f8_plane_check()
    forward, reverse = unequal_weight_reversal_diagnostic()
    print(
        "unequal-weight reversal diagnostic: "
        f"forward={forward}, reverse={reverse}; "
        "not claimed invariant"
    )
    assert len(results) >= 12
    assert any(result["compatible"] for result in results)
    assert any(not result["compatible"] for result in results)
    print("PHASE6 END-TO-END CHECK: PASS")
    print(
        "Independent routes agree: direct annihilator/intersection, "
        "restricted Gram hull dimension, reciprocal boundary support, and "
        "orbit transfer enumerator."
    )


if __name__ == "__main__":
    main()
