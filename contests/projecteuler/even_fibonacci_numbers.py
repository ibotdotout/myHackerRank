# https://www.hackerrank.com/contests/projecteuler/challenges/euler002


def solve(n):
    result = 0
    a, b = 1, 1
    while b < n:
        if b % 2 == 0:
            result += b
        a, b = b, a+b
    return result

if __name__ == "__main__":
    t = input()
    for i in xrange(t):
        n = input()
        print solve(n)
