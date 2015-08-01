# https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes

import unittest
import big_int


class TestBigInt(unittest.TestCase):

    def test_sample(self):
        a, b, c, d = 9, 29, 7, 27
        ans = 4710194409608608369201743232
        res = big_int.solve(a, b, c, d)
        self.assertEqual(ans, res)
