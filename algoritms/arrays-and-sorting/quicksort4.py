# https://www.hackerrank.com/challenges/quicksort4


def quick_sort(l):
    return partition(l, 0, len(l))


def partition(l, m, n):
    if n-m <= 1:
        return 0
    p = m
    pivot_val = l[n-1]
    swap_count = 1
    for i in range(m, n-1):
        if l[i] < pivot_val:
            l[p], l[i] = l[i], l[p]
            swap_count += 1
            p += 1
    l[p], l[n-1] = l[n-1], l[p]
    swap_count += partition(l, m, p)
    swap_count += partition(l, p + 1, n)
    return swap_count


def insert_sort(l):
    count = 0
    for i in range(1, len(l)):
        val = l[i]
        k = i-1
        while l[k] > val and k >= 0:
            l[k+1] = l[k]
            k -= 1
            count += 1
        l[k+1] = val
    return count

if __name__ == "__main__":
    n = input()
    l = map(int, raw_input().split())
    print insert_sort(l[:]) - quick_sort(l[:])
