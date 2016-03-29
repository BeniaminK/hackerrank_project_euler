#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


def primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]


def get_prime_streak(a, b, primes):
    import bisect
    streak = 0
    n = 0
    while True:
        val = n * n + a * n + b
        index = bisect.bisect_left(primes, val)
        if index < len(primes) and primes[index] == val:
            streak += 1
            n += 1
        else:
            return streak


def solve(n):
    MAX = 2000
    primes = primes1(MAX)
    possible_b_values = filter(lambda x: x < n, primes)
    current_max = (0, 0)
    longest_streak = 0
    for b in possible_b_values:
        for a in xrange(-n, n+1):
            streak = get_prime_streak(a, b, primes)
            if streak > longest_streak:
                current_max = (a,b)
                longest_streak = streak
    return "%d %d" % (current_max[0], current_max[1])


def main():
    n = int(raw_input())
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
            """2000
            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass