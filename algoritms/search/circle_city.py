# https://www.hackerrank.com/challenges/circle-city


def solve(r, k):
    possible_y = [(r-x**2)**0.5 for x in range(1, int(r**0.5)+1)]
    integer_y = [y for y in possible_y if y == int(y)]
    return False if len(integer_y)*4 > k else True

if __name__ == '__main__':
    t = input()
    for _ in range(t):
        r, k = map(int, raw_input().split())
        print "possible" if solve(r, k) else "impossible"
