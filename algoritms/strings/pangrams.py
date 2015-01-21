# https://www.hackerrank.com/challenges/pangrams


def solve(w):
    return len({c for c in w.lower() if c.isalpha()}) == 26


if __name__ == '__main__':
    w = raw_input()
    print "pangram" if solve(w) else "not pangram"
