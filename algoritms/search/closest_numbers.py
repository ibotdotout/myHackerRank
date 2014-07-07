# https://www.hackerrank.com/challenges/closest-numbers


def closest(l):
    l.sort()
    diff = [(b-a, a, b) for a, b in zip(l, l[1:])]
    diff.sort(key=lambda x: x[0])
    result = []
    min_diff = diff[0][0]
    for d, a, b in diff:
        if d > min_diff:
            break
        else:
            result.append(a)
            result.append(b)
    return result

if __name__ == '__main__':
    n = input()
    l = map(int, raw_input().split())
    print ' '.join(map(str, closest(l)))
