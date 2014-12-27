# https://www.hackerrank.com/challenges/sherlock-and-squares

import sherlock_and_squares as sas
import unittest


class SherlockAndSquaresTest(unittest.TestCase):

    def test_give_3_9_should_be_2(self):
        a, b = 3, 9
        res = sas.solve(a, b)
        self.assertEqual(res, 2)

    def test_give_17_24_should_be_0(self):
        a, b = 17, 24
        res = sas.solve(a, b)
        self.assertEqual(res, 0)

    def test_give_1_100_should_be_11(self):
        a, b = 1, 100
        res = sas.solve(a, b)
        self.assertEqual(res, 10)
