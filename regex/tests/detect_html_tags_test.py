# https://www.hackerrank.com/challenges/detect-html-tags

import detect_html_tags as html
import unittest


class DetectHtmlTagsTest(unittest.TestCase):

    def test_p_tags(self):
        text = "<p></p>"
        res = html.solve(text)
        self.assertEqual("p", res)

    def test_p_slash_tags(self):
        text = "<p/>"
        res = html.solve(text)
        self.assertEqual("p", res)

    def test_div_tags(self):
        text = "<div>blabla</div>"
        res = html.solve(text)
        self.assertEqual("div", res)

    def test_p_tags_with_space(self):
        text = "<   p   ></p>"
        res = html.solve(text)
        self.assertEqual("p", res)

    def test_a_div_p_tags(self):
        text = '''<p><a href="http://www.quackit.com/html/tutorial/''' \
               '''html_links.cfm">Eresrrresr</a></p> <div class="more-info"><a ''' \
               '''href="http://www.quackit.com/html/examples/''' \
               '''html_links_examples.cfm">fsesfesf</a></div>'''
        res = html.solve(text)
        self.assertEqual("a;div;p", res)
