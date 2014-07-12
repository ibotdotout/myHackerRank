# https://www.hackerrank.com/challenges/find-digits

import unittest
import find_digits


class FindDigitsTest(unittest.TestCase):
    def test_given_12_should_be_2(self):
        n = 12
        expected_result = 2
        result = find_digits.solve(n)
        self.assertEqual(expected_result, result)
