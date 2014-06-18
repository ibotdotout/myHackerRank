# https://www.hackerrank.com/challenges/insertionsort1

import unittest
import insertionsort1 as ins


class InsertionSortTest(unittest.TestCase):
    def setUp(self):
        self.l = [2, 4, 6, 8, 3]
        self.results = [l for l in ins.insert_sort(self.l)]

    def test_round1_get_24688(self):
        n = 0
        expected_result = [2, 4, 6, 8, 8]
        result = self.results[n]
        self.assertEqual(expected_result, result)

    def test_round2_get_24668(self):
        n = 1
        expected_result = [2, 4, 6, 6, 8]
        result = self.results[n]
        self.assertEqual(expected_result, result)

    def test_round3_get_24468(self):
        n = 2
        expected_result = [2, 4, 4, 6, 8]
        result = self.results[n]
        self.assertEqual(expected_result, result)

    def test_round4_get_23468(self):
        n = 3
        expected_result = [2, 3, 4, 6, 8]
        result = self.results[n]
        self.assertEqual(expected_result, result)
