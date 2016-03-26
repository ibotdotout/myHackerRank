# https://www.hackerrank.com/challenges/html-attributes

import re
import sys
import collections as cols


def solve(text):
    res = re.findall(r'(?s)<\w+.*?>', text)
    l = [re.findall(r'(?s)<?(\w+)(?:=[\'"].*?[\'"])?', str(i)) for i in res]
    s = cols.defaultdict(set)
    for i in l:
        s[i[0]] |= set(i[1:])
    return sorted([k+":"+",".join(sorted(v)) for k, v in s.items()])

if __name__ == '__main__':
    l = input()
    text = "".join([sys.stdin.readline() for i in range(l)])
    print "\n".join(solve(text))
