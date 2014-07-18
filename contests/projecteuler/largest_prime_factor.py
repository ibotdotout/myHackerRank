# https://www.hackerrank.com/contests/projecteuler/challenges/euler003


def solve(n):
    factors = []
    i = 2
    while n > 1:
        while n % i == 0:
            factors.append(i)
            n /= i
        i += 1
        if i ** 2 > n:
            if n > 1:
                factors.append(n)
                break
    return max(factors)

if __name__ == '__main__':
    t = input()
    for i in range(t):
        n = input()
        print solve(n)
