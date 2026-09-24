"""Independent Phase-4 comparison of candidate-first and code-first duals.

This file intentionally does not import the Phase-3 checker or any existing
validator.  It implements its own characteristic-two field arithmetic,
polynomial factorization, row reduction, two direct dual definitions, hulls,
reciprocal maps, factor supports, and constacyclic twist tests.

The two duals compared for a code C are:

  code-first:     D_cf(C) = {x : sum_i c_i sigma(x_i)=0 for every c in C}
  candidate-first:D_cand(C) = {x : sum_i x_i sigma(c_i)=0 for every c in C}

The second definition is the literal convention displayed in the accessible
source preprint arXiv:2412.08512, Section 2.2.  Results are finite evidence
for the convention derivation; they are not a general theorem proof.
"""

from collections import Counter
from itertools import product


class Field:
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
            raise ZeroDivisionError("zero is not invertible")
        return self.power(value, self.size - 2)

    def quotient(self, numerator, denominator):
        return self.mul(numerator, self.inverse(denominator))

    def frobenius(self, value, iteration):
        return self.power(value, 1 << (iteration % self.degree))


def trim(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return tuple(poly)


def add_poly(field, left, right):
    size = max(len(left), len(right))
    return trim(tuple(
        field.add(left[i] if i < len(left) else 0,
                  right[i] if i < len(right) else 0)
        for i in range(size)
    ))


def multiply_poly(field, left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] = field.add(result[i + j], field.mul(a, b))
    return trim(result)


def divide_poly(field, numerator, denominator):
    numerator = list(trim(numerator))
    denominator = trim(denominator)
    if denominator == (0,):
        raise ZeroDivisionError("polynomial division by zero")
    quotient = [0] * max(1, len(numerator) - len(denominator) + 1)
    while len(numerator) >= len(denominator) and any(numerator):
        coefficient = field.quotient(numerator[-1], denominator[-1])
        shift = len(numerator) - len(denominator)
        quotient[shift] = coefficient
        for i, value in enumerate(denominator):
            numerator[i + shift] = field.sub(
                numerator[i + shift], field.mul(coefficient, value)
            )
        while len(numerator) > 1 and numerator[-1] == 0:
            numerator.pop()
    return trim(quotient), trim(numerator)


def monic(field, poly):
    poly = trim(poly)
    return tuple(field.mul(value, field.inverse(poly[-1])) for value in poly)


def product_poly(field, factors):
    result = (1,)
    for factor in factors:
        result = multiply_poly(field, result, factor)
    return result


def factor_small(field, polynomial):
    """Factor the small square-free test moduli by monic divisor search."""
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


def reciprocal(field, polynomial, iteration):
    polynomial = monic(field, polynomial)
    degree = len(polynomial) - 1
    constant_image = field.frobenius(polynomial[0], iteration)
    scale = field.inverse(constant_image)
    result = [0] * (degree + 1)
    for i, coefficient in enumerate(polynomial):
        result[degree - i] = field.mul(
            scale, field.frobenius(coefficient, iteration)
        )
    return monic(field, result)


def rref(field, rows, columns):
    matrix = [list(row) for row in rows if any(row)]
    pivots = []
    pivot_row = 0
    for column in range(columns):
        candidate = next(
            (r for r in range(pivot_row, len(matrix)) if matrix[r][column]),
            None,
        )
        if candidate is None:
            continue
        matrix[pivot_row], matrix[candidate] = matrix[candidate], matrix[pivot_row]
        scale = field.inverse(matrix[pivot_row][column])
        matrix[pivot_row] = [field.mul(scale, value) for value in matrix[pivot_row]]
        for r in range(len(matrix)):
            if r == pivot_row or matrix[r][column] == 0:
                continue
            scale = matrix[r][column]
            matrix[r] = [
                field.sub(value, field.mul(scale, pivot))
                for value, pivot in zip(matrix[r], matrix[pivot_row])
            ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return [tuple(row) for row in matrix], pivots


def row_basis(field, rows, columns):
    reduced, _ = rref(field, rows, columns)
    return tuple(row for row in reduced if any(row))


def nullspace(field, rows, columns):
    reduced, pivots = rref(field, rows, columns)
    pivot_set = set(pivots)
    free = [i for i in range(columns) if i not in pivot_set]
    basis = []
    for free_column in free:
        vector = [0] * columns
        vector[free_column] = 1
        for row, pivot in zip(reduced, pivots):
            vector[pivot] = row[free_column]
        basis.append(tuple(vector))
    return tuple(basis)


def rank(field, rows, columns):
    return len(row_basis(field, rows, columns))


def generator_rows(generator, length):
    degree = len(generator) - 1
    return tuple(
        tuple(
            generator[i - shift] if shift <= i < shift + len(generator) else 0
            for i in range(length)
        )
        for shift in range(length - degree)
    )


def coordinate_frobenius(field, rows, iteration):
    return [
        tuple(field.frobenius(value, iteration) for value in row)
        for row in rows
    ]


def code_first_dual(field, code_rows, sigma_iteration, rho_iteration, length):
    """Directly solve <c,x>=sum c_i sigma(x_i)=0."""
    transformed_candidate = nullspace(field, code_rows, length)
    return row_basis(
        field,
        [
            tuple(field.frobenius(value, rho_iteration) for value in row)
            for row in transformed_candidate
        ],
        length,
    )


def candidate_first_dual(field, code_rows, sigma_iteration, length):
    """Directly solve <x,c>=sum x_i sigma(c_i)=0."""
    sigma_code_rows = coordinate_frobenius(field, code_rows, sigma_iteration)
    return row_basis(field, nullspace(field, sigma_code_rows, length), length)


def hull_dimension(field, code_rows, dual_rows, length):
    return (
        rank(field, code_rows, length)
        + rank(field, dual_rows, length)
        - rank(field, list(code_rows) + list(dual_rows), length)
    )


def in_span(field, vector, rows, length):
    return rank(field, list(rows), length) == rank(
        field, list(rows) + [vector], length
    )


def shift_vector(field, vector, twist):
    return (field.mul(twist, vector[-1]),) + tuple(vector[:-1])


def is_constacyclic(field, rows, twist, length):
    basis = row_basis(field, rows, length)
    return all(in_span(field, shift_vector(field, row, twist), basis, length)
               for row in basis)


def inverse_power(field, value, iteration):
    return field.inverse(field.frobenius(value, iteration))


def modulus_for(field, length, twist):
    coefficients = [0] * (length + 1)
    coefficients[0] = field.sub(0, twist)
    coefficients[length] = 1
    return tuple(coefficients)


def factor_permutation(field, factors, iteration):
    permutation = []
    for factor in factors:
        image = reciprocal(field, factor, iteration)
        matches = [i for i, candidate in enumerate(factors) if candidate == image]
        assert len(matches) == 1, (factor, image, matches)
        permutation.append(matches[0])
    return tuple(permutation)


def support_for(permutation, selected):
    chosen = set(selected)
    return {
        permutation[index]
        for index in chosen
        if permutation[index] not in chosen
    }


def evaluate_case(label, field, length, twist, k, same_factor_set=True):
    total_degree = field.degree
    rho_iteration = total_degree - k
    modulus = modulus_for(field, length, twist)
    factors = factor_small(field, modulus)
    assert product_poly(field, factors) == monic(field, modulus)
    assert len(set(factors)) == len(factors)
    if same_factor_set:
        sigma_permutation = factor_permutation(field, factors, k)
        rho_permutation = factor_permutation(field, factors, rho_iteration)
        assert sorted(sigma_permutation) == list(range(len(factors)))
        assert sorted(rho_permutation) == list(range(len(factors)))
    else:
        sigma_permutation = None
        rho_permutation = None

    dual_differences = 0
    hull_dimension_differences = 0
    candidate_sigma_generator_agreements = 0
    candidate_rho_generator_agreements = 0
    candidate_twist_checks = 0
    code_twist_checks = 0
    factor_support_differences = 0
    lcd_criterion_differences = 0
    code_lcd_count = 0
    candidate_lcd_count = 0
    rows_by_mask = {}

    for mask in range(1 << len(factors)):
        selected = tuple(i for i in range(len(factors)) if mask & (1 << i))
        generator = product_poly(field, [factors[i] for i in selected])
        code_rows = generator_rows(generator, length)
        rows_by_mask[mask] = row_basis(field, code_rows, length)
        code_dual = code_first_dual(
            field, code_rows, k, rho_iteration, length
        )
        candidate_dual = candidate_first_dual(field, code_rows, k, length)
        if candidate_dual != code_dual:
            dual_differences += 1

        code_hull = hull_dimension(field, code_rows, code_dual, length)
        candidate_hull = hull_dimension(field, code_rows, candidate_dual, length)
        if code_hull != candidate_hull:
            hull_dimension_differences += 1
        code_lcd = code_hull == 0
        candidate_lcd = candidate_hull == 0
        code_lcd_count += code_lcd
        candidate_lcd_count += candidate_lcd
        if code_lcd != candidate_lcd:
            lcd_criterion_differences += 1

        check = divide_poly(field, modulus, generator)[0]
        code_reciprocal_rows = row_basis(
            field,
            generator_rows(reciprocal(field, check, rho_iteration), length),
            length,
        )
        candidate_reciprocal_rows = row_basis(
            field,
            generator_rows(reciprocal(field, check, k), length),
            length,
        )
        if candidate_dual == candidate_reciprocal_rows:
            candidate_sigma_generator_agreements += 1
        if code_dual == code_reciprocal_rows:
            candidate_rho_generator_agreements += 1
        # The literal candidate-first dual agrees with the sigma reciprocal;
        # the code-first dual agrees with the rho reciprocal.
        assert candidate_dual == candidate_reciprocal_rows
        assert code_dual == code_reciprocal_rows

        if not is_constacyclic(
            field, candidate_dual,
            inverse_power(field, twist, k), length
        ):
            raise AssertionError("candidate-first twist prediction failed")
        candidate_twist_checks += 1
        if not is_constacyclic(
            field, code_dual,
            inverse_power(field, twist, rho_iteration), length
        ):
            raise AssertionError("code-first twist prediction failed")
        code_twist_checks += 1

        if same_factor_set:
            code_support = support_for(rho_permutation, selected)
            candidate_support = support_for(sigma_permutation, selected)
            if code_support != candidate_support:
                factor_support_differences += 1
            code_weighted = sum(len(factors[i]) - 1 for i in code_support)
            candidate_weighted = sum(len(factors[i]) - 1 for i in candidate_support)
            assert code_weighted == code_hull
            assert candidate_weighted == candidate_hull

    # Verify the relation D_candidate = sigma^2(D_code) directly, using only
    # this script's field map and row-space comparison.
    relation_failures = 0
    for mask in range(1 << len(factors)):
        code_rows = rows_by_mask[mask]
        code_dual = code_first_dual(field, code_rows, k, rho_iteration, length)
        sigma_squared_code_dual = row_basis(
            field,
            [
                tuple(field.frobenius(value, 2 * k) for value in row)
                for row in code_dual
            ],
            length,
        )
        candidate_dual = candidate_first_dual(field, code_rows, k, length)
        if sigma_squared_code_dual != candidate_dual:
            relation_failures += 1
    assert relation_failures == 0
    assert lcd_criterion_differences == 0

    # For the source's displayed rho reciprocal, count the literal
    # candidate-first disagreements.  This is the convention contradiction
    # probe when sigma and rho differ.
    source_displayed_rho_disagreements = 0
    for mask in range(1 << len(factors)):
        selected = tuple(i for i in range(len(factors)) if mask & (1 << i))
        generator = product_poly(field, [factors[i] for i in selected])
        code_rows = generator_rows(generator, length)
        check = divide_poly(field, modulus, generator)[0]
        source_rho_rows = row_basis(
            field,
            generator_rows(reciprocal(field, check, rho_iteration), length),
            length,
        )
        if candidate_first_dual(field, code_rows, k, length) != source_rho_rows:
            source_displayed_rho_disagreements += 1

    candidate_twist_value = inverse_power(field, twist, k)
    code_twist_value = inverse_power(field, twist, rho_iteration)
    print(
        f"{label}: factors={len(factors)}, selections={1 << len(factors)}, "
        f"sigma_iter={k}, rho_iter={rho_iteration}, "
        f"dual_differences={dual_differences}, "
        f"hull_dimension_differences={hull_dimension_differences}, "
        f"lcd_criterion_differences={lcd_criterion_differences}, "
        f"code_lcd_count={code_lcd_count}, candidate_lcd_count={candidate_lcd_count}, "
        f"factor_support_differences={factor_support_differences}, "
        f"candidate_sigma_generator_agreements={candidate_sigma_generator_agreements}, "
        f"code_rho_generator_agreements={candidate_rho_generator_agreements}, "
        f"candidate_twist={candidate_twist_value}, code_twist={code_twist_value}, "
        f"candidate_twist_checks={candidate_twist_checks}, "
        f"code_twist_checks={code_twist_checks}, "
        f"relation_failures={relation_failures}, "
        f"source_displayed_rho_disagreements={source_displayed_rho_disagreements}"
    )
    print(
        f"{label}: sigma_perm={sigma_permutation}, "
        f"rho_perm={rho_permutation}"
    )
    return {
        "factors": len(factors),
        "selections": 1 << len(factors),
        "dual_differences": dual_differences,
        "hull_dimension_differences": hull_dimension_differences,
        "factor_support_differences": factor_support_differences,
        "source_displayed_rho_disagreements": source_displayed_rho_disagreements,
    }


def main():
    f4 = Field(2, 0b111)
    f8 = Field(3, 0b1011)
    f16 = Field(4, 0b10011)

    results = [
        evaluate_case("F4 lambda=1 k=1", f4, 5, 1, 1),
        evaluate_case("F8 lambda=1 k=1", f8, 7, 1, 1),
        evaluate_case("F8 lambda=1 k=2", f8, 7, 1, 2),
        evaluate_case("F16 over F4 lambda=1 k=1", f16, 5, 1, 1),
        evaluate_case(
            "F16 over F4 lambda=alpha^3 k=1", f16, 3, 8, 1,
            same_factor_set=False,
        ),
    ]
    assert results[0]["dual_differences"] == 0
    assert results[1]["dual_differences"] > 0
    assert results[2]["dual_differences"] > 0
    assert results[3]["dual_differences"] > 0
    assert results[4]["dual_differences"] > 0
    print("PHASE4 CONVENTION EQUIVALENCE CHECK: PASS (finite evidence only)")


if __name__ == "__main__":
    main()
