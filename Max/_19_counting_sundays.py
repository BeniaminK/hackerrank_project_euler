#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


def progress_month(cur_date):
    year = cur_date[0]
    if cur_date[1] == 12:
        year += 1
        month = 1
    else:
        month = cur_date[1] + 1
    day = 1
    return [year, month, day]


def is_first_earlier_or_same(date_1, date_2):
    if date_1[0] < date_2[0]:
        return True
    elif date_1[0] > date_2[0]:
        return False
    elif date_1[1] < date_2[1]:
        return True
    elif date_1[1] > date_2[1]:
        return False
    elif date_1[2] < date_2[2]:
        return True
    elif date_1[2] > date_2[2]:
        return False
    elif date_1[2] == date_2[2]:
        return True


def zeller_congruence(cur_date):
    q = cur_date[2]
    m = (cur_date[1] - 3) % 12 + 3
    temp_year = cur_date[0] if m <= 12 else (cur_date[0]-1)
    K = temp_year % 100
    J = temp_year / 100
    h = (q + ((13 * (m+1)) / 5) + K + (K / 4) + (J / 4) + 5 * J) % 7
    # print "Date=%s\nq=%d\nm=%d\nK=%d\nJ=%d" % (str(cur_date), q, m, K, J)
    d = ((h + 5) % 7) + 1
    return d


def solve(start, stop):
    ctr = 0
    cur_date = start
    if start[2] != 1:
        cur_date = progress_month(cur_date)
    while is_first_earlier_or_same(cur_date, stop):
        # print [cur_date[0], cur_date[1], cur_date[2]], zeller_congruence(cur_date)
        if zeller_congruence(cur_date) == 7:
            ctr += 1
        cur_date = progress_month(cur_date)
    return ctr


def main():
    T = int(raw_input())
    for i in xrange(T):
        start = map(int, raw_input().split())
        stop = map(int, raw_input().split())
        # print "Z1:", zeller_congruence(start)
        # print "Z2:", zeller_congruence(stop)
        print solve(start, stop)

if __name__ == '__main__':
    main()


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_solver(self):
        import sys
        import StringIO
        input = \
            """12
            2015 2 1
            3015 2 1
1900 1 1
1910 1 1
2000 1 1
2020 1 1
2000 1 1
2000 3 1
1988 3 25
1989 7 13
1924 6 6
1925 6 16
1000000000000 2 2
1000000001000 2 2
2015 2 1
2015 3 1
2000 2 1
2000 10 1
10000000000000000 2 2
10000000000001000 2 2
10000000000001000 2 2
10000000000002000 2 2
10000000000002000 2 2
10000000000003000 2 2
10000000000003000 2 2
10000000000004000 2 2
            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass