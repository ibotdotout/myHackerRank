# https://www.hackerrank.com/challenges/acm-icpc-team

import acm_icpc_team as ait
import unittest


class AcmIcpcTeamTest(unittest.TestCase):

    def test_sample_should_be_5_2(self):
        l = ["10101", "11100", "11010", "00101"]
        res = ait.solve(l)
        self.assertEqual(res, [5, 2])

    def test_sample2_should_be_5_2(self):
        l = ["10101", "11101", "11010", "00101"]
        res = ait.solve(l)
        self.assertEqual(res, [5, 3])
