# https://www.hackerrank.com/challenges/play-game

import unittest
import play_game


class PlayGameTest(unittest.TestCase):
    def test_case_sample1_shoul_be_1001(self):
        stack = [999, 1, 1, 1, 0]
        expected = 1001
        result = play_game.play(stack)
        self.assertEqual(expected, result)

    def test_case_sample2_shoul_be_999(self):
        stack = [0, 1, 1, 1, 999]
        expected = 999
        result = play_game.play(stack)
        self.assertEqual(expected, result)

    def test_case1_shoul_be_1999(self):
        stack = [0, 1, 1, 1, 999, 1, 1, 1, 1000]
        expected = 1999
        result = play_game.play(stack)
        self.assertEqual(expected, result)
