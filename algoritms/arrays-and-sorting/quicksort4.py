# https://www.hackerrank.com/challenges/quicksort4


def quick_sort(l):
    count = []
    partition(count, l, 0, len(l))
    return sum(count)


def partition(count, l, m, n):
    if n-m <= 1:
        return l
    pivot = n-1
    pivot_val = l[n-1]
    bigger_idx = []
    swap_count = 0
    for i in range(m, n-1):
        if l[i] < pivot_val:
            swap_count += 1
            if bigger_idx:
                idx, bigger_idx = bigger_idx[0], bigger_idx[1:]
                l[i], l[idx] = l[idx], l[i]
        elif l[i] > pivot_val:
            pivot -= 1
            bigger_idx.append(i)
    l[pivot], l[n-1] = l[n-1], l[pivot]
    l = partition(count, l, m, pivot)
    l = partition(count, l, pivot + 1, n)
    count.append(swap_count + 1)
    return l


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
