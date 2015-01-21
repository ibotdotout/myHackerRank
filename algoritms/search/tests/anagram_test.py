# https://www.hackerrank.com/challenges/anagram

import anagram as ag
import unittest


class AnagramTest(unittest.TestCase):

    def test_give_abc_should_be_m1(self):
        w = "abc"
        res = ag.solve(w)
        self.assertEqual(res, -1)

    def test_give_ab_should_be_1(self):
        w = "ab"
        res = ag.solve(w)
        self.assertEqual(res, 1)

    def test_give_aaabbb_should_be_3(self):
        w = "aaabbb"
        res = ag.solve(w)
        self.assertEqual(res, 3)

    def test_give_xyyx_should_be_0(self):
        w = "xyyx"
        res = ag.solve(w)
        self.assertEqual(res, 0)
