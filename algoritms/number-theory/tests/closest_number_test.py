# https://www.hackerrank.com/challenges/closest-number

import closest_number as cn
import unittest


class ClosestNumberTest(unittest.TestCase):

    def test_give_349_1_4_should_be_348(self):
        l = [349, 1, 4]
        res = cn.solve(l)
        self.assertEqual(res, 348)

    def test_give_395_1_7_should_be_392(self):
        l = [395, 1, 7]
        res = cn.solve(l)
        self.assertEqual(res, 392)

    def test_give_4_m2_2_should_be_0(self):
        l = [4, -2, 2]
        res = cn.solve(l)
        self.assertEqual(res, 0)

    def test_long_case(self):
        l = [184804527, 1, 38664371]
        res = cn.solve(l)
        self.assertEqual(res, 193321855)
