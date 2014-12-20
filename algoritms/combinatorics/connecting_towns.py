# https://www.hackerrank.com/challenges/connecting-towns


def solve(l):
    res = 1
    for i in l:
        res = (res * i) % 1234567
    return res


if __name__ == "__main__":
    t = input()
    for _ in range(t):
        _ = input()
        l = [int(i) for i in raw_input().split()]
        print solve(l)
