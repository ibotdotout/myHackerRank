# https://www.hackerrank.com/contests/projecteuler/challenges/euler004

import unittest
import largest_palindrome_product as euler


class LargestPalindromeProductTest(unittest.TestCase):
    def test_given_101110_should_be_101101(self):
        given = 101110
        expected = 101101
        result = euler.solve(given)
        self.assertEqual(expected, result)

    def test_given_800000_should_be_793397(self):
        given = 800000
        expected = 793397
        result = euler.solve(given)
        self.assertEqual(expected, result)
