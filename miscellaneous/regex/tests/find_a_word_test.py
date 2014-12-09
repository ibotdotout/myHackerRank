# https://www.hackerrank.com/challenges/find-a-word

import find_a_word as faw
import unittest


class FindAWordTest(unittest.TestCase):

    def test_foo_with_foo_should_be_1(self):
        text = "foo"
        word = "foo"
        res = faw.solve(text, word)
        self.assertEqual(res, 1)

    def test_foo_foo_hyphen_bar_with_foo_should_be_2(self):
        text = "foo foo-bar"
        word = "foo"
        res = faw.solve(text, word)
        self.assertEqual(res, 2)

    def test_foo_foo_dot_bar_with_foo_should_be_2(self):
        text = "foo foo.bar"
        word = "foo"
        res = faw.solve(text, word)
        self.assertEqual(res, 2)

    def test_foo_foo_dot_foo_with_foo_should_be_2(self):
        text = "foo foo.foo"
        word = "foo"
        res = faw.solve(text, word)
        self.assertEqual(res, 3)

    def test_foo_foo_under_bar_with_foo_should_be_1(self):
        text = "foo foo_bar"
        word = "foo"
        res = faw.solve(text, word)
        self.assertEqual(res, 1)

    def test_foo_bar_under_foo_with_foo_should_be_1(self):
        text = "foo bar_foo"
        word = "foo"
        res = faw.solve(text, word)
        self.assertEqual(res, 1)

    def test_foo_foobar_with_foo_should_be_1(self):
        text = "foo foobar"
        word = "foo"
        res = faw.solve(text, word)
        self.assertEqual(res, 1)

    def test_open_foo_closed_with_foo_should_be_1(self):
        text = "(foo) foobar"
        word = "foo"
        res = faw.solve(text, word)
        self.assertEqual(res, 1)
