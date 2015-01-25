# https://www.hackerrank.com/challenges/fibonacci-modified


def solve(a, b, n):
    res = [a, b]
    for i in range(n - 2):
        res.append(res[-1]**2 + res[-2])
    return res[n-1]


if __name__ == '__main__':
    a, b, n = map(int, raw_input().split())
    print solve(a, b, n)
