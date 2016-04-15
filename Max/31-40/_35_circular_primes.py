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


def get_circulars(arr):
    circulars = []
    for i in xrange(len(arr)):
        new_num = arr[i:] + arr[:i]
        circulars.append(int("".join(map(str, new_num))))
    return circulars


def is_circular_prime(n, sieve):
    factor = 0
    num = n
    while num != 0:
        num /= 10
        factor += 1

    for i in xrange(factor):
        num, mod = divmod(n, 10 ** i)
        is_prime = mod * 10 ** (factor - i) + num
        # print is_prime
        if is_prime not in sieve:
            return False
    return True


def solve(n):
    sieve = sieve_of_eratosthenes(n)
    sum_of_circular_primes = 0
    for i in xrange(2, n):
        if is_circular_prime(i, sieve):
            sum_of_circular_primes += i
    return sum_of_circular_primes


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