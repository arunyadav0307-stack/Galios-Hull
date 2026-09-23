"""Dependency-free validation for the F_4 pilot example in the blueprint.

The script checks:
  * F_4[x] factorisation of x^5 - 1;
  * the k=1 inverse-Frobenius factor action;
  * direct dual-generator equality using the declared dual slot;
  * direct component-code hull dimensions;
  * the orbit-boundary histogram;
  * the four-component ring histogram.

For this pilot e*m_s-k=k=1, so the principal inverse-Frobenius and
second-slot Frobenius happen to agree.  The direct dual is still evaluated
from the defining inner product, independently of the reciprocal prediction.

F_4 is represented as F_2[a]/(a^2+a+1), with elements encoded by two bits.
"""

from collections import Counter
from itertools import product
from math import comb


# ---------------------------------------------------------------------------
# F_4 arithmetic: a^2+a+1=0, hence a^2=a+1 in characteristic two.
# ---------------------------------------------------------------------------


def add(x, y):
    return x ^ y


def mul(x, y):
    x0, x1 = x & 1, (x >> 1) & 1
    y0, y1 = y & 1, (y >> 1) & 1
    c0 = x0 * y0
    c1 = x0 * y1 ^ x1 * y0
    c2 = x1 * y1
    return (c0 ^ c2) | ((c1 ^ c2) << 1)


def square(x):
    return mul(x, x)


def inverse(x):
    if x == 0:
        raise ZeroDivisionError
    for y in range(1, 4):
        if mul(x, y) == 1:
            return y
    raise AssertionError("nonzero F_4 element has no inverse")


def divide(x, y):
    return mul(x, inverse(y))


# ---------------------------------------------------------------------------
# Polynomials have low-degree coefficients first.
# ---------------------------------------------------------------------------


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


def p_add(p, q):
    out = [0] * max(len(p), len(q))
    for i in range(len(out)):
        out[i] = (p[i] if i < len(p) else 0) ^ (q[i] if i < len(q) else 0)
    return trim(out)


def p_mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] ^= mul(a, b)
    return trim(out)


def p_divmod(f, g):
    f = list(trim(f))
    g = trim(g)
    quotient = [0] * max(1, len(f) - len(g) + 1)
    while len(f) >= len(g) and not (len(f) == 1 and f[0] == 0):
        c = divide(f[-1], g[-1])
        shift = len(f) - len(g)
        quotient[shift] = c
        for i, b in enumerate(g):
            f[i + shift] ^= mul(c, b)
        while len(f) > 1 and f[-1] == 0:
            f.pop()
    return trim(quotient), trim(f)


def p_scale(p, c):
    return trim([mul(c, x) for x in p])


def p_monic(p):
    return p_scale(p, inverse(p[-1]))


def brute_factor(p):
    """Sufficient for degree five; returns monic irreducible factors."""
    p = p_monic(p)
    if len(p) <= 2:
        return [p]
    max_degree = (len(p) - 1) // 2
    for degree in range(1, max_degree + 1):
        for coefficients in product(range(4), repeat=degree):
            g = tuple(coefficients) + (1,)
            if g[0] == 0:
                continue
            quotient, remainder = p_divmod(p, g)
            if remainder == (0,):
                return [g] + brute_factor(quotient)
    return [p]


def normalized_galois_reciprocal(f, automorphism_exponent=2):
    """Apply the explicit automorphism a -> a^(2^r) to reciprocal coefficients.

    The argument is an automorphism exponent, not the Galois parameter k and
    not an implicit rho.  The caller labels the principal reciprocal or an
    alternative comparator before passing it here.
    """
    degree = len(f) - 1
    image = square if automorphism_exponent == 2 else (lambda value: value)
    constant = image(f[0])
    out = [0] * (degree + 1)
    for i, coefficient in enumerate(f):
        out[degree - i] = mul(inverse(constant), image(coefficient))
    return p_monic(out)


