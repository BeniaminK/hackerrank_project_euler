#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite


def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653:
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s)
                   for a in _known_primes[:_precision_for_huge_n])

_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]


def sieve_of_eratosthenes(limit):
    primes = []
    numbers = [i for i in xrange(2, limit + 1)]
    for i in xrange(len(numbers)):
        num = numbers[i]
        if num == -1:
            continue
        else:
            primes.append(num)
            for j in xrange(i, len(numbers), num):
                numbers[j] = -1
    return primes


def solve(array, max_val):
    import bisect
    max_val_idx = min(bisect.bisect_right(array, max_val), len(array))

    sums_from_start = [0] * max_val_idx

    for idx in xrange(max_val_idx):
        sums_from_start[idx] = (sums_from_start[idx - 1] if idx != 0 else 0) + array[idx]

    # print max_val, sums_from_start
    longest_sum = 0
    sum_value = 0

    # print max_val, sums_from_start[:10], max_val_idx, array[max_val_idx]

    for idx in xrange(max_val_idx):
        if idx >= max_val_idx - longest_sum:
            break
        if array[idx] * longest_sum > max_val:
            # print "Shouldn't happen then..."
            break
        value_to_substract = sums_from_start[idx - 1] if idx != 0 else 0
        loop_2_start = max_val + value_to_substract
        second_idx = bisect.bisect_left(sums_from_start, loop_2_start)
        second_loop_start_idx = min(second_idx if sums_from_start[second_idx] == loop_2_start else second_idx - 1, max_val_idx-1)
        # print value_to_substract, loop_2_start, second_loop_start_idx

        for i in xrange(second_loop_start_idx, idx + longest_sum - 1, -1):
            # print idx, i, second_loop_start_idx
            possible_num = sums_from_start[i] - value_to_substract
            sum_length = i - idx + 1
            # print possible_num, max_val
            if is_prime(possible_num) and sum_length > longest_sum:
                # print "Primes sum: %-5d From %-5d Length: %-3d" % (possible_num, array[idx], sum_length)
                    longest_sum = sum_length
                    sum_value = possible_num
                    # return longest_sum, sum_value
                    break
    return sum_value, longest_sum


MAX_SIEVE = 10 ** 7
primes = sieve_of_eratosthenes(MAX_SIEVE)


def main():
    T = int(raw_input())
    for i in xrange(T):
        n = int(raw_input())
        sum_primes, length = solve(primes, n)
        print sum_primes, length


if __name__ == '__main__':
    main()


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_solutions(self):
        self.assertEqual((2, 1), solve(primes, 2))
        self.assertEqual((2, 1), solve(primes, 3))
        self.assertEqual((2, 1), solve(primes, 4))
        self.assertEqual((5, 2), solve(primes, 5))
        self.assertEqual((5, 2), solve(primes, 16))
        self.assertEqual((17, 4), solve(primes, 17))
        self.assertEqual((17, 4), solve(primes, 18))
        self.assertEqual((17, 4), solve(primes, 29))
        self.assertEqual((17, 4), solve(primes, 30))
        self.assertEqual((17, 4), solve(primes, 40))
        self.assertEqual((41, 6), solve(primes, 41))
        self.assertEqual((41, 6), solve(primes, 42))
        self.assertEqual((127, 9), solve(primes, 127))
        self.assertEqual((127, 9), solve(primes, 128))
        self.assertEqual((499, 17), solve(primes, 570))
        self.assertEqual((41, 6), solve(primes, 100))
        self.assertEqual((953, 21), solve(primes, 1000))
        self.assertEqual((9521, 65), solve(primes, 10000))
        self.assertEqual((99819619, 4685), solve(primes, 100000000))
        self.assertEqual((999973156643, 379317), solve(primes, 1000000000000))


    def test_solver(self):
        import sys
        import StringIO
        input = \
            """10
            1000000000000
            1000000000000
            1000000000000
            1000000000000
            1000000000000
            1000000000000
            1000000000000
            1000000000000
            1000000000000
            1000000000000
            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass