# https://www.hackerrank.com/challenges/simple-array-sum

import simple_array_sum as sas
import unittest


class SimpleArraySumTest(unittest.TestCase):

    def test_sample_should_be_31(self):
        l = [1, 2, 3, 4, 10, 11]
        res = sas.solve(l)
        self.assertEqual(31, res)
