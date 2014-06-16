# https://www.hackerrank.com/challenges/runningtime

import unittest
import runningtime as rt


class RunningTimeTest(unittest.TestCase):
    def test_input_21312_get_4(self):
        l = [2, 1, 3, 1, 2]
        expected_result = 4
        result = rt.get_shifted_number(l)
        self.assertEqual(expected_result, result)

    def test_input_112233557799_get_0(self):
        l = [1, 1, 2, 2, 3, 3, 5, 5, 7, 7, 9, 9]
        expected_result = 0
        result = rt.get_shifted_number(l)
        self.assertEqual(expected_result, result)

    def test_input_10_987654321_get_45(self):
        l = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected_result = 45
        result = rt.get_shifted_number(l)
        self.assertEqual(expected_result, result)
