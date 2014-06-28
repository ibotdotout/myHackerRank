# https://www.hackerrank.com/challenges/insertion-sort
# Using Count Inversions Algorithm
# http://www.geeksforgeeks.org/counting-inversions/


def merge_sort(l):
    tmp = l[:]
    return _merge_sort(l, tmp, 0, len(l) - 1)


def _merge_sort(l, tmp, left, right):
    inv_count = 0
    if right > left:
        mid = (right + left) / 2

        inv_count = _merge_sort(l, tmp, left, mid)
        inv_count += _merge_sort(l, tmp, mid + 1, right)

        inv_count += merge(l, tmp, left, mid + 1, right)

    return inv_count


def merge(l, tmp, left, mid, right):
    inv_count = 0

    i = left
    j = mid
    k = left

    while (i <= mid - 1) and (j <= right):
        if l[i] <= l[j]:
            tmp[k] = l[i]
            i += 1
        else:
            tmp[k] = l[j]
            j += 1
            inv_count += mid - i
        k += 1

    n = mid - i
    tmp[k:k+n] = l[i:mid]

    end = right + 1
    tmp[k+n:end] = l[j:end]
    l[left:end] = tmp[left:end]

    return inv_count


def shifted_number(l):
    return merge_sort(l)


if __name__ == "__main__":
    t = input()
    for i in range(t):
        n = input()
        l = map(int, raw_input().split())
        print shifted_number(l)
