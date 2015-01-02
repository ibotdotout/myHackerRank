# https://www.hackerrank.com/challenges/sherlock-and-watson

import sherlock_and_waton as saw
import unittest


class SherlockAndWatonTest(unittest.TestCase):

    def setUp(self):
        l = [1, 2, 3]
        q = 2
        self.res = saw.solve(l, q)

    def test_0th_array_should_be_2(self):
        index = 0
        self.assertEqual(self.res[index], 2)

    def test_1th_array_should_be_3(self):
        index = 1
        self.assertEqual(self.res[index], 3)

    def test_2th_array_should_be_1(self):
        index = 2
        self.assertEqual(self.res[index], 1)
