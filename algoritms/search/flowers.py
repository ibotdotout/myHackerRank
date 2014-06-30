# https://www.hackerrank.com/challenges/flowers


def buy_flowers(n, k, flowers_cost):
    prices = 0
    flowers_cost.sort(reverse=True)
    x = 0
    while k*x <= n:
        prices += sum(map(lambda c: c*(x+1), flowers_cost[x*k: (x+1)*k]))
        x += 1
    return prices

if __name__ == '__main__':
    n, k = map(int, raw_input().split())
    flowers_cost = map(int, raw_input().split())
    print buy_flowers(n, k, flowers_cost)
