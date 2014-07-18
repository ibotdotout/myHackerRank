# https://www.hackerrank.com/contests/projecteuler/challenges/euler004

ans = []


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def generate():
    for i in xrange(999, 100, -1):
        for j in xrange(999, 100, -1):
            n = i*j
            if n < 101101:
                continue
            if is_palindrome(n):
                ans.append(n)


def solve(n):
    import bisect
    if not ans:
        generate()
        ans.sort()
    return ans[bisect.bisect_left(ans, n)-1]

if __name__ == '__main__':
    for i in range(input()):
        n = input()
        print solve(n)
