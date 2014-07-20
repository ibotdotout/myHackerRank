# http://stackoverflow.com/questions/15439233/bitusing-a-binary-indexed-tree
# http://goo-apple.appspot.com/article/e94013d1-467d-4f07-9bcc-5c3f91db22a5

# Problem that BIT can solve - https://www.hackerrank.com/challenges/insertion-sort
# shifted number = index of value - number of less than that value
# solution
# https://www.hackerrank.com/rest/contests/master/challenges/insertion-sort/hackers/super_brent/download_solution


class BinaryIndexedTree():
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
            x += x & -x

    def query(self, x):
        val = 0
        while x > 0:
            val += self.arr[x]
            x -= x & -x
        return val
