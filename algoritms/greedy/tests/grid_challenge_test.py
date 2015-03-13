# https://www.hackerrank.com/challenges/grid-challenge

import unittest
import grid_challenge as gc


class GridChallengeTest(unittest.TestCase):

    def test_sample_case(self):
        grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
        res = gc.solve(grid)
        self.assertEqual(res, True)

    def test_sample_case2(self):
        grid = ["ebacd", "fghij", "olmkn", "trpqs", "aywuv"]
        res = gc.solve(grid)
        self.assertEqual(res, False)

    def test_sample_case3(self):
        grid = ["uxf", "vof", "hmp"]
        res = gc.solve(grid)
        self.assertEqual(res, False)
