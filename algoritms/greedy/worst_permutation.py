# https://www.hackerrank.com/challenges/worst-permutation


def solve(l, k):
    n = min(k, len(l))
    max_l = sorted(l, reverse=True)
    i = 0
    while n and i < len(l):
        idx = l.index(max_l[i])
        if i != idx:
            l[i], l[idx] = l[idx], l[i]
            n -= 1
        i += 1
    return l


if __name__ == '__main__':
    _, k = map(int, raw_input().split())
    l = map(int, raw_input().split())
    print " ".join(map(str, solve(l, k)))
