# https://www.hackerrank.com/challenges/jim-and-the-jokes

import unittest
import jim_and_jokes as jj


class JimAndJokesTest(unittest.TestCase):

    def test_give_10_25_8_31_should_be_1(self):
        l = [10, 25, 8, 31]
        res = jj.solve(l)
        self.assertEqual(res, 1)

    def test_give_2_25_2_25_should_be_0(self):
        l = [2, 25, 2, 25]
        res = jj.solve(l)
        self.assertEqual(res, 0)

    def test_give_3_33_3_33_should_be_0(self):
        l = [3, 33, 3, 33]
        res = jj.solve(l)
        self.assertEqual(res, 0)

    def test_give_12_31_12_31_12_31should_be_3(self):
        l = [12, 31, 12, 31, 12, 31]
        res = jj.solve(l)
        self.assertEqual(res, 3)

    def test_give_12_31_12_31_12_31_10_25_8_31should_be_4(self):
        l = [12, 31, 12, 31, 12, 31, 10, 25, 8, 31]
        res = jj.solve(l)
        self.assertEqual(res, 4)
