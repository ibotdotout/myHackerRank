# https://www.hackerrank.com/challenges/almost-sorted

import almost_sorted as als
import unittest


class AlmostSortedTest(unittest.TestCase):

    def test_sorted_give_2_4_should_be_true(self):
        l = [2, 4]
        res = als.solve(l)
        self.assertEqual(res, True)

    def test_swap_give_4_2_shoud_be_1_2(self):
        l = [4, 2]
        res = als.solve(l)
        self.assertEqual(res, [1, 2])

    def test_reverse_give_1_5_4_3_2_6_shoud_be_2_5(self):
        l = [1, 5, 4, 3, 2, 6]
        res = als.solve(l)
        self.assertEqual(res, (2, 5))

    def test_reverse_give_1_6_5_4_3_2_7_shoud_be_2_6(self):
        l = [1, 6, 5, 4, 3, 2, 7]
        res = als.solve(l)
        self.assertEqual(res, (2, 6))

    def test_no_give_3_1_2_shoud_be_none(self):
        l = [3, 1, 2]
        res = als.solve(l)
        self.assertEqual(res, None)
