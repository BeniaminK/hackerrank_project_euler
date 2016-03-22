#!/usr/bin/python
# -*- coding: utf-8 -*-

def solve(n):
    n -= 1
    trojek = n / 3
    piatek = n / 5
    pietnastek = n / 15
    trojki = (3 + trojek * 3) * trojek / 2
    piatki = (5 + piatek * 5) * piatek / 2
    pietnastki = (15 + pietnastek * 15) * pietnastek / 2
    # print trojki, piatki, pietnastki
    return trojki + piatki - pietnastki


def main():

    T = int(input())
    for i in xrange(T):
        n = int(input())
        print solve(n)

if __name__ == '__main__':
    main()
