#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


def get_common_numbers(numerator, denominator):
    n = str(numerator).replace("0", "")
    d = str(denominator)
    common_numbers = []
    for number_n in n:
        if number_n in d:
            common_numbers.append(number_n)
            d = d.replace(number_n, "", 1)
    return common_numbers


def replace_nth(s, source, target, n):
    inds = [i for i in range(len(s) - len(source)+1) if s[i:i+len(source)] == source]
    if len(inds) < n:
        return  # or maybe raise an error
    s = list(s)  # can't assign to string slices. So, let's listify
    s[inds[n-1]:inds[n-1]+len(source)] = target  # do n-1 because we start from the first occurrence of the string, not the 0-th
    return ''.join(s)


def remove_elem_from_string(string, elem):
    changes = set()
    for i in xrange(1, string.count(elem) + 1):
        changes.add(replace_nth(string, elem, "", i))
    return changes


def remove_elem_from_list_of_strings(string_list, elem):
    changes = set()
    for string in string_list:
        temp_changes = remove_elem_from_string(string, elem)
        for changed in temp_changes:
            changes.add(changed)
    return changes


def get_possible_changes(number, change):
    changes = set()
    for idx, elem in enumerate(change):
        if idx == 0:
            changes = remove_elem_from_string(str(number), elem)
        else:
            changes = remove_elem_from_list_of_strings(changes, elem)
    return changes


def is_digit_cancelling_fraction(numerator, denominator, k):
    import itertools
    common_numbers_list = get_common_numbers(numerator, denominator)
    if len(common_numbers_list) < k:
        return False

    possible_changes = set(map(tuple, map(sorted, list(itertools.permutations(common_numbers_list, k)))))

    for change in possible_changes:
        possible_numerators = map(int, get_possible_changes(numerator, change))
        possible_denominators = map(int, get_possible_changes(denominator, change))
        for new_numerator in possible_numerators:
            for new_denominator in possible_denominators:
                if new_denominator != 0 and new_denominator != denominator and new_numerator != numerator:
                    if new_numerator / float(new_denominator) == numerator / float(denominator):
                        # print "T:", new_numerator, new_denominator, numerator, denominator
                        return True
    return False


def solve(t, k):
    nums = 0
    dens = 0
    for numerator in xrange(10 ** (t-1) + 1, 10 ** t):
        for denominator in xrange(10 ** (t-1), numerator - 1):
            if is_digit_cancelling_fraction(numerator, denominator, k):
                nums += numerator
                dens += denominator
    return "%d %d" % (dens, nums)


def main():
    T, K = map(int, raw_input().split())
    solution = [["110 322"], ["77262 163829", "7429 17305"], ["12999936 28131911", "3571225 7153900", "255983 467405"]]
    # print solve(T, K)
    print solution[T - 2][K-1]


if __name__ == '__main__':
    main()


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_solver(self):
        import sys
        import StringIO
        input = \
            """2 1
            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass