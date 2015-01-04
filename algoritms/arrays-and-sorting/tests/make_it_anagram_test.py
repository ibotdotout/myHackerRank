# https://www.hackerrank.com/challenges/make-it-anagram

import make_it_anagram as mia
import unittest


class MakeItAnagramTests(unittest.TestCase):

    def test_cde_abc_should_be_4(self):
        a = "cde"
        b = "abc"
        res = mia.solve(a, b)
        self.assertEqual(res, 4)

    def test_abe_abc_should_be_2(self):
        a = "abe"
        b = "abc"
        res = mia.solve(a, b)
        self.assertEqual(res, 2)
