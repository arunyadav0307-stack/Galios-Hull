"""Small independent counterexample search for the orbit combinatorics.

This is not a proof of the general theorems.  It checks the cyclic support,
transfer-matrix, and orbit-polynomial identities over a larger small range
than the original pilot's a=1,...,5 check.
"""

from collections import Counter
from itertools import product
from math import comb


def polynomial_add(left, right):
    result = Counter(left)
    result.update(right)
    return Counter({key: value for key, value in result.items() if value})


def polynomial_mul(left, right):
    result = Counter()
    for (u1, z1), c1 in left.items():
        for (u2, z2), c2 in right.items():
            result[(u1 + u2, z1 + z2)] += c1 * c2
    return result


def matrix_mul(left, right):
    return [
        [
            polynomial_add(
                polynomial_mul(left[i][0], right[0][j]),
                polynomial_mul(left[i][1], right[1][j]),
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


def transfer_polynomial(length, weight):
    matrix = [
        [{(weight, 0): 1}, {(0, 0): 1}],
        [{(weight, weight): 1}, {(0, 0): 1}],
    ]
    powered = matrix_power(matrix, length)
    return polynomial_add(powered[0][0], powered[1][1])


def direct_cycle_polynomial(length, weight):
    result = Counter()
    for word in product((0, 1), repeat=length):
        boundary = sum(
            word[i] * (1 - word[(i + 1) % length])
            for i in range(length)
        )
        code_dimension = weight * sum(1 - bit for bit in word)
        result[(code_dimension, weight * boundary)] += 1
    return result


def main():
    for length in range(1, 13):
        observed = Counter()
        for word in product((0, 1), repeat=length):
            boundary = sum(
                word[i] * (1 - word[(i + 1) % length])
                for i in range(length)
            )
            observed[boundary] += 1
        expected = Counter({0: 2})
        for boundary in range(1, length // 2 + 1):
            expected[boundary] = 2 * comb(length, 2 * boundary)
        assert observed == expected, (length, observed, expected)

    for length in range(1, 9):
        for weight in (1, 2, 3):
            assert transfer_polynomial(length, weight) == direct_cycle_polynomial(
                length, weight
            ), (length, weight)

    for length in range(1, 13):
        for word in product((0, 1), repeat=length):
            direct_support = {
                (index + 1) % length
                for index, bit in enumerate(word)
                if bit == 1 and word[(index + 1) % length] == 0
            }
            boundary_support = {
                (index + 1) % length
                for index in range(length)
                if word[index] * (1 - word[(index + 1) % length])
            }
            assert direct_support == boundary_support, (length, word)

    print("orbit-polynomial identity checked for lengths 1 through 12")
    print("transfer trace checked for lengths 1 through 8 and weights 1, 2, 3")
    print("support/boundary orientation checked for every binary word of lengths 1 through 12")
    print("No combinatorial counterexample found in the tested finite range.")
    print("This search is computational evidence only, not a general proof.")


if __name__ == "__main__":
    main()
