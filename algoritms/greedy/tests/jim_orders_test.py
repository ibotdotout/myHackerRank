# https://www.hackerrank.com/challenges/jim-and-the-orders

import unittest
import jim_orders as jo


class JimOrdersTest(unittest.TestCase):

    def test_give_1_3_2_3_3_3_should_be_1_2_3(self):
        l = [1, 3, 2, 3, 3, 3]
        res = jo.solve(l)
        self.assertEqual(res, [1, 2, 3])

    def test_give_8_1_4_2_3_1_should_be_3_2_1(self):
        l = [8, 1, 4, 2, 3, 1]
        res = jo.solve(l)
        self.assertEqual(res, [3, 2, 1])
