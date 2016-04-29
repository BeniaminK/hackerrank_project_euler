#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


def pentagonal_number(n):
    return n * (3 * n - 1) / 2


def solve_quadratic_equation(a, b, c):
    import math
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return float('NaN'), float('NaN')
    sqrt_delta = math.sqrt(delta)
    x1 = (-b + sqrt_delta) / (2 * a)
    x2 = (-b - sqrt_delta) / (2 * a)
    return x1, x2


def is_pentagonal(number):
    import math
    x1, x2 = solve_quadratic_equation(3, -1, - 2 * number)
    if math.isnan(x1):
        return False
    x1_int = int(round(x1, 0))
    x2_int = int(round(x2, 0))
    if x1_int > 0 and pentagonal_number(x1_int) == number:
        return x1_int
    if x2_int > 0 and pentagonal_number(x2_int) == number:
        return x2_int
    return False


def solve(N, K):
    pentagons = []
    for n in xrange(K + 1, N):
        p_n = pentagonal_number(n)
        p_n_minus_k = pentagonal_number(n - K)
        if is_pentagonal(p_n - p_n_minus_k) or is_pentagonal(p_n + p_n_minus_k):
            pentagons.append(p_n)
    return "\n".join(map(str, pentagons))


def main():
    N, K = map(int, raw_input().split())
    print solve(N, K)

if __name__ == '__main__':
    main()


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_solver(self):
        import sys
        import StringIO
        input = \
            """10 2
            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass