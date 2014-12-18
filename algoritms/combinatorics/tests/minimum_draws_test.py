# https://www.hackerrank.com/challenges/minimum-draws

import minimum_draws as md
import unittest


class MinimumDrawsTest(unittest.TestCase):

    def test_give_1_should_be_2(self):
        give = 1
        res = md.solve(give)
        self.assertEqual(res, 2)

    def test_give_2_should_be_3(self):
        give = 2
        res = md.solve(give)
        self.assertEqual(res, 3)
