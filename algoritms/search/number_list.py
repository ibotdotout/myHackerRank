# https://www.hackerrank.com/challenges/number-list


def solve(l, k):
    n = len(l)
    result, p = 0, 0
    for i, v in enumerate(l):
        if v > k:
            result += (i+1-p)*(n-i)
            p = (i+1)
    return result


if __name__ == '__main__':
    t = input()
    for _ in range(t):
        _, k = map(int, raw_input().split())
        l = map(int, raw_input().split())
        print solve(l, k)
