# https://www.hackerrank.com/contests/w6/challenges/acm-icpc-team

import unittest
import acm_icpc_team as ait


class AcmICPCTeamTest(unittest.TestCase):
    def test_case1_should_get_2_5(self):
        l = ['10101', '11100', '11010', '00101']
        expected_result = [5, 2]
        result = ait.solve(l)
        self.assertEqual(expected_result, result)
