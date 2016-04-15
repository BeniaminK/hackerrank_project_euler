#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


def sieve_of_eratosthenes(max, min = -1):
    primes = set()
    numbers = [i for i in xrange(2, max + 1)]
    for i in xrange(len(numbers)):
        num = numbers[i]
        if num == -1:
            continue
        else:
            if num >= min:
                primes.add(num)
            for j in xrange(i, len(numbers), num):
                numbers[j] = -1
    return primes


def gen_primes_up_to(n):
    primes = sieve_of_eratosthenes(n)
    return primes


def get_truncates(prime):
    numbers = []
    divisor = 10
    import math
    log = int(math.ceil(math.log(prime, 10)))
    while divisor < 10 ** log:
        div, mod = divmod(prime, divisor)
        numbers.append(div)
        numbers.append(mod)
        divisor *= 10
    return numbers


def solve(n):
    primes = gen_primes_up_to(n)

    sum_of_primes = 0
    for prime in primes:
        if prime < 10:
            continue
        truncates = get_truncates(prime)
        is_truncable = True
        for possible_prime in truncates:
            if possible_prime not in primes:
                is_truncable = False
                break
        if is_truncable:
            sum_of_primes += prime
    return sum_of_primes


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
            """100
            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass
