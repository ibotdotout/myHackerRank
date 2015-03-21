# https://www.hackerrank.com/challenges/picking-cards

import unittest
import picking_cards as pc


class PickingCardsTest(unittest.TestCase):

    def test_give_0_0_0_should_be_6(self):
        l = [0] * 3
        res = pc.solve(l)
        self.assertEqual(res, 6)

    def test_give_0_0_1_should_be_4(self):
        l = [0] * 2 + [1]
        res = pc.solve(l)
        self.assertEqual(res, 4)

    def test_give_0_3_3_should_be_0(self):
        l = [0] * 1 + [3]*2
        res = pc.solve(l)
        self.assertEqual(res, 0)

    def test_give_0_0_0_3_3_should_be_12(self):
        l = [0] * 3 + [3]*2
        res = pc.solve(l)
        self.assertEqual(res, 12)

    def test_adv_case(self):
        l = [3, 3, 6, 1, 3, 9, 4, 2, 13, 5, 5, 1, 3, 11, 2, 1, 0]
        res = pc.solve(l)
        self.assertEqual(res, 759833446)
