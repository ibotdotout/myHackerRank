# https://www.hackerrank.com/challenges/finding-the-percentage

import unittest
import finding_the_percentage as ftp


class FindingThePercentageTest(unittest.TestCase):
    def test_case1_should_get_56dot00(self):
        students = {"Krishna": [67, 68, 69], "Arjun": [70, 98, 63],
                    "Malika": [52, 56, 60]}
        expteced_result = 56
        result = ftp.get_percentage_of(students, "Malika")
        self.assertEqual(float, type(result))
        self.assertAlmostEqual(expteced_result, result)

    def test_case2_should_get_26dot50(self):
        students = {"Harsh": [25, 26.5, 28], "Anurag": [26, 28, 30]}
        expteced_result = 26.50
        result = ftp.get_percentage_of(students, "Harsh")
        self.assertEqual(float, type(result))
        self.assertAlmostEqual(expteced_result, result)
