# https://www.hackerrank.com/challenges/building-a-list


import itertools


def solve(w):
    results = []
    n = len(w)
    for i in range(1, n+1):
        results += map(lambda x: "".join(x), itertools.combinations(w, i))
    return sorted(results)


if __name__ == '__main__':
    t = input()
    for _ in range(t):
        _ = input()
        w = raw_input()
        print "\n".join(solve(w))
