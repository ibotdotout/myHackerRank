# https://www.hackerrank.com/challenges/chocolate-feast


def get_chocolates(n, c, m):
    warppers = n / c
    total = warppers
    while warppers / m:
        chocolate = warppers / m
        warppers = warppers % m + chocolate
        total += chocolate
    return total

if __name__ == "__main__":
    T = input()
    for i in range(T):
        n, c, m = map(int, raw_input().split())
        print get_chocolates(n, c, m)
