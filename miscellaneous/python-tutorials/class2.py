# https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle


class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Point(x, y, z)

    def dot(self, other):
        x = self.x * other.x
        y = self.y * other.y
        z = self.z * other.z
        return x + y + z

    def cross(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Point(x, y, z)

    def scale(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** .5


def solve(A, B, C, D):
    import math
    A, B, C, D = Point(*A), Point(*B), Point(*C), Point(*D)
    X = (B - A).cross(C - B)
    Y = (C - B).cross(D - C)
    rad = math.acos(X.dot(Y) / (X.scale() * Y.scale()))
    return math.degrees(rad)


if __name__ == '__main__':
    points = []
    for i in xrange(4):
        a = map(float, raw_input().split())
        points.append(a)
    print "%.2f" % solve(*points)
