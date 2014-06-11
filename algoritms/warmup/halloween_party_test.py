# https://www.hackerrank.com/challenges/halloween-party

import unittest
import halloween_party as hp


class HalloweenPartyTest(unittest.TestCase):
    def test_input_5_get_6(self):
        k = 5
        expected_result = 6
        result = hp.get_maximun_pieces(k)
        self.assertEqual(expected_result, result)

    def test_input_6_get_9(self):
        k = 6
        expected_result = 9
        result = hp.get_maximun_pieces(k)
        self.assertEqual(expected_result, result)

    def test_input_7_get_12(self):
        k = 7
        expected_result = 12
        result = hp.get_maximun_pieces(k)
        self.assertEqual(expected_result, result)

    def test_input_8_get_16(self):
        k = 8
        expected_result = 16
        result = hp.get_maximun_pieces(k)
        self.assertEqual(expected_result, result)
