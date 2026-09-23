"""Validate two genuinely k-Galois examples for the hull-enumerator blueprint.

The declared inner product is <c,x> = sum c_i x_i^(p^k).  The direct
validator solves those defining equations independently: it introduces
y_i=x_i^(p^k), solves c dot y=0, and maps y back through the inverse
field automorphism.  The principal reciprocal is checked separately.

Example A (m=1, genuine non-involutory action):
    q=8=2^3, K=F_8, n=7, lambda=1, k=1.
    x^7-1 splits over F_8 and tau has one orbit of length 6.

Example B (extension component m_s>1):
    q=4=2^2, K=F_16=F_{q^2}, n=5, lambda=1, k=1.
    x^5-1 splits over F_16 and tau has one orbit of length 4.

For each example the script compares:
  1. direct generator-matrix hull computation with the declared dual slot;
  2. the inverse-Frobenius factor action and reciprocal;
  3. the orbit-boundary formula;
  4. a 2x2 transfer-matrix enumerator.

No third-party package is required.  The existing F_4 pilot is deliberately
left in code/validate_pilot.py and is not modified by this script.
"""

from collections import Counter
from itertools import product


# ---------------------------------------------------------------------------
# Binary extension fields F_{2^r}.
# Elements are bit vectors and modulus is the irreducible polynomial bit mask.
# ---------------------------------------------------------------------------


