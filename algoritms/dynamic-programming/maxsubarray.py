# https://www.hackerrank.com/challenges/maxsubarray


def solve(l):
    non_con_l = [i for i in l if i > 0]
    non_con = sum(non_con_l) if non_con_l else max(l)
    max_con, min_con, p = l[0], 0, 0
    for v in l:
            p += v
            max_con = max(p - min_con, max_con)
            min_con = min(p, min_con)
    return max_con, non_con

if __name__ == '__main__':
    t = input()
    for _ in range(t):
        _ = input()
        l = map(int, raw_input().split())
        print " ".join(map(str, solve(l)))
