# https://www.hackerrank.com/challenges/programming-language-detection

import re


def is_c(text):
    return True if re.search('^#include\s?(<|")\w+\.\w+(>|")', text) else False


def is_java(text):
    return True if re.search('import [\w.]+\*?;', text) else False


def solve(text):
    if is_c(text):
        return "C"
    elif is_java(text):
        return "Java"
    else:
        return "Python"

if __name__ == "__main__":
    import sys
    text = sys.stdin.read()
