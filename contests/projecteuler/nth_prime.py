# https://www.hackerrank.com/contests/projecteuler/challenges/euler007

# 10001st prime ~= 105000
sieve = [True] * 105000
sieve[0] = False
sieve[1] = False

primes = []


def generate():
    """
        Gereate primes with Sieve algorithm
        http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """
    global primes
    zeros = [False] * (len(sieve) / 2)
    for i in xrange(2, int(len(sieve) ** 0.5) + 1):
        if sieve[i]:
            sieve[i*i::i] = zeros[:((len(sieve)-1)/i) - i + 1]
    primes = [idx for idx, i in enumerate(sieve) if i]


def solve(n):
    return primes[n-1]

if __name__ == '__main__':
    generate()
    for i in xrange(input()):
        print solve(input())