def p_string(p):
    names = ["0", "1", "a", "a+1"]
    terms = []
    for i in range(len(p) - 1, -1, -1):
        coefficient = p[i]
        if coefficient == 0:
            continue
        monomial = "1" if i == 0 else ("x" if i == 1 else f"x^{i}")
        if i == 0:
            terms.append(names[coefficient])
        elif coefficient == 1:
            terms.append(monomial)
        else:
            terms.append(f"({names[coefficient]}){monomial}")
    return " + ".join(terms) or "0"


# ---------------------------------------------------------------------------
# Direct k-Galois hull computation for one component.
# ---------------------------------------------------------------------------


def v_add(a, b):
    return tuple(x ^ y for x, y in zip(a, b))


def v_scale(c, a):
    return tuple(mul(c, x) for x in a)


def galois_dot(codeword, candidate, sigma_exponent):
    # This is the defining equation <c,x>_k=0, evaluated directly.
    # sigma_exponent is p^k; no reciprocal convention is used here.
    value = 0
    for c, x in zip(codeword, candidate):
        sigma_x = square(x) if sigma_exponent == 2 else x
        value ^= mul(c, sigma_x)
    return value


def span(rows, length=5):
    result = {(0,) * length}
    for row in rows:
        new_result = set(result)
        for coefficient in range(1, 4):
            scaled = v_scale(coefficient, row)
            new_result.update(v_add(vector, scaled) for vector in result)
        result = new_result
    return result


def generator_rows(g, length=5):
    degree = len(g) - 1
    rows = []
    for shift in range(length - degree):
        row = [0] * length
        for i, coefficient in enumerate(g):
            row[i + shift] = coefficient
        rows.append(tuple(row))
    return rows


def selected_product(factors, selected):
    result = (1,)
    for index in selected:
        result = p_mul(result, factors[index])
    return result


def direct_dual(rows, sigma_exponent, length=5):
    """Compute the dual directly from <c,x>_k=0."""
    return {
        vector
        for vector in product(range(4), repeat=length)
        if all(
            galois_dot(row, vector, sigma_exponent) == 0
            for row in rows
        )
    }


def hull_dimension_for_selection(factors, selected, sigma_exponent,
                                length=5):
    generator = selected_product(factors, selected)
    rows = generator_rows(generator, length)
    code = span(rows, length)
    hull = code & direct_dual(rows, sigma_exponent, length)
    size = len(hull)
    dimension = 0
    while size > 1:
        assert size % 4 == 0
        size //= 4
        dimension += 1
    assert size == 1
    return dimension, len(code)


# ---------------------------------------------------------------------------
# Pilot validation.
# ---------------------------------------------------------------------------


