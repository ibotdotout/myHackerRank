# https://www.hackerrank.com/challenges/cyclicquadruples


import unittest
import cyclicquadruples as cq


class CyclicQuadruplesTest(unittest.TestCase):

    def test_give_1_4_1_3_1_2_4_4_should_be_8(self):
        seq = [1, 4, 1, 3, 1, 2, 4, 4]
        res = cq.solve(seq)
        self.assertEqual(res, 8)

    def test_give_1_3_1_2_1_3_3_4should_be_10(self):
        seq = [1, 3, 1, 2, 1, 3, 3, 4]
        res = cq.solve(seq)
        self.assertEqual(res, 10)
