# https://www.hackerrank.com/challenges/game-of-thrones


def solve(w):
    odd = 0
    s = set(w)
    for i in s:
        if w.count(i) % 2 != 0:
            odd += 1
        if odd >= 2:
            return False
    return True


if __name__ == '__main__':
    w = raw_input()
    print ('YES' if solve(w) else 'NO')
