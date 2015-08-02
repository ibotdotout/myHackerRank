# https://www.hackerrank.com/challenges/utopian-identification-number

import re


def solve(text):
    return True if re.match("^[a-z]{0,3}[0-9]{2,8}[A-Z]{3,}$", text) else False


if __name__ == '__main__':
    n = input()
    for i in range(n):
        text = raw_input()
        print "VALID" if solve(text) else "INVALID"
