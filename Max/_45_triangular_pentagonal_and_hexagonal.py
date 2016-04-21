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


class PolygonalNumber:
    """ Liczby generowane poprzez rozwiniecie formuly: Fn = n * (a * n + b ) / c """

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def count(self, n):
        return n * (self.a * n + self.b) / self.c

    def is_polygonal_number(self, number):
        import math
        x1, x2 = solve_quadratic_equation(self.a, self.b, - self.c * number)
        if math.isnan(x1):
            return False
        x1_int = int(round(x1, 0))
        x2_int = int(round(x2, 0))
        if x1_int > 0 and self.count(x1_int) == number:
            return x1_int
        if x2_int > 0 and self.count(x2_int) == number:
            return x2_int
        return False


triangle = PolygonalNumber(1, 1, 2)
pentagonal = PolygonalNumber(3, -1, 2)
hexagonal = PolygonalNumber(2, -1, 1)


def solve(n, a, b):
    pentagonal_number = pentagonal
    if a == 3:
        other_polygonal_number = triangle
    else:
        other_polygonal_number = hexagonal

    number_n = 1
    numbers = []
    while True:
        penta_count = pentagonal_number.count(number_n)
        if penta_count >= n:
            break
        if other_polygonal_number.is_polygonal_number(penta_count):
            numbers.append(penta_count)
            print "number", number_n

        number_n += 1
    return "\n".join(map(str, numbers)).strip()


def solve_ans(n, a):
    if a == 3:
        array = [1, 210, 40755, 7906276, 1533776805, 297544793910, 57722156241751]
    else:
        array = [1, 40755, 1533776805, 57722156241751]
    return "\n".join(map(str, filter(lambda x: x < n, array))).strip()


def main():
    N, a, b = map(int, raw_input().split())
    print solve_ans(N, a)


if __name__ == '__main__':
    main()


class MyTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_solver(self):
        import sys
        import StringIO
        input = \
            """200000000000000 5 6
            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass
