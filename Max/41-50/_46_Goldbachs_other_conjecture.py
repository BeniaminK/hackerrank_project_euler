#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

def sieve_of_eratosthenes(max):
    primes = set()
    numbers = [i for i in xrange(2, max + 1)]
    for i in xrange(len(numbers)):
        num = numbers[i]
        if num == -1:
            continue
        else:
            primes.add(num)
            for j in xrange(i, len(numbers), num):
                numbers[j] = -1
    return primes

def solve(n, primes, squares):
    posible_solutions = 0
    for prime in primes:
        if prime % 2 == 0:
            continue
        if prime >= n:
            break
        a = (n - prime) / 2
        if a in squares:
            posible_solutions += 1
    return posible_solutions


def main():
    MAX = 5 * 10 ** 5
    primes = sorted(sieve_of_eratosthenes(MAX))
    squares = set([x ** 2 for x in xrange(1, int(MAX ** 0.5))])
    T = int(raw_input())
    for i in xrange(T):
        n = int(raw_input())
        print solve(n, primes, squares)

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
            9
            15
            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass