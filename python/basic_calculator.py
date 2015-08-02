# https://www.hackerrank.com/challenges/basic-calculator


def cal(a, b):
    results = [a+b, a-b, a*b, a/b, a//b]
    return ["{0:.2f}".format(i) for i in results]


if __name__ == '__main__':
    a = float(input())
    b = float(input())
    print '\n'.join(cal(a, b))
