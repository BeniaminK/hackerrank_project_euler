#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


def get_recurring_cycle_length(d):
    # type: (int) -> int
    a = [0] * d
    num = 1
    iter = 1
    while True:
        num *= 10
        num %= d
        if num is 0:
            return 0
        elif a[num] is not 0:
            return iter - a[num]
        else:
            a[num] = iter
            iter += 1


def solve(n, longest_cycle):
    import bisect
    index = bisect.bisect_left(longest_cycle, n)
    return longest_cycle[index - 1]


def get_cycles_length(MAX):
    cycles_length = [0] * (MAX + 1)
    for i in xrange(1, MAX + 1):
        cycles_length[i] = get_recurring_cycle_length(i)
    return cycles_length


def get_longest_cycles(cycles_length):
    longest_cycles = [0]
    for i in xrange(1, len(cycles_length)):
        if cycles_length[i] > longest_cycles[-1]:
            longest_cycles.append(i)
    return longest_cycles


def main():
    T = int(raw_input())
    MAX = 10000
    cycles_length = get_cycles_length(MAX)
    longest_cycles = get_longest_cycles(cycles_length)
    for i in xrange(T):
        n = int(raw_input())
        print solve(n, longest_cycles)

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
5
10
17
            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass