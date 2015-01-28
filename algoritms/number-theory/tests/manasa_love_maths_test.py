# https://www.hackerrank.com/challenges/manasa-loves-maths

import manasa_love_maths as mlm
import unittest


class ManasaLoveMathsTest(unittest.TestCase):

    def test_give_61_should_be_true(self):
        n = 61
        res = mlm.solve(n)
        self.assertEqual(res, True)

    def test_give_409_should_be_true(self):
        n = 409
        res = mlm.solve(n)
        self.assertEqual(res, True)

    def test_give_22_should_be_False(self):
        n = 12
        res = mlm.solve(n)
        self.assertEqual(res, False)

    def test_give_62_should_be_False(self):
        n = 62
        res = mlm.solve(n)
        self.assertEqual(res, False)

    def test_give_75_should_be_true(self):
        n = 75
        res = mlm.solve(n)
        self.assertEqual(res, False)
