# https://www.hackerrank.com/challenges/sets

import unittest
import sets


class Setstest(unittest.TestCase):
    def test_case1_should_get_5_9_11_12(self):
        l = [2, 4, 5, 9]
        l2 = [2, 4, 11, 12]
        expeted_result = [5, 9, 11, 12]
        result = sets.not_in_both(l, l2)
        self.assertEqual(expeted_result, result)

    def test_case2_should_get_5_9_11_12_17(self):
        l = [2, 4, 5, 9, 17]
        l2 = [2, 4, 11, 12]
        expeted_result = [5, 9, 11, 12, 17]
        result = sets.not_in_both(l, l2)
        self.assertEqual(expeted_result, result)
