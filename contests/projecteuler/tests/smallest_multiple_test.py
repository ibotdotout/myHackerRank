# https://www.hackerrank.com/contests/projecteuler/challenges/euler005

import unittest
import smallest_multiple as euler


class SmallestMultipleTest(unittest.TestCase):
    def setUp(self):
        self.memo = euler.generate_memo()

    def test_given_3_should_be_6(self):
        given = 3
        expected = 6
        result = euler.solve(self.memo, given)
        self.assertEqual(expected, result)

    def test_given_10_should_be_2520(self):
        given = 10
        expected = 2520
        result = euler.solve(self.memo, given)
        self.assertEqual(expected, result)

    def test_given_14_should_be_360360(self):
        given = 14
        expected = 360360
        result = euler.solve(self.memo, given)
        self.assertEqual(expected, result)
