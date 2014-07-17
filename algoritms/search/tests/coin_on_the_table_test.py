# https://www.hackerrank.com/challenges/coin-on-the-table

import unittest
import coin_on_the_table as cott


class CoinOnTheTableTest(unittest.TestCase):

    def test_case1_should_be_0(self):
        k = 3
        table = ["RD", "*L"]
        expected = 0
        result = cott.operation_require(table, k)
        self.assertEqual(expected, result)

    def test_case2_should_be_1(self):
        k = 1
        table = ["RD", "*L"]
        expected = 1
        result = cott.operation_require(table, k)
        self.assertEqual(expected, result)

    def test_case0_should_be_minus_1(self):
        k = 0
        table = ["RD", "*L"]
        expected = -1
        result = cott.operation_require(table, k)
        self.assertEqual(expected, result)

    def test_case3_should_be_0(self):
        k = 2
        table = ["RRLD", "D*RR"]
        expected = 1
        result = cott.operation_require(table, k)
        self.assertEqual(expected, result)

    def test_case10_should_be_1(self):
        k = 5
        table = ["RRD", "DLL", "*UU"]
        expected = 1
        result = cott.operation_require(table, k)
        self.assertEqual(expected, result)
