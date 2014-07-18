# https://www.hackerrank.com/contests/projecteuler/challenges/euler001

import unittest
import multiples_of_3_and_5 as euler


class MultiplesOf3And5Test(unittest.TestCase):
    def test_case_10_should_get_23(self):
        n = 10
        expected_result = 23
        result = euler.solve(n)
        self.assertEqual(expected_result, result)

    def test_case_100_should_get_2318(self):
        n = 100
        expected_result = 2318
        result = euler.solve(n)
        self.assertEqual(expected_result, result)
