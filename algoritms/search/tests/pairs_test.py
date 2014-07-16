# https://www.hackerrank.com/challenges/pairs

import unittest
import pairs


class PairsTest(unittest.TestCase):
    def test_case1_should_be_3(self):
        k = 2
        l = [1, 5, 3, 4, 2]
        expected = 3
        result = pairs.solve(l, k)
        self.assertEqual(expected, result)

    def test_case2_should_be_0(self):
        k = 1
        l = [363374326, 364147530, 61825163, 1073065718, 1281246024,
             1399469912, 428047635, 491595254, 879792181, 1069262793]
        expected = 0
        result = pairs.solve(l, k)
        self.assertEqual(expected, result)

    def test_case3_should_be_7(self):
        k = 1
        l = [1, 2, 3, 5, 6, 7]
        expected = 4
        result = pairs.solve(l, k)
        self.assertEqual(expected, result)
