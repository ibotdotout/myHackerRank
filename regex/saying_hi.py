# https://www.hackerrank.com/challenges/saying-hi

import re


def solve(text):
    return True if re.match("(?i)^Hi\s[^dD].*", text) else False


if __name__ == "__main__":
    n = input()
    for i in range(n):
        text = raw_input()
        if solve(text):
            print text
