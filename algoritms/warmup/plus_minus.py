# https://www.hackerrank.com/challenges/plus-minus


def solve(l):
    n = float(len(l))
    pos = len([i for i in l if i > 0])
    neg = len([i for i in l if i < 0])
    return (pos/n, neg/n,  (n-pos-neg)/n)


if __name__ == '__main__':
    _ = int(input())
    l = [int(i) for i in raw_input().split()]
    print("\n".join(map(str, solve(l))))
