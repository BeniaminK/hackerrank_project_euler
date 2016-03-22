#!/usr/bin/python
# -*- coding: utf-8 -*-


def sum_of_squares(n):
    squares_sum = (2 * n**3 + 3 * n**2 + n) / 6
    return squares_sum


def square_of_sum(n):
    squares_sum = (n * (n + 1)) / 2
    return squares_sum ** 2


if __name__ == '__main__':
    N = int(input())
    for i in xrange(N):
        number = int(raw_input())
        print square_of_sum(number) - sum_of_squares(number)
