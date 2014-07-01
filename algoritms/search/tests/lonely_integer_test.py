# https://www.hackerrank.com/challenges/lonely-integer

import unittest
import lonely_integer as li


class LonelyIntegerTest(unittest.TestCase):
    def test_case1_should_get_1(self):
        l = [1]
        expected_result = [1]
        self.check_lonely_integer(l, expected_result)

    def test_case2_should_get_2(self):
        l = [1, 1, 2]
        expected_result = [2]
        self.check_lonely_integer(l, expected_result)

    def test_case3_should_get_2(self):
        l = [0, 0, 1, 2, 1]
        expected_result = [2]
        self.check_lonely_integer(l, expected_result)

    def check_lonely_integer(self, l, expected_result):
        result = li.get_lonely(l)
        self.assertEqual(expected_result, result)
