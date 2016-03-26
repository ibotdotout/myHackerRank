# https://www.hackerrank.com/challenges/detect-the-domain-name

import unittest
import detect_the_domain_name as dtdn


class DetectTheDomainNameTest(unittest.TestCase):

    def test_https_www_hrank_com_shoudl_be_found(self):
        text = "https://www.hackerrank.com"
        res = dtdn.solve(text)
        self.assertEqual(res, ["hackerrank.com"])

    def test_https_www_hrank_com_two_time_shoudl_be_founds(self):
        text = "https://www.hackerrank.com/" * 2
        res = dtdn.solve(text)
        self.assertEqual(res, ["hackerrank.com"])

    def test_https_ww2_hrank_co_shoudl_be_foundm(self):
        text = "https://ww2.hackerrank.com"
        res = dtdn.solve(text)
        self.assertEqual(res, ["hackerrank.com"])

    def test_https_abc_xyz_com_https_www_hrank_com_shoudl_be_found(self):
        text = "https://ww2.hackerrank.com https://abc.xyz.com/jobs"
        res = dtdn.solve(text)
        self.assertEqual(res, ["abc.xyz.com", "hackerrank.com"])

    def test_http_abc_xyz_com_shoudl_be_found(self):
        text = "http://abc.xyz.com/jobs"
        res = dtdn.solve(text)
        self.assertEqual(res, ["abc.xyz.com"])

    def test_http_abc_xyz_com___shoudl_be_found(self):
        text = "http://abc.xyz.com__/jobs"
        res = dtdn.solve(text)
        self.assertEqual(res, ["abc.xyz.com"])

    def test_abc_ddd_jpg_should_be_not_found(self):
        text = "abc.xyz.jpg"
        res = dtdn.solve(text)
        self.assertEqual(res, [])

    def test_metric_ind_rediff_com_should_be_found(self):
        text = "https://metric.ind.rediff.com"
        res = dtdn.solve(text)
        self.assertEqual(res, ["metric.ind.rediff.com"])

    def test_boxtv_com(self):
        text = "https://boxtv.com"
        res = dtdn.solve(text)
        self.assertEqual(res, ["boxtv.com"])

    def test_coursera_placement_resumes_s3_amazonaws_com_should_be_found(self):
        text = "http://coursera-placement-resumes.s3.amazonaws.com"
        res = dtdn.solve(text)
        self.assertEqual(res, ["coursera-placement-resumes.s3.amazonaws.com"])
