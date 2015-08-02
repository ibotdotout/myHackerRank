# https://www.hackerrank.com/challenges/find-a-string

import unittest
import find_a_string as fs


class FindAStringTest(unittest.TestCase):
    def test_case1_should_get_2(self):
        string = "ABCDCDC"
        sub_string = "CDC"
        expected_result = 2
        result = fs.get_index_sub_string(string, sub_string)
        self.assertEqual(expected_result, result)
