# https://www.hackerrank.com/challenges/sherlock-and-queries

import unittest
import sherlock_and_queries as saq


class SherlockAndQuriesTest(unittest.TestCase):
    def test_case1_should_be_13_754_2769_1508(self):
        a = [1, 2, 3, 4]
        b = [1, 2, 3]
        c = [13, 29, 71]
        expected_result = [13, 754, 2769, 1508]
        result = saq.queries(a, b, c)
        self.assertEqual(expected_result, result)

    def test_case10(self):
        import os
        path = os.path.dirname(__file__) + '/sherlock_and_queries_test_'
        with open(path + 'input10.txt', 'r') as fin:
            fin.readline()  # skip first line
            a = map(int, fin.readline().split())
            b = map(int, fin.readline().split())
            c = map(int, fin.readline().split())
        with open(path + 'output10.txt', 'r') as fout:
            expected_result = map(int, fout.readline().split())
        result = saq.queries(a, b, c)
        self.assertEqual(expected_result[:1000], result[:1000])
