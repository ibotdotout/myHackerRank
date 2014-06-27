# https://www.hackerrank.com/challenges/sherlock-and-minimax

import unittest
import sherlock_and_minimax as shm


class SherlockAndMinimaxTest(unittest.TestCase):
    def test_case1_get_4(self):
        l = [5, 8, 14]
        pq = [4, 9]
        expected_result = 4
        result = shm.minimax(l, pq)
        self.assertEqual(expected_result, result)
