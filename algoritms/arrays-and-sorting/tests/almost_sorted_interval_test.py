# https://www.hackerrank.com/challenges/almost-sorted-interval

import unittest
import almost_sorted_interval as asi


class AlmostSortedInterval(unittest.TestCase):
    def test_case1_get_8(self):
        l = [3, 1, 2, 5, 4]
        expected_result = 8
        result = asi.permute(l)
        self.assertEqual(expected_result, result)

    def test_case2_get_15(self):
        l = range(5)
        expected_result = 15
        result = asi.permute(l)
        self.assertEqual(expected_result, result)

    def test_case3_get_2202(self):
        l = [1, 4, 3, 5, 9, 7, 10, 6, 2, 11, 8, 12, 13, 17, 14, 15, 16, 18, 19,
             20, 21, 22, 24, 26, 27, 23, 25, 28, 29, 32, 31, 30, 33, 34, 37,
             36, 35, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 52,
             50, 49, 51, 53, 54, 55, 56, 57, 58, 59, 60, 62, 65, 63, 61, 68,
             69, 64, 66, 71, 72, 67, 73, 70, 74, 75, 76, 77, 82, 79, 80,
             81, 78, 83, 87, 84, 88, 85, 86, 89, 91, 90, 92, 93, 94, 95,
             96, 99, 98, 100, 97]
        expected_result = 2202
        result = asi.permute(l)
        self.assertEqual(expected_result, result)

    def test_case4_get_15(self):
        l = range(10**6)
        expected_result = 500000500000
        result = asi.permute(l)
        self.assertEqual(expected_result, result)
