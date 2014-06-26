# https://www.hackerrank.com/challenges/game-of-rotation

import unittest
import game_of_rotation as gr


class GameOfRotationTest(unittest.TestCase):
    def test_case1_get_140(self):
        l = [20, 30, 10]
        exptected_result = 140
        result = gr.get_PMEAN(l)
        self.assertEqual(exptected_result, result)

    def test_case2_get_70(self):
        l = [20, 30, 10, -100]
        exptected_result = 70
        result = gr.get_PMEAN(l)
        self.assertEqual(exptected_result, result)
