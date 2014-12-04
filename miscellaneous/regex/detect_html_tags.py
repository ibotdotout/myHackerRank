# https://www.hackerrank.com/challenges/detect-html-tags

import re


def solve(text):
    return ";".join(sorted(set(re.findall("<\s*?(\w+)\s*?.*?>", text))))

if __name__ == "__main__":
    n = input()
    text = "".join([raw_input() for i in range(n)])
    print solve(text)
