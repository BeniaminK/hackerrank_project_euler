#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


def is_string_a_palindrome(string):
    for i in xrange(len(string) / 2):
        if string[i] != string[-1-i]:
            return False
    return True


def str_base(number, base):
    if number < 0:
        return '-' + str_base(-number, base)
    (d, m) = divmod(number, base)
    if d > 0:
        return str_base(d, base) + str(m)
    return str(m)


def next_palindrome(a):
    s = str(a)
    n = len(s)
    k, r = divmod(n, 2)
    if r:
        left, mid, right = s[:k], s[k], s[k+1:]
        assert len(left) == len(right) == k
        assert s == left + mid + right
        mid_n = int(mid)
        if left:
            left_n, right_n, right_n_rev, left_n_rev = int(left), int(right), int(right[::-1]), int(left[::-1])
            if left_n_rev >= right_n:
                return int(left + mid + left[::-1])
            else:
                if mid_n == 9:
                    left_n += 1
                    return int(str(left_n) + '0' + str(left_n)[::-1])
                else:
                    return int(left + str(mid_n+1) + left[::-1])
        else:
            return mid_n  # 1-digit number
    else:
        left, right = s[:k], s[k:]
        assert len(left) == len(right) == k
        assert s == left + right
        left_n, right_n, left_n_rev = int(left), int(right), int(left[::-1])
        if right_n <= left_n_rev:
            return int(left + left[::-1])
        else:
            new_left = str(left_n + 1)
            return int(new_left + new_left[::-1])


def solve(n, k):
    sum_of_palindromes = 0
    palindrome = next_palindrome(1)
    while palindrome < n:
        base_k = str_base(palindrome, k)
        if is_string_a_palindrome(base_k):
            sum_of_palindromes += palindrome
        palindrome = next_palindrome(palindrome + 1)
    return sum_of_palindromes


def main():
    N, K = map(int, raw_input().split())
    print solve(N, K)

if __name__ == '__main__':
    main()


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_solver(self):
        import sys
        import StringIO
        input = \
            """1000000 9
            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass