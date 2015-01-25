# https://www.hackerrank.com/challenges/bigger-is-greater

import bigger_is_greater as big
import unittest


class BiggerIsGreaterTest(unittest.TestCase):

    def test_give_bb_should_be_bb(self):
        w = "bb"
        res = big.solve(w)
        self.assertEqual(res, "bb")

    def test_give_ab_should_be_ba(self):
        w = "ab"
        res = big.solve(w)
        self.assertEqual(res, "ba")

    def test_give_hefg_should_be_hegf(self):
        w = "hefg"
        res = big.solve(w)
        self.assertEqual(res, "hegf")

    def test_give_zwrjvf_should_be_zwrvfj(self):
        w = "zwrjvf"
        res = big.solve(w)
        self.assertEqual(res, "zwrvfj")

    def test_give_xsezxuqpj_should_be_xsjepquxz(self):
        w = "xsezxuqpj"
        res = big.solve(w)
        self.assertEqual(res, "xsjepquxz")
