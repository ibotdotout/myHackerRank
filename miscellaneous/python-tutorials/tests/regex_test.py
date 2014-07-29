# https://www.hackerrank.com/challenges/regex-1-validating-the-phone-number

import unittest
import regex


class RegexTest(unittest.TestCase):
    def test_case_sample1_should_be_True(self):
        given = 9587456281
        expected = True
        result = regex.is_phone_number(given)
        self.assertEqual(expected, result)

    def test_case_sample2_should_be_False(self):
        given = 1252478965
        expected = False
        result = regex.is_phone_number(given)
        self.assertEqual(expected, result)

    def test_case_sample3_should_be_False(self):
        given = "a7252478965"
        expected = False
        result = regex.is_phone_number(given)
        self.assertEqual(expected, result)
