# https://www.hackerrank.com/challenges/flipping-bits

import flipping_bits as fb
import unittest


class FlippingBitsTest(unittest.TestCase):

    def test_give_0_should_be_4294967295(self):
        a = 0
        res = fb.solve(a)
        self.assertEqual(res, 4294967295)

    def test_give_2147483647_should_be_2147483648(self):
        a = 2147483647
        res = fb.solve(a)
        self.assertEqual(res, 2147483648)
