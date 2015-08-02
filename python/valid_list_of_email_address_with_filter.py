# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter


def filter_email(emails):
    import re
    pattern = '^[\w\d\-]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$'
    result = [i for i in emails if re.search(pattern, i)]
    return sorted(result)


if __name__ == '__main__':
    n = input()
    emails = [raw_input() for i in xrange(n)]
    print "[" + ', '.join(map(lambda x: "'" + str(x) + "'",
                              filter_email(emails))) + "]"
