# https://www.hackerrank.com/challenges/number-list

import unittest
import number_list as nl


class NumberListTest(unittest.TestCase):

    def test_give_1_2_3_k_2_should_be_3(self):
        k = 2
        l = [1, 2, 3]
        res = nl.solve(l, k)
        self.assertEqual(res, 3)

    def test_give_1_2_3_k_1_should_be_5(self):
        k = 1
        l = [1, 2, 3]
        res = nl.solve(l, k)
        self.assertEqual(res, 5)

    def test_give_1_4_2_3_k_2_should_be_8(self):
        k = 2
        l = [1, 4, 2, 3]
        res = nl.solve(l, k)
        self.assertEqual(res, 8)
