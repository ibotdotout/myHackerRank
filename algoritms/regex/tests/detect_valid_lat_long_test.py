# https://www.hackerrank.com/challenges/detecting-valid-latitude-and-longitude

import detect_valid_lat_long as dvll
import unittest


class DetectValidLatLongTest(unittest.TestCase):

    def test_75_180_should_be_true(self):
        text = "(75, 180)"
        res = dvll.solve(text)
        self.assertEqual(True, res)

    def test_p75_m180_should_be_true(self):
        text = "(+75, -180)"
        res = dvll.solve(text)
        self.assertEqual(True, res)

    def test_p190_m147d45_should_be_false(self):
        text = "(+190.0, -147.45)"
        res = dvll.solve(text)
        self.assertEqual(False, res)

    # @unittest.skip("")
    def test_90d_180d_should_be_false(self):
        text = "(90., 180.)"
        res = dvll.solve(text)
        self.assertEqual(False, res)

    def test_090_180_should_be_false(self):
        text = "(090, 180)"
        res = dvll.solve(text)
        self.assertEqual(False, res)
