# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators

import unittest
import decorators


class DecoratorsTest(unittest.TestCase):
    def test_sample_case(self):
        numbers = ["07895462130", "919875641230", "9195969878"]
        expected = ["+91 78954 62130", "+91 91959 69878", "+91 98756 41230"]
        result = decorators.standardize(numbers)
        self.assertEqual(expected, result)
