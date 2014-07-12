# https://www.hackerrank.com/challenges/find-digits


def solve(n):
    return len([i for i in str(n) if i != '0' and n % int(i) == 0])

if __name__ == '__main__':
    t = input()
    for i in range(t):
        n = input()
        print solve(n)
