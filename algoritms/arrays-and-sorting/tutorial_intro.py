# https://www.hackerrank.com/challenges/tutorial-intro


def get_index(l, n):
    return l.index(n)

if __name__ == "__main__":
    n = input()
    x = input()
    print get_index(map(int, raw_input().split()), n)
