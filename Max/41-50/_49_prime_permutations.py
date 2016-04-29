#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


class solution:

    _k = 0

    def __init__(self, first, diff):
        self.first = first
        self.diff = diff

    def __eq__(self, other):
        return other.first == self.first and other.diff == self.diff

    def __hash__(self):
        return (hash(self.first) << 64) + hash(self.diff)

    def __cmp__(self, other):
        if self.first == other.first:
            return self.diff - other.diff
        else:
            return self.first - other.first

    def __repr__(self):
        return "%d|%d" % (self.first, self.diff)

    @staticmethod
    def set_k(k):
        solution._k = k

    def __str__(self):
        s = ""
        # print solution._k
        for i in xrange(solution._k):
            s += str(self.first + i * self.diff)
        return s

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


def is_permutation(num_1, num_2):
    str_1 = "".join(sorted(str(num_1)))
    str_2 = "".join(sorted(str(num_2)))
    return str_1 == str_2


def is_in_sorted_array(a, x, low_bound):
    import bisect
    idx = bisect.bisect_left(a, x, lo=low_bound)
    return idx < len(a) and a[idx] == x


def solve(k, n, numbers_set):
    elems = set()
    for idx, number in enumerate(numbers_set):
        if number > n:
            break
        # if idx % 1000 == 0:
        #     print idx, number
        import itertools
        str_number = str(number)
        for str_permutation in itertools.permutations(str_number):
            # print str_permutation
            elem = int("".join(str_permutation))
            if is_in_sorted_array(numbers_set, elem, idx + 1) and elem > number:
                if len(repr(elem)) > len(repr(number)):
                    print "It shouldn't get here unless 0 first. Numbers: ", elem, number
                    continue



                # they are same size
                diff = elem - number

                if len(repr(number)) != len(repr(number + (k - 1) * diff)):
                    continue

                is_good = True
                for i in xrange(k-2):
                    iter_i = number + (i + 2) * diff
                    if not is_permutation(iter_i, number) or not is_in_sorted_array(numbers_set, iter_i, idx + i + 2):
                        is_good = False
                        break

                if is_good:
                    elems.add(solution(number, diff))

        return elems


def solve_small(k, n, numbers_set):
    elems = set()
    if len(numbers_set) < k:
        return elems
    for idx, number in enumerate(numbers_set):
        if number >= n:
            return elems
        for i in xrange(idx + 1, len(numbers_set)):
            num_to_compare = numbers_set[i]

            # they are same size
            diff = num_to_compare - number

            if len(repr(number)) != len(repr(number + (k - 1) * diff)):
                continue

            is_good = True
            for i in xrange(k - 2):
                iter_i = number + (i + 2) * diff
                if not is_permutation(iter_i, number) or not is_in_sorted_array(numbers_set, iter_i, idx + i + 2):
                    is_good = False
                    break

            if is_good:
                elems.add(solution(number, diff))
    return elems


def get_list_sorted_by_size(primes):
    elems = {}
    for prime in primes:
        l = len(str(prime))
        if l in elems:
            elems[l].append(prime)
        else:
            elems[l] = [prime]
    return elems

def get_list_sorted_by_keys(primes):
    elems = {}
    for prime in primes:
        key = "".join(sorted(str(prime)))
        if key in elems:
            elems[key].append(prime)
        else:
            elems[key] = [prime]
    return elems


def main():
    N, K = map(int, raw_input().split())
    solution.set_k(K)
    MAX = 10 ** 6
    primes = filter(lambda x: x >= 1000, sieve_of_eratosthenes(MAX))
    primes_by_pow10 = get_list_sorted_by_keys(primes)
    solutions = []
    for key in primes_by_pow10:
        solutions.extend(solve_small(K, N, sorted(primes_by_pow10[key])))
        # print time.time(), "Key: ", key
    for elem in sorted(solutions):
        print str(elem)
    # print sorted(solutions)

if __name__ == '__main__':
    main()


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_solver(self):
        import sys
        import StringIO
        input = \
            """1000000 4
               1000000 3
            1000000 4
            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass