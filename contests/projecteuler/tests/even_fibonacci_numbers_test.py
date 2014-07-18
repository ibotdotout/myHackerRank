# https://www.hackerrank.com/contests/projecteuler/challenges/euler002

import unittest
import even_fibonacci_numbers as euler


class EvenFibonacciNumbersTest(unittest.TestCase):
    def test_input_10_should_get_10(self):
        n = 10
        expected_result = 10
        result = euler.solve(n)
        self.assertEqual(expected_result, result)

    def test_input_100_should_get_44(self):
        n = 100
        expected_result = 44
        result = euler.solve(n)
        self.assertEqual(expected_result, result)
