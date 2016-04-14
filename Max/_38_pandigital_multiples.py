#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


def is_string_pandigital(str_repr, n):
    """ Checks whether string is pandigital with number n.

    Pandigital - means contains only numbers from 1 to n."""
    if len(str_repr) != n:
        return False

    for i in xrange(n):
        if str(i+1) not in str_repr:
            return False
    return True


def is_pandigital(base_number, k):
    s = ""
    multiplier = 1
    while True:
        s += str(base_number * multiplier)
        if len(s) > k:
            return False
        elif len(s) == k:
            return is_string_pandigital(s, k)
        else:
            multiplier += 1
            continue


def solve(n, k):
    s = ""
    for i in xrange(3, n):
        if is_pandigital(i, k):
            s += str(i) + "\n"
    return s.strip()


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
            """100 8
            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass