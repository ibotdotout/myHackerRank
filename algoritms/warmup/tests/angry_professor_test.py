# https://www.hackerrank.com/challenges/angry-professor

import unittest
import angry_professor as ap


class AngryProfessorTest(unittest.TestCase):

    def test_sample1_should_be_true(self):
        k = 3
        l = [-1, -3, 4, 2]
        res = ap.solve(l, k)
        self.assertEqual(res, True)

    def test_sample2_should_be_false(self):
        k = 2
        l = [0, -1, 2, 1]
        res = ap.solve(l, k)
        self.assertEqual(res, False)
