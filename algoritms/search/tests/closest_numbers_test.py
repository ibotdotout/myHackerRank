# https://www.hackerrank.com/challenges/closest-numbers

import unittest
import closest_numbers as cn


class ClosestNumbersTest(unittest.TestCase):
    def test_case1_should_get_minus20_30(self):
        l = [-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457,
             -6461594, 266854]
        expected_result = [-20, 30]
        result = cn.closest(l)
        self.assertEqual(expected_result, result)

    def test_case2_should_get_minus520_minus470_minus20_30(self):
        l = [-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457,
             -6461594, 266854, -520, -470]
        expected_result = [-520, -470, -20, 30]
        result = cn.closest(l)
        self.assertEqual(expected_result, result)

    def test_case3_should_get_2_3_3_4_4_5(self):
        l = [5, 4, 3, 2]
        expected_result = [2, 3, 3, 4, 4, 5]
        result = cn.closest(l)
        self.assertEqual(expected_result, result)
