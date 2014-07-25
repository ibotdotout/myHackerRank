# https://www.hackerrank.com/contests/projecteuler/challenges/euler007

import unittest
import nth_prime as prime


class NthPrimeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        prime.generate()

    def test_given_3_should_be_5(self):
        given = 3
        expected = 5
        result = prime.solve(given)
        self.assertEqual(expected, result)

    def test_given_6_should_be_13(self):
        given = 6
        expected = 13
        result = prime.solve(given)
        self.assertEqual(expected, result)
