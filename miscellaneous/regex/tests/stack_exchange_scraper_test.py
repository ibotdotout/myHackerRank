# https://www.hackerrank.com/challenges/stack-exchange-scraper

import stack_exchange_scraper as sxs
import unittest


class StackExchangeScraperTest(unittest.TestCase):

    def test_id_80407(self):
        text = '<div class="summary"><h3>' \
               '<a href="/questions/80407/about-power-supply-of-opertional-amplifier"' \
               ' class="question-hyperlink">about power supply of operational' \
               ' amplifier</a></h3>' \
               '<span title="2013-08-27 21:39:31Z" class="relativetime">11' \
               ' hours ago</span>'
        res = sxs.solve(text)
        ans = "80407;about power supply of operational amplifier;11 hours ago"
        self.assertEqual(ans, res)

    def test_id_80405(self):
        text = '<div class="summary"><h3>' \
               '<a href="/questions/80405/5v-regulator-power-dissipation"' \
               ' class="question-hyperlink">5V Regulator Power' \
               ' Dissipation</a></h3>' \
               '<span title="2013-08-27 21:39:31Z" class="relativetime">11' \
               ' hours ago</span>'
        res = sxs.solve(text)
        ans = "80405;5V Regulator Power Dissipation;11 hours ago"
        self.assertEqual(ans, res)
