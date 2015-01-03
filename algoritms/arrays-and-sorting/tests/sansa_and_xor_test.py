# https://www.hackerrank.com/challenges/sansa-and-xor

import sansa_and_xor as sax
import unittest


class SansaAndXorTest(unittest.TestCase):

    def test_give_123_should_be_2(self):
        l = [1, 2, 3]
        res = sax.solve(l)
        self.assertEqual(res, 2)

    def test_give_157_should_be_6(self):
        l = [1, 5, 7]
        res = sax.solve(l)
        self.assertEqual(res, 6)
