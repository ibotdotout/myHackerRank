# https://www.hackerrank.com/challenges/find-median

import unittest
import find_median as fm


class FindMedianTest(unittest.TestCase):
    def test_case1_should_get_3(self):
        l = [0, 1, 2, 4, 6, 5, 3]
        expected_result = 3
        result = fm.median(l)
        self.assertEqual(expected_result, result)

    def test_case2_should_get_4(self):
        l = [0, 1, 2, 4, 6, 5, 3, 4, 7]
        expected_result = 4
        result = fm.median(l)
        self.assertEqual(expected_result, result)
