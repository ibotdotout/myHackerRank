# https://www.hackerrank.com/challenges/time-conversion

import time_conversion as tc
import unittest


class TimeConversionTest(unittest.TestCase):

    def test_sample_pm(self):
        t = "07:05:45PM"
        result = tc.solve(t)
        self.assertEqual("19:05:45", result)

    def test_sample_am(self):
        t = "07:05:45AM"
        result = tc.solve(t)
        self.assertEqual("07:05:45", result)

    def test_sample_12_am(self):
        t = "12:05:45AM"
        result = tc.solve(t)
        self.assertEqual("00:05:45", result)

    def test_sample_12_pm(self):
        t = "12:05:45PM"
        result = tc.solve(t)
        self.assertEqual("12:05:45", result)
