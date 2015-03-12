# https://www.hackerrank.com/challenges/jim-and-the-orders


def solve(l):
    sent = sorted([(l[i] + l[i+1], i//2) for i in range(0, len(l), 2)])
    return [idx + 1 for v, idx in sent]


if __name__ == '__main__':
    n = input()
    l = []
    for _ in range(n):
        l += map(int, raw_input().split())
    print " ".join(map(str, solve(l)))
