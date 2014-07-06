# https://www.hackerrank.com/challenges/find-a-string


def get_index_sub_string(string, sub_string):
    count = 0
    while sub_string in string:
        count += 1
        string = string[string.index(sub_string)+1:]
    return count


if __name__ == '__main__':
    string = raw_input()
    sub = raw_input()
    print get_index_sub_string(string, sub)
