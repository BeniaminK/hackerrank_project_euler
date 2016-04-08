#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


def solve(n):
    solutions = []
    for i in xrange(10, 600000):
        b = map(int, str(i))
        sum_of_nth_powers = 0
        for elem in b:
            sum_of_nth_powers += elem ** n
        if sum_of_nth_powers == i:
            solutions.append(sum_of_nth_powers)
    return sum(solutions)


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
        inputs = ["3", "4", "5", "6"]
        for idx, input in enumerate(inputs):
            oldstdin = sys.stdin
            oldstdout = sys.stdout
            sys.stdin = StringIO.StringIO(input)
            res = main()
            # result = brute_force(int(input))
            # self.assertEqual(res, result,
            #                  "For input: %s result in smart is: %d and in brute force is: %d" % (input, res, result))
        pass
        pass