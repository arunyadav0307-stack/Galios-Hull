"""Independent Phase-3 exhaustive checks for the labeled enumerator.

This file deliberately does not import the repository's validator modules or
reuse their finite-field, reciprocal, hull, orbit, or transfer implementations.
It implements a small characteristic-two finite-field and polynomial engine,
computes direct semilinear duals by linear algebra, and compares those results
with independently reconstructed factor-support, boundary, and transfer data.

The checks are finite evidence only; they are not a proof of the general theory.
"""

from collections import Counter
from itertools import product
from math import prod


class GF2m:
    def __init__(self, degree, modulus):
        assert degree >= 1
        assert modulus & (1 << degree)
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

    def pow(self, value, exponent):
        result = 1
        base = value
        while exponent:
            if exponent & 1:
                result = self.mul(result, base)
            base = self.mul(base, base)
            exponent >>= 1
        return result

    def inv(self, value):
        if value == 0:
            raise ZeroDivisionError("zero has no inverse")
        return self.pow(value, self.size - 2)

    def div(self, numerator, denominator):
        return self.mul(numerator, self.inv(denominator))

    def frobenius(self, value, iteration):
        return self.pow(value, 1 << (iteration % self.degree))


# Polynomials use low-degree-first coefficient tuples.
def p_trim(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return tuple(poly)


def p_add(field, left, right):
    length = max(len(left), len(right))
    return p_trim(
        tuple(
            field.add(
                left[index] if index < len(left) else 0,
                right[index] if index < len(right) else 0,
            )
            for index in range(length)
        )
    )


def p_mul(field, left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] = field.add(result[i + j], field.mul(a, b))
    return p_trim(result)


def p_scale(field, poly, scalar):
    return p_trim(tuple(field.mul(scalar, coefficient) for coefficient in poly))


def p_divmod(field, numerator, denominator):
    numerator = list(p_trim(numerator))
    denominator = p_trim(denominator)
    if denominator == (0,):
        raise ZeroDivisionError("polynomial division by zero")
    quotient = [0] * max(1, len(numerator) - len(denominator) + 1)
    while len(numerator) >= len(denominator) and not (
        len(numerator) == 1 and numerator[0] == 0
    ):
        scalar = field.div(numerator[-1], denominator[-1])
        shift = len(numerator) - len(denominator)
        quotient[shift] = scalar
        for index, coefficient in enumerate(denominator):
            position = index + shift
            numerator[position] = field.sub(
                numerator[position], field.mul(scalar, coefficient)
            )
        while len(numerator) > 1 and numerator[-1] == 0:
            numerator.pop()
    return p_trim(quotient), p_trim(numerator)


def p_monic(field, poly):
    poly = p_trim(poly)
    return p_scale(field, poly, field.inv(poly[-1]))


def p_product(field, polys):
    result = (1,)
    for poly in polys:
        result = p_mul(field, result, poly)
    return result


def factor_squarefree(field, polynomial):
    """Brute-force monic factorization for the small tested degrees."""
    polynomial = p_monic(field, polynomial)
    degree = len(polynomial) - 1
    if degree <= 1:
        return [polynomial]
    for divisor_degree in range(1, degree // 2 + 1):
        for coefficients in product(range(field.size), repeat=divisor_degree):
            if coefficients[0] == 0:
                continue
            divisor = tuple(coefficients) + (1,)
            quotient, remainder = p_divmod(field, polynomial, divisor)
            if remainder == (0,):
                return factor_squarefree(field, divisor) + factor_squarefree(
                    field, quotient
                )
    return [polynomial]


def p_reciprocal(field, polynomial, frobenius_iteration):
    polynomial = p_monic(field, polynomial)
    degree = len(polynomial) - 1
    image_constant = field.frobenius(polynomial[0], frobenius_iteration)
    scale = field.inv(image_constant)
    result = [0] * (degree + 1)
    for index, coefficient in enumerate(polynomial):
        result[degree - index] = field.mul(
            scale, field.frobenius(coefficient, frobenius_iteration)
        )
    return p_monic(field, result)


def p_derivative(field, polynomial):
    result = []
    for index in range(1, len(polynomial)):
        result.append(polynomial[index] if index % 2 else 0)
    return p_trim(result or (0,))


def p_eval(field, polynomial, value):
    result = 0
    for coefficient in reversed(polynomial):
        result = field.add(field.mul(result, value), coefficient)
    return result


# Row-space and nullspace routines over the independently implemented field.
def rref(field, rows, columns):
    matrix = [list(row) for row in rows if any(row)]
    pivot_columns = []
    pivot_row = 0
    for column in range(columns):
        candidate = next(
            (index for index in range(pivot_row, len(matrix)) if matrix[index][column]),
            None,
        )
        if candidate is None:
            continue
        matrix[pivot_row], matrix[candidate] = matrix[candidate], matrix[pivot_row]
        scale = field.inv(matrix[pivot_row][column])
        matrix[pivot_row] = [field.mul(scale, value) for value in matrix[pivot_row]]
        for row in range(len(matrix)):
            if row == pivot_row or matrix[row][column] == 0:
                continue
            scale = matrix[row][column]
            matrix[row] = [
                field.sub(value, field.mul(scale, pivot_value))
                for value, pivot_value in zip(matrix[row], matrix[pivot_row])
            ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return [tuple(row) for row in matrix], pivot_columns


def row_basis(field, rows, columns):
    reduced, _ = rref(field, rows, columns)
    return tuple(row for row in reduced if any(row))


def nullspace(field, rows, columns):
    reduced, pivot_columns = rref(field, rows, columns)
    pivot_set = set(pivot_columns)
    free_columns = [column for column in range(columns) if column not in pivot_set]
    basis = []
    for free in free_columns:
        vector = [0] * columns
        vector[free] = 1
        for row, pivot in zip(reduced, pivot_columns):
            vector[pivot] = row[free]
        basis.append(tuple(vector))
    return tuple(basis)


def matrix_rank(field, rows, columns):
    return len(row_basis(field, rows, columns))


def generator_rows(field, generator, length):
    degree = len(generator) - 1
    return tuple(
        tuple(
            generator[index - shift] if shift <= index < shift + len(generator) else 0
            for index in range(length)
        )
        for shift in range(length - degree)
    )


def direct_dual(field, code_rows, sigma_iteration, rho_iteration, length):
    # The defining equations are G * sigma(x)^T = 0.  Solve for y=sigma(x),
    # then apply rho to the nullspace vectors.
    y_basis = nullspace(field, code_rows, length)
    x_basis = [
        tuple(field.frobenius(value, rho_iteration) for value in vector)
        for vector in y_basis
    ]
    return row_basis(field, x_basis, length)


def hull_dimension(field, code_rows, dual_rows, length):
    code_dimension = matrix_rank(field, code_rows, length)
    dual_dimension = matrix_rank(field, dual_rows, length)
    sum_dimension = matrix_rank(field, list(code_rows) + list(dual_rows), length)
    return code_dimension + dual_dimension - sum_dimension


def sharp_factor_index(field, factors, index, rho_iteration):
    image = p_reciprocal(field, factors[index], rho_iteration)
    matches = [other for other, factor in enumerate(factors) if factor == image]
    assert len(matches) == 1, (index, image, matches)
    return matches[0]


def orbit_decomposition(permutation):
    seen = set()
    orbits = []
    for start in range(len(permutation)):
        if start in seen:
            continue
        orbit = []
        current = start
        while current not in seen:
            seen.add(current)
            orbit.append(current)
            current = permutation[current]
        assert current == start
        orbits.append(tuple(orbit))
    return orbits


# Polynomial dictionaries use (u exponent, z exponent) as keys.
def poly_add(left, right):
    result = Counter(left)
    result.update(right)
    return Counter({key: value for key, value in result.items() if value})


def poly_mul(left, right):
    result = Counter()
    for (u1, z1), count1 in left.items():
        for (u2, z2), count2 in right.items():
            result[(u1 + u2, z1 + z2)] += count1 * count2
    return result


def matrix_mul(left, right):
    return [
        [
            poly_add(
                poly_mul(left[i][0], right[0][j]),
                poly_mul(left[i][1], right[1][j]),
            )
            for j in range(2)
        ]
        for i in range(2)
    ]


def matrix_power(matrix, exponent):
    result = [[{(0, 0): 1}, {}], [{}, {(0, 0): 1}]]
    while exponent:
        if exponent & 1:
            result = matrix_mul(result, matrix)
        matrix = matrix_mul(matrix, matrix)
        exponent >>= 1
    return result


def orbit_transfer(length, weight):
    matrix = [
        [{(weight, 0): 1}, {(0, 0): 1}],
        [{(weight, weight): 1}, {(0, 0): 1}],
    ]
    powered = matrix_power(matrix, length)
    return poly_add(powered[0][0], powered[1][1])


def multiply_polynomials(polynomials):
    result = Counter({(0, 0): 1})
    for polynomial in polynomials:
        result = poly_mul(result, polynomial)
    return result


def direct_orbit_polynomial(orbit_length, weight):
    result = Counter()
    for word in product((0, 1), repeat=orbit_length):
        boundary = sum(
            word[index] * (1 - word[(index + 1) % orbit_length])
            for index in range(orbit_length)
        )
        result[(weight * sum(1 - bit for bit in word), weight * boundary)] += 1
    return result


def evaluate_case(name, field, base_degree, length, lam, k):
    extension_degree = field.degree
    rho_iteration = extension_degree - k
    modulus = [0] * (length + 1)
    modulus[0] = field.sub(0, lam)
    modulus[length] = 1
    factors = factor_squarefree(field, tuple(modulus))
    assert p_product(field, factors) == p_monic(field, tuple(modulus))
    assert all(factor[0] != 0 for factor in factors)
    assert len(set(factors)) == len(factors)
    tau = tuple(
        sharp_factor_index(field, factors, index, rho_iteration)
        for index in range(len(factors))
    )
    assert sorted(tau) == list(range(len(factors)))
    # The principal reciprocal is generally not an involution.  Its square
    # applies rho twice, while the sigma reciprocal is its inverse.
    for factor in factors:
        twice = p_reciprocal(
            field, p_reciprocal(field, factor, rho_iteration), rho_iteration
        )
        rho_squared = p_monic(
            field,
            tuple(field.frobenius(coefficient, 2 * rho_iteration)
                  for coefficient in factor),
        )
        assert twice == rho_squared
        inverse = p_reciprocal(
            field, p_reciprocal(field, factor, rho_iteration), k
        )
        assert inverse == factor
    inverse_tau = tuple(
        sharp_factor_index(field, factors, index, k)
        for index in range(len(factors))
    )
    assert all(inverse_tau[tau[index]] == index for index in range(len(factors)))
    orbits = orbit_decomposition(tau)
    weights = [base_degree * (len(factor) - 1) for factor in factors]
    assert all(weights[index] == weights[orbit[0]] for orbit in orbits for index in orbit)

    direct_joint = Counter()
    direct_hull_support_checks = 0
    reciprocal_checks = 0
    inverse_orientation_differences = 0
    inverse_orientation_dimension_failures = 0
    code_signature_to_selections = {}
    for mask in range(1 << len(factors)):
        selected = [index for index in range(len(factors)) if mask & (1 << index)]
        generator = p_product(field, [factors[index] for index in selected])
        code_rows = generator_rows(field, generator, length)
        code_signature = row_basis(field, code_rows, length)
        previous_selections = code_signature_to_selections.setdefault(
            code_signature, []
        )
        assert not previous_selections, (
            "factor-selection collision",
            previous_selections,
            selected,
        )
        previous_selections.append(tuple(selected))
        code_dimension = matrix_rank(field, code_rows, length)
        dual_rows = direct_dual(
            field, code_rows, k, rho_iteration, length
        )
        dual_dimension = matrix_rank(field, dual_rows, length)
        assert code_dimension + dual_dimension == length

        check = p_divmod(field, tuple(modulus), generator)[0]
        predicted_dual_generator = p_reciprocal(
            field, check, rho_iteration
        )
        predicted_dual_rows = row_basis(
            field,
            generator_rows(field, predicted_dual_generator, length),
            length,
        )
        assert predicted_dual_rows == dual_rows
        reciprocal_checks += 1

        hull_dim = hull_dimension(field, code_rows, dual_rows, length)
        direct_joint[(base_degree * code_dimension, base_degree * hull_dim)] += 1

        support = {
            tau[index]
            for index in selected
            if tau[index] not in selected
        }
        expected_hull_dim = base_degree * sum(
            len(factors[index]) - 1 for index in support
        )
        assert base_degree * hull_dim == expected_hull_dim
        inverse_support = {
            index
            for index in range(len(factors))
            if index not in selected and tau[index] in selected
        }
        if support != inverse_support:
            inverse_orientation_differences += 1
        inverse_hull_dim = base_degree * sum(
            len(factors[index]) - 1 for index in inverse_support
        )
        if inverse_hull_dim != base_degree * hull_dim:
            inverse_orientation_dimension_failures += 1
        direct_hull_support_checks += 1

    transfer_data = []
    for orbit in orbits:
        orbit_weight = weights[orbit[0]]
        transfer_data.append(orbit_transfer(len(orbit), orbit_weight))
        assert orbit_transfer(len(orbit), orbit_weight) == direct_orbit_polynomial(
            len(orbit), orbit_weight
        )
    transfer_joint = multiply_polynomials(transfer_data)
    assert transfer_joint == direct_joint

    # Check the closed form orbit coefficients independently of the matrix.
    for orbit in orbits:
        a = len(orbit)
        w = weights[orbit[0]]
        observed = Counter()
        for word in product((0, 1), repeat=a):
            boundary = sum(
                word[index] * (1 - word[(index + 1) % a])
                for index in range(a)
            )
            observed[boundary] += 1
        expected = Counter({0: 2})
        for boundary in range(1, a // 2 + 1):
            # The integer form avoids relying on the rational run formula.
            from math import comb

            expected[boundary] = 2 * comb(a, 2 * boundary)
        assert observed == expected
        assert orbit_transfer(a, w) == direct_orbit_polynomial(a, w)

    print(
        f"{name}: factors={len(factors)}, orbit_lengths="
        f"{[len(orbit) for orbit in orbits]}, selections={1 << len(factors)}, "
        f"unique_codes={len(code_signature_to_selections)}, selection_collisions=0, "
        f"reciprocal_checks={reciprocal_checks}, support_checks="
        f"{direct_hull_support_checks}, inverse_orientation_differences="
        f"{inverse_orientation_differences}, inverse_dimension_failures="
        f"{inverse_orientation_dimension_failures}, total={sum(direct_joint.values())}"
    )
    print(f"{name}: direct_joint == transfer_joint: True")
    return direct_joint, orbits, weights, code_signature_to_selections


def candidate_first_dual(field, code_rows, sigma_iteration, length):
    # This is only a literature-convention probe.  It uses the literal
    # alternative definition <x,c>_k=0, with the candidate in the first slot.
    sigma_rows = [
        tuple(field.frobenius(value, sigma_iteration) for value in row)
        for row in code_rows
    ]
    return row_basis(field, nullspace(field, sigma_rows, length), length)


def source_convention_probe():
    """Expose the source-preprint slot/convention issue independently."""
    field = GF2m(3, 0b1011)  # F_8
    length = 7
    k = 1
    rho_iteration = field.degree - k
    modulus = (1,) + (0,) * (length - 1) + (1,)
    factors = factor_squarefree(field, modulus)
    # A nontrivial selection where the sigma and rho reciprocals differ.
    selected = [1]
    generator = p_product(field, [factors[index] for index in selected])
    code_rows = generator_rows(field, generator, length)
    literal_candidate_first = candidate_first_dual(field, code_rows, k, length)
    check = p_divmod(field, modulus, generator)[0]
    sigma_candidate = row_basis(
        field, generator_rows(field, p_reciprocal(field, check, k), length), length
    )
    rho_candidate = row_basis(
        field,
        generator_rows(field, p_reciprocal(field, check, rho_iteration), length),
        length,
    )
    assert literal_candidate_first == sigma_candidate
    assert literal_candidate_first != rho_candidate
    print(
        "literal candidate-first literature convention probe: sigma reciprocal "
        "matches and rho reciprocal differs on F8 n=7 selection"
    )


def incompatible_edge_check():
    field = GF2m(2, 0b111)
    length = 5
    lam = 2
    k = 0
    rho_iteration = field.degree - k
    modulus = [field.sub(0, lam)] + [0] * (length - 1) + [1]
    factors = factor_squarefree(field, tuple(modulus))
    generator = factors[0]
    code_rows = generator_rows(field, generator, length)
    dual_rows = direct_dual(field, code_rows, k, rho_iteration, length)
    predicted_twist = field.inv(field.frobenius(lam, rho_iteration))
    original_shift = lambda vector: (field.mul(lam, vector[-1]),) + vector[:-1]
    predicted_shift = lambda vector: (
        field.mul(predicted_twist, vector[-1]),
    ) + vector[:-1]
    # The diagnostic checks membership in the row span through RREF, without
    # importing the existing constacyclic test.
    direct_basis = row_basis(field, dual_rows, length)

    def in_span(vector, rows):
        return matrix_rank(field, list(rows), length) == matrix_rank(
            field, list(rows) + [vector], length
        )

    assert all(in_span(predicted_shift(vector), direct_basis) for vector in direct_basis)
    assert predicted_twist != lam
    assert not all(in_span(original_shift(vector), direct_basis) for vector in direct_basis)
    print(
        "incompatible F4 k=0 edge: predicted_twist differs from original and "
        "direct dual is not original-twist constacyclic"
    )


def main():
    f4 = GF2m(2, 0b111)
    f8 = GF2m(3, 0b1011)
    f16 = GF2m(4, 0b10011)

    component_results = []
    component_results.append(
        evaluate_case("F4 lambda=1 k=1", f4, 1, 5, 1, 1)
    )
    component_results.append(
        evaluate_case("F4 lambda=alpha k=1", f4, 1, 5, 2, 1)
    )
    component_results.append(
        evaluate_case("F8 lambda=1 k=1", f8, 1, 7, 1, 1)
    )
    component_results.append(
        evaluate_case("F8 lambda=1 k=2", f8, 1, 7, 1, 2)
    )
    component_results.append(
        evaluate_case("F16 over F4 lambda=1 k=1", f16, 2, 5, 1, 1)
    )

    # A two-component product check: independent component choices multiply.
    first_joint = component_results[0][0]
    product_joint = poly_mul(first_joint, first_joint)
    assert sum(product_joint.values()) == 8 ** 2
    first_signatures = component_results[0][3]
    product_signatures = {}
    for left_signature in first_signatures:
        for right_signature in first_signatures:
            pair_signature = (left_signature, right_signature)
            assert pair_signature not in product_signatures
            product_signatures[pair_signature] = True
    assert len(product_signatures) == 64
    print(
        "F4 x F4 labeled product: component enumerators multiply, "
        "unique_product_codes=64, product_collisions=0"
    )

    source_convention_probe()
    incompatible_edge_check()
    print("PHASE3 INDEPENDENT ENUMERATOR CHECK: PASS (finite evidence only)")


if __name__ == "__main__":
    main()
