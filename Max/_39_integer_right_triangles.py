#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


MIN = 12
MAX = 5 * 10 ** 6


def get_number_of_right_triangles(perim):
    number_of_right_triangles = 0
    for a in xrange(1, (perim - 1) / 2):
        numerator = perim ** 2 - 2 * perim * a
        denominator = 2 * perim - 2 * a
        if numerator <= 0 or denominator <= 0:
            continue
        if numerator % denominator == 0 and a >= numerator / denominator:
            number_of_right_triangles += 1
    return number_of_right_triangles


def generate_triangle_numbers(size):
    array = [0] * (size+1)
    for perimeter in xrange(MIN, size):
        array[perimeter] = get_number_of_right_triangles(perimeter)
    return array


def propagate_answer_to_table(array):
    current_index = 0
    current_max = 0
    for idx, val in enumerate(array):
        if val > current_max:
            current_index = idx
            current_max = val
        array[idx] = current_index


def generate_triangles(a, b, c):
    a1 = 1 * a + -2 * b + 2 * c
    b1 = 2 * a + -1 * b + 2 * c
    c1 = 2 * a + -2 * b + 3 * c
    a2 = 1 * a + 2 * b + 2 * c
    b2 = 2 * a + 1 * b + 2 * c
    c2 = 2 * a + 2 * b + 3 * c
    a3 = -1 * a + 2 * b + 2 * c
    b3 = -2 * a + 1 * b + 2 * c
    c3 = -2 * a + 2 * b + 3 * c
    return [a1, b1, c1], [a2, b2, c2], [a3, b3, c3]


def generate_primitive_pythagorean_triples(size):
    """ https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples """
    array = [0] * (size+1)
    lookup = [[3, 4, 5]]
    while len(lookup) != 0:
        a, b, c = lookup.pop()
        perimeter = a + b + c
        for x in xrange(perimeter, size, perimeter):
            array[x] += 1
        t1, t2, t3 = generate_triangles(a, b, c)
        for t in t1, t2, t3:
            if sum(t) <= size:
                lookup.append(t)
    return array


def main():
    T = int(raw_input())
    array = generate_primitive_pythagorean_triples(MAX)
    propagate_answer_to_table(array)
    for i in xrange(T):
        n = int(raw_input())
        print array[n]

if __name__ == '__main__':
    main()


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_solver(self):
        import sys
        import StringIO
        input = \
            """2
            12
            80
            """
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        main()
        pass