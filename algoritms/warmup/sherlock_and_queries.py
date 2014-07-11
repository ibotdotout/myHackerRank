# https://www.hackerrank.com/challenges/sherlock-and-queries


def queries(a, b, c):
    a = [0] + a
    mod = (10 ** 9) + 7
    count = [1] * (len(b) + 1)
    for k, v in enumerate(b):
        count[v] = (count[v] * c[k]) % mod
    for k, v in enumerate(count[1:], start=1):
        i = 1
        while i*k < len(a):
            a[i*k] = (a[i*k] * v) % mod
            i += 1
    return a[1:]

if __name__ == '__main__':
    n, m = map(int, raw_input().split())
    a = map(int, raw_input().split())
    b = map(int, raw_input().split())
    c = map(int, raw_input().split())
    print ' '.join(map(str, queries(a, b, c)))
