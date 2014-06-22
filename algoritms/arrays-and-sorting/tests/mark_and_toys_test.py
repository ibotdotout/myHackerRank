# https://www.hackerrank.com/challenges/mark-and-toys

import unittest
import mark_and_toys as mt


class MarkAndToysTest(unittest.TestCase):
    def test_case1_get_4(self):
        k = 50
        l = [1, 12, 5, 111, 200, 1000, 10]
        excepted_result = 4
        result = mt.max_toys(l, k)
        self.assertEqual(excepted_result, result)
