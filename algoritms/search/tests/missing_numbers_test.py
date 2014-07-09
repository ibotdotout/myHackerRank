# https://www.hackerrank.com/challenges/missing-numbers

import unittest
import missing_numbers as msn


class MissingNumbersTest(unittest.TestCase):
    def test_case1_should_get_204_205_206(self):
        a = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
        b = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]
        expected_result = [204, 205, 206]
        result = msn.not_in_a(a, b)
        self.assertEqual(expected_result, result)
