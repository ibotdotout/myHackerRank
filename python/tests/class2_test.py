# https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle

import unittest
import class2


class Class2Test(unittest.TestCase):
    def test_sample_case(self):
        given = [[0, 4, 5], [1, 7, 6], [0, 5, 9], [1, 7, 2]]
        expected = 8.19
        result = class2.solve(*given)
        self.assertAlmostEqual(expected, result, 2)
