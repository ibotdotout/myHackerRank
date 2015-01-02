# https://www.hackerrank.com/challenges/sherlock-and-watson


def solve(l, k):
    k = k % len(l)
    return l[-k:]+l[:-k]

if __name__ == '__main__':
    _, k, q = [int(i) for i in raw_input().split()]
    l = [int(i) for i in raw_input().split()]
    res = solve(l, k)
    for _ in range(q):
        print res[input()]
