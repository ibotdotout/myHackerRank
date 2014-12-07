# https://www.hackerrank.com/challenges/uk-and-us-2

import re


def solve(text, word):
    _w = word.lower().replace("our", "or")
    return len(re.findall("(?i)"+word+"(\W|$)|"+_w+"(\W|$)", text))


if __name__ == '__main__':
    n = input()
    text = " ".join([raw_input() for i in range(n)])
    t = input()
    for i in range(t):
        print solve(text, raw_input())
