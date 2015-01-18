# https://www.hackerrank.com/challenges/circle-city


import circle_city as cc
import unittest


class CircleCityTest(unittest.TestCase):

    def test_give_1_3_should_be_false(self):
        r, k = 1, 3
        res = cc.solve(r, k)
        self.assertEqual(res, False)

    def test_give_1_4_should_be_true(self):
        r, k = 1, 4
        res = cc.solve(r, k)
        self.assertEqual(res, True)

    def test_give_4_4_should_be_true(self):
        r, k = 4, 4
        res = cc.solve(r, k)
        self.assertEqual(res, True)

    def test_give_25_11_should_be_false(self):
        r, k = 25, 11
        res = cc.solve(r, k)
        self.assertEqual(res, False)

    def test_give_25_12_should_be_true(self):
        r, k = 25, 12
        res = cc.solve(r, k)
        self.assertEqual(res, True)

    def test_give_432892665_10_should_be_false(self):
        r, k = 432892665, 10
        res = cc.solve(r, k)
        self.assertEqual(res, False)
