# https://www.hackerrank.com/challenges/cut-the-tree

import unittest
import cut_the_tree


class CutTheTreeTest(unittest.TestCase):
    def test_case1_should_be_400(self):
        v = [100, 200, 100, 500, 100, 600]
        edge = [[1, 2], [2, 3], [2, 5], [4, 5], [5, 6]]
        expected = 400
        result = cut_the_tree.minimun_tree_diff(v, edge)
        self.assertEqual(expected, result)

    def test_case4_should_be_99(self):
        v = [205, 573, 985, 242, 830, 514, 592, 263, 142, 915]
        edge = [[2, 8], [10, 5], [1, 7], [6, 9], [4, 3], [8, 10], [5, 1],
                [7, 6], [9, 4]]
        expected = 99
        result = cut_the_tree.minimun_tree_diff(v, edge)
        self.assertEqual(expected, result)

    def test_case5_should_be_1068(self):
        import os
        test_input = os.path.join(os.path.dirname(__file__),
                                  "cut_the_tree_test_input_05.txt")
        with open(test_input, 'r') as fin:
            n = int(fin.readline())
            v = map(int, fin.readline().split())
            edge = [map(int, fin.readline().split()) for i in xrange(n-1)]
        expected = 1068
        result = cut_the_tree.minimun_tree_diff(v, edge)
        self.assertEqual(expected, result)
