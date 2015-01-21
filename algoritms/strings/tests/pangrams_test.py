# https://www.hackerrank.com/challenges/pangrams

import unittest
import pangrams as pg


class PangramsTest(unittest.TestCase):

    def test_sample_1_should_be_true(self):
        w = "We promptly judged antique ivory buckles for the next prize"
        res = pg.solve(w)
        self.assertEqual(res, True)

    def test_sample_2_should_be_false(self):
        w = "We promptly judged antique ivory buckles for the prize"
        res = pg.solve(w)
        self.assertEqual(res, False)
