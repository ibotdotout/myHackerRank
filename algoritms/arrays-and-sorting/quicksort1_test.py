# https://www.hackerrank.com/challenges/quicksort1

import unittest
import quicksort1 as qs


class QuickSortTest(unittest.TestCase):
    def test_case1_get_32457(self):
        l = [4, 5, 3, 7, 2]
        expected_result = [3, 2, 4, 5, 7]
        result = qs.quick_sort1(l)
        self.assertEqual(expected_result, result)
