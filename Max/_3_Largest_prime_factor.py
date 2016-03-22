#!/usr/bin/python
# -*- coding: utf-8 -*-

def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def solve(elem):
    a = factors(elem)
    a = sorted(a)[::-1]
    for elem in a:
        if len(factors(elem)) == 2:
            return elem


def main():
    T = int(input())
    test_cases = [0] * T
    for i in xrange(T):
        test_cases[i] = int(input())

    for elem in test_cases:
        print solve(elem)

if __name__ == '__main__':
    main()