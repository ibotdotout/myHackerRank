# https://www.hackerrank.com/challenges/uk-and-us

import uk_and_us as ukus
import unittest


class UkAndUsTest(unittest.TestCase):

    def test_find_end_with_ze_should_be_1(self):
        text = "to familiarize oneself with ui of hackerrank is easy"
        word = "familiarize"
        res = ukus.solve(text, word)
        self.assertEqual(1, res)

    def test_find_end_with_se_should_be_2(self):
        text = "hackerrank has such a good ui that it takes no time to" \
               "familiarise its environment"
        word = "familiarize"
        res = ukus.solve(text, word)
        self.assertEqual(1, res)

    def test_find_end_with_za_and_se_should_be_2(self):
        text = "hackerrank has such a good ui that it takes no time to" \
               "familiarise its environment" \
               "to familiarize oneself with ui of hackerrank is easy"
        word = "familiarize"
        res = ukus.solve(text, word)
        self.assertEqual(2, res)
