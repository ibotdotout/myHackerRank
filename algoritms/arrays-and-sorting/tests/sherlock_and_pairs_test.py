# https://www.hackerrank.com/challenges/sherlock-and-pairs

import sherlock_and_pairs as sap
import unittest


class SherlockAndPairsTest(unittest.TestCase):

    def test_give_1_2_3_should_be_0(self):
        l = [1, 2, 3]
        res = sap.solve(l)
        self.assertEqual(res, 0)

    def test_give_1_1_3_should_be_2(self):
        l = [1, 1, 3]
        res = sap.solve(l)
        self.assertEqual(res, 2)

    def test_give_1_1_3_1_should_be_6(self):
        l = [1, 1, 3, 1]
        res = sap.solve(l)
        self.assertEqual(res, 6)

    def test_give_1_1_3_1_1_3_should_be_11(self):
        l = [1, 1, 3, 1, 1, 3]
        res = sap.solve(l)
        self.assertEqual(res, 14)
