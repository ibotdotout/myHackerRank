# https://www.hackerrank.com/challenges/pairs


def has(l, v):
    from bisect import bisect_left
    i = bisect_left(l, v)
    if i != len(l) and l[i] == v:
        return True
    return None


def solve(l, k):
    l.sort()
    return len([v for v in l if has(l, v+k)])

if __name__ == '__main__':
    n, k = map(int, raw_input().split())
    l = map(int, raw_input().split())
    print solve(l, k)
