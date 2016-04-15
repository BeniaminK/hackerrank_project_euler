#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


def is_too_long(str_repr, n):
    """ Checks whether string is longer than n. """
    return len(str_repr) > n


def is_current_number_too_big(current_number, n):
    """ Checks whether current number is too big to create a pandigital solution. """
    max_number_length = (n - 1) / 2
    return len(str(current_number)) > max_number_length


def is_pandigital(str_repr, n):
    """ Checks whether string is pandigital with number n"""
    if len(str_repr) != n:
        return False

    for i in xrange(n):
        if str(i+1) not in str_repr:
            return False

    return True


def solve(n):
    solutions_set = set()

    current_number = 1
    while True:
        for i in xrange(1, current_number):
            product = i * current_number
            str_repr = "".join(map(str, [product, i, current_number]))
            if is_too_long(str_repr, n):
                break
            if is_pandigital(str_repr, n):
                solutions_set.add(product)
        current_number += 1
        if is_current_number_too_big(current_number, n):
            break
    return sum(solutions_set)


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
            """9
            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass

    def test_is_too_long(self):
        self.assertFalse(is_too_long("111", 3))
        self.assertTrue(is_too_long("1011", 3))

        self.assertFalse(is_too_long("122", 4))
        self.assertFalse(is_too_long("9872", 4))
        self.assertTrue(is_too_long("10990", 4))

        self.assertFalse(is_too_long("9872", 5))
        self.assertFalse(is_too_long("10990", 5))
        self.assertTrue(is_too_long("1110110", 5))
        self.assertTrue(is_too_long("902180", 5))

    def test_is_current_number_too_big(self):
        self.assertFalse(is_current_number_too_big(9, 3))
        self.assertTrue(is_current_number_too_big(10, 3))

        self.assertFalse(is_current_number_too_big(9, 4))
        self.assertTrue(is_current_number_too_big(10, 4))

        self.assertFalse(is_current_number_too_big(99, 5))
        self.assertTrue(is_current_number_too_big(100, 5))

        self.assertFalse(is_current_number_too_big(99, 6))
        self.assertTrue(is_current_number_too_big(100, 6))

        self.assertFalse(is_current_number_too_big(999, 7))
        self.assertTrue(is_current_number_too_big(1000, 7))

    def test_is_pandigital(self):
        self.assertFalse(is_pandigital("01233", 3))
        self.assertFalse(is_pandigital("0123", 3))
        self.assertTrue(is_pandigital("123", 3))

        self.assertTrue(is_pandigital("1234", 4))
        self.assertFalse(is_pandigital("012334", 4))
        self.assertFalse(is_pandigital("01234", 4))

        self.assertTrue(is_pandigital("12345", 5))
        self.assertFalse(is_pandigital("0123345", 5))
        self.assertFalse(is_pandigital("012345", 5))
