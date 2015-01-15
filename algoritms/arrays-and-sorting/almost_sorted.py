# https://www.hackerrank.com/challenges/almost-sorted


def solve(l):
    sl = sorted(l)
    if l == sl:
        return True  # boolean - sorted
    indexs = []
    for i in range(len(l)):
        if l[i] != sl[i]:
            indexs.append(i+1)
    if len(indexs) == 2:
        return indexs  # list - swap
    elif indexs:
        a, b = indexs[0], indexs[-1]
        subl = l[a-1:b]
        if subl[::-1] == sl[a-1:b]:
            return a, b  # turple - reverse

if __name__ == '__main__':
    n = input()
    l = [int(i) for i in raw_input().split()]
    res = solve(l)
    if res:
        print "yes"
        if type(res) is not bool:
            if type(res) is list:
                print "swap",
            elif type(res) is tuple:
                print "reverse",
            print " ".join(map(str, res))
    else:
        print "no"
