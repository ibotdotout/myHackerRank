# https://www.hackerrank.com/challenges/countingsort3


def count(l):
    result = [l.count(0)]
    for i in range(1, 100):
        result.append(l.count(i) + result[-1])
    return result

if __name__ == '__main__':
    n = input()
    l = []
    for i in range(n):
        x, s = raw_input().split()
        l.append(int(x))
    print ' '.join(map(str, count(l)))
