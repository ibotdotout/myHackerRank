# https://www.hackerrank.com/challenges/cut-the-sticks


def solve(l):
    res = []
    l = sorted(l)
    while l:
        res.append(len(l))
        l = [i-l[0] for i in l if i-l[0] > 0]
    return res


if __name__ == '__main__':
    _ = input()
    l = [int(i) for i in raw_input().split()]
    print "\n".join(map(str, solve(l)))
