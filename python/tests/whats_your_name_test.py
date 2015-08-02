# https://www.hackerrank.com/challenges/whats-your-name

import unittest
import whats_your_name as wyn


class WhatsYourNameTest(unittest.TestCase):
    def test_case1(self):
        name = "Guido"
        lastname = "Rossum"
        expected_result = "Hello Guido Rossum! You just delved into python."
        result = wyn.into_python(name, lastname)
        self.assertEqual(expected_result, result)
