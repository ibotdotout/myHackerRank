# https://www.hackerrank.com/challenges/cavity-map


def solve(m):
    result = m[:]
    direct = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    n = len(m)
    for i in range(1, n-1):
        for j in range(1, n-1):
            if all(map(lambda x: m[i][j] > m[i+x[0]][j+x[1]], direct)):
                result[i][j] = 'X'
    return result

if __name__ == '__main__':
    n = input()
    m = [map(int, raw_input()) for _ in range(n)]
    for i in solve(m):
        print "".join(map(str, i))
