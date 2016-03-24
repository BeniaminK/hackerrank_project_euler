#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


def solve(triangle):
    for i in xrange(1, len(triangle)):
        for idx, val in enumerate(triangle[i]):
            if idx == 0:
                triangle[i][idx] += triangle[i - 1][idx]
            elif idx == i:
                triangle[i][idx] += triangle[i - 1][idx - 1]
            else:
                triangle[i][idx] += max(triangle[i - 1][idx], triangle[i - 1][idx - 1])
    return max(triangle[-1])


def main():
    T = int(input())
    for i in xrange(T):
        n = int(input())
        triangle = []
        for j in xrange(n):
            triangle.append(map(int,raw_input().split()))
        print solve(triangle)

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
4
3
7 4
2 4 6
8 5 9 3"""
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass