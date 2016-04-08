#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


def sum_of_squares(n):
    return (n * (n + 1) * (2 * n + 1)) / 6


def solve(n):
    n = n / 2 + 1
    mod = 10 ** 9 + 7
    sum = (16 * n ** 3 + 14 * n) / 3 - 3 - 6 * n ** 2
    return sum % mod


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
            """4
            1
3
5
7
            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass