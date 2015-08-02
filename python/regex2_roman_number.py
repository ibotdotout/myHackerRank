# https://www.hackerrank.com/challenges/regex-2-validate-a-roman-number


def valid_roman_number(num):
    import re
    result = True
    pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    match = re.search(pattern, num)
    if not match:
        result = False
    return result

if __name__ == '__main__':
    num = raw_input()
    print valid_roman_number(num)
