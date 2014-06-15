# https://www.hackerrank.com/challenges/insertionsort1

import unittest
import insertionsort1 as ins


class InsertionSortTest(unittest.TestCase):
    def test_round1_get_24688(self):
        l = [2, 4, 6, 8, 3]
        n = 0
        expected_result = [2, 4, 6, 8, 8]
        result = ins.insert_sort(l)
        self.assertEqual(expected_result, result[n])

    def test_round2_get_24668(self):
        l = [2, 4, 6, 8, 3]
        n = 1
        expected_result = [2, 4, 6, 6, 8]
        result = ins.insert_sort(l)
        self.assertEqual(expected_result, result[n])

    def test_round3_get_24468(self):
        l = [2, 4, 6, 8, 3]
        n = 2
        expected_result = [2, 4, 4, 6, 8]
        result = ins.insert_sort(l)
        self.assertEqual(expected_result, result[n])

    def test_round4_get_23468(self):
        l = [2, 4, 6, 8, 3]
        n = 3
        expected_result = [2, 3, 4, 6, 8]
        result = ins.insert_sort(l)
        self.assertEqual(expected_result, result[n])
