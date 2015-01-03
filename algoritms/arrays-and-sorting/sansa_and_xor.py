# https://www.hackerrank.com/challenges/sansa-and-xor
# xor only odds times number, results of even times number will be 0


def solve(l):
    n = len(l)
    ans = 0
    for i, x in enumerate(l):
        if (i+1) * (n-i) % 2 == 1:
            ans ^= x
    return ans


if __name__ == '__main__':
    t = input()
    for _ in range(t):
        _ = input()
        l = [int(i) for i in raw_input().split()]
        print solve(l)
