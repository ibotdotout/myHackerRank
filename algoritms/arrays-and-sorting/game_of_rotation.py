# https://www.hackerrank.com/challenges/game-of-rotation


def get_PMEAN(l):
    pmean = sum([(k + 1) * v for k, v in enumerate(l)])
    result = pmean
    total = sum(l)
    n = len(l)
    for i in l[:-1]:
        pmean -= total - i * n
        result = max(result, pmean)
    return result

if __name__ == '__main__':
    n = input()
    l = map(int, raw_input().split())
    print get_PMEAN(l)
