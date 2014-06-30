# https://www.hackerrank.com/challenges/almost-sorted-interval

# Solution From
# https://www.hackerrank.com/challenges/almost-sorted-interval/editorial

# Not Completed
# got 60/100 fail with time out but in c/c++ this algorithm can sovle very fast
# try in python 3 got 60/100 but slower than python 2
# try to use dynamic stack but static stack is better

# Good Python alogritm with intervals 60/100
# https://www.hackerrank.com/rest/contests/master/challenges/almost-sorted-interval/hackers/leepenkman/download_solution
# https://www.hackerrank.com/rest/contests/master/challenges/almost-sorted-interval/hackers/euclidian/download_solution

arr = []  # global Binary Indexed Tree


def low_bit(x):
    return x & (-x)


def add(x, v, n):
    global arr
    while x <= n:
        arr[x] += v
        x += low_bit(x)


def get(x):
    global arr
    v = 0
    while x > 0:
        v += arr[x]
        x -= low_bit(x)
    return v


def permute(l):
    l = l[:1] + l[:]
    n = len(l)
    left = [0] * n
    right = [n] * n
    stack = [0] * n
    global arr
    arr = [0] * (n+12)
    r = [[] for _ in xrange(n)]  # create 2d list with deep copy

    # after testcase 6 find left[],right[] take a round 3s
    top = 0
    for i in xrange(1, n):
        while top > 0 and l[i] > l[stack[top-1]]:
            top -= 1
        left[i] = (stack[top-1] if top else 0)
        stack[top] = i
        top += 1

    top = 0
    for i in xrange(n-1, 0, -1):
        while top > 0 and l[i] < l[stack[top-1]]:
            top -= 1
        right[i] = (stack[top-1] if top else n)
        stack[top] = i
        top += 1

    # big neck bottle
    ans = 0
    for i in xrange(n-1, 0, -1):
        for j in r[i]:
            add(j, -1, n+12)
        add(i, 1, n+12)
        r[left[i]].append(i)
        ans += get(right[i] - 1)
    return ans

if __name__ == '__main__':
    import sys
    n = sys.stdin.readline().split()
    l = map(int, sys.stdin.readline().split())
    print permute(l)
