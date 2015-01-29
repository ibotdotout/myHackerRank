# https://www.hackerrank.com/challenges/closest-number


def solve(l):
    a, b, x = l
    ab = a ** b
    v = ab // x
    ans = v * x if ab % x <= x / 2 else (v + 1) * x
    return int(ans)

if __name__ == '__main__':
    t = input()
    for _ in range(t):
        l = map(int, raw_input().split())
        print solve(l)
