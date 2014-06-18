# https://www.hackerrank.com/challenges/correctness-invariant

import unittest
import correctness_invariant as ci


class CorrectnessInvarianTest(unittest.TestCase):
    def test_input_143562_get_123456(self):
        l = [1, 4, 3, 5, 6, 2]
        expected_result = [1, 2, 3, 4, 5, 6]
        result = ci.insertion_sort(l)
        self.assertEqual(expected_result, result)
