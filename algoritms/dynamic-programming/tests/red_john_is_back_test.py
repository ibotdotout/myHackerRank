# https://www.hackerrank.com/challenges/red-john-is-back

import unittest
import red_john_is_back as rj


class RedJohnIsBack(unittest.TestCase):
    def test_arrage_brick_given_3_should_be_0(self):
        given = 3
        expected = 0
        result = rj.arrage_brick(given)
        self.assertEqual(expected, result)

    def test_arrage_brick_given_4_should_be_2(self):
        given = 4
        expected = 2
        result = rj.arrage_brick(given)
        self.assertEqual(expected, result)

    def test_arrage_brick_given_7_should_be_5(self):
        given = 7
        expected = 5
        result = rj.arrage_brick(given)
        self.assertEqual(expected, result)

    def test_given_1_should_be_0(self):
        given = 1
        expected = 0
        result = rj.solve(given)
        self.assertEqual(expected, result)

    def test_given_7_should_be_3(self):
        given = 7
        expected = 3
        result = rj.solve(given)
        self.assertEqual(expected, result)
