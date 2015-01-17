# https://www.hackerrank.com/challenges/the-grid-search


def solve(grid, pattern):
    for i in range(len(grid)):
        for idx in range(len(pattern)):
            x = grid[i+idx].find(pattern[idx])
            if x < 0:
                break
        else:
            return True
    return False

if __name__ == '__main__':
    t = input()
    for _ in range(t):
        n, m = map(int, raw_input().split())
        grid = [raw_input() for _ in range(n)]
        n, m = map(int, raw_input().split())
        pattern = [raw_input() for _ in range(n)]
        print "YES" if solve(grid, pattern) else "NO"
