# https://www.hackerrank.com/challenges/detect-the-domain-name


import re


def solve(text):
    regex = r"(?:https?://(?:ww[w2]\.)?)([-a-z0-9\.]+\.[a-z0-9]+)"
    domains = re.findall(regex, text)
    return sorted(set(domains))

if __name__ == "__main__":
    n = input()
    text = "".join([raw_input() for _ in range(n)])
    print ";".join(solve(text))
