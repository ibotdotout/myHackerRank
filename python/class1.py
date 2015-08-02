# https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers


class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return ComplexNumber(real, imaginary)

    def __sub__(self, other):
        real = self.real - other.real
        imaginary = self.imaginary - other.imaginary
        return ComplexNumber(real, imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real, imaginary)

    def __div__(self, other):
        div = float(other.real ** 2 + other.imaginary ** 2)
        tmp = self * ComplexNumber(other.real, -other.imaginary)
        real = tmp.real / div
        imaginary = tmp.imaginary / div
        return ComplexNumber(real, imaginary)

    def mod(self):
        import math
        real = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        return ComplexNumber(real, 0)

    def __repr__(self):
        if self.imaginary == 0:
            rep = "%.2f" % (self.real)
        elif self.real == 0:
            rep = "%.2fi" % (self.imaginary)
        elif self.imaginary > 0:
            rep = "%.2f + %.2fi" % (self.real, self.imaginary)
        else:
            rep = "%.2f - %.2fi" % (self.real, abs(self.imaginary))
        return rep


def solve(a, b):
    a = ComplexNumber(*a)
    b = ComplexNumber(*b)
    result = [a+b, a-b, a*b, a/b, a.mod(), b.mod()]
    return map(str, result)


if __name__ == '__main__':
    a = map(float, raw_input().split())
    b = map(float, raw_input().split())
    print '\n'.join(solve(a, b))
