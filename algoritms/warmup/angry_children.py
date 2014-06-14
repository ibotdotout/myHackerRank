# https://www.hackerrank.com/challenges/angry-children


def range_diff(l, k):
    l.sort()
    results = [l[i + k - 1] - l[i] for i in range(len(l) - k)]
    return min(results)

if __name__ == "__main__":
    N = input()
    k = input()
    l = [input() for i in range(N)]
    print range_diff(l, k)
