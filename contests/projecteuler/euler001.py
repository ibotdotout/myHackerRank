# https://www.hackerrank.com/contests/projecteuler/challenges/euler001


def solve(n):
    total = 0
    for i in [3, 5]:
        nn = (n - 1) / i
        total += i * nn * (nn + 1) / 2
    nn = (n - 1) / 15
    total -= 15 * nn * (nn + 1) / 2
    return total

if __name__ == '__main__':
    t = input()
    for i in range(t):
        n = input()
        print solve(n)
