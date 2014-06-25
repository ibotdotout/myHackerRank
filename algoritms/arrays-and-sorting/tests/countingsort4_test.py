# https://www.hackerrank.com/challenges/countingsort4

import unittest
import countingsort4 as cs


class CountingSort4Test(unittest.TestCase):
    def test_case1(self):
        case1 = [(0, 'ab'), (6, 'cd'), (0, 'ef'), (6, 'gh'), (4, 'ij'),
                 (0, 'ab'), (6, 'cd'), (0, 'ef'), (6, 'gh'), (0, 'ij'),
                 (4, 'that'), (3, 'be'), (0, 'to'), (1, 'be'), (5, 'question'),
                 (1, 'or'), (2, 'not'), (4, 'is'), (2, 'to'), (4, 'the')]

        expected_result = '- - - - - to be or not to be '\
                          '- that is the question - - - -'
        result = cs.get_string_order(case1)
        self.assertEqual(expected_result, result)
        pass
