#!/usr/bin/python
# -*- coding: utf-8 -*-


SIZE = 20
WINDOW = 4


def get_max_horiz(grid):
    max_horiz = 0
    for row in xrange(SIZE):
        for col in xrange(SIZE - WINDOW + 1):
            prod = 1
            for elem in xrange(WINDOW):
                prod *= grid[row][col + elem]
            max_horiz = max(max_horiz, prod)
    return max_horiz


def get_max_vert(grid):
    max_vert = 0
    for row in xrange(SIZE - WINDOW + 1):
        for col in xrange(SIZE):
            prod = 1
            for elem in xrange(WINDOW):
                prod *= grid[row + elem][col]
                max_vert = max(max_vert, prod)
    return max_vert


def get_max_diag_right(grid):
    max_diag_right = 0
    for row in xrange(SIZE - WINDOW + 1):
        for col in xrange(SIZE - WINDOW + 1):
            prod = 1
            for elem in xrange(WINDOW):
                prod *= grid[row + elem][col + elem]
                max_diag_right = max(max_diag_right, prod)
    return max_diag_right


def get_max_diag_left(grid):
    max_diag_left = 0
    for row in xrange(SIZE - WINDOW + 1):
        for col in xrange(WINDOW - 1, SIZE):
            prod = 1
            for elem in xrange(WINDOW):
                prod *= grid[row + elem][col - elem]
                max_diag_left = max(max_diag_left, prod)
    return max_diag_left


def solve(grid):
    max_horiz = get_max_horiz(grid)
    max_vert = get_max_vert(grid)
    max_diag_right = get_max_diag_right(grid)
    max_diag_left = get_max_diag_left(grid)
    max_prod = max(max_diag_left, max_diag_right, max_vert, max_horiz)
    return max_prod


def main():
    grid = [0 for j in xrange(SIZE)]
    for i in xrange(SIZE):
        row = raw_input()
        grid[i] = map(int, row.split())
    print solve(grid)

if __name__ == '__main__':
    main()

import unittest
class MyTest(unittest.TestCase):

    def setUp(self):
        global SIZE
        global WINDOW
        SIZE = 5
        WINDOW = 3
        pass

    def testSolve(self):
        input_hor = \
            """ 10 10 10 10 10
                10 10 10 10 10
                10 10 10 10 10
                10 10 10 10 10
                10 10 20 20 20 """
        input_ver = \
            """ 10 10 10 10 10
                10 10 10 10 10
                10 10 10 10 20
                10 10 10 10 20
                10 10 10 10 20 """
        input_diag_right = \
            """ 10 10 10 10 10
                10 10 10 10 10
                10 10 20 10 10
                10 10 10 20 10
                10 10 10 10 20 """
        input_diag_left = \
            """ 10 10 10 10 10
                10 10 10 10 10
                10 10 20 10 10
                10 20 10 20 30
                20 10 10 30 10 """
        output = 73812150
        import sys
        import StringIO

        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input_diag_left)
        main()
        pass