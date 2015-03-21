# https://www.hackerrank.com/challenges/picking-cards


def solve(l):
    ll = sorted(l)
    ways = 1
    mod = 10 ** 9 + 7
    for i in range(len(l), 0, -1):
        ways *= i - ll[i-1]
        ways %= mod
    return ways


if __name__ == '__main__':
    t = input()
    for _ in range(t):
        _ = input()
        l = map(int, raw_input().split())
        print solve(l)
