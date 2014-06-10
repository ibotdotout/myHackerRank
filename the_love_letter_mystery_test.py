# https://www.hackerrank.com/challenges/the-love-letter-mystery

import unittest
import the_love_letter_mystery as ll


class LoveLetterTest(unittest.TestCase):
    def test_input_abc_get_2(self):
        text = "abc"
        expected_result = 2
        result = ll.get_reduce_number_to_palindrome(text)
        self.assertEquals(expected_result, result)

    def test_input_abcba_get_0(self):
        text = "abcba"
        expected_result = 0
        result = ll.get_reduce_number_to_palindrome(text)
        self.assertEquals(expected_result, result)

    def test_input_abcd_get_4(self):
        text = "abcd"
        expected_result = 4
        result = ll.get_reduce_number_to_palindrome(text)
        self.assertEquals(expected_result, result)
