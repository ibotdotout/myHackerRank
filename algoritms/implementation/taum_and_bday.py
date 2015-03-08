# https://www.hackerrank.com/challenges/taum-and-bday


def solve(a, b):
    x, y, z = b
    b, w = a

    return b * min(x, y + z) + w * min(y, x + z)

if __name__ == '__main__':

    t = input()
    for _ in range(t):
        a = map(int, raw_input().split())
        b = map(int, raw_input().split())
        print solve(a, b)
