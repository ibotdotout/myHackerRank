# https://www.hackerrank.com/challenges/quicksort2


def quick_sort2(l):
    m, n = 0, len(l)
    ans = []
    l = qsort(ans, l, m, n)
    return ans


def qsort(ans, l, m, n):
    if n - m <= 1:
        return l
    smaller = [i for i in l[m+1:n] if i < l[m]]
    bigger = [i for i in l[m+1:n] if i >= l[m]]
    l[m:n] = smaller + [l[m]] + bigger
    p_idx = m + len(smaller)
    l = qsort(ans, l, m, p_idx)
    l = qsort(ans, l, p_idx+1, n)
    ans.append(l[m:n])
    return l

if __name__ == "__main__":
    n = input()
    l = map(int, raw_input().split())
    for i in quick_sort2(l):
        print ' '.join(map(str, i))
