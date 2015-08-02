# https://www.hackerrank.com/challenges/map-and-lambda-expression

import unittest
import map_and_lambda as mal


class MapAndLambdaTest(unittest.TestCase):
    def test_sample_case(self):
        given = 5
        exepcted = [0, 1, 1, 8, 27]
        result = mal.cube_fibo(given)
        self.assertEqual(exepcted, result)

    def test_sample_case2(self):
        given = 6
        exepcted = [0, 1, 1, 8, 27, 125]
        result = mal.cube_fibo(given)
        self.assertEqual(exepcted, result)

    def test_sample_case3(self):
        given = 1
        exepcted = [0]
        result = mal.cube_fibo(given)
        self.assertEqual(exepcted, result)

    def test_sample_case4(self):
        given = 0
        exepcted = []
        result = mal.cube_fibo(given)
        self.assertEqual(exepcted, result)
