# https://www.hackerrank.com/challenges/nested-list


def second_lowest(std):
    import heapq
    marks = set([i[1] for i in std])
    second_low = heapq.nsmallest(2, marks)[1]
    result = [i[0] for i in std if i[1] == second_low]
    return sorted(result)

if __name__ == '__main__':
    std = []
    n = input()
    for i in xrange(n):
        name = raw_input()
        mark = float(raw_input())
        std.append([name, mark])
    print '\n'.join(second_lowest(std))
