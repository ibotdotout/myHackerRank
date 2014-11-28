# https://www.hackerrank.com/challenges/detecting-valid-latitude-and-longitude

import re


def solve(text):
    pattern = "\+?\-?([1-9]\d*\.\d+|[1-9]\d*)"
    res = re.match("\({0}, {0}\)".format(pattern), text)
    if res:
        if float(res.group(1)) <= 90 and float(res.group(2)) <= 180:
            return True
    return False

if __name__ == "__main__":
    n = input()
    for i in range(n):
        text = raw_input()
        print "Valid" if solve(text) else "Invalid"
