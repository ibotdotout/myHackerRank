# https://www.hackerrank.com/challenges/find-hackerrank

import re


def solve(text):
    hrank = "hackerrank"
    is_start = re.search("^"+hrank, text)
    is_end = re.search(hrank+"$", text)
    if is_start and is_end:
        return 0
    elif is_start:
        return 1
    elif is_end:
        return 2
    else:
        return -1

if __name__ == '__main__':
    n = input()
    for i in range(n):
        text = raw_input()
        print solve(text)
