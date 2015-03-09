# https://www.hackerrank.com/challenges/jim-and-the-jokes

import collections as cols


def base_n(v, n):
    value = 0
    i = 0
    while v != 0:
        c = v % 10
        if c >= n:
            return -1
        value += c * pow(n, i)
        i += 1
        v /= 10
    return value


def solve(l):
    dec = []
    jokes = 0
    for i in range(len(l)//2):
        a, b = l[2*i], l[2*i+1]
        dec.append(base_n(b, a))
    counter = cols.Counter(dec)
    for i, v in counter.items():
        if i > 0:
            jokes += v*(v-1)//2 if v > 0 else 0
    return jokes


if __name__ == '__main__':
    n = input()
    l = []
    for i in range(n):
        l += map(int, raw_input().split())
    print solve(l)
