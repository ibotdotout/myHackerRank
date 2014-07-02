# https://www.hackerrank.com/challenges/encryption

import unittest
import encryption as ecp


class EncryptionTest(unittest.TestCase):
    def test_case1_should_get_hae_and_via_ecy(self):
        w = "haveaniceday"
        expected_result = "hae and via ecy"
        self.helper_assert(w, expected_result)

    def test_case2_should_get_fto_ehg_ee_dd(self):
        w = "feedthedog"
        expected_result = "fto ehg ee dd"
        self.helper_assert(w, expected_result)

    def test_case3_should_get_clu_hlt_io(self):
        w = "chillout"
        expected_result = "clu hlt io"
        self.helper_assert(w, expected_result)

    def helper_assert(self, w, expected_result):
        result = ecp.encode(w)
        self.assertEqual(expected_result, result)
