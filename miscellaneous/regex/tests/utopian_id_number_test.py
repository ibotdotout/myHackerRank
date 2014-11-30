# https://www.hackerrank.com/challenges/utopian-identification-number

import utopian_id_number as uin
import unittest


class UtopianIdNumberTest(unittest.TestCase):

    def test_abc012333ABCDEEEE_should_be_ture(self):
        text = "abc012333ABCDEEEE"
        res = uin.solve(text)
        self.assertEqual(True, res)

    def test_0123AB_should_be_ture(self):
        text = "0123AB"
        res = uin.solve(text)
        self.assertEqual(False, res)
