# https://www.hackerrank.com/challenges/sherlock-and-gcd

import unittest
import sherlock_and_gcd as sgcd


class SherlcokAndGCDTest(unittest.TestCase):
    def test_give_1_2_3_should_be_True(self):
        l = [1, 2, 3]
        expected_result = True
        result = sgcd.sherlock_gcd(l)
        self.assertEqual(expected_result, result)

    def test_give_2_4_should_be_False(self):
        l = [2, 4]
        expected_result = False
        result = sgcd.sherlock_gcd(l)
        self.assertEqual(expected_result, result)
