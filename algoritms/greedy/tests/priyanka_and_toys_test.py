# https://www.hackerrank.com/challenges/priyanka-and-toys

import unittest
import priyanka_and_toys as pat


class PriyakaAndToysTest(unittest.TestCase):

    def test_give_1_2_3_17_10_should_be_3(self):
        l = [1, 2, 3, 17, 10]
        res = pat.solve(l)
        self.assertEqual(res, 3)

    def test_give_1_2_3_5_6_17_10_should_be_4(self):
        l = [1, 2, 3, 5, 31, 17, 10]
        res = pat.solve(l)
        self.assertEqual(res, 4)

    def test_give_16_18_10_13_2_9_17_17_0_19_should_be_(self):
        l = [16, 18, 10, 13, 2, 9, 17, 17, 0, 19]
        res = pat.solve(l)
        self.assertEqual(res, 3)
