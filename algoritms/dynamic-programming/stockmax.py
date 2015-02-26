# https://www.hackerrank.com/challenges/stockmax
# http://stackoverflow.com/questions/9514191/maximizing-profit-for-given-stock-quotes


def solve(l):
    profit, maximum = 0, 0
    for price in reversed(l):
        if maximum < price:
            maximum = price
        profit += maximum - price
    return profit


if __name__ == '__main__':
    t = input()
    for _ in range(t):
        _ = input()
        l = map(int, raw_input().split())
        print solve(l)
