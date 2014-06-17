# https://www.hackerrank.com/challenges/quicksort2

import unittest
import quicksort2 as qs


class QuickSort2Test(unittest.TestCase):
    def setUp(self):
        self.l = [5, 8, 1, 3, 7, 9, 2]
        self.result = qs.quick_sort2(self.l)

    def test_case1_round1_get_23(self):
        n = 0
        expected_result = [2, 3]
        self.assertEqual(expected_result, self.result[n])

    def test_case1_round2_get_123(self):
        n = 1
        expected_result = [1, 2, 3]
        self.assertEqual(expected_result, self.result[n])

    def test_case1_round3_get_789(self):
        n = 2
        expected_result = [7, 8, 9]
        self.assertEqual(expected_result, self.result[n])

    def test_case1_round4_get_1235789(self):
        n = 3
        expected_result = [1, 2, 3, 5, 7, 8, 9]
        self.assertEqual(expected_result, self.result[n])
