# https://www.hackerrank.com/challenges/detect-html-links

import re


def solve(text):
    regex = '(?:<a\shref=")([^"]+?)(?:".*?>)(?:<.+?>)*(.*?)(?=</)'
    return [",".join([x.strip() for x in i]) for i in re.findall(regex, text)]

if __name__ == '__main__':
    n = input()
    text = "".join([raw_input() for _ in range(n)])
    print("\n".join(solve(text)))
