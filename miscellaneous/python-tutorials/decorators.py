# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators


def mobile(func):
    def inner(numbers):
        return sorted([func(i) for i in numbers])
    return inner


@mobile
def standardize(num):
    return "+91" + ' ' + num[-10:-5] + ' ' + num[-5:]

if __name__ == '__main__':
    numbers = []
    for i in range(input()):
        numbers.append(raw_input())
    print '\n'.join(standardize(numbers))
