#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import math


def solve(n):
    sum_of_numbers = 0
    for i in xrange(10, n):
        arr = []
        num = i
        while num != 0:
            num, mod = divmod(num, 10)
            arr.append(mod)
        sum_of_factorials = sum(map(math.factorial, arr))
        if sum_of_factorials % i == 0:
            sum_of_numbers += i
    return sum_of_numbers


def main():
    N = int(raw_input())
    print solve(N)

if __name__ == '__main__':
    main()


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_solver(self):
        import sys
        import StringIO
        input = \
            """20
            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass