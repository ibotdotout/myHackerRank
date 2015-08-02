# https://www.hackerrank.com/challenges/split-number

import split_number as sp
import unittest


class SplitNumberTest(unittest.TestCase):

    def test_space(self):
        text = "1 877 2638277"
        res = sp.solve(text)
        self.assertEqual(res, ("1", "877", "2638277"))

    def test_hyphen(self):
        text = "1-877-2634277"
        res = sp.solve(text)
        self.assertEqual(res, ("1", "877", "2634277"))
