# https://www.hackerrank.com/challenges/sherlock-and-anagrams


import unittest
import sherlock_and_anagrams as saa


class SherlockAndAnagramsTest(unittest.TestCase):

    def test_give_abba_should_be_4(self):
        w = "abba"
        res = saa.solve(w)
        self.assertEqual(res, 4)

    def test_give_abcd_should_be_0(self):
        w = "abcd"
        res = saa.solve(w)
        self.assertEqual(res, 0)

    def test_give_aba_should_be_2(self):
        w = "aba"
        res = saa.solve(w)
        self.assertEqual(res, 2)

    def test_give_aaabcaaa_should_be_6(self):
        w = "aaabcaaa"
        res = saa.solve(w)
        self.assertEqual(res, 36)

    def test_give_aaa_should_be_4(self):
        w = "aaa"
        res = saa.solve(w)
        self.assertEqual(res, 4)

    def test_give_aaaa_should_be_10(self):
        w = "aaaa"
        res = saa.solve(w)
        self.assertEqual(res, 10)
