# https://www.hackerrank.com/challenges/missing-numbers


def not_in_a(a, b):
    return [i for i in set(a) if a.count(i) < b.count(i)]

if __name__ == '__main__':
    _ = input()
    a = map(int, raw_input().split())
    _ = input()
    b = map(int, raw_input().split())
    print ' '.join(map(str, not_in_a(a, b)))
