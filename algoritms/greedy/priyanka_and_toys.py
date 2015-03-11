# https://www.hackerrank.com/challenges/priyanka-and-toys


def solve(l):
    l = sorted(set(l))
    curr_w = l[0]
    count = 1
    for w in l:
        if w > curr_w + 4:
            curr_w = w
            count += 1
    return count

if __name__ == '__main__':
    _ = input()
    l = map(int, raw_input().split())
    print solve(l)
