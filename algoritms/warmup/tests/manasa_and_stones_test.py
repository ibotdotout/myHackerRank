# https://www.hackerrank.com/challenges/manasa-and-stones

import unittest
import manasa_and_stones as mas


class ManasaAndStonesTest(unittest.TestCase):
    def test_input_3_1_2_get_2_3_4(self):
        _input = [3, 1, 2]
        expected_result = [2, 3, 4]
        result = mas.manasa_stones(_input)
        self.assertEqual(expected_result, result)

    def test_input_4_10_100_get_30_120_210_300(self):
        _input = [4, 10, 100]
        expected_result = [30, 120, 210, 300]
        result = mas.manasa_stones(_input)
        self.assertEqual(expected_result, result)
