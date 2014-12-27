# https://www.hackerrank.com/challenges/acm-icpc-team


def merge(a, b):
    return "".join([x if x == '1' else y for x, y in zip(a, b)])


def solve(l):
    merged = []
    max_count, team_count = 0, 0
    for i in range(len(l)):
        for j in range(i+1, len(l)):
                x = merge(l[i], l[j])
                count = x.count('1')
                max_count = count if count > max_count else max_count
                merged.append(x)
    team_count = len([i for i in merged if i.count('1') == max_count])
    return [max_count, team_count]

if __name__ == '__main__':
    n, w = [int(i) for i in raw_input().split()]
    l = [raw_input() for _ in range(n)]
    print "\n".join([str(i) for i in solve(l)])
