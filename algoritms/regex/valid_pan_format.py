# https://www.hackerrank.com/challenges/valid-pan-format

import re


def solve(text):
    res = re.match("[A-Z]{5}\d{4}[A-Z]", text)
    return (res is not None)


if __name__ == '__main__':
    n = input()
    for i in range(n):
        text = raw_input()
        print "YES" if solve(text) else "NO"
