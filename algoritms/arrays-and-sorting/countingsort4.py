# https://www.hackerrank.com/challenges/countingsort4


def get_string_order(l):
    half = len(l)/2
    helper = [[] for i in range(100)]
    for i, (k, v) in enumerate(l):
        if i < half:
            v = '-'
        helper[k].append(v)
    result = sum(helper, [])  # flattened list.
    return ' '.join(result)

if __name__ == '__main__':
    n = input()
    l = list()
    for i in range(n):
        k, v = raw_input().split()
        l.append((int(k), v))
    print get_string_order(l)
