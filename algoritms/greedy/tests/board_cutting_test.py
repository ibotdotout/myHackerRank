# https://www.hackerrank.com/challenges/board-cutting

import unittest
import board_cutting as bc


class BoradCuttingTest(unittest.TestCase):

    def test_sample_case1(self):
        y = [2]
        x = [1]
        res = bc.solve(y, x)
        self.assertEqual(res, 4)

    def test_sample_case2(self):
        y = [2, 1, 3, 1, 4]
        x = [4, 1, 2]
        res = bc.solve(y, x)
        self.assertEqual(res, 42)

    def test_sample_case3(self):
        y = [2, 1, 3, 1, 4]
        x = [4, 1, 6+pow(10, 9)]
        res = bc.solve(y, x)
        self.assertEqual(res, 42)
