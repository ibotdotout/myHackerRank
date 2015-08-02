# https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth

import unittest
import xml2


class Xml2Test(unittest.TestCase):
    def test_sample_case(self):
        given = "<feed xml:lang='en'>\n" \
                "    <title>HackerRank</title>\n" \
                "    <subtitle lang='en'>Programming challenges</subtitle>\n" \
                "    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>\n" \
                "    <updated>2013-12-25T12:00:00</updated>\n" \
                "</feed>"
        expected = 1
        result = xml2.depth(given)
        self.assertEqual(expected, result)

    def test_sample_case2(self):
        given = "<feed xml:lang='en'>" \
                "<title>HackerRank</title>" \
                "<subtitle lang='en'>Programming challenges</subtitle>" \
                "<link rel='alternate' type='text/html'" \
                " href='http://hackerrank.com/'/>" \
                "<updated>2013-12-25T12:00:00</updated>" \
                "<entry>" \
                "<author gender='male'>Harsh</author>" \
                "<question type='hard'>XML 1</question>" \
                "<description type='text'>This is related to XML" \
                "parsing</description>" \
                "</entry>" \
                "</feed>"
        expected = 2
        result = xml2.depth(given)
        self.assertEqual(expected, result)
