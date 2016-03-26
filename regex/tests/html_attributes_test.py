# https://www.hackerrank.com/challenges/html-attributes

import html_attributes as html
import unittest


class HtmlAttributesTest(unittest.TestCase):

    def test_p_tag_should_be_p(self):
        text = '<p>hello</p>'
        res = html.solve(text)
        self.assertEqual(["p:"], res)

    def test_div_class_tag_should_be_div_class(self):
        text = '<div class="bla">hello</div>'
        res = html.solve(text)
        self.assertEqual(["div:class"], res)

    def test_p_div_class_tag_should_be_div_class_p(self):
        text = '<p>hello</p><div class="bla">hello</div>'
        res = html.solve(text)
        self.assertEqual(["div:class", "p:"], res)

    def test_p_div_class_div_class_id_tag_should_be_div_class_id_p(self):
        text = '<p>hello</p><div class="bla">hello</div><div id=\'x\''\
               'class="bla">hello</div>'
        res = html.solve(text)
        self.assertEqual(["div:class,id", "p:"], res)

    def test_p_div_class_div_id_tag_should_be_div_class_id_p(self):
        text = '<p>hello</p><div class="bla">hello</div><div id=\'x\'' \
               '>hello</div>'
        res = html.solve(text)
        self.assertEqual(["div:class,id", "p:"], res)
