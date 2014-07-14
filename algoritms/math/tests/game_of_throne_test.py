# https://www.hackerrank.com/challenges/game-of-thrones

import unittest
import game_of_throne as got


class GameOfThroneTest(unittest.TestCase):
    def assert_helper(self, given, expected_result):
        result = got.solve(given)
        self.assertEqual(expected_result, result)

    def test_case1_should_be_true(self):
        w = "aaabbbb"
        expected_result = True
        self.assert_helper(w, expected_result)

    def test_case2_should_be_false(self):
        w = "cdefghmnopqrstuvw"
        expected_result = False
        self.assert_helper(w, expected_result)

    def test_case3_should_be_true(self):
        w = "cdcdcdcdeeeef"
        expected_result = True
        self.assert_helper(w, expected_result)
