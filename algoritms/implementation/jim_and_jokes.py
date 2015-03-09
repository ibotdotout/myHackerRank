# https://www.hackerrank.com/challenges/jim-and-the-jokes


def base_n(x, b):
    try:
        return int(str(x), b)
    except:
        return None


def solve(l):
    cnt = {}
    jokes = 0
    for i in range(0, len(l), 2):
        x, b = l[i], l[i+1]
        v = base_n(b, x)
        if v:
            cnt[v] = cnt.get(v, 0) + 1
    for i, v in cnt.items():
        jokes += v*(v-1)//2 if v > 0 else 0
    return jokes


if __name__ == '__main__':
    n = input()
    l = []
    for i in range(n):
        l += map(int, raw_input().split())
    print solve(l)
