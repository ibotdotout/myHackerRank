# https://www.hackerrank.com/challenges/sherlock-and-anagrams


def solve(w):
    n = len(w)
    count = dict()
    for i in range(n):
        for j in range(i, n):
            ss = "".join(sorted(w[i:j+1]))
            count[ss] = count.get(ss, 0) + 1
    result = sum((i * (i-1)) / 2 for i in count.values())
    return result


if __name__ == '__main__':
    t = input()
    for _ in range(t):
        w = raw_input()
        print solve(w)
