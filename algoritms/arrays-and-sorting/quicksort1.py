# https://www.hackerrank.com/challenges/quicksort1


def quick_sort1(l):
    p_idx = 0
    result = [l[p_idx]]
    for i in range(1, len(l)):
        p = result[p_idx]
        v = l[i]
        if v > p:
            result.append(v)
        else:
            result.insert(p_idx, v)
            p_idx += 1
    return result

if __name__ == "__main__":
    n = input()
    l = map(int, raw_input().split())
    print ' '.join(map(str, quick_sort1(l)))
