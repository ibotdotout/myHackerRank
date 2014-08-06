# https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers

import unittest
import class1


class Class1Test(unittest.TestCase):
    def test_sample_case(self):
        complex_num = [[2, 1], [5, 6]]
        expected = ["7.00 + 7.00i", "-3.00 - 5.00i", "4.00 + 17.00i",
                    "0.26 - 0.11i", "2.24", "7.81"]
        result = class1.solve(*complex_num)
        self.assertEqual(expected, result)

    def test_case4(self):
        complex_num = [[0, 9], [9, 0]]
        expected = ["9.00 + 9.00i", "-9.00 + 9.00i", "81.00i",
                    "1.00i", "9.00", "9.00"]
        result = class1.solve(*complex_num)
        self.assertEqual(expected, result)
