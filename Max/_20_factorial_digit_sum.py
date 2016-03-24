#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


def solve(n):
    return


def get_all_factorials(number):
    factorials = [0 for i in xrange(number + 1)]
    factorials[0] = 1
    for i in xrange(1, number + 1):
        factorials[i] = i * factorials[i-1]
    return factorials


def get_sum(val):
    sum_val = 0
    while val != 0:
        val, mod = divmod(val, 10)
        sum_val += mod
    return sum_val


def get_sums(factorials):
    sums = [0 for i in xrange(len(factorials))]
    for idx, val in enumerate(factorials):
        sums[idx] = get_sum(val)
    return sums


def main():
    T = int(input())
    MAX = 1000
    factorials = get_all_factorials(MAX + 1)
    sums = get_sums(factorials)
    for i in xrange(T):
        n = int(input())
        print sums[n]

if __name__ == '__main__':
    main()


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_solver(self):
        import sys
        import StringIO
        input = \
            """2
3
6
            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass