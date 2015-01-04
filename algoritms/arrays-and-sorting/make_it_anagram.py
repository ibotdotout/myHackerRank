# https://www.hackerrank.com/challenges/make-it-anagram
from collections import Counter


def solve(a, b):
    chars_a = Counter(a)
    chars_b = Counter(b)
    return sum([abs(chars_a[k] - chars_b[k]) for k in set(a) | set(b)])

if __name__ == '__main__':
    a = raw_input()
    b = raw_input()
    print solve(a, b)
