# https://www.hackerrank.com/challenges/count-luck
# inspire by Astaroth@hrank.io to use bfs


def get_start_and_exit_position(forest):
    for i, s in enumerate(forest):
        for j, c in enumerate(s):
            if c == 'M':
                start = (i, j)
            elif c == '*':
                exit = (i, j)
    return start, exit


def bfs(forest, start, exit):
    def get_next_pos(curr):
        in_range = lambda curr: False if curr[0] < 0 or curr[0] >= len(forest) \
            or curr[1] < 0 or curr[1] >= len(forest[0]) else True

        pos = []
        for d in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            next_pos = (curr[0] + d[0], curr[1] + d[1])
            if in_range(next_pos) and forest[next_pos[0]][next_pos[1]] != 'X' \
                    and next_pos not in visited:
                pos.append(next_pos)
        return pos

    visited = {}
    queue = [(start, 0)]

    while queue:
        curr, k = queue.pop(0)
        if curr in visited:
            continue
        else:
            visited[curr] = 1
            if curr == exit:
                return k
            next_pos = get_next_pos(curr)
            if len(next_pos) > 1:
                k += 1
            for pos in next_pos:
                queue.append((pos, k))
    return None


def solve(forest):
    start, exit = get_start_and_exit_position(forest)
    return bfs(forest, start, exit)

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
