# https://www.hackerrank.com/challenges/number-list


def solve(l, k):
    n = len(l)
    result = 0
    for i in range(n):
        m = l[i]
        for v in l[i:]:
            if v > m:
                m = v
            if m > k:
                result += 1
    return result


if __name__ == '__main__':
    t = input()
    for _ in range(t):
        _, k = map(int, raw_input().split())
        l = map(int, raw_input().split())
        print solve(l, k)
