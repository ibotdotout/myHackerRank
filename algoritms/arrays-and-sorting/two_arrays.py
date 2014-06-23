# https://www.hackerrank.com/challenges/two-arrays


def more_than_k(k, a, b):
    a.sort()
    b = sorted(b, reverse=True)
    result = [i + j >= k for (i, j) in zip(a, b)]
    return all(result)

if __name__ == "__main__":
    t = input()
    for i in range(t):
        n, k = map(int, raw_input().split())
        a = map(int, raw_input().split())
        b = map(int, raw_input().split())
        if more_than_k(k, a, b):
            print("YES")
        else:
            print("NO")
