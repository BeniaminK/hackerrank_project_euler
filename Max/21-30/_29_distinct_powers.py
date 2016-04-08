#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def brute_force(n):
    powers_set = set()
    for i in xrange(2, n+1):
        for j in xrange(2, n+1):
            powers_set.add(i ** j)
    return len(powers_set)


def count_how_many_less(number, j, k):
    print "%d = %d^%d" % (number, j, k)
    pass


def get_floor_log(maximum_number, base):
    power = 2
    while True:
        if base ** power > maximum_number:
            return power - 1
        else:
            power += 1
    pass


def count_solutions_for(base, maximum_number):
    power_set = set()
    max = get_floor_log(maximum_number, base)
    if max is 1 or max is 0:
        return maximum_number - 1
    for j in xrange(1, max + 1):
        for i in xrange(2, maximum_number + 1):
            power_set.add(i * j)
    return len(power_set)


def smart_solution(n):
    is_power = []
    for i in xrange(2, n):
        for power in xrange(2, n):
            if i ** power <= n:
                is_power.append(i**power)
            else:
                break
    is_power = set(is_power)
    solutions = 0
    for i in xrange(2, n+1):
        if i in is_power:
            continue
        else:
            solutions += count_solutions_for(i, n)
    return solutions


def solve(n):
    return smart_solution(n)
    # return brute_force(n)


def main():
    n = int(raw_input())
    result = solve(n)
    print result
    return result


if __name__ == '__main__':
    main()


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_solver(self):
        import sys
        import StringIO
        inputs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "100", "1000"]
        for idx, input in enumerate(inputs):
            oldstdin = sys.stdin
            oldstdout = sys.stdout
            sys.stdin = StringIO.StringIO(input)
            res = main()
            result = brute_force(int(input))
            self.assertEqual(res, result, "For input: %s result in smart is: %d and in brute force is: %d" % (input, res, result))
            assert (res == result)
        pass