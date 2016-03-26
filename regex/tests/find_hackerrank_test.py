# https://www.hackerrank.com/challenges/find-hackerrank

import unittest
import find_hackerrank as fh


class FindHackerRankTest(unittest.TestCase):

    def test_end_with_hrank_should_be_2(self):
        text = "i love hackerrank"
        res = fh.solve(text)
        self.assertEqual(res, 2)

    def test_start_with_hrank_should_be_1(self):
        text = "hackerrank is an awesome place for programmers"
        res = fh.solve(text)
        self.assertEqual(res, 1)

    def test_hrank_should_be_0(self):
        text = "hackerrank"
        res = fh.solve(text)
        self.assertEqual(res, 0)

    def test_non_hrank_should_be_minus1(self):
        text = "i think hackerrank is a great place to hangout"
        res = fh.solve(text)
        self.assertEqual(res, -1)
