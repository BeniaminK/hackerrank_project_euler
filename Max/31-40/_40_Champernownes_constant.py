#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


MAX = 10 ** 18


def get_digit_at(idx, start_positions):
    import bisect
    digits_count = bisect.bisect_right(start_positions, idx)
    start = start_positions[digits_count - 1]

    div, mod = divmod(idx - start, digits_count)
    return int(str(10 ** (digits_count - 1) + div)[mod])


def solve(idx_numbers, start_positions):
    # type: (list) -> int
    product = 1
    for idx in idx_numbers:
        product *= get_digit_at(idx, start_positions)
    return product


def get_start_positions(MAX):
    start_positions = [1]
    power = 1
    while start_positions[-1] < MAX:
        start_positions.append(start_positions[-1] + power * (10 ** power - 10 ** (power-1)))
        power += 1
    return start_positions


def main():
    T = int(raw_input())
    start_positions = get_start_positions(MAX)
    for i in xrange(T):
        i_array = map(int, raw_input().split())
        print solve(i_array, start_positions)

if __name__ == '__main__':
    main()


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_solver(self):
        import sys
        import StringIO
        input = \
            """1
            1 2 3 4 5 6 7 10 12
            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass