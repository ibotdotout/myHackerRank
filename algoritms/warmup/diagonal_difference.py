# https://www.hackerrank.com/challenges/diagonal-difference


def solve(arr, n):
    p = sum(arr[::n+1])
    s = sum(arr[n-1:-n+1:n-1])
    return abs(p - s)

if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for _ in range(n) for i in input().split(' ')]
    print(solve(arr, n))
