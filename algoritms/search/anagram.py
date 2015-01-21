# https://www.hackerrank.com/challenges/anagram


def solve(w):
    l = len(w)
    a, b = w[:l/2], w[l/2:]
    return \
        -1 if l % 2 else sum(max(a.count(i) - b.count(i), 0) for i in set(a))


if __name__ == '__main__':
    t = input()
    for _ in range(t):
        w = raw_input()
        print solve(w)
