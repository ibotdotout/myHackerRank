# https://www.hackerrank.com/challenges/uk-and-us

import re


def solve(text, word):
    return len(re.findall(word[:-2]+"ze|"+word[:-2]+"se", text))


if __name__ == '__main__':
    n = input()
    text = " ".join([raw_input() for i in range(n)])
    t = input()
    for i in range(t):
        print solve(text, raw_input())
