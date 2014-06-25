# https://www.hackerrank.com/challenges/countingsort4


def get_string_order(l):
    half = len(l)/2
    for i in range(half):
        a, b = l[i]
        l[i] = (a, '-')
    l.sort(key=lambda item: item[0])
    result = ""
    for k, v in l:
        result += ' '+v
    return result.strip()

if __name__ == '__main__':
    n = input()
    l = list()
    for i in range(n):
        k, v = raw_input().split()
        l.append((int(k), v))
    print get_string_order(l)
