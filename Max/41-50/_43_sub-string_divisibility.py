#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


def is_divisable_triplet(number_str, starting_letter, divisor):
    if len(number_str) < starting_letter - 1 + 3:
        return True
    a = "".join(number_str[starting_letter-1:starting_letter + 2])
    return int(a) % divisor == 0


def generate_all_pandigital_primes(n):
    import itertools
    pandigital_primes = []
    num = [str(x) for x in xrange(0, n+1)]
    for elem in itertools.permutations(num):
        # possible_substring = int("".join(elem))
        if not is_divisable_triplet(elem, 2, 2):
            continue
        if not is_divisable_triplet(elem, 3, 3):
            continue
        if not is_divisable_triplet(elem, 4, 5):
            continue
        if not is_divisable_triplet(elem, 5, 7):
            continue
        if not is_divisable_triplet(elem, 6, 11):
            continue
        if not is_divisable_triplet(elem, 7, 13):
            continue
        if not is_divisable_triplet(elem, 8, 17):
            continue
        pandigital_primes.append(int("".join(elem)))
    return pandigital_primes


def solve(n):
    a = generate_all_pandigital_primes(n)
    return sum(filter(lambda x: x <= 10 ** (n + 1), a))


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
            """3
            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass