#!/usr/bin/python
# -*- coding: utf-8 -*-


def sieve_of_eratosthenes(max):
    primes = []
    numbers = [i for i in xrange(2, max + 1)]
    for i in xrange(len(numbers)):
        num = numbers[i]
        if num == -1:
            continue
        else:
            primes.append(num)
            for j in xrange(i, len(numbers), num):
                numbers[j] = -1
    return primes


def sum_primes(primes):
    sums = [0 for i in xrange(len(primes) + 1)]
    for i in xrange(len(primes)):
        prev = sums[i - 1] if i != 0 else 0
        sums[i] = primes[i] + prev
    return sums


if __name__ == '__main__':
    MAX = 10 ** 6
    primes = sieve_of_eratosthenes(MAX)
    primes_sum = sum_primes(primes)
    import bisect
    N = int(input())
    for i in xrange(N):
        number = int(raw_input())
        index = bisect.bisect_left(primes, number)
        if primes[index] == number:
            print primes_sum[index]
        else:
            print primes_sum[index - 1]
