# https://www.hackerrank.com/challenges/triplets


class BinaryIndexedTree(object):
    def __init__(self, max_value):
        self.max_value = max_value
        self.arr = [0] * max_value

    def get(self, x):
        return self.query(x) - self.query(x - 1)

    def set(self, x, v):
        curr = self.get(x)
        self.update(x, v - curr)

    def update(self, x, v):
        while x <= self.max_value:
            self.arr[x] += v
            x += x & (-x)

    def query(self, x):
        val = 0
        while x > 0:
            val += self.arr[x]
            x -= x & (-x)
        return val


def count_triples(l):
    a, b, c = [BinaryIndexedTree(len(l) + 4) for i in xrange(3)]
    m = {}
    for idx, val in enumerate(sorted(set(l)), start=1):
        m[val] = idx
    for val in l:
        h = m[val]
        a.set(h, 1)
        b.set(h, a.query(h - 1))
        c.set(h, b.query(h - 1))
    return c.query(c.max_value - 1)


if __name__ == '__main__':
    n = input()
    l = map(int, raw_input().split())
    print count_triples(l)
