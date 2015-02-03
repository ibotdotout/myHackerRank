# https://www.hackerrank.com/challenges/john-and-gcd-list

import fractions


def solve(l):
    lcm = lambda a, b: abs(a * b) // fractions.gcd(a, b)
    return [lcm(a, b) for a, b in zip([1] + l, l + [1])]

if __name__ == '__main__':
    t = input()
    for _ in range(t):
        _ = input()
        l = map(int, raw_input().split())
        print " ".join(map(str, solve(l)))
