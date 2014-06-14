# https://www.hackerrank.com/challenges/sherlock-and-the-beast
"""
study this code
it's wonderful
    https://www.hackerrank.com/technic
    https://www.hackerrank.com/rest/contests/sep13/challenges/sherlock-and-the-beast/hackers/technic/download_solution
"""


def solve(n):
    # n = 5x + 3y
    f = lambda n, x: (n-5*x)/3
    x, y = 0, 0
    while (n-5*x) % 3 != 0 and y >= 0:
        x += 1
        y = f(n, x)
    y = f(n, x)
    if y >= 0:
        return "555"*y + "33333"*x
    else:
        return "-1"


if __name__ == "__main__":
    for i in range(input()):
        print solve(input())
