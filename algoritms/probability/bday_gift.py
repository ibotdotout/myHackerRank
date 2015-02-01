# https://www.hackerrank.com/challenges/bday-gift


def solve(l):
    return sum(l)/2.0


if __name__ == '__main__':
    n = input()
    l = [input() for _ in range(n)]
    print("{0:0.1f}".format(solve(l)))
