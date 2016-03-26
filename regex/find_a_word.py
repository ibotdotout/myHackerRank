# https://www.hackerrank.com/challenges/find-a-word

import re


def solve(text, word):
    return len(re.findall(r'\b'+word+r'\b', text))


if __name__ == "__main__":
    n = input()
    text = " ".join([raw_input() for i in range(n)])
    t = input()
    for i in range(t):
        print solve(text, raw_input())
