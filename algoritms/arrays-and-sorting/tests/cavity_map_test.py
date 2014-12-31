# https://www.hackerrank.com/challenges/cavity-map

import unittest
import cavity_map as cm


class CavityMapTest(unittest.TestCase):

    def test_sample_case(self):
        m = [[1, 1, 1, 2], [1, 9, 1, 2], [1, 8, 9, 2], [1, 2, 3, 4]]
        res = cm.solve(m)
        ans = ["1112", "1X12", "18X2", "1234"]
        res = ["".join(map(str, i)) for i in res]
        self.assertEqual(res, ans)
