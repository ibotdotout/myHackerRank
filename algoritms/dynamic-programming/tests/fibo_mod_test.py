# https://www.hackerrank.com/challenges/fibonacci-modified

import fibo_mod as fm
import unittest


class FiboModTest(unittest.TestCase):

    def test_give_0_1_5_should_be_5(self):
        a, b, n = 0, 1, 5
        res = fm.solve(a, b, n)
        self.assertEqual(res, 5)

    def test_give_1_3_4_should_be_103(self):
        a, b, n = 1, 3, 4
        res = fm.solve(a, b, n)
        self.assertEqual(res, 103)

    def test_give_1_3_2_should_be_3(self):
        a, b, n = 1, 3, 2
        res = fm.solve(a, b, n)
        self.assertEqual(res, 3)
