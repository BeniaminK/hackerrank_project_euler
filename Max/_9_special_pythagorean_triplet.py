#!/usr/bin/python
# -*- coding: utf-8 -*-


def solve(n):
    pairs = []
    for i in xrange(1, n):
        for j in xrange(i+1, n):
            if i * i + j * j == (n - i - j) ** 2:
                pairs.append((i, j, n - i - j))

    if len(pairs) == 0:
        return -1
    else:
        max_pair = []
        max_prod = 0
        for elem in pairs:
            prod = elem[0] * elem[1] * elem[2]
            if prod > max_prod:
                max_prod = prod
                max_pair = elem
        return max_pair[0] * max_pair[1] * max_pair[2]


def generate_all():
    MAX = 3000
    max_values = [-1 for i in xrange(MAX)]
    for i in xrange(1, MAX):
        for j in xrange(i + 1, MAX):
            if i + j > MAX:
                break
            import math
            k = math.sqrt(i * i + j * j)
            if k.is_integer():
                k = int(k)
                if i + j + k > MAX:
                    break
                else:
                    max_values[i + j + k - 1] = max(i * j * k, max_values[i + j + k - 1])

    return max_values


def main():

    T = int(input())
    max_values = generate_all()
    for i in xrange(T):
        n = int(input())
        print max_values[n-1]

if __name__ == '__main__':
    main()
