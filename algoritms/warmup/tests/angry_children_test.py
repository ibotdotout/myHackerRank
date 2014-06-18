# https://www.hackerrank.com/challenges/angry-children

import unittest
import angry_children as ac


class AngryChilderTest(unittest.TestCase):
    def test_input_case_0_get_20(self):
        _list = [10, 100, 300, 200, 1000, 20, 30]
        k = 3
        expected_result = 20
        result = ac.range_diff(_list, k)
        self.assertEqual(expected_result, result)

    def test_input_case_1_get_20(self):
        _list = [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]
        k = 4
        expected_result = 3
        result = ac.range_diff(_list, k)
        self.assertEqual(expected_result, result)
