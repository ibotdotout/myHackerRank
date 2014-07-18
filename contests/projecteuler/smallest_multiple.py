# https://www.hackerrank.com/contests/projecteuler/challenges/euler005


def factors(memo, n):
    factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            if memo[n / i]:
                i = (n / i)
                factors.extend(memo[i])
            else:
                factors.append(i)
            n /= i
        i += 1
        if i ** 2 > n:
            if n > 1:
                factors.append(n)
                break
    return factors


def generate_memo():
    memo = [[] for i in xrange(41)]
    for i in xrange(2, 41):
        memo[i] = factors(memo, i)
    return memo


def solve(memo, n):
    product = []
    for i in xrange(2, n + 1):
        for factor in set(memo[i]):
            product.extend([factor]*(memo[i].count(factor) -
                           product.count(factor)))
    result = 1
    for i in product:
        result *= i
    return result


if __name__ == '__main__':
    memo = generate_memo()
    t = input()
    for i in xrange(t):
        n = input()
        print solve(memo, n)
