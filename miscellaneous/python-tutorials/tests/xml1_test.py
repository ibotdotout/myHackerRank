# https://www.hackerrank.com/challenges/xml-1-find-the-score

import unittest
import xml1


class Xml1Test(unittest.TestCase):
    def test_sample_case(self):
        given = "<feed xml:lang='en'>\n" \
                "    <title>HackerRank</title>\n" \
                "    <subtitle lang='en'>Programming challenges</subtitle>\n" \
                "    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>\n" \
                "    <updated>2013-12-25T12:00:00</updated>\n" \
                "</feed>"
        expected = 5
        result = xml1.score(given)
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
        expected = 8
        result = xml1.score(given)
        self.assertEqual(expected, result)
