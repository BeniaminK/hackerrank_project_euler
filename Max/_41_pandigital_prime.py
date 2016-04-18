#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


def is_prime(possible_prime):
    for i in range(2, int(possible_prime ** 0.5) + 1):
        if possible_prime % i == 0:
            return False
    return True


def solve(n, all_primes):
    import bisect
    idx = bisect.bisect_left(all_primes, n)
    if idx < len(all_primes) and all_primes[idx] == n:
        return all_primes[idx]
    else:
        return all_primes[idx-1]


def generate_all_pandigital_primes():
    import itertools
    pandigital_primes = [-1]
    for i in xrange(2, 10):
        if i in [2, 3, 5, 6, 8, 9]:
            continue
        num = [str(x) for x in xrange(1, i + 1)]
        for elem in itertools.permutations(num):
            possible_prime = int("".join(elem))
            if is_prime(possible_prime):
                pandigital_primes.append(possible_prime)
    return pandigital_primes


def main():
    T = int(raw_input())
    all_table = sorted(generate_all_pandigital_primes())
    for i in xrange(T):
        n = int(raw_input())
        print solve(n, all_table)

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
            100
            10000
            10000000000
            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass