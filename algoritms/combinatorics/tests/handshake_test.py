# https://www.hackerrank.com/challenges/handshake

import handshake as hs
import unittest


class HandShakeTest(unittest.TestCase):

    def test_give_1_should_be_0(self):
        give = 1
        res = hs.solve(give)
        self.assertEqual(res, 0)

    def test_give_2_should_be_1(self):
        give = 2
        res = hs.solve(give)
        self.assertEqual(res, 1)

    def test_give_3_should_be_3(self):
        give = 3
        res = hs.solve(give)
        self.assertEqual(res, 3)

    def test_give_4_should_be_6(self):
        give = 4
        res = hs.solve(give)
        self.assertEqual(res, 6)