def verify_small_orbit_counts():
    """Check P_{a,w} coefficients for a=1,...,5 with w suppressed."""
    for length in range(1, 6):
        direct = Counter(
            sum(word[i] * (1 - word[(i + 1) % length]) for i in range(length))
            for word in product([0, 1], repeat=length)
        )
        formula = Counter({0: 2})
        for boundaries in range(1, length // 2 + 1):
            formula[boundaries] = (
                length * comb(length - 1, 2 * boundaries - 1) // boundaries
            )
        assert direct == formula, (length, direct, formula)


def main():
    sigma_exponent = 2  # p^k for q=4, k=1
    principal_exponent = 2  # p^(e*m_s-k), equal here by coincidence
    verify_small_orbit_counts()
    print("orbit polynomial checks: a=1,...,5 PASS")
    # In characteristic two, x^5-1 = x^5+1.
    polynomial = (1, 0, 0, 0, 0, 1)
    factors = brute_factor(polynomial)
    assert len(factors) == 3
    assert sorted(len(factor) - 1 for factor in factors) == [1, 2, 2]

    print("factorisation:", " * ".join(p_string(factor) for factor in factors))

    quadratic_factors = [factor for factor in factors if len(factor) - 1 == 2]
    assert len(quadratic_factors) == 2
    images = [normalized_galois_reciprocal(factor, automorphism_exponent=principal_exponent) for factor in quadratic_factors]
    assert images[0] == quadratic_factors[1]
    assert images[1] == quadratic_factors[0]

    linear_factor = next(factor for factor in factors if len(factor) - 1 == 1)
    assert normalized_galois_reciprocal(linear_factor, principal_exponent) == linear_factor
    print("Hermitian factor action: fixed linear factor; quadratic factors swapped")

    component_histogram = Counter()
    dual_generator_checks = 0
    for mask in range(1 << len(factors)):
        selected = [i for i in range(len(factors)) if (mask >> i) & 1]
        complement = [i for i in range(len(factors)) if not ((mask >> i) & 1)]
        generator = selected_product(factors, selected)
        check = selected_product(factors, complement)
        rows = generator_rows(generator)
        direct = direct_dual(rows, sigma_exponent)
        predicted = normalized_galois_reciprocal(check, principal_exponent)
        assert direct == span(generator_rows(predicted))
        dual_generator_checks += 1
        hull_dimension, code_size = hull_dimension_for_selection(
            factors, selected, sigma_exponent
        )
        code_dimension = 0
        size = code_size
        while size > 1:
            assert size % 4 == 0
            size //= 4
            code_dimension += 1
        component_histogram[(code_dimension, hull_dimension)] += 1

    expected_component = Counter(
        {
            (0, 0): 1,
            (1, 0): 1,
            (4, 0): 1,
            (5, 0): 1,
            (2, 2): 2,
            (3, 2): 2,
        }
    )
    assert component_histogram == expected_component
    assert Counter(h for (_, h), count in component_histogram.items() for _ in range(count)) == Counter({0: 4, 2: 4})

    # Enumerate the four-component joint histogram directly.
    ring_joint_histogram = Counter()
    component_pairs = []
    for mask in range(1 << len(factors)):
        selected = [i for i in range(len(factors)) if (mask >> i) & 1]
        hull_dimension, code_size = hull_dimension_for_selection(
            factors, selected, sigma_exponent
        )
        code_dimension = 0
        size = code_size
        while size > 1:
            assert size % 4 == 0
            size //= 4
            code_dimension += 1
        component_pairs.append((code_dimension, hull_dimension))

    for choices in product(component_pairs, repeat=4):
        ring_joint_histogram[
            (sum(code_dimension for code_dimension, _ in choices),
             sum(hull_dimension for _, hull_dimension in choices))
        ] += 1

    # This is the exact product of the component polynomial four times.
    theoretical_joint = Counter({(0, 0): 1})
    for _ in range(4):
        next_histogram = Counter()
        for (old_dimension, old_hull), old_count in theoretical_joint.items():
            for (new_dimension, new_hull), new_count in expected_component.items():
                next_histogram[(old_dimension + new_dimension,
                                old_hull + new_hull)] += old_count * new_count
        theoretical_joint = next_histogram

    assert ring_joint_histogram == theoretical_joint
    ring_hull_histogram = Counter()
    for (_, hull_dimension), count in ring_joint_histogram.items():
        ring_hull_histogram[hull_dimension] += count

    expected_ring = Counter({0: 256, 2: 1024, 4: 1536, 6: 1024, 8: 256})
    assert ring_hull_histogram == expected_ring
    assert sum(ring_joint_histogram.values()) == 4096

    print("direct dual-generator checks:", dual_generator_checks, "of", 2 ** len(factors))
    print("component joint histogram:", dict(sorted(component_histogram.items())))
    print("ring joint histogram terms:", len(ring_joint_histogram))
    print("ring hull histogram:", dict(sorted(ring_hull_histogram.items())))
    print("PASS: direct hulls, factor action, orbit formula, and enumerator agree")


if __name__ == "__main__":
    main()
