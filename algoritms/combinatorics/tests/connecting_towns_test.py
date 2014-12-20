# https://www.hackerrank.com/challenges/connecting-towns

import unittest
import connecting_towns


class ConnectingTownsTest(unittest.TestCase):

    def test_give_1_3_should_be_3(self):
        give = [1, 3]
        res = connecting_towns.solve(give)
        self.assertEqual(res, 3)

    def test_give_2_2_2_should_be_8(self):
        give = [2, 2, 2]
        res = connecting_towns.solve(give)
        self.assertEqual(res, 8)
