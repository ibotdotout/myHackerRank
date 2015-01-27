# https://www.hackerrank.com/challenges/restaurant


def solve(l, b):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    return (l * b) / (gcd(l, b) ** 2)

if __name__ == '__main__':
    t = input()
    for _ in range(t):
        l, b = map(int, raw_input().split())
        print solve(l, b)
