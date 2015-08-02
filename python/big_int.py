# https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes


def solve(a, b, c, d):
    return pow(a, b) + pow(c, d)

if __name__ == '__main__':
    l = [input() for _ in range(4)]
    print solve(*l)
