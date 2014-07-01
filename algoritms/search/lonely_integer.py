# https://www.hackerrank.com/challenges/lonely-integer


def get_lonely(l):
    result = []
    for i in l:
        if l.count(i) == 1:
            result.append(i)
    return result

if __name__ == "__main__":
    n = input()
    l = map(int, raw_input().split())
    print ' '.join(map(str, get_lonely(l)))
