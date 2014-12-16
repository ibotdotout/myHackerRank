# https://www.hackerrank.com/challenges/even-tree

import even_tree as et
import unittest


class EvenTreeTest(unittest.TestCase):

    def test_count_node(self):
        v_list = [(2, 1), (3, 2), (4, 2)]
        m, n = 4, 3
        res = et.count_node(v_list, m, n)
        self.assertEqual(res, [4, 3, 1, 1])

    def test_even_tree(self):
        v_list = [(1, 5), (6, 5), (2, 1), (3, 2), (4, 2)]
        m, n = 6, 5
        res = et.even_tree(v_list, m, n)
        self.assertEqual(res, 1)
