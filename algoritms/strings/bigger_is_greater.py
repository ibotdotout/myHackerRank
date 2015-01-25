# https://www.hackerrank.com/challenges/bigger-is-greater

import bisect


def solve(w):
    for i in range(len(w)-2, -1, -1):
        if w[i+1] > w[i]:
            tail = w[i+1:][::-1]
            smallest_grater_idx = bisect.bisect_right(tail, w[i])
            rest = tail[:smallest_grater_idx] + w[i] + \
                tail[smallest_grater_idx+1:]
            w = w[:i] + tail[smallest_grater_idx] + "".join(rest)
            break
    return w

if __name__ == '__main__':
    t = input()
    for _ in range(t):
        w = raw_input()
        ans = solve(w)
        print(ans if ans != w else "no answer")
