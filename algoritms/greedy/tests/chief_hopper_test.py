# https://www.hackerrank.com/challenges/chief-hopper


import unittest
import chief_hopper as ch


class ChiefHopperTest(unittest.TestCase):

    def test_give_3_4_3_2_4_should_be_4(self):
        l = [3, 4, 3, 2, 4]
        res = ch.solve(l)
        self.assertEqual(res, 4)

    def test_give_2_2_2_should_be_2(self):
        l = [2] * 3
        res = ch.solve(l)
        self.assertEqual(res, 2)

    def test_give_4_should_be_2(self):
        l = [4]
        res = ch.solve(l)
        self.assertEqual(res, 2)
