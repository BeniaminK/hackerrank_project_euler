#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


# Dynamic Programming Python implementation of Coin Change problem
def solve(S, m, n):
    # We need n+1 rows as the table is consturcted in bottom up
    # manner using the base case 0 value case (n = 0)
    table = [[0 for x in range(m)] for x in range(n+1)]

    # Fill the enteries for 0 value case (n = 0)
    for i in range(m):
        table[0][i] = 1

    # Fill rest of the table enteries in bottom up manner
    for i in range(1, n+1):
        for j in range(m):
            # Count of solutions including S[j]
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0

            # Count of solutions excluding S[j]
            y = table[i][j-1] if j >= 1 else 0

            # total count
            table[i][j] = x + y
    # for row in table:
    #     print row

    return [table[i][m-1] for i in xrange(n+1)]


def main():

    MAX = 10 ** 5 + 1
    S = [1, 2, 5, 10, 20, 50, 100, 200]
    m = len(S)
    count_result = solve(S, m, MAX)

    T = int(raw_input())
    for i in xrange(T):
        n = int(raw_input())
        print count_result[n] % (10**9+7)

if __name__ == '__main__':
    main()


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_solver(self):
        import sys
        import StringIO
        input = \
            """6
10
15
20
100000
0
10000
            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass