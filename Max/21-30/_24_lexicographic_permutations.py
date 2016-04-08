#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


def solve(text, sizes, n):
    used_text = text
    solution = ""
    n -= 1
    for idx, val in enumerate(sizes[1:]):
        div, n = divmod(n, val)
        solution += used_text[div]
        used_text = used_text.replace(used_text[div], "")
    return solution + used_text


def get_sizes(size):
    sizes = [0] * size
    for i in xrange(size):
        if i == 0:
            sizes[i] = 1
        else:
            sizes[i] = sizes[i-1] * (i+1)
    return sizes[::-1]


def main():
    T = int(raw_input())
    TEXT = "abcdefghijklm"
    sizes_array = get_sizes(len(TEXT))
    for i in xrange(T):
        n = int(raw_input())
        print solve(TEXT, sizes_array, n)

if __name__ == '__main__':
    main()


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_solver(self):
        import sys
        import StringIO
        input = \
            """15
            1
            2
            3
            4
            5
            6
            21321
            2143213
            456
            56
            21322
            21323
            21324
            21325
            67876898
            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass