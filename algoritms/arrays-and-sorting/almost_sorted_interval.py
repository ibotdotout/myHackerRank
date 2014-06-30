# https://www.hackerrank.com/challenges/almost-sorted-interval

# Solution From
# https://www.hackerrank.com/challenges/almost-sorted-interval/editorial

# Not Completed
# got 60/100 fail with time out but in c/c++ this algorithm can sovle very fast
# try to use dynamic stack but static stack is better

# Good Python alogritm with intervals 60/100
# https://www.hackerrank.com/rest/contests/master/challenges/almost-sorted-interval/hackers/leepenkman/download_solution


def low_bit(x):
    return x & (-x)


def add(arr, x, v):
    n = len(arr)
    while x <= n:
        arr[x] += v
        x += low_bit(x)


def get(arr, x):
    v = 0
    while x > 0:
        v += arr[x]
        x -= low_bit(x)
    return v


def permute(l):
    l = l[:1] + l[:]
    n = len(l)
    left = [0] * n
    right = [0] * n
    stack = [0] * n
    bit = [0] * (n+12)
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
            add(bit, j, -1)
        add(bit, i, 1)
        r[left[i]].append(i)

        ans += get(bit, right[i] - 1)
    return ans

if __name__ == '__main__':
    n = input()
    l = map(int, raw_input().split())
    print permute(l)
