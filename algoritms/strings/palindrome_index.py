# https://www.hackerrank.com/challenges/palindrome-index


def solve(w):
    is_palindrome = lambda w: w == w[::-1]
    remove_i = lambda w, i: w[:i] + w[i+1:]
    if is_palindrome(w):
        return -1
    for i in range(len(w)/2):
        if w[i] != w[-(i+1)]:
            return i if is_palindrome(remove_i(w, i)) else len(w)-(i+1)

if __name__ == '__main__':
    t = input()
    for _ in range(t):
        w = raw_input()
        print solve(w)
