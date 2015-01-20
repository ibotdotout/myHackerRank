# https://www.hackerrank.com/challenges/unbounded-knapsack


def solve(l, max_price):
    # knapsack unbounded
    k = [0]
    for i in range(1, max_price+1):
        price = [k[i-v] + v for v in l if i >= v]
        k.append(max(price) if price else k[-1])
    return k[-1]


if __name__ == '__main__':
    t = input()
    for _ in range(t):
        _, k = map(int, raw_input().split())
        l = map(int, raw_input().split())
        print solve(l, k)
