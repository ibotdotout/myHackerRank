# https://www.hackerrank.com/challenges/insertion-sort

import unittest
import insertion_sort as ins


class InsertionSortTest(unittest.TestCase):
    def test_case1_get_0(self):
        l = [1, 1, 1, 2, 2]
        expected_result = 0
        result = ins.shifted_number(l)
        self.assertEqual(expected_result, result)

    def test_case2_get_4(self):
        l = [2, 1, 3, 1, 2]
        expected_result = 4
        result = ins.shifted_number(l)
        self.assertEqual(expected_result, result)
