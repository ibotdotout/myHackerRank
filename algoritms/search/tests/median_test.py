# https://www.hackerrank.com/challenges/median

import unittest
import median


class MedianTest(unittest.TestCase):
    def test_case_sample(self):
        a, r, w = 'a', 'r', 'Wrong!'
        given = [(r, 1), (a, 1), (a, 2), (a, 1), (r, 1), (r, 2), (r, 1)]
        expected = [w, 1, 1.5, 1, 1.5, 1, w]
        result = median.running_median(given)
        self.assertEqual(expected, list(result))

    def test_case_sample2(self):
        a = 'a'
        given = [(a, 9), (a, 2), (a, 8), (a, 4), (a, 1)]
        expected = [9, 5.5, 8, 6, 4]
        result = median.running_median(given)
        self.assertEqual(expected, list(result))

    def case_from_file(self, case):
        import os
        path = os.path.dirname(__file__) + '/median_test_'
        with open(path + 'input' + case + '.txt', 'r') as fin:
            cmd = lambda x: (x[0], int(x[1]))
            n = int(fin.readline())
            given = [cmd(fin.readline().split()) for i in xrange(n)]
        with open(path + 'output' + case + '.txt', 'r') as fout:
            expected = [fout.readline().strip() for i in xrange(n)]
        result = median.running_median(given)
        i = 0
        max_iter = 100000
        for res in result:
            if i > max_iter:
                break
            self.assertEqual(expected[i], str(res))
            i += 1

    def test_case3(self):
        self.case_from_file('03')

    def test_case1(self):
        self.case_from_file('01')
