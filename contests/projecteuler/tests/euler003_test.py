# https://www.hackerrank.com/contests/projecteuler/challenges/euler003

import unittest
import euler003 as euler


class Euler003Test(unittest.TestCase):
    def test_give_8_should_be_2(self):
        n = 8
        expected_result = 2
        result = euler.solve(n)
        self.assertEqual(expected_result, result)

    def test_give_10_should_be_5(self):
        n = 10
        expected_result = 5
        result = euler.solve(n)
        self.assertEqual(expected_result, result)

    def test_give_17_should_be_17(self):
        n = 17
        expected_result = 17
        result = euler.solve(n)
        self.assertEqual(expected_result, result)

    def test_give_13195_should_be_29(self):
        n = 13195
        expected_result = 29
        result = euler.solve(n)
        self.assertEqual(expected_result, result)

    def test_give_600851475143_should_be_6857(self):
        n = 600851475143
        expected_result = 6857
        result = euler.solve(n)
        self.assertEqual(expected_result, result)

    def test_give_6857_should_be_6857(self):
        n = 6857
        expected_result = 6857
        result = euler.solve(n)
        self.assertEqual(expected_result, result)
