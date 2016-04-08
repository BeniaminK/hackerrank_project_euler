#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


def solve(n, array):
    return array[n - 1]


def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def generate_sum_of_divisors(max):
    array = [0 for i in xrange(max + 1)]
    for i in xrange(1, max+1):
        factors_i = factors(i)
        array[i] = sum(factors_i) - i
    return array


def get_amicable_array(sum_of_divisors):
    array = [0 for i in xrange(len(sum_of_divisors))]
    for i in xrange(len(array)):
        sum_of_i = sum_of_divisors[i]
        if sum_of_i != i and sum_of_i < len(sum_of_divisors) and sum_of_divisors[sum_of_i] == i:
                array[i] = array[i-1] + i
        else:
            array[i] = array[i-1] if i != 0 else 0
    return array


def main():
    T = int(input())
    MAX = 10 ** 5
    sum_of_divisors = generate_sum_of_divisors(MAX)
    amicable = get_amicable_array(sum_of_divisors)
    for i in xrange(T):
        n = int(input())
        print solve(n, amicable)

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
300
220
284
            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass