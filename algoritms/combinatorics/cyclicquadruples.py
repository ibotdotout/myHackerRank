# https://www.hackerrank.com/challenges/cyclicquadruples
# guild solution
# http://hr-filepicker.s3.amazonaws.com/infinitum-may14/477-cyclicquadruples.pdf

# solution explain
# https://sillymesillythoughtssillystuff.wordpress.com/tag/hackerrank/

# solution code example
# https://github.com/algorhythms/HackerRankAlgorithms/blob/master/Cyclic%20Quadruples.py


def solve(seq):
    mod = 10 ** 9 + 7
    fiexed_range = lambda l, r: max(0, min(r) - max(l) + 1)
    normal_range = lambda l, r: r-l+1

    l = [seq[i*2] for i in range(4)]
    r = [seq[i*2+1] for i in range(4)]

    w0 = 1
    for v in map(normal_range, l, r):
        w0 *= v
    w0 %= mod

    l = l + l
    r = r + r

    w1 = 0
    for i in range(4):
        w1 += fiexed_range(l[i:i+2], r[i: i+2]) * normal_range(l[i+2], r[i+2]) \
            * normal_range(l[i+3], r[i+3])
    w1 %= mod

    w2 = 0
    for i in range(4):
        w2 += fiexed_range(l[i:i+3], r[i: i+3]) * normal_range(l[i+3], r[i+3])
    w2 %= mod

    for i in range(2):
        w2 += fiexed_range(l[i:i+2], r[i: i+2]) \
            * fiexed_range(l[i+2:i+4], r[i+2:i+4])
    w2 %= mod

    w3 = 0
    for i in range(4):
        w3 += fiexed_range(l[i:i+4], r[i: i+4])
    w3 %= mod

    w4 = fiexed_range(l[:4], r[:4])
    w4 %= mod

    return (w0-w1+w2-w3+w4) % mod


if __name__ == '__main__':
    t = input()
    for _ in range(t):
        seq = map(int, raw_input().split())
        print solve(seq)
