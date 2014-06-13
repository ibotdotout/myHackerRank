# https://www.hackerrank.com/challenges/filling-jars

import unittest
import filling_jars as fj


class FillingJarsTest(unittest.TestCase):
    def test_input_1_2_100_get_200(self):
        a, b, k = 1, 2, 100
        excepted_result = 200
        result = fj.fill_jars(a, b, k)
        self.assertEqual(excepted_result, result)

    def test_input_2_5_100_get_400(self):
        a, b, k = 2, 5, 100
        excepted_result = 400
        result = fj.fill_jars(a, b, k)
        self.assertEqual(excepted_result, result)

    def test_input_3_4_100_get_200(self):
        a, b, k = 3, 4, 100
        excepted_result = 200
        result = fj.fill_jars(a, b, k)
        self.assertEqual(excepted_result, result)
