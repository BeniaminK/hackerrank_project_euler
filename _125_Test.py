#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import time


class MyTest(unittest.TestCase):

    def setUp(self):
        from _125_Palindromic_sums import find_all_palindromes, init_squares
        find_all_palindromes(10 ** 9)
        init_squares(10 ** 9)

    def testSolve(self):
        start_time = time.time()
        from _125_Palindromic_sums import solve_math, solve_rev
        # self.assertEqual(solve(1000, 1), 4164)
        # self.assertEqual(solve(1000, 2), 3795)
        # # self.assertEqual(solve(10000000, 1444), 6079706)
        # self.assertEqual(solve(1, 1), 0)
        # self.assertEqual(solve(5, 1), 5)
        # self.assertEqual(solve(6, 1), 5)
        # self.assertEqual(solve(1000000000, 1000000000), 0)
        # print("--- %s seconds ---" % (time.time() - start_time))
        self.assertEqual(solve_math(1000, 1), 4164)
        self.assertEqual(solve_math(1000, 2), 3795)
        self.assertEqual(solve_math(10000000, 1444), 6079706)
        self.assertEqual(solve_math(1, 1), 0)
        self.assertEqual(solve_math(5, 1), 5)
        self.assertEqual(solve_math(6, 1), 5)
        self.assertEqual(solve_math(1000000000, 1000000000), 0)
        print("--- %s seconds ---" % (time.time() - start_time))
        start_time = time.time()
        self.assertEqual(solve_rev(1000, 1), 4164)
        self.assertEqual(solve_rev(1000, 2), 3795)
        self.assertEqual(solve_rev(10000000, 1444), 6079706)
        self.assertEqual(solve_rev(1, 1), 0)
        self.assertEqual(solve_rev(5, 1), 0)
        self.assertEqual(solve_rev(6, 1), 5)
        self.assertEqual(solve_rev(1000000000, 1000000000), 0)
        print("--- %s seconds ---" % (time.time() - start_time))

    def testCanBeDivided(self):
        from _125_Palindromic_sums import can_be_divided
        self.assertEqual(can_be_divided(5, 1), True)
        self.assertEqual(can_be_divided(101, 1), False)
        self.assertEqual(can_be_divided(626, 1), False)
        self.assertEqual(can_be_divided(595, 1), True)
        self.assertEqual(can_be_divided(696, 2), True)

    def testMathCanBeDivided(self):
        from _125_Palindromic_sums import math_can_be_divided
        self.assertEqual(math_can_be_divided(5, 1), True)
        self.assertEqual(math_can_be_divided(101, 1), False)
        self.assertEqual(math_can_be_divided(626, 1), False)
        self.assertEqual(math_can_be_divided(595, 1), True)
        self.assertEqual(math_can_be_divided(696, 2), True)

    def testFindAllPalindromes(self):
        start_time = time.time()
        from _125_Palindromic_sums import find_all_palindromes
        pals = find_all_palindromes(100, True)
        N = len(pals)
        self.assertEqual(N, 18)
        pals = find_all_palindromes(10 ** 6, True)
        N = len(pals)
        self.assertEqual(N, 1998)
        pals = find_all_palindromes(10 ** 9, True)
        N = len(pals)
        self.assertEqual(N, 109998)
        print("--- %s seconds ---" % (time.time() - start_time))


    def testNextPalindrome(self):
        from _125_Palindromic_sums import next_palindrome
        self.assertEqual(next_palindrome(5), 5)
        self.assertEqual(next_palindrome(10), 11)
        self.assertEqual(next_palindrome(80), 88)
        self.assertEqual(next_palindrome(192), 202)
        self.assertEqual(next_palindrome(9008), 9009)
        self.assertEqual(next_palindrome(9009), 9009)
        self.assertEqual(next_palindrome(9010), 9119)
        self.assertEqual(next_palindrome(90009), 90009)
        self.assertEqual(next_palindrome(90010), 90109)
        self.assertEqual(next_palindrome(12345678901), 12345754321)
        self.assertEqual(next_palindrome(12345678901), 12345754321)
        self.assertEqual(next_palindrome(12345678901), 12345754321)
        self.assertEqual(next_palindrome(12345678), 12355321)
        self.assertEqual(next_palindrome(1234567890), 1234664321)
        self.assertEqual(next_palindrome(12345678901), 12345754321)

