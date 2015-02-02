# https://www.hackerrank.com/challenges/equations

# apply from
# http://stackoverflow.com/questions/9469898/1-x-1-y-1-nfactorial
# http://code.antonio081014.com/2012/10/interviewstreet-equation.html


def generate_primes(n):
    """
        Gereate primes with Sieve algorithm
        http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """
    sieve = [False, False] + [True] * (n-1)
    zeros = [False] * (len(sieve) / 2)
    for i in xrange(2, int(len(sieve) ** 0.5) + 1):
        if sieve[i]:
            sieve[i*i::i] = zeros[:((len(sieve)-1)/i) - i + 1]
    return [idx for idx, i in enumerate(sieve) if i]


def get_pow(p, n):
    exp = 0
    while n != 0:
        exp += n / p
        n /= p
    return exp


def solve(n):
    m = 1000007
    primes = generate_primes(n)
    res = 1
    for p in primes:
        exp = get_pow(p, n)
        res = ((res % m) * (exp * 2 + 1) % m) % m
    return res

if __name__ == '__main__':
    n = input()
    print solve(n)
