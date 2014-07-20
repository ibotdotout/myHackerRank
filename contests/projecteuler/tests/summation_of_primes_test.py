# https://www.hackerrank.com/contests/projecteuler/challenges/euler010

import unittest
import summation_of_primes as sop


class SummationOfPrimesTest(unittest.TestCase):
    def test_given_5_should_be_10(self):
        given = 5
        expected = 10
        result = sop.solve(given)
        self.assertEqual(expected, result)

    def test_given_10_should_be_17(self):
        given = 10
        expected = 17
        result = sop.solve(given)
        self.assertEqual(expected, result)

    def test_given_6_should_be_10(self):
        given = 6
        expected = 10
        result = sop.solve(given)
        self.assertEqual(expected, result)

    def test_given_20_should_be_41(self):
        given = 20
        expected = 41 + 17 + 19
        result = sop.solve(given)
        self.assertEqual(expected, result)

    def test_given_15_should_be_41(self):
        given = 15
        expected = 41
        result = sop.solve(given)
        self.assertEqual(expected, result)
