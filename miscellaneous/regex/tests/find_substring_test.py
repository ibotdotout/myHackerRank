# https://www.hackerrank.com/challenges/find-substring

import find_substring as fs
import unittest


class FindSubstringTest(unittest.TestCase):

    def test_this_should_be_0(self):
        text = "this"
        word = "is"
        res = fs.solve(text, word)
        self.assertEqual(0, res)

    def test_existing_should_be_0(self):
        text = "existing"
        word = "is"
        res = fs.solve(text, word)
        self.assertEqual(1, res)

    def test_existing_pessimist_optimist_this_is_should_be_3(self):
        text = "existing pessimist optimist this is"
        word = "is"
        res = fs.solve(text, word)
        self.assertEqual(3, res)
