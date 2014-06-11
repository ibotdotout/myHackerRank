# https://www.hackerrank.com/challenges/maximizing-xor

import unittest
import maximizing_xor as mx


class MaximizingXorTest(unittest.TestCase):
    def test_input_1_10_get_15(self):
        l, r = 1, 10
        expected_result = 15
        result = mx.maximun_xor(l, r)
        self.assertEquals(expected_result, result)
