#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


def solve(n):
    sum = 0
    n = 2 ** n
    while n != 0:
        n, mod = divmod(n, 10)
        sum += mod
    return sum


def main():
    T = int(input())
    for i in xrange(T):
        n = int(input())
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
            """ 3
                3
                4
                7
            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass