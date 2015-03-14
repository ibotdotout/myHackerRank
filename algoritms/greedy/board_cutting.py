# https://www.hackerrank.com/challenges/board-cutting


def solve(y, x):
    total_cost = 0
    n = [1, 1]
    cost = [(i, 0) for i in x] + [(i, 1) for i in y]
    for v, d in sorted(cost, reverse=True):
        total_cost += v * n[1-d]
        total_cost %= (10 ** 9 + 7)
        n[d] += 1
    return total_cost


if __name__ == '__main__':
    t = input()
    for _ in range(t):
        _, _ = map(int, raw_input().split())
        y = map(int, raw_input().split())
        x = map(int, raw_input().split())
        print solve(y, x)
