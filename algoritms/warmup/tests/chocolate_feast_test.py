# https://www.hackerrank.com/challenges/chocolate-feast

import unittest
import chocolate_feast as cf


class ChocolateFeastTest(unittest.TestCase):
    def test_input_10_2_5_get_6(self):
        n, c, m = 10, 2, 5
        expected_result = 6
        result = cf.get_chocolates(n, c, m)
        self.assertEqual(expected_result, result)

    def test_input_12_4_4_get_3(self):
        n, c, m = 12, 4, 4
        expected_result = 3
        result = cf.get_chocolates(n, c, m)
        self.assertEqual(expected_result, result)

    def test_input_6_2_2_get_5(self):
        n, c, m = 6, 2, 2
        expected_result = 5
        result = cf.get_chocolates(n, c, m)
        self.assertEqual(expected_result, result)
