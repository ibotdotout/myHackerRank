# https://www.hackerrank.com/challenges/nested-list

import unittest
import nested_list


class NestedListTest(unittest.TestCase):
    def test_sample_case(self):
        given = [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2],
                 ["Akriti", 41], ["Harsh", 39]]
        expected = ["Berry", "Harry"]
        result = nested_list.second_lowest(given)
        self.assertEqual(expected, result)

    def test_sample_case2(self):
        given = [["Harry", 37.21], ["Berry", 37.31], ["Tina", 37.2],
                 ["Akriti", 41], ["Harsh", 39]]
        expected = ["Harry"]
        result = nested_list.second_lowest(given)
        self.assertEqual(expected, result)
