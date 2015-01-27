# https://www.hackerrank.com/challenges/reverse-game

import reverse_game as rg
import unittest


class ReverseGameTest(unittest.TestCase):

    def test_give_3_1_should_be_2(self):
        a, b = 3, 1
        res = rg.solve(a, b)
        self.assertEqual(res, 2)

    def test_give_5_2_should_be_4(self):
        a, b = 5, 2
        res = rg.solve(a, b)
        self.assertEqual(res, 4)

    def test_give_5_0_should_be_1(self):
        a, b = 5, 0
        res = rg.solve(a, b)
        self.assertEqual(res, 1)

    def test_give_6_3_should_be_4(self):
        a, b = 6, 3
        res = rg.solve(a, b)
        self.assertEqual(res, 4)
