# https://www.hackerrank.com/challenges/equations

import equations as eq
import unittest


class EquationsTest(unittest.TestCase):

    def test_give_1_should_be_1(self):
        n = 1
        res = eq.solve(n)
        self.assertEqual(res, 1)

    def test_give_2_should_be_3(self):
        n = 2
        res = eq.solve(n)
        self.assertEqual(res, 3)

    def test_give_3_should_be_9(self):
        n = 3
        res = eq.solve(n)
        self.assertEqual(res, 9)

    def test_give_4_should_be_21(self):
        n = 4
        res = eq.solve(n)
        self.assertEqual(res, 21)

    def test_give_2415_should_be_922287(self):
        n = 2415
        res = eq.solve(n)
        self.assertEqual(res, 922287)

    def test_give_32327_should_be_656502(self):
        n = 32327
        res = eq.solve(n)
        self.assertEqual(res, 656502)
