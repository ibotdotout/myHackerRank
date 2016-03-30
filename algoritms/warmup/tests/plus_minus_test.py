# https://www.hackerrank.com/challenges/plus-minus

import plus_minus as pm
import unittest


class PlusMinusTest(unittest.TestCase):

    def test_sample(self):
        l = [-4, 3, -9, 0, 4, 1]
        result = pm.solve(l)
        expected = (0.500000, 0.333333, 0.166667)
        for e, r in zip(expected, result):
            self.assertTrue(abs(e-r) < 10e4)
