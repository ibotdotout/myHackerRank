# https://www.hackerrank.com/challenges/solve-me-second

import solve_me_second as sms
import unittest


class SolveMeSecondTest(unittest.TestCase):

    def test_give_2_3_should_be_5(self):
        a, b = 2, 3
        res = sms.solve(a, b)
        self.assertEqual(res, 5)

    def test_give_3_7_should_be_10(self):
        a, b = 3, 7
        res = sms.solve(a, b)
        self.assertEqual(res, 10)
