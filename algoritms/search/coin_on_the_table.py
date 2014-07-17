# https://www.hackerrank.com/challenges/coin-on-the-table

# solution:
# http://fenghaolw.blogspot.com/2014/01/coin-on-table.html

# DP solution:
# https://www.hackerrank.com/rest/contests/master/challenges/coin-on-the-table/hackers/aruff/download_solution


def dfs(table, count, row, col, step, k, changes):
    cmd = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    if row >= 0 and row < len(table) and \
       col >= 0 and col < len(table[0]) and \
       changes < count[row][col]:

        if step < k:
            count[row][col] = changes
            for order, (my, mx) in cmd.items():
                move = (0 if table[row][col] == order else 1)
                dfs(table, count, row + my, col + mx, step + 1, k,
                    changes + move)

        else:
            if table[row][col] == '*':
                count[row][col] = changes


def operation_require(table, k):
    result = -1
    m = len(table[0])
    idx = ''.join(table).index('*')
    star = (idx / m, idx % m)
    if sum(star) <= k:
        max_k = 1001
        count = [[max_k for i in xrange(m)] for j in xrange(len(table))]
        dfs(table, count, 0, 0, 0, k, 0)
        result = count[star[0]][star[1]]
    return result

if __name__ == '__main__':
    n, m, k = map(int, raw_input().split())
    table = [raw_input() for i in xrange(n)]
    print operation_require(table, k)
