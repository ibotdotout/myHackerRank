# https://www.hackerrank.com/challenges/palindrome-index

import palindrome_index as pi
import unittest


class PalindromeIndexTest(unittest.TestCase):

    def test_give_aaab_should_be_3(self):
        w = "aaab"
        res = pi.solve(w)
        self.assertEqual(res, 3)

    def test_give_aaa_should_be_m1(self):
        w = "aaa"
        res = pi.solve(w)
        self.assertEqual(res, -1)

    def test_give_baa_should_be_0(self):
        w = "baa"
        res = pi.solve(w)
        self.assertEqual(res, 0)
