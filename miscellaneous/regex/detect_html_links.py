# https://www.hackerrank.com/challenges/detect-html-links

import re


def solve(text):
    regex = '(?:<\s*a\s*href=")([^"]+?)(?:".*?>)(?:<.+?>)*\s*(.*?)\s*(?=</)'
    return [",".join(i) for i in re.findall(regex, text)]

if __name__ == '__main__':
    n = input()
    text = "".join([raw_input() for _ in range(n)])
    print("\n".join(solve(text)))
