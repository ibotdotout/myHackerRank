# https://www.hackerrank.com/challenges/quicksort4

import unittest
import quicksort4 as qs


class QuickSort4Test(unittest.TestCase):
    def test_quick_sort_corrected(self):
        l = [1, 3, 9, 8, 2, 7, 5]
        expected_result = sorted(l)
        qs.quick_sort(l)
        result = l
        self.assertEqual(expected_result, result)

    def test_quick_sort_swap_count_equal_8(self):
        l = [1, 3, 9, 8, 2, 7, 5]
        expected_result = 8
        result = qs.quick_sort(l)
        self.assertEqual(expected_result, result)

    def test_insert_sort_corrted(self):
        l = [1, 3, 9, 8, 2, 7, 5]
        expected_result = sorted(l)
        qs.insert_sort(l)
        result = l
        self.assertEqual(expected_result, result)

    def test_insert_sort_shift_count_equal_9(self):
        l = [1, 3, 9, 8, 2, 7, 5]
        expected_result = 9
        result = qs.insert_sort(l)
        self.assertEqual(expected_result, result)

    def test_insert_sort_shift_count_equal_55(self):
        l = range(10, 0, -1)
        expected_result = 45
        result = qs.insert_sort(l)
        self.assertEqual(expected_result, result)

    def test_quick_sort_swap_count_equal_9(self):
        l = range(10, 0, -1)
        expected_result = 29
        result = qs.quick_sort(l)
        self.assertEqual(expected_result, result)
