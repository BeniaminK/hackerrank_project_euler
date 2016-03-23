#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


def solve(n):
    return


def main():
    T = int(input())
    total = 0
    for i in xrange(T):
        n = int(input())
        total += n
    print str(total)[:10]

if __name__ == '__main__':
    main()


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_solver(self):
        import sys
        import StringIO
        input = \
        """5
37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676"""
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass