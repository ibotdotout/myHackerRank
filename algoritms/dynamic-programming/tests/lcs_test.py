# https://www.hackerrank.com/challenges/dynamic-programming-classics-the-longest-common-subsequence

import lcs
import unittest


class LCSTest(unittest.TestCase):

    def test_12341_1231_should_be_1231(self):
        a = [1, 2, 3, 4, 1]
        b = [1, 2, 3, 1]
        res = lcs.solve(a, b)
        self.assertEqual(res, [1, 2, 3, 1])

    def test_12341_341213_should_be_123(self):
        a = [1, 2, 3, 4, 1]
        b = [3, 4, 1, 2, 1, 3]
        res = lcs.solve(a, b)
        self.assertEqual(res, [1, 2, 3])
