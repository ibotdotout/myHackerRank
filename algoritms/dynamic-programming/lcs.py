# https://www.hackerrank.com/challenges/dynamic-programming-classics-the-longest-common-subsequence


def solve(a, b):
    memo = lcs(a, b)
    return backtrack(memo, a, b)


def backtrack(memo, a, b):
    i, j = len(a), len(b)
    result = []
    while i >= 1 and j >= 1:
        if a[i-1] == b[j-1]:
            result.append(a[i-1])
            j -= 1
            i -= 1
        else:
            if memo[i][j-1] > memo[i-1][j]:
                j -= 1
            else:
                i -= 1
    return result[::-1]


def lcs(a, b):
    w, h = len(a) + 1, len(b) + 1
    memo = [[0 for _ in range(h)] for _ in range(w)]
    for i in range(1, w):
        for j in range(1, h):
            if a[i-1] == b[j-1]:
                memo[i][j] = memo[i-1][j-1] + 1
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])
    return memo


if __name__ == "__main__":
    _ = raw_input()
    a = [int(i) for i in raw_input().split()]
    b = [int(i) for i in raw_input().split()]
    print " ".join([str(x) for x in solve(a, b)])
