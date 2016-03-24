#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

MAX = 500

def solve(N, M, matrix_moves):
    if N < M:
        N, M = M, N
    # N is greater or equal M
    return matrix_moves[N - 1][M - 1]


def count_moves(row, col, matrix_moves):
    cnt_row = row + 1
    cnt_col = col + 1
    # go right
    right_moves = 0
    cur_col = cnt_col - 1
    if cur_col == 0:
        right_moves = 1
    else:
        r = max(cnt_row, cur_col)
        c = min(cnt_row, cur_col)
        right_moves = matrix_moves[r - 1][c - 1]
    #go down
    down_moves = 0
    cur_row = cnt_row - 1
    if cur_row == 0:
        down_moves = 1
    else:
        r = max(cur_row, cnt_col)
        c = min(cur_row, cnt_col)
        down_moves = matrix_moves[r - 1][c - 1]
    return right_moves + down_moves


def generate_all():
    matrix_moves = [[0 for i in xrange(j + 1)] for j in xrange(0, MAX)]

    for row in xrange(0, MAX):
        for col in xrange(0, row + 1):
            matrix_moves[row][col] = count_moves(row, col, matrix_moves)
    return matrix_moves


def main():
    T = int(input())
    mod = 10 ** 9 + 7
    matrix = generate_all()
    for i in xrange(T):
        N, M = map(int, raw_input().split())
        print solve(N, M, matrix) % mod

if __name__ == '__main__':
    main()


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_solver(self):
        import sys
        import StringIO
        input = \
            """2
               2 2
               3 2"""
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass