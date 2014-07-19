# https://www.hackerrank.com/challenges/median


def running_median(orders):
    """ insert v in sorted list """
    def append(l, v):
        import bisect
        bisect.insort(l, v)
        return True

    def remove(l, v):
        """ binary search then pop() is faster than if v in l than remove() """
        import bisect
        idx = bisect.bisect_left(l, v)
        if idx < len(l) and l[idx] == v:
            l.pop(idx)
            return bool(l)

    l = []
    cmd = {'r': remove, 'a': append}

    for c, v in orders:
        if not cmd[c](l, v):
            yield "Wrong!"
        else:
            n = len(l)
            midle = n/2
            if n % 2 == 1:  # is odd
                yield l[midle]
            else:  # is even
                median = sum(l[midle - 1: midle + 1])/2.0
                yield int(median) if median.is_integer() else median

if __name__ == '__main__':
    cmd = lambda x: (x[0], int(x[1]))
    orders = [cmd(raw_input().split()) for i in xrange(input())]
    result = running_median(orders)
    for res in result:
        print str(res)
