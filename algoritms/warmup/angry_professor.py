# https://www.hackerrank.com/challenges/angry-professor


def solve(l, k):
    return len([i for i in l if i <= 0]) < k

if __name__ == '__main__':
    t = input()
    for _ in range(t):
        _, k = map(int, raw_input().split())
        l = map(int, raw_input().split())
        print 'YES' if solve(l, k) else 'NO'
