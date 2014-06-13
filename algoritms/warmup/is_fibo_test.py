# https://www.hackerrank.com/challenges/is-fibo

import unittest
import is_fibo as fibo


class IsFiboTest(unittest.TestCase):
    def setUp(self):
        self.fibo_list = fibo.fibo_list(10)

    def test_input_5_get_IsFibo(self):
        n = 5
        result = fibo.is_fibo(self.fibo_list, n)
        self.assertTrue(result)

    def test_input_8_get_IsFibo(self):
        n = 8
        result = fibo.is_fibo(self.fibo_list, n)
        self.assertTrue(result)

    def test_input_7_get_IsNotFibo(self):
        n = 7
        result = fibo.is_fibo(self.fibo_list, n)
        self.assertFalse(result)

    def test_fibo_list_10_get_0112358(self):
        self.assertEqual([0, 1, 1, 2, 3, 5, 8], self.fibo_list)
