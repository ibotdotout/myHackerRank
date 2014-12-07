# kttps://www.hackerrank.com/challenges/detect-the-email-addresses

import detect_the_email_address as dtea
import unittest


class DetectTheEmailAdressTest(unittest.TestCase):

    def test_botbot_at_gmail_com_should_be_detected(self):
        text = "hello botbot@gmail.com, why you here ?"
        res = dtea.solve(text)
        self.assertEqual(res, "botbot@gmail.com")

    def test_botbot_at_gmail_com_2_timesshould_be_detected(self):
        text = "hello botbot@gmail.com, why you here ?" * 2
        res = dtea.solve(text)
        self.assertEqual(res, "botbot@gmail.com")

    def test_dotdot_at_gmail_com_should_be_detected(self):
        text = "hello dotdot@gmail.com, why you here ?"
        res = dtea.solve(text)
        self.assertEqual(res, "dotdot@gmail.com")

    def test_a4952_at_gmail_com_should_be_detected(self):
        text = "hello a4952@gmail.com, why you here ?"
        res = dtea.solve(text)
        self.assertEqual(res, "a4952@gmail.com")

    def test_a4952_botbot_at_gmail_should_be_detected(self):
        text = "hello botbot@gmail.com a4952@gmail.com, why you here ?"
        res = dtea.solve(text)
        self.assertEqual(res, "a4952@gmail.com;botbot@gmail.com")

    def test_a_bcd_at_gmail_should_be_detected(self):
        text = "hello a_bcd@gmail.com, why you here ?"
        res = dtea.solve(text)
        self.assertEqual(res, "a_bcd@gmail.com")

    def test_a_dot_bcd_at_gmail_should_be_detected(self):
        text = "hello a.bcd@gmail.com, why you here ?"
        res = dtea.solve(text)
        self.assertEqual(res, "a.bcd@gmail.com")

    def test_double_dot_domain_should_be_detected(self):
        text = "hello web.thehindu@thehindu.co.in, why you here ?"
        res = dtea.solve(text)
        self.assertEqual(res, "web.thehindu@thehindu.co.in")
