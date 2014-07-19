# https://www.hackerrank.com/challenges/median


def running_median(orders):
    def append(l, v):
        import bisect
        idx = bisect.bisect_left(l, v)
        l.insert(idx, v)
        return True

    def remove(l, v):
        if v in l:
            l.remove(v)
            return bool(l)

    def reduce_decimal_floating(v):
        if abs(v - int(v)) <= 0:
            v = int(v)
        return v

    l = []
    cmd = {'r': lambda x: remove(l, x),
           'a': lambda x: append(l, x)}

    for c, v in orders:
        if not cmd[c](v):
            yield "Wrong!"
        else:
            n = len(l)
            if n % 2 == 1:  # is odd
                yield l[n/2]
            else:  # is even
                yield reduce_decimal_floating(sum(l[n/2 - 1: n/2 + 1])/2.0)

if __name__ == '__main__':
    cmd = lambda x: (x[0], int(x[1]))
    orders = [cmd(raw_input().split()) for i in xrange(input())]
    result = running_median(orders)
    for res in result:
        print str(res)
