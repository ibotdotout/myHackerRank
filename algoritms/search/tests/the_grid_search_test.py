# https://www.hackerrank.com/challenges/the-grid-search

import the_grid_search as tgs
import unittest


class TheGridSearchTest(unittest.TestCase):

    def test_sample_case_should_be_true(self):
        grid = ["1234567890", "0987654321", "1111111111", "1111111111",
                "2222222222"]
        pattern = ["876543", "111111", "111111"]
        res = tgs.solve(grid, pattern)
        self.assertEqual(res, True)

    def test_sample_case_should_be_false(self):
        grid = ["1234567890", "0987654321", "1111111111", "1111111111",
                "2222222222"]
        pattern = ["876543", "222222", "222222"]
        res = tgs.solve(grid, pattern)
        self.assertEqual(res, False)
