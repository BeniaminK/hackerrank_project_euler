#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def solve(n, numbers, factor_numbers):
    import bisect
    index = bisect.bisect_left(factor_numbers, n + 1)

    return numbers[index]


def generate_all():
    MAX_SIZE = 10 ** 3
    numbers = [1]
    factors_num_arr = [1]
    left = MAX_SIZE
    iter = 2
    while factors_num_arr[-1] < MAX_SIZE:
        number = ((0 + iter) * (iter + 1)) / 2
        factors_num = len(factors(number))

        if factors_num > factors_num_arr[-1]:
            numbers.append(number)
            factors_num_arr.append(factors_num)
            # print "Found: %d with %d factors." % (number, factors_num)
        iter += 1
    return numbers, factors_num_arr

def get_generated_all():
    numbers = [1, 3, 6, 28, 36, 120, 300, 528, 630, 2016, 3240, 5460, 25200, 73920, 157080, 437580, 749700, 1385280, 1493856,
     2031120, 2162160, 17907120, 76576500, 103672800, 236215980, 842161320]
    factors_num_arr = [1, 2, 4, 6, 9, 16, 18, 20, 24, 36, 40, 48, 90, 112, 128, 144, 162, 168, 192, 240, 320, 480, 576, 648, 768, 1024]
    return numbers, factors_num_arr


def main():
    T = int(input())
    numbers, factors_num_arr = get_generated_all()
    # print numbers
    # print factors_num_arr
    for i in xrange(T):
        n = int(input())
        print solve(n, numbers, factors_num_arr)

if __name__ == '__main__':
    main()


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_solver(self):
        import sys
        import StringIO
        input = "5\n1\n2\n3\n4\n500"
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass