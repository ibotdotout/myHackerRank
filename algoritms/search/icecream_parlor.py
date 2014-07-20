# https://www.hackerrank.com/challenges/icecream-parlor


def solve(m, n, c):
    for idx, val in enumerate(c):
        if m - val in c[idx + 1:]:
            return [idx + 1, idx + 1 + c[idx + 1:].index(m - val) + 1]

if __name__ == '__main__':
    t = input()
    for i in xrange(t):
        m = input()
        n = input()
        c = map(int, raw_input().split())
        print ' '.join(map(str, solve(m, n, c)))
