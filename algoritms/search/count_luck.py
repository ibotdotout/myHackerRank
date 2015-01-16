# https://www.hackerrank.com/challenges/count-luck


def get_start_position(forest):
    start = (0, 0)
    for i, s in enumerate(forest):
        x = s.find('M')
        if x >= 0:
            start = (i, x)
    return start


def move(forest, memo, curr, k):
    def in_range(curr):
        if curr[0] < 0 or curr[0] >= len(forest) \
                or curr[1] < 0 or curr[1] >= len(forest[0]):
            return False
        else:
            return True

    direct = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    if not in_range(curr):
        return -1
    if memo[curr[0]][curr[1]] == 1:
        return -1
    else:
        memo[curr[0]][curr[1]] = 1
        if forest[curr[0]][curr[1]] == '*':
            return k
        elif forest[curr[0]][curr[1]] == 'X':
            return -1
        else:
            w = 0
            prev = curr
            for d in direct:
                curr = (prev[0] + d[0], prev[1] + d[1])
                if in_range(curr):
                    x = forest[curr[0]][curr[1]]
                    if memo[curr[0]][curr[1]] == 0 and \
                            (x == '.' or x == '*'):
                        w += 1
            else:
                if w > 1:
                    k += 1
            res = []
            for d in direct:
                curr = (prev[0] + d[0], prev[1] + d[1])
                res.append(move(forest, memo, curr, k))
            return max(res)


def solve(forest):
    start = get_start_position(forest)
    memo = [[0 for _ in forest[0]] for _ in forest]
    k = move(forest, memo, start, 0)
    return k

if __name__ == '__main__':
    t = input()
    for _ in range(t):
        n, m = map(int, raw_input().split())
        forest = [raw_input() for _ in range(n)]
        k = input()
        if k == solve(forest):
            print "Impressed"
        else:
            print "Oops!"
