# https://www.hackerrank.com/challenges/building-a-list

import unittest
import building_list as bl


class BuildingListTest(unittest.TestCase):

    def test_sample_case_ab(self):
        w = "ab"
        res = bl.solve(w)
        self.assertEqual(res, ["a", "ab", "b"])

    def test_sample_case_xy(self):
        w = "xy"
        res = bl.solve(w)
        self.assertEqual(res, ["x", "xy", "y"])

    def test_sample_case_xyz(self):
        w = "xyz"
        res = bl.solve(w)
        self.assertEqual(res, ["x", "xy", "xyz", "xz", "y", "yz", "z"])
