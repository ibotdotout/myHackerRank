# https://www.hackerrank.com/challenges/find-substring

import re


def solve(text, word):
    return len(re.findall("[\w\d_]+"+word+"[\w\d_]+", text))


if __name__ == "__main__":
    n = input()
    text = " ".join([raw_input() for i in range(n)])
    t = input()
    for i in range(t):
        word = raw_input()
        print solve(text, word)
