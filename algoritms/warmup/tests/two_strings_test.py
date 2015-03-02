# https://www.hackerrank.com/challenges/two-strings

import unittest
import two_strings as ts


class TwoStringsTest(unittest.TestCase):

    def test_hello_world_should_be_true(self):
        a, b = "hello", "world"
        res = ts.solve(a, b)
        self.assertEqual(res, True)

    def test_hi_world_should_be_false(self):
        a, b = "hi", "world"
        res = ts.solve(a, b)
        self.assertEqual(res, False)
