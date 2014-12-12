# https://www.hackerrank.com/challenges/ide-identifying-comments

import re


def solve(text):
    regex = r"(?s)(//.+?(?=\n|$)|/\*.*?\*/)"
    return [re.sub(r"\n\s+", "\n", i) for i in re.findall(regex, text)]

if __name__ == "__main__":
    import sys
    text = sys.stdin.read()
    res = solve(text)
    print "\n".join(solve(text))
