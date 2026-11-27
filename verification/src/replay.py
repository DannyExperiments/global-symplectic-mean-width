"""Exact finite checks for the symplectic mean-width proof and examples."""

from fractions import Fraction as F
from itertools import product


def transpose(matrix):
    return tuple(zip(*matrix))


def multiply(left, right):
    return tuple(
        tuple(sum(x * y for x, y in zip(row, column)) for column in zip(*right))
        for row in left
    )


def combine(left, right, weight):
    return tuple(
        tuple(a + weight * b for a, b in zip(row, other))
        for row, other in zip(left, right)
    )


def scale(matrix, factor):
    return tuple(tuple(factor * entry for entry in row) for row in matrix)


def diagonal(entries):
    return tuple(
        tuple(entry if i == j else F(0) for j in range(len(entries)))
        for i, entry in enumerate(entries)
    )


def apply(matrix, vector):
    return tuple(sum(a * b for a, b in zip(row, vector)) for row in matrix)


def block_rotation(a, b):
    return ((a, -b, 0, 0), (b, a, 0, 0), (0, 0, a, -b), (0, 0, b, a))


def support_box(vector):
    return sum(map(abs, vector))


def support_cross_polytope(vector):
    return max(map(abs, vector))


def main():
    identity = diagonal((1, 1, 1, 1))
    complex_structure = ((0, 0, -1, 0), (0, 0, 0, -1), (1, 0, 0, 0), (0, 1, 0, 0))
    j_inv = transpose(complex_structure)
    rotations = [(F(1), F(0)), (F(3, 5), F(4, 5)), (F(5, 13), F(12, 13))]
    squeezes = (F(1, 3), F(1, 2), F(1), F(3, 2), F(2), F(3))
    test_vectors = tuple(product((-1, 0, 1), repeat=4))
    polar_cases = support_cases = 0

    for s, t in product(squeezes, repeat=2):
        spectrum = (s, t, 1 / s, 1 / t)
        reciprocal = tuple(1 / val for val in spectrum)
        for a, b in rotations:
            q = block_rotation(a, b)
            q_t = transpose(q)
            assert multiply(q_t, q) == identity
            assert multiply(multiply(q_t, complex_structure), q) == complex_structure
            positive = multiply(multiply(q, diagonal(spectrum)), q_t)
            inverse = multiply(multiply(q, diagonal(reciprocal)), q_t)
            # Use a left unitary factor so the check also exercises nonsymmetric P.
            unitary = block_rotation(F(7, 25), F(24, 25))
            p = multiply(unitary, positive)
            p_t = transpose(p)
            assert multiply(multiply(p_t, complex_structure), p) == complex_structure
            assert multiply(multiply(p, complex_structure), p_t) == complex_structure
            b_matrix = multiply(p_t, p)
            assert b_matrix == multiply(positive, positive)
            assert multiply(multiply(b_matrix, complex_structure), b_matrix) == complex_structure
            assert multiply(multiply(j_inv, positive), complex_structure) == inverse
            assert multiply(positive, inverse) == identity
            midpoint = scale(combine(positive, inverse, 1), F(1, 2))
            half_difference = scale(combine(positive, inverse, -1), F(1, 2))
            covariance = combine(multiply(midpoint, midpoint), identity, -1)
            # A symmetric matrix times its transpose is positive semidefinite.
            assert covariance == multiply(half_difference, transpose(half_difference))
            assert (covariance == diagonal((0,) * 4)) == (s == t == 1)
            assert (b_matrix == identity) == (s == t == 1)
            polar_cases += 1

            for vec in test_vectors:
                left, right = apply(positive, vec), apply(inverse, vec)
                center = apply(midpoint, vec)
                j_vec = apply(complex_structure, vec)
                for support in (support_box, support_cross_polytope):
                    assert support(j_vec) == support(vec)
                    assert support(right) == support(apply(positive, j_vec))
                    assert 2 * support(center) <= support(left) + support(right)
                    support_cases += 1

    guide_squeezes = (F(1), F(5, 4), F(3, 2), F(2), F(5, 2), F(3))
    ratios = []
    for s in guide_squeezes:
        t = 1 / s
        assert (2 * s) * (2 * t) == 4
        width_times_pi = 4 * (s + t)
        ratios.append(width_times_pi / 8)
        assert ((s - t) / 2) ** 2 == (width_times_pi / 8) ** 2 - 1
    assert ratios == [F(1), F(41, 40), F(13, 12), F(5, 4), F(29, 20), F(5, 3)]
    assert 8 * ratios[3] == 10
    assert ratios[3] ** 2 - 1 == F(9, 16)
    direction = (F(3, 5), F(4, 5))
    assert sum(entry**2 for entry in direction) == 1
    assert 2 * support_box(direction) == F(14, 5)
    assert 2 * support_box((2 * direction[0], direction[1] / 2)) == F(16, 5)

    r1, r2, scale1, scale2 = F(1), F(4), F(2), F(1, 2)
    assert scale1**2 * scale2**2 == 1
    assert F(4, 3) * (r1 + r2) == F(20, 3)
    assert F(4, 3) * (scale1 * r1 + scale2 * r2) == F(16, 3)
    # Coordinates are ordered (x1, x2, y1, y2).
    scaling = diagonal((scale1, scale2, scale1, scale2))
    assert multiply(multiply(transpose(scaling), complex_structure), scaling) != complex_structure

    print(f"Polar and covariance fixtures over exact rationals: {polar_cases}.")
    print(f"Support and reciprocal-image checks: {support_cases}.")
    print(f"Square explorer settings checked: {len(guide_squeezes)}.")
    print("At squeeze 2: area 4, mean-width ratio 5/4, added covariance (9/16)I.")
    print("Unequal disk radii example: determinant-one change decreases width from 20/3 to 16/3.")


if __name__ == "__main__":
    main()
