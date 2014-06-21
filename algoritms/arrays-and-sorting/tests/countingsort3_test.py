# https://www.hackerrank.com/challenges/countingsort3

import unittest
import countingsort3 as cs


class CountingSort3Test(unittest.TestCase):
    def test_case1(self):
        l = [4, 3, 0, 1, 5, 1, 2, 4, 2, 4]
        expected_result = [1, 3, 5, 6, 9, 10] + [10]*94
        result = cs.count(l)
        self.assertEqual(expected_result, result)
