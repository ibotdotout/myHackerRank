# https://www.hackerrank.com/challenges/power-of-large-numbers

# apply from
# https://krishnanceg.wordpress.com/2013/12/01/hackerrank-nov-challenge-power-of-large-numbers/


def modexp(x, y, mod):
    """ return x**y % mod """
    if y == 0:
        return 1
    zz = modexp(x, y/2, mod) ** 2
    if y % 2:
        zz *= x
    return zz % mod


def algor_solve(x, y):
    """ using number-theroy """
    mod = 10**9 + 7
    x = x % mod
    y = y % (mod - 1)
    return modexp(x, y, mod)


def solve(x, y):
    """ using efficient build-in pow(x, y, z) ~= (x ** y) % z """
    mod = 10**9 + 7
    return pow(x, y, mod)

if __name__ == '__main__':
    import sys
    t = int(sys.stdin.readline())
    for _ in range(t):
        x, y = map(int, sys.stdin.readline().split())
        print solve(x, y)
