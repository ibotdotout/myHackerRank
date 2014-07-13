# https://www.hackerrank.com/challenges/find-point

import unittest
import find_point


class FindPointTest(unittest.TestCase):
    def test_case1_shoul_be_2_2(self):
        pq = [0, 0, 1, 1]
        expected_result = [2, 2]
        result = find_point.symmetric_point(pq)
        self.assertEqual(expected_result, result)
