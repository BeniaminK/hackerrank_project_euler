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


if __name__ == '__main__':
    MAX = int(1.05 * 10 ** 5)
    primes = sieve_of_eratosthenes(MAX)
    print len(primes)
    N = int(input())
    for i in xrange(N):
        number = int(raw_input())
        print primes[number - 1]
