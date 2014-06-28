# https://www.hackerrank.com/challenges/insertion-sort


def shifted_number(l):
    import bisect
    sorted_list = []
    n = 0
    for i in l:
        idx = bisect.bisect_right(sorted_list, i)
        sorted_list.insert(idx, i)
        n += len(sorted_list) - idx - 1
    return n

if __name__ == "__main__":
    t = input()
    for i in range(t):
        n = input()
        l = map(int, raw_input().split())
        print shifted_number(l)
