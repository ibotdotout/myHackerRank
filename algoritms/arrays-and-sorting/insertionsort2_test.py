# https://www.hackerrank.com/challenges/insertionsort2

import unittest
import insertionsort2 as ins


class InsertionSortTest(unittest.TestCase):
    def setUp(self):
        self.l = [1, 4, 3, 5, 6, 2]
        self.results = [l for l in ins.insert_sort(self.l)]

    def test_round1_get_143562(self):
        n = 0
        expected_result = [1, 4, 3, 5, 6, 2]
        result = self.results[n]
        self.assertEqual(expected_result, result)

    def test_round2_get_134562(self):
        n = 1
        expected_result = [1, 3, 4, 5, 6, 2]
        result = self.results[n]
        self.assertEqual(expected_result, result)

    def test_round3_get_134562(self):
        n = 2
        expected_result = [1, 3, 4, 5, 6, 2]
        result = self.results[n]
        self.assertEqual(expected_result, result)

    def test_round4_get_134562(self):
        n = 3
        expected_result = [1, 3, 4, 5, 6, 2]
        result = self.results[n]
        self.assertEqual(expected_result, result)

    def test_round5_get_123456(self):
        n = 4
        expected_result = [1, 2, 3, 4, 5, 6]
        result = self.results[n]
        self.assertEqual(expected_result, result)
