# https://www.hackerrank.com/challenges/countingsort1


def count(l):
    return [l.count(i) for i in range(0, 100)]

if __name__ == "__main__":
    n = input()
    l = map(int, raw_input().split())
    print(' '.join(map(str, count(l))))
