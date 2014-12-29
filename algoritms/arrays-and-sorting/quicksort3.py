# https://www.hackerrank.com/challenges/quicksort3


def quick_sort3(l):
    m, n = 0, len(l)
    ans = []
    l = qsort(ans, l, m, n)
    return ans


def qsort(ans, l, m, n):
    if n - m <= 1:
        return l
    pivot, curr = l[n-1], m
    for fwd in range(m, n-1):
        if l[fwd] <= pivot:
            l[curr], l[fwd] = l[fwd], l[curr]
            curr += 1
    l[curr], l[n-1] = l[n-1], l[curr]
    ans.append([i for i in l])
    l = qsort(ans, l, m, curr)
    l = qsort(ans, l, curr+1, n)
    return l

if __name__ == "__main__":
    n = input()
    l = map(int, raw_input().split())
    for i in quick_sort3(l):
        print ' '.join(map(str, i))
