# https://www.hackerrank.com/challenges/count-luck

import count_luck as cl
import unittest


class CountLuckTest(unittest.TestCase):

    def test_sample_1_should_be_1(self):
        forest = ["*.M", ".X."]
        res = cl.solve(forest)
        self.assertEqual(res, 1)

    def test_sample_2_should_be_3(self):
        forest = [".X.X......X", ".X*.X.XXX.X", ".XX.X.XM...", "......XXXX."]
        res = cl.solve(forest)
        self.assertEqual(res, 3)

    def test_sample_3_should_be_9(self):
        forest = ["...XXXXXXXXXXXXXXXXXXX...................",
                  ".X..X.X.X.X.X.X.X..XXXX*X.X.X.X.X.X.X.XXM",
                  ".XXXX.X.X.X.X.X.X.XX.X.X.X.X.X.X.X.X.X.X.",
                  "........................................."]
        res = cl.solve(forest)
        self.assertEqual(res, 9)
