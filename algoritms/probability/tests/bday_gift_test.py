# https://www.hackerrank.com/challenges/bday-gift

import bday_gift as bg
import unittest


class BDayGiftTest(unittest.TestCase):

    def test_give_1_1_2_should_be_2(self):
        l = [1, 1, 2]
        res = bg.solve(l)
        self.assertEqual(res, 2)

    def test_give_1_2_2_2_should_be_3p5(self):
        l = [1, 2, 2, 2]
        res = bg.solve(l)
        self.assertEqual(res, 3.5)
