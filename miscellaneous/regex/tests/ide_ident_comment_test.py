# https://www.hackerrank.com/challenges/ide-identifying-comments

import ide_ident_comment as iic
import unittest


class IDEIdentCommentTest(unittest.TestCase):

    def test_single_line_coment(self):
        text = "x = 1; // a single line comment after code"
        res = iic.solve(text)
        self.assertEqual(res, ["// a single line comment after code"])

    def test_single_line_coment_in_multi_line(self):
        text = "x = 1; // a single line comment after code\n" \
               "x = 2;"
        res = iic.solve(text)
        self.assertEqual(res, ["// a single line comment after code"])

    def test_multi_line_coment_in_multi_line(self):
        text = "/*This is a program to calculate area of a circle after\n" \
               "         getting the radius as input from the user*/\n" \
               "#include<stdio.h>"
        res = iic.solve(text)
        ans = "/*This is a program to calculate area of a circle after\n" \
              "getting the radius as input from the user*/"
        self.assertEqual(res, [ans])
