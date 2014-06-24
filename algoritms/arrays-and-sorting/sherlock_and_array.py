# https://www.hackerrank.com/challenges/sherlock-and-array


def sherlock_array(l):
    sum_left = 0
    sum_right = sum(l)
    for i in range(0, len(l)):
        sum_right -= l[i]
        if sum_left == sum_right:
            return True
        sum_left += l[i]
    return False

if __name__ == '__main__':
    t = input()
    for i in range(t):
        n = input()
        l = map(int, raw_input().split())
        print('YES' if sherlock_array(l) else 'NO')
