# https://www.hackerrank.com/challenges/even-tree


def count_node(v_list, m, n):
    count = [1 for i in range(m)]

    for child, parent in reversed(v_list):
        count[parent-1] += count[child-1]

    return count


def even_tree(v_list, m, n):
    count = count_node(v_list, m, n)

    cut_count = -1
    for i in count:
        if i % 2 == 0:
            cut_count += 1

    return cut_count


if __name__ == "__main__":
    m, n = [int(i) for i in raw_input().split()]
    v_list = []
    for i in range(n):
        v_list.append((int(i) for i in raw_input().split()))
    print(even_tree(v_list, m, n))
