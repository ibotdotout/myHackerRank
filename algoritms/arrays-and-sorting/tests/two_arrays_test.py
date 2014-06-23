# https://www.hackerrank.com/challenges/two-arrays

import unittest
import two_arrays as ta


class TwoArraysTest(unittest.TestCase):
    def test_case1_get_true(self):
        k = 10
        a = [2, 1, 3]
        b = [7, 8, 9]
        expected_result = True
        result = ta.more_than_k(k, a, b)
        self.assertEqual(expected_result, result)

    def test_case2_get_false(self):
        k = 5
        a = [1, 2, 2, 1]
        b = [3, 3, 3, 4]
        expected_result = False
        result = ta.more_than_k(k, a, b)
        self.assertEqual(expected_result, result)
