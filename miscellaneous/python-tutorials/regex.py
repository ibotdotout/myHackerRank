# https://www.hackerrank.com/challenges/regex-1-validating-the-phone-number


def is_phone_number(number):
    import re
    match = re.search("^[7-9]\d{9}$", str(number))
    return True if match else False

if __name__ == '__main__':
    t = input()
    for i in xrange(t):
        print 'YES' if is_phone_number(raw_input()) else 'NO'
