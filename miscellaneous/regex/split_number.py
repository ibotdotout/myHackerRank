# https://www.hackerrank.com/challenges/split-number

import re


def solve(text):
    res = re.match("(\d{1,3}).(\d{1,3}).(\d{4,10})", text)
    return (res.group(1), res.group(2), res.group(3))

if __name__ == "__main__":
    n = input()
    for i in range(n):
        text = raw_input()
        print \
            "CountryCode={0},LocalAreaCode={1},Number={2}".format(*solve(text))
