"""Phase-5 independent convention/invariance search.

This is a fresh implementation.  It does not import Phase-4 or Phase-3 code.
The code-first and candidate-first duals are solved separately from their
annihilator equations.  The search exhausts the factor selections of the
listed small constacyclic moduli and samples arbitrary linear codes to look
for hull-dimension or LCD counterexamples.

The output is finite evidence only.  The general hull-dimension/LCD statement
is proved in validation/PHASE5_CONVENTION_INVARIANCE_AUDIT.md by a restricted
Gram-matrix argument; this program does not replace that proof.
"""

from itertools import product
import random


class BinaryField:
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
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def multiply_poly(field, left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            result[i + j] ^= field.mul(left_value, right_value)
    return trim(result)


def divide_poly(field, numerator, denominator):
    remainder = list(trim(numerator))
    denominator = trim(denominator)
    if denominator == (0,):
        raise ZeroDivisionError("polynomial division by zero")
    quotient = [0] * max(1, len(remainder) - len(denominator) + 1)
    while len(remainder) >= len(denominator) and any(remainder):
        coefficient = field.mul(remainder[-1], field.inverse(denominator[-1]))
        shift = len(remainder) - len(denominator)
        quotient[shift] = coefficient
        for i, value in enumerate(denominator):
            remainder[i + shift] ^= field.mul(coefficient, value)
        while len(remainder) > 1 and remainder[-1] == 0:
            remainder.pop()
    return trim(quotient), trim(remainder)


def monic(field, poly):
    poly = trim(poly)
    scale = field.inverse(poly[-1])
    return tuple(field.mul(scale, value) for value in poly)


def factor_small(field, polynomial):
    polynomial = monic(field, polynomial)
    degree = len(polynomial) - 1
    if degree <= 1:
        return [polynomial]
    for divisor_degree in range(1, degree // 2 + 1):
        for coefficients in product(range(field.size), repeat=divisor_degree):
            if coefficients[0] == 0:
                continue
            divisor = tuple(coefficients) + (1,)
            quotient, remainder = divide_poly(field, polynomial, divisor)
            if remainder == (0,):
                return factor_small(field, divisor) + factor_small(field, quotient)
    return [polynomial]


def product_poly(field, factors):
    result = (1,)
    for factor in factors:
        result = multiply_poly(field, result, factor)
    return result


def reciprocal(field, polynomial, iteration):
    polynomial = monic(field, polynomial)
    degree = len(polynomial) - 1
    scale = field.inverse(field.frobenius(polynomial[0], iteration))
    result = [0] * (degree + 1)
    for index, coefficient in enumerate(polynomial):
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
                for value, pivot_value in zip(matrix[row], matrix[pivot_row])
            ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return [tuple(row) for row in matrix], pivots


def row_basis(field, rows, columns):
    reduced, _ = rref(field, rows, columns)
    return tuple(row for row in reduced if any(row))


def rank(field, rows, columns):
    return len(row_basis(field, rows, columns))


def nullspace(field, rows, columns):
    reduced, pivots = rref(field, rows, columns)
    pivot_set = set(pivots)
    free_columns = [column for column in range(columns)
                    if column not in pivot_set]
    result = []
    for free_column in free_columns:
        vector = [0] * columns
        vector[free_column] = 1
        for row, pivot in zip(reduced, pivots):
            vector[pivot] = row[free_column]
        result.append(tuple(vector))
    return tuple(result)


def field_sum(values):
    result = 0
    for value in values:
        result ^= value
    return result


def scalar_vector(field, scalar, vector):
    return tuple(field.mul(scalar, value) for value in vector)


def add_vectors(field, left, right):
    return tuple(a ^ b for a, b in zip(left, right))


def linear_combination(field, coefficients, rows, columns):
    result = (0,) * columns
    for coefficient, row in zip(coefficients, rows):
        result = add_vectors(field, result, scalar_vector(field, coefficient, row))
    return result


def intersection_basis(field, left, right, columns):
    """Return a basis for span(left) intersect span(right)."""
    left = row_basis(field, left, columns)
    right = row_basis(field, right, columns)
    variables = len(left) + len(right)
    equations = []
    for column in range(columns):
        equations.append(
            [row[column] for row in left]
            + [field.neg(row[column]) for row in right]
        )
    coefficients = nullspace(field, equations, variables)
    common = []
    for coefficient_vector in coefficients:
        common.append(
            linear_combination(field, coefficient_vector[:len(left)], left,
                               columns)
        )
    return row_basis(field, common, columns)


def transform_rows(field, rows, iteration):
    return row_basis(
        field,
        [tuple(field.frobenius(value, iteration) for value in row)
         for row in rows],
        len(rows[0]) if rows else 0,
    )


def direct_code_first_dual(field, code_rows, sigma_iteration, length):
    """Solve sum_i c_i sigma(x_i)=0 from the code-first equations."""
    # Put y_i=sigma(x_i), solve the ordinary equations sum_i c_i y_i=0,
    # then apply the explicitly computed inverse Frobenius to every solution.
    y_nullspace = nullspace(field, code_rows, length)
    rho_iteration = field.degree - sigma_iteration
    candidates = [
        tuple(field.frobenius(value, rho_iteration) for value in row)
        for row in y_nullspace
    ]
    result = row_basis(field, candidates, length)
    for candidate in result:
        assert all(
            field_sum(field.mul(c_i, field.frobenius(x_i, sigma_iteration))
                      for c_i, x_i in zip(code, candidate)) == 0
            for code in code_rows
        )
    return result


def direct_candidate_first_dual(field, code_rows, sigma_iteration, length):
    """Solve sum_i x_i sigma(c_i)=0 independently from candidate equations."""
    sigma_code = [
        tuple(field.frobenius(value, sigma_iteration) for value in row)
        for row in code_rows
    ]
    result = row_basis(field, nullspace(field, sigma_code, length), length)
    for candidate in result:
        assert all(
            field_sum(field.mul(x_i, field.frobenius(c_i, sigma_iteration))
                      for x_i, c_i in zip(candidate, code)) == 0
            for code in code_rows
        )
    return result


def hull_dimension(field, code, dual, length):
    return (len(row_basis(field, code, length))
            + len(row_basis(field, dual, length))
            - rank(field, list(code) + list(dual), length))


def hull_basis(field, code, dual, length):
    return intersection_basis(field, code, dual, length)


def shifted(field, vector, twist):
    return (field.mul(twist, vector[-1]),) + tuple(vector[:-1])


def is_constacyclic(field, code, twist, length):
    basis = row_basis(field, code, length)
    return all(
        rank(field, list(basis), length)
        == rank(field, list(basis) + [shifted(field, row, twist)], length)
        for row in basis
    )


def modulus(field, length, twist):
    result = [0] * (length + 1)
    result[0] = field.neg(twist)
    result[length] = 1
    return tuple(result)


def generator_rows(generator, length):
    degree = len(generator) - 1
    return tuple(
        tuple(generator[index - shift]
              if shift <= index < shift + len(generator) else 0
              for index in range(length))
        for shift in range(length - degree)
    )


def inverse_power(field, value, iteration):
    return field.inverse(field.frobenius(value, iteration))


def factor_permutation(field, factors, iteration):
    result = []
    for factor in factors:
        image = reciprocal(field, factor, iteration)
        matches = [index for index, other in enumerate(factors)
                   if other == image]
        if len(matches) != 1:
            return None
        result.append(matches[0])
    return tuple(result)


def support_boundary(permutation, selected):
    selected = set(selected)
    return {
        permutation[index]
        for index in selected
        if permutation[index] not in selected
    }


def weighted_support(factors, support):
    return sum(len(factors[index]) - 1 for index in support)


def compatible(field, twist, k):
    return field.mul(twist, field.frobenius(twist, k)) == 1


def choose_nontrivial_compatible(field, k):
    for value in range(2, field.size):
        if compatible(field, value, k):
            return value
    return None


def choose_incompatible(field, k):
    for value in range(2, field.size):
        if not compatible(field, value, k):
            return value
    return None


def tuple_histogram(counter):
    return tuple(sorted(counter.items()))


def evaluate_case(label, field, length, twist, k):
    rho_iteration = field.degree - k
    factors = factor_small(field, modulus(field, length, twist))
    assert product_poly(field, factors) == monic(
        field, modulus(field, length, twist)
    )
    selections = 1 << len(factors)
    sigma_perm = factor_permutation(field, factors, k)
    rho_perm = factor_permutation(field, factors, rho_iteration)
    same_factor_set = (
        compatible(field, twist, k)
        and sigma_perm is not None
        and rho_perm is not None
    )
    if same_factor_set:
        assert sorted(sigma_perm) == list(range(len(factors)))
        assert sorted(rho_perm) == list(range(len(factors)))

    dual_difference = 0
    relation_failures = 0
    hull_difference = 0
    lcd_difference = 0
    support_difference = 0
    dual_support_difference = 0
    hull_generator_support_difference = 0
    support_weight_failures = 0
    reciprocal_failures = 0
    permutation_failures = 0
    constacyclic_failures = 0
    twist_transform_failures = 0
    frobenius_noninvariant = 0
    hull_subspace_difference = 0
    code_hist = {}
    candidate_hist = {}
    code_dim_hist = {}
    candidate_dim_hist = {}
    code_lcd = 0
    candidate_lcd = 0
    first_examples = {}
    code_twist = inverse_power(field, twist, rho_iteration)
    candidate_twist = inverse_power(field, twist, k)
    transformed_twist = field.frobenius(code_twist, 2 * k)
    if transformed_twist != candidate_twist:
        twist_transform_failures += 1

    for mask in range(selections):
        selected = tuple(index for index in range(len(factors))
                         if mask & (1 << index))
        generator = product_poly(field, [factors[index] for index in selected])
        code = row_basis(field, generator_rows(generator, length), length)
        assert is_constacyclic(field, code, twist, length)
        transformed_code = transform_rows(field, code, 2 * k)
        transformed_lambda = field.frobenius(twist, 2 * k)
        if not is_constacyclic(field, transformed_code,
                               transformed_lambda, length):
            constacyclic_failures += 1
        if transformed_code != code:
            frobenius_noninvariant += 1
            first_examples.setdefault("frobenius_noninvariant", mask)

        code_dual = direct_code_first_dual(field, code, k, length)
        candidate_dual = direct_candidate_first_dual(field, code, k, length)
        transformed_dual = transform_rows(field, code_dual, 2 * k)
        if transformed_dual != candidate_dual:
            relation_failures += 1
        if code_dual != candidate_dual:
            dual_difference += 1
            first_examples.setdefault("dual_difference", mask)

        h_code = hull_dimension(field, code, code_dual, length)
        h_candidate = hull_dimension(field, code, candidate_dual, length)
        if h_code != h_candidate:
            hull_difference += 1
            first_examples.setdefault("hull_difference", mask)
        code_lcd_flag = h_code == 0
        candidate_lcd_flag = h_candidate == 0
        code_lcd += code_lcd_flag
        candidate_lcd += candidate_lcd_flag
        if code_lcd_flag != candidate_lcd_flag:
            lcd_difference += 1
            first_examples.setdefault("lcd_difference", mask)
        code_dimension = len(code)
        code_dim_hist[code_dimension] = code_dim_hist.get(code_dimension, 0) + 1
        candidate_dim_hist[code_dimension] = (
            candidate_dim_hist.get(code_dimension, 0) + 1
        )
        code_hist[(code_dimension, h_code)] = (
            code_hist.get((code_dimension, h_code), 0) + 1
        )
        candidate_hist[(code_dimension, h_candidate)] = (
            candidate_hist.get((code_dimension, h_candidate), 0) + 1
        )

        h_code_basis = hull_basis(field, code, code_dual, length)
        h_candidate_basis = hull_basis(field, code, candidate_dual, length)
        if h_code_basis != h_candidate_basis:
            hull_subspace_difference += 1
            first_examples.setdefault("hull_subspace_difference", mask)
        transformed_hull = transform_rows(field, h_code_basis, 2 * k)
        expected_hull = intersection_basis(
            field, transformed_code, candidate_dual, length
        )
        if transformed_hull != expected_hull:
            raise AssertionError("intersection transformation identity failed")

        if not is_constacyclic(field, code_dual, code_twist, length):
            raise AssertionError("code-first predicted twist failed")
        if not is_constacyclic(field, candidate_dual, candidate_twist, length):
            raise AssertionError("candidate-first predicted twist failed")

        if same_factor_set:
            selected_set = set(selected)
            complement = set(range(len(factors))) - selected_set
            cf_dual_support = {rho_perm[index] for index in complement}
            candidate_dual_support = {
                sigma_perm[index] for index in complement
            }
            if cf_dual_support != candidate_dual_support:
                dual_support_difference += 1
                first_examples.setdefault("dual_support_difference", mask)
            cf_hull_generator_support = selected_set | cf_dual_support
            candidate_hull_generator_support = (
                selected_set | candidate_dual_support
            )
            if cf_hull_generator_support != candidate_hull_generator_support:
                hull_generator_support_difference += 1
                first_examples.setdefault("hull_generator_support_difference", mask)
            cf_support = support_boundary(rho_perm, selected)
            candidate_support = support_boundary(sigma_perm, selected)
            if cf_support != candidate_support:
                support_difference += 1
                first_examples.setdefault("support_difference", mask)
            if weighted_support(factors, cf_support) != h_code:
                support_weight_failures += 1
            if weighted_support(factors, candidate_support) != h_candidate:
                support_weight_failures += 1

            check = divide_poly(field, modulus(field, length, twist), generator)[0]
            rho_generator = reciprocal(field, check, rho_iteration)
            sigma_generator = reciprocal(field, check, k)
            rho_rows = row_basis(field, generator_rows(rho_generator, length),
                                 length)
            sigma_rows = row_basis(field, generator_rows(sigma_generator, length),
                                   length)
            if rho_rows != code_dual or sigma_rows != candidate_dual:
                raise AssertionError("reciprocal did not match direct dual")

        for factor in factors:
            rho_then_sigma = reciprocal(
                field, reciprocal(field, factor, rho_iteration), k
            )
            sigma_then_rho = reciprocal(
                field, reciprocal(field, factor, k), rho_iteration
            )
            if rho_then_sigma != factor or sigma_then_rho != factor:
                reciprocal_failures += 1
                break

    if same_factor_set:
        assert sigma_perm is not None and rho_perm is not None
        for index in range(len(factors)):
            if (sigma_perm[rho_perm[index]] != index
                    or rho_perm[sigma_perm[index]] != index):
                permutation_failures += 1
        assert code_hist == candidate_hist or hull_difference == 0

    assert relation_failures == 0
    assert hull_difference == 0
    assert lcd_difference == 0
    assert support_weight_failures == 0
    assert reciprocal_failures == 0
    assert constacyclic_failures == 0
    assert twist_transform_failures == 0
    assert code_hist == candidate_hist
    assert code_dim_hist == candidate_dim_hist
    assert code_lcd == candidate_lcd

    mean_numerator = sum(h * count for (d, h), count in code_hist.items())
    total = sum(code_hist.values())
    mean = mean_numerator / total
    variance = sum((h - mean) ** 2 * count
                   for (d, h), count in code_hist.items()) / total
    print(
        f"{label}: factors={len(factors)}, selections={selections}, "
        f"compatible={compatible(field, twist, k)}, "
        f"dual_differences={dual_difference}, relation_failures={relation_failures}, "
        f"hull_dimension_differences={hull_difference}, "
        f"lcd_differences={lcd_difference}, code_lcd={code_lcd}, "
        f"candidate_lcd={candidate_lcd}, "
        f"dual_support_differences={dual_support_difference}, "
        f"hull_generator_support_differences={hull_generator_support_difference}, "
        f"support_differences={support_difference}, "
        f"frobenius_noninvariant={frobenius_noninvariant}, "
        f"hull_subspace_differences={hull_subspace_difference}, "
        f"tau_inverse_failures={permutation_failures}, "
        f"mean={mean:.12g}, variance={variance:.12g}"
    )
    if first_examples:
        print(f"{label}: first_examples={first_examples}")
    if same_factor_set:
        print(
            f"{label}: sigma_perm={sigma_perm}, rho_perm={rho_perm}, "
            f"support_comparison=available"
        )
    else:
        print(f"{label}: support_comparison=not_applicable_for_incompatible_twist")
    return {
        "label": label,
        "selections": selections,
        "compatible": compatible(field, twist, k),
        "dual_differences": dual_difference,
        "hull_differences": hull_difference,
        "lcd_differences": lcd_difference,
        "dual_support_differences": dual_support_difference,
        "hull_generator_support_differences": hull_generator_support_difference,
        "support_differences": support_difference,
        "frobenius_noninvariant": frobenius_noninvariant,
        "hull_subspace_differences": hull_subspace_difference,
        "histogram": tuple_histogram(code_hist),
        "mean": mean,
        "variance": variance,
    }


def generic_code_search():
    """Search arbitrary F8^3 codes for a hull or LCD counterexample."""
    field = BinaryField(3, 0b1011)
    random_source = random.Random(20260924)
    hull_failures = 0
    lcd_failures = 0
    relation_failures = 0
    sampled = 0
    for _ in range(1200):
        rows = [[random_source.randrange(field.size) for _ in range(3)]
                for __ in range(2)]
        code = row_basis(field, rows, 3)
        if len(code) != 2:
            continue
        sampled += 1
        code_dual = direct_code_first_dual(field, code, 1, 3)
        candidate_dual = direct_candidate_first_dual(field, code, 1, 3)
        if transform_rows(field, code_dual, 2) != candidate_dual:
            relation_failures += 1
        h_code = hull_dimension(field, code, code_dual, 3)
        h_candidate = hull_dimension(field, code, candidate_dual, 3)
        if h_code != h_candidate:
            hull_failures += 1
        if (h_code == 0) != (h_candidate == 0):
            lcd_failures += 1
    print(
        f"arbitrary F8^3 rank-2 sample: sampled={sampled}, "
        f"hull_dimension_counterexamples={hull_failures}, "
        f"lcd_counterexamples={lcd_failures}, relation_failures={relation_failures}"
    )
    return sampled, hull_failures, lcd_failures, relation_failures


def build_cases():
    fields = [
        ("F4", BinaryField(2, 0b111), 3),
        ("F8", BinaryField(3, 0b1011), 7),
        ("F16", BinaryField(4, 0b10011), 5),
    ]
    cases = []
    for name, field, length in fields:
        cases.append((f"{name} k=0 lambda=1", field, length, 1, 0))
        for k in range(1, field.degree):
            cases.append((f"{name} k={k} lambda=1", field, length, 1, k))
            compatible_value = choose_nontrivial_compatible(field, k)
            if compatible_value is not None:
                cases.append((
                    f"{name} k={k} compatible-nontrivial",
                    field, 3, compatible_value, k,
                ))
            incompatible_value = choose_incompatible(field, k)
            if incompatible_value is not None:
                cases.append((
                    f"{name} k={k} incompatible",
                    field, 3, incompatible_value, k,
                ))
    return cases


def main():
    results = []
    for case in build_cases():
        results.append(evaluate_case(*case))
    sampled, hull_failures, lcd_failures, relation_failures = generic_code_search()
    assert hull_failures == 0
    assert lcd_failures == 0
    assert relation_failures == 0
    assert sampled > 0
    assert any(result["dual_differences"] > 0 for result in results)
    assert any(result["frobenius_noninvariant"] > 0 for result in results)
    assert any(result["support_differences"] > 0 for result in results)
    assert all(result["hull_differences"] == 0 for result in results)
    assert all(result["lcd_differences"] == 0 for result in results)
    print("PHASE5 CONVENTION COUNTEREXAMPLE SEARCH: PASS (finite evidence only)")


if __name__ == "__main__":
    main()
