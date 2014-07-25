# https://www.hackerrank.com/challenges/play-game


def play(stack):
    stack.reverse()
    dp = [0] * len(stack)
    dp[:3] = stack[0], sum(stack[:2]), sum(stack[:3])
    pre = [stack[0]]
    for val in stack[1:]:
        pre.append(val + pre[-1])
    for i in xrange(3, len(stack)):
        dp[i] = pre[i-1] - dp[i-1] + stack[i]
        dp[i] = max(dp[i], pre[i-2] - dp[i-2] + sum(stack[i:i-2:-1]))
        dp[i] = max(dp[i], pre[i-3] - dp[i-3] + sum(stack[i:i-3:-1]))
    return dp[-1]

if __name__ == '__main__':
    t = input()
    for i in xrange(t):
        n = input()
        l = map(int, raw_input().split())
        print play(l)
