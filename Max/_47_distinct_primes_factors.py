#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


def sieve_of_eratosthenes(limit):
    primes = set()
    numbers = [i for i in xrange(2, limit + 1)]
    for i in xrange(len(numbers)):
        num = numbers[i]
        if num == -1:
            continue
        else:
            primes.add(num)
            for j in xrange(i, len(numbers), num):
                numbers[j] = -1
    return primes


def factors(n, primes):
    factors_set = set()

    for prime in primes:
        while n % prime == 0:
            factors_set.add(prime)
            n /= prime
        if prime > n:
            break
    return factors_set


def gen(val, n, k, *solutions):
    numbers = [1]
    mnoznik = set()
    while len(numbers) is not 0:
        num = numbers.pop()
        mnoznik.add(num)
        for divisor in solutions:
            if val * num * divisor <= n + k - 1:
                numbers.append(num * divisor)
    return mnoznik


def calculate_primes_factors(n, k, values, *solutions):
    value = 1
    for elem in solutions:
        value *= elem
    numbers = gen(value, n, k, *solutions)
    for elem in numbers:
        values[value * elem] = 1

    return


def gen_solution_packs(n, k, primes):
    """
    :param n: maximum number to stop at
    :param k: count of numbers to join together
    :param primes: list of possible numbers
    :return: k-element groups of elements in primes, in which their multiplication is <=n
    """
    import itertools
    solution_pack = []
    for combination in itertools.combinations(primes, k):
        result = 1
        for elem in combination:
            result *= elem
        if result <= n + k - 1:
            solution_pack.append(combination)
    return solution_pack


def gen_solution_packs2(n, numbers_length, primes):
    """ Faster than above but more code to write and less dynamic.
    :param n:
    :param numbers_length:
    :param primes:
    :return:
    """
    solution_pack = []
    max_limit = n + numbers_length - 1
    if numbers_length == 2:
        for i in xrange(0, len(primes) - 1):
            if primes[i] * primes[i+1] > max_limit:
                break
            for j in xrange(i + 1, len(primes)):
                if primes[i] * primes[j] > max_limit:
                    break
                else:
                    solution_pack.append((primes[i], primes[j]))
    elif numbers_length == 3:
        for i in xrange(0, len(primes) - 2):
            if primes[i] * primes[i + 1] * primes[i+2] > max_limit:
                break
            for j in xrange(i + 1, len(primes) - 1):
                if primes[i] * primes[j] * primes[j+1] > max_limit:
                    break
                for k in xrange(j + 1, len(primes)):
                    if primes[i] * primes[j] * primes[k] > max_limit:
                        break
                    else:
                        solution_pack.append((primes[i], primes[j], primes[k]))
    elif numbers_length == 4:
        for i in xrange(0, len(primes) - 3):
            if primes[i] * primes[i + 1] * primes[i+2] * primes[i+3] > max_limit:
                break
            for j in xrange(i + 1, len(primes) - 2):
                if primes[i] * primes[j] * primes[j+1] * primes[j+2] > max_limit:
                    break
                for k in xrange(j + 1, len(primes) - 1):
                    if primes[i] * primes[j] * primes[k] * primes[k+1] > max_limit:
                        break
                    for l in xrange(k + 1, len(primes) - 1):
                        if primes[i] * primes[j] * primes[k] * primes[l] > max_limit:
                            break
                        else:
                            solution_pack.append((primes[i], primes[j], primes[k], primes[l]))
    return solution_pack



def solve(n, k):
    import time
    # print time.time(), "START"
    primes = sorted(sieve_of_eratosthenes(n))
    # print time.time(), "Sito Eratostenesa"
    values = [0] * (n + k)
    # print time.time(), "values"
    # solution_pack = gen_solution_packs(n, k, primes)
    solution_pack = gen_solution_packs2(n, k, primes)
    # print time.time(), "solution_pack"
    for solution in solution_pack:
        calculate_primes_factors(n, k, values, *solution)
    # print time.time(), "odpowiedzi"

    in_a_row = 0
    solution = []
    for i in xrange(0, n + k):
        if values[i] == 1:
            in_a_row += 1
        else:
            in_a_row = 0

        if in_a_row >= k:
            solution.append(i - k + 1)
        else:
            pass
    # print time.time()
    return "\n".join(map(str, solution)).strip()


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
            """644 3
            2000000 3
            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass
