# https://www.hackerrank.com/challenges/bear-and-workbook

import bear_and_workbook as bw
import unittest


class BearAndWorkBookTest(unittest.TestCase):
    def test_sample_should_be_4(self):
        n, k = 5, 3
        t = [4, 2, 6, 1, 10]
        expected = 4
        result = bw.solve(n, k, t)
        self.assertEqual(expected, result)

    def test_large_samplf(self):
        n, k = 40, 7
        t = [1, 10, 12, 4, 11, 6, 8, 15, 23, 24, 23, 24, 39, 34, 50, 3, 58, 62,
             71, 79, 95, 100, 2, 2,
             100, 100, 100, 100, 100, 100, 1, 100, 100, 100, 100, 100, 3,
             100, 100, 100]
        expected = 12
        result = bw.solve(n, k, t)
        self.assertEqual(expected, result)
