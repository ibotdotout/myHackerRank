# https://www.hackerrank.com/challenges/bus-station

import bus_station as bs
import unittest


class BusStationTest(unittest.TestCase):

    def test_give_1_2_1_1_1_should_be_3_6(self):
        l = [1, 2, 1, 1, 1]
        res = bs.solve(l)
        self.assertEqual(res, [3, 6])

    def test_give_1_2_1_1_1_2_1_3_should_be_3_4_6_12(self):
        l = [1, 2, 1, 1, 1, 2, 1, 3]
        res = bs.solve(l)
        self.assertEqual(res, [3, 4, 6, 12])
