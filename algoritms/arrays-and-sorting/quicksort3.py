# https://www.hackerrank.com/challenges/quicksort3


def quick_sort3(l):
    m, n = 0, len(l)
    ans = []
    l = qsort(ans, l, m, n)
    return ans


def qsort(ans, l, m, n):
    if n - m <= 1:
        return l
    last = len(l[m:n-1])
    idx = m
    pivot = l[n-1]
    while idx < m + last:
        if l[idx] >= pivot:
            curr = idx
            fwd = idx + 1
            while l[fwd] >= pivot and fwd < m + last:
                fwd += 1
            if fwd != n-1:
                l[curr], l[fwd] = l[fwd], l[curr]
        idx += 1
    correct_idx = m + len([i for i in l[m:n-1] if i < pivot])
    l[correct_idx], l[n-1] = l[n-1], l[correct_idx]
    ans.append([i for i in l])
    p_idx = correct_idx
    l = qsort(ans, l, m, p_idx)
    l = qsort(ans, l, p_idx+1, n)
    return l

if __name__ == "__main__":
    n = input()
    l = map(int, raw_input().split())
    for i in quick_sort3(l):
        print ' '.join(map(str, i))
