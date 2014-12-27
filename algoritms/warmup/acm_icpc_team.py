# https://www.hackerrank.com/challenges/acm-icpc-team
from itertools import combinations


def solve(l):
    max_count, team_count = 0, 0
    merged = [bin(int(a, 2) | int(b, 2)) for a, b in combinations(l, 2)]
    for i in merged:
        count = i.count('1')
        if count > max_count:
            max_count, team_count = count, 1
        elif count == max_count:
            team_count += 1
    return [max_count, team_count]

if __name__ == '__main__':
    n, w = [int(i) for i in raw_input().split()]
    l = [raw_input() for _ in range(n)]
    print "\n".join([str(i) for i in solve(l)])
