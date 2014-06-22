# https://www.hackerrank.com/challenges/mark-and-toys


def max_toys(prices, rupees):
    answer = 0
    total_price = 0
    for i in sorted(prices):
        if total_price + i <= rupees:
            answer += 1
            total_price += i
        else:
            break
    return answer

if __name__ == '__main__':
    n, k = map(int, raw_input().split())
    prices = map(int, raw_input().split())
    print max_toys(prices, k)
