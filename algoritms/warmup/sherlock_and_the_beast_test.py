# https://www.hackerrank.com/challenges/sherlock-and-the-beast

import unittest
import sherlock_and_the_beast as sb


class SherlockAndTheBeastTest(unittest.TestCase):
    def test_input_1_get_minus1(self):
        n = 1
        expected_result = "-1"
        result = sb.solve(n)
        self.assertEqual(expected_result, result)

    def test_input_3_get_555(self):
        n = 3
        expected_result = "555"
        result = sb.solve(n)
        self.assertEqual(expected_result, result)

    def test_input_5_get_33333(self):
        n = 5
        expected_result = "33333"
        result = sb.solve(n)
        self.assertEqual(expected_result, result)

    def test_input_11_get_55555533333(self):
        n = 11
        expected_result = "55555533333"
        result = sb.solve(n)
        self.assertEqual(expected_result, result)
