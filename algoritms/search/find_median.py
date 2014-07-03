# https://www.hackerrank.com/challenges/find-median


def median(l):
    l.sort()
    return l[len(l)/2]

if __name__ == '__main__':
    n = input()
    l = map(int, raw_input().split())
    print median(l)
