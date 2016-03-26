#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


def get_next_fibo(fibo, fibo_prev, iter):
    if iter == 1:
        return 1, 1, 2
    else:
        return fibo + fibo_prev, fibo, iter + 1


def generate_fibonacci(max_number_length):
    memo_fibonacci = [0] * (max_number_length + 1)
    fibo = 1
    fibo_prev = None
    iter = 1
    while memo_fibonacci[max_number_length] == 0:
        length_fibo = len(str(fibo))
        if memo_fibonacci[length_fibo] == 0:
            memo_fibonacci[length_fibo] = iter
        fibo, fibo_prev, iter = get_next_fibo(fibo, fibo_prev, iter)
    return memo_fibonacci


def main():
    T = int(raw_input())
    MAX = 5000
    fibos = generate_fibonacci(MAX)
    for i in xrange(T):
        n = int(raw_input())
        print fibos[n]

if __name__ == '__main__':
    main()


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_solver(self):
        import sys
        import StringIO
        input = \
            """4
            1
            2
            3
            4
            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass