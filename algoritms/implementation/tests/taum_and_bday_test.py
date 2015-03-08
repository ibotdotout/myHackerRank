# https://www.hackerrank.com/challenges/taum-and-bday

import unittest
import taum_and_bday as tab


class TaumAndBdayTest(unittest.TestCase):

    def test_sample_case(self):
        a = [10, 10]
        b = [1, 1, 1]
        res = tab.solve(a, b)
        self.assertEqual(res, 20)

    def test_sample_case2(self):
        a = [10, 3]
        b = [5, 2, 1]
        res = tab.solve(a, b)
        self.assertEqual(res, 36)

    def test_sample_case3(self):
        a = [3, 10]
        b = [5, 1, 2]
        res = tab.solve(a, b)
        self.assertEqual(res, 19)
