# https://www.hackerrank.com/challenges/find-point


def symmetric_point(pq):
    px, py, qx, qy = pq
    sx = 2 * qx - px
    sy = 2 * qy - py
    return [sx, sy]

if __name__ == '__main__':
    t = input()
    for i in range(t):
        pq = map(int, raw_input().split())
        print ' '.join(map(str, symmetric_point(pq)))
