# https://www.hackerrank.com/challenges/list-comprehensions

import unittest
import list_comprehensions as lc


class ListComprehensionsTest(unittest.TestCase):
    def test_case_1112(self):
        x, y, z, n = [1, 1, 1, 2]
        expected_result = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0],
                           [1, 1, 1]]
        result = lc.get_lists(x, y, z, n)
        self.assertEqual(expected_result, result)

    def test_case_2222(self):
        x, y, z, n = [2, 2, 2, 2]
        expected_result = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2],
                           [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2],
                           [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1],
                           [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0],
                           [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1],
                           [2, 2, 2]]
        result = lc.get_lists(x, y, z, n)
        self.assertEqual(expected_result, result)
