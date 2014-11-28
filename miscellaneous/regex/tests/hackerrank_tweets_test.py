# https://www.hackerrank.com/challenges/hackerrank-tweets

import hackerrank_tweets as ht
import unittest


class HackerrankTweetsTest(unittest.TestCase):

    def test_1tag_should_be_1(self):
        text = "I love #hackerrank"
        res = ht.solve(text)
        self.assertEqual(res, 1)

    def test_no_tag_should_be_0(self):
        text = "I love #hckerrank"
        res = ht.solve(text)
        self.assertEqual(res, 0)
