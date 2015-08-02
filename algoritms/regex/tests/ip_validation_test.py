# https://www.hackerrank.com/challenges/ip-address-validation

import ip_validation as ipv
import unittest


class IPValidationTest(unittest.TestCase):

    def test_ipv6_with1pos_should_be_True(self):
        text = "1050:1000:1000:a000:5:600:300c:326b"
        res = ipv.is_ipv6(text)
        self.assertEqual(True, res)

    def test_ipv4_should_be_True(self):
        text = "121.18.19.20"
        res = ipv.is_ipv4(text)
        self.assertEqual(True, res)

    def test_ipv4_249_should_be_True(self):
        text = "249.18.19.20"
        res = ipv.is_ipv4(text)
        self.assertEqual(True, res)

    def test_ipv6_should_be_True(self):
        text = "2001:0db8:0000:0000:0000:ff00:0042:8329"
        res = ipv.is_ipv6(text)
        self.assertEqual(True, res)

    def test_non_ip_should_be_neither(self):
        text = "This line has junk text."
        res = ipv.is_ipv6(text)
        self.assertEqual(False, res)
        res = ipv.is_ipv4(text)
        self.assertEqual(False, res)

    def test_like_ipv4_should_be_neither(self):
        text = "253.214.111.564"
        res = ipv.is_ipv6(text)
        self.assertEqual(False, res)
        res = ipv.is_ipv4(text)
        self.assertEqual(False, res)
