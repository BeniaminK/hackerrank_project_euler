#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

REST = 10 ** 10


def pow_mod(x, y, z):
    """Calculate (x ** y) % z efficiently."""
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number


def get_last_10_of_self_power(power):
    # result = 1
    # for i in xrange(power):
    #     result *= power
    #     result %= rest
    # return result
    return pow_mod(power, power, REST)


def solve(n):
    suma = 0
    for i in xrange(1, n + 1):
        suma += get_last_10_of_self_power(i)
    return suma % REST


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
            """11"""
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass