# https://www.hackerrank.com/challenges/sherlock-and-squares


def solve(a, b):
    return int(b**0.5) - int((a-1)**0.5)

if __name__ == '__main__':
    t = input()
    for _ in range(t):
        a, b = [int(i) for i in raw_input().split()]
        print solve(a, b)
