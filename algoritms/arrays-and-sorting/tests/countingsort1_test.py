# https://www.hackerrank.com/challenges/countingsort1

import unittest
import countingsort1 as cs


class CountingSort1Test(unittest.TestCase):
    def test_case1(self):
        l = list(range(0, 100))
        expected_result = [1 for i in range(0, 100)]
        result = cs.count(l)
        self.assertEqual(expected_result, result)
