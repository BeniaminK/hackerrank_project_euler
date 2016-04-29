#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


def solve_quadratic_equation(a, b, c):
    import math

    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return float('NaN'), float('NaN')
    sqrt_delta = math.sqrt(delta)
    x1 = (-b + sqrt_delta) / (2 * a)
    x2 = (-b - sqrt_delta) / (2 * a)
    return x1, x2


def count_triangle_number(number):
    return (number * (number+1)) / 2


def solve(n):
    a = 1
    b = 1
    c = - 2 * n
    x1, x2 = solve_quadratic_equation(a, b, c)
    import math
    if math.isnan(x1):
        return -1
    x1_int = int(round(x1, 0))
    x2_int = int(round(x2, 0))

    if count_triangle_number(x1_int) == n:
        return x1_int
    elif count_triangle_number(x2_int) == n:
        return x2_int
    else:
        return -1


def main():
    T = int(raw_input())
    for i in xrange(T):
        n = int(raw_input())
        print solve(n)

if __name__ == '__main__':
    main()


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_solver(self):
        import sys
        import StringIO
        input = \
            """3
            2
            3
            55
            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass