# https://www.hackerrank.com/challenges/detect-html-links

import detect_html_links as dtl
import unittest


class DetectHtmlLinksTest(unittest.TestCase):

    def test_hackerrank_com_HackerRank(self):
        text = '<a href="http://www.hackerrank.com">HackerRank</a>'
        res = dtl.solve(text)
        self.assertEqual(res, ["http://www.hackerrank.com,HackerRank"])

    def test_hrank_io_HackerRank(self):
        text = '<a href="http://hrank.io">HackerRank</a>'
        res = dtl.solve(text)
        self.assertEqual(res, ["http://hrank.io,HackerRank"])

    def test_hrank_io_HackerRank_with_blank(self):
        text = '<a href="http://hrank.io">    HackerRank    </a>'
        res = dtl.solve(text)
        self.assertEqual(res, ["http://hrank.io,HackerRank"])

    def test_hrank_io_with_html_tags_HackerRank(self):
        text = '<a href="http://www.hackerrank.com">' \
               '<h1><b>HackerRank</b></h1></a>'
        res = dtl.solve(text)
        self.assertEqual(res, ["http://www.hackerrank.com,HackerRank"])

    def test_p_tag_has_a_href(self):
        text = '<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">' \
               'Example Link</a></p>'
        res = dtl.solve(text)
        ans = \
            "http://www.quackit.com/html/tutorial/html_links.cfm,Example Link"
        self.assertEqual(res, [ans])

    def test_multiple_line(self):
        text = '<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">' \
               'Example Link</a></p>' \
               '<div class="more-info"><a href="http://www.quackit.com/html/' \
               'examples/html_links_examples.cfm">More' \
               ' Link Examples...</a></div>'
        res = dtl.solve(text)
        ans = [
            "http://www.quackit.com/html/tutorial/html_links.cfm,Example Link",
            "http://www.quackit.com/html/examples/html_links_examples.cfm,"
            "More Link Examples..."]
        self.assertEqual(res, ans)

    def test_spacial_char_in_link(self):
        text = '<li id="n-sitesupport"><a' \
               ' href="//donate.wikimedia.org/wiki/Special:' \
               'FundraiserRedirector?utm_source=donate&amp;' \
               'utm_medium=sidebar&amp;utm_campaign=' \
               'C13_en.wikipedia.org&amp;uselang=en" ' \
               'title="Support us">Donate to Wikipedia</a></li>'
        res = dtl.solve(text)
        ans = ["//donate.wikimedia.org/wiki/Special:FundraiserRedirector?"
               "utm_source=donate&amp;utm_medium=sidebar&amp;utm_campaign="
               "C13_en.wikipedia.org&amp;uselang=en,Donate to Wikipedia"]
        self.assertEqual(res, ans)

    def test_blank_title(self):
        text = '<li class="interwiki-bg"><a href="//bg.wikipedia.org/wiki/" ' \
               'title="" lang="bg" hreflang="bg"></a></li>'
        res = dtl.solve(text)
        ans = ["//bg.wikipedia.org/wiki/,"]
        self.assertEqual(res, ans)

    def test_area_href_should_not_found(self):
        text = '<li class="interwiki-bg"><area href="//bg.wikipedia.org/wiki/" ' \
               'title="" lang="bg" hreflang="bg"></a></li>'
        res = dtl.solve(text)
        ans = []
        self.assertEqual(res, ans)
