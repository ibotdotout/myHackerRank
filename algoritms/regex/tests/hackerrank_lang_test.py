# https://www.hackerrank.com/challenges/hackerrank-language

import hackerrank_lang as hl
import unittest


class HackerRankLangTest(unittest.TestCase):

    def test_11011_LUA_should_be_true(self):
        text = "11011 LUA"
        res = hl.solve(text)
        self.assertEqual(True, res)

    def test_11044_X_should_be_false(self):
        text = "11044 X"
        res = hl.solve(text)
        self.assertEqual(False, res)

    def test_1_CPP_should_be_false(self):
        text = "1 CPP"
        res = hl.solve(text)
        self.assertEqual(False, res)
