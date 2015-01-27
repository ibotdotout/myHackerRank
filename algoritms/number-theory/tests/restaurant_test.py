# https://www.hackerrank.com/challenges/restaurant

import restaurant as rt
import unittest


class RestaurantTest(unittest.TestCase):

    def test_give_2_2_should_be_1(self):
        l, b = 2, 2
        res = rt.solve(l, b)
        self.assertEqual(res, 1)

    def test_give_6_9_should_be_6(self):
        l, b = 6, 9
        res = rt.solve(l, b)
        self.assertEqual(res, 6)

    def test_give_309_528_should_be_18128(self):
        l, b = 309, 528
        res = rt.solve(l, b)
        self.assertEqual(res, 18128)
