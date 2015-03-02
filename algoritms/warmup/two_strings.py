# https://www.hackerrank.com/challenges/two-strings


def solve(a, b):
    return bool(set(a) & set(b))


if __name__ == '__main__':
    t = input()
    for _ in range(t):
        a = raw_input()
        b = raw_input()
        print "YES" if solve(a, b) else "NO"
