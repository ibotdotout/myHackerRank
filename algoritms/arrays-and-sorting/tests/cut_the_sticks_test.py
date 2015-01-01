# https://www.hackerrank.com/challenges/cut-the-sticks

import cut_the_sticks as cts
import unittest


class CutTheSticksTest(unittest.TestCase):

    def test_sample_case_1(self):
        l = [5, 4, 4, 2, 2, 8]
        res = cts.solve(l)
        ans = [6, 4, 2, 1]
        self.assertEqual(res, ans)

    def test_sample_case_2(self):
        l = [1, 2, 3, 4, 3, 3, 2, 1]
        res = cts.solve(l)
        ans = [8, 6, 4, 1]
        self.assertEqual(res, ans)
