# https://www.hackerrank.com/challenges/play-game


def play(stack):
    stack.reverse()
    dp = [0] * len(stack)
    dp[:3] = stack[0], sum(stack[:2]), sum(stack[:3])
    total = sum(stack[:3])
    for i in xrange(3, len(stack)):
        total += stack[i]
        dp[i] = total - min(dp[i-1], dp[i-2], dp[i-3])
    return dp[-1]

if __name__ == '__main__':
    t = input()
    for i in xrange(t):
        n = input()
        l = map(int, raw_input().split())
        print play(l)
