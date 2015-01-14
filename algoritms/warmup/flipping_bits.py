# https://www.hackerrank.com/challenges/flipping-bits


def solve(a):
    # 2**32 = 4294967295
    return 4294967295 - a

if __name__ == '__main__':
    t = input()
    for _ in range(t):
        a = input()
        print solve(a)
