# https://www.hackerrank.com/challenges/tutorial-intro

import unittest
import tutorial_intro as ti


class TutorialIntroTest(unittest.TestCase):
    def setUp(self):
        self.l = [1, 4, 5, 7, 9, 12]

    def test_input_4_get_1(self):
        num = 4
        expected_result = 1
        result = ti.get_index(self.l, num)
        self.assertEqual(expected_result, result)

    def test_input_7_get_3(self):
        num = 7
        expected_result = 3
        result = ti.get_index(self.l, num)
        self.assertEqual(expected_result, result)
