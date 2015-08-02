# https://www.hackerrank.com/challenges/uk-and-us-2

import uk_and_us_2 as uu2
import unittest


class UKandUS2Test(unittest.TestCase):

    def test_odour_odour_should_be_1(self):
        text = "fshh odour sfsfsfesf"
        word = "odour"
        res = uu2.solve(text, word)
        self.assertEqual(1, res)

    def test_odor_odour_odour_should_be_2(self):
        text = "fshh odour odor"
        word = "odour"
        res = uu2.solve(text, word)
        self.assertEqual(2, res)

    def test_odor_odourse_odour_should_be_1(self):
        text = "fshh odourse odor sfsfsfesf"
        word = "odour"
        res = uu2.solve(text, word)
        self.assertEqual(1, res)

    def test_Odor_odourse_odour_should_be_1(self):
        text = "fshh odourse Odor sfsfsfesf"
        word = "odour"
        res = uu2.solve(text, word)
        self.assertEqual(1, res)

