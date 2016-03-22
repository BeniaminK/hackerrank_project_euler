#!/usr/bin/python
# -*- coding: utf-8 -*-


def generate_multiples(size):
    a = [0 for i in xrange(size)]
    for i in xrange(1, size + 1):
        from fractions import gcd
        if i == 1:
            a[0] = 1
        else:
            a[i-1] = a[i-2] * i / gcd(i, a[i-2])
    return a


if __name__ == '__main__':
    N = int(input())
    minimal_multiples = generate_multiples(40)
    for i in xrange(N):
        number = int(raw_input())
        print minimal_multiples[number - 1]
