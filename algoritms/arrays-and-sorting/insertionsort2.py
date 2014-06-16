# https://www.hackerrank.com/challenges/insertionsort2


def insert_sort(l):
    for i in range(1, len(l)):
        val = l[i]
        k = i - 1
        while k >= 0 and l[k] > val:
            l[k+1] = l[k]
            k -= 1
        l[k+1] = val
        #  if yield l that will return reference of l insted of l's data
        yield l[:]

if __name__ == "__main__":
    N = input()
    l = map(int, raw_input().split())
    for i in insert_sort(l):
        print ' '.join(map(str, i))
