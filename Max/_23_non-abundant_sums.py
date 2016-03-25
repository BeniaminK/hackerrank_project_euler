#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest



def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))



def can_be_expressed_as_sum(n, abundants_arr):
    import bisect
    elem = abundants_arr[0]
    for val in abundants_arr:
        if 2 * val > n:
            break
        idx = bisect.bisect_left(abundants_arr, n - val)
        if abundants_arr[idx] + val == n:
            return True
    return False


def solve(n, abundants_arr):
    if can_be_expressed_as_sum(n, abundants_arr):
        return "YES"
    else:
        return "NO"

def generate_sum_of_divisors(max):
    array = [0 for i in xrange(max + 1)]
    for i in xrange(1, max+1):
        factors_i = factors(i)
        array[i] = sum(factors_i) - i
    return array

def generate_abundants(MAX):
    sum_of_divisors = generate_sum_of_divisors(MAX)
    abundants = []
    for idx, val in enumerate(sum_of_divisors):
        if val > idx:
            abundants.append(idx)
    return abundants


def main():
    T = int(raw_input())
    MAX = 10 ** 5
    abundants = generate_abundants(MAX)
    for i in xrange(T):
        n = int(raw_input())
        print solve(n, abundants)

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
24
49

            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass