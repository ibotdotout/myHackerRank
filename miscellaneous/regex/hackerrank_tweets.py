# https://www.hackerrank.com/challenges/hackerrank-tweets

import re


def solve(text):
    res = re.findall("hackerrank", text.lower())
    return len(res)

if __name__ == '__main__':
    n = input()
    text = ""
    for i in range(n):
        text += raw_input()
    print solve(text)
