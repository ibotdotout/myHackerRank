# https://www.hackerrank.com/challenges/detect-the-email-addresses

import re


def solve(text):
    regex = "(?i)[\w\._]+?@[\w\.]+\.\w+"
    return ";".join(sorted(set(re.findall(regex, text))))

if __name__ == "__main__":
    n = input()
    text = " ".join([raw_input() for i in range(n)])
    print solve(text)
