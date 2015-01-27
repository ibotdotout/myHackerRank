# https://www.hackerrank.com/challenges/reverse-game


def solve(a, b):
    # n 0 n-1 1 n-2 2 n-3
    # 0 1  2  3  4  5  6
    # 6, 3 --> (6-1-3) * 2 = 4
    # 5, 0 --> (0 *2 ) + 1 = 1
    return b * 2 + 1 if b < a/2 else (a-1-b) * 2

if __name__ == '__main__':
    t = input()
    for _ in range(t):
        a, b = map(int, raw_input().split())
        print solve(a, b)
