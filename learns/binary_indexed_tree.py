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

    def low_bit(self, num):
        return num & (-num)

    def add(self, x):
        while x <= self.max_value:
            self.arr[x] += 1
            x += self.low_bit(x)

    def get(self, x):
        val = 0
        while x > 0:
            val += self.arr[x]
            x -= self.low_bit(x)
        return val
