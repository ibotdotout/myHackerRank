# https://www.hackerrank.com/challenges/alien-username

import re


def solve(text):
    return True if re.match("^[_\.]\d+[a-zA-Z]*_?$", text) else False

if __name__ == "__main__":
    n = input()
    for i in range(n):
        text = raw_input()
        print "VALID" if solve(text) else "INVALID"
