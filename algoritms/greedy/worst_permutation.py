# https://www.hackerrank.com/challenges/worst-permutation


def solve(l, k):
    n = len(l)
    indexs = [0 for _ in range(n+1)]
    for i in range(len(l)):
        indexs[l[i]] = i
    i = 0
    while k and i < n:
        if l[i] != n-i:
            k -= 1
            idx = indexs[n-i]
            l[i], l[idx] = l[idx], l[i]
            indexs[l[i]], indexs[l[idx]] = indexs[l[idx]], indexs[l[i]]
        i += 1
    return l


if __name__ == '__main__':
    _, k = map(int, raw_input().split())
    l = map(int, raw_input().split())
    print " ".join(map(str, solve(l, k)))
