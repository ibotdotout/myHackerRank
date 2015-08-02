# https://www.hackerrank.com/challenges/decorators-2-name-directory

import unittest
import decorators2


class Decorators2Test(unittest.TestCase):
    def test_sample_case(self):
        given = [['Mike Thomson', 20, 'M'], ['Robert Bustle', 32, 'M'],
                 ['Andria Bustle', 30, 'F']]
        excepted = ['Mr. Mike Thomson', 'Ms. Andria Bustle',
                    'Mr. Robert Bustle']
        result = decorators2.list_name(given)
        self.assertEqual(excepted, result)
