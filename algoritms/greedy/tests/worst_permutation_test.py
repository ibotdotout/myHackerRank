# https://www.hackerrank.com/challenges/worst-permutation

import unittest
import worst_permutation as wp


class WorstPermutationTest(unittest.TestCase):

    def test_give_4_2_3_5_1_k_1_should_be_52341(self):
        l = [4, 2, 3, 5, 1]
        k = 1
        res = wp.solve(l, k)
        self.assertEqual(res, [5, 2, 3, 4, 1])

    def test_give_6_4_2_3_5_1_k_1_should_be_654321(self):
        l = [6, 4, 2, 3, 5, 1]
        k = 2
        res = wp.solve(l, k)
        self.assertEqual(res, [6, 5, 4, 3, 2, 1])

    def test_give_2_1_3_k_1_should_be_312(self):
        l = [2, 1, 3]
        k = 1
        res = wp.solve(l, k)
        self.assertEqual(res, [3, 1, 2])

    def test_give_2_1_3_k_2_should_be_321(self):
        l = [2, 1, 3]
        k = 2
        res = wp.solve(l, k)
        self.assertEqual(res, [3, 2, 1])
