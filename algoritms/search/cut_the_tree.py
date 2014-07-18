# https://www.hackerrank.com/challenges/cut-the-tree


def gen_t(v, edge):
    from collections import defaultdict
    t = defaultdict(set)
    for a, b in edge:
        t[a].add(b)
        t[b].add(a)
    return t


def dfs(t, v, root):
    """ deapth first search with stack avoid recursive limit """
    w = [0] * len(v)
    visited, visit_stack, val_stack = set(), [root], []
    while visit_stack:
        curr = visit_stack.pop()
        if curr not in visited:
            visited.add(curr)
            left_childs = t[curr] - visited  # node not visited
            if not left_childs:  # is leaf node
                w[curr-1] = v[curr-1]
            else:
                val_stack.append(curr)
            visit_stack.extend(left_childs)
    for curr in reversed(val_stack):  # cal weight of parent
        w[curr-1] = v[curr-1] + sum([w[i-1] for i in t[curr]])
    return w


def minimun_tree_diff(v, edge):
    t = gen_t(v, edge)
    w = dfs(t, v, 1)
    total = sum(v)
    return min([abs(total - val * 2) for val in w])

if __name__ == '__main__':
    n = input()
    v = map(int, raw_input().split())
    edge = [map(int, raw_input().split()) for i in range(n-1)]
    print minimun_tree_diff(v, edge)
