#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
2
10
100
"""

fibonacci = []
nums = []
fibo_even = []


def solve(elem):
    import bisect
    return fibo_even[bisect.bisect_left(nums, elem) - 1]


def generate_fibonacci(max_n):
    global fibonacci, nums, fibo_even
    fibonacci.append(1)
    fibonacci.append(2)

    while fibonacci[len(fibonacci) - 1] < max_n:
        fibo_minus_2 = fibonacci[len(fibonacci) - 2]
        fibo_minus_1 = fibonacci[len(fibonacci) - 1]
        fibonacci.append(fibo_minus_2 + fibo_minus_1)

    for i in xrange(len(fibonacci)):
        if fibonacci[i] % 2 is 0:
            if len(nums) == 0:
                fibo_even.append(fibonacci[i])
                nums.append(fibonacci[i])
            else:
                fibo_even.append(fibonacci[i] + fibo_even[len(nums) - 1])
                nums.append(fibonacci[i])


def main():
    T = int(input())
    test_cases = [0] * T
    for i in xrange(T):
        test_cases[i] = int(input())

    max_n = max(test_cases)
    generate_fibonacci(max_n)

    for elem in test_cases:
        print solve(elem)

if __name__ == '__main__':
    main()
