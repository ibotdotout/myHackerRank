# https://www.hackerrank.com/challenges/valid-pan-format

import valid_pan_format as vpf
import unittest


class ValidPanFormatTest(unittest.TestCase):

    def test_valid_should_be_ture(self):
        text = "ABCDS1234Y"
        res = vpf.solve(text)
        self.assertEqual(res, True)

    def test_invalid_should_be_false(self):
        text = "ABAB12345Y"
        res = vpf.solve(text)
        self.assertEqual(res, False)

    def test_invalid2_should_be_false(self):
        text = "abAB12345Y"
        res = vpf.solve(text)
        self.assertEqual(res, False)
