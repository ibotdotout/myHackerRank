# https://www.hackerrank.com/challenges/insertionsort1


def insert_sort(l):
    display_list = l[:]  # copy l to display_list without ref
    for i in range(len(l) - 1, 0, -1):
        if l[i-1] > l[i]:
            display_list[i] = display_list[i-1]
            l[i], l[i-1] = l[i-1], l[i]
            yield display_list
            display_list = l[:]
    yield l

if __name__ == "__main__":
    N = input()
    l = map(int, raw_input().split())
    for i in insert_sort(l):
        print ' '.join(map(str, i))
