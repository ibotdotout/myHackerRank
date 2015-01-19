# https://www.hackerrank.com/challenges/maxsubarray

import maxsubarray as msa
import unittest


class MaxSubArrayTest(unittest.TestCase):

    def test_give_1_2_3_4_should_be_10_10(self):
        l = [1, 2, 3, 4]
        res = msa.solve(l)
        self.assertEqual(res, (10, 10))

    def test_give_2_m1_2_3_4_m5_should_be_10_11(self):
        l = [2, -1, 2, 3, 4, -5]
        res = msa.solve(l)
        self.assertEqual(res, (10, 11))

    def test_give_m10_should_be_m10_m10(self):
        l = [-10]
        res = msa.solve(l)
        self.assertEqual(res, (-10, -10))

    def test_give_m1_m2_m3_m4_m4_m5_m6_should_be_m1_m1(self):
        l = [-1, -2, -3, -4, -5, -6]
        res = msa.solve(l)
        self.assertEqual(res, (-1, -1))
