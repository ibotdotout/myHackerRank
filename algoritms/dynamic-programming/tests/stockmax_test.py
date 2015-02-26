# https://www.hackerrank.com/challenges/stockmax

import unittest
import stockmax as stm


class StockMaxTest(unittest.TestCase):

    def test_give_5_3_2_should_be_0(self):
        l = [5, 3, 2]
        res = stm.solve(l)
        self.assertEqual(res, 0)

    def test_give_1_2_100_should_be_197(self):
        l = [1, 2, 100]
        res = stm.solve(l)
        self.assertEqual(res, 197)

    def test_give_1_3_1_2_should_be_3(self):
        l = [1, 3, 1, 2]
        res = stm.solve(l)
        self.assertEqual(res, 3)

    def test_give_1_3_1_2_1000_should_be_3993(self):
        l = [1, 3, 1, 2, 1000]
        res = stm.solve(l)
        self.assertEqual(res, 3993)

    def test_give_1_3_1_2_1000_800_1_1_701_should_be_4693(self):
        l = [1, 3, 1, 2, 1000, 800, 1, 1, 701]
        res = stm.solve(l)
        self.assertEqual(res, 5393)
