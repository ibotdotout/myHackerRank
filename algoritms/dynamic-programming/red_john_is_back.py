# https://www.hackerrank.com/challenges/red-john-is-back

import bisect

primes = [2, 3]
memo = {2: 0, 3: 0}


def solve(n):
    global primes
    global ans
    global memo
    n = arrage_brick(n)
    if n > primes[-1]:
        for i in xrange(primes[-1], n+1, 2):
            for prime in primes:
                if i % prime == 0:
                    break
                if prime ** 2 > i:
                    if i not in memo:
                        memo[i] = 0
                        primes.append(i)
                    break
    idx = bisect.bisect_right(primes, n)
    return idx


def _arrage_brick(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return _arrage_brick(n-1) + _arrage_brick(n-4)


def arrage_brick(n):
    if n > 3:
        return _arrage_brick(n)
    else:
        return 0

if __name__ == '__main__':
    t = input()
    for i in xrange(t):
        print solve(input())
