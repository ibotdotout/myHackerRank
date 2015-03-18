# https://www.hackerrank.com/challenges/number-list


def solve(l, k):
    n = len(l)
    result = 0
    for w in range(n):
        life_time, m = 0, 0
        for j in range(w, n):
            if life_time > 0:
                if l[j] > m:
                    life_time = w
                    m = l[j]
            else:
                ll = l[j-w:j+1]
                m = max(ll)
                life_time = ll.index(m)
            if m > k:
                result += 1
            life_time -= 1
    return result


if __name__ == '__main__':
    t = input()
    for _ in range(t):
        _, k = map(int, raw_input().split())
        l = map(int, raw_input().split())
        print solve(l, k)
