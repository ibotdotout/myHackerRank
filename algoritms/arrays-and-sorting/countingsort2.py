# https://www.hackerrank.com/challenges/countingsort2

n = input()
l = map(int, raw_input().split())
l.sort()
print ' '.join(map(str, l))
