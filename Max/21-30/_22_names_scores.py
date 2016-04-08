#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


def get_name_score(name):
    score = 0
    for elem in name:
        score += ord(elem) - 64
    return score


def solve(name, name_list):
    score = get_name_score(name)
    # print "Score: %d" % (score)
    import bisect
    idx = bisect.bisect_left(name_list, name) + 1
    # print "Index of %s in %s is %d" % (name, name_list, idx)
    score *= idx
    return score


def main():
    T = int(raw_input())
    names = [None for i in xrange(T)]
    for i in xrange(T):
        n = raw_input()
        names[i] = n
    names = sorted(names)
    T = int(raw_input())
    for i in xrange(T):
        name = raw_input()
        print solve(name, names)

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
ALEX
LUIS
JAMES
BRIAN
PAMELA
1
PAMELA
            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass