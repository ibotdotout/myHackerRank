# https://www.hackerrank.com/challenges/manasa-loves-maths

import itertools


def solve(n):
    # any number is divisible by 8 when the last 3 digits are divisible by 8
    p = itertools.permutations(str(n), min(len(str(n)), 3))
    for i in p:
        val = int("".join(i))
        if val % 8 == 0:
            return True
    return False

if __name__ == '__main__':
    t = input()
    for _ in range(t):
        n = input()
        print 'YES' if solve(n) else 'NO'
