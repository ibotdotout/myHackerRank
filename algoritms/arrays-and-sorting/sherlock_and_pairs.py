# https://www.hackerrank.com/challenges/sherlock-and-pairs

import collections


def solve(l):
    count = collections.Counter(l)
    return sum([(i-1)*i for i in count.values()])

if __name__ == '__main__':
    t = input()
    for _ in range(t):
        _ = input()
        l = [int(i) for i in raw_input().split()]
        print solve(l)
