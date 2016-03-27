# https://www.hackerrank.com/challenges/diagonal-difference

import diagonal_difference as dd
import unittest


class DiagonalDifferenceTest(unittest.TestCase):
    def test_sample_should_be_15(self):
        n = 3
        arr = [11, 2, 4, 4, 5, 6, 10, 8, -12]
        results = dd.solve(arr, n)
        self.assertEqual(15, results)
