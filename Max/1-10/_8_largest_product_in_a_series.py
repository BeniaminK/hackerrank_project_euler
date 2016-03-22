#!/usr/bin/python
# -*- coding: utf-8 -*-


def count_prod(numbers, i, k):
    prod = 1
    for ind in xrange(i, i + k):
        prod *= numbers[ind]
    return prod


def solve(n, k):
    current_max = 0
    numbers = []
    while n != 0:
        n, mod = divmod(n, 10)
        numbers.append(mod)

    for i in xrange(0, len(numbers) - k + 1):
        prod = count_prod(numbers, i, k)
        current_max = max(prod, current_max)
    return current_max


def main():

    T = int(input())
    for i in xrange(T):
        size, k = map(int, raw_input().split(" "))
        n = int(raw_input())
        print solve(n, k)

if __name__ == '__main__':
    main()
