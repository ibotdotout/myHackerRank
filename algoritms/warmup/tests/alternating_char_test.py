# https://www.hackerrank.com/challenges/alternating-characters

import unittest
import alternating_char as ac


class AlternatingCharTest(unittest.TestCase):

    def test_ABABABAB_should_be_0(self):
        text = "ABABABAB"
        res = ac.solve(text)
        self.assertEqual(res, 0)

    def test_AAAA_should_be_3(self):
        text = "AAAA"
        res = ac.solve(text)
        self.assertEqual(res, 3)

    def test_BABABA_should_be_0(self):
        text = "BABABA"
        res = ac.solve(text)
        self.assertEqual(res, 0)
