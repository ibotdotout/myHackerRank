# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list


def second_max(l):
    import heapq
    return heapq.nlargest(2, set(l))[1]

if __name__ == '__main__':
    n = input()
    l = map(int, raw_input().split())
    print second_max(l)
