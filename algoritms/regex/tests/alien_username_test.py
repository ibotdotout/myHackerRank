# https://www.hackerrank.com/challenges/alien-username

import alien_username as au
import unittest


class AlienUsernameTest(unittest.TestCase):

    def test__0898989811abced__should_be_true(self):
        text = "_0898989811abced_"
        res = au.solve(text)
        self.assertEqual(True, res)

    def test_d0898989811abced__should_be_true(self):
        text = ".0898989811abced_"
        res = au.solve(text)
        self.assertEqual(True, res)

    def test_d0898989811ABced__should_be_true(self):
        text = ".0898989811ABced_"
        res = au.solve(text)
        self.assertEqual(True, res)

    def test__abce_should_be_false(self):
        text = "_abce"
        res = au.solve(text)
        self.assertEqual(False, res)

    def test__09090909abcD0_should_be_false(self):
        text = "_09090909abcD0"
        res = au.solve(text)
        self.assertEqual(False, res)
