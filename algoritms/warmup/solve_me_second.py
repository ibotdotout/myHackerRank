# https://www.hackerrank.com/challenges/solve-me-second


def solve(a, b):
    return a+b


if __name__ == '__main__':
    t = input()
    for _ in range(t):
        a, b = tuple(int(i) for i in raw_input().split())
        print solve(a,b)
