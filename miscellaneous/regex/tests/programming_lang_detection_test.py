# https://www.hackerrank.com/challenges/programming-language-detection

import programming_lang_detection as pld
import unittest


class ProgrammingLangDetectionTest(unittest.TestCase):

    def test_java_code_should_be_java(self):
        text = "import java.io.*; " \
               "public class SquareNum { " \
               "public static void main(String args[]) " \
               "throws IOException " \
               "{ " \
               "System.out.println(\"This is a small Java Program!\"); " \
               "}} "
        res = pld.solve(text)
        self.assertEqual(res, "Java")

    def test_c_code_should_be_c(self):
        text = "#include<stdio.h>\n int main()"
        res = pld.solve(text)
        self.assertEqual(res, "C")

    def test_python_code_should_be_python(self):
        text = "def test_python_code_should_be_python(self):"
        res = pld.solve(text)
        self.assertEqual(res, "Python")
