# https://www.hackerrank.com/challenges/handshake


def solve(n):
    return (n-1)*n/2


if __name__ == "__main__":
    t = input()
    for _ in range(t):
        n = input()
        print solve(n)
