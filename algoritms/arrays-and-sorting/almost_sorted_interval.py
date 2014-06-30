# https://www.hackerrank.com/challenges/almost-sorted-interval

# Solution From
# https://www.hackerrank.com/challenges/almost-sorted-interval/editorial

# complete 100/100
# after optimization by remove overhead of function calling
# using sys.stdin.readline() instead of input(), raw_input()
# remove duplicate compute


def permute(l):
    l = l[:1] + l[:]
    n = len(l)
    nn = n + 12
    left = [0] * n
    right = [n] * n
    stack = left[:]
    arr = [0] * (nn)
    r = [[] for _ in xrange(n)]  # create 2d list with deep copy

    # after testcase 6 find left[],right[] take a round 3s
    top = 0
    for i in xrange(1, n):
        val = l[i]
        while top > 0 and val > l[stack[top-1]]:
            top -= 1
        if top:
            left[i] = stack[top-1]
        stack[top] = i
        top += 1

    top = 0
    for i in xrange(n-1, 0, -1):
        val = l[i]
        while top > 0 and val < l[stack[top-1]]:
            top -= 1
        if top:
            right[i] = stack[top-1]
        stack[top] = i
        top += 1

    # big neck bottle
    ans = 0
    for i in xrange(n-1, 0, -1):
        for j in r[i]:
            while j <= nn:
                arr[j] += -1
                j += (j & (-j))
        j = i
        while j <= nn:
            arr[j] += 1
            j += (j & (-j))
        r[left[i]].append(i)
        v = 0
        x = right[i] - 1
        while x > 0:
            v += arr[x]
            x -= (x & (-x))
        ans += v
    return ans

if __name__ == '__main__':
    import sys
    n = sys.stdin.readline().split()
    l = map(int, sys.stdin.readline().split())
    print permute(l)
