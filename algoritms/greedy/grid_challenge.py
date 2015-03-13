# https://www.hackerrank.com/challenges/grid-challenge


def is_valid_colum(g):
    n = len(g[0])
    for j in range(n-1):
        for i in range(n):
            if not g[j][i] <= g[j+1][i]:
                return False
    return True


def solve(g):
    l = [sorted(i) for i in g]
    return is_valid_colum(l)

if __name__ == '__main__':
    t = input()
    for _ in range(t):
        n = input()
        grid = []
        for _ in range(n):
            grid.append(raw_input())
        print "YES" if solve(grid) else "NO"
