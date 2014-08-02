# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter

import unittest
import valid_list_of_email_address_with_filter as valie_email


class ValieListOfEmailAddressWithFilterTest(unittest.TestCase):
    def test_sample_case(self):
        emails = ['lara@hackerrank.com', 'brian-23@hackerrank.com',
                  'britts_54@hackerrank.com']
        expected = ['brian-23@hackerrank.com', 'britts_54@hackerrank.com',
                    'lara@hackerrank.com']
        result = valie_email.filter_email(emails)
        self.assertEqual(expected, result)

    def test_sample_case2(self):
        emails = ['x', 'lara@hackerrank.com', 'brian-23@hackerrank.com',
                  'britts_54@hackerrank.com']
        expected = ['brian-23@hackerrank.com', 'britts_54@hackerrank.com',
                    'lara@hackerrank.com']
        result = valie_email.filter_email(emails)
        self.assertEqual(expected, result)

    def test_case_5(self):
        emails = ["itsme@gmail", '@something', "@something.com",
                  "@something.co1", 'sone.com']
        expected = []
        result = valie_email.filter_email(emails)
        self.assertEqual(expected, result)
