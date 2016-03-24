#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


def get_all_max_collatz_sequences(max):
    sequences = [0 for i in xrange(max)]
    for i in xrange(1, max + 1):
        length = 0
        cur_num = i
        while cur_num != 1:
            length += 1
            if cur_num % 2 is 0:
                cur_num /= 2
            else:
                cur_num = 3 * cur_num + 1
            if cur_num < i:
                length += sequences[cur_num - 1] - 1
                cur_num = 1
        sequences[i - 1] = length + 1
    return sequences


def get_solution_array_from(max_collatz_sequences):
    array = [0]
    sizes = [0]
    for idx, val in enumerate(max_collatz_sequences):
        if max_collatz_sequences[array[-1]] <= val:
            array.append(idx)
            sizes.append(val)
        else:
            pass

    array = [i + 1 for i in array[1:]]
    return array, sizes


def main():
    MAX = 5 * 10 ** 6
    T = int(raw_input())
    max_collatz_sequences = get_all_max_collatz_sequences(MAX)
    solution_array, sizes = get_solution_array_from(max_collatz_sequences)
    # solution_array = [1, 2, 3, 6, 7, 9, 18, 19, 25, 27, 54, 55, 73, 97, 129, 171, 231, 235, 313, 327, 649, 654, 655, 667, 703, 871, 1161, 2223, 2322, 2323, 2463, 2919, 3711, 6171, 10971, 13255, 17647, 17673, 23529, 26623, 34239, 35497, 35655, 52527, 77031, 106239, 142587, 156159, 216367, 230631, 410011, 511935, 626331, 837799, 1117065, 1126015, 1501353, 1564063, 1723519, 2298025, 3064033, 3542887, 3732423]
    for i in xrange(T):
        n = int(raw_input())
        import bisect
        index = bisect.bisect_left(solution_array, n)
        if index == len(solution_array):
            print solution_array[-1]
        elif solution_array[index] == n:
            print solution_array[index]
        else:
            print solution_array[index - 1]

if __name__ == '__main__':
    main()


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_solver(self):
        import sys
        import StringIO
        input = \
        """14
        10
        3542886
        3542887
        3542888
        15
        20
        1
        3
        100000
        5000000
        1723518
        19
        26
        28
        """

        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass