# https://www.hackerrank.com/challenges/quicksort3

import unittest
import quicksort3 as qs


class QuickSort3Test(unittest.TestCase):
    def setUp(self):
        self.l = [1, 3, 9, 8, 2, 7, 5]
        self.result = qs.quick_sort3(self.l)

    def test_case1_round1(self):
        n = 0
        expected_result = [1, 3, 2, 5, 9, 7, 8]
        self.assertEqual(expected_result, self.result[n])

    def test_case1_round2(self):
        n = 1
        expected_result = [1, 2, 3, 5, 9, 7, 8]
        self.assertEqual(expected_result, self.result[n])

    def test_case1_round3(self):
        n = 2
        expected_result = [1, 2, 3, 5, 7, 8, 9]
        self.assertEqual(expected_result, self.result[n])
