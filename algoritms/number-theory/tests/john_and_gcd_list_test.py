# https://www.hackerrank.com/challenges/john-and-gcd-list

import john_and_gcd_list as jgl
import unittest


class JohnAndGCDListTest(unittest.TestCase):

    def test_give_1_2_3_should_be_1_2_6_3(self):
        l = [1, 2, 3]
        res = jgl.solve(l)
        self.assertEqual(res, [1, 2, 6, 3])

    def test_give_5_10_5_should_be_5_10_10_5(self):
        l = [5, 10, 5]
        res = jgl.solve(l)
        self.assertEqual(res, [5, 10, 10, 5])
