# https://www.hackerrank.com/challenges/saying-hi

import saying_hi as sh
import unittest


class SayingHiTest(unittest.TestCase):

    def test_Hi_Alex_how_are_you_doing_should_be_true(self):
        text = "Hi Alex how are you doing"
        res = sh.solve(text)
        self.assertEqual(True, res)

    def test_Alex_greeted_Martha_by_saying_Hi_Martha_should_be_false(self):
        text = "Alex greeted Martha by saying Hi Martha"
        res = sh.solve(text)
        self.assertEqual(False, res)

    def test_hI_dave_how_are_you_doing_should_be_false(self):
        text = "hI dave how are you doing"
        res = sh.solve(text)
        self.assertEqual(False, res)
