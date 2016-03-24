#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


def get_name_of_large_number(number):
    dic = {10**12: "Trillion",
           10**9: "Billion",
           10**6: "Million",
           10**3: "Thousand",
           1: ""}
    return dic[number]


def get_single_number_as_string(val):
    dic = {1:"One",
           2:"Two",
           3:"Three",
           4:"Four",
           5:"Five",
           6:"Six",
           7:"Seven",
           8:"Eight",
           9:"Nine",
           0:"Zero"}
    return dic[val]


def get_tens_number_as_string(val):
    dic = {20:"Twenty",
           30:"Thirty",
           40:"Forty",
           50:"Fifty",
           60:"Sixty",
           70:"Seventy",
           80:"Eighty",
           90:"Ninety"}
    return dic[val]


def get_less_than_twenty_number_as_string(val):
    dic = {10:"Ten",
           11:"Eleven",
           12:"Twelve",
           13:"Thirteen",
           14:"Fourteen",
           15:"Fifteen",
           16:"Sixteen",
           17:"Seventeen",
           18:"Eighteen",
           19:"Nineteen"}
    return dic[val]


def get_hundreds_as_string(hundreds):
    str_val = ""
    if hundreds != 0:
        str_val += get_single_number_as_string(hundreds)
        str_val += " "
        str_val += "Hundred"
    return str_val


def get_less_than_100_as_string(val):
    if val == 0:
        return ""
    elif val < 10:
        return get_single_number_as_string(val)
    elif val < 20:
        return get_less_than_twenty_number_as_string(val)
    else:
        tens, singles = divmod(val, 10)
        return get_tens_number_as_string(tens * 10) + " " + (get_single_number_as_string(singles) if val % 10 != 0 else "")


def get_number_as_string(val):
    str_val = ""
    hundreds, val = divmod(val, 100)
    str_val += get_hundreds_as_string(hundreds)
    str_val += " "
    str_val += get_less_than_100_as_string(val)
    return str_val


def solve(n):
    numbers = []
    if n == 0:
        return get_single_number_as_string(n)
    while n != 0:
        n, mod = divmod(n, 1000)
        numbers.append(mod)

    str_val = ""
    for idx, val in enumerate(numbers[::-1]):
        if val is 0:
            continue
        else:
            str_val += get_number_as_string(val) + " "
            large_number = 10 ** ((len(numbers) - idx - 1) * 3)
            str_val += get_name_of_large_number(large_number) + " "
    return str_val


def main():
    T = int(input())
    import re
    for i in xrange(T):
        n = int(input())
        print re.sub(" +", " ", solve(n).strip())

if __name__ == '__main__':
    main()


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_solver(self):
        import sys
        import StringIO
        input = \
            """20
            30
            0
            20
            10
            17
            104382426112
            100
            1000
            10000
            100000
            1000000
            10000000
            100000000
            1000000000
            10000000000
            100000000000
            1000000000000
            10000000010
            0
            30"""
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass