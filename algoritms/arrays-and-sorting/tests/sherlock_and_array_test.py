# https://www.hackerrank.com/challenges/sherlock-and-array

import unittest
import sherlock_and_array as saa


class SherlockAndArrayTest(unittest.TestCase):
    def test_case1_get_false(self):
        l = [1, 2, 3]
        expected_result = False
        result = saa.sherlock_array(l)
        self.assertEqual(expected_result, result)

    def test_case2_get_true(self):
        l = [1, 2, 3, 3]
        expected_result = True
        result = saa.sherlock_array(l)
        self.assertEqual(expected_result, result)

    def test_caes3_get_false(self):
        l = [5, -2, 2, -5, 5]
        expected_result = True
        result = saa.sherlock_array(l)
        self.assertEqual(expected_result, result)

    def test_caes4_get_false(self):
        l = [5, -2, 2, -5, 10]
        expected_result = True
        result = saa.sherlock_array(l)
        self.assertEqual(expected_result, result)
