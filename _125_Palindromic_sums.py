#!/usr/bin/python
# -*- coding: utf-8 -*-


global palindromes
global squares
palindromes = None
squares = None

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


def find_all_palindromes(max_number, reinitialize=False):
    global palindromes
    if palindromes is not None and not reinitialize:
        return palindromes
    palindromes = {}
    next_pal = 0

    while True:
        next_pal = next_palindrome(next_pal + 1)
        if next_pal > max_number:
            break
        palindromes[next_pal] = {}

    return palindromes


def check_can_be_divided(arr, number):
    first = last = 0

    if len(arr) < 2:
        return False

    sum = arr[first]

    while True:
        if sum < number:
            if last < len(arr) - 1:
                last += 1
            else:
                return False
            sum += arr[last]
        elif sum == number:
            if last == first:
                return False
            return True
        else:
            sum -= arr[first]
            first += 1

        if arr[last] > number:
            break
    return False


def can_be_divided(number, d):
    for i in xrange(d):
        squares_from_i = squares[i::d]
        if check_can_be_divided(squares_from_i, number):
            return True
    return False


def math_can_be_divided(number, d):

    import math
    # for a in xrange(1, math.floor(math.sqrt(number))):
    #     sum = n * a**2 + (n**2 - n) * a * d + (n-1)*n*(2*n-1) / 6 * d**2

    for n in xrange(2, 30):
        A = n
        B = (n**2 - n) * d
        C = (n-1)*n*(2*n-1) / 6. * d**2 - number
        if not C.is_integer():
            continue
        DELTA = B ** 2 - 4 * A * C
        if DELTA >= 0:
            sqrt_DELTA = math.sqrt(DELTA)
            if not sqrt_DELTA.is_integer():
                continue
            x1 = (-B - sqrt_DELTA) / (2 * A)
            x2 = (-B + sqrt_DELTA) / (2 * A)
            if x1 > 0 and x1.is_integer():
                return True
            if x2 > 0 and x2.is_integer():
                return True
    return False
    #
    #
    # a = 1
    # n = 2
    # sum = n * a**2 + (n**2 - n) * a * d + (n-1)*n*(2*n-1) / 6 * d**2
    # while True:
    #     if sum < number:
    #         n += 1
    #         sum = n * a**2 + (n**2 - n) * a * d + (n-1)*n*(2*n-1) / 6 * d**2
    #     elif sum == number:
    #         return True
    #     else:
    #         a += 1
    #         n = 2
    #         sum = n * a**2 + (n**2 - n) * a * d + (n-1)*n*(2*n-1) / 6 * d**2
    #
    #     if a*a > number:
    #         return False
    # pass


def init_squares(max_number, reinitialize=False):
    global squares
    if squares is not None and not reinitialize:
        return
    import math
    squares = [x * x for x in xrange(1, int(math.ceil(math.sqrt(max_number))))]
    return squares


def solve_math(N, d, max_n=None):
    if max_n is None:
        max_n = N
    find_all_palindromes(max_n)
    sum = 0
    global palindromes
    for key in palindromes.keys():
        if key > N:
            continue
        flag = False
        if d in palindromes[key]:
            flag = palindromes[key][d]
        if flag or math_can_be_divided(key, d):
            palindromes[key][d] = True
            sum += key
        else:
            palindromes[key][d] = False
    return sum


def is_palindrome(n):
    if n % 10 == 0:
        return False
    if n / 10 == 0:
        return True
    # s = str(n)
    # for i in xrange(len(s)/2):
    #     if s[i] != s[len(s)-i-1]:
    #         return False
    # return True
    return str(n) == str(n)[::-1]


def solve_rev(N, d, max_n=None):
    if max_n is None:
        max_n = N
    init_squares(max_n)

    list = set()

    # print "Len squares: ", len(squares)
    #
    # print "N, d: ",N, d

    for startIndex in range(0, len(squares)-1):
        temp_total = squares[startIndex]
        end_index = startIndex + d

        if end_index >= len(squares):
            break
        temp_total += squares[end_index]

        while temp_total < N:
            if is_palindrome(temp_total):
                list.add(temp_total)
            end_index += d
            if end_index >= len(squares):
                break
            temp_total += squares[end_index]

    # print list
    return sum(list)


def main():

    T = int(input())
    test_cases = []
    max_n = 0
    for i in xrange(T):
        n, d = map(int, raw_input().split())
        max_n = max(max_n, n)
        test_cases.append([n, d])
    for i in xrange(T):
        print solve_rev(test_cases[i][0], test_cases[i][1], max_n)
"""
4
10000 10
1000000000 4
6443625136 11
3258325512 5
"""
"""
4
1 1
5 1
6 1
1000000000 1000000000
"""
if __name__ == '__main__':
    main()
