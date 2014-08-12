# https://www.hackerrank.com/challenges/red-john-is-back

sieve = [1 for i in xrange(220000)]
sieve[0] = 0
sieve[1] = 0

brick = [1, 1, 1, 1]


def solve(n):
    return sieve[arrage_brick(n)]


def generate_primes():
    """
        Gereate primes with Sieve algorithm
        http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """
    zeros = [0] * (len(sieve) / 2)
    for i in xrange(2, int(len(sieve) ** 0.5) + 1):
        if sieve[i] != 0:
            sieve[i*i::i] = zeros[:((len(sieve)-1)/i) - i + 1]
    # Count how many primes is less equal than i
    for i in xrange(2, len(sieve)):
        sieve[i] += sieve[i-1]


def gernerate_arrage_brick():
    """ f(n) = f(n-1) + f(n-4) where f(0)=f(1)=f(2)=f(3)=1 """
    for i in xrange(4, 41):
        brick.append(brick[-1] + brick[-4])


def arrage_brick(n):
    return brick[n]

if __name__ == '__main__':
    gernerate_arrage_brick()
    generate_primes()
    t = input()
    for i in xrange(t):
        print solve(input())