class BinaryField:
    def __init__(self, degree, modulus):
        self.degree = degree
        self.modulus = modulus
        self.size = 1 << degree
        self.alpha = 2
        assert self.pow(self.alpha, self.size - 1) == 1
        for prime in (2, 3, 5, 7):
            if (self.size - 1) % prime == 0:
                assert self.pow(self.alpha, (self.size - 1) // prime) != 1

    def add(self, x, y):
        return x ^ y

    def mul(self, x, y):
        raw = 0
        a, b = x, y
        while b:
            if b & 1:
                raw ^= a
            b >>= 1
            a <<= 1
        # Reduce while the raw degree is at least the modulus degree.
        for bit in range(raw.bit_length() - 1, self.degree - 1, -1):
            if (raw >> bit) & 1:
                raw ^= self.modulus << (bit - self.degree)
        return raw

    def pow(self, x, exponent):
        result = 1
        base = x
        while exponent:
            if exponent & 1:
                result = self.mul(result, base)
            base = self.mul(base, base)
            exponent >>= 1
        return result

    def inv(self, x):
        if x == 0:
            raise ZeroDivisionError
        return self.pow(x, self.size - 2)

    def frobenius(self, x, exponent):
        return self.pow(x, exponent)

    def neg(self, x):
        # Characteristic two.
        return x


# ---------------------------------------------------------------------------
# Polynomial arithmetic over a binary extension field.
# Coefficients are low-degree first.
# ---------------------------------------------------------------------------


def p_trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


def p_add(F, p, q):
    out = [0] * max(len(p), len(q))
    for i in range(len(out)):
        out[i] = (p[i] if i < len(p) else 0) ^ (q[i] if i < len(q) else 0)
    return p_trim(out)


def p_mul(F, p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] ^= F.mul(a, b)
    return p_trim(out)


def p_scale(F, p, c):
    return p_trim([F.mul(c, x) for x in p])


def p_monic(F, p):
    return p_scale(F, p, F.inv(p[-1]))


def linear_factor(F, root):
    # x-root = x+root in characteristic two.
    return (root, 1)


def product_polynomials(F, factors):
    result = (1,)
    for factor in factors:
        result = p_mul(F, result, factor)
    return result


def normalized_galois_reciprocal(F, f, automorphism_exponent):
    """Apply one explicit automorphism to reciprocal coefficients.

    ``automorphism_exponent`` is the integer r in a -> a^(2^r), not
    the Galois parameter k itself and not a symbolic rho.  The caller
    supplies either the principal inverse-Frobenius exponent or the
    explicitly labeled alternative p^k exponent.
    """
    degree = len(f) - 1
    constant_image = F.frobenius(f[0], automorphism_exponent)
    scale = F.inv(constant_image)
    result = [0] * (degree + 1)
    for i, coefficient in enumerate(f):
        image = F.frobenius(coefficient, automorphism_exponent)
        result[degree - i] = F.mul(scale, image)
    return p_monic(F, result)


# ---------------------------------------------------------------------------
# Finite-field linear algebra.
# ---------------------------------------------------------------------------


def matrix_rref(F, matrix, columns):
    rows = [list(row) for row in matrix if any(row)]
    pivot_columns = []
    pivot_row = 0
    for column in range(columns):
        selected = next(
            (r for r in range(pivot_row, len(rows)) if rows[r][column]),
            None,
        )
        if selected is None:
            continue
        rows[pivot_row], rows[selected] = rows[selected], rows[pivot_row]
        scale = F.inv(rows[pivot_row][column])
        rows[pivot_row] = [F.mul(scale, x) for x in rows[pivot_row]]
        for r in range(len(rows)):
            if r != pivot_row and rows[r][column]:
                factor = rows[r][column]
                rows[r] = [
                    a ^ F.mul(factor, b)
                    for a, b in zip(rows[r], rows[pivot_row])
                ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return rows, pivot_columns


def matrix_rank(F, matrix, columns):
    _, pivots = matrix_rref(F, matrix, columns)
    return len(pivots)


def nullspace(F, matrix, columns):
    rref, pivots = matrix_rref(F, matrix, columns)
    pivot_set = set(pivots)
    free_columns = [c for c in range(columns) if c not in pivot_set]
    basis = []
    for free in free_columns:
        vector = [0] * columns
        vector[free] = 1
        for row, pivot in enumerate(pivots):
            vector[pivot] = rref[row][free]
        basis.append(tuple(vector))
    return basis


def row_basis(F, matrix, columns):
    rref, _ = matrix_rref(F, matrix, columns)
    return [tuple(row) for row in rref if any(row)]


def span(F, rows, length):
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


def vector_frobenius(F, vector, exponent):
    return tuple(F.frobenius(x, exponent) for x in vector)


def generator_rows(F, generator, length):
    degree = len(generator) - 1
    return [
        tuple(
            generator[i - shift] if 0 <= i - shift < len(generator) else 0
            for i in range(length)
        )
        for shift in range(length - degree)
    ]


def direct_dual_from_inner_product(F, code_basis, sigma_exponent,
                                   inverse_exponent, length):
    """Compute {x: sum c_i x_i^(2^k)=0} from the defining equations.

    Put y_i=x_i^(2^k).  The actual equations are c dot y=0, so the
    nullspace is formed from the original code rows, not from a reciprocal
    convention.  Since x= y^(2^(em-k)), map the nullspace basis back through
    the inverse automorphism.  The returned set is the direct semilinear dual.
    """
    transformed_candidate_basis = nullspace(F, code_basis, length)
    direct_basis = [
        vector_frobenius(F, vector, inverse_exponent)
        for vector in transformed_candidate_basis
    ]
    assert all(
        vector_frobenius(F, candidate, sigma_exponent) == transformed
        for transformed, candidate in zip(
            transformed_candidate_basis, direct_basis
        )
    )
    return direct_basis, span(F, direct_basis, length)


def galois_inner_product(F, codeword, candidate, sigma_exponent):
    value = 0
    for c, x in zip(codeword, candidate):
        value ^= F.mul(c, F.frobenius(x, sigma_exponent))
    return value


def direct_hull_dimensions(F, rows, sigma_exponent, inverse_exponent):
    """Return (K-dimension of C, K-dimension of Hull_k(C))."""
    n = len(rows[0]) if rows else 0
    C_basis = row_basis(F, rows, n)
    code_dimension = len(C_basis)
    dual_basis, direct_dual = direct_dual_from_inner_product(
        F, C_basis, sigma_exponent, inverse_exponent, n
    )
    assert all(
        galois_inner_product(F, row, candidate, sigma_exponent) == 0
        for row in C_basis
        for candidate in dual_basis
    )
    stacked = C_basis + dual_basis
    intersection_dimension = (
        len(C_basis) + len(dual_basis) - matrix_rank(F, stacked, n)
    )
    return code_dimension, intersection_dimension


# ---------------------------------------------------------------------------
# Polynomial enumerators.
# A polynomial is Counter[(u_degree,z_degree)] -> coefficient.
# ---------------------------------------------------------------------------


def poly_add(a, b):
    result = Counter(a)
    result.update(b)
    return Counter({key: value for key, value in result.items() if value})


def poly_mul(a, b):
    result = Counter()
    for (u1, z1), c1 in a.items():
        for (u2, z2), c2 in b.items():
            result[(u1 + u2, z1 + z2)] += c1 * c2
    return result


def matrix_mul(A, B):
    return [
        [
            poly_add(poly_mul(A[i][0], B[0][j]), poly_mul(A[i][1], B[1][j]))
            for j in range(2)
        ]
        for i in range(2)
    ]


def matrix_power(A, exponent):
    result = [[{(0, 0): 1}, {}], [{}, {(0, 0): 1}]]
    base = A
    while exponent:
        if exponent & 1:
            result = matrix_mul(result, base)
        base = matrix_mul(base, base)
        exponent >>= 1
    return result


def transfer_orbit_polynomial(length, weight):
    # Correct matrix for code dimension, not selected-factor codimension.
    T = [
        [{(weight, 0): 1}, {(0, 0): 1}],
        [{(weight, weight): 1}, {(0, 0): 1}],
    ]
    powered = matrix_power(T, length)
    return poly_add(powered[0][0], powered[1][1])


def multiply_global_polynomials(polynomials):
    result = {(0, 0): 1}
    for polynomial in polynomials:
        result = poly_mul(result, polynomial)
    return result


def boundary_orbit_polynomial(length, weight):
    result = Counter()
    for word in product([0, 1], repeat=length):
        code_dimension = weight * sum(1 - bit for bit in word)
        boundaries = sum(
            word[i] * (1 - word[(i + 1) % length])
            for i in range(length)
        )
        result[(code_dimension, weight * boundaries)] += 1
    return result


def boundary_global_polynomial(orbits):
    return multiply_global_polynomials(
        [boundary_orbit_polynomial(length, weight) for length, weight in orbits]
    )


# ---------------------------------------------------------------------------
# Examples and validation.
# ---------------------------------------------------------------------------


def roots_and_factors(F, n):
    assert (F.size - 1) % n == 0
    step = (F.size - 1) // n
    roots = [F.pow(F.alpha, step * j) for j in range(n)]
    factors = [linear_factor(F, root) for root in roots]
    polynomial = (1,) + (0,) * (n - 1) + (1,)
    assert product_polynomials(F, factors) == polynomial
    assert len(set(factors)) == n
    return roots, factors


def tau_orbits(F, factors, automorphism_exponent):
    index = {factor: i for i, factor in enumerate(factors)}
    permutation = []
    for factor in factors:
        image = normalized_galois_reciprocal(F, factor, automorphism_exponent)
        assert image in index
        permutation.append(index[image])

    orbits = []
    visited = set()
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
    return permutation, orbits


def constacyclic_shift(F, vector, twist):
    return (F.mul(twist, vector[-1]),) + vector[:-1]


def is_constacyclic(F, code, twist):
    return all(constacyclic_shift(F, vector, twist) in code for vector in code)


def direct_histogram(F, factors, n, sigma_exponent,
                     inverse_exponent, principal_exponent, component_weight):
    histogram = Counter()
    dual_checks = 0
    for mask in range(1 << len(factors)):
        selected = [
            factors[i]
            for i in range(len(factors))
            if (mask >> i) & 1
        ]
        complement = [
            factors[i]
            for i in range(len(factors))
            if not ((mask >> i) & 1)
        ]
        generator = product_polynomials(F, selected)
        check = product_polynomials(F, complement)
        rows = generator_rows(F, generator, n)
        code_basis = row_basis(F, rows, n)
        direct_dual_basis, direct_dual = direct_dual_from_inner_product(
            F, code_basis, sigma_exponent, inverse_exponent, n
        )
        assert all(
            galois_inner_product(F, codeword, candidate, sigma_exponent) == 0
            for codeword in code_basis
            for candidate in direct_dual_basis
        )
        predicted = normalized_galois_reciprocal(F, check, principal_exponent)
        predicted_dual = span(F, generator_rows(F, predicted, n), n)
        assert direct_dual == predicted_dual
        # These examples have lambda=1, so the predicted twist is also 1.
        assert is_constacyclic(F, direct_dual, 1)
        dual_checks += 1

        code_dimension, hull_dimension = direct_hull_dimensions(
            F, rows, sigma_exponent, inverse_exponent
        )
        histogram[
            (component_weight * code_dimension,
             component_weight * hull_dimension)
        ] += 1
    return histogram, dual_checks


def validate_example(name, F, q, e, m, k, n):
    sigma_exponent = 2 ** k
    inverse_exponent = 2 ** (e * m - k)
    principal_exponent = inverse_exponent
    roots, factors = roots_and_factors(F, n)
    permutation, index_orbits = tau_orbits(F, factors, principal_exponent)
    orbit_data = [(len(orbit), m) for orbit in index_orbits]

    # For a linear factor every K-degree is one, so w=m.
    boundary = boundary_global_polynomial(orbit_data)
    transfer = multiply_global_polynomials(
        [transfer_orbit_polynomial(length, weight)
         for length, weight in orbit_data]
    )
    direct, dual_checks = direct_histogram(
        F, factors, n, sigma_exponent, inverse_exponent, principal_exponent, m
    )

    assert boundary == transfer
    assert direct == boundary
    assert sum(direct.values()) == 2 ** n

    print(f"{name}:")
    print(f"  q={q}, e={e}, m_s={m}, k={k}, n={n}")
    print(f"  sigma exponent p^k={sigma_exponent}")
    print(f"  principal reciprocal exponent p^(e*m_s-k)={principal_exponent}; direct uses p^k={sigma_exponent}")
    print(f"  tau permutation on root indices: {permutation}")
    print(f"  orbit lengths: {[len(orbit) for orbit in index_orbits]}")
    print(f"  orbit-boundary == transfer: {boundary == transfer}")
    print(f"  direct dual-generator checks: {dual_checks} of {2 ** n}")
    print(f"  direct == theory: {direct == boundary}")
    print(f"  joint histogram: {dict(sorted(direct.items()))}")
    hull_histogram = Counter()
    for (_, hull_dimension), count in direct.items():
        hull_histogram[hull_dimension] += count
    print(f"  hull histogram: {dict(sorted(hull_histogram.items()))}")
    print("  PASS")


def main():
    # Example A: m_s=1 but a genuine non-involutory k-Galois orbit.
    # F_8 = F_2[a]/(a^3+a+1), q=8=2^3, k=1,
    # sigma=p^k=2 is used in the defining inner product; the finalized
    # principal reciprocal exponent is p^(e*m-k)=4.
    F8 = BinaryField(3, 0b1011)
    validate_example(
        "Example A (m_s=1, orbit length 6)",
        F=F8,
        q=8,
        e=3,
        m=1,
        k=1,
        n=7,
    )

    # Example B: an extension component K=F_16=F_{4^2}.
    # q=4=2^2, m_s=2, k=1,
    # sigma=p^k=2 is used in the defining inner product; the finalized
    # principal reciprocal exponent is p^(e*m-k)=8.
    F16 = BinaryField(4, 0b10011)
    validate_example(
        "Example B (m_s=2, orbit length 4)",
        F=F16,
        q=4,
        e=2,
        m=2,
        k=1,
        n=5,
    )

    print("ALL LONG-ORBIT AND m_s>1 VALIDATIONS PASS")


if __name__ == "__main__":
    main()
