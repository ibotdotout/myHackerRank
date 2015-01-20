# https://www.hackerrank.com/challenges/unbounded-knapsack

import unbounded_knapsack as uk
import unittest


class UnBoundedKnapsackTest(unittest.TestCase):

    def test_give_k_12_p_1_6_9_should_be_12(self):
        k = 12
        l = [1, 6, 9]
        res = uk.solve(l, k)
        self.assertEqual(res, 12)

    def test_give_k_9_p_3_4_4_4_8_should_be_9(self):
        k = 9
        l = [3, 4, 4, 4, 8]
        res = uk.solve(l, k)
        self.assertEqual(res, 9)

    def test_give_k_4_p_3_5_should_be_3(self):
        k = 4
        l = [3, 5]
        res = uk.solve(l, k)
        self.assertEqual(res, 3)
