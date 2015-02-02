# https://www.hackerrank.com/challenges/power-of-large-numbers

import unittest
import power_large_number as pln


class PowerOfLargeNumberTest(unittest.TestCase):

    def test_give_4_5_should_be_1024(self):
        x, y = 4, 5
        res = pln.solve(x, y)
        self.assertEqual(res, 1024)

    def test_sample_large1(self):
        x = 34534985349875439875439875349875
        y = 93475349759384754395743975349573495
        res = pln.solve(x, y)
        self.assertEqual(res, 735851262)
