# https://www.hackerrank.com/challenges/basic-calculator

import unittest
import basic_calculator


class BasicCalculatorTest(unittest.TestCase):
    def test_case_sample(self):
        a = 2.3
        b = 4
        expected = ['6.30', '-1.70', '9.20', '0.57', '0.00']
        result = basic_calculator.cal(a, b)
        self.assertEqual(expected, result)
