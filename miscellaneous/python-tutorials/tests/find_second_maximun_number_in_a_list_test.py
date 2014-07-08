# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

import unittest
import find_second_maximun_number_in_a_list as fs


class FindSecondMaximunNumberInAListTest(unittest.TestCase):
    def test_case1_should_get_5(self):
        l = [2, 3, 6, 6, 5]
        expected_result = 5
        result = fs.second_max(l)
        self.assertEqual(expected_result, result)

    def test_case1_should_get_minus57(self):
        l = [57, 57, -57, 57]
        expected_result = -57
        result = fs.second_max(l)
        self.assertEqual(expected_result, result)
