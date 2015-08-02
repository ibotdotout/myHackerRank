# https://www.hackerrank.com/challenges/regex-2-validate-a-roman-number

import unittest
import regex2_roman_number as rrn


class RegexRomanNumberTest(unittest.TestCase):
    def test_given_CDXXI_should_be_True(self):
        given = "CDXXI"
        expected = True
        result = rrn.valid_roman_number(given)
        self.assertEqual(expected, result)

    def test_given_AAA_should_be_False(self):
        given = "AAA"
        expected = False
        result = rrn.valid_roman_number(given)
        self.assertEqual(expected, result)

    def test_given_XXXX_should_be_False(self):
        given = "XXXX"
        expected = False
        result = rrn.valid_roman_number(given)
        self.assertEqual(expected, result)

    def test_given_CI_should_be_True(self):
        given = "CI"
        expected = True
        result = rrn.valid_roman_number(given)
        self.assertEqual(expected, result)

    def test_given_IC_should_be_False(self):
        given = "IC"
        expected = False
        result = rrn.valid_roman_number(given)
        self.assertEqual(expected, result)

    def test_given_DXXVIIII_should_be_False(self):
        given = "DXXVIIII"
        expected = False
        result = rrn.valid_roman_number(given)
        self.assertEqual(expected, result)
