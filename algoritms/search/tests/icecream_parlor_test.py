# https://www.hackerrank.com/challenges/icecream-parlor

import unittest
import icecream_parlor as icp


class IcecreamParlorTest(unittest.TestCase):
    def test_case_sample1(self):
        m, n = 4, 5
        c = [1, 4, 5, 3, 2]
        exptected = [1, 4]
        result = icp.solve(m, n, c)
        self.assertEqual(exptected, result)

    def test_case_sample2(self):
        m, n = 4, 4
        c = [2, 2, 3, 3]
        exptected = [1, 2]
        result = icp.solve(m, n, c)
        self.assertEqual(exptected, result)
