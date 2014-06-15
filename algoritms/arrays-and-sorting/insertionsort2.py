# https://www.hackerrank.com/challenges/insertionsort2


def insert_sort(l):
    itr_l = [l[0]]
    for key, val in enumerate(l[1:]):
        itr_l.append(val)
        itr_l.sort()
        yield itr_l + l[key+2:]

if __name__ == "__main__":
    N = input()
    l = map(int, raw_input().split())
    for i in insert_sort(l):
        print ' '.join(map(str, i))
