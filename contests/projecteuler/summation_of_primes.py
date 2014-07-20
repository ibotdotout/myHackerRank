# https://www.hackerrank.com/contests/projecteuler/challenges/euler010
import bisect

primes = [2, 3]
ans = [2, 5]
memo = {2: 0, 3: 0}


def solve(n):
    global primes
    global ans
    global memo
    if n > primes[-1]:
        for i in xrange(primes[-1], n+1, 2):
            for prime in primes:
                if i % prime == 0:
                    break
                if prime ** 2 > i:
                    if i not in memo:
                        memo[i] = 0
                        primes.append(i)
                        ans.append(i + ans[-1])
                    break
    idx = bisect.bisect_right(primes, n)
    return ans[idx-1]

if __name__ == '__main__':
    t = input()
    for i in xrange(t):
        print solve(input())
